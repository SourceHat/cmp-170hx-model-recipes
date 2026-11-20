'Compare bounded HY4 fixtures with the pinned eager decoder.'

import ast

from pathlib import Path

from types import SimpleNamespace

import torch

from torch import nn

from torch.nn import functional as F

def official():
    data = Path(__file__).with_name("hy4_reference.txt").read_bytes()
    identity = "Transformers c2ec850510a37978ea83df226589623d5f2be776"
    classes = {"HYV4Flash" + name for name in (
        "RMSNorm", "RotaryEmbedding", "MLP", "Experts", "TopkRouter", "MoE", "CompressedIndexer",
        "Attention", "UnweightedRMSNorm", "HyperConnection", "HyperHead", "DecoderLayer")}
    helpers = {"rotate_half", "apply_rotary_pos_emb", "_apply_partial_rotary_pos_emb",
               "repeat_kv", "eager_attention_forward"}
    selected = [
        n for n in ast.parse(data).body
        if isinstance(n, (ast.FunctionDef, ast.ClassDef)) and n.name in classes | helpers
    ]
    if {n.name for n in selected} != classes | helpers:
        raise ValueError("The expected eager reference is incomplete")
    for node in selected:
        node.decorator_list.clear()
        if isinstance(node, ast.ClassDef):
            for attr in node.body:
                if isinstance(attr, ast.FunctionDef) and attr.name == "forward":
                    attr.decorator_list.clear()
    scope = dict(torch=torch, nn=nn, F=F, ACT2FN={"silu": F.silu}, maybe_autocast=torch.autocast,
                 GradientCheckpointingLayer=nn.Module,
                 ALL_ATTENTION_FUNCTIONS=SimpleNamespace(get_interface=lambda name, fallback: fallback))
    body = ast.Module(body=[ast.parse("from __future__ import annotations").body[0], *selected], type_ignores=[])
    exec(compile(body, "<pinned-hy4-prefix>", "exec"), scope)
    return scope, identity

def norm(x, w, eps):
    f = x.float()
    return w * (f * torch.rsqrt(f.square().mean(dim=-1, keepdim=True) + eps)).to(x.dtype)
