"Use ExLlamaV3's fused GPU attention over HY4's gathered latent rows."

from functools import lru_cache

import torch

from torch.nn import functional as F

@lru_cache(maxsize=8)
def page_table(device, batches, keys):
    pages = keys // 256
    return torch.arange(batches * pages, dtype=torch.int32, device=device).view(batches, pages)

def attention(q_nope, q_rope, latents, rotated_keys, projection, indices, sinks):
    from exllamav3.modules.attention_fn.dsa_triton import dsa_attn

    batch, heads, queries, nope = q_nope.shape
    keys = latents.shape[1]
    if queries != 1 or projection.shape[0] != heads:
        raise ValueError("Expect one HY4 decode query per lane")
    if padding := (-keys) % 256:
        latents = F.pad(latents, (0, 0, 0, padding))
        rotated_keys = F.pad(rotated_keys, (0, 0, 0, padding))
        keys += padding
    wk, wv = projection[:, :nope], projection[:, nope:]
    absorbed = torch.bmm(q_nope[:, :, 0].transpose(0, 1), wk).transpose(0, 1)
    q = torch.cat((absorbed, q_rope[:, :, 0]), dim=-1).half().contiguous()
    state = dsa_attn(
        q, latents.half().contiguous(), rotated_keys.half().contiguous(),
        page_table(q.device, batch, keys), sinks=sinks.float().contiguous(),
        indices=indices[:, 0].int().contiguous(), k_len=indices.shape[-1], pool_len=keys,
        scale=(nope + q_rope.shape[-1]) ** -0.5, out_latent=True,
        block_h=16, block_n=32, num_stages=1, page_size=256,
    )
    return torch.bmm(state.to(projection.dtype), wv.transpose(1, 2)).transpose(0, 1).unsqueeze(2)
