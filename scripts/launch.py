#!/usr/bin/env python3
"""Render and launch a recipe with explicit devices and configurable networking."""
import argparse
import json
import os
from pathlib import Path
import shutil

REPO = Path(__file__).resolve().parents[1]


def selected_devices(value, count):
    devices = [v.strip() for v in value.split(",")]
    if len(devices) != count or len(set(devices)) != count:
        raise ValueError(f"Select {count} distinct devices in pipeline/layer order")
    if any(not v or not (v.isdecimal() or v.startswith("GPU-")) for v in devices):
        raise ValueError("Use GPU ordinals or GPU UUIDs")
    return devices


def load_recipe(path):
    path = Path(path)
    if not path.is_file():
        path = REPO / "recipes" / str(path) / "recipe.json"
    return json.loads(path.read_text())


def render(recipe, *, devices, runtime_root, model_path, draft_path=None,
           engram_path=None, source_model_path=None, output_dir=None,
           host="127.0.0.1", port=8000):
    devices = selected_devices(devices, recipe["hardware"]["card_count"])
    if not host.strip() or not 1 <= port <= 65535:
        raise ValueError("Provide a bind host and a port between 1 and 65535")
    root = Path(runtime_root).resolve()
    model_path = Path(model_path).resolve()
    output = Path(output_dir or REPO / ".local" / "launches" / recipe["id"]).resolve()
    runtime_id = recipe["runtime"]["id"]
    runtime = root / runtime_id
    python = str(runtime / ".venv" / "bin" / "python")
    env = {"CUDA_VISIBLE_DEVICES": ",".join(devices), "TORCH_CUDA_ARCH_LIST": "8.0"}
    env.update(recipe["launch"]["environment"])
    env.update({"HF_HUB_OFFLINE": "1", "TRANSFORMERS_OFFLINE": "1"})
    cache_root = root / "cache" / runtime_id
    env.update({name: str(cache_root / child) for name, child in [
        ("TORCH_EXTENSIONS_DIR", "torch_extensions"),
        ("TRITON_CACHE_DIR", "triton"), ("VLLM_CACHE_ROOT", "vllm"),
        ("TORCHINDUCTOR_CACHE_DIR", "torchinductor"),
    ]})
    serving = recipe["serving"]
    artifacts = {}
    links = {}
    if runtime_id == "tabby":
        config = json.loads(json.dumps(recipe["engine_config"]))
        config["network"].update(host=host, port=port)
        alias = output / "models" / recipe["model"]["served_name"]
        links[str(alias)] = str(model_path)
        config["model"]["model_dir"] = str(alias.parent)
        config["model"]["model_name"] = alias.name
        artifacts["config.yml"] = json.dumps(config, indent=2) + "\n"
        argv = [python, str(REPO / "scripts" / "serve_tabby.py"),
                "--runtime", str(runtime), "--config", str(output / "config.yml")]
        if serving.get("output_chunk_tokens") is not None:
            argv += ["--output-chunk-tokens", str(serving["output_chunk_tokens"])]
    elif runtime_id == "apex-awq":
        args = recipe["engine_config"]["argv"]
        if draft_path is None:
            raise ValueError("Apex AWQ requires --draft-path for its prepared BF16 DFlash2 head")
        replacements = {"@MODEL@": str(model_path),
                        "@DRAFT@": str(Path(draft_path).resolve()) if draft_path else "",
                        "@HOST@": host, "@PORT@": str(port)}
        argv = [python, str(REPO / "scripts" / "serve_vllm.py"),
                "--runtime", str(runtime), "--engine", runtime_id, "--"]
        argv += [replace_paths(arg, replacements) for arg in args]
        overlay = runtime / "packages"
        env["PYTHONPATH"] = str(overlay) + os.pathsep + str(REPO / "runtimes" / runtime_id / "helpers")
    elif runtime_id == "deepseek":
        if engram_path is None or source_model_path is None:
            raise ValueError("DeepSeek requires --source-model-path and --engram-path for its prepared assets")
        env.update({"MODEL_DIR": str(model_path),
                    "SOURCE_MODEL_DIR": str(Path(source_model_path).resolve()),
                    "ENGRAM_DIR": str(Path(engram_path).resolve()),
                    "DEVICES": ",".join(devices), "BIND_ADDRESS": host, "PORT": str(port)})
        argv = ["docker", "compose", "-f", str(REPO / "recipes" / recipe["id"] / "compose.yaml"),
                "up", "--build", "--exit-code-from", "deepseek"]
    else:
        raise ValueError(f"Unknown runtime: {runtime_id}")
    return {"argv": argv, "environment": env, "output_dir": str(output),
            "artifacts": artifacts, "symlinks": links, "cwd": str(REPO)}


def replace_paths(value, replacements):
    if value.lstrip().startswith(("{", "[")):
        def replace_node(node):
            if isinstance(node, dict):
                return {key: replace_node(child) for key, child in node.items()}
            if isinstance(node, list):
                return [replace_node(child) for child in node]
            if isinstance(node, str):
                for old, new in replacements.items():
                    node = node.replace(old, new)
            return node

        # Substitute inside the parsed object so path quotes stay valid JSON.
        return json.dumps(replace_node(json.loads(value)), separators=(",", ":"))
    for old, new in replacements.items():
        value = value.replace(old, new)
    return value


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("recipe", help="Recipe id or path to recipe.json")
    parser.add_argument("--devices", required=True, help="Ordered ordinals or UUIDs, comma-separated")
    parser.add_argument("--host", default="127.0.0.1", help="Bind host (default: 127.0.0.1)")
    parser.add_argument("--port", type=int, default=8000, help="Listen port (default: 8000)")
    parser.add_argument("--runtime-root", type=Path, default=REPO / ".local" / "runtimes")
    parser.add_argument("--model-path", type=Path, required=True)
    parser.add_argument("--draft-path", type=Path)
    parser.add_argument("--engram-path", type=Path)
    parser.add_argument("--source-model-path", type=Path, help="Original checkpoint for the DeepSeek TP3 view")
    parser.add_argument("--output-dir", type=Path)
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()
    try:
        plan = render(load_recipe(args.recipe), devices=args.devices,
                      runtime_root=args.runtime_root, model_path=args.model_path,
                      draft_path=args.draft_path, engram_path=args.engram_path,
                      source_model_path=args.source_model_path, output_dir=args.output_dir,
                      host=args.host, port=args.port)
    except (ValueError, OSError) as error:
        parser.error(str(error))
    if args.dry_run:
        print(json.dumps(plan, indent=2))
        return
    executable = shutil.which(plan["argv"][0])
    if executable is None:
        parser.error("Install the matching runtime or Docker; see docs/REPRODUCING.md")
    out = Path(plan["output_dir"])
    out.mkdir(parents=True, exist_ok=True)
    for name, raw in plan["artifacts"].items():
        (out / name).write_text(raw)
    for alias, target in plan["symlinks"].items():
        alias = Path(alias)
        alias.parent.mkdir(parents=True, exist_ok=True)
        if alias.is_symlink() and alias.resolve() == Path(target):
            continue
        if alias.exists() or alias.is_symlink():
            parser.error(f"A different model already occupies {alias}")
        alias.symlink_to(target, target_is_directory=True)
    env = dict(os.environ, **plan["environment"])
    os.execve(executable, [executable, *plan["argv"][1:]], env)


if __name__ == "__main__":
    main()
