'Continuously recycle target-only serving lanes while keeping DFly2 batches separate.'

from functools import partial

from queue import Empty

from types import MethodType

from hy4_quality_batch import grouped_forward

from hy4_quality_batch import prefill_requests

from hy4_quality_batch import release

from hy4_quality_device_step import key_width

from hy4_quality_device_step import step

from hy4_shared_pool import LANES

from hy4_shared_pool import PAGE

from hy4_standard_expert_pack import PackedExperts

def fits(rows, capacity):
    # Idle target lanes use one scratch page each, recycled before the next page.
    return len(rows) <= LANES and sum(r.slots for r in rows) + LANES - len(rows) <= capacity

def generate(engine, batch):
    target, torch = engine.runner.target, engine.torch
    dispatch = getattr(engine, "expert_dispatch", None)
    native = partial(step, target, experts=dispatch)
    if engine.fused_mla:
        from hy4_fused_mla import attention
        native = partial(native, attend=attention)
    grouped = getattr(engine, "grouped_replay", None)
    grouped_native = partial(native, experts=grouped) if grouped else None
    grouped_limit = getattr(engine, "grouped_replay_limit", 0)
    buckets = getattr(engine, "exact_fallback_buckets", {})
    sections = getattr(engine, "exact_sections", None)
    readback = getattr(engine, "cpu_readback", None)
    experts = [b.mlp for b in target.blocks if isinstance(b.mlp, PackedExperts)]
    reference = [m.forward for m in experts]
    active, logits = {}, {}

    def admit(rows):
        prompts = {}
        for row in rows:
            lane = next(i for i in range(LANES) if i not in active)
            if target.pool.lengths[lane]:
                release(target, lane)
            active[lane] = row
            prompts[lane] = torch.tensor(row.ids, dtype=torch.long, device=target.entry)
        if prompts:
            with engine.use_recall({"method": "measured_causal_topk", "query_tile": 32,
                                   "key_tile": 8192, "split_ragged": True}):
                logits.update(prefill_requests(target, prompts))
        engine.active = len(active)
        engine.last_batch = max(engine.last_batch, len(active))
        return tuple(prompts)

    def waiting():
        accepted = []
        for _ in range(LANES - len(active)):
            try:
                row = engine.backlog.popleft() if engine.backlog else engine.queue.get_nowait()
            except Empty:
                break
            if row.dfly or not fits([*active.values(), *accepted, row], target.pool.capacity):
                engine.backlog.appendleft(row)
                break
            accepted.append(row)
        return accepted

    with torch.inference_mode():
        try:
            for m in experts:
                if dispatch is not None and m in dispatch:
                    m.forward = dispatch[m]
                elif not hasattr(m, "peer_experts"):
                    m.forward = MethodType(grouped_forward, m)
            admit(batch)
            while active:
                if engine.stopped.is_set():
                    raise InterruptedError("Model is draining")
                tokens = {}
                candidates = tuple(active)
                while candidates:
                    rows = torch.stack([logits[i] for i in candidates])
                    picked = (readback(rows) if readback and len(candidates) in readback.widths
                              else rows.argmax(-1).tolist())
                    for lane, token in zip(candidates, picked, strict=True):
                        row = active[lane]
                        engine.emit(row, (token,), final=False)
                        if row.reason is None:
                            tokens[lane] = token
                            continue
                        row.updates.put(("done", engine.emit(row, (), final=True)))
                        del active[lane], logits[lane]
                        release(target, lane)
                    candidates = admit(waiting())
                if not active:
                    break
                padding = {}
                faster = getattr(target, "latency_decode", None)
                if faster is None or not faster.selected(tuple(active)):
                    for i in range(LANES):
                        if i in active:
                            continue
                        if target.pool.lengths[i] >= PAGE:
                            release(target, i)
                        if not target.pool.lengths[i]:
                            padding[i] = torch.tensor([engine.eos], device=target.entry)
                if padding:
                    prefill_requests(target, padding)
                ids = torch.tensor([tokens.get(i, engine.eos) for i in range(LANES)],
                                   device=target.entry)[:, None]
                decode = native
                if len(active) == LANES:
                    largest = max(target.pool.lengths)
                    mode = buckets.get(key_width(target.pool.lengths, 2048)) if buckets and largest < 2048 else None
                    if sections is not None and mode == "section_replay" and sections.supports(tuple(active)):
                        decode = sections.step
                    elif grouped_native and (largest < grouped_limit or mode == "expert_replay"):
                        decode = grouped_native
                out = decode(ids, active_lanes=tuple(active))
                logits = {i: out[i] for i in active}
        except BaseException:
            for row in active.values():
                if row not in batch:
                    row.updates.put(("error", ""))
            raise
        finally:
            for m, original in zip(experts, reference, strict=True):
                m.forward = original
            if target.trial is None and target.pool.pending is None:
                engine.reset(target)
