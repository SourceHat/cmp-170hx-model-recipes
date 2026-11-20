'Native HY4 sliding attention with bounded EXL3 Q8 KV and ragged rollback.'

import torch

from hy4_paged_q8_probe import BITS

from hy4_paged_q8_probe import GROUPS

from hy4_paged_q8_probe import LATENT

from hy4_paged_q8_probe import PAGE

from hy4_paged_q8_probe import ROPE

from hy4_shared_pool import CONTEXT

from hy4_shared_pool import LANES

from mla_eager_reference import projected_attention

WINDOW = 512

VERIFY = 6

class SlidingQ8:
    def __init__(self, kernel, device, context=CONTEXT):
        if type(context) is not int or not 0 < context <= CONTEXT:
            raise ValueError("Invalid native HY4 context")
        self.kernel, self.context = kernel, context
        # Keep the previous window intact while six trial rows are written.
        pages = (WINDOW + VERIFY + PAGE - 1) // PAGE
        self.capacity = pages * PAGE
        base = torch.arange(LANES * pages, dtype=torch.int32, device=device).view(LANES, pages)
        self.device = base.device
        self.table = base.repeat(1, 2)
        self.planes = (torch.empty((LANES * pages, PAGE, GROUPS * BITS), dtype=torch.int32, device=device),
                       torch.empty((LANES * pages, PAGE, GROUPS), dtype=torch.float16, device=device),
                       torch.empty((LANES * pages, PAGE, 1, ROPE), dtype=torch.bfloat16, device=device))
        self.tail = torch.arange(1 - WINDOW, 1, device=device)
        self.lengths = (0,) * LANES
        self.pending = None
        self.written = None

    def _lanes(self, lanes):
        if (not lanes or any(type(i) is not int or not 0 <= i < LANES for i in lanes)
                or len(set(lanes)) != len(lanes)):
            raise ValueError("Use distinct HY4 request lanes")
        return torch.tensor(lanes, dtype=torch.long, device=self.device)

    def _store(self, lanes, start, latent, rope):
        b, width, dim = latent.shape
        if (not 0 < width <= WINDOW or (b, dim) != (len(lanes), LATENT)
                or rope.shape != (b, width, ROPE) or rope.dtype != torch.bfloat16
                or latent.device != self.device or rope.device != self.device):
            raise ValueError("Invalid HY4 sliding Q8 rows")
        positions = torch.tensor(start, dtype=torch.int32, device=self.device).remainder_(self.capacity)
        self.kernel(latent.half().contiguous(), rope.contiguous(), *self.planes,
                    self.table.index_select(0, self._lanes(lanes)), positions, BITS)

    def seed(self, lanes, ends, latent, rope):
        self._lanes(lanes)
        width = latent.shape[1]
        if (self.pending is not None or len(ends) != len(lanes)
                or any(self.lengths[i] or type(end) is not int or not 0 < end <= self.context
                       or min(end, WINDOW) != width for i, end in zip(lanes, ends, strict=True))):
            raise ValueError("Seed only the final native window of an empty request")
        self._store(lanes, [end - width for end in ends], latent, rope)
        lengths = list(self.lengths)
        for lane, end in zip(lanes, ends, strict=True):
            lengths[lane] = end
        self.lengths = tuple(lengths)

    def begin(self, widths):
        if (self.pending is not None or len(widths) != LANES or not any(widths)
                or any(type(w) is not int or not 0 <= w <= VERIFY for w in widths)):
            raise ValueError("Reserve one native target or DFly2 verification wave")
        ends = tuple(a + b for a, b in zip(self.lengths, widths, strict=True))
        if max(ends) > self.context:
            raise ValueError("HY4 request exceeds native context")
        self.pending, self.written = ends, list(self.lengths)

    def append(self, lanes, latent, rope):
        self._lanes(lanes)
        width = latent.shape[1]
        if (self.written is None or not 0 < width <= VERIFY
                or any(self.written[i] + width > self.pending[i] for i in lanes)):
            raise ValueError("HY4 sliding append exceeds the reserved wave")
        self._store(lanes, [self.written[i] for i in lanes], latent, rope)
        for lane in lanes:
            self.written[lane] += width

    def _end(self, lanes, tentative):
        ends = self.written if tentative else self.lengths
        if ends is None:
            raise ValueError("No HY4 sliding trial is active")
        return torch.tensor([ends[i] for i in lanes], dtype=torch.long, device=self.device)

    def window(self, lanes, *, tentative=False):
        self._lanes(lanes)
        return (self._end(lanes, tentative)[:, None] + self.tail - 1).clamp_min_(-1)

    def read(self, lanes, slots, *, tentative=False):
        i = self._lanes(lanes)
        ends = self._end(lanes, tentative)[:, None]
        if (slots.ndim != 2 or slots.shape[0] != len(lanes) or slots.device != self.device
                or slots.dtype not in (torch.int32, torch.int64)):
            raise ValueError("Invalid HY4 sliding key coordinates")
        valid = slots >= 0
        if ((slots < -1) | (valid & ((slots < ends - WINDOW) | (slots >= ends)))).any():
            raise ValueError("HY4 sliding read is outside the visible window")
        physical = slots.clamp_min(0).long().remainder_(self.capacity)
        page = self.table[i[:, None], physical // PAGE].long()
        offset = physical % PAGE
        return tuple(x[page, offset].flatten(2).masked_fill(~valid[..., None], 0) for x in self.planes)

    def resolve(self, kept):
        if (self.written is None or len(kept) != LANES
                or any(type(n) is not int or not 0 <= n <= end - old
                       for n, end, old in zip(kept, self.written, self.lengths, strict=True))):
            raise ValueError("HY4 sliding commit must select a written prefix")
        self.lengths = tuple(a + b for a, b in zip(self.lengths, kept, strict=True))
        self.pending = self.written = None

    def release(self, lane):
        if self.pending is not None or type(lane) is not int or not 0 <= lane < LANES:
            raise ValueError("Release a sliding lane between waves")
        self.lengths = tuple(0 if i == lane else n for i, n in enumerate(self.lengths))

class SlidingTarget:
    """Use the same native attention step for ordinary decode and DFly2 verify."""

    def __init__(self, m, scope, rotary, device, ext, append):
        if (m.attention_type, m.config.sliding_window, m.kv_lora_rank, m.qk_rope_head_dim) != (
                "sliding_attention", WINDOW, LATENT, ROPE):
            raise ValueError("Expected the native HY4 sliding attention geometry")
        self.m, self.scope, self.rotary, self.ext = m, scope, rotary, ext
        self.cache = SlidingQ8(append, device, m.config.max_position_embeddings)
        self.weight = m.kv_b_proj.weight.view(m.num_heads, m.qk_nope_head_dim + m.v_head_dim, LATENT)

    def project(self, x, positions, *, query=True):
        m = self.m
        b, w = x.shape[:2]
        if positions.shape != (b, w) or (positions < 0).any() or (positions >= self.cache.context).any():
            raise ValueError("Native HY4 sliding position limit exceeded")
        k, r = m.kv_a_proj_with_mqa(x).split((LATENT, ROPE), -1)
        if query:
            q0, qr = m.q_b_proj(m.q_a_layernorm(m.q_a_proj(x))).view(
                b, w, m.num_heads, m.qk_nope_head_dim + ROPE).transpose(1, 2).split(
                    (m.qk_nope_head_dim, ROPE), -1)
        else:
            q0, qr = None, r.unsqueeze(1)
        qr, r = self.scope["apply_rotary_pos_emb"](qr, r.unsqueeze(1),
            *self.rotary(x, positions.unsqueeze(0).expand(3, -1, -1), layer_type="sliding_attention"))
        return q0, qr, m.kv_a_layernorm(k).contiguous(), r.squeeze(1).contiguous()

    def step(self, lanes, x, positions):
        if x.shape[:2] != (len(lanes), 1):
            raise ValueError("Use one cached target step per live request")
        m = self.m
        q0, qr, k, r = self.project(x, positions)
        self.cache.append(lanes, k, r)
        slots = self.cache.window(lanes, tentative=True)
        words, scales, roped = self.cache.read(lanes, slots, tentative=True)
        keys = torch.empty((len(lanes) * WINDOW, LATENT), dtype=torch.float16, device=x.device)
        self.ext.dequant_cache_cont(words.flatten(0, 1).contiguous(), scales.flatten(0, 1).contiguous(), keys, 0.0)
        local = torch.arange(WINDOW, device=x.device).expand_as(slots).masked_fill(slots < 0, -1)
        y = projected_attention(q0, qr, keys.view(len(lanes), WINDOW, LATENT).to(x.dtype), roped, self.weight,
                                local[:, None], torch.full_like(local[:, :1], WINDOW - 1), m.sinks).transpose(1, 2)
        y = y.to(x.dtype) * m.gate_proj(x).view(len(lanes), 1, m.num_heads, m.v_head_dim).sigmoid()
        return m.post_proj_norm(m.o_proj(y.flatten(2))), slots
