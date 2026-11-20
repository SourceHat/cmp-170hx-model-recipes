"""Bounded request-level prefix attribution. No tokens or prompt text leave this module."""
from collections import Counter, OrderedDict
from contextvars import ContextVar


PREFIX_REQUEST = ContextVar("prefix_request", default=None)


class PrefixHistory:
    def __init__(self, page_size=256, max_histories=128, max_pages=131072):
        self.page_size = page_size
        self.max_histories = max_histories
        self.max_pages = max_pages
        self.observed = OrderedDict()
        self.completed = OrderedDict()
        self.observed_pages = Counter()
        self.completed_pages = Counter()
        self.sessions = OrderedDict()

    def _remember(self, histories, counts, serial, hashes):
        old = histories.pop(serial, ())
        counts.subtract(old)
        histories[serial] = tuple(hashes)
        counts.update(hashes)
        while len(histories) > self.max_histories or sum(map(len, histories.values())) > self.max_pages:
            _, removed = histories.popitem(last=False)
            counts.subtract(removed)
        # Remove zero counts: otherwise a bounded history leaves an unbounded index.
        for key in old:
            if counts[key] <= 0:
                counts.pop(key, None)
        if len(counts) > self.max_pages or any(value <= 0 for value in counts.values()):
            for key in list(counts):
                if counts[key] <= 0:
                    del counts[key]

    @staticmethod
    def _common(left, right):
        for i, (a, b) in enumerate(zip(left, right)):
            if a != b:
                return i
        return min(len(left), len(right))

    @staticmethod
    def _known_prefix(hashes, counts):
        for i, h in enumerate(hashes):
            if counts.get(h, 0) <= 0:
                return i
        return len(hashes)

    def allocation(self, serial, hashes, input_tokens, pagetable, recurrent_cache, metadata=None):
        metadata = metadata or {}
        seen = self._known_prefix(hashes, self.observed_pages)
        built = self._known_prefix(hashes, self.completed_pages)
        resident = 0
        broken_at = None
        checkpoints = []
        lost = []
        invalid_positions = 0
        prev = None
        for i, h in enumerate(hashes):
            page = pagetable.get_live_page(h)
            if page is not None and resident == i:
                resident += 1
                if page.prev_hash != prev and broken_at is None:
                    broken_at = i * self.page_size
            if recurrent_cache is not None:
                stash = recurrent_cache.get(h)
                if stash is not None:
                    if stash.get("position") == (i + 1) * self.page_size:
                        checkpoints.append(i + 1)
                    else:
                        invalid_positions += 1
                reason = getattr(recurrent_cache, "loss_reasons", {}).get(h)
                if reason is not None:
                    lost.append((i + 1, reason))
            prev = h
        usable = max((n for n in checkpoints if n <= resident), default=0)
        if recurrent_cache is None:
            usable = resident
        ps = self.page_size
        row = {
            "version": 1, "input_tokens": input_tokens,
            "eligible_prefix_tokens": len(hashes) * ps,
            "previous_observed_prefix_tokens": seen * ps,
            "previous_completed_prefix_tokens": built * ps,
            "history_known": bool(seen),
            "resident_prefix_tokens": resident * ps,
            "latest_matching_checkpoint_tokens": max(checkpoints, default=0) * ps,
            "valid_checkpoint_tokens": usable * ps,
            "previous_completed_kv_missing_tokens": max(0, built - resident) * ps,
            "resident_kv_without_state_tokens": max(0, resident - usable) * ps,
            "broken_ancestry_at_tokens": broken_at,
            "invalid_checkpoint_positions": invalid_positions,
            "checkpoint_loss_tokens": {
                reason: max((n for n, r in lost if r == reason and usable < n <= resident), default=0) * ps
                for reason in ("budget", "stranded")
            },
            "active_jobs_at_allocation": len(pagetable.generator.active_jobs),
            "active_decode_at_allocation": sum(j.is_prefill_done() for j in pagetable.generator.active_jobs),
            "session_history_known": False,
            "session_shared_prefix_tokens": None,
            "session_first_changed_message": None,
            "session_first_changed_normalized_message": None,
        }
        session = metadata.get("session_key")
        prior = self.sessions.get(session) if session else None
        if prior is not None:
            row["session_history_known"] = True
            shared = self._common(prior["hashes"], hashes)
            row["session_shared_prefix_tokens"] = shared * ps
            row["session_prior_prefix_tokens"] = len(prior["hashes"]) * ps
            row["session_prefix_changed"] = shared < min(len(prior["hashes"]), len(hashes))
            for field, target in (("message_hashes", "session_first_changed_message"),
                                  ("normalized_message_hashes", "session_first_changed_normalized_message")):
                a, b = prior["metadata"].get(field), metadata.get(field)
                if a is not None and b is not None:
                    common = self._common(a, b)
                    if common < min(len(a), len(b)):
                        row[target] = common
            row["session_template_options_changed"] = (
                prior["metadata"].get("template_options_hash") != metadata.get("template_options_hash"))
        if session:
            self.sessions.pop(session, None)
            self.sessions[session] = {"hashes": tuple(hashes), "metadata": dict(metadata), "serial": serial}
            while len(self.sessions) > self.max_histories or sum(len(s["hashes"]) for s in self.sessions.values()) > self.max_pages:
                self.sessions.popitem(last=False)
        self._remember(self.observed, self.observed_pages, serial, hashes)
        return row

    def completed_sequence(self, serial, pages, metadata=None):
        hashes = []
        for p in pages:
            if p.kv_position != self.page_size:
                break
            hashes.append(p.phash)
        self._remember(self.completed, self.completed_pages, serial, hashes)
        metadata = metadata or {}
        session = metadata.get("session_key")
        prior = self.sessions.get(session)
        if prior is not None and prior["serial"] == serial:
            prior["hashes"] = tuple(hashes)

    @staticmethod
    def checkpoint_target(row, min_gap_tokens=2048):
        """Save one demonstrated fork boundary, not every page on the branch."""
        shared = min(row["resident_prefix_tokens"], row["previous_completed_prefix_tokens"])
        return shared if shared - row["valid_checkpoint_tokens"] >= min_gap_tokens else None

    @staticmethod
    def restored(row, position, stashed_state):
        row["restored_position_tokens"] = position
        row["restored_state_position_tokens"] = stashed_state.get("position") if stashed_state else None
        row["restored_mtp_carry"] = stashed_state.get("mtp_hidden") is not None if stashed_state else False
        reasons = []
        if row.get("session_prefix_changed"):
            reasons.append("incoming_prefix_change")
        if row["previous_completed_kv_missing_tokens"]:
            reasons.append("kv_page_loss")
        if row["broken_ancestry_at_tokens"] is not None:
            reasons.append("broken_ancestry")
        if row["resident_kv_without_state_tokens"]:
            reasons.append("recurrent_checkpoint_gap")
        for reason, tokens in row["checkpoint_loss_tokens"].items():
            if tokens:
                reasons.append("checkpoint_" + reason)
        if not row["history_known"] and not row["session_history_known"]:
            reasons.append("unknown_history")
        row["replay_reasons"] = reasons
