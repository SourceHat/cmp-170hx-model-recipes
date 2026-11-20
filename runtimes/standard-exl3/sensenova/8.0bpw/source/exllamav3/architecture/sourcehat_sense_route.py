"""Replay the existing SenseNova router without relaunching its CUDA kernels."""

from weakref import WeakKeyDictionary

import torch


class RouteGraph:
    def __init__(self, operation, residual, stream):
        self.input = residual.clone()
        self.graph = torch.cuda.CUDAGraph()
        current = torch.cuda.current_stream(residual.device)
        with torch.cuda.stream(stream):
            stream.wait_stream(current)
            operation(self.input)
            stream.synchronize()
            self.graph.capture_begin(capture_error_mode="thread_local")
            try:
                self.output = operation(self.input)
            finally:
                self.graph.capture_end()
        current.wait_stream(stream)

    def __call__(self, residual):
        self.input.copy_(residual)
        self.graph.replay()
        return self.output


def make_router(eager, widths):
    captures = WeakKeyDictionary()
    stats = {"captures": 0, "replays": 0, "errors": []}
    streams = {}
    widths = frozenset(widths)

    def forward(router, residual, params, out_dtype=None):
        if (not residual.is_cuda or residual.ndim != 4 or residual.shape[1] != 1
                or residual.shape[0] not in widths or residual.dtype != torch.bfloat16
                or not residual.is_contiguous() or torch.cuda.is_current_stream_capturing()):
            return eager(router, residual, params, out_dtype)
        by_shape = captures.setdefault(router, {})
        key = (residual.device, residual.shape)
        if key not in by_shape:
            if residual.device not in streams:
                streams[residual.device] = torch.cuda.Stream(device=residual.device)
            try:
                by_shape[key] = RouteGraph(lambda x: eager(router, x, params, out_dtype), residual,
                                           streams[residual.device])
                stats["captures"] += 1
            except RuntimeError as error:
                by_shape[key] = None
                if len(stats["errors"]) < 3:
                    stats["errors"].append(str(error)[-1500:])
        graph = by_shape[key]
        if graph is None:
            return eager(router, residual, params, out_dtype)
        stats["replays"] += 1
        return graph(residual)

    return forward, stats
