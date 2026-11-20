"""Opt-in E4M3 byte kernels for the GLM indexer on SM80."""
import os

import torch
import triton
import triton.language as tl


FLAG = "MESHIFY_GLM_INDEXER_SM80"


def enabled(device):
    if os.environ.get(FLAG) != "1":
        return False
    device = torch.device(device)
    if device.type != "cuda":
        return False
    if torch.cuda.get_device_capability(device) != (8, 0):
        raise ValueError("The opted-in indexer fallback requires SM80")
    return True


@triton.jit
def encode_e4m3(x):
    bits = x.to(tl.float32).to(tl.int32, bitcast=True)
    sign = (bits >> 24) & 128
    magnitude = tl.minimum(tl.abs(x), 448.0)
    raw = magnitude.to(tl.float32).to(tl.int32, bitcast=True)
    # Retain three mantissa bits with round-to-nearest, ties-to-even.
    normal = ((raw + 0x7FFFF + ((raw >> 20) & 1)) >> 20) - 960
    sub_value = magnitude * 512.0
    sub_floor = sub_value.to(tl.int32)
    fraction = sub_value - sub_floor.to(tl.float32)
    sub = sub_floor + ((fraction > 0.5) | ((fraction == 0.5) & ((sub_floor & 1) != 0))).to(tl.int32)
    code = tl.where(magnitude < 0.015625, sub, normal)
    code = tl.where(x != x, 127, code)
    return (sign | code).to(tl.uint8)


@triton.jit
def decode_e4m3(byte):
    code = byte.to(tl.int32)
    exponent = (code >> 3) & 15
    mantissa = code & 7
    magnitude = tl.where(
        exponent == 0,
        mantissa.to(tl.float32) * 0.001953125,
        (8 + mantissa).to(tl.float32) * tl.exp2(exponent.to(tl.float32) - 10.0),
    )
    magnitude = tl.where((code & 127) == 127, float("nan"), magnitude)
    bits = magnitude.to(tl.int32, bitcast=True) | ((code & 128) << 24)
    return bits.to(tl.float32, bitcast=True)


@triton.jit
def _mqa_logits_kernel(
    Q, K, KS, W, START, END, TABLE, OUT,
    Q_STRIDE: tl.constexpr, K_STRIDE: tl.constexpr, KS_STRIDE: tl.constexpr,
    W_STRIDE: tl.constexpr, TABLE_STRIDE: tl.constexpr,
    N_KEYS: tl.constexpr, HEADS: tl.constexpr, BLOCK_H: tl.constexpr,
    PAGED: tl.constexpr, PAGE_SIZE: tl.constexpr, PAGE_BYTES: tl.constexpr,
    BLOCK_K: tl.constexpr,
):
    row = tl.program_id(0)
    keys = tl.program_id(1) * BLOCK_K + tl.arange(0, BLOCK_K)
    heads = tl.arange(0, BLOCK_H)
    dims = tl.arange(0, 128)
    if PAGED:
        end = tl.load(END + row)
        start = 0
        valid = (keys < end) & (keys < N_KEYS)
        page = tl.load(TABLE + row * TABLE_STRIDE + keys // PAGE_SIZE, mask=valid, other=0)
        key_offsets = page[None, :].to(tl.int64) * PAGE_BYTES + (keys[None, :] % PAGE_SIZE) * 128 + dims[:, None]
        scale_offsets = page.to(tl.int64) * (PAGE_BYTES // 4) + PAGE_SIZE * 32 + keys % PAGE_SIZE
    else:
        start = tl.load(START + row)
        end = tl.load(END + row)
        valid = (keys >= start) & (keys < end) & (keys < N_KEYS)
        key_offsets = keys[None, :] * K_STRIDE + dims[:, None]
        scale_offsets = keys * KS_STRIDE
    q_codes = tl.load(Q + row * Q_STRIDE + heads[:, None] * 128 + dims[None, :], mask=heads[:, None] < HEADS, other=0)
    k_codes = tl.load(K + key_offsets, mask=valid[None, :], other=0)
    q = decode_e4m3(q_codes).to(tl.bfloat16)
    k = decode_e4m3(k_codes).to(tl.bfloat16)
    products = tl.dot(q, k, allow_tf32=False)
    scale = tl.load(KS + scale_offsets, mask=valid, other=0.0)
    weight = tl.load(W + row * W_STRIDE + heads, mask=heads < HEADS, other=0.0)
    logits = tl.sum(tl.maximum(products, 0.0) * weight[:, None], axis=0) * scale
    logits = tl.where(valid, logits, -float("inf"))
    tl.store(OUT + row * N_KEYS + keys, logits, mask=keys < N_KEYS)


def _validate_q(q, weights, rank):
    values, scales = q
    if scales is not None or values.dtype != torch.float8_e4m3fn:
        raise ValueError("The SM80 indexer supports E4M3 Q with folded scales only")
    if values.ndim != rank or values.shape[-1] != 128 or values.shape[-2] not in (16, 32, 64):
        raise ValueError("Unsupported GLM indexer query layout")
    rows = values.numel() // (values.shape[-2] * 128)
    if weights.dtype != torch.float32 or weights.shape != (rows, values.shape[-2]):
        raise ValueError("Unsupported GLM indexer weight layout")
    if not values.is_contiguous() or not weights.is_contiguous():
        raise ValueError("The SM80 indexer requires contiguous query and weights")
    if values.device != weights.device:
        raise ValueError("Query and weights must share a device")
    return values, rows


def mqa_logits(q, kv, weights, cu_seqlen_ks, cu_seqlen_ke, clean_logits):
    values, rows = _validate_q(q, weights, 3)
    keys, scales = kv
    if (keys.dtype != torch.float8_e4m3fn or keys.ndim != 2 or keys.shape[1] != 128
            or keys.stride(-1) != 1 or scales.dtype != torch.float32 or scales.shape != (keys.shape[0],)):
        raise ValueError("Unsupported E4M3 key/scale workspace")
    for bounds in (cu_seqlen_ks, cu_seqlen_ke):
        if bounds.dtype != torch.int32 or bounds.shape != (rows,) or not bounds.is_contiguous():
            raise ValueError("Unsupported per-query key bounds")
    if any(x.device != values.device for x in (keys, scales, cu_seqlen_ks, cu_seqlen_ke)):
        raise ValueError("All indexer inputs must share a device")
    out = torch.empty((rows, keys.shape[0]), dtype=torch.float32, device=values.device)
    if rows and keys.shape[0]:
        _mqa_logits_kernel[(rows, triton.cdiv(keys.shape[0], 32))](
            values.view(torch.uint8), keys.view(torch.uint8), scales, weights,
            cu_seqlen_ks, cu_seqlen_ke, cu_seqlen_ks, out,
            Q_STRIDE=values.stride(0), K_STRIDE=keys.stride(0), KS_STRIDE=scales.stride(0),
            W_STRIDE=weights.stride(0), TABLE_STRIDE=0, N_KEYS=keys.shape[0],
            HEADS=values.shape[-2], BLOCK_H=max(32, values.shape[-2]), PAGED=False,
            PAGE_SIZE=1, PAGE_BYTES=0, BLOCK_K=32, num_warps=4,
        )
    return out


def paged_mqa_logits(q, kv_cache, weights, context_lens, block_tables, schedule_metadata,
                     max_model_len, clean_logits, indices=None):
    values, rows = _validate_q(q, weights, 4)
    if values.shape[1] != 1 or indices is not None:
        raise ValueError("The staged SM80 fallback supports ordinary decode only")
    if (kv_cache.dtype != torch.uint8 or kv_cache.ndim != 4 or kv_cache.shape[2:] != (1, 132)
            or kv_cache.stride(-1) != 1 or kv_cache.stride(0) % 4):
        raise ValueError("Unsupported GLM pooled-key cache layout")
    if context_lens.dtype != torch.int32 or context_lens.shape != (rows, 1) or not context_lens.is_contiguous():
        raise ValueError("Unsupported ordinary context lengths")
    if (block_tables.dtype != torch.int32 or block_tables.ndim != 2 or block_tables.shape[0] != rows
            or block_tables.stride(-1) != 1 or block_tables.shape[1] * kv_cache.shape[1] < max_model_len):
        raise ValueError("Unsupported or undersized ordinary block table")
    if any(x.device != values.device for x in (kv_cache, context_lens, block_tables)):
        raise ValueError("All indexer inputs must share a device")
    if type(max_model_len) is not int or max_model_len <= 0:
        raise ValueError("A positive bounded model length is required")
    out = torch.empty((rows, max_model_len), dtype=torch.float32, device=values.device)
    if rows:
        _mqa_logits_kernel[(rows, triton.cdiv(max_model_len, 32))](
            values.view(torch.uint8), kv_cache, kv_cache.view(torch.float32), weights,
            context_lens, context_lens, block_tables, out,
            Q_STRIDE=values.stride(0), K_STRIDE=0, KS_STRIDE=0,
            W_STRIDE=weights.stride(0), TABLE_STRIDE=block_tables.stride(0), N_KEYS=max_model_len,
            HEADS=values.shape[-2], BLOCK_H=max(32, values.shape[-2]), PAGED=True,
            PAGE_SIZE=kv_cache.shape[1], PAGE_BYTES=kv_cache.stride(0), BLOCK_K=32, num_warps=4,
        )
    return out


def paged_metadata(context_lens, block_size, num_sms, indices=None):
    if indices is not None or context_lens.ndim != 2 or context_lens.shape[1] != 1:
        raise ValueError("The staged SM80 fallback supports ordinary scheduling only")
    # The fallback assigns tiles directly and does not consume DeepGEMM metadata.
    return torch.zeros((1, 2), dtype=torch.int32, device=context_lens.device)
