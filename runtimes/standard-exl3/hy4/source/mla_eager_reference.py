'Bounded compact-cache attention with the pinned eager BF16 rounding points.'

import torch

import torch.nn.functional as F

def projected_attention(q_nope, q_rope, latents, rotated_keys, projection, indices, query_slots, sinks):
    batch, heads, queries, nope = q_nope.shape
    _, keys, rank = latents.shape
    rope = q_rope.shape[-1]
    if (not 0 < keys <= 2048 or rotated_keys.shape != (batch, keys, rope)
            or q_rope.shape[:3] != (batch, heads, queries)
            or projection.shape[0] != heads or projection.shape[-1] != rank or projection.shape[1] <= nope
            or indices.shape[:2] != (batch, queries) or query_slots.shape != (batch, queries)
            or indices.dtype not in (torch.int32, torch.int64) or sinks.shape != (heads,)):
        raise ValueError("Unsupported shape for the bounded HY4 projected attention reference")
    valid = indices >= 0
    if ((indices < -1) | (indices >= keys) | (valid & (indices > query_slots.unsqueeze(-1)))).any():
        raise ValueError("Noncausal or unavailable HY4 cache slot")

    # The eager implementation rounds the projection, scores and probabilities
    # independently. Absorbing the projections into FP32 moves those boundaries.
    kv = F.linear(latents.unsqueeze(1), projection.flatten(0, 1)).view(batch, keys, heads, -1).transpose(1, 2)
    k_nope, value = kv.split((nope, projection.shape[1] - nope), dim=-1)
    k = torch.cat((k_nope, rotated_keys[:, None].expand(-1, heads, -1, -1)), dim=-1)
    q = torch.cat((q_nope, q_rope), dim=-1)
    score = torch.matmul(q, k.transpose(-1, -2)) * ((nope + rope) ** -0.5)
    selected = torch.zeros((batch, queries, keys + 1), dtype=torch.bool, device=latents.device)
    selected.scatter_(-1, indices.masked_fill(~valid, keys).long(), True)
    score = score.masked_fill(~selected[:, None, :, :keys], float("-inf"))
    sink = sinks.reshape(1, -1, 1, 1).expand(batch, -1, queries, 1)
    scores = torch.cat((score, sink), dim=-1)
    probs = F.softmax(scores - scores.max(dim=-1, keepdim=True).values, dim=-1, dtype=scores.dtype)
    return torch.matmul(probs[..., :-1].to(value.dtype), value)
