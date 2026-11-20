'Replay a group of resident HY4 blocks between host Engram reads.'

from dataclasses import dataclass

from dataclasses import fields

from itertools import groupby

import torch

import triton

import triton.language as tl

from hy4_cached_index import GROUP_TILE

from hy4_cached_index import pack_tile

from hy4_paged_q8_probe import PAGE

from hy4_sliding_runtime import WINDOW

@triton.jit
def store_closed(BITS, SCALES, PACKED, MASS, POS, TABLE,
                 PAGES: tl.constexpr, STRIDE: tl.constexpr,
                 TILE: tl.constexpr, RATIO: tl.constexpr, DIM: tl.constexpr):
    lane = tl.program_id(0)
    token = tl.load(POS + lane)
    if token % RATIO == RATIO - 1:
        group = token // RATIO
        page = tl.load(TABLE + lane * PAGES + group // STRIDE)
        row = page * STRIDE + group % STRIDE
        src = lane * TILE + group % TILE
        d = tl.arange(0, DIM)
        tl.store(BITS + row * DIM + d, tl.load(PACKED + src * DIM + d))
        tl.store(SCALES + row, tl.load(MASS + src))

def append_index(ix, raw, meta):
    """Use stable addresses and only commit a complete native four-token group."""
    lanes, slots = meta.physical, meta.slots
    ratio = ix.indexer.compress_ratio
    point = slots % ratio
    ix.first[lanes] = torch.where(point == 0, meta.phases, ix.first[lanes])
    ix.partial[lanes, point] = raw
    # Keep the native pooling GEMM geometry used by prompt and eager decode.
    row = torch.arange(len(slots), device=raw.device)
    group = (slots // ratio) % GROUP_TILE
    tile = raw.new_zeros((len(slots), GROUP_TILE, ratio, raw.shape[-1]))
    first = meta.phases.new_zeros((len(slots), GROUP_TILE))
    tile[row, group] = ix.partial[lanes]
    first[row, group] = ix.first[lanes]
    bits, scales = pack_tile(ix.indexer, ix.inv, tile, first)
    store_closed[(len(slots),)](ix.bits, ix.scales, bits, scales, slots, meta.shared,
                                meta.shared.shape[1], PAGE // ratio, GROUP_TILE, ratio, raw.shape[-1])
    ix.lengths[lanes] = slots + 1

@dataclass(frozen=True)
class DenseMeta:
    physical: torch.Tensor
    slots: torch.Tensor
    phases: torch.Tensor
    shared: torch.Tensor
    rotary: torch.Tensor
    index_picks: torch.Tensor
    slide_picks: torch.Tensor
    slide_starts: torch.Tensor
    index_starts: torch.Tensor

    @classmethod
    def prepare(cls, wave, sliding, width):
        slots = wave.slots[:, None]
        index = torch.arange(width, device=slots.device, dtype=torch.int32)
        index = index.expand(len(slots), -1).masked_fill(index > slots, -1)
        logical = slots + sliding.tail[-min(width, WINDOW):]
        ring = logical.remainder(sliding.capacity).masked_fill(logical < 0, -1).int()
        starts = wave.slots.int()
        return cls(wave.physical, wave.slots, wave.phases, wave.shared, wave.rotary,
                   index, ring, starts.remainder(sliding.capacity), starts)

    def tensors(self):
        return tuple(getattr(self, f.name) for f in fields(self))

class RankGraph:
    def __init__(self, operation, hidden, meta, stream, *, shared=False):
        self.operation = operation
        self.input = torch.empty_like(hidden)
        self.shared = shared
        self.meta = meta if shared else DenseMeta(*(torch.empty_like(v) for v in meta.tensors()))
        self.buffers = self.meta.tensors()
        self.update(hidden, meta)
        self.graph = torch.cuda.CUDAGraph()
        current = torch.cuda.current_stream(hidden.device)
        with torch.cuda.stream(stream):
            stream.wait_stream(current)
            # Run the exact same row first to resolve CUDA and Triton kernel setup.
            self.operation(self.input, self.meta)
            stream.synchronize()
            self.graph.capture_begin(capture_error_mode="thread_local")
            try:
                self.output = self.operation(self.input, self.meta)
            finally:
                self.graph.capture_end()
        current.wait_stream(stream)

    def update(self, hidden, meta):
        self.input.copy_(hidden)
        if not self.shared:
            torch._foreach_copy_(self.buffers, meta.tensors())

    def __call__(self, hidden, meta):
        self.update(hidden, meta)
        self.graph.replay()
        return self.output

class SectionGraphs:
    """One graph for each span of layers between Engram waits."""

    def __init__(self, runtime, lanes):
        self.runtime = runtime
        self.lanes = frozenset(lanes)
        self.partial_lanes = frozenset()
        self.partial_limit = 256
        self.long_lanes = frozenset()
        self.sections = []
        self.long_sections = []
        self.sliding = []
        self.streams = runtime.streams
        self.graphs = {}
        self.errors = {}
        limits = []
        for _, blocks in runtime.stages:
            sections = []
            for block in blocks:
                if not sections or block.engram is not None:
                    sections.append([])
                sections[-1].append(block)
                if block.sparse:
                    ix = block.attention.index.indexer
                    limits.append(ix.group_topk * ix.compress_ratio)
            self.sections.append(sections)
            self.long_sections.append([tuple(span) for section in sections
                                       for _, span in groupby(section, key=lambda b: b.sparse)])
            self.sliding.append(next(b.attention.cache for b in blocks if not b.sparse))
        self.limit = min(limits, default=2048)

    def supports(self, wave):
        history, width = max(wave.starts), len(wave.starts)
        if history >= self.limit:
            return width in self.long_lanes
        return width in self.lanes or (history < self.partial_limit and width in self.partial_lanes)

    def stage(self, rank, wave, table, hidden, inject):
        largest = max(wave.starts)
        long = largest >= self.limit
        width = WINDOW if long else min(self.limit, max(64, 1 << largest.bit_length()))
        sections = self.long_sections[rank] if long else self.sections[rank]
        meta = DenseMeta.prepare(wave, self.sliding[rank], width)
        for n, blocks in enumerate(sections):
            if blocks[0].engram is not None:
                hidden = inject(blocks[0].engram, hidden)
            if long and blocks[0].sparse:
                # Sparse recall still depends on history; sliding blocks always use the same window.
                for block in blocks:
                    hidden = self.runtime.layer(block, hidden, wave, table)
                continue
            for block in blocks:
                if block.sparse:
                    block.attention.index.table = table
            key = (rank, n, len(wave.starts), -width if long else width)
            graph = self.graphs.get(key)
            if graph is None and key not in self.errors:
                if torch.cuda.mem_get_info(hidden.device)[0] < 2 * 1024**3:
                    self.errors[key] = "Insufficient free VRAM for a new graph"
                else:
                    def operation(row, inputs, blocks=blocks):
                        for block in blocks:
                            row = self.runtime.layer(block, row, inputs, None, inputs)
                        return row

                    try:
                        graph = RankGraph(operation, hidden, meta, self.streams[hidden.device])
                        self.graphs[key] = graph
                    except RuntimeError as error:
                        self.errors[key] = str(error)
            if graph is not None:
                hidden = graph(hidden, meta)
            else:
                for block in blocks:
                    hidden = self.runtime.layer(block, hidden, wave, table)
        return hidden
