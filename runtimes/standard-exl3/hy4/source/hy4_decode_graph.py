'Replay a resident CUDA expert block without rebuilding its launch sequence.'

import torch

class DecodeGraph:
    def __init__(self, operation, example, stream):
        device = example.device
        current = torch.cuda.current_stream(device)
        self.input = torch.empty_like(example).contiguous()
        self.input.copy_(example)
        self.graph = torch.cuda.CUDAGraph()
        with torch.cuda.stream(stream):
            stream.wait_stream(current)
            operation(self.input)
            # The cooperative EXL3 kernels must be tuned before CUDA capture.
            stream.synchronize()
            self.graph.capture_begin(capture_error_mode="thread_local")
            try:
                self.output = operation(self.input)
            finally:
                self.graph.capture_end()
        current.wait_stream(stream)

    def __call__(self, view):
        self.input.copy_(view)
        self.graph.replay()
        return self.output

class GraphExperts:
    def __init__(self, operation, stream, widths):
        self.operation, self.widths = operation, frozenset(widths)
        self.stream = stream
        self.graphs = {}

    def prepare(self, lanes, example):
        if lanes in self.widths and lanes not in self.graphs:
            self.graphs[lanes] = DecodeGraph(self.operation, example, self.stream)

    def __call__(self, hidden):
        selected = self.graphs.get(hidden.shape[0])
        return self.operation(hidden) if selected is None else selected(hidden)

    decode = __call__
