"Dispatch HY4's merged gate/up EXL3 expert matrices from device route IDs."

import torch

from torch.nn import functional as F

from decoder_prefix_probe import norm

from hy4_ops import latent_swiglu

from hy4_ops import routed_scores

from hy4_standard_expert_pack import SIZES

class DeviceExperts:
    def __init__(self, packed):
        from exllamav3.ext import exllamav3_ext as ext

        self.mgemm = ext.exl3_mgemm
        self.device = packed.device
        self.cfg = packed.cfg
        self.fixed = packed.fixed
        self.topk = self.cfg.num_experts_per_tok
        self.bits = sorted(set(packed.bits))
        self.bitrates = torch.tensor(packed.bits, dtype=torch.int32, device=self.device)
        self.pointers = {}
        # Retain the referenced allocations for the lifetime of the device tables.
        self.weights = {}
        for name, (out_width, in_width) in SIZES.items():
            matrices = [packed.loaded[i, name] for i in range(len(packed.bits))]
            if any(
                m.trellis.shape != (in_width // 16, out_width // 16, 16 * k)
                or m.K != k or not m.mul1 or m.mcg or m.bias is not None
                or any(not v.is_contiguous() or v.device != self.device
                       for v in (m.trellis, m.suh, m.svh))
                for k, m in zip(packed.bits, matrices, strict=True)
            ):
                raise ValueError("The resident HY4 expert geometry does not match indexed EXL3")
            self.weights[name] = matrices
            self.pointers[name] = tuple(
                torch.tensor([getattr(m, field).data_ptr() for m in matrices],
                             dtype=torch.int64, device=self.device)
                for field in ("trellis", "suh", "svh")
            )

    def multiply(self, name, rows, indices):
        out_width, in_width = SIZES[name]
        a = rows.reshape(-1, 1, in_width).contiguous()
        b, su, sv = self.pointers[name]
        c = torch.empty((len(a), 1, out_width), dtype=torch.float32, device=a.device)
        hadamard = torch.empty_like(a)
        for bits, choices in indices:
            self.mgemm(a, b, c, su, hadamard, sv, choices, None, bits, -1,
                       False, True, -1, -1, 0)
        return c[:, 0]

    def experts(self, latents, probs, ids):
        order = ids.argsort(dim=-1)
        ordered_ids = ids.gather(1, order)
        ordered_probs = probs.gather(1, order)
        flat = ordered_ids.reshape(1, -1)
        bits = self.bitrates[flat]
        # Every slot is written by exactly one launch. The EXL3 kernel skips -1.
        indices = [(k, flat.masked_fill(bits != k, -1)) for k in self.bits]
        tiled = latents[:, None].expand(-1, self.topk, -1).half().contiguous()
        gu = self.multiply("gate_up", tiled, indices).bfloat16()
        active = latent_swiglu(gu, self.cfg.swiglu_limit).half()
        down = self.multiply("down", active, indices).bfloat16().view(*ids.shape, -1)
        weighted = (down * ordered_probs[..., None]).to(latents.dtype)
        total = torch.zeros_like(latents)
        # Keep the reference's ascending-expert order and BF16 rounding per add.
        for part in weighted.unbind(dim=1):
            total.add_(part)
        return total

    def __call__(self, x):
        if x.shape[:2] != (4, 1) or x.dtype != torch.bfloat16:
            raise ValueError("Indexed EXL3 dispatch expects four BF16 decode rows")

        def linear(v, name):
            return F.linear(v, self.fixed[name + ".weight"])

        cfg = self.cfg
        _, probs, ids = routed_scores(x, self.fixed["gate.weight"], self.fixed["gate.e_score_correction_bias"],
                                     self.topk, cfg.routed_scaling_factor)
        x = x[:, 0]
        total = self.experts(linear(x, "routed_expert_down_proj"), probs, ids)
        routed = linear(total, "routed_expert_up_proj")
        shared = linear(F.silu(linear(x, "shared_experts.gate_proj")) * linear(x, "shared_experts.up_proj"),
                        "shared_experts.down_proj")
        return norm(routed + shared, self.fixed["combine_output_norm.weight"], cfg.rms_norm_eps).unsqueeze(1)
