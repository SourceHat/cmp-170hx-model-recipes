"""Compute the native two-stream routing normalization in one GPU launch."""

import torch
import triton
import triton.language as tl
from triton.language.extra.cuda import libdevice


@triton.jit
def logsum2(a, b, PRECISE: tl.constexpr):
    m = tl.maximum(a, b)
    if PRECISE:
        return m + libdevice.log(libdevice.exp(a - m) + libdevice.exp(b - m))
    else:
        return m + tl.log(tl.exp(a - m) + tl.exp(b - m))


@triton.jit
def sinkhorn2_kernel(X, Y, ROWS, STRIDE: tl.constexpr, ITERATIONS: tl.constexpr,
                     BLOCK: tl.constexpr, PRECISE: tl.constexpr):
    row = tl.program_id(0) * BLOCK + tl.arange(0, BLOCK)
    ptr = X + row * STRIDE
    a = tl.load(ptr, row < ROWS, 0.)
    b = tl.load(ptr + 1, row < ROWS, 0.)
    c = tl.load(ptr + 2, row < ROWS, 0.)
    d = tl.load(ptr + 3, row < ROWS, 0.)
    for _ in range(ITERATIONS):
        x, y = logsum2(a, b, PRECISE), logsum2(c, d, PRECISE)
        a, b, c, d = a - x, b - x, c - y, d - y
        x, y = logsum2(a, c, PRECISE), logsum2(b, d, PRECISE)
        a, b, c, d = a - x, b - y, c - x, d - y
    ptr = Y + row * 4
    if PRECISE:
        tl.store(ptr, libdevice.exp(a), row < ROWS)
        tl.store(ptr + 1, libdevice.exp(b), row < ROWS)
        tl.store(ptr + 2, libdevice.exp(c), row < ROWS)
        tl.store(ptr + 3, libdevice.exp(d), row < ROWS)
    else:
        tl.store(ptr, tl.exp(a), row < ROWS)
        tl.store(ptr + 1, tl.exp(b), row < ROWS)
        tl.store(ptr + 2, tl.exp(c), row < ROWS)
        tl.store(ptr + 3, tl.exp(d), row < ROWS)


def sinkhorn2(logits, iterations, *, precise=True):
    assert logits.is_cuda and logits.dtype == torch.float32 and logits.shape[-2:] == (2, 2)
    src = logits.reshape(-1, 4)
    n = src.shape[0]
    out = torch.empty((n, 4), dtype=src.dtype, device=src.device)
    sinkhorn2_kernel[(triton.cdiv(n, 64),)](src, out, n, src.stride(0), iterations, 64, precise,
                                            num_warps=2, enable_fp_fusion=False)
    return out.view(logits.shape)
