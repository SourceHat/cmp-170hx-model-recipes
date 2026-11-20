'Decode only occupied lanes and overlap two groups across the P2P ranks.'

import os

from concurrent.futures import Future

from concurrent.futures import ThreadPoolExecutor

from concurrent.futures import wait

from contextlib import nullcontext

from dataclasses import dataclass

from itertools import groupby

import torch

from torch.nn import functional as F

from decoder_prefix_probe import norm

from hy4_cached_index import GROUP_TILE

from hy4_cached_index import pack_tile

from hy4_engram_read_ahead import EngramReadAhead

from hy4_fused_connections import branch

from hy4_fused_connections import write

from hy4_fused_experts import FusedDecodeExperts

from hy4_fused_mla import attention as gathered_attention

from hy4_latency_recall import RATIO

from hy4_latency_recall import mixed_recall_pages

from hy4_latency_recall import recall

from hy4_latency_recall import recall_pages

from hy4_paged_q8_probe import BITS

from hy4_paged_q8_probe import LATENT

from hy4_paged_q8_probe import PAGE

from hy4_paged_q8_probe import ROPE

from hy4_quality_device_step import key_width

from hy4_shared_pool import LANES

from hy4_sliding_runtime import WINDOW

from hy4_standard_expert_pack import PackedExperts

@dataclass(frozen=True)
class Wave:
    physical: torch.Tensor
    positions: torch.Tensor
    starts: tuple
    slots: torch.Tensor
    phases: torch.Tensor
    ids: torch.Tensor
    history: torch.Tensor
    shared: torch.Tensor
    rotary: torch.Tensor
    index_pages: object = None

def append_groups(ix, raw, wave, table):
    lanes, slots = wave.physical, wave.slots
    ix.table = table
    point = slots % ix.indexer.compress_ratio
    ix.first[lanes] = torch.where(point == 0, wave.phases, ix.first[lanes])
    ix.partial[lanes, point] = raw
    size = ix.indexer.compress_ratio
    closing = [i for i, n in enumerate(wave.starts) if n % size == size - 1]
    if closing:
        row = torch.arange(len(wave.starts), device=raw.device)
        slot = (slots // size) % GROUP_TILE
        tile = raw.new_zeros((len(wave.starts), GROUP_TILE, size, raw.shape[-1]))
        phases = wave.phases.new_zeros((len(wave.starts), GROUP_TILE))
        tile[row, slot] = ix.partial[lanes]
        phases[row, slot] = ix.first[lanes]
        bits, scales = pack_tile(ix.indexer, ix.inv, tile, phases)
        use = torch.tensor(closing, device=raw.device)
        groups = slots[use] // size
        pages = wave.shared[use, groups // ix.stride].long()
        ix.bits[pages, groups % ix.stride] = bits[use, slot[use]]
        ix.scales[pages, groups % ix.stride] = scales[use, slot[use]]
    ix.lengths[lanes] = slots + 1

def gathered(a, q, qr, planes, table, picks, projection, sinks):
    valid = picks >= 0
    safe = picks.clamp_min(0).long()
    r = torch.arange(safe.shape[0], device=safe.device)[:, None]
    pages = table[r, safe // PAGE].clamp_min(0).long()
    words, scales, rope = (v[pages, safe % PAGE].flatten(2).masked_fill(~valid[..., None], 0) for v in planes)
    k = words.shape[1]
    x = torch.empty((len(words) * k, LATENT), dtype=torch.float16, device=q.device)
    a.ext.dequant_cache_cont(words.flatten(0, 1).contiguous(), scales.flatten(0, 1).contiguous(), x, 0.)
    local = torch.arange(k, device=q.device).expand_as(picks).masked_fill(~valid, -1)
    return gathered_attention(q, qr, x.view(len(words), k, LATENT).bfloat16(), rope, projection,
                              local[:, None], sinks)

def place_head_rows(logits, lanes):
    """Place packed logits directly into the known request slots."""
    result = logits.new_zeros((LANES, logits.shape[-1]))
    for row, lane in enumerate(lanes):
        result[lane].copy_(logits[row])
    return result

class LatencyDecode:
    def __init__(self, target, *, pipeline=True, paged=True, fused_experts=True, graph_widths=()):
        self.target, self.pipeline = target, pipeline
        self.single = self.four = True
        self.head_lane_slices = False
        self.stages = tuple((device, tuple(blocks))
                            for device, blocks in groupby(target.blocks, key=lambda b: b.device))
        if len({d for d, _ in self.stages}) != len(self.stages):
            raise ValueError("Latency runner requires the contiguous HY4 rank layout")
        self.reuse_recall_pages = os.environ.get("HY4_REUSE_RECALL_PAGES") == "1"
        self.reuse_recall_widths = frozenset()
        self.mixed_recall_min = None
        self.mixed_recall_max = None
        self.mixed_recall_rows = None
        self.fused_recall_widths = frozenset()
        self.fused_recall_limit = None
        self.stage_index = {}
        for d, blocks in self.stages:
            indices = [b.attention.index for b in blocks if b.sparse]
            if indices:
                first = indices[0]
                if all((x.stride, x.indexer.group_topk, x.group_slots.numel()) ==
                       (first.stride, first.indexer.group_topk, first.group_slots.numel()) for x in indices):
                    self.stage_index[d] = first
        self.workers = ThreadPoolExecutor(max_workers=len(self.stages), thread_name_prefix="hy4-rank")
        self.streams = {d: torch.cuda.Stream(device=d) for d, _ in self.stages}
        self.ahead = getattr(target, "engram_read_ahead", None) or EngramReadAhead(target)
        self.dense_graphs = None
        self.grouped = {}
        self.paged = None
        if paged:
            from hy4_paged_attention import attention

            self.paged = attention
        for device, blocks in self.stages:
            with torch.cuda.device(device):
                for block in blocks:
                    if isinstance(block.mlp, PackedExperts):
                        if fused_experts:
                            dispatch = FusedDecodeExperts(block.mlp)
                        else:
                            dispatch = getattr(target, "verified_panel_experts", {})[block.mlp]
                        self.grouped[block.mlp] = dispatch
        if graph_widths:
            self.prepare_graphs(graph_widths)
        self.key = None
        self.tables = {}

    def prepare_graphs(self, widths):
        from hy4_decode_graph import GraphExperts

        for device, blocks in self.stages:
            with torch.cuda.device(device):
                stream = torch.cuda.Stream(device=device)
                examples = {lanes: torch.zeros((lanes, 1, self.target.cfg.hidden_size), device=device,
                                                dtype=torch.bfloat16) for lanes in widths}
                for block in blocks:
                    if block.mlp not in self.grouped:
                        continue
                    if torch.cuda.mem_get_info(device)[0] < 2 * 1024**3:
                        break
                    eager = self.grouped[block.mlp].decode
                    graphed = GraphExperts(eager, stream, widths)
                    try:
                        for lanes, row in examples.items():
                            graphed.prepare(lanes, row)
                    except RuntimeError:
                        # Keep the eager path if this device cannot capture the projection.
                        break
                    self.grouped[block.mlp] = graphed

    def page_tables(self):
        pool = self.target.pool
        key = tuple(tuple(x) for x in pool.pages)
        if key != self.key:
            width = pool.required(pool.context)
            host = torch.tensor([list(x) + [-1] * (width - len(x)) for x in key], dtype=torch.int32)
            self.tables = {device: host.to(device) for device, _ in self.stages}
            self.key = key
        return self.tables

    def selected(self, lanes):
        return self.four if len(lanes) == LANES else self.single

    def enable_rank_graphs(self, widths):
        from hy4_rank_graph import SectionGraphs

        self.dense_graphs = SectionGraphs(self, widths)

    def meta(self, device, lanes, local, ids, history, starts, table):
        phys = torch.tensor(lanes, device=device)
        offsets = self.target.offsets.to(device)[phys]
        slots = torch.tensor(starts, device=device)
        # Sliding page IDs are identical for all layers on a rank.
        slides = next(b.attention.cache.table for d, blocks in self.stages if d == device
                      for b in blocks if not b.sparse)
        shared = table.index_select(0, phys)
        index_pages = None
        if ((self.reuse_recall_pages or len(lanes) in self.reuse_recall_widths or self.mixed_recall_min is not None)
                and (index := self.stage_index.get(device)) is not None):
            largest = max(starts)
            width = index.indexer.group_topk * RATIO
            sparse_rows = sum(n >= width for n in starts)
            if (self.mixed_recall_min is not None and largest >= self.mixed_recall_min
                    and (self.mixed_recall_max is None or (len(lanes) == 4 and largest <= self.mixed_recall_max))
                    and (self.mixed_recall_rows is None or self.mixed_recall_rows == sparse_rows)
                    and 0 < sparse_rows <= len(lanes) // 2):
                index_pages = mixed_recall_pages(index, starts, slots, shared)
            elif largest >= width and (self.reuse_recall_pages or len(lanes) in self.reuse_recall_widths):
                index_pages = recall_pages(index, slots, largest, shared)
        return Wave(phys, torch.tensor(local, device=device), starts, slots, slots + offsets, ids.to(device),
                    history.to(device), shared, slides.index_select(0, phys), index_pages)

    def attend(self, block, x, wave, table, dense=None):
        a, m = block.attention, block.attention.m
        positions = wave.phases[:, None]
        starts = wave.slots.int().contiguous() if dense is None else dense.index_starts
        if block.sparse:
            q_res, q, qr, k, r = a.project(x, positions)
            a.kv.kernel(k.half().contiguous(), r.contiguous(), *a.kv.planes, wave.shared, starts, BITS)
            ix = a.index
            raw = m.compressed_indexer.token_key_norm(m.compressed_indexer.token_key_projection(x))
            if dense is None:
                append_groups(ix, raw[:, 0], wave, table)
                largest = max(wave.starts)
                fused = (len(wave.starts) in self.fused_recall_widths
                         and (self.fused_recall_limit is None or largest <= self.fused_recall_limit))
                picks = recall(ix, x[:, 0], q_res[:, 0], wave.phases, wave.slots, largest, wave.shared,
                               prepared=wave.index_pages, fused_gather=fused)
                picks = picks[:, :key_width(wave.starts, picks.shape[1])]
            else:
                from hy4_rank_graph import append_index

                append_index(ix, raw[:, 0], dense)
                picks = dense.index_picks
            src, pages = a.kv.planes, wave.shared
            projection = m.kv_b_proj.weight.view(m.num_heads, m.qk_nope_head_dim + m.v_head_dim, LATENT)
        else:
            b = x.shape[0]
            k, r = m.kv_a_proj_with_mqa(x).split((LATENT, ROPE), -1)
            q, qr = m.q_b_proj(m.q_a_layernorm(m.q_a_proj(x))).view(
                b, 1, m.num_heads, m.qk_nope_head_dim + ROPE).transpose(1, 2).split((m.qk_nope_head_dim, ROPE), -1)
            qr, r = a.scope["apply_rotary_pos_emb"](
                qr, r.unsqueeze(1),
                *a.rotary(x, positions.unsqueeze(0).expand(3, -1, -1), layer_type="sliding_attention"))
            cache = a.cache
            cache_start = starts.remainder(cache.capacity) if dense is None else dense.slide_starts
            cache.kernel(m.kv_a_layernorm(k).half().contiguous(), r.squeeze(1).contiguous(),
                         *cache.planes, wave.rotary, cache_start, BITS)
            if dense is None:
                logical = wave.slots[:, None] + cache.tail[-key_width(wave.starts, WINDOW):]
                picks = logical.remainder(cache.capacity).masked_fill(logical < 0, -1)
            else:
                picks = dense.slide_picks
            src, pages, projection = cache.planes, wave.rotary, a.weight
        picks = picks.int().contiguous()
        if self.paged is not None:
            y = self.paged(q, qr, src, pages, picks, projection, m.sinks)
        else:
            y = gathered(a, q, qr, src, pages, picks, projection, m.sinks)
        value = y.transpose(1, 2).to(x.dtype)
        value = value * m.gate_proj(x).view(x.shape[0], 1, m.num_heads, m.v_head_dim).sigmoid()
        return m.post_proj_norm(m.o_proj(value.flatten(2)))

    def layer(self, block, x, wave, table, dense=None):
        gate, raw = branch(x, block.hca, block.na, block.cfg)
        x = write(x, self.attend(block, raw, wave, table, dense), gate)
        gate, raw = branch(x, block.hcm, block.nm, block.cfg)
        expert = self.grouped.get(block.mlp)
        if expert is None:
            y = block.mlp(raw)
        elif dense is not None and hasattr(expert, "operation"):
            # Capture the kernels directly inside the enclosing rank graph.
            y = expert.operation(raw)
        elif hasattr(expert, "decode"):
            y = expert.decode(raw)
        else:
            y = expert.routed(raw, decode=True)
        return write(x, y, gate)

    @torch.inference_mode()
    def stage(self, rank, waves, table, ends, engrams, incoming, outgoing, pipelined):
        device, blocks = self.stages[rank]
        cached = {}
        outputs = []
        with torch.cuda.device(device), (torch.cuda.stream(self.streams[device]) if pipelined else nullcontext()):
            try:
                for i, wave in enumerate(waves):
                    if incoming is None:
                        x = F.embedding(wave.ids, self.target.embed)
                        x = x.unsqueeze(2).expand(-1, -1, self.target.cfg.hc_mult, -1).contiguous()
                    else:
                        x = incoming[i].result()

                    def inject(layer, row):
                        if layer not in cached:
                            cached[layer] = self.ahead.take(layer, engrams[layer])
                        payload = cached[layer]
                        if pipelined:
                            payload = tuple(v.index_select(0, wave.positions) for v in payload)
                        return row + layer.step(row, *payload)

                    graphs = self.dense_graphs
                    if graphs is not None and not pipelined and graphs.supports(wave):
                        x = graphs.stage(rank, wave, table, x, inject)
                    else:
                        for block in blocks:
                            if block.engram is not None:
                                x = inject(block.engram, x)
                            x = self.layer(block, x, wave, table)
                    if outgoing is not None:
                        other = self.stages[rank+1][0]
                        with torch.cuda.stream(self.streams[other]) if pipelined else nullcontext():
                            sent = x.to(other, non_blocking=True)
                        outgoing[i].set_result(sent)
                    else:
                        outputs.append(x)
                for block in blocks:
                    if block.sparse:
                        block.attention.kv.generation = self.target.pool.generation
                        block.attention.kv.updated = ends
                    else:
                        block.attention.cache.lengths = ends
            except BaseException as error:
                if outgoing:
                    for pending in outgoing:
                        if not pending.done():
                            pending.set_exception(error)
                raise
        return outputs

    @torch.inference_mode()
    def step(self, ids, *, active_lanes=None, pipeline=None):
        t = self.target
        outputs, physical, lanes = self.features(ids, active_lanes=active_lanes, pipeline=pipeline)
        with torch.cuda.device(t.head.device):
            x = torch.cat(outputs, dim=0).to(t.head.device)
            x = norm(t.collapse(x), t.head_scale, t.cfg.rms_norm_eps).to(t.head.dtype)
            logits = F.linear(x, t.head)[:, 0]
            if len(lanes) == LANES and lanes == tuple(range(LANES)):
                return logits
            if self.head_lane_slices:
                return place_head_rows(logits, lanes)
            return logits.new_zeros((LANES, logits.shape[-1])).index_copy_(0, physical.to(t.head.device), logits)

    @torch.inference_mode()
    def features(self, ids, *, active_lanes=None, pipeline=None):
        t = self.target
        lanes = tuple(range(LANES)) if active_lanes is None else tuple(active_lanes)
        widths = tuple(int(i in lanes) for i in range(LANES))
        starts = t.pool.lengths
        t.pool.reserve(widths)
        ends = t.pool.pending
        physical = torch.tensor(lanes, device=t.entry)
        ids = ids.to(t.entry).index_select(0, physical)
        history = t.tail.index_select(0, physical)
        active_starts = tuple(starts[i] for i in lanes)
        engrams = self.ahead.submit(ids, history, active_starts)
        split = len(lanes) == LANES and (self.pipeline if pipeline is None else pipeline)
        cuts = (slice(0, 2), slice(2, 4)) if split else (slice(0, len(lanes)),)
        tables = self.page_tables()
        slots = tuple(range(len(lanes)))
        waves = [tuple(self.meta(d, lanes[c], slots[c], ids[c], history[c], active_starts[c], tables[d])
                       for c in cuts) for d, _ in self.stages]
        links = [[Future() for _ in cuts] for _ in range(len(waves) - 1)]
        args = [(i, batch, tables[device], ends, engrams, links[i-1] if i else None,
                 links[i] if i < len(links) else None, split)
                for i, ((device, _), batch) in enumerate(zip(self.stages, waves, strict=True))]
        if split:
            for device, stream in self.streams.items():
                stream.wait_stream(torch.cuda.current_stream(device))
            jobs = [self.workers.submit(self.stage, *a) for a in args]
            wait(jobs)
            for device, stream in self.streams.items():
                torch.cuda.current_stream(device).wait_stream(stream)
            outputs = [work.result() for work in jobs][-1]
            for x in outputs:
                x.record_stream(torch.cuda.current_stream(x.device))
        else:
            outputs = []
            for a in args:
                outputs = self.stage(*a)
        t.pool.commit(widths)
        t.tail.index_copy_(0, physical, torch.cat((history[:, 1:], ids), dim=1))
        return outputs, physical, lanes
