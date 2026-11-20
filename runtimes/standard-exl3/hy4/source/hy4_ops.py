'Independent hyperconnection and latent expert arithmetic for HY4 Flash.'

import torch

from torch.nn import functional as F

def ihc_read(streams, fn, base, scale, norm_eps, gate_eps, magnitude):
    count, width = streams.shape[-2:]
    if (fn.shape, base.shape, scale.shape) != ((2 * count, count * width), (2 * count,), (2,)):
        raise ValueError("HY4 iHC checkpoint and residual stream geometry disagree")
    if fn.dtype != torch.float32 or base.dtype != fn.dtype or scale.dtype != fn.dtype:
        raise ValueError("The published iHC parameters must stay FP32")
    with torch.autocast(device_type=streams.device.type, enabled=False):
        wide = streams.flatten(-2).float()
        norm = torch.rsqrt(wide.square().mean(-1, keepdim=True) + norm_eps)
        logits = F.linear(wide, fn) * norm
        read, write = (logits * scale.repeat_interleave(count) + base).sigmoid().split(count, dim=-1)
        incoming = ((read + gate_eps).unsqueeze(-1) * streams).sum(dim=-2).to(streams.dtype)
        return magnitude * write + gate_eps, incoming

def ihc_write(streams, branch, post):
    if streams.shape[:-2] != branch.shape[:-1] or streams.shape[-1] != branch.shape[-1] or post.shape != streams.shape[:-1]:
        raise ValueError("HY4 iHC branch does not align with its residual streams")
    return (post.float().unsqueeze(-1) * branch.float().unsqueeze(-2) + streams.float()).to(streams.dtype)

def routed_scores(hidden, weight, correction, topk, scaling):
    """Exact released single-group router. The correction only chooses expert IDs."""
    if weight.ndim != 2 or hidden.shape[-1] != weight.shape[-1] or correction.shape != (weight.shape[0],) or not 0 < topk <= weight.shape[0]:
        raise ValueError("HY4 router geometry differs from its checkpoint")
    with torch.autocast(device_type=hidden.device.type, enabled=False):
        logits = F.linear(hidden.flatten(0, -2).float(), weight.float())
        scores = logits.sigmoid()
        selected = (scores + correction).topk(topk, dim=-1, sorted=False).indices
        coefficients = scores.gather(-1, selected)
        coefficients = coefficients / (coefficients.sum(-1, keepdim=True) + 1e-20) * scaling
    return logits, coefficients, selected

def latent_swiglu(projected, limit):
    gate, up = projected.chunk(2, dim=-1)
    return F.silu(gate.clamp_max(limit)) * up.clamp(-limit, limit)
