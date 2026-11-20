'Keep the four HY4 evaluation lanes occupied without changing the sampler.'

from collections import defaultdict

from itertools import groupby

import torch

from torch.nn import functional as F

from decoder_prefix_probe import norm

from hy4_chunked_prefill import PROMPT_TILE

from hy4_chunked_prefill import prefill_tile

from hy4_ops import latent_swiglu

from hy4_ops import routed_scores

from hy4_shared_pool import LANES

def route_rows(ids):
    # The reference uses where(mask.T), which orders each expert by slot, then lane.
    return sorted((expert, slot, lane)
                  for lane, row in enumerate(ids) for slot, expert in enumerate(row))

def grouped_forward(self, x):
    cfg = self.cfg
    if x.shape[:2] != (LANES, 1) or x.dtype != torch.bfloat16:
        raise ValueError("Use four native BF16 decode rows")

    def linear(v, name):
        return F.linear(v, self.fixed[name + ".weight"])

    _, p, ids = routed_scores(x, self.fixed["gate.weight"], self.fixed["gate.e_score_correction_bias"],
                              cfg.num_experts_per_tok, cfg.routed_scaling_factor)
    routes = route_rows(ids.tolist())
    lookup = torch.tensor([(s, r) for _, s, r in routes], device=x.device)
    x = x[:, 0]
    latents = linear(x, "routed_expert_down_proj")
    total = torch.zeros_like(latents)
    start = 0
    for expert, group in groupby(routes, key=lambda entry: entry[0]):
        count = sum(1 for _ in group)
        slot, lane = lookup[start:start + count].unbind(1)
        start += count
        tile = F.pad(latents[lane], (0, 0, 0, LANES - count)).half().contiguous()
        g = self.matrix(expert, "gate_up").forward(tile, {}).bfloat16()
        v = latent_swiglu(g, cfg.swiglu_limit).half().contiguous()
        result = self.matrix(expert, "down").forward(v, {})[:count].bfloat16()
        total[lane] = total[lane] + (result * p[lane, slot, None]).to(latents.dtype)
    routed = linear(total, "routed_expert_up_proj")
    shared = linear(F.silu(linear(x, "shared_experts.gate_proj")) * linear(x, "shared_experts.up_proj"),
                    "shared_experts.down_proj")
    return norm(routed + shared, self.fixed["combine_output_norm.weight"], cfg.rms_norm_eps).unsqueeze(1)

def prefill_requests(target, prompts):
    lengths = {lane: len(ids) for lane, ids in prompts.items()}
    logits = {}
    for start in range(0, max(lengths.values()), PROMPT_TILE):
        groups = defaultdict(list)
        for lane, length in sorted(lengths.items()):
            if length > start:
                groups[min(PROMPT_TILE, length - start)].append(lane)
        for width, lanes in groups.items():
            stop = start + width
            tile = torch.stack([prompts[lane][start:stop] for lane in lanes])
            _, out, _ = prefill_tile(target, tile, lane_ids=tuple(lanes))
            for i, lane in enumerate(lanes):
                if stop == lengths[lane]:
                    logits[lane] = out[i, 0].clone()
    if set(logits) != prompts.keys() or any(target.pool.lengths[lane] != n for lane, n in lengths.items()):
        raise ValueError("Refill must commit exactly the new request's prompt")
    return logits

def release(target, lane):
    if target.trial is not None or target.pool.pending is not None:
        raise ValueError("Retire a lane between complete target steps")
    for block in target.blocks:
        a = block.attention
        with torch.cuda.device(block.device):
            if block.sparse:
                a.index.lengths[lane] = 0
                a.index.partial[lane].zero_()
                a.index.first[lane] = 0
            else:
                a.cache.release(lane)
    target.pool.release(lane)
    target.tail[lane].fill_(target.cfg.engram_pad_id)
