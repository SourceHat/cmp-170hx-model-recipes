'Short-history HY4 target with a causal step shared by decode and verification.'

import torch

from engram_layer_probe import residual

from host_engram import HostEngram

from host_engram import decode

from hy4_engram import hash_parameters

from hy4_engram import hash_rows

from hy4_engram import ngram_tokens

ATTN_ALIASES = {"gate_proj.weight": "linear_gate.weight", "sinks": "learnable_sink_param"}

class Engram:
    def __init__(self, layer, w, cfg, layout, staged, lut):
        prefix = f"model.layers.{layer - 1}.engram_layer."
        tensor = prefix + "multi_head_embedding.embedding.weight"
        self.weights = {key.removeprefix(prefix): w.tensor(key) for key in w.index
                        if key.startswith(prefix) and key != tensor}
        self.lookup = self.weights["lookup_table"]
        self.cfg, self.lut = cfg, lut
        self.sizes, self.offsets, self.multipliers = hash_parameters(cfg.engram_layer_head_vocab_sizes[str(layer)],
            self.lookup.numel(), cfg.engram_max_ngram_size, cfg.engram_seed, layer, w.device)
        parts = sorted((part for part in staged if part["identity"]["tensor"] == tensor),
                       key=lambda part: part["identity"]["rank"])
        self.table = HostEngram(parts, tensor, *layout[tensor])

    def fetch(self, wave):
        cfg = self.cfg
        pad = cfg.engram_pad_id
        before = wave.tokens[:, max(0, wave.start - cfg.engram_max_ngram_size + 1):wave.start]
        ngrams = ngram_tokens(wave.ids, wave.slots, cfg.engram_max_ngram_size, pad, history=before)
        rows = hash_rows(ngrams, self.lookup, pad, self.sizes, self.offsets, self.multipliers, cfg.engram_n_head_per_ngram)
        values = decode(torch.from_numpy(self.table.gather(rows.cpu().numpy())).to(wave.ids.device), self.lut)
        mask = (wave.ids != pad) & (wave.ids < self.lookup.numel())
        return values, mask

    def step(self, x, values, mask):
        return residual(x, values, mask, self.weights, len(self.sizes), self.cfg.hc_mult)
