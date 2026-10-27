#!/usr/bin/env python3
"""Register the captured SM80 backend before starting the native vLLM API."""
import argparse
from pathlib import Path
import runpy
import sys


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--runtime", type=Path, required=True)
    parser.add_argument("--engine", choices=["apex-awq", "deepseek"], required=True)
    args, rest = parser.parse_known_args()
    sys.path.insert(0, str(args.runtime.resolve() / "packages"))
    if args.engine == "apex-awq":
        import meshify_sm80_nope8  # Registers the measured eight-bit attention backend.
    sys.argv = ["vllm-api-server", *(rest[1:] if rest[:1] == ["--"] else rest)]
    runpy.run_module("vllm.entrypoints.launchers.api_server.entry", run_name="__main__")


if __name__ == "__main__":
    main()
