"Prompt tiles for HY4's native sliding window and shared indexed Q8 cache."

from types import SimpleNamespace

import torch

from torch.nn import functional as F

from decoder_prefix_probe import norm

from hy4_cached_index import GROUP_TILE

from hy4_cached_index import pack_tile

from hy4_compact_index_probe import DIM

from hy4_compact_index_probe import PAGE

from hy4_compact_index_probe import RATIO

from hy4_compact_index_probe import fp8_rows

from hy4_ops import ihc_write

from hy4_packed_prefill import packed_prefill

from hy4_shared_pool import LANES

from hy4_sliding_runtime import WINDOW

from hy4_standard_expert_pack import PackedExperts

from mla_eager_reference import projected_attention

PROMPT_TILE = 64

QUERY_TILE = 8

KEY_TILE = 1024

ATTEND_TILE = 2

ALL_LANES = tuple(range(LANES))

def append_index_groups(index, raw, phases, starts, lane_ids=ALL_LANES):
    """Finish the previous partial groups and pack aligned fixed tiles."""
    if lane_ids == ALL_LANES:
        index._validate(raw, phases)
    elif (phases.ndim != 2 or phases.shape[0] != len(lane_ids) or not phases.shape[1] or
          raw.shape != (*phases.shape, DIM) or raw.dtype != torch.bfloat16 or phases.dtype != torch.long or
          raw.device != index.table.device or phases.device != raw.device or (phases < 0).any() or
          any(starts[lane] + phases.shape[1] > index.capacity for lane in lane_ids)):
        raise ValueError("Invalid HY4 index input for the active prompt lanes")
    if index.trial is not None or tuple(index.lengths.tolist()) != starts:
        raise ValueError("Index prefill requires committed prefixes")
    inputs, offsets = [], [0] * len(lane_ids)
    for row, lane in enumerate(lane_ids):
        g, prior = divmod(starts[lane], RATIO)
        x = torch.cat((index.partial[lane, :prior], raw[row]), dim=0)
        p = torch.cat((index.first[lane:lane+1].expand(prior), phases[row]))
        complete, tail = divmod(len(x), RATIO)
        inputs.append((g, x[:complete * RATIO].reshape(complete, RATIO, DIM), p[:complete * RATIO:RATIO]))
        if tail:
            index.partial[lane, :tail] = x[-tail:]
            index.first[lane] = p[complete * RATIO]
        elif complete:
            index.partial[lane] = x[-RATIO:]
            index.first[lane] = p[-RATIO]
    while any(offset < len(x) for offset, (_, x, _) in zip(offsets, inputs, strict=True)):
        tile = raw.new_zeros((LANES, GROUP_TILE, RATIO, DIM))
        first = phases.new_zeros((LANES, GROUP_TILE))
        written = []
        for row, (lane, (group, x, p)) in enumerate(zip(lane_ids, inputs, strict=True)):
            offset = offsets[row]
            if offset == len(x):
                continue
            g = group + offset
            position = g % GROUP_TILE
            n = min(GROUP_TILE - position, len(x) - offset)
            tile[lane, position:position + n] = x[offset:offset + n]
            first[lane, position:position + n] = p[offset:offset + n]
            offsets[row] += n
            written.append((lane, g, position, n))
        bits, scales = pack_tile(index.indexer, index.inv, tile, first)
        for lane, g, position, n in written:
            ids = torch.arange(g, g + n, device=raw.device)
            page = index.table[lane, ids // index.stride].long()
            if (page < 0).any():
                raise ValueError("A complete index group needs its reserved target page")
            row = ids % index.stride
            index.bits[page, row] = bits[lane, position:position+n]
            index.scales[page, row] = scales[lane, position:position+n]
    if lane_ids == ALL_LANES:
        index.lengths.add_(raw.shape[1])
    else:
        index.lengths[list(lane_ids)] += raw.shape[1]

def prompt_recall(index, x, residual, phases, logical, lanes=None):
    """Score small query and group tiles while keeping chronological causal keys."""
    cfg = index.indexer
    budget = cfg.group_topk * RATIO
    columns = torch.arange(budget, device=x.device)
    dense = columns.expand(*logical.shape, -1).masked_fill(columns > logical[..., None], -1)
    if not (logical >= budget).any():
        return dense
    query = cfg.query_projection(residual).view(*logical.shape, cfg.num_heads, DIM)
    q, qs = fp8_rows(query, phases[..., None], index.inv)
    f = q.contiguous().view(torch.float8_e4m3fn).float()
    weights = cfg.head_weight_projection(x).float() * ((cfg.num_heads * DIM) ** -.5)
    weights *= qs
    table = index.table if lanes is None else index.table.index_select(0, lanes)
    current = logical // RATIO
    missing = index.group_slots.numel()
    n = cfg.group_topk - 1
    rows = []
    for qt in range(0, logical.shape[1], QUERY_TILE):
        end = qt + QUERY_TILE
        here = current[:, qt:end]
        lengths = logical[:, qt:end]
        best = weights.new_full((*here.shape, n), float("-inf"))
        chosen = torch.full_like(best, missing, dtype=torch.long)
        for begin in range(0, int(here.max()), KEY_TILE):
            group = begin + torch.arange(KEY_TILE, device=x.device)
            active = group < here[..., None]
            safe = group.clamp(max=missing-1)
            page = table[:, safe // index.stride].long()
            if (active.any(1) & (page < 0)).any():
                raise ValueError("Missing committed index page in prompt recall")
            local = safe % index.stride
            keys = index.bits[page.clamp_min(0), local].contiguous().view(torch.float8_e4m3fn).float()
            ks = index.scales[page.clamp_min(0), local]
            score = torch.einsum("bqhd,bgd->bqhg", f[:, qt:end], keys).relu_()
            score = ((score * weights[:, qt:end, :, None]).sum(2) * ks[:, None]).masked_fill_(~active, float("-inf"))
            values = torch.cat((best, score), dim=-1)
            ids = torch.cat((chosen, group.expand_as(score).masked_fill(~active, missing)), dim=-1)
            stable = ids.argsort(dim=-1, stable=True)
            top = values.gather(-1, stable).argsort(dim=-1, descending=True, stable=True)[..., :n]
            top = stable.gather(-1, top)
            best, chosen = values.gather(-1, top), ids.gather(-1, top)
        groups = torch.cat((chosen, here[..., None]), dim=-1)
        keys = (groups[..., None] * RATIO + torch.arange(RATIO, device=x.device)).flatten(-2)
        keys.masked_fill_(keys > lengths[..., None], -1)
        keys = keys.masked_fill(keys < 0, index.capacity).sort(dim=-1).values
        keys.masked_fill_(keys == index.capacity, -1)
        rows.append(torch.where(lengths[..., None] >= budget, keys, dense[:, qt:end]))
    return torch.cat(rows, dim=1)

def dequant(ext, words, scales, dimension):
    lead = words.shape[:-1]
    dst = torch.empty((*lead, dimension), device=words.device, dtype=torch.float16)
    ext.dequant_cache_cont(words.flatten(0, -2).contiguous(), scales.flatten(0, -2).contiguous(),
                           dst.flatten(0, -2), 0.0)
    return dst

def indexed_tile(attention, x, slots, phases, starts, layout, lane_ids=ALL_LANES):
    m = attention.m
    index = attention.index
    if attention.working is not None or index.trial is not None:
        raise ValueError("Cannot prefill in the middle of target verification")
    bsz = len(lane_ids)
    lanes = attention.lanes if lane_ids == ALL_LANES else torch.tensor(lane_ids, device=x.device)
    qresid, q, qr, k, r = attention.project(x, phases)
    attention.kv.append(layout, lanes, slots[:, 0].int().contiguous(), k, r)
    raw = m.compressed_indexer.token_key_norm(m.compressed_indexer.token_key_projection(x))
    index.bind(layout)
    append_index_groups(index, raw, phases, starts, lane_ids)
    real = prompt_recall(index, x, qresid, phases, slots, None if lane_ids == ALL_LANES else lanes)
    projection = m.kv_b_proj.weight.view(m.num_heads, m.qk_nope_head_dim + m.v_head_dim, m.kv_lora_rank)
    if int(slots.max()) < m.compressed_indexer.group_topk * RATIO:
        width = int(slots.max()) + 1
        logical = torch.arange(width, device=x.device).expand(bsz, -1)
        logical = logical.masked_fill(logical > slots[:, -1:], -1)
        w, s, rope = attention.kv.read(layout, lanes, logical)
        keys = dequant(attention.ext, w, s, m.kv_lora_rank).to(x.dtype)
        result = projected_attention(q, qr, keys, rope, projection, real[..., :width], slots, m.sinks)
    else:
        blocks = []
        for begin in range(0, x.shape[1], ATTEND_TILE):
            t = min(ATTEND_TILE, x.shape[1] - begin)
            selected = real[:, begin:begin + t]
            count = selected.shape[-1]
            w, s, rope = attention.kv.read(layout, lanes, selected.flatten(1))
            keys = dequant(attention.ext, w, s, m.kv_lora_rank).view(bsz*t, count, -1).to(x.dtype)
            local = torch.arange(count, device=x.device).expand_as(selected).masked_fill(selected < 0, -1)
            qpart, rpart = (a[:, :, begin:begin+t].transpose(1, 2).reshape(bsz*t, m.num_heads, 1, -1)
                            for a in (q, qr))
            part = projected_attention(qpart, rpart, keys, rope.view(bsz*t, count, -1),
                projection, local.view(bsz*t, 1, count),
                torch.full((bsz*t, 1), count-1, device=x.device), m.sinks)
            blocks.append(part.view(bsz, t, m.num_heads, m.v_head_dim).transpose(1, 2))
        result = torch.cat(blocks, dim=2)
    return finish(m, x, result), real

def finish(m, x, attended):
    y = attended.transpose(1, 2).to(x.dtype)
    y = y * m.gate_proj(x).view(*x.shape[:2], m.num_heads, m.v_head_dim).sigmoid()
    return m.post_proj_norm(m.o_proj(y.flatten(2)))

def sliding_tile(attention, x, slots, phases, starts, lane_ids=ALL_LANES):
    m, cache = attention.m, attention.cache
    width = x.shape[1]
    if cache.pending is not None or cache.lengths != starts or width + WINDOW - 1 > cache.capacity:
        raise ValueError("Sliding prompt tile must retain the committed window")
    q, qr, k, r = attention.project(x, phases)
    cache._store(lane_ids, [starts[i] for i in lane_ids], k, r)
    # The bounded span contains all live keys for every query in this tile.
    logical = slots[:, :1] + torch.arange(1-WINDOW, width, device=x.device)
    physical = logical.clamp_min(0).remainder(cache.capacity)
    batches = torch.tensor(lane_ids, device=x.device)[:, None]
    page = cache.table[batches, physical//PAGE].long()
    packed, scales, rope = (a[page, physical % PAGE].flatten(2).masked_fill((logical < 0)[..., None], 0)
                            for a in cache.planes)
    keys = dequant(attention.ext, packed, scales, m.kv_lora_rank).to(x.dtype)
    use = ((logical[:, None] >= 0) & (logical[:, None] <= slots[..., None]) &
           (logical[:, None] > slots[..., None] - WINDOW))
    local = torch.arange(logical.shape[1], device=x.device).expand_as(use).masked_fill(~use, -1)
    projection = m.kv_b_proj.weight.view(m.num_heads, m.qk_nope_head_dim + m.v_head_dim, m.kv_lora_rank)
    output = projected_attention(q, qr, keys, rope, projection, local,
                                 (slots - logical[:, :1]), m.sinks)
    cache.lengths = tuple(n + (width if i in lane_ids else 0) for i, n in enumerate(starts))
    return finish(m, x, output), logical[:, None].expand_as(use).masked_fill(~use, -1)

def prefill_tile(target, ids, *, capture=False, lane_ids=ALL_LANES):
    if (not lane_ids or tuple(sorted(set(lane_ids))) != lane_ids or not set(lane_ids) <= set(ALL_LANES) or
            target.trial is not None or ids.ndim != 2 or ids.shape[0] != len(lane_ids) or not 1 <= ids.shape[1] <= PROMPT_TILE
            or ids.dtype != torch.long or (ids < 0).any() or (ids >= target.cfg.vocab_size).any()):
        raise ValueError("Prefill a bounded tile on distinct native HY4 request lanes")
    width = ids.shape[1]
    starts = target.pool.lengths
    if any(starts[lane] + width > target.max_lengths[lane] for lane in lane_ids):
        raise ValueError("Prompt tile exceeds original HY4 context")
    ids = ids.to(target.entry)
    lanes = torch.tensor(lane_ids, device=target.entry)
    slots = torch.tensor([starts[i] for i in lane_ids], device=target.entry)[:, None] + torch.arange(width, device=target.entry)
    phases = slots + target.offsets[lanes, None]
    tail = torch.cat((target.tail.index_select(0, lanes), ids), dim=1)
    widths = tuple(width if i in lane_ids else 0 for i in ALL_LANES)
    target.pool.reserve(widths)
    x = F.embedding(ids, target.embed).unsqueeze(2).expand(-1, -1, target.cfg.hc_mult, -1).contiguous()
    layouts, trace = {}, []
    for block in target.blocks:
        d = block.device
        with torch.cuda.device(d):
            x = x.to(d)
            positions = phases.to(d)
            tokens = slots.to(d)
            if block.engram is not None:
                wave = SimpleNamespace(ids=ids.to(d), tokens=tail.to(d), start=target.tail.shape[1], slots=tokens)
                x = x + block.engram.step(x, *block.engram.fetch(wave))
            gate, raw = block.branch(x, block.hca, block.na)
            if block.sparse:
                if d not in layouts:
                    layouts[d] = target.pool.layout(d, tentative=True)
                value, recalled = indexed_tile(block.attention, raw, tokens, positions, starts, layouts[d], lane_ids)
            else:
                value, recalled = sliding_tile(block.attention, raw, tokens, positions, starts, lane_ids)
            x = ihc_write(x, value, gate)
            gate, raw = block.branch(x, block.hcm, block.nm)
            if isinstance(block.mlp, PackedExperts):
                if lane_ids == ALL_LANES:
                    value = packed_prefill(block.mlp, raw)
                else:
                    local = lanes.to(d)
                    padded = raw.new_zeros((LANES, *raw.shape[1:])).index_copy_(0, local, raw)
                    value = packed_prefill(block.mlp, padded).index_select(0, local)
            else:
                value = block.mlp(raw)
            x = ihc_write(x, value, gate)
            if capture:
                trace.append((x, recalled))
    target.pool.commit(widths)
    target.tail.index_copy_(0, lanes, tail[:, -target.tail.shape[1]:])
    if target.head is not None:
        last = norm(target.collapse(x[:, -1:].to(target.head.device)), target.head_scale,
                    target.cfg.rms_norm_eps).to(target.head.dtype)
        return last, F.linear(last, target.head), trace
    return x, None, trace

def ragged_tiles(input_ids):
    """Group only the live requests that have the same width in this prompt tile."""
    lengths = tuple(ids.shape[0] for ids in input_ids)
    if len(lengths) != LANES or min(lengths) <= 0 or any(ids.ndim != 1 for ids in input_ids):
        raise ValueError("Provide one non-empty vector per native HY4 request")
    for start in range(0, max(lengths), PROMPT_TILE):
        groups = {}
        for lane, length in enumerate(lengths):
            width = min(PROMPT_TILE, length - start)
            if width > 0:
                groups.setdefault(width, []).append(lane)
        for width, group in groups.items():
            stop = start + width
            yield tuple(group), start, stop, torch.stack([input_ids[lane][start:stop] for lane in group])
