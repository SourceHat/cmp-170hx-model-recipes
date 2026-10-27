import copy
import json
from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from native_prefill import HISTOGRAMS, recover_prefill


class NativePrefillRecoveryTests(unittest.TestCase):
    def setUp(self):
        self.records = json.loads((ROOT / "data/native-prefill-recovery.json").read_text())["records"]
        self.record = copy.deepcopy(self.records[0])

    def test_real_snapshots_reproduce_all_four_observations(self):
        for record in self.records:
            with self.subTest(record=record["id"]):
                self.assertEqual(recover_prefill(record), record["measurement"])
        self.assertAlmostEqual(self.records[0]["measurement"]["prefill_tok_s"], 2030.6989281672732)
        self.assertEqual(self.records[1]["measurement"]["processed_prompt_tokens"], 15107)
        self.assertEqual(self.records[1]["measurement"]["cached_prompt_tokens"], 17664)

    def test_more_than_one_completed_request_cannot_supply_a_c1_timer(self):
        self.record["after"]["prefill_seconds"]["count"] += 1
        with self.assertRaisesRegex(ValueError, "exactly one"):
            recover_prefill(self.record)

    def test_each_token_histogram_requires_the_same_single_request_delta(self):
        for metric in HISTOGRAMS[1:]:
            altered = copy.deepcopy(self.record)
            altered["after"][metric]["count"] += 1
            with self.subTest(metric=metric), self.assertRaisesRegex(ValueError, "exactly one"):
                recover_prefill(altered)

    def test_changed_worker_epoch_or_model_labels_are_rejected(self):
        for field, value in (("epoch_sha256", "0" * 64), ("labels", {"model_name": "different"})):
            altered = copy.deepcopy(self.record)
            altered["after"][field] = value
            with self.subTest(field=field), self.assertRaises(ValueError):
                recover_prefill(altered)

    def test_request_input_and_output_must_match_the_native_counters(self):
        for field in ("input_tokens", "accepted_output_tokens"):
            altered = copy.deepcopy(self.record)
            altered["request"][field] += 1
            with self.subTest(field=field), self.assertRaisesRegex(ValueError, "recorded request"):
                recover_prefill(altered)

    def test_cached_tokens_are_not_counted_as_new_prefill(self):
        altered = copy.deepcopy(self.records[1])
        altered["after"]["prefix_hits"] += 1
        with self.assertRaisesRegex(ValueError, "prefix counters"):
            recover_prefill(altered)

    def test_missing_nonfinite_negative_or_nonintegral_metrics_are_rejected(self):
        for value in (None, float("nan"), float("inf"), -1):
            altered = copy.deepcopy(self.record)
            altered["after"]["prefill_seconds"]["sum"] = value
            with self.subTest(value=value), self.assertRaises(ValueError):
                recover_prefill(altered)
        altered = copy.deepcopy(self.record)
        del altered["after"]["prefill_seconds"]["sum"]
        with self.assertRaises(ValueError):
            recover_prefill(altered)
        altered = copy.deepcopy(self.record)
        altered["after"]["computed_prompt_tokens"]["sum"] += .5
        with self.assertRaisesRegex(ValueError, "Nonintegral token"):
            recover_prefill(altered)

    def test_zero_native_duration_is_not_replaced_with_client_ttft(self):
        self.record["after"]["prefill_seconds"]["sum"] = self.record["before"]["prefill_seconds"]["sum"]
        with self.assertRaisesRegex(ValueError, "not positive"):
            recover_prefill(self.record)

    def test_metric_reset_is_rejected(self):
        self.record["after"]["prompt_tokens"]["sum"] = 0
        with self.assertRaisesRegex(ValueError, "metric reset"):
            recover_prefill(self.record)


if __name__ == "__main__":
    unittest.main()
