'Run the released DFly2 blocks directly on selected committed HY4 Q8 rows.'

from contextlib import ExitStack

from dataclasses import dataclass

import torch

from torch.nn import functional as F

from dfly_math import correct_hidden

from dfly_math import rms_norm

from dfly_math import seed_block

from dfly_proposal_probe import DRAFT_ROOT

from dfly_proposal_probe import TARGETS

from dfly_proposal_probe import projected_kv

from hy4_cached_target import ATTN_ALIASES

from hy4_paged_q8_probe import LATENT

from hy4_shared_pool import LANES

from hy4_sliding_runtime import VERIFY

@dataclass(frozen=True)
class DraftAnchor:
    generation: int
    hidden: torch.Tensor
    next_tokens: torch.Tensor
    recalled: dict

class DraftBlock:
    def __init__(self, cfg, scope, owner, layer, weights, ext):
        self.owner, self.ext, self.scope = owner, ext, scope
        self.device = weights.device
        self.eps = cfg.rms_norm_eps
        prefix = DRAFT_ROOT + str(layer) + "."
        with torch.device("meta"):
            self.m = scope["HYV4FlashAttention"](cfg, TARGETS[layer])
        self.m.compressed_indexer = None
        weights.load(self.m, prefix + "self_attn.", ATTN_ALIASES)
        self.n1, self.n2, self.gate, self.up, self.down = [weights.tensor(prefix + tag) for tag in (
            "input_layernorm.weight", "post_attention_layernorm.weight", "mlp.gate_proj.weight",
            "mlp.up_proj.weight", "mlp.down_proj.weight")]

    def __call__(self, hidden, selected, positions, layout):
        hidden, selected, positions = (x.to(self.device) for x in (hidden, selected, positions))
        if (selected.ndim != 2 or selected.shape[0] != LANES or selected.shape[1] > 2048
                or (selected < -1).any()):
            raise ValueError("Invalid committed target recall for DFly2")
        valid = selected >= 0
        # Compact selected keys in the target's order, then append the local causal draft block.
        old_width = int(valid.sum(1).max())
        if not old_width:
            raise ValueError("A DFly2 anchor must retain target history")
        order = (~valid).to(torch.uint8).argsort(dim=-1, stable=True)[:, :old_width]
        old = selected.gather(1, order).long()
        packed, scales, kr = self.owner.kv.read(layout, self.owner.lanes, old)
        k = hidden.new_empty((LANES * old_width, LATENT), dtype=torch.float16)
        self.ext.dequant_cache_cont(packed.flatten(0, 1).contiguous(), scales.flatten(0, 1).contiguous(), k, 0.0)
        k = k.view(LANES, old_width, LATENT).to(hidden.dtype)
        m = self.m
        h = rms_norm(hidden, self.n1, self.eps)
        heads, n, r = m.num_heads, m.qk_nope_head_dim, m.qk_rope_head_dim
        q0, qr = m.q_b_proj(rms_norm(m.q_a_proj(h), m.q_a_layernorm.weight, self.eps)).view(
            LANES, VERIFY, heads, n + r).transpose(1, 2).split((n, r), dim=-1)
        kz, rz = projected_kv(h, m.kv_a_proj_with_mqa.weight, m.kv_a_layernorm.weight, r, self.eps)
        phases = self.owner.rotary(h, positions.unsqueeze(0), layer_type="indexed_attention")
        qr, rz = self.scope["apply_rotary_pos_emb"](qr, rz.unsqueeze(1), *phases)
        kp, vp = m.expand_kv(torch.cat((k, kz), dim=1).unsqueeze(1),
                             torch.cat((kr, rz.squeeze(1)), dim=1).unsqueeze(1))
        rows = torch.arange(VERIFY, device=self.device)
        valid = torch.cat((old[:, None, :].expand(-1, VERIFY, -1) >= 0,
                           (rows <= rows[:, None]).expand(LANES, -1, -1)), dim=2)
        mask = hidden.new_zeros((LANES, 1, VERIFY, old_width + VERIFY)).masked_fill_(~valid[:, None], float("-inf"))
        branch = self.scope["eager_attention_forward"](m, torch.cat((q0, qr), dim=-1), kp, vp, mask, m.scaling)[0]
        branch = branch * m.gate_proj(h).view(LANES, VERIFY, heads, m.v_head_dim).sigmoid()
        hidden = hidden + rms_norm(m.o_proj(branch.flatten(2)), m.post_proj_norm.weight, self.eps)
        front = rms_norm(hidden, self.n2, self.eps)
        return hidden + F.linear(F.silu(F.linear(front, self.gate)) * F.linear(front, self.up), self.down)

class NativeDFly:
    def __init__(self, target):
        fixed = getattr(target, "fixed_assets", None)
        weights = fixed.weights
        meta = fixed.metadata()
        cfg = target.cfg
        if (tuple(meta["dfly_target_kv_layers"]), tuple(meta["dfly_target_index_layer"]),
                meta["speculative_config"]["num_speculative_tokens"], meta["dfly_num_hidden_layers"],
                meta["dfly_mtp_fusion"], meta["dfly_enable_hidden_correction"]) != (TARGETS, TARGETS, VERIFY - 1, 5, "slot0", True):
            raise ValueError("Unsupported native HY4 DFly2 geometry")
        if target.head is None or target.head.dtype != torch.bfloat16:
            raise ValueError("Native DFly2 requires the full target and its original BF16 head")
        self.target = target
        self.mask = meta["dfly_mask_token_id"]
        with ExitStack() as files:
            w = weights(files, target.embed.device)
            self.fusion = [w.tensor(DRAFT_ROOT + "mtp_fusion." + n) for n in
                           ("enorm.weight", "hnorm.weight", "eh_proj.weight", "gate")]
        self.blocks = []
        for i, layer in enumerate(TARGETS):
            block = target.blocks[layer]
            if not block.sparse:
                raise ValueError("Each DFly2 block belongs on its indexed target cache rank")
            with ExitStack() as files, torch.cuda.device(block.device):
                w = weights(files, block.device)
                self.blocks.append(DraftBlock(cfg, target.scope, block.attention, i, w, target.ext))
        with ExitStack() as files:
            w = weights(files, target.head.device)
            self.final_norm = w.tensor(DRAFT_ROOT + "final_norm.weight")
            self.correction = [w.tensor(DRAFT_ROOT + "hidden_correction." + n) for n in
                               ("hidden_norm.weight", "embed_norm.weight", "gate_proj.weight",
                                "up_proj.weight", "down_proj.weight")]

    def propose(self, anchor):
        t = self.target
        d = t.embed.device
        if (t.pool.pending is not None or anchor.generation != t.pool.generation
                or sorted(anchor.recalled) != list(TARGETS) or anchor.hidden.shape != (LANES, t.cfg.hidden_size)
                or anchor.next_tokens.shape != (LANES,)):
            raise ValueError("DFly2 needs the current committed target anchor")
        positions = (torch.tensor(t.pool.lengths, device=d) + t.offsets.to(d))[:, None] + torch.arange(VERIFY, device=d)
        if (positions >= t.cfg.max_position_embeddings).any():
            raise ValueError("DFly2 verification would exceed the native position limit")
        ids = torch.full((LANES, VERIFY), self.mask, device=d, dtype=torch.long)
        ids[:, 0] = anchor.next_tokens.to(d)
        hidden = seed_block(F.embedding(ids, t.embed), anchor.hidden.to(d), *self.fusion, t.cfg.rms_norm_eps)
        layouts = {}
        for layer, step in zip(TARGETS, self.blocks, strict=True):
            if step.device not in layouts:
                layouts[step.device] = t.pool.layout(step.device)
            with torch.cuda.device(step.device):
                hidden = step(hidden, anchor.recalled[layer], positions, layouts[step.device])
        head = t.head
        hidden = rms_norm(hidden.to(head.device), self.final_norm, t.cfg.rms_norm_eps)
        previous = ids[:, 0].to(head.device)
        out = [previous]
        for step in range(1, VERIFY):
            emb = F.embedding(previous.to(d), t.embed).to(head.device)
            fixed = correct_hidden(hidden[:, step], emb, *self.correction, t.cfg.rms_norm_eps)
            previous = torch.mm(fixed, head.T, out_dtype=torch.float32).argmax(dim=-1)
            out.append(previous)
        return torch.stack(out, dim=1)
