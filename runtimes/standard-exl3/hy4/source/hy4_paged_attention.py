'Decode HY4 attention directly from its EXL3 Q8 pages and BF16 RoPE.'

import torch

import triton

import triton.language as tl

from exllamav3.modules.attention_fn.dsa_triton import _dsa_attn_combine_kernel

from exllamav3.modules.attention_fn.triton_paged import _get_h32

from exllamav3.modules.attention_fn.triton_paged import _qc_load_v

from exllamav3.modules.attention_fn.triton_paged import _rot_h32

@triton.jit
def split_attention(Q, QR, WORDS, SCALES, ROPE, TABLE, PICKS, ML, ACC, H32,
                    H: tl.constexpr, K: tl.constexpr, PAGES: tl.constexpr,
                    SPLITS: tl.constexpr, SCALE: tl.constexpr,
                    BH: tl.constexpr, BN: tl.constexpr, QUERY_WIDTH: tl.constexpr = 1):
    pid, split = tl.program_id(0), tl.program_id(1)
    head_blocks: tl.constexpr = (H + BH - 1) // BH
    row = pid // head_blocks
    h = (pid % head_blocks) * BH + tl.arange(0, BH)
    d = tl.arange(0, 512)
    dr = tl.arange(0, 64)
    h_valid = h < H
    q = tl.load(Q + (row * H + h[:, None]) * 512 + d[None, :], h_valid[:, None], 0)
    q = _rot_h32(q, H32, BH, 512)
    q_rope = tl.load(QR + (row * H + h[:, None]) * 64 + dr[None, :], h_valid[:, None], 0)
    start, stop = split * tl.cdiv(K, SPLITS), tl.minimum((split + 1) * tl.cdiv(K, SPLITS), K)
    maximum = tl.full((BH,), -float("inf"), tl.float32)
    mass = tl.zeros((BH,), tl.float32)
    accum = tl.zeros((BH, 512), tl.float32)
    for begin in range(start, stop, BN):
        offset = begin + tl.arange(0, BN)
        logical = tl.load(PICKS + row * K + offset, offset < stop, -1)
        valid = logical >= 0
        page = tl.load(TABLE + (row // QUERY_WIDTH) * PAGES + tl.maximum(logical, 0) // 256, valid, 0)
        physical = page * 256 + tl.maximum(logical, 0) % 256
        v = _qc_load_v(WORDS, SCALES, physical, 0, d, valid, 8, 1, 512, 512)
        r = tl.load(ROPE + physical[:, None] * 64 + dr[None, :], valid[:, None], 0).to(tl.float16)
        s = tl.dot(q_rope, tl.trans(r), acc=tl.dot(q, tl.trans(v))) * SCALE
        s = tl.where(valid[None, :], s, -float("inf"))
        new = tl.maximum(maximum, tl.max(s, 1))
        finite = tl.where(new == -float("inf"), 0., new)
        alpha = tl.where(maximum == -float("inf"), 0., tl.exp(maximum - finite))
        p = tl.where(valid[None, :], tl.exp(s - finite[:, None]), 0.)
        mass = mass * alpha + tl.sum(p, 1)
        accum = accum * alpha[:, None] + tl.dot(p.to(tl.float16), v)
        maximum = new
    base = (pid * SPLITS + split) * BH + tl.arange(0, BH)
    tl.store(ML + base * 2, maximum)
    tl.store(ML + base * 2 + 1, mass)
    tl.store(ACC + base[:, None] * 512 + d[None, :], accum)

def attention(q_nope, q_rope, planes, table, indices, projection, sinks):
    b, h, query_width, nope = q_nope.shape
    words, scales, rope = planes
    wk, wv = projection[:, :nope], projection[:, nope:]
    if query_width == 1:
        q = torch.bmm(q_nope[:, :, 0].transpose(0, 1), wk).transpose(0, 1).half().contiguous()
        qr = q_rope[:, :, 0].half().contiguous()
    else:
        queries = q_nope.permute(1, 0, 2, 3).reshape(h, b * query_width, nope)
        q = torch.bmm(queries, wk).transpose(0, 1).half().contiguous()
        qr = q_rope.transpose(1, 2).reshape(b * query_width, h, 64).half().contiguous()
        indices = indices.reshape(b * query_width, -1).contiguous()
    k = indices.shape[-1]
    splits = max(1, min(16 if query_width == 1 else 8, triton.cdiv(k, 32)))
    bh, bn = 16, 16
    rows = b * query_width
    blocks = rows * triton.cdiv(h, bh)
    ml = torch.empty((blocks * splits * bh, 2), dtype=torch.float32, device=q.device)
    acc = torch.empty((blocks * splits * bh, 512), dtype=torch.float32, device=q.device)
    out = torch.empty((h, rows, 512), dtype=torch.float16, device=q.device)
    h32 = _get_h32(q.device)
    split_attention[(blocks, splits)](
        q, qr, words, scales, rope, table, indices, ml, acc, h32, h, k, table.shape[1],
        splits, (nope + 64) ** -.5, bh, bn, query_width, num_warps=4, num_stages=1,
    )
    _dsa_attn_combine_kernel[(blocks, 4)](
        ml, acc, sinks.float().contiguous(), q, out, 0, rows, splits, h32,
        h, 512, 64, True, False, 0, bh, 128, OUT_LATENT=1, QC=8, num_warps=4,
    )
    output = torch.bmm(out.to(projection.dtype), wv.transpose(1, 2))
    return output.view(h, b, query_width, -1).permute(1, 0, 2, 3)
