"""BF16 NoPE-512 sparse attention for the bounded SM80 Apex AWQ profile."""
import json
import torch
from vllm.v1.attention.ops.meshify_triton_mla_sparse import triton_mla_sparse_attention


def sparse_nope_attention(q, cache, indices, scale, lengths=None):
    if q.dtype != torch.bfloat16 or cache.dtype != torch.bfloat16 or q.shape[-1] != 512 or cache.shape[-1] != 512:
        raise ValueError('The SM80 fallback requires BF16 NoPE-512 tensors')
    indices = indices.reshape(q.shape[0], 1, -1)
    if lengths is not None:
        positions = torch.arange(indices.shape[-1], device=indices.device)
        indices = indices.masked_fill(positions >= lengths.reshape(-1, 1, 1), -1)
    return triton_mla_sparse_attention(q, cache.reshape(-1, 1, 512), indices, scale, num_kv_splits=1)


def run_parity():
    generator = torch.Generator(device='cuda:0').manual_seed(1177)
    q = torch.randn((3, 4, 512), device='cuda:0', dtype=torch.bfloat16, generator=generator) * 0.2
    cache = torch.randn((64, 1, 512), device='cuda:0', dtype=torch.bfloat16, generator=generator) * 0.2
    indices = torch.arange(32, device='cuda:0', dtype=torch.int32).expand(3, 1, -1).clone()
    indices[1, :, 17:] = -1
    indices[2] = -1
    lengths = torch.tensor([32, 11, 0], device='cuda:0', dtype=torch.int32)
    actual = sparse_nope_attention(q, cache, indices, 512 ** -0.5, lengths)
    expected = torch.zeros_like(actual)
    for row, count in enumerate([32, 11, 0]):
        if count:
            values = cache[:count, 0].float()
            probabilities = torch.softmax(q[row].float() @ values.T * 512 ** -0.5, dim=-1)
            expected[row] = (probabilities @ values).to(torch.bfloat16)
    if not torch.isfinite(actual).all() or not torch.allclose(actual, expected, atol=0.003, rtol=0.03):
        raise ValueError('SM80 sparse NoPE numerical parity failed')
    print(json.dumps(dict(SM80_sparse_NoPE_parity=True, cases=3,
                         max_absolute_error=(actual - expected).abs().max().item(), GPU_index=0)), flush=True)
    del q, cache, indices, lengths, actual, expected
    torch.cuda.empty_cache()
