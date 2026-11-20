'Exercise the existing EXL3 Q8 codec on the five HY4 DFly2 cache owners.'

from types import SimpleNamespace

PAGE, LATENT, ROPE, GROUPS, BITS = 256, 512, 64, 16, 8

def codec():
    from exllamav3.ext import exllamav3_ext as ext
    from exllamav3.modules.attention_fn.mla_triton import mla_kv_quant_append

    return ext, mla_kv_quant_append, {"source": "bundled ExLlamaV3"}

def decoder_config(raw):
    cfg = SimpleNamespace(**raw["text_config"])
    cfg.rope_parameters["indexed_attention"] = cfg.rope_parameters.pop("deepseek_sparse_attention")
    cfg.layer_types = ["indexed_attention" if kind == "deepseek_sparse_attention" else kind for kind in cfg.layer_types]
    return cfg
