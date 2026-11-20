'Verify a native DFly2 proposal in a single target sweep when the keys fit.'

from types import SimpleNamespace

import torch

from torch.nn import functional as F

from decoder_prefix_probe import norm

from dfly_proposal_probe import TARGETS

from hy4_chunked_prefill import dequant

from hy4_chunked_prefill import finish

from hy4_compact_index_probe import RATIO

from hy4_native_dfly import DraftAnchor

from hy4_native_generation import VerifyWave

from hy4_ops import ihc_write

from hy4_packed_prefill import packed_prefill

from hy4_quality_device_step import attention

from hy4_shared_pool import LANES

from hy4_sliding_runtime import VERIFY

from hy4_sliding_runtime import WINDOW

from hy4_sliding_runtime import PAGE

from hy4_standard_expert_pack import PackedExperts

def early(runner, proposed, live_lanes=LANES):
    target = runner.target
    target.begin(VERIFY)
    counts = torch.zeros(LANES, dtype=torch.long, device=proposed.device)
    eligible = torch.arange(LANES, device=proposed.device) < live_lanes
    steps = []
    for i in range(VERIFY):
        sample = target.step(proposed[:, i:i+1].contiguous(), capture=True)
        steps.append(sample)
        if i == VERIFY - 1:
            break
        eligible = eligible & (sample[1][:, 0].argmax(-1) == proposed[:, i+1])
        counts += eligible
        if not bool(eligible.any()):
            break
    accepted = tuple(counts.tolist())
    target.commit(tuple(1 + n for n in accepted))
    return VerifyWave(proposed, accepted, runner._anchor(steps, counts))

def indexed(a, x, slots, phases, starts):
    qresid, q, qr, k, r = a.project(x, phases)
    del qresid
    a.kv.append(a.working, a.lanes, slots[:, 0].int().contiguous(), k, r)
    index = a.index
    m = a.m
    index.append(m.compressed_indexer.token_key_norm(m.compressed_indexer.token_key_projection(x)), phases)
    width = x.shape[1]
    key_len = max(starts) + width
    logical = torch.arange(key_len, device=x.device).expand(LANES, -1)
    newest = logical.masked_fill(logical > slots[:, -1:], -1)
    packed, scales, rope = a.kv.read(a.working, a.lanes, newest)
    keys = dequant(a.ext, packed, scales, m.kv_lora_rank).to(x.dtype)
    local = logical[:, None].expand(LANES, width, key_len).masked_fill(logical[:, None] > slots[..., None], -1)
    projection = m.kv_b_proj.weight.view(m.num_heads, m.qk_nope_head_dim + m.v_head_dim, m.kv_lora_rank)
    out = finish(m, x, attention(q, qr, keys, rope, projection, local, m.sinks))
    budget = m.compressed_indexer.group_topk * RATIO
    recall = F.pad(local, (0, budget - key_len), value=-1)
    return out, recall

def sliding(a, x, slots, phases, starts):
    cache = a.cache
    lanes = tuple(range(LANES))
    q, qr, k, r = a.project(x, phases)
    cache.append(lanes, k, r)
    width = x.shape[1]
    previous = min(max(starts), WINDOW - 1)
    offsets = torch.arange(-previous, width, device=x.device)
    logical = slots[:, :1] + offsets
    physical = logical.clamp_min(0).remainder(cache.capacity)
    page = cache.table[torch.arange(LANES, device=x.device)[:, None], physical // PAGE].long()
    packed, scales, rope = (v[page, physical % PAGE].flatten(2).masked_fill(logical[..., None] < 0, 0)
                            for v in cache.planes)
    keys = dequant(a.ext, packed, scales, a.m.kv_lora_rank).to(x.dtype)
    valid = ((logical[:, None] >= 0) & (logical[:, None] <= slots[..., None])
             & (logical[:, None] > slots[..., None] - WINDOW))
    local = torch.arange(len(offsets), device=x.device).expand_as(valid).masked_fill(~valid, -1)
    return finish(a.m, x, attention(q, qr, keys, rope, a.weight, local, a.m.sinks))

def tile(runner, proposed):
    target = runner.target
    width = proposed.shape[1]
    starts = target.pool.lengths
    target.begin(width)
    ids = proposed.to(target.entry)
    slots = torch.tensor(starts, device=target.entry)[:, None] + torch.arange(width, device=target.entry)
    phases = slots + target.offsets[:, None]
    tail = torch.cat((target.tail, ids), dim=1)
    x = F.embedding(ids, target.embed).unsqueeze(2).expand(-1, -1, target.cfg.hc_mult, -1).contiguous()
    ranks, recall = {}, {}
    for layer, block in enumerate(target.blocks):
        d = block.device
        with torch.cuda.device(d):
            if d not in ranks:
                ranks[d] = (ids.to(d), slots.to(d), phases.to(d), tail.to(d))
            local, positions, rope, history = ranks[d]
            x = x.to(d)
            if block.engram is not None:
                wave = SimpleNamespace(ids=local, slots=positions, tokens=history, start=target.tail.shape[1])
                x = x + block.engram.step(x, *block.engram.fetch(wave))
            gate, hidden = block.branch(x, block.hca, block.na)
            if block.sparse:
                y, selected = indexed(block.attention, hidden, positions, rope, starts)
                if layer in TARGETS:
                    recall[layer] = selected
            else:
                y = sliding(block.attention, hidden, positions, rope, starts)
            x = ihc_write(x, y, gate)
            gate, hidden = block.branch(x, block.hcm, block.nm)
            block_out = packed_prefill(block.mlp, hidden) if isinstance(block.mlp, PackedExperts) else block.mlp(hidden)
            x = ihc_write(x, block_out, gate)
    hidden = norm(target.collapse(x.to(target.head.device)), target.head_scale,
                  target.cfg.rms_norm_eps).to(target.head.dtype)
    predictions = F.linear(hidden, target.head).argmax(dim=-1)
    counts = (predictions[:, :-1] == proposed[:, 1:]).long().cumprod(dim=1).sum(dim=1)
    accepted = tuple(counts.tolist())
    target.trial = (width, target.trial[1], list(ids.split(1, dim=1)))
    target.commit(tuple(n + 1 for n in accepted))
    lanes = torch.arange(LANES, device=hidden.device)
    index = {layer: rows[lanes.to(rows.device), counts.to(rows.device)] for layer, rows in recall.items()}
    anchor = DraftAnchor(target.pool.generation, hidden[lanes, counts], predictions[lanes, counts], index)
    return VerifyWave(proposed, accepted, anchor)

def verify(runner, anchor, mode, live_lanes=LANES):
    proposed = runner.draft.propose(anchor)
    end = max(runner.target.pool.lengths) + VERIFY
    budget = min(b.attention.m.compressed_indexer.group_topk * RATIO
                 for b in runner.target.blocks if b.sparse)
    if mode == "tile" and end <= budget:
        return tile(runner, proposed)
    return early(runner, proposed, live_lanes)
