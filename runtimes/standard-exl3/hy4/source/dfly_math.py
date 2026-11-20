'Reference slot fusion and hidden correction for the released HY4 DFly2 draft.'

import torch

from torch.nn import functional as F

def rms_norm(x, weight, eps):
    wide = x.float()
    return (wide * torch.rsqrt(wide.square().mean(dim=-1, keepdim=True) + eps) * weight).to(x.dtype)

def seed_block(embeddings, target_hidden, embedding_norm, hidden_norm, projection, gate, eps):
    if (embeddings.ndim != 3 or embeddings.shape[1] < 2 or target_hidden.shape != embeddings[:, 0].shape or
            embeddings.dtype != torch.bfloat16 or target_hidden.dtype != embeddings.dtype):
        raise ValueError("DFly2 needs aligned BF16 anchors and one target state per request")
    width = embeddings.shape[-1]
    if (embedding_norm.shape, hidden_norm.shape, projection.shape, gate.shape) != ((width,), (width,), (width, 2 * width), (width,)):
        raise ValueError("DFly2 slot-0 fusion weights do not match the checkpoint geometry")
    anchors = embeddings[:, 0]
    features = torch.cat((rms_norm(anchors, embedding_norm, eps), rms_norm(target_hidden, hidden_norm, eps)), dim=-1)
    fused = anchors + gate * F.linear(features, projection)
    return torch.cat((fused.unsqueeze(1), embeddings[:, 1:]), dim=1)

def correct_hidden(hidden, previous_embeds, hidden_norm, embedding_norm, gate_biasless, up, down, eps):
    if (hidden.ndim != 2 or hidden.shape != previous_embeds.shape or hidden.dtype != torch.bfloat16 or
            previous_embeds.dtype != hidden.dtype):
        raise ValueError("DFly2 hidden correction needs the previous token from each matched request")
    width, inner = hidden.shape[-1], gate_biasless.shape[0]
    if (hidden_norm.shape, embedding_norm.shape, gate_biasless.shape, up.shape, down.shape) != (
            (width,), (width,), (inner, 2 * width), (inner, 2 * width), (width, inner)):
        raise ValueError("DFly2 hidden correction tensor geometry differs from the source")
    combined = torch.cat((rms_norm(hidden, hidden_norm, eps), rms_norm(previous_embeds, embedding_norm, eps)), -1)
    delta = F.linear(F.silu(F.linear(combined, gate_biasless)) * F.linear(combined, up), down)
    return hidden + delta
