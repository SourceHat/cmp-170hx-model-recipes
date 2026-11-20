'Portable row storage and lookup for the published HY4 Engram tables.'

import numpy as np

import torch

FORMAT = "hy4-engram-e4m3-bf16-scale-v1"

def e4m3_lut(device):
    # Byte addressing also works on CUDA devices without native FP8 tensor operations.
    return torch.arange(256, dtype=torch.uint8).view(torch.float8_e4m3fn).bfloat16().to(device)

def hash_parameters(vocab_sizes, map_size, ngram_size, seed, layer_id, device):
    """Compute the immutable per-layer hash factors and global row offsets once."""
    sizes = torch.tensor([size for order in vocab_sizes for size in order], dtype=torch.long, device=device)
    half_bound = max(1, np.iinfo(np.int64).max // map_size // 2)
    rng = np.random.default_rng(seed + 10007 * layer_id)
    drawn = rng.integers(0, half_bound, size=ngram_size, dtype=np.int64)
    multipliers = torch.tensor((drawn * 2 + 1).tolist(), dtype=torch.long, device=device)
    return sizes, sizes.cumsum(0) - sizes, multipliers

def hash_rows(ngrams, lookup, pad_id, sizes, offsets, multipliers, heads_per_order):
    """Return row IDs in n-gram-major order in the unsharded table."""
    if (ngrams.shape[-1] != multipliers.numel() or len(sizes) != (multipliers.numel() - 1) * heads_per_order or
            sizes.shape != offsets.shape or not 0 <= pad_id < len(lookup)):
        raise ValueError("Engram token and hash plan geometry disagree")
    compressed = lookup[ngrams.clamp_max(len(lookup) - 1)]
    compressed = torch.where(ngrams < len(lookup), compressed, lookup[pad_id])
    mixed = compressed.long() * multipliers
    result = []
    acc = mixed[..., 0]
    for i in range(1, mixed.shape[-1]):
        start = (i - 1) * heads_per_order
        stop = start + heads_per_order
        acc = torch.bitwise_xor(acc, mixed[..., i])
        result.append(acc.unsqueeze(-1).remainder(sizes[start:stop]) + offsets[start:stop])
    return torch.cat(result, dim=-1)

def ngram_tokens(input_ids, positions, ngram_size, pad_id, history=None):
    """Build a chunk's n-grams from its retained prefix without crossing document boundaries."""
    if input_ids.ndim != 2 or input_ids.shape != positions.shape or not input_ids.shape[1] or ngram_size < 2:
        raise ValueError("Expected aligned token and position matrices")
    batch, length = input_ids.shape
    prior = ngram_size - 1
    if history is not None:
        if history.ndim != 2 or history.shape[0] != batch or history.shape[1] > prior:
            raise ValueError("Unexpected retained Engram prefix")
        prefix = torch.nn.functional.pad(history, (prior - history.shape[1], 0), value=pad_id)
    else:
        prefix = input_ids.new_full((batch, prior), pad_id)
    extended = torch.cat((prefix, input_ids), dim=-1)
    shifted = [input_ids]
    for offset in range(1, ngram_size):
        shifted.append(torch.where(positions >= offset, extended[:, prior - offset:prior - offset + length], pad_id))
    return torch.stack(shifted, dim=-1)
