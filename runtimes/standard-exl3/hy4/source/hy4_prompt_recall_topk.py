'Causal HY4 prompt recall using score and group ID as one top-k key.'

import torch

from hy4_compact_index_probe import DIM

from hy4_compact_index_probe import RATIO

from hy4_compact_index_probe import fp8_rows

def rank_key(scores, ids, missing):
    # IEEE float magnitude plus sign gives an ordered integer, including equal signed zeros.
    raw = scores.contiguous().view(torch.int32).long()
    score = torch.where(raw < 0, -(raw & 0x7fffffff), raw)
    shift = missing.bit_length()
    return (score << shift) | (missing - ids)

def choose_cohorts(lengths, split_ragged):
    if not split_ragged:
        return [list(range(len(lengths)))]
    groups = []
    for lane in sorted(range(len(lengths)), key=lengths.__getitem__):
        if not groups or lengths[lane] > 2 * max(1, lengths[groups[-1][0]]):
            groups.append([])
        groups[-1].append(lane)
    return groups

def recall_group(index, f, weights, table, logical, dense, query_tile, key_tile):
    cfg = index.indexer
    current = logical // RATIO
    missing, n = index.group_slots.numel(), cfg.group_topk - 1
    shift = missing.bit_length()
    mask = (1 << shift) - 1
    invalid = -(0x7f800000 << shift)
    key_range = torch.arange(key_tile, device=f.device)
    token_range = torch.arange(RATIO, device=f.device)
    rows = []
    for lo in range(0, logical.shape[1], query_tile):
        hi = lo + query_tile
        here = current[:, lo:hi]
        lengths = logical[:, lo:hi]
        best = torch.full((*here.shape, n), invalid, device=f.device, dtype=torch.int64)
        for begin in range(0, int(here.max()), key_tile):
            group = begin + key_range
            active = group < here[..., None]
            safe = group.clamp(max=missing - 1)
            page = table[:, safe // index.stride].long()
            if (active.any(1) & (page < 0)).any():
                raise ValueError("Missing committed index page in prompt recall")
            local = safe % index.stride
            page = page.clamp_min(0)
            keys = index.bits[page, local].contiguous().view(torch.float8_e4m3fn).float()
            scales = index.scales[page, local]
            scores = torch.einsum("bqhd,bgd->bqhg", f[:, lo:hi], keys).relu_()
            scores = ((scores * weights[:, lo:hi, :, None]).sum(2) * scales[:, None]).masked_fill_(~active, float("-inf"))
            ids = group.expand_as(scores).masked_fill(~active, missing)
            selected = rank_key(scores, ids, missing)
            best = torch.topk(torch.cat((best, selected), dim=-1), n, sorted=False).values
        chosen = missing - (best & mask)
        groups = torch.cat((chosen, here[..., None]), dim=-1)
        slots = (groups[..., None] * RATIO + token_range).flatten(-2)
        slots.masked_fill_(slots > lengths[..., None], -1)
        slots = slots.masked_fill(slots < 0, index.capacity).sort(dim=-1).values
        slots.masked_fill_(slots == index.capacity, -1)
        rows.append(torch.where(lengths[..., None] >= cfg.group_topk * RATIO, slots, dense[:, lo:hi]))
    return torch.cat(rows, dim=1)

def prompt_recall_topk(index, x, residual, phases, logical, lanes=None, *, query_tile=16, key_tile=8192,
                       split_ragged=False):
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
    groups = choose_cohorts(logical.max(dim=-1).values.tolist(), split_ragged) if split_ragged else [list(range(len(x)))]
    if len(groups) == 1 and groups[0] == list(range(len(x))):
        return recall_group(index, f, weights, table, logical, dense, query_tile, key_tile)
    out = torch.empty_like(dense)
    for cohort in groups:
        rows = torch.tensor(cohort, device=x.device)
        inputs = [v.index_select(0, rows) for v in (f, weights, table, logical, dense)]
        out.index_copy_(0, rows, recall_group(index, *inputs, query_tile, key_tile))
    return out
