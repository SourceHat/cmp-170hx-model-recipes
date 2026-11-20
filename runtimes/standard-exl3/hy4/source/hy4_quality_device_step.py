"Single-token HY4 target decode driven by the host's committed page plan."

from types import SimpleNamespace

import torch

from torch.nn import functional as F

from decoder_prefix_probe import norm

from hy4_cached_index import GROUP_TILE

from hy4_cached_index import pack_tile

from hy4_compact_index_probe import DIM

from hy4_compact_index_probe import RATIO

from hy4_compact_index_probe import fp8_rows

from hy4_compact_index_probe import rank

from hy4_indexed_runtime import SCORE_TILE

from hy4_ops import ihc_write

from hy4_paged_q8_probe import BITS

from hy4_paged_q8_probe import LATENT

from hy4_paged_q8_probe import PAGE

from hy4_paged_q8_probe import ROPE

from hy4_shared_pool import LANES

from hy4_sliding_runtime import WINDOW

ONE = (1,) * LANES

def attention(q_nope, q_rope, latents, rotated_keys, projection, indices, sinks):
    # Match the eager BF16 projection and softmax order. The page plan builds the mask.
    batch, heads, queries, nope = q_nope.shape
    keys, rope = latents.shape[1], q_rope.shape[-1]
    kv = F.linear(latents.unsqueeze(1), projection.flatten(0, 1)).view(batch, keys, heads, -1).transpose(1, 2)
    k_nope, value = kv.split((nope, projection.shape[1] - nope), dim=-1)
    k = torch.cat((k_nope, rotated_keys[:, None].expand(-1, heads, -1, -1)), dim=-1)
    q = torch.cat((q_nope, q_rope), dim=-1)
    score = torch.matmul(q, k.transpose(-1, -2)) * ((nope + rope) ** -0.5)
    selected = torch.zeros((batch, queries, keys + 1), dtype=torch.bool, device=latents.device)
    selected.scatter_(-1, indices.masked_fill(indices < 0, keys).long(), True)
    score = score.masked_fill(~selected[:, None, :, :keys], float("-inf"))
    sink = sinks.reshape(1, -1, 1, 1).expand(batch, -1, queries, 1)
    scores = torch.cat((score, sink), dim=-1)
    probs = F.softmax(scores - scores.max(dim=-1, keepdim=True).values, dim=-1, dtype=scores.dtype)
    return torch.matmul(probs[..., :-1].to(value.dtype), value)

def projected(a, x, q, qr, planes, slots, projection, attend=attention):
    words, scales, rotated = planes
    width = words.shape[1]
    keys = torch.empty((LANES * width, LATENT), dtype=torch.float16, device=x.device)
    a.ext.dequant_cache_cont(words.flatten(0, 1).contiguous(), scales.flatten(0, 1).contiguous(), keys, 0.0)
    local = torch.arange(width, device=x.device).expand_as(slots).masked_fill(slots < 0, -1)
    m = a.m
    y = attend(q, qr, keys.view(LANES, width, LATENT).to(x.dtype), rotated, projection,
               local[:, None], m.sinks).transpose(1, 2)
    y = y.to(x.dtype) * m.gate_proj(x).view(LANES, 1, m.num_heads, m.v_head_dim).sigmoid()
    return m.post_proj_norm(m.o_proj(y.flatten(2)))

def key_width(starts, capacity):
    return min(capacity, max(64, 1 << max(starts).bit_length()))

def sliding(a, x, slots, phases, starts, ends, lane_ids, attend=attention, *, compact=False):
    cache = a.cache
    if cache.pending is not None or cache.lengths != starts:
        raise ValueError("Start a single-row decode from the committed sliding window")
    y = sliding_math(a, x, slots, phases, lane_ids, key_width(starts, WINDOW) if compact else WINDOW, attend)
    cache.lengths = ends
    return y

def sliding_math(a, x, slots, phases, lane_ids, width, attend):
    m, cache = a.m, a.cache
    k, r = m.kv_a_proj_with_mqa(x).split((LATENT, ROPE), -1)
    q, qr = m.q_b_proj(m.q_a_layernorm(m.q_a_proj(x))).view(
        LANES, 1, m.num_heads, m.qk_nope_head_dim + ROPE).transpose(1, 2).split((m.qk_nope_head_dim, ROPE), -1)
    qr, r = a.scope["apply_rotary_pos_emb"](qr, r.unsqueeze(1),
        *a.rotary(x, phases[:, None].unsqueeze(0).expand(3, -1, -1), layer_type="sliding_attention"))
    k = m.kv_a_layernorm(k).half().contiguous()
    cache.kernel(k, r.squeeze(1).contiguous(), *cache.planes, cache.table,
                 slots.int().remainder(cache.capacity).contiguous(), BITS)
    tail = cache.tail[-width:]
    logical = (slots[:, None] + tail).clamp_min(-1)
    valid = logical >= 0
    physical = logical.clamp_min(0).remainder(cache.capacity)
    page = cache.table[lane_ids[:, None], physical // PAGE].long()
    planes = tuple(p[page, physical % PAGE].flatten(2).masked_fill(~valid[..., None], 0) for p in cache.planes)
    return projected(a, x, q, qr, planes, logical, a.weight, attend)

def append_index(index, raw, phases, slots, starts, layout):
    index.bind(layout)
    offset = slots % RATIO
    index.first.copy_(torch.where(offset == 0, phases, index.first))
    index.partial[index.rows, offset] = raw
    closed = [i for i, n in enumerate(starts) if n % RATIO == RATIO - 1]
    if closed:
        tile_id = slots // RATIO % GROUP_TILE
        tile = raw.new_zeros((LANES, GROUP_TILE, RATIO, DIM))
        first = phases.new_zeros((LANES, GROUP_TILE))
        tile[index.rows, tile_id] = index.partial
        first[index.rows, tile_id] = index.first
        bits, scales = pack_tile(index.indexer, index.inv, tile, first)
        rows = index.rows if len(closed) == LANES else torch.tensor(closed, device=raw.device)
        group = slots[rows] // RATIO
        page = index.table[rows, group // index.stride].long()
        index.bits[page, group % index.stride] = bits[rows, tile_id[rows]]
        index.scales[page, group % index.stride] = scales[rows, tile_id[rows]]
    index.lengths.copy_(layout.lengths)

def recall(index, x, q_resid, phases, latest, largest, table=None):
    cfg = index.indexer
    budget = cfg.group_topk * RATIO
    lanes = latest.shape[0]
    slots = torch.arange(budget, device=x.device).expand(lanes, -1)
    dense = slots.masked_fill(slots > latest[:, None], -1)
    if largest < budget:
        return dense
    current = latest // RATIO
    count = cfg.group_topk - 1
    query = cfg.query_projection(q_resid).reshape(lanes, cfg.num_heads, DIM)
    q, qs = fp8_rows(query, phases[:, None], index.inv)
    head = cfg.head_weight_projection(x).float() * ((cfg.num_heads * DIM) ** -0.5)
    best = head.new_full((lanes, count), float("-inf"))
    missing = index.group_slots.numel()
    chosen = torch.full((lanes, count), missing, device=x.device, dtype=torch.long)
    tile = torch.arange(SCORE_TILE, device=x.device)
    for begin in range(0, largest // RATIO, SCORE_TILE):
        ids = begin + tile
        valid = ids < current[:, None]
        safe = ids.clamp(max=missing - 1)
        page = (index.table if table is None else table)[:, safe // index.stride].long().clamp_min(0)
        offset = safe % index.stride
        values = rank(q, qs, head, index.bits[page, offset], index.scales[page, offset], valid)
        candidates = ids.expand(LANES, -1).masked_fill(~valid, missing)
        joined, which = torch.cat((best, values), dim=1), torch.cat((chosen, candidates), dim=1)
        order = which.argsort(dim=1, stable=True)
        ranked = joined.gather(1, order).argsort(dim=1, descending=True, stable=True)[:, :count]
        top = order.gather(1, ranked)
        best, chosen = joined.gather(1, top), which.gather(1, top)
    groups = torch.cat((chosen, current[:, None]), dim=1)
    tokens = (groups[..., None] * RATIO + torch.arange(RATIO, device=x.device)).flatten(1)
    tokens = tokens.masked_fill(tokens > latest[:, None], -1)
    tokens = torch.where((latest >= budget)[:, None], tokens, dense)
    ordered = tokens.masked_fill(tokens < 0, index.capacity).sort(dim=1).values
    return ordered.masked_fill(ordered == index.capacity, -1)

def indexed(a, x, slots, phases, starts, ends, layout, lane_ids, attend=attention, *, compact=False):
    if a.working is not None or a.index.trial is not None or a.kv.visible_lengths() != starts:
        raise ValueError("Start a single-row decode from the committed shared cache")
    qresid, q, qr, k, r = a.project(x, phases[:, None])
    a.kv.kernel(k.half().contiguous(), r.contiguous(), *a.kv.planes, layout.table,
                slots.int().contiguous(), BITS)
    a.kv.generation, a.kv.updated = layout.generation, ends
    ix = a.index
    raw = a.m.compressed_indexer.token_key_norm(a.m.compressed_indexer.token_key_projection(x))
    append_index(ix, raw[:, 0], phases, slots, starts, layout)
    real = recall(ix, x[:, 0], qresid[:, 0], phases, slots, max(starts))
    if compact:
        real = real[:, :key_width(starts, real.shape[1])]
    return indexed_value(a, x, q, qr, layout.table, lane_ids, real, attend), real

def indexed_value(a, x, q, qr, table, lane_ids, real, attend):
    logical = real.clamp_min(0)
    page = table[lane_ids[:, None], logical // PAGE].long().clamp_min(0)
    planes = tuple(p[page, logical % PAGE].flatten(2).masked_fill((real < 0)[..., None], 0) for p in a.kv.planes)
    m = a.m
    projection = m.kv_b_proj.weight.view(m.num_heads, m.qk_nope_head_dim + m.v_head_dim, m.kv_lora_rank)
    return projected(a, x, q, qr, planes, real, projection, attend)

def step(target, ids, *, attend=None, experts=None, compact=None, active_lanes=None):
    faster = getattr(target, "latency_decode", None)
    ready = tuple(range(LANES)) if active_lanes is None else active_lanes
    if faster is not None and faster.selected(ready):
        return faster.step(ids, active_lanes=ready)
    starts = target.pool.lengths
    if (target.trial is not None or target.pool.pending is not None or ids.shape != (LANES, 1)
            or ids.dtype != torch.long or any(n >= m for n, m in zip(starts, target.max_lengths, strict=True))):
        raise ValueError("Expected one row per lane within the native context")
    torch._assert_async(((ids >= 0) & (ids < target.cfg.vocab_size)).all(), "Invalid HY4 token ID")
    if experts is None:
        experts = getattr(target, "verified_panel_experts", None)
    if compact is None:
        compact = getattr(target, "verified_panel_compact", False)
    if attend is None:
        attend = getattr(target, "device_attention", attention)
    target.pool.reserve(ONE)
    ends = target.pool.pending
    ids = ids.to(target.entry)
    ahead = getattr(target, "engram_read_ahead", None)
    pending_engram = ahead.submit(ids, target.tail, starts) if ahead is not None else None
    x = F.embedding(ids, target.embed).unsqueeze(2).expand(-1, -1, target.cfg.hc_mult, -1).contiguous()
    metadata = {}
    layouts = {}
    selected = {}
    for block in target.blocks:
        d = block.device
        with torch.cuda.device(d):
            if d not in metadata:
                slots = torch.tensor(starts, device=d)
                local_ids = ids.to(d)
                prefix = torch.cat((target.tail.to(d), local_ids), dim=1)
                metadata[d] = (slots, slots + target.offsets.to(d), local_ids, prefix, torch.arange(LANES, device=d))
            slots, phases, local_ids, prefix, lane_ids = metadata[d]
            x = x.to(d)
            if block.engram is not None:
                layer = block.engram
                if ahead is None:
                    wave = SimpleNamespace(ids=local_ids, tokens=prefix, start=target.tail.shape[1], slots=slots[:, None])
                    values = layer.fetch(wave)
                else:
                    values = ahead.take(layer, pending_engram[layer])
                x = x + layer.step(x, *values)
            gate, raw = block.branch(x, block.hca, block.na)
            if block.sparse:
                if d not in layouts:
                    layouts[d] = target.pool.layout(d, tentative=True)
                y, _ = indexed(block.attention, raw, slots, phases, starts, ends, layouts[d], lane_ids, attend,
                               compact=compact)
            else:
                y = sliding(block.attention, raw, slots, phases, starts, ends, lane_ids, attend, compact=compact)
            x = ihc_write(x, y, gate)
            gate, raw = block.branch(x, block.hcm, block.nm)
            mlp = block.mlp
            forward = experts.get(mlp, mlp.forward) if experts is not None else mlp.forward
            if active_lanes and len(active_lanes) < LANES and hasattr(forward, "decode_subset"):
                if d not in selected:
                    selected[d] = torch.tensor(active_lanes, device=d)
                value = forward.decode_subset(raw, selected[d])
            else:
                value = forward(raw)
            x = ihc_write(x, value, gate)
    target.pool.commit(ONE)
    target.tail = torch.cat((target.tail[:, 1:], ids), dim=1)
    x = norm(target.collapse(x.to(target.head.device)), target.head_scale, target.cfg.rms_norm_eps).to(target.head.dtype)
    return F.linear(x, target.head)[:, 0]
