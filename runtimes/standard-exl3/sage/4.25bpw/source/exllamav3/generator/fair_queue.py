"""Keep request rotation from evicting the histories it is meant to share."""


class FairQueue:
    def __init__(self, page_size=256, prefill_quantum=2048, generation_quantum=512):
        self.page_size = page_size
        self.prefill_quantum = prefill_quantum
        self.generation_quantum = generation_quantum
        self.prefill_yields = 0
        self.generation_yields = 0
        self.rotation_blocked_kv = 0
        self.rotation_blocked_recurrent = 0

    def rotation_fits(self, job, pending):
        generator = job.generator
        jobs = list({id(item): item for item in
                     [*generator.active_jobs, *pending, job]}.values())
        capacity = generator.max_total_tokens
        pages = 0
        for item in jobs:
            limit = item.max_new_tokens
            if limit is None:
                self.rotation_blocked_kv += 1
                return False
            remaining = max(0, limit - item.new_tokens)
            for sequence in item.sequences:
                tokens = len(sequence.sequence_ids) + remaining + generator.num_draft_tokens + 1
                pages += (tokens + self.page_size - 1) // self.page_size
            if pages * self.page_size > capacity:
                self.rotation_blocked_kv += 1
                return False

        recurrent = generator.recurrent_cache
        if recurrent is not None:
            sizes = [item.recurrent_state.checkpoint_size for item in generator.active_jobs
                     if item.recurrent_state is not None]
            hidden = 0
            if generator.mtp_draft:
                hidden = generator.model.config.hidden_size * 2
            # Count complete future histories, rather than just their next 2k turn.
            # Checkpoint sizes are host metadata; this must not copy or synchronize CUDA tensors.
            if not sizes or (max(sizes) + hidden) * len(jobs) > recurrent.max_size:
                self.rotation_blocked_recurrent += 1
                return False
        return True

    def prefill_due(self, job, pending):
        if (not pending or len(job.sequences) != 1 or job.embeddings or job.prefix_token is not None
                or getattr(job, 'banned_strings', None)):
            return False
        sequence = job.sequences[0]
        return (not job.is_prefill_done()
                and sequence.kv_position % self.page_size == 0
                and sequence.kv_position - job.prefill_turn_start >= self.prefill_quantum
                and self.rotation_fits(job, pending))

    def generation_due(self, job, pending):
        return (bool(pending) and len(job.sequences) == 1
                and not getattr(job, 'banned_strings', None)
                and job.new_tokens >= self.generation_quantum
                and job.sequences[0].kv_position % self.page_size == 0
                and self.rotation_fits(job, pending))

    def stats(self):
        return {'prefill_quantum_tokens': self.prefill_quantum,
                'generation_quantum_tokens': self.generation_quantum,
                'prefill_yields': self.prefill_yields,
                'generation_yields': self.generation_yields,
                'rotation_blocked_kv': self.rotation_blocked_kv,
                'rotation_blocked_recurrent': self.rotation_blocked_recurrent}
