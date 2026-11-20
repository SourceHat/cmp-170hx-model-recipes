"""Keep Sage's pooled-key updates and their page addressing on the GPU."""

import torch
import triton
import triton.language as tl
from triton.language.extra.cuda import libdevice


@triton.jit(do_not_specialize=["width", "append"])
def _write_complete_pools(plane, pooled, ape, table, seq, width, append,
                          PAGE: tl.constexpr, HEAD: tl.constexpr):
    lane, slot = tl.program_id(0), tl.program_id(1)
    pos = tl.load(seq + lane)
    group = pos // 4 + slot
    if (group + 1) * 4 <= pos + append:
        tok = group * 4
        page = tl.load(table + lane * width + tok // PAGE)
        row = page * PAGE + tok % PAGE
        d = tl.arange(0, HEAD)
        base = plane + row * (2 * HEAD) + d
        k0 = tl.load(base).to(tl.float32)
        k1 = tl.load(base + 2 * HEAD).to(tl.float32)
        k2 = tl.load(base + 4 * HEAD).to(tl.float32)
        k3 = tl.load(base + 6 * HEAD).to(tl.float32)
        g0 = tl.load(base + HEAD).to(tl.float32) + tl.load(ape + d).to(tl.float32)
        g1 = tl.load(base + 3 * HEAD).to(tl.float32) + tl.load(ape + HEAD + d).to(tl.float32)
        g2 = tl.load(base + 5 * HEAD).to(tl.float32) + tl.load(ape + 2 * HEAD + d).to(tl.float32)
        g3 = tl.load(base + 7 * HEAD).to(tl.float32) + tl.load(ape + 3 * HEAD + d).to(tl.float32)
        m = tl.maximum(tl.maximum(g0, g1), tl.maximum(g2, g3))
        e0, e1 = libdevice.exp(g0 - m), libdevice.exp(g1 - m)
        e2, e3 = libdevice.exp(g2 - m), libdevice.exp(g3 - m)
        inv = tl.div_rn(1.0, ((e0 + e1) + e2) + e3)
        value = (((e0 * inv) * k0 + (e1 * inv) * k1) + (e2 * inv) * k2) + (e3 * inv) * k3
        pool_row = page * (PAGE // 4) + group % (PAGE // 4)
        tl.store(pooled + pool_row * HEAD + d, value)


def update_pool_on_device(layer, ape, table, lengths, append):
    plane = layer.get_idx()
    pool = layer.get_pool()
    with torch.cuda.device(plane.device):
        _write_complete_pools[(table.shape[0], (append + 3) // 4)](
            plane, pool, ape, table, lengths, table.shape[1], append,
            plane.shape[1], pool.shape[-1], num_warps=2, enable_fp_fusion=False,
        )
