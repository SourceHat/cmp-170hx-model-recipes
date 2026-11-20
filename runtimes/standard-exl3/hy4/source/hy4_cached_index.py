'Incremental HY4 FP8 group cache for causal recall and speculative rollback.'

import torch

from torch.nn.functional import pad

from hy4_compact_index_probe import DIM

from hy4_compact_index_probe import PAGE

from hy4_compact_index_probe import RATIO

from hy4_compact_index_probe import fp8_rows

from hy4_compact_index_probe import rank

GROUP_TILE = 32

def pack_tile(indexer, inv, raw, first):
    return fp8_rows(indexer.pool_groups(raw.flatten(1, 2)), first, inv)

def pack_history(indexer, inv, raw, positions):
    """Pack complete groups with the same GEMM geometry as a one-group append."""
    lanes, tokens, _ = raw.shape
    groups = tokens // RATIO
    bits, scales = [], []
    for begin in range(0, groups, GROUP_TILE):
        end = min(groups, begin + GROUP_TILE)
        count = end - begin
        tile = raw.new_zeros((lanes, GROUP_TILE, RATIO, DIM))
        first = positions.new_zeros((lanes, GROUP_TILE))
        tile[:, :count] = raw[:, begin * RATIO:end * RATIO].reshape(lanes, count, RATIO, DIM)
        first[:, :count] = positions[:, begin * RATIO:end * RATIO:RATIO]
        b, s = pack_tile(indexer, inv, tile, first)
        bits.append(b[:, :count])
        scales.append(s[:, :count])
    if not groups:
        return raw.new_empty((lanes, 0, DIM), dtype=torch.uint8), raw.new_empty((lanes, 0), dtype=torch.float32)
    return torch.cat(bits, 1), torch.cat(scales, 1)

class IndexPages:
    def __init__(self, table, indexer, inv_freq):
        if (table.ndim != 2 or not table.numel() or table.dtype != torch.int32 or
                not torch.equal(table.flatten().sort().values, torch.arange(table.numel(), device=table.device,
                                                                          dtype=table.dtype)) or
                (indexer.compress_ratio, indexer.head_dim) != (RATIO, DIM)):
            raise ValueError("Unexpected HY4 index pages or native grouping geometry")
        self.table, self.indexer, self.inv = table, indexer, inv_freq
        self.lanes, self.capacity, self.stride = table.shape[0], table.shape[1] * PAGE, PAGE // RATIO
        self.group_slots = torch.arange(self.capacity // RATIO, device=table.device)
        self.rows = torch.arange(self.lanes, device=table.device)
        self.bits = torch.zeros((table.numel(), self.stride, DIM), dtype=torch.uint8, device=table.device)
        self.scales = torch.ones((table.numel(), self.stride), dtype=torch.float32, device=table.device)
        self.lengths = torch.zeros((self.lanes,), dtype=torch.long, device=table.device)
        self.partial = torch.zeros((self.lanes, RATIO, DIM), dtype=torch.bfloat16, device=table.device)
        self.first = torch.zeros_like(self.lengths)
        self.trial = None

    def _validate(self, raw, positions):
        if (positions.ndim != 2 or positions.shape[0] != self.lanes or not positions.shape[1] or
                raw.shape != (*positions.shape, DIM) or raw.dtype != torch.bfloat16 or positions.dtype != torch.long or
                raw.device != self.table.device or positions.device != raw.device or (positions < 0).any() or
                (self.lengths + positions.shape[1] > self.capacity).any()):
            raise ValueError("Invalid raw HY4 index keys, phase positions or page capacity")

    def seed(self, raw, positions):
        """Pool the prompt once; keep just the unfinished group's raw keys."""
        self._validate(raw, positions)
        if self.trial is not None or self.lengths.any():
            raise ValueError("An index seed requires empty pages")
        width = raw.shape[1]
        groups, remainder = divmod(width, RATIO)
        if groups:
            g = self.group_slots[:groups]
            page, offset = self.table[:, g // self.stride].long(), g % self.stride
            self.bits[page, offset], self.scales[page, offset] = pack_history(self.indexer, self.inv, raw, positions)
        if remainder:
            self.partial[:, :remainder] = raw[:, groups * RATIO:]
            self.first.copy_(positions[:, groups * RATIO])
        self.lengths.fill_(width)

    def begin(self):
        if self.trial is not None:
            raise ValueError("An index verification is already pending")
        self.trial = (self.lengths.clone(), self.partial.clone(), self.first.clone(), [])

    def _step(self, raw, positions, active, *, write_groups):
        offset = self.lengths % RATIO
        self.first.copy_(torch.where(active & (offset == 0), positions, self.first))
        self.partial[self.rows, offset] = torch.where(active[:, None], raw, self.partial[self.rows, offset])
        closed = active & (offset == RATIO - 1)
        if write_groups and closed.any():
            tile_id = self.lengths // RATIO % GROUP_TILE
            tile = raw.new_zeros((self.lanes, GROUP_TILE, RATIO, DIM))
            first = positions.new_zeros((self.lanes, GROUP_TILE))
            tile[self.rows, tile_id] = self.partial
            first[self.rows, tile_id] = self.first
            bits, scales = pack_tile(self.indexer, self.inv, tile, first)
            group = self.lengths[closed] // RATIO
            p = self.table[self.rows[closed], group // self.stride].long()
            o = group % self.stride
            self.bits[p, o], self.scales[p, o] = bits[self.rows[closed], tile_id[closed]], scales[self.rows[closed], tile_id[closed]]
        self.lengths += active

    def append(self, raw, positions):
        self._validate(raw, positions)
        pending = None if self.trial is None else self.trial[-1]
        if pending is not None and len(pending) + raw.shape[1] > 6:
            raise ValueError("The native DFly2 verify window holds at most six rows")
        active = torch.ones_like(self.lengths, dtype=torch.bool)
        for t in range(raw.shape[1]):
            r, p = raw[:, t], positions[:, t]
            self._step(r, p, active, write_groups=True)
            if pending is not None:
                pending.append((r.clone(), p.clone()))

    def resolve(self, accepted):
        if (self.trial is None or accepted.shape != self.lengths.shape or accepted.device != self.lengths.device or
                accepted.dtype not in (torch.int32, torch.int64) or (accepted < 0).any() or
                (accepted >= len(self.trial[-1])).any()):
            raise ValueError("Accepted DFly2 counts must identify a row in the trial window")
        lengths, partial, first, pending = self.trial
        self.trial = None
        self.lengths.copy_(lengths)
        self.partial.copy_(partial)
        self.first.copy_(first)
        # Newly closed groups already contain the exact accepted bytes. Rewind the unfinished raw tail.
        for t, (r, p) in enumerate(pending):
            self._step(r, p, accepted >= t, write_groups=False)

    def recall(self, x, q_resid, positions):
        """Select causal target slots for each request's latest appended token."""
        if (x.ndim != 2 or x.shape[0] != self.lanes or q_resid.ndim != 2 or q_resid.shape[0] != self.lanes or
                positions.shape != self.lengths.shape or (self.lengths == 0).any()):
            raise ValueError("Recall expects one appended target query per request")
        index = self.indexer
        latest = self.lengths - 1
        budget = index.group_topk * RATIO
        offsets = torch.arange(RATIO, device=x.device)
        dense_slots = torch.arange(budget, device=x.device).expand(self.lanes, -1)
        dense = dense_slots.masked_fill(dense_slots > latest[:, None], -1)
        use_sparse = self.lengths > budget
        if not use_sparse.any():
            return dense
        current = latest // RATIO
        g = self.group_slots
        page, offset = self.table[:, g // self.stride].long(), g % self.stride
        packed, scale = self.bits[page, offset], self.scales[page, offset]
        query = index.query_projection(q_resid).reshape(self.lanes, index.num_heads, DIM)
        q, qs = fp8_rows(query, positions[:, None], self.inv)
        head = index.head_weight_projection(x).float() * ((index.num_heads * DIM) ** -0.5)
        valid = g < current[:, None]
        logits = rank(q, qs, head, packed, scale, valid)
        count = min(index.group_topk - 1, len(g))
        picks = logits.topk(count, dim=-1).indices
        picks = picks.masked_fill(~valid.gather(1, picks), -1)
        picks = pad(picks, (0, index.group_topk - 1 - count), value=-1)
        groups = torch.cat((picks, current[:, None]), dim=-1)
        slots = (groups[..., None] * RATIO + offsets).flatten(1)
        slots = slots.masked_fill((slots < 0) | (slots > latest[:, None]), -1)
        return torch.where(use_sparse[:, None], slots, dense)
