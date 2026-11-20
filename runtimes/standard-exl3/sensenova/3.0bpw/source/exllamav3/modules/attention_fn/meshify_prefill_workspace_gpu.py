"""Experimental bounded head-group staging for the existing Q8 attention path."""

import torch
import triton
import triton.language as tl

from .meshify_prefill_workspace import workspace_layout
from .triton_paged import _get_h32, _qc_load_v, _rot_h32


WORKSPACE_STATS = {'calls': 0, 'fallbacks': 0, 'maximum_scratch_bytes': 0,
                   'head_group_passes': 0}


@triton.jit
def _stage_heads(k, v, ks, vs, kd, vd, table, lengths, h32,
                 pages_per_sequence, table_stride, append_length, head_offset,
                 KV_HEADS: tl.constexpr, GROUP_HEADS: tl.constexpr,
                 HEAD_DIM: tl.constexpr, HD_PAD: tl.constexpr,
                 PAGE_SIZE: tl.constexpr, ROWS: tl.constexpr):
    batch = tl.program_id(1)
    head = tl.program_id(2) % GROUP_HEADS
    plane = tl.program_id(2) // GROUP_HEADS
    row = tl.program_id(0) * ROWS + tl.arange(0, ROWS)
    total = tl.load(lengths + batch) + append_length
    valid = (row < total) & (row < pages_per_sequence * PAGE_SIZE)
    page = tl.load(table + batch * table_stride + row // PAGE_SIZE, mask=valid, other=0)
    physical = page * PAGE_SIZE + row % PAGE_SIZE
    columns = tl.arange(0, HD_PAD)
    if plane == 0:
        values = _qc_load_v(k, ks, physical, head_offset + head, columns, valid,
                            8, KV_HEADS, HEAD_DIM, HD_PAD)
    else:
        values = _qc_load_v(v, vs, physical, head_offset + head, columns, valid,
                            8, KV_HEADS, HEAD_DIM, HD_PAD)
    values = _rot_h32(values, h32, ROWS, HD_PAD)
    offset = (((batch * pages_per_sequence * PAGE_SIZE + row[:, None]) * GROUP_HEADS
               + head) * HEAD_DIM + columns[None, :])
    mask = (row < pages_per_sequence * PAGE_SIZE)[:, None] & (columns < HEAD_DIM)[None, :]
    if plane == 0:
        tl.store(kd + offset, values, mask=mask)
    else:
        tl.store(vd + offset, values, mask=mask)


def bounded_prefill(*, q, k_cache, v_cache, block_table, cache_seqlens, qc,
                    pre_appended_len, kv_heads, budget_bytes, causal=True,
                    softmax_scale=None, softcap=0.0, out=None, max_kv_len=None):
    from .triton_paged import paged_attn_triton_prefill

    if qc[2:] != (8, 8) or not causal:
        WORKSPACE_STATS['fallbacks'] += 1
        return None
    batch, query_length, query_heads, head_dim = q.shape
    if query_heads % kv_heads:
        return None
    pages_per_sequence = block_table.shape[1]
    if max_kv_len is not None:
        pages_per_sequence = min(pages_per_sequence,
                                 -(-(max_kv_len + pre_appended_len) // k_cache.shape[1]))
    plan = workspace_layout(batch, pages_per_sequence, k_cache.shape[0], kv_heads,
                            head_dim, budget_bytes, k_cache.shape[1])
    if plan is None:
        WORKSPACE_STATS['fallbacks'] += 1
        return None
    WORKSPACE_STATS['calls'] += 1
    WORKSPACE_STATS['maximum_scratch_bytes'] = max(WORKSPACE_STATS['maximum_scratch_bytes'], plan['bytes'])
    WORKSPACE_STATS['head_group_passes'] += kv_heads // plan['head_group']
    group = plan['head_group']
    shape = (plan['pages'], k_cache.shape[1], group, head_dim)
    kd = torch.empty(shape, dtype=torch.float16, device=q.device)
    vd = torch.empty_like(kd)
    table = block_table[:, :pages_per_sequence]
    identity = torch.arange(batch * pages_per_sequence, dtype=torch.int32,
                            device=q.device).view(batch, pages_per_sequence)
    result = out if out is not None else torch.empty_like(q)
    group_queries = query_heads // kv_heads * group
    h32 = _get_h32(q.device)
    for head in range(0, kv_heads, group):
        _stage_heads[(triton.cdiv(pages_per_sequence * k_cache.shape[1], 32), batch, group * 2)](
            k_cache, v_cache, qc[0], qc[1], kd, vd, table, cache_seqlens, h32,
            pages_per_sequence, table.stride(0), pre_appended_len, head,
            kv_heads, group, head_dim, triton.next_power_of_2(head_dim), k_cache.shape[1], 32,
            num_warps=4, num_stages=1)
        first = head * query_heads // kv_heads
        queries = q[:, :, first:first + group_queries, :]
        paged_attn_triton_prefill(
            q=queries, k=None, v=None, k_cache=kd, v_cache=vd, block_table=identity,
            cache_seqlens=cache_seqlens, causal=causal, softmax_scale=softmax_scale,
            softcap=softcap, pre_appended_len=pre_appended_len, max_kv_len=max_kv_len,
            out=result[:, :, first:first + group_queries, :])
    return result
