'Build all sixteen Engram row IDs for a decode token in one GPU launch.'

import torch

import triton

import triton.language as tl

@triton.jit
def lookup(TAB, tok, pad: tl.constexpr, count: tl.constexpr):
    return tl.load(TAB + tl.where((tok >= 0) & (tok < count), tok, pad)).to(tl.int64)

@triton.jit
def decode_hash(IDS, TAIL, SLOTS, TAB, SIZES, OFFSETS, FACTORS, ROWS, VALID,
                PAD: tl.constexpr, VOCAB: tl.constexpr):
    lane = tl.program_id(0)
    cols = tl.arange(0, 16)
    pos = tl.load(SLOTS + lane)
    tok = tl.load(IDS + lane)
    prev = tl.where(pos >= 1, tl.load(TAIL + 2 * lane + 1), PAD)
    prev2 = tl.where(pos >= 2, tl.load(TAIL + 2 * lane), PAD)
    two = (lookup(TAB, tok, PAD, VOCAB) * tl.load(FACTORS)
           ^ lookup(TAB, prev, PAD, VOCAB) * tl.load(FACTORS + 1))
    three = two ^ (lookup(TAB, prev2, PAD, VOCAB) * tl.load(FACTORS + 2))
    size = tl.load(SIZES + cols)
    v = tl.where(cols < 8, two, three) % size
    v = tl.where(v < 0, v + size, v) + tl.load(OFFSETS + cols)
    tl.store(ROWS + 16 * lane + cols, v)
    tl.store(VALID + lane, (tok != PAD) & (tok < VOCAB))

def fused(layer, ids, history, slots):
    n = ids.shape[0]
    rows = torch.empty((n, 1, 16), device=ids.device, dtype=torch.long)
    valid = torch.empty((n, 1), device=ids.device, dtype=torch.bool)
    decode_hash[(n,)](ids, history, slots, layer.lookup, layer.sizes, layer.offsets, layer.multipliers,
                      rows, valid, layer.cfg.engram_pad_id, layer.lookup.numel(), num_warps=1)
    return rows, valid
