"""Route capture by physical weight owner and require every native visit."""

from collections import Counter
from contextlib import contextmanager


class VisitCapture:
    def __init__(self, order, physical_layers):
        selected = set(physical_layers)
        ordinal = Counter()
        expected = []
        for physical in order:
            if physical in selected:
                expected.append((physical, ordinal[physical]))
            ordinal[physical] += 1
        if not selected or not selected.issubset(ordinal):
            raise ValueError("Calibration selection must name native physical layers")
        self.expected = tuple(expected)
        self.by_layer = {layer: {} for layer in sorted(selected)}
        self.batches = set()
        self.cursor = None
        self.tainted = False

    @contextmanager
    def batch(self, batch_id):
        if self.tainted or self.cursor is not None or batch_id in self.batches:
            raise ValueError("Calibration batch is already committed, active or tainted")
        self.cursor = 0
        try:
            yield self
            if self.cursor != len(self.expected):
                raise ValueError("Incomplete SenseNova calibration traversal")
            self.batches.add(batch_id)
        except BaseException:
            # A failed batch may already have added rows to its Hessians. Never publish those sums.
            self.tainted = True
            raise
        finally:
            self.cursor = None

    @contextmanager
    def visit(self, physical, ordinal, params):
        if physical not in self.by_layer:
            yield
            return
        i = self.cursor
        if (i is None or i >= len(self.expected) or self.expected[i] != (physical, ordinal) or
                "capture" in params or params.get("prefill")):
            raise ValueError("Calibration must use a full forward through the native visits")
        params["capture"] = self.by_layer[physical]
        try:
            yield
            self.cursor += 1
        finally:
            del params["capture"]

    def finish(self):
        if self.tainted or self.cursor is not None or not self.batches:
            raise ValueError("Only completed native calibration batches may be packed")
        return self.by_layer
