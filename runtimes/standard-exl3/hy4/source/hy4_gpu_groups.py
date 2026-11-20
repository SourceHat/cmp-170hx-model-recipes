"Group HY4's EXL3 expert rows entirely on the device."

import torch

from torch.nn import functional as F

import triton

import triton.language as tl

from decoder_prefix_probe import norm

from hy4_device_experts import DeviceExperts

from hy4_ops import latent_swiglu

from hy4_ops import routed_scores

@triton.jit
def reduce_bf16(src, dst, dim: tl.constexpr, topk: tl.constexpr, block: tl.constexpr):
    lane = tl.program_id(0)
    col = tl.program_id(1) * block + tl.arange(0, block)
    accum = tl.full((block,), 0, tl.bfloat16)
    for i in tl.static_range(topk):
        row = tl.load(src + (lane * topk + i) * dim + col, col < dim, 0)
        accum = (accum.to(tl.float32) + row.to(tl.float32)).to(tl.bfloat16)
    tl.store(dst + lane * dim + col, accum, col < dim)

def reduction(weighted):
    lanes, topk, dim = weighted.shape
    out = weighted.new_empty((lanes, dim))
    reduce_bf16[(lanes, triton.cdiv(dim, 256))](weighted.contiguous(), out, dim, topk, 256)
    return out

def group_plan(ids):
    lanes, topk = ids.shape
    n = lanes * topk
    pos = torch.arange(n, device=ids.device)
    lane, slot = pos // topk, pos % topk
    key = ids.flatten() * n + slot * lanes + lane
    permutation = key.argsort()
    selected = ids.flatten()[permutation]
    first = torch.cat((torch.ones_like(selected[:1], dtype=torch.bool), selected[1:] != selected[:-1]))
    group = first.long().cumsum(0) - 1
    first_pos = torch.where(first, pos, 0).cummax(0).values
    row = pos - first_pos
    destinations = torch.empty_like(pos).scatter_(0, permutation, group * lanes + row)
    choices = ids.new_full((n + 1,), -1)
    choices.scatter_(0, torch.where(first, group, n), selected)
    return destinations.reshape_as(ids), choices[:-1][None], permutation // topk, group, row

def prompt_group_plan(ids, n_experts, tile):
    tokens, topk = ids.shape
    n = tokens * topk
    pos = torch.arange(n, device=ids.device)
    permutation = ids.flatten().argsort(stable=True)
    selected = ids.flatten()[permutation]
    first = torch.cat((torch.ones_like(selected[:1], dtype=torch.bool), selected[1:] != selected[:-1]))
    begin = torch.where(first, pos, 0).cummax(0).values
    row = (pos - begin) % tile
    new_group = row == 0
    group = new_group.long().cumsum(0) - 1
    # Each expert can leave one partially filled tile at the end.
    cap = min(n, n_experts + n // tile)
    destinations = torch.empty_like(pos).scatter_(0, permutation, group * tile + row)
    choices = ids.new_full((cap + 1,), -1)
    choices.scatter_(0, torch.where(new_group, group, cap), selected)
    return destinations.reshape_as(ids), choices[:-1][None], permutation // topk, group, row

class GpuGroupedExperts(DeviceExperts):
    """Batch complete four-row expert tiles, including the original padding."""

    def multiply(self, name, rows, indices):
        b, su, sv = self.pointers[name]
        width = self.weights[name][0].out_features
        out = torch.zeros((*rows.shape[:2], width), dtype=torch.float32, device=rows.device)
        scratch = torch.empty_like(rows)
        for bits, choices in indices:
            self.mgemm(rows, b, out, su, scratch, sv, choices, None, bits, -1,
                       False, True, -1, -1, 0)
        return out

    def experts(self, latents, probs, ids):
        lanes, topk = ids.shape
        if lanes != 4 or topk != self.topk:
            raise ValueError("Use native HY4 four-lane decode tiles")
        return self.run_groups(latents, probs, ids, group_plan(ids), lanes)

    def run_groups(self, latents, probs, ids, plan, tile):
        destinations, choices, source, group, row = plan
        rate = self.bitrates[choices.clamp_min(0)]
        indices = [(k, choices.masked_fill(rate != k, -1)) for k in self.bits]
        tiles = torch.zeros((choices.shape[1], tile, latents.shape[-1]), device=latents.device, dtype=torch.float16)
        tiles[group, row] = latents[source].half()
        gu = self.multiply("gate_up", tiles, indices).bfloat16()
        hidden = latent_swiglu(gu, self.cfg.swiglu_limit).half().contiguous()
        down = self.multiply("down", hidden, indices).bfloat16().flatten(0, 1)
        order = ids.argsort(1)
        summed = (down[destinations.gather(1, order)] * probs.gather(1, order)[..., None]).to(latents.dtype)
        return reduction(summed)

    def routed(self, hidden, *, decode=False):
        def linear(v, name):
            return F.linear(v, self.fixed[name + ".weight"])

        cfg = self.cfg
        _, p, ids = routed_scores(hidden, self.fixed["gate.weight"], self.fixed["gate.e_score_correction_bias"],
                                  self.topk, cfg.routed_scaling_factor)
        tokens = hidden.flatten(0, 1)
        latents = linear(tokens, "routed_expert_down_proj")
        if decode:
            tile, plan = len(tokens), group_plan(ids)
        else:
            tile = 8 if len(tokens) <= 32 else 16
            plan = prompt_group_plan(ids, len(self.bitrates), tile)
        total = self.run_groups(latents, p, ids, plan, tile)
        routed = linear(total, "routed_expert_up_proj")
        shared = linear(F.silu(linear(tokens, "shared_experts.gate_proj")) * linear(tokens, "shared_experts.up_proj"),
                        "shared_experts.down_proj")
        return norm(routed + shared, self.fixed["combine_output_norm.weight"], cfg.rms_norm_eps).view_as(hidden)

    def prefill(self, hidden):
        return self.routed(hidden)

    def decode_subset(self, hidden, lanes):
        selected = hidden.index_select(0, lanes)
        result = self.routed(selected, decode=True)
        return torch.zeros_like(hidden).index_copy_(0, lanes, result)
