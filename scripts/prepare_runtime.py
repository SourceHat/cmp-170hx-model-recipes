#!/usr/bin/env python3
"""Build the shared Tabby runtime in an isolated local directory."""
import argparse
import json
from pathlib import Path
import subprocess

REPO = Path(__file__).resolve().parents[1]


def build_plan(runtime, root, python="python3.12", torch_index="https://download.pytorch.org/whl/cu131"):
    root = Path(root).resolve() / runtime
    interpreter = str(root / ".venv" / "bin" / "python")
    pip = [interpreter, "-m", "pip"]
    constraints = str(REPO / "runtimes" / runtime / "constraints.txt")
    commands = [[python, "-m", "venv", str(root / ".venv")],
                pip + ["install", "--upgrade", "pip", "setuptools", "wheel", "packaging", "ninja"],
                pip + ["install", "torch==2.14.0", "--index-url", torch_index]]
    if runtime == "tabby":
        sources = [
            ("tabbyapi", "https://github.com/theroyallab/tabbyAPI.git", "be74bf0a00bcb3a518e6feb7606f150c189be637", "tabbyapi.patch"),
            ("exllamav3", "https://github.com/turboderp-org/exllamav3.git", "d3739fd393337b1ff4d6c2a342b12f0c87a9592f", "exllamav3.patch"),
        ]
        for name, url, revision, patch in sources:
            source = str(root / name)
            patch = str(REPO / "runtimes" / "tabby" / patch)
            commands += [["git", "clone", "--no-checkout", url, source],
                         ["git", "-C", source, "checkout", "--detach", revision],
                         ["git", "-C", source, "apply", "--check", patch],
                         ["git", "-C", source, "apply", patch]]
        commands += [pip + ["install", "-c", constraints, "-e", str(root / "tabbyapi")],
                     pip + ["install", "--no-build-isolation", "-c", constraints, "-e", str(root / "exllamav3")]]
    else:
        raise ValueError("Use the pinned base/build and overlay instructions for vLLM runtimes")
    return {"directory": str(root), "commands": commands,
            "environment": {"TORCH_CUDA_ARCH_LIST": "8.0", "MAX_JOBS": "4"}}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("runtime", choices=["tabby"])
    parser.add_argument("--root", type=Path, default=REPO / ".local" / "runtimes")
    parser.add_argument("--python", default="python3.12")
    parser.add_argument("--torch-index", default="https://download.pytorch.org/whl/cu131")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()
    plan = build_plan(args.runtime, args.root, args.python, args.torch_index)
    if args.dry_run:
        print(json.dumps(plan, indent=2))
        return
    root = Path(plan["directory"])
    if root.exists():
        parser.error("Choose a fresh runtime directory; existing builds are preserved")
    root.mkdir(parents=True)
    import os
    environment = dict(os.environ, **plan["environment"])
    for command in plan["commands"]:
        subprocess.run(command, check=True, env=environment)
    print(root)


if __name__ == "__main__":
    main()
