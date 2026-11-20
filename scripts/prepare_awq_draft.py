#!/usr/bin/env python3
"""Pair the unchanged BF16 DFlash2 head with the selected Apex target embedding."""
import argparse
import json
from pathlib import Path
import shutil


def embedding_location(target):
    index = json.loads((target / "model.safetensors.index.json").read_text())
    key = "model.language_model.embed_tokens.weight"
    return target / index["weight_map"][key], key


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--draft", type=Path, required=True)
    parser.add_argument("--target", type=Path, required=True)
    parser.add_argument("--destination", type=Path, required=True)
    args = parser.parse_args()
    from safetensors import safe_open
    from safetensors.torch import save_file
    target, key = embedding_location(args.target)
    args.destination.mkdir(parents=True, exist_ok=False)
    for source in args.draft.iterdir():
        if source.is_file() and source.suffix in (".json", ".safetensors", ".md"):
            shutil.copy2(source, args.destination / source.name)
    with safe_open(str(target), framework="pt", device="cpu") as tensors:
        embedding = tensors.get_tensor(key)
    save_file({"embed_tokens.weight": embedding}, str(args.destination / "target_embed_tokens.safetensors"))
    with safe_open(str(args.destination / "target_embed_tokens.safetensors"), framework="pt", device="cpu") as tensors:
        import torch
        if not torch.equal(embedding.view(torch.uint8), tensors.get_tensor("embed_tokens.weight").view(torch.uint8)):
            raise RuntimeError("The target embedding did not survive byte-exact staging")
    print(args.destination)


if __name__ == "__main__":
    main()
