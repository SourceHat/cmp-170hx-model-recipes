#!/usr/bin/env python3
"""Load the selected native MTP recipe in the pinned, patched TabbyAPI."""
import argparse
import os
from pathlib import Path
import sys


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--runtime", type=Path, required=True)
    parser.add_argument("--config", type=Path, required=True)
    parser.add_argument("--output-chunk-tokens", type=int)
    args = parser.parse_args()
    root = args.runtime.resolve()
    repo = Path(__file__).resolve().parents[1]
    sys.path[:0] = [str(root / "tabbyapi"), str(root / "exllamav3"),
                   str(repo / "runtimes" / "tabby" / "helpers")]
    import common.model as model
    from endpoints.OAI.utils import chat_completion
    from backends.exllamav3.model import ExllamaV3Container
    from backends.exllamav3 import model as backend
    from meshify_decode_budget import install as install_budget
    from meshify_qwen_compat import install as install_qwen_compat
    from responses_compat import install as install_responses_compat
    import responses_compat
    from meshify_prefix_diagnostics import install as install_prefix_diagnostics
    from meshify_prefix_metrics import install as install_prefix_metrics
    from endpoints import server
    if args.output_chunk_tokens is not None:
        install_budget(ExllamaV3Container, args.output_chunk_tokens)
    install_qwen_compat(model, chat_completion)
    install_prefix_metrics(backend)
    original_setup = server.setup_app

    def setup_app(*args, **kwargs):
        app = original_setup(*args, **kwargs)
        install_responses_compat(app)
        install_prefix_diagnostics(app, chat_completion, backend, responses=responses_compat)
        return app

    server.setup_app = setup_app
    os.chdir(root / "tabbyapi")
    sys.argv = ["main.py", "--config", str(args.config.resolve())]
    from main import entrypoint
    entrypoint()


if __name__ == "__main__":
    main()
