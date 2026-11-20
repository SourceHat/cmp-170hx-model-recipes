'Pack and reduce short HY4 expert batches with a few GPU launches.'

import torch

from torch.nn import functional as F

import triton

import triton.language as tl

from decoder_prefix_probe import norm

from hy4_gpu_groups import GpuGroupedExperts

from hy4_ops import routed_scores

@triton.jit
def greater(a, b):
    return tl.maximum(a, b)

@triton.jit
def plan_routes(IDS, PROBS, BITS, SOURCE, CHOICES, DEST, WEIGHTS,
                LANES: tl.constexpr, TOP: tl.constexpr, BLOCK: tl.constexpr,
                RATES: tl.constexpr, FILTER: tl.constexpr = False):
    n: tl.constexpr = LANES * TOP
    row = tl.arange(0, BLOCK)
    e = tl.load(IDS + row, row < n, 1 << 20).to(tl.int32)
    if FILTER:
        e = tl.where(e < 0, 1 << 20, e)
    key = e * n + row % TOP * LANES + row // TOP
    key = tl.sort(key, descending=False)
    e = key // n
    lane = key % LANES
    slot = key % n // LANES
    prev = tl.gather(e, tl.maximum(row - 1, 0), 0)
    valid = row < n
    if FILTER:
        valid &= e < (1 << 20)
    start = ((row == 0) | (prev != e)) & valid
    group = tl.cumsum(start.to(tl.int32), 0) - 1
    first = tl.associative_scan(tl.where(start, row, 0), 0, greater)
    within = row - first
    position = group * LANES + within
    tl.store(SOURCE + position, lane, valid)
    bits = tl.load(BITS + e, start, -1)
    for i in tl.static_range(len(RATES)):
        tl.store(CHOICES + i * n + group, e, start & (bits == RATES[i]))
    weight = tl.load(PROBS + lane * TOP + slot, valid, 0.)
    for i in tl.static_range(LANES):
        mine = valid & (lane == i)
        order = tl.cumsum(mine.to(tl.int32), 0) - 1
        tl.store(DEST + i * TOP + order, position, mine)
        tl.store(WEIGHTS + i * TOP + order, weight, mine)

@triton.jit
def pack_input(LATENT, SOURCE, TILES, WIDTH: tl.constexpr, BLOCK: tl.constexpr):
    row, col = tl.program_id(0), tl.program_id(1) * BLOCK + tl.arange(0, BLOCK)
    src = tl.load(SOURCE + row)
    x = tl.load(LATENT + tl.maximum(src, 0) * WIDTH + col, (src >= 0) & (col < WIDTH), 0.)
    tl.store(TILES + row * WIDTH + col, x.to(tl.float16), col < WIDTH)

@triton.jit
def activate(GU, ACTIVE, WIDTH: tl.constexpr, LIMIT: tl.constexpr, BLOCK: tl.constexpr):
    row, col = tl.program_id(0), tl.program_id(1) * BLOCK + tl.arange(0, BLOCK)
    g = tl.load(GU + row * (2 * WIDTH) + col, col < WIDTH, 0.).to(tl.bfloat16).to(tl.float32)
    up = tl.load(GU + row * (2 * WIDTH) + WIDTH + col, col < WIDTH, 0.).to(tl.bfloat16).to(tl.float32)
    g = tl.minimum(g, LIMIT)
    up = tl.minimum(tl.maximum(up, -LIMIT), LIMIT)
    gate = (g * tl.sigmoid(g)).to(tl.bfloat16).to(tl.float32)
    y = (gate * up).to(tl.bfloat16).to(tl.float16)
    tl.store(ACTIVE + row * WIDTH + col, y, col < WIDTH)

@triton.jit
def reduce(ROWS, DEST, WEIGHTS, OUT, WIDTH: tl.constexpr, TOP: tl.constexpr, BLOCK: tl.constexpr,
           FILTER: tl.constexpr = False):
    lane, col = tl.program_id(0), tl.program_id(1) * BLOCK + tl.arange(0, BLOCK)
    total = tl.full((BLOCK,), 0, tl.bfloat16)
    for k in tl.static_range(TOP):
        row = tl.load(DEST + lane * TOP + k)
        p = tl.load(WEIGHTS + lane * TOP + k)
        valid = col < WIDTH
        if FILTER:
            valid &= row >= 0
        v = tl.load(ROWS + tl.maximum(row, 0) * WIDTH + col, valid, 0).to(tl.bfloat16).to(tl.float32)
        scaled = (v * p).to(tl.bfloat16).to(tl.float32)
        total = (total.to(tl.float32) + scaled).to(tl.bfloat16)
    tl.store(OUT + lane * WIDTH + col, total, col < WIDTH)

class FusedDecodeExperts(GpuGroupedExperts):
    def experts(self, latents, probs, ids, *, filtered=False):
        lanes, top = ids.shape
        n = lanes * top
        width = latents.shape[-1]
        device = latents.device
        picks = ids.new_full((len(self.bits), n), -1)
        source = torch.full((n * lanes,), -1, device=device, dtype=torch.int32)
        dest = (torch.full((n,), -1, device=device, dtype=torch.int32) if filtered else
                torch.empty(n, device=device, dtype=torch.int32))
        weights = (torch.zeros(n, device=device, dtype=torch.float32) if filtered else
                   torch.empty(n, device=device, dtype=torch.float32))
        plan_routes[(1,)](ids, probs, self.bitrates, source, picks, dest, weights,
                           lanes, top, triton.next_power_of_2(n), tuple(self.bits), FILTER=filtered, num_warps=2)
        tiles = torch.empty((n, lanes, width), device=device, dtype=torch.float16)
        pack_input[(n * lanes, triton.cdiv(width, 256))](latents, source, tiles, width, 256)
        indices = [(rate, picks[i:i+1]) for i, rate in enumerate(self.bits)]
        gate_up = self.multiply("gate_up", tiles, indices)
        middle = gate_up.shape[-1] // 2
        hidden = torch.empty((n, lanes, middle), device=device, dtype=torch.float16)
        activate[(n * lanes, triton.cdiv(middle, 256))](gate_up, hidden, middle,
                                                        float(self.cfg.swiglu_limit), 256,
                                                        enable_fp_fusion=False)
        down = self.multiply("down", hidden, indices)
        output = torch.empty_like(latents)
        reduce[(lanes, triton.cdiv(width, 256))](down, dest, weights, output, width, top, 256,
                                                FILTER=filtered, enable_fp_fusion=False)
        return output

    def decode(self, hidden):
        def linear(x, name):
            return F.linear(x, self.fixed[name + ".weight"])

        cfg = self.cfg
        x = hidden[:, 0]
        _, p, ids = routed_scores(hidden, self.fixed["gate.weight"], self.fixed["gate.e_score_correction_bias"],
                                  self.topk, cfg.routed_scaling_factor)
        result = self.experts(linear(x, "routed_expert_down_proj"), p, ids)
        routed = linear(result, "routed_expert_up_proj")
        shared = linear(F.silu(linear(x, "shared_experts.gate_proj")) * linear(x, "shared_experts.up_proj"),
                        "shared_experts.down_proj")
        return norm(routed + shared, self.fixed["combine_output_norm.weight"], cfg.rms_norm_eps).unsqueeze(1)

    __call__ = decode
