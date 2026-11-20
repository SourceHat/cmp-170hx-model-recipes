'Run native indexed HY4 attention on a shared, rollback-safe Q8 pool.'

import torch

from hy4_cached_index import IndexPages

from hy4_compact_index_probe import DIM

from hy4_compact_index_probe import PAGE

from hy4_compact_index_probe import RATIO

from hy4_compact_index_probe import fp8_rows

from hy4_compact_index_probe import rank

from hy4_shared_pool import LANES

from hy4_shared_pool import SharedPool

from hy4_shared_pool import SharedQ8Latents

from mla_eager_reference import projected_attention

SCORE_TILE = 1024

class SharedIndex(IndexPages):
    def __init__(self, pool, indexer, inv, device):
        self.pool = pool
        self.indexer, self.inv = indexer, inv
        self.lanes, self.capacity, self.stride = LANES, pool.context, PAGE // RATIO
        self.rows = torch.arange(LANES, device=device)
        self.bits = torch.zeros((pool.capacity, self.stride, DIM), dtype=torch.uint8, device=device)
        self.scales = torch.ones((pool.capacity, self.stride), dtype=torch.float32, device=device)
        self.lengths = torch.zeros((LANES,), dtype=torch.long, device=device)
        self.partial = torch.zeros((LANES, RATIO, DIM), dtype=torch.bfloat16, device=device)
        self.first = torch.zeros_like(self.lengths)
        self.group_slots = torch.arange(pool.context // RATIO, device=device)
        self.table = pool.layout(device).table
        self.trial = None

    def bind(self, layout):
        self.table = layout.table

    def recall(self, x, q_resid, positions):
        index = self.indexer
        latest = self.lengths - 1
        if (latest < 0).any():
            raise ValueError("An indexed target query needs its own written key")
        budget = index.group_topk * RATIO
        slots = torch.arange(budget, device=x.device).expand(LANES, -1)
        dense = slots.masked_fill(slots > latest[:, None], -1)
        use_sparse = self.lengths > budget
        if not use_sparse.any():
            return dense
        current = latest // RATIO
        count = index.group_topk - 1
        query = index.query_projection(q_resid).reshape(LANES, index.num_heads, DIM)
        q, qs = fp8_rows(query, positions[:, None], self.inv)
        head = index.head_weight_projection(x).float() * ((index.num_heads * DIM) ** -0.5)
        best = head.new_full((LANES, count), float("-inf"))
        missing = self.group_slots.numel()
        chosen = torch.full((LANES, count), missing, device=x.device, dtype=torch.long)
        for begin in range(0, int(current.max()), SCORE_TILE):
            ids = begin + torch.arange(SCORE_TILE, device=x.device)
            valid = ids < current[:, None]
            safe = ids.clamp(max=missing - 1)
            page = self.table[:, safe // self.stride].long()
            if (valid & (page < 0)).any():
                raise ValueError("An active sparse group must own a physical page")
            offset = safe % self.stride
            keys = self.bits[page.clamp_min(0), offset]
            scales = self.scales[page.clamp_min(0), offset]
            values = rank(q, qs, head, keys, scales, valid)
            candidates = ids.expand(LANES, -1).masked_fill(~valid, missing)
            joined, which = torch.cat((best, values), dim=1), torch.cat((chosen, candidates), dim=1)
            order = which.argsort(dim=1, stable=True)
            ranked = joined.gather(1, order).argsort(dim=1, descending=True, stable=True)[:, :count]
            top = order.gather(1, ranked)
            best, chosen = joined.gather(1, top), which.gather(1, top)
        groups = torch.cat((chosen, current[:, None]), dim=1)
        tokens = (groups[..., None] * RATIO + torch.arange(RATIO, device=x.device)).flatten(1)
        tokens = tokens.masked_fill(tokens > latest[:, None], -1)
        tokens = torch.where(use_sparse[:, None], tokens, dense)
        # Fix the gathered key order independently of group score and lane timing.
        ordered = tokens.masked_fill(tokens < 0, self.capacity).sort(dim=1).values
        return ordered.masked_fill(ordered == self.capacity, -1)

class IndexedTarget:
    """Reference cached step used identically for ordinary decode and DFly2 verify."""

    def __init__(self, m, scope, rotary, pool_tokens, device, ext, append, *, shared_pool=None):
        if m.compressed_indexer is None or m.attention_type != "indexed_attention":
            raise ValueError("This target owns a native indexed attention block")
        self.m, self.scope, self.rotary = m, scope, rotary
        self.device, self.ext = device, ext
        if shared_pool is not None and shared_pool.capacity * PAGE != pool_tokens:
            raise ValueError("Every indexed block must use the same shared Q8 pool geometry")
        self.owns_pool = shared_pool is None
        self.pool = SharedPool(pool_tokens) if shared_pool is None else shared_pool
        self.kv = SharedQ8Latents(self.pool, append, device)
        self.index = SharedIndex(self.pool, m.compressed_indexer, rotary.indexed_attention_inv_freq, device)
        self.lanes = torch.arange(LANES, device=device)
        self.working = None

    def project(self, x, positions):
        m = self.m
        b, w = x.shape[:2]
        nope, rope = m.qk_nope_head_dim, m.qk_rope_head_dim
        q_resid = m.q_a_layernorm(m.q_a_proj(x))
        q0, qr = m.q_b_proj(q_resid).view(b, w, m.num_heads, nope + rope).transpose(1, 2).split((nope, rope), -1)
        k, kr = m.kv_a_proj_with_mqa(x).split((m.kv_lora_rank, rope), -1)
        qr, kr = self.scope["apply_rotary_pos_emb"](qr, kr.unsqueeze(1),
            *self.rotary(x, positions.unsqueeze(0), layer_type="indexed_attention"))
        return q_resid, q0, qr, m.kv_a_layernorm(k).contiguous(), kr.squeeze(1).contiguous()

    def prime(self, x, offsets):
        if not self.owns_pool or x.shape[0] != LANES or any(self.pool.lengths) or x.shape[1] <= 0:
            raise ValueError("Prime four empty target lanes before decoding")
        h = x.shape[1]
        positions = offsets[:, None] + torch.arange(h, device=self.device)
        if positions.min() < 0 or positions.max() >= self.pool.context:
            raise ValueError("Native HY4 phase limit exceeded")
        m = self.m
        # The target query projections are unused during cache seeding.
        k, r = m.kv_a_proj_with_mqa(x).split((m.kv_lora_rank, m.qk_rope_head_dim), -1)
        _, kr = self.scope["apply_rotary_pos_emb"](r.unsqueeze(1), r.unsqueeze(1),
            *self.rotary(x, positions.unsqueeze(0), layer_type="indexed_attention"))
        k, r = m.kv_a_layernorm(k).contiguous(), kr.squeeze(1).contiguous()
        raw = m.compressed_indexer.token_key_norm(m.compressed_indexer.token_key_projection(x))
        self.pool.reserve([h] * LANES)
        view = self.pool.layout(self.device, tentative=True)
        self.index.bind(view)
        self.index.seed(raw, positions)
        self.kv.append(view, self.lanes, torch.zeros(LANES, device=self.device, dtype=torch.int32), k, r)
        self.pool.commit([h] * LANES)

    def begin(self, width):
        if not self.owns_pool or not 1 <= width <= 6 or self.working is not None:
            raise ValueError("One native verify window can contain one to six rows")
        if tuple(self.index.lengths.tolist()) != self.pool.lengths:
            raise ValueError("Shared latent and sparse index committed lengths differ")
        self.pool.reserve([width] * LANES)
        self.attach_trial(self.pool.layout(self.device, tentative=True))

    def attach_trial(self, layout):
        if (self.working is not None or self.pool.pending is None or layout.generation != self.pool.generation
                or layout.table.device != self.lanes.device or tuple(self.index.lengths.tolist()) != self.pool.lengths):
            raise ValueError("Indexed layer trial must use the current shared target reservation")
        self.working = layout
        self.index.bind(self.working)
        self.index.begin()

    def step(self, x, offsets):
        if self.working is None or x.shape[:2] != (LANES, 1):
            raise ValueError("Use one cached target step over four active requests")
        m = self.m
        slot = self.index.lengths.clone()
        current = offsets + slot
        if (current < 0).any() or (current >= self.pool.context).any():
            raise ValueError("Native HY4 phase limit exceeded")
        q_resid, q0, qr, k, r = self.project(x, current[:, None])
        self.kv.append(self.working, self.lanes, slot.int(), k, r)
        raw = m.compressed_indexer.token_key_norm(m.compressed_indexer.token_key_projection(x))
        self.index.append(raw, current[:, None])
        real = self.index.recall(x[:, 0], q_resid[:, 0], current)
        words, scales, roped = self.kv.read(self.working, self.lanes, real)
        size = words.shape[1]
        keys = torch.empty((LANES * size, m.kv_lora_rank), dtype=torch.float16, device=x.device)
        self.ext.dequant_cache_cont(words.flatten(0, 1).contiguous(), scales.flatten(0, 1).contiguous(), keys, 0.0)
        local = torch.arange(size, device=x.device).expand_as(real).masked_fill(real < 0, -1)
        w = m.kv_b_proj.weight.view(m.num_heads, m.qk_nope_head_dim + m.v_head_dim, m.kv_lora_rank)
        y = projected_attention(q0, qr, keys.view(LANES, size, -1).to(x.dtype), roped, w,
            local[:, None], torch.full((LANES, 1), size - 1, device=x.device), m.sinks).transpose(1, 2)
        y = y.to(x.dtype) * m.gate_proj(x).view(LANES, 1, m.num_heads, m.v_head_dim).sigmoid()
        return m.post_proj_norm(m.o_proj(y.flatten(2))), real

    def resolve(self, accepted):
        if not self.owns_pool:
            raise ValueError("The composed target must resolve the complete Q8 pool together")
        self.resolve_index(accepted)
        self.pool.commit([int(x) + 1 for x in accepted.tolist()])
        if tuple(self.index.lengths.tolist()) != self.pool.lengths:
            raise ValueError("Committed sparse index and latent lengths differ")

    def resolve_index(self, accepted):
        if self.working is None:
            raise ValueError("No indexed layer trial is open")
        self.index.resolve(accepted)
        self.working = None
