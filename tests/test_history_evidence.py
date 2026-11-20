import copy
import json
from pathlib import Path
import sys
import unittest

REPO = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO / "scripts"))
from history_docs import load_history, point_row
from history_evidence import numerical_metrics, quality_metrics, request_metrics
from validate_history import validate_documents


class EvidenceSelectionTests(unittest.TestCase):
    def test_request_selection_retains_timers_without_payloads_or_identifiers(self):
        raw = {"content": "private response", "reasoning_content": "private reasoning",
               "messages": [{"content": "private prompt"}], "id": "private-id",
               "usage": {"prompt_tokens": 1234, "completion_tokens": 64,
                         "prompt_tokens_details": {"cached_tokens": 1200}, "secret": "private-key"},
               "timings": {"predicted_ms": 2000, "predicted_n": 64, "secret": "private"},
               "ttft_seconds": 0.1, "elapsed_seconds": 2.2, "finish_reason": "length"}
        result = request_metrics(raw)
        self.assertEqual(result["usage"]["prompt_tokens_details"]["cached_tokens"], 1200)
        self.assertEqual(result["timings"], {"predicted_ms": 2000, "predicted_n": 64})
        self.assertNotIn("private", json.dumps(result))

    def test_quality_denominators_come_from_actual_category_counts(self):
        source = {"passed": 2, "total": 3, "categories": {"coding": 1, "reasoning": 1},
                  "tasks": [{"category": "coding", "grade": {"passed": True}},
                            {"category": "coding", "grade": {"passed": False}},
                            {"category": "reasoning", "grade": {"passed": True}}]}
        result = quality_metrics(source)
        self.assertEqual(result["categories"]["coding"]["total"], 2)
        self.assertEqual(result["categories"]["reasoning"]["total"], 1)

    def test_original_grades_and_incomplete_answers_survive_regrading(self):
        result = quality_metrics({"passed": 1, "total": 1, "tasks": [
            {"category": "agent", "grade": {"passed": True}, "original_grade": {"passed": False},
             "truncated": True, "original_result": {"content": "private", "finish_reason": "length",
                                                        "usage": {"completion_tokens": 8192}}}]})
        sample = result["samples"][0]
        self.assertTrue(sample["passed"])
        self.assertFalse(sample["original_grade_passed"])
        self.assertTrue(sample["truncated"])
        self.assertEqual(sample["request"]["finish_reason"], "length")
        self.assertNotIn("private", json.dumps(result))

    def test_error_text_and_physical_card_identities_are_omitted(self):
        result = numerical_metrics({"passed": False, "context_tokens": 4096,
                                    "error": "private prompt and credential",
                                    "per_card_peak_used_MiB": {"physical-card-A": 50000, "physical-card-B": 48000}})
        self.assertEqual(result["per_card_peak_used_MiB_unordered"], [48000, 50000])
        self.assertTrue(result["error_present"])
        self.assertFalse(result["flags"]["passed"])
        self.assertNotIn("private", json.dumps(result))
        self.assertNotIn("physical-card", json.dumps(result))

    def test_nonfinite_values_and_boolean_token_counts_are_rejected_by_selection(self):
        self.assertEqual(numerical_metrics({"input_tokens": True, "generated_tokens": float("nan"),
                                           "elapsed_seconds": float("inf")}), {})


class EvidenceAccountingTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.original = load_history(REPO)
        sources = json.loads((REPO / "archive/history/sources.json").read_text())["sources"]
        cls.sources = {(row["file"], row["sha256"]) for row in sources}

    def test_quality_score_cannot_change_without_changing_the_underlying_grades(self):
        history = copy.deepcopy(self.original)
        row = next(row for row in history["observations"].values()
                   if row["kind"] == "quality_evaluation" and row["metrics"]["passed"] < row["metrics"]["total"])
        row["metrics"]["passed"] += 1
        with self.assertRaisesRegex(ValueError, "quality grades differ"):
            validate_documents(history, self.sources)

    def test_quality_latency_cannot_use_a_different_request_denominator(self):
        history = copy.deepcopy(self.original)
        row = next(row for row in history["observations"].values() if "task_total_latency_seconds" in row["metrics"])
        row["metrics"]["task_total_latency_seconds"]["count"] += 1
        with self.assertRaisesRegex(ValueError, "latency denominator"):
            validate_documents(history, self.sources)

    def test_results_without_exact_configurations_cannot_claim_a_binding(self):
        history = copy.deepcopy(self.original)
        row = next(row for row in history["observations"].values() if not row["configuration_ids"])
        row["configuration_binding"] = "recorded_config_or_job"
        with self.assertRaisesRegex(ValueError, "unbound result"):
            validate_documents(history, self.sources)

    def test_wave_table_identifies_profile_request_count_and_output_budget(self):
        point = next(row for row in self.original["points"].values()
                     if row["request_count"] > 1 and row.get("requested_output_tokens_per_request"))
        row = point_row(point, self.original)
        self.assertIn("profiles/", row[0])
        self.assertEqual(row[2], str(point["request_count"]))
        self.assertIn("budget", row[4])

    def test_client_estimate_cannot_fill_qualified_decode_fields(self):
        history = copy.deepcopy(self.original)
        point = next(row for row in history["points"].values() if row["measurement_kind"] == "client_estimated_decode_wave"
                     and row.get("reported_after_first_token_tok_s_estimate") is not None)
        point["decode_tok_s_aggregate"] = point["reported_after_first_token_tok_s_estimate"]
        with self.assertRaisesRegex(ValueError, "legacy estimate"):
            validate_documents(history, self.sources)

    def test_multi_instance_request_counts_must_reconstruct_the_whole_wave(self):
        history = copy.deepcopy(self.original)
        point = next(row for row in history["points"].values() if row.get("model_instance_count"))
        point["requests_per_instance"][0] += 1
        with self.assertRaisesRegex(ValueError, "multi-instance wave accounting"):
            validate_documents(history, self.sources)


if __name__ == "__main__":
    unittest.main()
