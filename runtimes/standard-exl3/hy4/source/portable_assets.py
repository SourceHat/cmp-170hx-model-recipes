'Open the files in a downloaded standard HY4 EXL3 repository.'

from contextlib import ExitStack

import json

from pathlib import PurePosixPath

from safetensors import safe_open

from decoder_prefix_probe import official

from hy4_paged_q8_probe import decoder_config

from source import REVISION

def read(path):
    return json.loads(path.read_bytes())

def member(root, name):
    path = PurePosixPath(name)
    if path.is_absolute() or not path.parts or ".." in path.parts:
        raise ValueError(f"Invalid model file name: {name}")
    return root.joinpath(*path.parts)

class FixedWeights:
    def __init__(self, files, device, assets):
        self.files, self.device, self.assets = files, device, assets
        self.index = assets.index
        self.handles = {}

    def archive(self, key):
        name = self.index[key]
        if name not in self.handles:
            self.handles[name] = self.files.enter_context(
                safe_open(member(self.assets.root, name), framework="pt", device="cpu"))
        return self.handles[name]

    def tensor(self, key):
        return self.archive(key).get_tensor(key).to(self.device)

    def load(self, model, prefix, aliases=None):
        keys = {} if aliases is None else aliases
        model.load_state_dict({k: self.tensor(prefix + keys.get(k, k)) for k in model.state_dict()},
                              strict=True, assign=True)
        return model.eval()

class FixedAssets:
    def __init__(self, root, engram, variant):
        self.root, self.engram = root, engram
        contract = read(root / "weight-contract.json")
        self.index = read(root / "model.safetensors.index.json")["weight_map"]
        self.bits = contract["routed_expert_bits"]
        if ((contract["variant"], contract["source_revision"], contract["scope"])
                != (variant, REVISION, "standard_only")
                or set(self.bits) != set(map(str, range(1, 42)))
                or any(len(row) != 512 for row in self.bits.values())
                or len(self.index) != 1878 or "lm_head.weight" not in self.index):
            raise ValueError("Use the matching published standard HY4 Flash pack")
        self.manifest = read(engram / "manifest.json")
        if (self.manifest["source_revision"] != REVISION or len(self.manifest["tables"]) != 4
                or len(self.manifest["parts"]) != 12):
            raise ValueError("Provide the four original packed Engram tables")
        self.backing = [
            {**part, "status": "verified", "path": str(member(engram, part["file"]))}
            for part in self.manifest["parts"]
        ]
        self.packs = root / "standard-expert-packs" / variant

    def metadata(self):
        return read(self.root / "config.json")

    def weights(self, files, device):
        return FixedWeights(files, device, self)

    def initialize(self, device):
        scope, reference = official()
        cfg = decoder_config(self.metadata())
        cfg.candidate_topk = cfg.compressed_indexer_group_topk * cfg.compressed_indexer_compress_ratio
        cfg._attn_implementation = "eager"
        return (cfg, scope, scope["HYV4FlashRotaryEmbedding"](cfg).to(device),
                self.manifest["tables"], self.backing, reference)

    def vision(self, device):
        with ExitStack() as files:
            w = self.weights(files, device)
            return {k: w.tensor(k) for k in w.index if k.startswith("vit.")}

    def check_layout(self):
        from host_engram import HostEngram

        shards = [member(self.root, n) for n in sorted(set(self.index.values()))]
        groups = [self.packs / f"layer-{layer:02d}/experts-{start:03d}/experts.safetensors"
                  for layer in range(1, 42) for start in range(0, 512, 8)]
        for path in [*shards, *groups]:
            if not path.is_file():
                raise FileNotFoundError(path)
        for tensor, layout in self.manifest["tables"].items():
            parts = sorted((p for p in self.backing if p["identity"]["tensor"] == tensor),
                           key=lambda p: p["identity"]["rank"])
            HostEngram(parts, tensor, *layout)
        raw = self.metadata()
        cfg = decoder_config(raw)
        if ((cfg.max_position_embeddings, len(cfg.layer_types), cfg.engram_layer_ids,
             raw["dfly_num_hidden_layers"]) != (1048576, 42, [2, 12, 22, 32], 5)
                or any(r["rope_type"] != "default" for r in cfg.rope_parameters.values())):
            raise ValueError("The original HY4 context, RoPE or draft layout differs")
        with safe_open(member(self.root, self.index["lm_head.weight"]), framework="pt", device="cpu") as f:
            if f.get_slice("lm_head.weight").get_dtype() != "BF16":
                raise ValueError("The HY4 head must be BF16")
        with safe_open(groups[0], framework="pt", device="cpu") as f:
            from hy4_standard_expert_pack import SIZES

            if not {f"{i}.{kind}.{field}" for i in range(8) for kind in SIZES
                    for field in ("suh", "svh", "trellis", "mul1")} <= set(f.keys()):
                raise ValueError("Packed expert tensor layout differs")
        return {"fixed_shards": len(shards), "expert_groups": len(groups), "engram_tables": 4}

class ExpertFiles:
    def __init__(self, variant, layer, device, cfg, weights):
        self.root = weights.assets.packs / f"layer-{layer:02d}"
        self.bits = weights.assets.bits[str(layer)]
        self.loaded = {}
        self.cfg, self.device = cfg, device
        prefix = f"model.layers.{layer}.mlp."
        self.fixed = {k.removeprefix(prefix): weights.tensor(k) for k in weights.index
                      if k.startswith(prefix) and not k.startswith(prefix + "experts.")}

    def load_group(self, first):
        import torch
        from exllamav3.modules.quant.exl3 import LinearEXL3
        from hy4_standard_expert_pack import CHUNK, SIZES

        path = self.root / f"experts-{first:03d}" / "experts.safetensors"
        with safe_open(path, framework="pt", device="cpu") as archive:
            for expert in range(first, first + CHUNK):
                for key, (out_width, in_width) in SIZES.items():
                    view = {f: archive.get_tensor(f"{expert}.{key}.{f}").to(self.device)
                            for f in ("suh", "svh", "trellis", "mul1")}
                    mat = LinearEXL3(None, in_width, out_width, **view,
                                     out_dtype=torch.float32, key=f"{expert}.{key}")
                    if mat.K != self.bits[expert]:
                        raise ValueError("Packed expert bits differ from the published contract")
                    self.loaded[expert, key] = mat

    def matrix(self, expert, name):
        from hy4_standard_expert_pack import CHUNK

        if (expert, name) not in self.loaded:
            self.load_group(expert // CHUNK * CHUNK)
        return self.loaded[expert, name]

    def load(self):
        from hy4_standard_expert_pack import CHUNK

        for first in range(0, len(self.bits), CHUNK):
            self.load_group(first)
