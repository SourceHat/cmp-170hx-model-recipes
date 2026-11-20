"""Tensor primitives for the released SenseNova Loop model."""

import torch
import torch.nn.functional as F


def fold_fp32_gate_bias(activation, bias):
    if activation.dtype != torch.float32 or bias.dtype != torch.float32 or bias.shape != activation.shape[-1:]:
        raise ValueError("SenseNova delta gate requires matching FP32 activations and bias")
    return activation + bias


def pack_rows(rows: torch.Tensor) -> tuple[torch.Tensor, torch.Tensor]:
    """Pack a bounded block of embedding rows; storage is int8 + one FP16 scale per row."""
    if rows.ndim != 2 or not rows.is_floating_point() or not torch.isfinite(rows).all():
        raise ValueError("Expected a finite floating-point matrix")
    values = rows.to(dtype=torch.float32, copy=True)
    peak = values.abs().amax(dim=-1)
    # Keep even small nonzero rows representable after converting the scale to FP16.
    scale = torch.where(peak > 0, (peak / 127).clamp_min(2.0**-24), torch.ones_like(peak)).half()
    if not torch.isfinite(scale).all():
        raise ValueError("Embedding scale is outside FP16 range")
    values.div_(scale.float().unsqueeze(-1)).round_().clamp_(-127, 127)
    return values.to(torch.int8).contiguous(), scale.contiguous()


def gather_rows(indices, packed, scale, dtype):
    """Expand only the requested rows, on the same device as the packed table."""
    shape = (*indices.shape, packed.shape[-1])
    requested = indices.reshape(-1)
    values = packed.index_select(0, requested).float()
    values.mul_(scale.index_select(0, requested).float().unsqueeze(-1))
    return values.to(dtype).reshape(shape)


def sinkhorn(logits, iterations):
    logits = logits.float()
    for _ in range(iterations):
        logits = logits - torch.logsumexp(logits, dim=-1, keepdim=True)
        logits = logits - torch.logsumexp(logits, dim=-2, keepdim=True)
    return logits.exp()


def route(residual, weight, bias, settings):
    if weight.dtype != torch.float32 or bias.dtype != torch.float32:
        raise ValueError("SenseNova mHC routers require source FP32 weights and bias")
    with torch.autocast(device_type=residual.device.type, enabled=False):
        flat = residual.flatten(-2).float()
        x = flat * torch.rsqrt(flat.square().mean(-1, keepdim=True) + 1e-6)
        logits = F.linear(x, weight, bias)
        streams = settings["streams"]
        pre = logits[..., :streams].sigmoid()
        post = 2 * logits[..., streams:2 * streams].sigmoid()
        if settings["fixed_identity"]:
            mix = torch.eye(streams, device=flat.device, dtype=torch.float32).expand(
                *flat.shape[:-1], streams, streams
            )
        else:
            mix = sinkhorn(logits[..., 2 * streams:].unflatten(-1, (streams, streams)), settings["iterations"])
        branch = torch.matmul(pre.to(residual.dtype).unsqueeze(-2), residual).squeeze(-2)
        scale = settings.get("pre_scale", 1.0)
        if scale != 1.0:
            branch = branch * scale
    return branch, post, mix


def merge(residual, branch, post, mix):
    with torch.autocast(device_type=residual.device.type, enabled=False):
        return torch.matmul(mix.to(residual.dtype), residual) + post.to(branch.dtype).unsqueeze(-1) * branch.unsqueeze(-2)


def enter(hidden, physical_layer, settings):
    if physical_layer == settings["start"]:
        return hidden.unsqueeze(-2).expand(*hidden.shape[:-1], settings["streams"], hidden.shape[-1]).contiguous()
    return hidden.unflatten(-1, (settings["streams"], -1))


def leave(residual, physical_layer, settings):
    return residual.mean(-2) if physical_layer == settings["end"] - 1 else residual.flatten(-2)
