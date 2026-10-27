"""NVMe-backed Engram embedding for bounded-memory eager V4.1 validation."""
import os

import torch
from torch import nn

from vllm.config import get_current_vllm_config
from vllm.distributed import (get_tensor_model_parallel_rank,
                              get_tensor_model_parallel_world_size,
                              tensor_model_parallel_all_gather)
from vllm.model_executor.utils import set_weight_attrs
from vllm.triton_utils import tl, triton
from vllm.v1.attention.ops.fp8_sm80 import _decode_fp8_f32

from v41_disk_rows import DiskRows


@triton.jit
def decode_rows(values, scales, output, rows, dim: tl.constexpr):
    row = tl.program_id(0) * 16 + tl.arange(0, 16)
    column = tl.arange(0, dim)
    raw = tl.load(values + row[:, None] * dim + column[None, :],
                  mask=row[:, None] < rows, other=0)
    scale = tl.load(scales + row[:, None] * (dim // 32) + column[None, :] // 32,
                    mask=row[:, None] < rows, other=0)
    scale = (scale.to(tl.int32) << 23).to(tl.float32, bitcast=True)
    decoded = _decode_fp8_f32(raw, False) * scale
    tl.store(output + row[:, None] * dim + column[None, :], decoded.to(tl.bfloat16),
             mask=row[:, None] < rows)


def source_loader(param, loaded_weight):
    if tuple(loaded_weight.shape) != param.meshify_source_shape:
        raise ValueError('Loaded Engram tensor differs from the pinned geometry')
    if loaded_weight.dtype != param.meshify_source_dtype:
        raise ValueError('Loaded Engram tensor dtype differs')
    # The original table stays on disk; only requested raw rows enter RAM/VRAM.
    param.meshify_source_loaded = True


class DiskParallelEngramEmbedding(nn.Module):
    def __init__(self, num_embeddings, dim, head_sizes, block_size=32,
                 cpu_offload=False, *, checkpoint_prefix):
        super().__init__()
        config = get_current_vllm_config()
        if not config.model_config.enforce_eager:
            raise ValueError('Disk Engram requires --enforce-eager; captured host lookups are invalid')
        if block_size != 32 or dim != 256 or not head_sizes or any(n <= 0 for n in head_sizes):
            raise ValueError('Unsupported pinned Engram geometry')
        if sum(head_sizes) > num_embeddings:
            raise ValueError('Engram head buckets exceed the table')
        self.num_embeddings, self.dim, self.block_size = num_embeddings, dim, block_size
        self.tp_size = get_tensor_model_parallel_world_size()
        rank = get_tensor_model_parallel_rank()
        self.n_hash_cols = len(head_sizes)
        self.part_n_hash_cols = (self.n_hash_cols + self.tp_size - 1) // self.tp_size
        self.head_start = rank * self.part_n_hash_cols
        self.vocab_start_idx = sum(head_sizes[:self.head_start])
        self.vocab_end_idx = sum(head_sizes[:self.head_start + self.part_n_hash_cols])
        self.part_num_embeddings = self.vocab_end_idx - self.vocab_start_idx
        self.cpu_offload = True
        cache_mib = int(os.environ.get('MESHIFY_V41_ENGRAM_RAM_CACHE_MIB', '64'))
        if not 0 <= cache_mib <= 256:
            raise ValueError('Engram row cache exceeds the initial host admission budget')
        self.rows = DiskRows(os.environ['MESHIFY_V41_ENGRAM_DIRECTORY'], checkpoint_prefix,
                             num_embeddings, dim, cache_bytes=cache_mib * 1024**2)
        self.weight = nn.Parameter(torch.empty((0, dim), device='cpu',
                                               dtype=torch.float8_e4m3fn), requires_grad=False)
        self.weight_scale_inv = nn.Parameter(torch.empty((0, dim // block_size), device='cpu',
                                                         dtype=torch.uint8), requires_grad=False)
        for param, shape, dtype in (
                (self.weight, (num_embeddings, dim), torch.float8_e4m3fn),
                (self.weight_scale_inv, (num_embeddings, dim // block_size), torch.float8_e8m0fnu)):
            set_weight_attrs(param, {'weight_loader':source_loader, 'meshify_source_shape':shape,
                                    'meshify_source_dtype':dtype, 'meshify_source_loaded':False})

    def lookup(self, indices, out, background=False):
        if not self.weight.meshify_source_loaded or not self.weight_scale_inv.meshify_source_loaded:
            raise RuntimeError('Engram source loader did not verify both table components')
        if indices.ndim != 2 or indices.shape[1] != self.n_hash_cols:
            raise ValueError('Engram hash columns differ from the rank layout')
        if tuple(out.shape) != (indices.shape[0], self.part_n_hash_cols, self.dim):
            raise ValueError('Engram output shape differs')
        end = min(self.head_start + self.part_n_hash_cols, self.n_hash_cols)
        selected = indices[:, self.head_start:end].to('cpu', dtype=torch.int64).tolist()
        packed_rows = []
        for row in selected:
            packed_rows.extend(n if self.vocab_start_idx <= n < self.vocab_end_idx else -1 for n in row)
            packed_rows.extend([-1] * (self.part_n_hash_cols - len(row)))
        if not packed_rows:
            return
        values, scales = self.rows.gather(packed_rows)
        values = torch.frombuffer(values, dtype=torch.uint8).pin_memory().to(indices.device, non_blocking=True)
        scales = torch.frombuffer(scales, dtype=torch.uint8).pin_memory().to(indices.device, non_blocking=True)
        decode_rows[((len(packed_rows) + 15) // 16,)](values, scales, out,
                                                   rows=len(packed_rows), dim=self.dim)

    def forward(self, indices):
        out = torch.empty((indices.shape[0], self.part_n_hash_cols, self.dim),
                          dtype=torch.bfloat16, device=indices.device)
        self.lookup(indices, out)
        if self.tp_size > 1:
            out = tensor_model_parallel_all_gather(out, dim=1)
        return out[:, :self.n_hash_cols].flatten(1)
