'One shared HY4 indexed-cache page allocation for four independent requests.'

from dataclasses import dataclass

import heapq

from weakref import WeakSet

import torch

from hy4_paged_q8_probe import BITS

from hy4_paged_q8_probe import GROUPS

from hy4_paged_q8_probe import LATENT

from hy4_paged_q8_probe import PAGE

from hy4_paged_q8_probe import ROPE

CONTEXT = 1048576

LANES = 4

@dataclass(frozen=True)
class Layout:
    generation: int
    table: torch.Tensor
    lengths: torch.Tensor

class SharedPool:
    """A page ID has one request owner, shared by all cache-owning blocks."""

    def __init__(self, tokens, native_context=CONTEXT):
        if (type(tokens) is not int or tokens < PAGE or tokens % PAGE or
                type(native_context) is not int or not 0 < native_context <= CONTEXT):
            raise ValueError("HY4 requires a page-aligned pool and native context")
        self.capacity = tokens // PAGE
        self.context = native_context
        self.free = list(range(self.capacity))
        self.pages = [[] for _ in range(LANES)]
        self.lengths = (0,) * LANES
        self.pending = None
        self.generation = 0
        self.layers = WeakSet()

    @staticmethod
    def required(length):
        return (length + PAGE - 1) // PAGE

    def reserve(self, widths):
        if (self.pending is not None or len(widths) != LANES or
                any(type(v) is not int or v < 0 for v in widths) or not any(widths)):
            raise ValueError("Reserve once per target or verify wave")
        ends = tuple(a + b for a, b in zip(self.lengths, widths, strict=True))
        new = [self.required(end) - len(pages) for end, pages in zip(ends, self.pages, strict=True)]
        if max(ends) > self.context:
            raise ValueError("HY4 request exceeds the original maximum context")
        if sum(new) > len(self.free):
            raise ValueError("Shared HY4 Q8 cache has insufficient free pages")
        for slots, extra in zip(self.pages, new, strict=True):
            slots.extend(heapq.heappop(self.free) for _ in range(extra))
        self.pending = ends
        self.generation += 1

    def commit(self, kept):
        if (self.pending is None or len(kept) != LANES or any(type(n) is not int or not 0 <= n <= end - old
                for n, end, old in zip(kept, self.pending, self.lengths, strict=True))):
            raise ValueError("Only a prefix of each reserved verify lane can commit")
        ends = tuple(a + b for a, b in zip(self.lengths, kept, strict=True))
        if any(any(written < end for written, end in zip(layer.visible_lengths(), ends, strict=True))
               for layer in self.layers):
            raise ValueError("Every layer must write the accepted rows before they can commit")
        self.lengths = ends
        for length, slots in zip(self.lengths, self.pages, strict=True):
            used = self.required(length)
            for page in slots[used:]:
                heapq.heappush(self.free, page)
            del slots[used:]
        self.pending = None
        self.generation += 1

    def release(self, lane):
        if self.pending is not None or type(lane) is not int or not 0 <= lane < LANES:
            raise ValueError("Release an idle request only between verification waves")
        for page in self.pages[lane]:
            heapq.heappush(self.free, page)
        self.pages[lane].clear()
        self.lengths = tuple(0 if i == lane else n for i, n in enumerate(self.lengths))
        self.generation += 1

    def layout(self, device, *, tentative=False):
        lengths = self.pending if tentative else self.lengths
        if lengths is None:
            raise ValueError("No outstanding HY4 verification wave")
        width = self.required(self.context)
        table = [r + [-1] * (width - len(r)) for r in self.pages]
        return Layout(self.generation, torch.tensor(table, dtype=torch.int32, device=device),
                      torch.tensor(lengths, dtype=torch.int32, device=device))

    def locate(self, layout, lanes, logical):
        if (layout.generation != self.generation or lanes.ndim != 1 or logical.ndim != 2 or
                len(logical) != len(lanes) or (lanes < 0).any() or (lanes >= LANES).any() or
                logical.device != layout.table.device or lanes.device != layout.table.device or
                logical.dtype not in (torch.int32, torch.int64) or lanes.dtype not in (torch.int32, torch.int64)):
            raise ValueError("Stale or invalid HY4 page layout")
        visible = logical >= 0
        if ((logical < -1) | (visible & (logical >= layout.lengths[lanes, None]))).any():
            raise ValueError("HY4 query would expose an uncommitted row")
        col = logical.clamp_min(0).long()
        page = layout.table[lanes[:, None], col // PAGE].long()
        if (visible & (page < 0)).any():
            raise RuntimeError("Live HY4 row does not have a physical page")
        return page.clamp_min(0), col % PAGE, visible

class SharedQ8Latents:
    """A layer's real EXL3 Q8 and BF16 RoPE planes use the common physical IDs."""

    def __init__(self, pool, kernel, device):
        if pool.pending is not None or any(pool.lengths):
            raise ValueError("Every cache layer must be created before the first append")
        self.pool, self.kernel, self.device = pool, kernel, torch.device(device)
        n = pool.capacity
        self.planes = (torch.empty((n, PAGE, GROUPS * BITS), dtype=torch.int32, device=device),
                       torch.empty((n, PAGE, GROUPS), dtype=torch.float16, device=device),
                       torch.empty((n, PAGE, 1, ROPE), dtype=torch.bfloat16, device=device))
        self.generation, self.updated = -1, []
        pool.layers.add(self)

    def visible_lengths(self):
        return self.updated if self.generation == self.pool.generation else self.pool.lengths

    def append(self, layout, lanes, start, latent, rope):
        b, width, dim = latent.shape
        if (self.pool.pending is None or dim != LATENT or not width or rope.shape != (b, width, ROPE) or
                latent.device != self.device or rope.device != self.device or rope.dtype != torch.bfloat16 or
                lanes.shape != start.shape or b != len(lanes) or lanes.unique().numel() != b or
                start.dtype != torch.int32 or start.device != self.device or (start < 0).any()):
            raise ValueError("Invalid HY4 Q8 write")
        # Validate the entire write span before touching the shared planes.
        last = start + width - 1
        self.pool.locate(layout, lanes, torch.stack((start, last), dim=1))
        current = list(self.visible_lengths())
        lane_ids = lanes.tolist()
        if start.tolist() != [current[i] for i in lane_ids]:
            raise ValueError("Append each layer's next consecutive HY4 rows")
        self.kernel(latent.half().contiguous(), rope.contiguous(), *self.planes,
                    layout.table.index_select(0, lanes).contiguous(), start.contiguous(), BITS)
        for lane in lane_ids:
            current[lane] += width
        self.generation, self.updated = self.pool.generation, current

    def read(self, layout, lanes, logical):
        page, offset, visible = self.pool.locate(layout, lanes, logical)
        checked = torch.tensor(self.visible_lengths(), dtype=torch.int32, device=self.device)
        if (visible & (logical >= checked[lanes, None])).any():
            raise ValueError("HY4 query would expose an unwritten row")
        return tuple(x[page, offset].flatten(2).masked_fill(~visible[..., None], 0) for x in self.planes)
