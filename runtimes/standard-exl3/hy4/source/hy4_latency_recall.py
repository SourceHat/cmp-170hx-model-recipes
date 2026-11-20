"Recall HY4's causal FP8 groups with tensor cores and stable top-k."

from dataclasses import dataclass

import torch

from hy4_compact_index_probe import DIM

from hy4_compact_index_probe import RATIO

from hy4_compact_index_probe import fp8_rows

from hy4_prompt_recall_topk import rank_key

@dataclass(frozen=True)
class RecallPages:
    dense: torch.Tensor
    current: torch.Tensor
    tiles: tuple

@dataclass(frozen=True)
class MixedRecall:
    rows: torch.Tensor
    latest: torch.Tensor
    table: torch.Tensor
    dense: torch.Tensor
    sparse: RecallPages

def dense_indices(latest, width):
    positions = torch.arange(width, device=latest.device).expand(len(latest), -1)
    return positions.masked_fill(positions > latest[:, None], -1)

def mixed_recall_pages(index, starts, latest, table):
    width = index.indexer.group_topk * RATIO
    lanes = [i for i, n in enumerate(starts) if n >= width]
    if not lanes or len(lanes) == len(starts):
        return None
    rows = torch.tensor(lanes, device=latest.device)
    positions = latest.index_select(0, rows)
    pages = table.index_select(0, rows)
    return MixedRecall(rows, positions, pages, dense_indices(latest, width),
                       recall_pages(index, positions, max(starts), pages))

def recall_pages(index, latest, largest, table):
    width = index.indexer.group_topk * RATIO
    dense = dense_indices(latest, width)
    current = latest // RATIO
    max_group, step = largest // RATIO, 4096
    tile = torch.arange(min(step, max_group), device=latest.device)
    tiles = []
    for begin in range(0, max_group, step):
        ids = begin + tile[:max_group - begin]
        mask = ids < current[:, None]
        pages = table[:, ids // index.stride].long().clamp_min(0)
        tiles.append((ids, mask, pages, ids % index.stride))
    return RecallPages(dense, current, tuple(tiles))

def recall(index, hidden, residual, phases, latest, largest, table, prepared=None, *, fused_gather=False):
    cfg = index.indexer
    width = cfg.group_topk * RATIO
    if isinstance(prepared, MixedRecall):
        rows = prepared.rows
        picks = recall(index, hidden.index_select(0, rows), residual.index_select(0, rows),
                       phases.index_select(0, rows), prepared.latest, largest, prepared.table, prepared.sparse,
                       fused_gather=fused_gather)
        return prepared.dense.index_copy(0, rows, picks)
    if prepared is None:
        dense = dense_indices(latest, width)
    else:
        dense = prepared.dense
    if largest < width:
        return dense
    current = latest // RATIO if prepared is None else prepared.current
    queries = cfg.query_projection(residual).reshape(len(latest), cfg.num_heads, DIM)
    packed, scales = fp8_rows(queries, phases[:, None], index.inv)
    q = packed.contiguous().view(torch.float8_e4m3fn).half()
    weights = cfg.head_weight_projection(hidden).float()
    weights = weights * scales * ((cfg.num_heads * DIM) ** -.5)
    missing = index.group_slots.numel()
    shift = missing.bit_length()
    mask = (1 << shift) - 1
    lo = -(0x7f800000 << shift)
    best = torch.full((len(latest), cfg.group_topk - 1), lo, dtype=torch.long, device=hidden.device)
    def page_tiles():
        max_group, step = largest // RATIO, 4096
        tile = torch.arange(min(step, max_group), device=hidden.device)
        for begin in range(0, max_group, step):
            ids = begin + tile[:max_group - begin]
            yield ids, ids < current[:, None], table[:, ids // index.stride].long().clamp_min(0), ids % index.stride

    for ids, allowed, pg, offset in page_tiles() if prepared is None else prepared.tiles:
        if fused_gather:
            from hy4_recall_gather import gather

            keys, key_scales = gather(index, pg, offset)
        else:
            keys = index.bits[pg, offset].contiguous().view(torch.float8_e4m3fn).half()
            key_scales = index.scales[pg, offset]
        dots = torch.bmm(q, keys.transpose(1, 2), out_dtype=torch.float32).relu_()
        scaled = (dots * weights[..., None]).sum(1) * key_scales
        ordering = rank_key(scaled, ids.expand_as(scaled), missing).masked_fill(~allowed, lo)
        best = torch.topk(torch.cat((best, ordering), 1), best.shape[1], sorted=False).values
    groups = torch.cat((missing - (best & mask), current[:, None]), 1)
    slots = (groups[..., None] * RATIO + torch.arange(RATIO, device=hidden.device)).flatten(1)
    slots = slots.masked_fill(slots > latest[:, None], index.capacity).sort(1).values
    sparse = slots.masked_fill(slots == index.capacity, -1)
    return torch.where((latest >= width)[:, None], sparse, dense)
