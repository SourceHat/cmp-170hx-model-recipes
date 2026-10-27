"""Canonicalize a scaled EXL3 head for the native shared unquantized head."""
from collections.abc import Iterable

import torch


def dequantize_head(weight: torch.Tensor, scales: torch.Tensor,
                    dtype: torch.dtype, chunk_rows: int = 1024) -> torch.Tensor:
    if (weight.device.type != 'cpu' or scales.device.type != 'cpu'
            or weight.dtype != torch.float8_e4m3fn or weight.ndim != 2
            or scales.dtype not in (torch.uint8, torch.float8_e8m0fnu)
            or scales.shape != (weight.shape[0], weight.shape[1] // 32)
            or weight.shape[1] % 32 or dtype not in (torch.bfloat16, torch.float16, torch.float32)):
        raise ValueError('Unsupported scaled EXL3 head; require CPU E4M3 rows and UE8M0 groups of32')
    if not 1 <= chunk_rows <= 4096:
        raise ValueError('Head conversion requires a bounded row chunk')
    output = torch.empty(weight.shape, dtype=dtype, device='cpu')
    scale_bytes = scales.view(torch.uint8)
    for start in range(0, weight.shape[0], chunk_rows):
        end = min(start + chunk_rows, weight.shape[0])
        # UE8M0 bytes form IEEE fp32 exponent bits, as in the source row codec.
        bits = scale_bytes[start:end].to(torch.int32) << 23
        expanded = bits.contiguous().view(torch.float32).repeat_interleave(32, dim=1)
        decoded = weight[start:end].to(torch.float32) * expanded
        if not torch.isfinite(decoded).all():
            raise ValueError('Non-finite decoded EXL3 head')
        output[start:end].copy_(decoded)
    if not torch.isfinite(output).all():
        raise ValueError('EXL3 head overflows the native dtype')
    return output


def canonical_head_weights(weights: Iterable[tuple[str, torch.Tensor]],
                           dtype: torch.dtype) -> Iterable[tuple[str, torch.Tensor]]:
    head = None
    scales = None
    for name, value in weights:
        if name in ('head.weight', 'lm_head.weight'):
            if head is not None:
                raise ValueError('Duplicate target head weights')
            head = value
        elif name in ('head.scale', 'head.weight_scale', 'lm_head.scale', 'lm_head.weight_scale'):
            if scales is not None:
                raise ValueError('Duplicate target head scales')
            scales = value
        else:
            yield name, value
    if head is None:
        if scales is not None:
            raise ValueError('Target head scales without weights')
        return
    if scales is not None:
        head = dequantize_head(head, scales, dtype)
    elif head.dtype == torch.float8_e4m3fn:
        raise ValueError('FP8 target head lacks its scales')
    # The outer vision mapper expects the source spelling, not lm_head.*.
    yield 'head.weight', head
