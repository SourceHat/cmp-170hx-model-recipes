#!/usr/bin/env python3
"""Download a pinned recipe checkpoint and emit its artifact preparation manifest."""
import argparse
import hashlib
import json
from pathlib import Path

from launch import load_recipe


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("recipe")
    parser.add_argument("--directory", type=Path, required=True)
    parser.add_argument("--draft", action="store_true")
    args = parser.parse_args()
    recipe = load_recipe(args.recipe)
    source = recipe["draft_model"] if args.draft else recipe["model"]
    from huggingface_hub import HfApi, snapshot_download
    info = HfApi().model_info(source["hf_repo"], revision=source["revision"], files_metadata=True)
    if info.sha != source["revision"]:
        parser.error("The resolved checkpoint revision differs from the recipe")
    root = args.directory.resolve()
    snapshot_download(source["hf_repo"], revision=source["revision"], local_dir=root)
    rows = []
    for entry in info.siblings:
        p = root / entry.rfilename
        if not p.is_file():
            continue
        row = {"name": entry.rfilename, "bytes": p.stat().st_size}
        if entry.lfs:
            row["lfs_sha256"] = entry.lfs.sha256
        else:
            row["sha256"] = hashlib.sha256(p.read_bytes()).hexdigest()
        rows.append(row)
    manifest = {"repository": source["hf_repo"], "revision": info.sha,
                "directory": str(root), "files": rows}
    destination = root.parent / (root.name + "-download.json")
    destination.write_text(json.dumps(manifest, indent=2) + "\n")
    print(destination)


if __name__ == "__main__":
    main()
