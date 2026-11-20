'Serve a downloaded HY4 Flash EXL3 quant on local P2P CUDA devices.'

import argparse

from collections import deque

from http.server import ThreadingHTTPServer

import json

import os

from pathlib import Path

from queue import Empty

from queue import Queue

import signal

from threading import Event

from threading import Thread

from portable_assets import FixedAssets

from portable_assets import read

from serve_hy4 import Engine as Serving

from serve_hy4 import POOL

from serve_hy4 import LANES

from serve_hy4 import handler

class Engine(Serving):
    def __init__(self, profile, assets, stopped):
        import torch
        from transformers import AutoTokenizer
        from hy4_engram_hash_gpu import fused
        from hy4_exact_grouped_graph import capture_grouped
        from hy4_exact_sections import ExactSections
        from hy4_latency_decode import LatencyDecode
        from hy4_long_decode_tuning import activate
        from hy4_native_generation import NativeGeneration
        from hy4_native_target import NativeTarget
        from hy4_prefill_recall_policy import use_recall
        from hy4_resident_parity_check import align_devices, reset
        from hy4_runner_dispatch import activate_gpu_runner

        variant = profile["variant"]
        n = profile["ranks"]
        if torch.cuda.device_count() != n:
            raise ValueError(f"Expose exactly {n} peer-connected CUDA devices via CUDA_VISIBLE_DEVICES")
        devices = [torch.device("cuda", i) for i in range(n)]
        self.peers = sum(torch.cuda.can_device_access_peer(i, j)
                         for i in range(n) for j in range(n) if i != j)
        if self.peers != n * (n - 1):
            raise ValueError("HY4 requires direct P2P across the selected CUDA devices")
        self.torch, self.reset, self.stopped = torch, reset, stopped
        self.tokenizer = AutoTokenizer.from_pretrained(str(assets.root), local_files_only=True,
                                                       trust_remote_code=False)
        self.fast_target, self.fused_mla = True, True
        self.expert_mode, self.draft_verify, self.use_recall = "gpu_groups", "early", use_recall
        self.name = "hy4-flash-exl3-" + variant
        self.job = "standalone"
        tune = profile["tuning"]
        self.rank_graph_widths = tuple(tune["section_graph_widths"])
        self.exact_fallback_buckets = {int(k): v for k, v in tune["four_lane_sections"].items()}
        self.grouped_replay, self.grouped_replay_limit = None, 0
        self.exact_sections = self.cpu_readback = None
        self.partial_replay_widths = []
        with torch.inference_mode():
            target = NativeTarget(variant, devices, profile["block_ranks"], POOL, (0,) * LANES,
                                  embedding_rank=profile["embedding_rank"],
                                  head_rank=profile["head_rank"], fixed_assets=assets)
            for block in target.blocks[1:]:
                with torch.cuda.device(block.device):
                    block.mlp.load()
            self.runner = NativeGeneration(target)
            self.vision = assets.vision(devices[profile["vision_rank"]])
            self.expert_dispatch = activate_gpu_runner(target, fused=True, compact=True)
            target.engram_read_ahead.single_hash = fused
            runtime = LatencyDecode(target, pipeline=False, graph_widths=self.rank_graph_widths)
            runtime.single, runtime.four = 1 in self.rank_graph_widths, 4 in self.rank_graph_widths
            target.latency_decode = runtime
            runtime.enable_rank_graphs(self.rank_graph_widths)
            self.long_decode = activate(runtime, {int(k): v for k, v in tune["long_decode"].items()})
            physical = {2: (0, 3), 3: (2, 0, 3)}
            self.partial_replay_widths = [w for w in tune["partial_replay_widths"]
                                          if runtime.selected(physical[w])]
            if self.partial_replay_widths:
                if runtime.dense_graphs is None:
                    runtime.enable_rank_graphs(())
                runtime.dense_graphs.partial_lanes = frozenset(self.partial_replay_widths)
            limit = tune["grouped_replay_history_limit"]
            if limit and min(torch.cuda.mem_get_info(d)[0] for d in devices) >= 3 * 2**30:
                try:
                    self.grouped_replay = capture_grouped(target, self.expert_dispatch)
                    self.grouped_replay_limit = limit
                except RuntimeError:
                    self.grouped_replay = None
            if self.exact_fallback_buckets:
                target.latency_decode.head_lane_slices = tune["head_lane_slices"]
                self.exact_sections = ExactSections(target, self.expert_dispatch)
            align_devices(devices)
        self.eos = self.tokenizer.eos_token_id
        self.queue, self.backlog = Queue(maxsize=32), deque()
        self.active = self.last_batch = self.draft_requests = 0

def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--model-dir", required=True, type=Path)
    p.add_argument("--engram-dir", type=Path, help="Optional separate location of the NVMe Engram directory")
    p.add_argument("--profile", required=True, type=Path)
    p.add_argument("--port", default=8152, type=int)
    p.add_argument("--cpu-nice", type=int, choices=range(-20, 20))
    p.add_argument("--check-layout", action="store_true", help="Check the local pack without loading on CUDA")
    args = p.parse_args()
    profile = read(args.profile)
    assets = FixedAssets(args.model_dir, args.engram_dir or args.model_dir / "engram", profile["variant"])
    if args.check_layout:
        print(json.dumps(assets.check_layout()))
        return
    if args.cpu_nice is not None:
        os.setpriority(os.PRIO_PROCESS, 0, args.cpu_nice)
    stopped = Event()
    signal.signal(signal.SIGTERM, lambda *_: stopped.set())
    engine = Engine(profile, assets, stopped)
    server = ThreadingHTTPServer(("127.0.0.1", args.port), handler(engine))
    Thread(target=server.serve_forever, daemon=True).start()
    print(json.dumps(engine.stats()), flush=True)
    try:
        while not stopped.is_set():
            try:
                batch = engine.sample()
            except Empty:
                continue
            engine.active = engine.last_batch = len(batch)
            if batch[0].dfly:
                engine.draft_requests += len(batch)
            try:
                engine.generate(batch)
            except Exception:
                for row in batch:
                    row.updates.put(("error", ""))
                if not stopped.is_set():
                    raise
            finally:
                engine.active = 0
    finally:
        server.shutdown()
        server.server_close()

if __name__ == "__main__":
    main()
