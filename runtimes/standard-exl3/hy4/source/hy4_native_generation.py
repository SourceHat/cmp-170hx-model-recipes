'Keep native DFly2 acceptance, target caches and the next anchor in sync.'

from dataclasses import dataclass

import torch

from dfly_proposal_probe import TARGETS

from hy4_chunked_prefill import PROMPT_TILE

from hy4_chunked_prefill import prefill_tile

from hy4_chunked_prefill import ragged_tiles

from hy4_native_dfly import DraftAnchor

from hy4_native_dfly import NativeDFly

from hy4_shared_pool import LANES

from hy4_sliding_runtime import VERIFY

@dataclass(frozen=True)
class VerifyWave:
    proposed: torch.Tensor
    accepted_counts: tuple
    anchor: DraftAnchor

class NativeGeneration:
    """Deterministic four-request runner for packed target and native draft parity."""

    def __init__(self, target):
        self.target = target
        self.draft = NativeDFly(target)

    def _anchor(self, steps, rows):
        hs = torch.cat([x[0] for x in steps], dim=1)
        ls = torch.stack([x[1].argmax(dim=-1)[:, 0] for x in steps], dim=1)
        lane = torch.arange(LANES, device=hs.device)
        recalled = {}
        for layer in TARGETS:
            indices = torch.stack([x[2][layer][1] for x in steps], dim=1)
            recalled[layer] = indices[lane.to(indices.device), rows.to(indices.device)]
        return DraftAnchor(self.target.pool.generation, hs[lane, rows], ls[lane, rows], recalled)

    def prefill(self, input_ids):
        if (input_ids.ndim != 2 or input_ids.shape[0] != LANES or not input_ids.shape[1]
                or any(self.target.pool.lengths)):
            raise ValueError("Prefill four fresh native HY4 requests")
        for start in range(0, input_ids.shape[1], PROMPT_TILE):
            stop = min(start + PROMPT_TILE, input_ids.shape[1])
            result = prefill_tile(self.target, input_ids[:, start:stop].contiguous(),
                                  capture=stop == input_ids.shape[1])
        h, logits, trace = result
        result = (h, logits, [(x[:, -1:], recalled[:, -1]) for x, recalled in trace])
        return self._anchor([result], torch.zeros(LANES, device=result[0].device, dtype=torch.long))

    def prefill_ragged(self, input_ids):
        t = self.target
        if (len(input_ids) != LANES or any(t.pool.lengths) or
                any(ids.ndim != 1 or ids.dtype != torch.long or not 0 < ids.numel() <= limit
                    or (ids < 0).any() or (ids >= t.cfg.vocab_size).any()
                    for ids, limit in zip(input_ids, t.max_lengths, strict=True))):
            raise ValueError("Use four valid fresh native HY4 requests")
        lengths = tuple(ids.numel() for ids in input_ids)
        if sum(t.pool.required(n) for n in lengths) > t.pool.capacity:
            raise ValueError("The four prompt histories exceed the common Q8 pool")
        tokens = tuple(ids.to(t.entry) for ids in input_ids)
        output, index = {}, {layer: {} for layer in TARGETS}
        for lanes, _, stop, tile in ragged_tiles(tokens):
            final = {lane for lane in lanes if lengths[lane] == stop}
            hidden, logits, trace = prefill_tile(t, tile, capture=bool(final), lane_ids=lanes)
            for row, lane in enumerate(lanes):
                if lane not in final:
                    continue
                output[lane] = (hidden[row, 0], logits[row, 0].argmax())
                for layer in TARGETS:
                    index[layer][lane] = trace[layer][1][row, -1]
        if set(output) != set(range(LANES)) or t.pool.lengths != lengths:
            raise ValueError("Each prompt must commit its exact final row")
        return DraftAnchor(t.pool.generation, torch.stack([output[i][0] for i in range(LANES)]),
                           torch.stack([output[i][1] for i in range(LANES)]),
                           {layer: torch.stack([rows[i] for i in range(LANES)]) for layer, rows in index.items()})

    def verify(self, anchor):
        proposed = self.draft.propose(anchor)
        if proposed.shape != (LANES, VERIFY):
            raise ValueError("The verify wave must include the anchor and five native draft tokens")
        self.target.begin(VERIFY)
        steps = [self.target.step(ids, capture=True) for ids in proposed.split(1, dim=1)]
        predictions = torch.cat([row[1].argmax(dim=-1) for row in steps], dim=1)
        consecutive = (predictions[:, :-1] == proposed[:, 1:]).long().cumprod(dim=1)
        counts = consecutive.sum(dim=1)
        accepted = tuple(counts.tolist())
        self.target.commit(tuple(n + 1 for n in accepted))
        return VerifyWave(proposed, accepted, self._anchor(steps, counts))
