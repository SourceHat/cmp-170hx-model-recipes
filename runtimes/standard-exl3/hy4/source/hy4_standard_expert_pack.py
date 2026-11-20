from portable_assets import ExpertFiles

from fractions import Fraction

import torch

from torch.nn import functional as F

from decoder_prefix_probe import norm

from hy4_ops import latent_swiglu

from hy4_ops import routed_scores

VARIANTS = {"4p875-tp2": Fraction(39, 8), "8p0-tp3": Fraction(8)}

SIZES = {"gate_up": (3072, 1536), "down": (1536, 1536)}

CHUNK = 8

class PackedExperts(ExpertFiles):
    """Read and execute a committed packed expert layer without loading source expert weights."""



    def forward(self, x):
        cfg = self.cfg
        if x.shape[:2] != (4, 1) or x.dtype != torch.bfloat16:
            raise ValueError("Use the same four-row target step for ordinary and speculative decode")

        def linear(v, name):
            return F.linear(v, self.fixed[name + ".weight"])

        _, p, ids = routed_scores(x, self.fixed["gate.weight"], self.fixed["gate.e_score_correction_bias"],
                                  cfg.num_experts_per_tok, cfg.routed_scaling_factor)
        x = x[:, 0]
        latents = linear(x, "routed_expert_down_proj")
        total = torch.zeros_like(latents)
        for expert in ids.unique(sorted=True).tolist():
            slot, lane = torch.where((ids == expert).T)
            tile = F.pad(latents[lane], (0, 0, 0, 4 - len(lane))).half().contiguous()
            g = self.matrix(expert, "gate_up").forward(tile, {}).bfloat16()
            v = latent_swiglu(g, cfg.swiglu_limit).half().contiguous()
            result = self.matrix(expert, "down").forward(v, {})[:len(lane)].bfloat16()
            total[lane] = total[lane] + (result * p[lane, slot, None]).to(latents.dtype)
        routed = linear(total, "routed_expert_up_proj")
        shared = linear(F.silu(linear(x, "shared_experts.gate_proj")) * linear(x, "shared_experts.up_proj"),
                        "shared_experts.down_proj")
        return norm(routed + shared, self.fixed["combine_output_norm.weight"], cfg.rms_norm_eps).unsqueeze(1)
