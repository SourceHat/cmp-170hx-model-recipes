'Check all real HY4 Engram residuals with host-backed rows on one GPU.'

import torch

import torch.nn.functional as F

def residual(hidden, embeddings, mask, w, head_count, lanes):
    embeddings = torch.stack([
        F.rms_norm(embeddings[:, :, i], (embeddings.shape[-1],), w[f"lookup_per_head_norms.{i}.weight"])
        for i in range(head_count)
    ], dim=2).flatten(start_dim=-2)
    width = hidden.shape[-1]
    gates = []
    for i in range(lanes):
        keys = F.linear(embeddings, w[f"key_projs.{i}.weight"], w[f"key_projs.{i}.bias"])
        keys = F.rms_norm(keys, (width,), w[f"norm_key.{i}.weight"])
        queries = F.rms_norm(hidden[:, :, i], (width,), w[f"norm_query.{i}.weight"])
        score = (keys * queries).sum(dim=-1) * width**-0.5
        gates.append(torch.sigmoid(score.abs().clamp_min(1e-6).sqrt() * score.sign()))
    values = F.linear(embeddings, w["value_proj.weight"], w["value_proj.bias"])
    signal = w["unified_pre_gamma"] * F.rms_norm(values, (width,))
    branches = torch.stack([w[f"unified_per_hc_scales.{i}"] * signal for i in range(lanes)], dim=2)
    return (torch.stack(gates, dim=2).unsqueeze(-1) * signal.unsqueeze(2) + branches).masked_fill(
        ~mask[:, :, None, None], 0)
