"""SenseNova Loop uses Qwen3.5 projections with shared physical blocks and local visit state."""

import copy

import torch
import torch.nn.functional as F

from ..modules import Embedding, Linear, Module, TransformerBlock
from ..modules.arch_specific.sensenova_ops import enter, gather_rows, leave, merge, route
from .qwen3_5 import Qwen3_5BaseModel, Qwen3_5VLBaseConfig
from .qwen3_5_mtp import Qwen3_5MTPModel
from .qwen3_vl import Qwen3VLVisionModel


def cuda_device(device):
    device = torch.device(device)
    if device.type != "cuda":
        raise ValueError("SenseNova target weights must reside on one CUDA device")
    return device


class PackedTokenTable(torch.nn.Module):
    def __init__(self, q8, scales):
        super().__init__()
        self.register_buffer("q8", q8, persistent=False)
        self.register_buffer("scales", scales, persistent=False)

    def forward(self, ids):
        return gather_rows(ids, self.q8, self.scales, torch.bfloat16)


class SenseNovaEmbedding(Embedding):
    def __init__(self, config, key):
        super().__init__(config, key, config.vocab_size, config.hidden_size)
        self.caps.pop("prefer_cpu", None)

    def load(self, device, **kwargs):
        device = cuda_device(device)
        stc = self.config.stc
        qfile, sfile = self.key + ".q8_weight", self.key + ".q8_scale"
        has_q, has_s = stc.has_tensor(qfile), stc.has_tensor(sfile)
        if has_q != has_s or (has_q and stc.has_tensor(self.key + ".weight")):
            raise ValueError("Expected exactly one complete SenseNova input table")
        if not has_q:
            super().load(device, **kwargs)
            return
        q8 = stc.get_tensor(qfile, device)
        scales = stc.get_tensor(sfile, device)
        if (q8.dtype, tuple(q8.shape), scales.dtype, tuple(scales.shape)) != (
                torch.int8, (self.vocab_size, self.hidden_size), torch.float16, (self.vocab_size,)):
            raise ValueError("Unexpected SenseNova Q8 input table layout")
        self.device = device
        self.embedding = PackedTokenTable(q8, scales)

    def get_tensors(self):
        if isinstance(self.embedding, PackedTokenTable):
            return {self.key + ".q8_weight": self.embedding.q8, self.key + ".q8_scale": self.embedding.scales}
        return super().get_tensors() if self.embedding is not None else {}


class SenseNovaHead(Linear):
    def __init__(self, config):
        super().__init__(config, "lm_head", config.hidden_size, config.vocab_size,
                         qbits_key="head_bits", caps={"logits_output": True})
        self.weight = None

    def optimizer_targets(self):
        return []

    def load(self, device, **kwargs):
        device = cuda_device(device)
        weight = self.config.stc.get_tensor(self.key + ".weight", device, allow_bf16=True)
        if weight.dtype != torch.bfloat16 or tuple(weight.shape) != (
                self.out_features_unpadded, self.in_features_unpadded):
            raise ValueError("SenseNova head must retain its original BF16 weights")
        self.device, self.weight = device, weight

    def unload(self):
        self.device = None
        self.weight = None

    def get_tensors(self):
        return {self.key + ".weight": self.weight} if self.weight is not None else {}

    def recons_size(self):
        return 0

    def forward(self, x, params, out_dtype=None):
        # Casting the small activation, rather than the table, keeps main and MTP on one BF16 copy.
        logits = F.linear(x.to(torch.bfloat16), self.weight)
        return logits.to(out_dtype or self.out_dtype or torch.float)


class SenseNovaRouter(Module):
    def __init__(self, config, key):
        super().__init__(config, key, None)
        self.settings = config.mhc_settings
        self.hidden_size = config.hidden_size
        self.weight = self.bias = None

    def optimizer_targets(self):
        return []

    def load(self, device, **kwargs):
        device = cuda_device(device)
        weight = self.config.stc.get_tensor(self.key + ".weight", device)
        bias = self.config.stc.get_tensor(self.key + ".bias", device)
        streams = self.settings["streams"]
        n = 2 * streams + (0 if self.settings["fixed_identity"] else streams**2)
        if (weight.dtype, tuple(weight.shape), bias.dtype, tuple(bias.shape)) != (
                torch.float32, (n, streams * self.hidden_size), torch.float32, (n,)):
            raise ValueError(f"Unexpected source FP32 mHC tensors: {self.key}")
        self.device, self.weight, self.bias = device, weight, bias

    def unload(self):
        self.device = None
        self.weight = self.bias = None

    def get_tensors(self):
        return {self.key + ".weight": self.weight, self.key + ".bias": self.bias} if self.weight is not None else {}

    def forward(self, x, params, out_dtype=None):
        return route(x, self.weight, self.bias, self.settings)


class SenseNovaBlock(TransformerBlock):
    def __init__(self, block):
        super().__init__(block.config, block.key, block.layer_idx, attn_norm=block.attn_norm,
                         attn=block.attn, mlp_norm=block.mlp_norm, mlp=block.mlp)

    def forward(self, x, params, out_dtype=None):
        capture = params.get("sensenova_visit_capture")
        if capture is None:
            return self.forward_visit(x, params, out_dtype)
        with capture.visit(self.layer_idx, params.get("layer_instance", 0), params):
            return self.forward_visit(x, params, out_dtype)

    def forward_visit(self, x, params, out_dtype=None):
        return super().forward(x, params, out_dtype)


class SenseNovaMHCBlock(SenseNovaBlock):
    def __init__(self, block):
        super().__init__(block)
        self.settings = block.config.mhc_settings
        self.attn_router = SenseNovaRouter(self.config, self.key + ".mhc_attn")
        self.mlp_router = SenseNovaRouter(self.config, self.key + ".mhc_ffn")
        self.register_submodule(self.attn_router)
        self.register_submodule(self.mlp_router)

    def forward_visit(self, x, params, out_dtype=None):
        r = enter(x.to(torch.bfloat16), self.layer_idx, self.settings)
        branch, post, mix = self.attn_router.forward(r, params)
        # RMSNorm takes FP32 input for an FP16 output; widening the routed BF16 branch is exact.
        branch = self.attn_norm.forward(branch.float(), params, out_dtype=torch.half)
        branch = self.attn.forward(branch, params).to(torch.bfloat16)
        if params.get("prefill"):
            return x
        r = merge(r, branch, post, mix)
        branch, post, mix = self.mlp_router.forward(r, params)
        branch = self.mlp_norm.forward(branch.float(), params, out_dtype=torch.half)
        branch = self.mlp.forward(branch, params).to(torch.bfloat16)
        r = merge(r, branch, post, mix)
        y = leave(r, self.layer_idx, self.settings)
        return y.to(torch.float) if self.layer_idx == self.settings["end"] - 1 else y


class SenseNovaMTP(Qwen3_5MTPModel):
    def __init__(self, config, **kwargs):
        # Only the target traverses the loop. The released draft visits its one layer once.
        draft_config = copy.copy(config)
        draft_config.layer_map = draft_config.layer_map_str = None
        super().__init__(draft_config, **kwargs)
        self.caps["default_draft_size"] = 1


class SenseNovaVision(Qwen3VLVisionModel):
    def __init__(self, config, **kwargs):
        vision_config = copy.copy(config)
        vision_config.layer_map = vision_config.layer_map_str = None
        super().__init__(vision_config, **kwargs)

    @staticmethod
    def get_additional_compiled_tensors(config):
        source = Qwen3VLVisionModel.get_additional_compiled_tensors(config)
        if not getattr(config, "sensenova_packed_vision", False):
            return source
        return {key: spec for key, spec in source.items() if not key.endswith((".attn.qkv.weight", ".attn.qkv.bias"))}


class SenseNovaLoopConfig(Qwen3_5VLBaseConfig):
    arch_string = "SenseNovaLoopForConditionalGeneration"
    vision_processor_type = "Qwen2VLImageProcessor"

    def __init__(self, directory, **kwargs):
        if kwargs.pop("layer_map", None) is not None:
            raise ValueError("Use the published SenseNova execution order")
        super().__init__(directory, "text_config", SenseNovaLoopModel, SenseNovaVision, SenseNovaMTP, **kwargs)
        total = self.num_hidden_layers
        loop = self.config_dict["loop_settings"]
        start, end, n = loop["start"], loop["end"], loop["eval_count"]
        if not 0 <= start < end <= total or not isinstance(n, int) or n <= 0 or loop["counts"] != [n]:
            raise ValueError("SenseNova requires a fixed native loop")
        self.layer_map = [*range(start), *(list(range(start, end)) * n), *range(end, total)]
        self.mhc_settings = self.config_dict["mhc"]
        boundaries = (0, start, end, total)
        a, b = self.mhc_settings["start"], self.mhc_settings["end"]
        if (self.mhc_settings["streams"] != 2 or self.mhc_settings["iterations"] <= 0 or
                not any(lo <= a < b <= hi for lo, hi in zip(boundaries, boundaries[1:])) or
                self.vision.deepstack_visual_indexes):
            raise ValueError("Unsupported SenseNova stream or vision schedule")
        if self.tie_word_embeddings or self.mtp_num_hidden_layers != 1 or self.mtp_use_dedicated_embeddings:
            raise ValueError("Expected the released single draft and untied BF16 head")


class SenseNovaLoopModel(Qwen3_5BaseModel):
    config_class = SenseNovaLoopConfig

    def __init__(self, config, **kwargs):
        super().__init__(config, "model.language_model", use_moe=False, **kwargs)
        self.modules[0] = SenseNovaEmbedding(config, self.modules[0].key)
        self.modules[self.logit_layer_idx] = SenseNovaHead(config)
        a, b = config.mhc_settings["start"], config.mhc_settings["end"]
        for layer in range(config.num_hidden_layers):
            i = self.first_block_idx + layer
            block_type = SenseNovaMHCBlock if a <= layer < b else SenseNovaBlock
            self.modules[i] = block_type(self.modules[i])
        self.caps.update({"supports_tp": False, "loop_calibration_required": True})
