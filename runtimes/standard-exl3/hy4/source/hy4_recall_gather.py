'Read paged FP8 keys and their scales in one launch.'

from functools import cache

import torch

import triton

import triton.language as tl

@cache
def fp8_lut(device):
    bits = torch.arange(256, dtype=torch.int16, device=device).to(torch.uint8)
    return bits.view(torch.float8_e4m3fn).half()

@triton.jit
def _read(BITS, SCALES, PAGE_IDS, OFFSETS, LUT, KEYS, WEIGHTS,
          N: tl.constexpr, STRIDE: tl.constexpr, D: tl.constexpr, B: tl.constexpr):
    lane = tl.program_id(0)
    k = tl.program_id(1) * B + tl.arange(0, B)
    d = tl.arange(0, D)
    valid = k < N
    page = tl.load(PAGE_IDS + lane * N + k, valid, 0)
    offset = tl.load(OFFSETS + k, valid, 0)
    row = page * STRIDE + offset
    bits = tl.load(BITS + row[:, None] * D + d[None, :], valid[:, None], 0).to(tl.int32)
    decoded = tl.load(LUT + bits)
    tl.store(KEYS + (lane * N + k[:, None]) * D + d[None, :], decoded, valid[:, None])
    tl.store(WEIGHTS + lane * N + k, tl.load(SCALES + row, valid, 0), valid)

def gather(index, pages, offsets):
    lanes, groups = pages.shape
    width = index.bits.shape[-1]
    keys = torch.empty((lanes, groups, width), device=pages.device, dtype=torch.half)
    scales = torch.empty((lanes, groups), device=pages.device, dtype=index.scales.dtype)
    _read[(lanes, triton.cdiv(groups, 16))](index.bits, index.scales, pages, offsets,
                                          fp8_lut(pages.device), keys, scales,
                                          groups, index.stride, width, 16, num_warps=4)
    return keys, scales
