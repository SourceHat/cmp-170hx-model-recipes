'Replay the exact four-lane fallback across whole HY4 decoder sections.'

from itertools import groupby

from types import SimpleNamespace

import torch

from torch.nn import functional as F

from decoder_prefix_probe import norm

from hy4_ops import ihc_write

from hy4_paged_q8_probe import BITS

from hy4_quality_device_step import ONE

from hy4_quality_device_step import indexed_value

from hy4_quality_device_step import key_width

from hy4_quality_device_step import sliding_math

from hy4_quality_device_step import step as eager

from hy4_rank_graph import DenseMeta

from hy4_rank_graph import RankGraph

from hy4_rank_graph import append_index

from hy4_shared_pool import LANES

class ExactSections:
    def __init__(self, target, dispatch):
        self.target, self.dispatch = target, dispatch
        self.attend = target.device_attention
        self.stages = []
        self.graphs, self.errors = {}, {}
        self.rank_meta = {}
        self.limit = min(a.attention.index.indexer.group_topk * a.attention.index.indexer.compress_ratio
                         for a in target.blocks if a.sparse)
        for device, blocks in groupby(target.blocks, key=lambda b: b.device):
            stages = []
            for block in blocks:
                if not stages or block.engram is not None:
                    stages.append([])
                stages[-1].append(block)
            sliding = next(b.attention.cache for group in stages for b in group if not b.sparse)
            self.stages.append((device, sliding, stages))
        self.streams = {device: torch.cuda.Stream(device=device) for device, _, _ in self.stages}

    def supports(self, active_lanes):
        return len(active_lanes) == LANES and max(self.target.pool.lengths) < self.limit

    def layer(self, block, x, meta):
        a = block.attention
        gate, raw = block.branch(x, block.hca, block.na)
        if block.sparse:
            _, q, qr, k, r = a.project(raw, meta.phases[:, None])
            a.kv.kernel(k.half().contiguous(), r.contiguous(), *a.kv.planes, meta.shared, meta.index_starts, BITS)
            indexer = a.m.compressed_indexer
            keys = indexer.token_key_norm(indexer.token_key_projection(raw))[:, 0]
            append_index(a.index, keys, meta)
            y = indexed_value(a, raw, q, qr, meta.shared, meta.physical, meta.index_picks.long(), self.attend)
        else:
            y = sliding_math(a, raw, meta.slots, meta.phases, meta.physical, meta.slide_picks.shape[1], self.attend)
        x = ihc_write(x, y, gate)
        gate, raw = block.branch(x, block.hcm, block.nm)
        return ihc_write(x, self.dispatch.get(block.mlp, block.mlp.forward)(raw), gate)

    def section(self, device, number, blocks, hidden, meta, width):
        key = (device, number, width)
        graph = self.graphs.get(key)

        def operation(x, inputs):
            for block in blocks:
                x = self.layer(block, x, inputs)
            return x

        if graph is None and key not in self.errors:
            if torch.cuda.mem_get_info(device)[0] < 2 * 2**30:
                self.errors[key] = "Insufficient headroom for section replay"
            else:
                try:
                    graph = self.graphs[key] = RankGraph(operation, hidden, meta, self.streams[device], shared=True)
                except RuntimeError as error:
                    self.errors[key] = str(error)
        return graph(hidden, meta) if graph is not None else operation(hidden, meta)

    def step(self, ids, *, active_lanes=tuple(range(LANES))):
        target = self.target
        if not self.supports(active_lanes):
            return eager(target, ids, active_lanes=active_lanes)
        pool = target.pool
        starts = pool.lengths
        pool.reserve(ONE)
        ends = pool.pending
        ids = ids.to(target.entry)
        ahead = target.engram_read_ahead
        futures = ahead.submit(ids, target.tail, starts)
        hidden = F.embedding(ids, target.embed).unsqueeze(2).expand(-1, -1, target.cfg.hc_mult, -1).contiguous()
        width = key_width(starts, self.limit)
        for device, sliding, sections in self.stages:
            with torch.cuda.device(device):
                hidden = hidden.to(device, non_blocking=True)
                layout = pool.layout(device, tentative=True)
                slots = torch.tensor(starts, device=device)
                wave = SimpleNamespace(slots=slots, phases=slots + target.offsets.to(device), shared=layout.table,
                                       rotary=sliding.table, physical=torch.arange(LANES, device=device))
                current = DenseMeta.prepare(wave, sliding, width)
                key = (device, width)
                meta = self.rank_meta.get(key)
                if meta is None:
                    meta = self.rank_meta[key] = DenseMeta(*(torch.empty_like(v) for v in current.tensors()))
                # Each section on this rank reads the same offsets and page plan.
                torch._foreach_copy_(meta.tensors(), current.tensors())
                for number, blocks in enumerate(sections):
                    if (engram := blocks[0].engram) is not None:
                        hidden = hidden + engram.step(hidden, *ahead.take(engram, futures[engram]))
                    hidden = self.section(device, number, blocks, hidden, meta, width)
                    for block in blocks:
                        a = block.attention
                        if block.sparse:
                            a.kv.generation, a.kv.updated = layout.generation, ends
                            a.index.bind(layout)
                        else:
                            a.cache.lengths = ends
        pool.commit(ONE)
        target.tail = torch.cat((target.tail[:, 1:], ids), dim=1)
        x = norm(target.collapse(hidden.to(target.head.device)), target.head_scale,
                 target.cfg.rms_norm_eps).to(target.head.dtype)
        return F.linear(x, target.head)[:, 0]
