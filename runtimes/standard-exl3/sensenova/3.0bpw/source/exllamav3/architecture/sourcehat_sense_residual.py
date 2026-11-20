"""Fuse the two-stream BF16 residual mix without changing its rounding points."""

import torch
import triton
import triton.language as tl


@triton.jit
def _merge_two(R, Y, P, M, OUT, WIDTH: tl.constexpr, BLOCK: tl.constexpr):
    row = tl.program_id(0)
    d = tl.program_id(1) * BLOCK + tl.arange(0, BLOCK)
    valid = d < WIDTH
    a = tl.load(R + (2 * row) * WIDTH + d, valid, 0).to(tl.float32)
    b = tl.load(R + (2 * row + 1) * WIDTH + d, valid, 0).to(tl.float32)
    v = tl.load(Y + row * WIDTH + d, valid, 0).to(tl.float32)
    for i in tl.static_range(2):
        c0 = tl.load(M + 4 * row + 2 * i).to(tl.bfloat16).to(tl.float32)
        c1 = tl.load(M + 4 * row + 2 * i + 1).to(tl.bfloat16).to(tl.float32)
        scale = tl.load(P + 2 * row + i).to(tl.bfloat16).to(tl.float32)
        old = (a * c0 + b * c1).to(tl.bfloat16).to(tl.float32)
        update = (v * scale).to(tl.bfloat16).to(tl.float32)
        tl.store(OUT + (2 * row + i) * WIDTH + d, old + update, valid)


def merge_two(residual, branch, post, mix):
    width = residual.shape[-1]
    output = torch.empty_like(residual)
    block = 512
    _merge_two[(residual.numel() // (2 * width), triton.cdiv(width, block))](
        residual, branch, post, mix, output, width, block, enable_fp_fusion=False,
    )
    return output


@triton.jit
def _add_branch(MIXED, Y, P, OUT, WIDTH: tl.constexpr, BLOCK: tl.constexpr):
    row = tl.program_id(0)
    d = tl.program_id(1) * BLOCK + tl.arange(0, BLOCK)
    valid = d < WIDTH
    mixed = tl.load(MIXED + row * WIDTH + d, valid, 0).to(tl.float32)
    update = tl.load(Y + (row // 2) * WIDTH + d, valid, 0).to(tl.float32)
    scale = tl.load(P + row).to(tl.bfloat16).to(tl.float32)
    update = (update * scale).to(tl.bfloat16).to(tl.float32)
    tl.store(OUT + row * WIDTH + d, mixed + update, valid)


def merge_add(residual, branch, post, mix):
    # Keep cuBLAS's batched accumulation and the existing BF16 boundaries.
    mixed = torch.matmul(mix.to(torch.bfloat16), residual)
    result = torch.empty_like(mixed)
    width = residual.shape[-1]
    block = 512
    _add_branch[(residual.numel() // width, triton.cdiv(width, block))](
        mixed, branch, post, result, width, block, enable_fp_fusion=False,
    )
    return result


def install(*, solo_only=False, mixed=False):
    from exllamav3.architecture import sensenova_loop

    eager = sensenova_loop.merge

    def fused(residual, branch, post, mix):
        if (residual.is_cuda and residual.dtype == branch.dtype == torch.bfloat16
                and residual.shape[-2] == 2 and all(t.is_contiguous() for t in (residual, branch, post, mix))):
            if residual.numel() == 2 * residual.shape[-1] or not (solo_only or mixed):
                return merge_two(residual, branch, post, mix)
            if mixed:
                return merge_add(residual, branch, post, mix)
        return eager(residual, branch, post, mix)

    sensenova_loop.merge = fused
    return eager
