'Apply each resident HY4 packed expert once to its rows in a prompt tile.'

import torch

from torch.nn import functional as F

from decoder_prefix_probe import norm

from hy4_ops import latent_swiglu

from hy4_ops import routed_scores

MAX_TILE = 256

def packed_prefill(packed, hidden):
    cfg = packed.cfg
    if (hidden.ndim != 3 or hidden.shape[0] != 4 or not 0 < hidden.shape[1] <= MAX_TILE
            or hidden.shape[-1] != cfg.hidden_size or hidden.device != packed.device or hidden.dtype != torch.bfloat16):
        raise ValueError("Use a bounded BF16 tile of four native HY4 text requests")
    peer = getattr(packed, "peer_experts", None)
    if peer is not None:
        return peer(hidden)
    if hidden.shape[1] == 1:
        return packed.forward(hidden)
    if gpu_prefill := getattr(packed, "gpu_expert_prefill", None):
        return gpu_prefill(hidden)

    def lm(x, name):
        return F.linear(x, packed.fixed[name + ".weight"])

    _, probs, expert_ids = routed_scores(hidden, packed.fixed["gate.weight"], packed.fixed["gate.e_score_correction_bias"],
                                         cfg.num_experts_per_tok, cfg.routed_scaling_factor)
    rows = hidden.flatten(0, 1)
    latent = lm(rows, "routed_expert_down_proj")
    output = torch.zeros_like(latent)
    order = expert_ids.flatten().argsort(stable=True)
    counts = expert_ids.flatten().bincount(minlength=cfg.n_routed_experts).tolist()
    start = 0
    for expert, n in enumerate(counts):
        if not n:
            continue
        choices = order[start:start + n]
        start += n
        positions, routes = choices // cfg.num_experts_per_tok, choices % cfg.num_experts_per_tok
        x = latent[positions].half().contiguous()
        y = packed.matrix(expert, "gate_up").forward(x, {}).bfloat16()
        y = latent_swiglu(y, cfg.swiglu_limit).half().contiguous()
        y = packed.matrix(expert, "down").forward(y, {}).bfloat16()
        scaled = (y * probs[positions, routes, None]).to(latent.dtype)
        output[positions] = output[positions] + scaled
    routed = lm(output, "routed_expert_up_proj")
    shared = lm(F.silu(lm(rows, "shared_experts.gate_proj")) * lm(rows, "shared_experts.up_proj"),
                "shared_experts.down_proj")
    return norm(routed + shared, packed.fixed["combine_output_norm.weight"], cfg.rms_norm_eps).view_as(hidden)
