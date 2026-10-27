import copy
from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from selected_prefill import common_decode


def trace(label):
    return {"label": label, "clock": "CLOCK_MONOTONIC", "status": "complete",
            "truncated": False, "requeued": False, "generated_tokens": 256,
            "first_generation_ns": 1_000_000_000, "finished_ns": 4_000_000_000,
            "events": [[1_000_000_000, 1, False], [2_000_000_000, 100, False],
                       [3_000_000_000, 200, False], [4_000_000_000, 256, False]],
            "prefill_spans": []}


class SelectedPrefillEvidenceTests(unittest.TestCase):
    def test_common_interval_uses_accepted_counts_and_explicit_boundaries(self):
        measured = common_decode([trace("a"), trace("b")])
        self.assertEqual(measured["accepted_tokens"], 398)
        self.assertEqual(measured["seconds"], 3)
        self.assertEqual(measured["tok_s"], 398 / 3)
        self.assertEqual(measured["per_request_tokens"], [199, 199])

    def test_prefill_in_a_different_request_invalidates_the_shared_interval(self):
        rows = [trace("a"), trace("b")]
        rows[1]["events"][1][2] = True
        with self.assertRaisesRegex(ValueError, "Prefill overlapped"):
            common_decode(rows)

    def test_pending_native_prefill_span_cannot_be_hidden_between_samples(self):
        row = trace("a")
        row["prefill_spans"] = [[1_500_000_000, 1_600_000_000]]
        with self.assertRaisesRegex(ValueError, "native prefill span"):
            common_decode([row])

    def test_incomplete_and_requeued_requests_do_not_supply_aggregate_rates(self):
        for key, value in (("status", "cancelled"), ("truncated", True), ("requeued", True)):
            row = trace("a")
            row[key] = value
            with self.subTest(key=key), self.assertRaises(ValueError):
                common_decode([row])

    def test_reset_nonmonotonic_or_mismatched_counts_are_rejected(self):
        for events in ([[1, 2, False], [1, 3, False]], [[1, 3, False], [2, 2, False]],
                       [[1, 1, False], [2, 255, False]]):
            row = trace("a")
            row["events"] = events
            with self.subTest(events=events), self.assertRaises(ValueError):
                common_decode([row])

    def test_missing_duplicate_or_too_short_intervals_are_rejected(self):
        for rows in ([], [trace("a"), trace("a")]):
            with self.assertRaises(ValueError):
                common_decode(rows)
        a, b = trace("a"), trace("b")
        b["first_generation_ns"] = 3_900_000_000
        with self.assertRaisesRegex(ValueError, "common generation interval"):
            common_decode([a, b])


if __name__ == "__main__":
    unittest.main()
