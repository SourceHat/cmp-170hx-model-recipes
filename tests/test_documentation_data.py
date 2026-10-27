import copy
import json
from pathlib import Path
import re
import sys
import unittest

REPO = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO / "scripts"))
from archive_indexes import archive_documents, family_slug, prefill_dataset, prefill_rows, qwen_replica_rows
from build_docs import headline_points, performance_row
from build_docs import number, quant_label
from history_docs import load_history, STATUS


class HeadlineMeasurementTests(unittest.TestCase):
    def setUp(self):
        folder = REPO / "recipes/qwen27-orca-mtp3-native"
        self.recipe = json.loads((folder / "recipe.json").read_text())
        self.points = json.loads((folder / "benchmarks.json").read_text())["points"]

    def test_unmatched_pool_or_cohort_cannot_supply_headline_prefill(self):
        single, wave = headline_points(self.recipe, self.points)
        for field, value in (("cohort", "different campaign"),
                             ("test_configuration", {"cache_tokens": 12345}),
                             ("output_tokens_per_request", 512)):
            with self.subTest(field=field):
                mismatched = copy.deepcopy(single)
                mismatched[field] = value
                with self.assertRaisesRegex(ValueError, "matching cold one-request"):
                    headline_points(self.recipe, [mismatched, wave])

    def test_missing_backend_prefill_cannot_be_inferred_from_ttft(self):
        single, wave = copy.deepcopy(headline_points(self.recipe, self.points))
        single["backend_prefill_tok_s_per_request_median"] = None
        single["ttft_median_seconds"] = 10.0
        row = performance_row(self.recipe, [single, wave])
        self.assertEqual(row[2], "-")
        self.assertEqual(row[3], "10.00")

    def test_warm_or_other_input_lengths_cannot_enter_cold_32k_comparison(self):
        single, wave = copy.deepcopy(headline_points(self.recipe, self.points))
        for field, value in (("cache_state", "cached_prefix"), ("input_target_tokens", 2048)):
            with self.subTest(field=field):
                altered = copy.deepcopy(single)
                altered[field] = value
                with self.assertRaisesRegex(ValueError, "matching cold one-request"):
                    headline_points(self.recipe, [altered, wave])

    def test_missing_native_awq_prefill_is_not_replaced_with_a_reconstruction(self):
        folder = REPO / "recipes/apex-abliterated-awq-dflash2-pp3-balanced"
        recipe = json.loads((folder / "recipe.json").read_text())
        points = json.loads((folder / "benchmarks.json").read_text())["points"]
        historical = [point for point in points if point["cohort"] != "selected-serving-native-prefill"]
        self.assertEqual(performance_row(recipe, historical)[2], "-")
        single, wave = headline_points(recipe, points)
        self.assertEqual(single["cohort"], wave["cohort"])
        self.assertEqual(single["cohort"], "selected-serving-native-prefill")
        self.assertEqual(performance_row(recipe, points)[2], number(single["backend_prefill_tok_s_per_request_median"]))

    def test_qwen_summary_uses_observed_replica_medians_with_historical_wave_size(self):
        import statistics
        folder = REPO / "recipes/qwen3.8-27b-exl3"
        recipe = json.loads((folder / "recipe.json").read_text())
        result = json.loads((folder / "historical-replica-result.json").read_text())
        cold = result["measurements"]["one_stream_per_card"]["cold"]
        row = performance_row(recipe, [])
        rates = [value for replica in cold["request_timing_by_replica"]
                 for value in replica["backend_prefill_tok_s_per_request"]]
        self.assertEqual(row[2], number(statistics.median(rates)))
        self.assertEqual(row[4], number(statistics.median(card["generation_tps"] for card in cold["per_card"])))
        self.assertEqual(row[5], 16)
        self.assertEqual(recipe["serving"]["max_requests"], 8)

    def test_apex_label_uses_main_checkpoint_bpw_instead_of_the_expert_format(self):
        folder = REPO / "recipes/apex-abliterated-exl3-mtp1-tp3"
        recipe = json.loads((folder / "recipe.json").read_text())
        self.assertEqual(quant_label(recipe), "EXL3 4.37 bpw")


class PrefillViewTests(unittest.TestCase):
    def observation(self, identity, **metrics):
        return {"result_id": identity, "metrics": metrics, "configuration_ids": [],
                "profile_ids": [], "associated_profile_ids": ["named-source-profile"],
                "configuration_binding": "unresolved", "sources": [{"file": "report.json"}]}

    def test_entries_keep_array_boundaries_cache_counts_failures_and_binding(self):
        cold = {"processed_prompt_tokens": 1000, "cached_prompt_tokens": 0,
                "backend_prefill_seconds": 2.0, "prefill_tok_s": 500.0}
        warm = {"processed_prompt_tokens": 100, "cached_prompt_tokens": 900,
                "backend_prefill_seconds": 0.5, "prefill_tok_s": 200.0}
        history = {"observations": {
            "a": self.observation("a", cold_prefill=[cold, cold], flags={"passed": False}),
            "b": self.observation("b", prefill=[warm]),
        }}
        result = prefill_rows(history)
        self.assertEqual(len(result), 3)
        self.assertEqual([row["entry_index"] for row in result], [0, 1, 0])
        self.assertEqual([row["entries_in_source_array"] for row in result], [2, 2, 1])
        self.assertEqual([row["cached_prompt_tokens"] for row in result], [0, 0, 900])
        self.assertFalse(result[0]["reported_passed"])
        self.assertEqual(result[2]["configuration_ids"], [])
        self.assertEqual(result[2]["prefill_tok_s"], 200.0)
        self.assertEqual(prefill_dataset(history)["source_array_count"], 2)

    def test_client_time_without_backend_timer_does_not_create_prefill(self):
        history = {"observations": {"a": self.observation("a", values={"ttft_seconds": 5.0,
                                                                                "input_tokens": 1000})}}
        self.assertEqual(prefill_rows(history), [])


class ArchiveNavigationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.history = load_history(REPO)
        cls.documents = archive_documents(cls.history, STATUS)

    def linked_ids(self, text):
        return set(re.findall(r"\]\((?:\.\./)?history/profiles/([^/)]+)\.md\)", text))

    def test_profiles_and_experiments_partition_the_complete_catalog(self):
        archived = set(self.history["coverage"]["archived_profile_ids"])
        all_ids = {row["id"] for row in self.history["records"]}
        self.assertEqual(self.linked_ids(self.documents["PROFILES.md"]), archived)
        self.assertEqual(self.linked_ids(self.documents["EXPERIMENTS.md"]), all_ids - archived)

    def test_each_family_indexes_all_and_only_its_records(self):
        families = {row["family"] for row in self.history["records"]}
        self.assertEqual(len({family_slug(family) for family in families}), len(families))
        for family in families:
            expected = {row["id"] for row in self.history["records"] if row["family"] == family}
            page = self.documents[f"models/{family_slug(family)}.md"]
            self.assertEqual(self.linked_ids(page), expected)

    def test_prefill_export_preserves_every_original_numerical_entry(self):
        expected = {(row["result_id"], field, index): entry
                    for row in self.history["observations"].values()
                    for field in ("cold_prefill", "prefill")
                    for index, entry in enumerate(row["metrics"].get(field, []))}
        actual = prefill_rows(self.history)
        self.assertEqual(len(actual), len(expected))
        for row in actual:
            source = expected[row["result_id"], row["source_field"], row["entry_index"]]
            self.assertEqual({key: row[key] for key in source}, source)

    def test_qwen_archival_view_reconstructs_totals_without_combining_cohorts(self):
        rows = qwen_replica_rows(REPO)
        self.assertEqual(len(rows), 4)
        for row in rows:
            self.assertEqual(row["output_budget_tokens_per_request"], 1024)
            self.assertEqual(row["total_requests"], row["replicas"] * row["requests_per_replica"])
            self.assertAlmostEqual(row["decode_tok_s_total"], sum(row["decode_tok_s_per_replica"]), places=9)
            self.assertAlmostEqual(row["decode_tok_s_total"], row["accepted_tokens_in_shared_interval"] /
                                   row["shared_decode_interval_seconds"], places=9)


if __name__ == "__main__":
    unittest.main()
