#!/usr/bin/env python3
"""Install the captured runtime source overlay into an isolated package directory."""
import argparse
import hashlib
import json
from pathlib import Path
import shutil
import os
import tempfile

REPO = Path(__file__).resolve().parents[1]


def apply(manifest, target):
    manifest = json.loads(Path(manifest).read_text())
    target = Path(target).resolve()
    for item in manifest["files"]:
        relative = Path(item["target"])
        if relative.is_absolute() or ".." in relative.parts:
            raise ValueError("Overlay target leaves its package directory")
        source = (REPO / item["file"]).resolve()
        if not source.is_relative_to(REPO):
            raise ValueError("Overlay source leaves the repository")
        if hashlib.sha256(source.read_bytes()).hexdigest() != item["sha256"]:
            raise ValueError(f"Overlay payload differs: {item['file']}")
        destination = target / relative
        destination.parent.mkdir(parents=True, exist_ok=True)
        if not destination.resolve().is_relative_to(target):
            raise ValueError("Overlay target resolves outside its package directory")
        # Replace the inode so an isolated tree made with hardlinks does not
        # rewrite its original image/package source.
        with tempfile.NamedTemporaryFile(dir=destination.parent, delete=False) as stream:
            temporary = Path(stream.name)
        try:
            shutil.copyfile(source, temporary)
            temporary.chmod(0o644)
            os.replace(temporary, destination)
        finally:
            temporary.unlink(missing_ok=True)
    return len(manifest["files"])


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("runtime", choices=["apex-awq", "deepseek"])
    parser.add_argument("--target", type=Path, required=True)
    args = parser.parse_args()
    print(apply(REPO / "runtimes" / args.runtime / "overlay-manifest.json", args.target), "files installed")


if __name__ == "__main__":
    main()
