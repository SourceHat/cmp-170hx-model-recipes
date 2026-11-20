'Short-batch HY4 residual stream gates and RMS normalization.'

import torch

import triton

import triton.language as tl

@triton.jit
def partial_gate(X, FN, SCRATCH, N: tl.constexpr, PARTS: tl.constexpr, B: tl.constexpr):
    lane, part, out = tl.program_id(0), tl.program_id(1), tl.program_id(2)
    i = part * B + tl.arange(0, B)
    x = tl.load(X + lane * N + i, i < N, 0).to(tl.float32)
    if out < 8:
        y = tl.load(FN + out * N + i, i < N, 0)
    else:
        y = x
    tl.store(SCRATCH + (lane * 9 + out) * PARTS + part, tl.sum(x * y))

@triton.jit
def finish_gate(SCRATCH, BASE, SCALE, GATE, PARTS: tl.constexpr, N: tl.constexpr,
                EPS: tl.constexpr, GATE_EPS: tl.constexpr, MAG: tl.constexpr, P: tl.constexpr):
    lane = tl.program_id(0)
    out, i = tl.arange(0, 8), tl.arange(0, P)
    sq = tl.load(SCRATCH + (lane * 9 + 8) * PARTS + i, i < PARTS, 0)
    norm = tl.rsqrt(tl.sum(sq) / N + EPS)
    logits = tl.load(SCRATCH + (lane * 9 + out[:, None]) * PARTS + i[None, :], i[None, :] < PARTS, 0)
    value = tl.sum(logits, 1) * norm * tl.load(SCALE + out // 4) + tl.load(BASE + out)
    gate = tl.sigmoid(value)
    tl.store(GATE + lane * 8 + out, tl.where(out < 4, gate, gate * MAG) + GATE_EPS)

@triton.jit
def apply_gate(X, GATE, W, V, WIDTH: tl.constexpr, EPS: tl.constexpr, B: tl.constexpr):
    lane = tl.program_id(0)
    i = tl.arange(0, B)
    x = tl.full((B,), 0., tl.float32)
    for s in tl.static_range(4):
        g = tl.load(GATE + lane * 8 + s)
        stream = tl.load(X + (lane * 4 + s) * WIDTH + i, i < WIDTH, 0).to(tl.float32)
        x += g * stream
    x = x.to(tl.bfloat16).to(tl.float32)
    z = (x * tl.rsqrt(tl.sum(x * x) / WIDTH + EPS)).to(tl.bfloat16).to(tl.float32)
    w = tl.load(W + i, i < WIDTH, 0).to(tl.float32)
    tl.store(V + lane * WIDTH + i, z * w, i < WIDTH)

@triton.jit
def mix(X, V, GATE, Y, WIDTH: tl.constexpr, B: tl.constexpr):
    lane, s = tl.program_id(0), tl.program_id(1)
    i = tl.program_id(2) * B + tl.arange(0, B)
    idx = (lane * 4 + s) * WIDTH + i
    a = tl.load(X + idx, i < WIDTH, 0).to(tl.float32)
    b = tl.load(V + lane * WIDTH + i, i < WIDTH, 0).to(tl.float32)
    g = tl.load(GATE + lane * 8 + 4 + s)
    tl.store(Y + idx, a + b * g, i < WIDTH)

def branch(x, hc, weights, cfg):
    n, _, count, width = x.shape
    total = count * width
    part = triton.cdiv(total, 1024)
    buf = torch.empty((n, 9, part), device=x.device, dtype=torch.float32)
    gates = torch.empty((n, 8), device=x.device, dtype=torch.float32)
    y = torch.empty((n, 1, width), device=x.device, dtype=torch.bfloat16)
    partial_gate[(n, part, 9)](x, hc.fn, buf, total, part, 1024, num_warps=4)
    finish_gate[(n,)](buf, hc.base, hc.scale, gates, part, total,
                       cfg.rms_norm_eps, cfg.hc_eps, cfg.hc_magnitude, triton.next_power_of_2(part),
                       num_warps=4, enable_fp_fusion=False)
    apply_gate[(n,)](x, gates, weights, y, width, cfg.rms_norm_eps, triton.next_power_of_2(width),
                     num_warps=8, enable_fp_fusion=False)
    return gates, y

def write(x, value, gates):
    y = torch.empty_like(x)
    width = x.shape[-1]
    mix[(x.shape[0], 4, triton.cdiv(width, 256))](x, value, gates, y, width, 256, enable_fp_fusion=False)
    return y
