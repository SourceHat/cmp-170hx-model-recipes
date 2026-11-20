'Run the native HY4 target with one Q8 allocator shared by all indexed blocks.'

from contextlib import ExitStack

from types import SimpleNamespace

import torch

from torch.nn import functional as F

from decoder_prefix_probe import norm

from hy4_cached_target import ATTN_ALIASES

from hy4_cached_target import Engram

from hy4_engram import e4m3_lut

from hy4_indexed_runtime import IndexedTarget

from hy4_ops import ihc_read

from hy4_ops import ihc_write

from hy4_paged_q8_probe import codec

from hy4_shared_pool import LANES

from hy4_shared_pool import SharedPool

from hy4_sliding_runtime import SlidingTarget

from hy4_sliding_runtime import VERIFY

from hy4_standard_expert_pack import PackedExperts

from hy4_standard_expert_pack import VARIANTS

REQUESTS = tuple(range(LANES))

class TargetBlock:
    def __init__(self, layer, cfg, scope, rotary, geometry, backing, w, ext, append, pool, pool_tokens,
                 variant, retain_all):
        prefix = f"model.layers.{layer}."
        self.device, self.cfg = w.device, cfg
        with torch.device("meta"):
            m = scope["HYV4FlashAttention"](cfg, layer)
            self.hca, self.hcm = (scope["HYV4FlashHyperConnection"](cfg) for _ in range(2))
            dense = scope["HYV4FlashMLP"](cfg) if cfg.mlp_layer_types[layer] == "dense" else None
        w.load(m, prefix + "self_attn.", ATTN_ALIASES)
        for hc, branch in ((self.hca, "attn"), (self.hcm, "mlp")):
            w.load(hc, prefix + f"hc_{branch}_layer.hc_pre.", {k: "hc_" + k for k in ("fn", "base", "scale")})
        self.na, self.nm = (w.tensor(prefix + f"{k}.weight") for k in ("input_layernorm", "post_attention_layernorm"))
        self.engram = (Engram(layer + 1, w, cfg, geometry, backing, e4m3_lut(w.device))
                       if layer + 1 in cfg.engram_layer_ids else None)
        self.sparse = m.attention_type == "indexed_attention"
        self.attention = (IndexedTarget(m, scope, rotary, pool_tokens, w.device, ext, append, shared_pool=pool)
                          if self.sparse else SlidingTarget(m, scope, rotary, w.device, ext, append))
        self.mlp = w.load(dense, prefix + "mlp.") if dense is not None else PackedExperts(variant, layer, w.device, cfg, w)
        if dense is None and retain_all:
            for i in range(cfg.n_routed_experts):
                for name in ("gate_up", "down"):
                    self.mlp.matrix(i, name)

    def branch(self, x, hc, weight):
        p, latent = ihc_read(x, hc.fn, hc.base, hc.scale, self.cfg.rms_norm_eps, self.cfg.hc_eps, self.cfg.hc_magnitude)
        return p, norm(latent, weight, self.cfg.rms_norm_eps)

    def step(self, x, ids, tail, slots, offsets):
        x, ids, tail, slots, offsets = (t.to(self.device) for t in (x, ids, tail, slots, offsets))
        if self.engram is not None:
            wave = SimpleNamespace(ids=ids, tokens=torch.cat((tail, ids), dim=1),
                                   start=tail.shape[1], slots=slots[:, None])
            x = x + self.engram.step(x, *self.engram.fetch(wave))
        gate, raw = self.branch(x, self.hca, self.na)
        if self.sparse:
            branch, recall = self.attention.step(raw, offsets)
        else:
            branch, recall = self.attention.step(REQUESTS, raw, (slots + offsets)[:, None])
        x = ihc_write(x, branch, gate)
        gate, raw = self.branch(x, self.hcm, self.nm)
        return ihc_write(x, self.mlp.forward(raw), gate), recall

class NativeTarget:
    """Four native request lanes with identical ordinary and verify decode steps."""

    def __init__(self, variant, devices, owners, pool_tokens, offsets, *, embedding_rank=0, head_rank=-1,
                 retain_all=False, fixed_assets=None):
        if variant not in VARIANTS:
            raise ValueError("A native target must select a verified standard EXL3 variant")
        devices = tuple(torch.device(d) for d in devices)
        if (not devices or len(set(devices)) != len(devices) or any(d.type != "cuda" or d.index is None for d in devices)
                or not owners or any(type(n) is not int or not 0 <= n < len(devices) for n in owners)
                or not 0 <= embedding_rank < len(devices) or not -len(devices) <= head_rank < len(devices)):
            raise ValueError("Use exact managed CUDA ranks and block owners")
        self.devices = devices
        self.entry = devices[embedding_rank]
        self.fixed_assets = fixed_assets
        weights = fixed_assets.weights
        self.cfg, self.scope, rope, geometry, backing, self.reference = fixed_assets.initialize(self.entry)
        if (len(owners) > len(self.cfg.layer_types) or len(offsets) != LANES
                or any(type(n) is not int or not 0 <= n < self.cfg.max_position_embeddings for n in offsets)):
            raise ValueError("Invalid HY4 depth or original RoPE offsets")
        self.pool = SharedPool(pool_tokens, self.cfg.max_position_embeddings)
        self.offsets = torch.tensor(offsets, device=self.entry)
        self.max_lengths = tuple(self.pool.context - o for o in offsets)
        self.tail = torch.full((LANES, self.cfg.engram_max_ngram_size - 1), self.cfg.engram_pad_id,
                               device=self.entry, dtype=torch.long)
        self.ext, append, self.codec_identity = codec()
        self.blocks = []
        self.trial = None
        self.head = None
        phases = {self.entry: rope}
        with ExitStack() as files:
            self.embed = weights(files, self.entry).tensor("model.embed_tokens.weight")
        for layer, rank in enumerate(owners):
            d = devices[rank]
            if d not in phases:
                phases[d] = self.scope["HYV4FlashRotaryEmbedding"](self.cfg).to(d)
            with ExitStack() as files, torch.cuda.device(d):
                self.blocks.append(TargetBlock(layer, self.cfg, self.scope, phases[d], geometry, backing,
                    weights(files, d), self.ext, append, self.pool, pool_tokens, variant, retain_all))
        if len(owners) == len(self.cfg.layer_types):
            with ExitStack() as files:
                w = weights(files, devices[head_rank])
                with torch.device("meta"):
                    self.collapse = self.scope["HYV4FlashHyperHead"](self.cfg)
                w.load(self.collapse, "model.hc_head.", {"hc_" + k: "hc_head_" + k for k in ("fn", "base", "scale")})
                self.head_scale, self.head = w.tensor("model.norm.weight"), w.tensor("lm_head.weight")
                if self.head.dtype != torch.bfloat16:
                    raise ValueError("HY4 native target requires its BF16 head")

    def begin(self, width):
        if (self.trial is not None or type(width) is not int or not 1 <= width <= VERIFY
                or any(n + width > limit for n, limit in zip(self.pool.lengths, self.max_lengths, strict=True))):
            raise ValueError("Invalid native HY4 verification width or position")
        self.pool.reserve([width] * LANES)
        layouts = {}
        for block in self.blocks:
            if block.sparse:
                if block.device not in layouts:
                    layouts[block.device] = self.pool.layout(block.device, tentative=True)
                block.attention.attach_trial(layouts[block.device])
            else:
                block.attention.cache.begin([width] * LANES)
        self.trial = (width, self.tail, [])

    def step(self, ids, *, capture=False):
        if (self.trial is None or len(self.trial[2]) == self.trial[0] or ids.shape != (LANES, 1)
                or ids.dtype != torch.long or (ids < 0).any() or (ids >= self.cfg.vocab_size).any()):
            raise ValueError("Write one native target row per request in the reserved trial")
        _, previous, tokens = self.trial
        ids = ids.to(self.entry)
        slots = torch.tensor(self.pool.lengths, device=self.entry) + len(tokens)
        x = F.embedding(ids, self.embed).unsqueeze(2).expand(-1, -1, self.cfg.hc_mult, -1).contiguous()
        trace = []
        for block in self.blocks:
            with torch.cuda.device(block.device):
                x, recall = block.step(x, ids, previous, slots, self.offsets)
            if capture:
                trace.append((x, recall))
        tokens.append(ids)
        self.trial = (self.trial[0], torch.cat((previous[:, 1:], ids), dim=1), tokens)
        if self.head is not None:
            x = norm(self.collapse(x.to(self.head.device)), self.head_scale, self.cfg.rms_norm_eps).to(self.head.dtype)
            return x, F.linear(x, self.head), trace
        return x, None, trace

    def commit(self, kept):
        if (self.trial is None or len(kept) != LANES
                or any(type(n) is not int or not 1 <= n <= len(self.trial[2]) for n in kept)):
            raise ValueError("Keep the target anchor and at most the written draft prefix")
        tokens = torch.cat((self.tail, *self.trial[2]), dim=1)
        end = torch.tensor(kept, device=self.entry)
        self.tail = tokens.gather(1, end[:, None] + torch.arange(self.tail.shape[1], device=self.entry))
        accepted = {}
        for block in self.blocks:
            if block.sparse:
                if block.device not in accepted:
                    accepted[block.device] = end.to(block.device) - 1
                block.attention.resolve_index(accepted[block.device])
            else:
                block.attention.cache.resolve(kept)
        self.pool.commit(kept)
        for block in self.blocks:
            lengths = tuple(block.attention.index.lengths.tolist()) if block.sparse else block.attention.cache.lengths
            if lengths != self.pool.lengths:
                raise ValueError("Native target blocks disagree on the committed request lengths")
        self.trial = None
