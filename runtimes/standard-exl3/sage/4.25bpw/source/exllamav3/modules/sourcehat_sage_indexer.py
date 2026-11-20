"""Batch the existing pooled-index CUDA scorer across concurrent decode lanes."""

from itertools import groupby

import torch
import triton
import triton.language as tl


@triton.jit
def _expand(IDS, SEQ, OUT, K: tl.constexpr, KP: tl.constexpr,
            P: tl.constexpr, WIDTH: tl.constexpr, B: tl.constexpr, RAGGED: tl.constexpr = False):
    lane = tl.program_id(0)
    col = tl.program_id(1) * B + tl.arange(0, B)
    pos = tl.load(SEQ + lane) + 1
    used = tl.minimum(K, pos // P) * P if RAGGED else K * P
    pool = tl.load(IDS + lane * KP + col // P, col < used, -1)
    tail_len = pos % P
    tail_start = pos - tail_len
    tail_col = col - used
    value = tl.where(pool >= 0, pool * P + col % P, -1)
    value = tl.where((tail_col >= 0) & (tail_col < tail_len), tail_start + tail_col, value)
    tl.store(OUT + lane * WIDTH + col, value, col < WIDTH)


def pooled_indices(q, w, keys, block_table, cache_seqlens, max_count, *, k=512, p=4,
                   lane_counts=None, score_tile=32768, compact=False):
    from exllamav3.ext import exllamav3_ext as ext
    from exllamav3.modules.attention_fn.dsa_triton import _dsa_indexer_fewq_kernel

    lanes, heads, dims = q.shape
    epp = keys.shape[1]
    stride = score_tile if lane_counts is not None and not compact else triton.next_power_of_2(max_count)
    counts = (cache_seqlens + 1) // p
    scores = torch.full((lanes, stride), -float("inf"), dtype=torch.half, device=q.device)
    kp = triton.cdiv(k, 32) * 32
    width = triton.cdiv(k * p + p - 1, 32) * 32
    selected = torch.empty((lanes, kp), dtype=torch.int32, device=q.device)
    output = torch.empty((lanes, width), dtype=torch.int32, device=q.device)
    with torch.cuda.device(q.device):
        _dsa_indexer_fewq_kernel[(lanes, triton.cdiv(max_count, 128))](
            q, w, keys, scores, counts, lanes, cache_seqlens, counts, block_table, block_table.shape[1],
            H_i=heads, H_pad=max(triton.next_power_of_2(heads), 16), D_i=dims, S_stride=stride,
            compress_rate=p, scale=dims ** -.5 * heads ** -.5, BLOCK_N=128, MULTIROW=1, EPP=epp,
            num_warps=8, num_stages=2,
        )
        if lane_counts is None:
            ext.dsa_topk(scores[:, :max_count], selected, k, None, 0)
        else:
            # A short lane has its own threshold and tie order. Group only equal K.
            first = 0
            for count, lanes_at_k in groupby(min(k, n) for n in lane_counts):
                end = first + sum(1 for _ in lanes_at_k)
                if count:
                    view = selected[first:end, :triton.cdiv(count, 32) * 32]
                    dest = view if view.is_contiguous() else torch.empty_like(view, memory_format=torch.contiguous_format)
                    ext.dsa_topk(scores[first:end], dest, count, None, 0)
                    if dest is not view:
                        view.copy_(dest)
                first = end
        _expand[(lanes, triton.cdiv(width, 256))](selected, cache_seqlens, output, k, kp, p, width, 256,
                                                 RAGGED=lane_counts is not None)
    return output
