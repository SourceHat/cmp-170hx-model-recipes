"""Reuse pinned page rows and block while sampled tokens arrive."""

import torch

def tensor_version(tensor):
    # EXL3 replaces inference-mode page rows when an assignment changes.
    return None if torch.is_inference(tensor) else tensor._version

class PinnedPageRows:
    def __init__(self, *, pinned=True):
        self.pinned = pinned
        self.sources = ()
        self.versions = ()
        self.buffer = None

    def get(self, sources, width):
        sources = tuple(sources)
        versions = tuple(tensor_version(row) for row in sources)
        shape = (len(sources), width)
        if (self.buffer is not None and self.buffer.shape == shape and versions == self.versions
                and len(sources) == len(self.sources) and all(a is b for a, b in zip(sources, self.sources))):
            return self.buffer
        # Don't rewrite a buffer that a previous transfer could still be reading.
        table = torch.zeros(shape, dtype=torch.int32, device="cpu", pin_memory=self.pinned)
        for i, row in enumerate(sources):
            count = min(width, row.shape[-1])
            table[i:i + 1, :count].copy_(row[:, :count])
        self.sources, self.versions, self.buffer = sources, versions, table
        return table

def wait_for_samples(generator, device):
    event = getattr(generator, "_cpu_wait_sample_event", None)
    if event is None or event.device != device:
        event = generator._cpu_wait_sample_event = torch.cuda.Event(blocking=True)
    event.record(torch.cuda.current_stream(device))
    event.synchronize()
