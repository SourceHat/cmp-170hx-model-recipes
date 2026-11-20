'Check compact paged FP8 index keys and causal reads on the released indexer.'

import torch

PAGE, RATIO, DIM = 256, 4, 128

def fp8_rows(x, positions, inv):
    """Use the published GPT-J rotary layout, H128, and power-of-two E4M3 scale."""
    theta = positions.float().unsqueeze(-1) * inv
    r = x[..., DIM // 2:].float()
    even, odd = r[..., ::2], r[..., 1::2]
    rotated = torch.cat((even * theta.cos() - odd * theta.sin(), odd * theta.cos() + even * theta.sin()), -1)
    v = torch.cat((x[..., :DIM // 2].float(), rotated.bfloat16().float()), -1)
    for step in (1, 2, 4, 8, 16, 32, 64):
        a, b = v.reshape(*x.shape[:-1], DIM // (2 * step), 2, step).unbind(-2)
        v = torch.stack((a + b, a - b), -2).reshape(x.shape)
    v = v * 0.08838834764831845
    scale = (v.abs().amax(-1).clamp_min(1e-4) / 448).log2().ceil().exp2()
    return (v / scale[..., None]).clamp(-448, 448).to(torch.float8_e4m3fn).view(torch.uint8), scale

def rank(q, qscale, head, keys, kscale, valid):
    query = q.contiguous().view(torch.float8_e4m3fn).float()
    pooled = keys.contiguous().view(torch.float8_e4m3fn).float()
    scores = torch.einsum("bhd,bgd->bhg", query, pooled).relu()
    logits = (scores * (head * qscale)[..., None]).sum(1) * kscale
    return logits.masked_fill(~valid, float("-inf"))
