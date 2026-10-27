import copy
import json
from pathlib import Path
import sys
import unittest

REPO = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO / "scripts"))
from history_docs import load_history
from validate_history import receipt, validate_documents


class HistoryTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.original = load_history(REPO)
        sources = json.loads((REPO / "archive/history/sources.json").read_text())["sources"]
        cls.sources = {(row["file"], row["sha256"]) for row in sources}

    def test_missing_archived_profile_cannot_be_hidden_by_adjusting_total_count(self):
        history = copy.deepcopy(self.original)
        name = history["coverage"]["archived_profile_ids"][0]
        history["records"] = [record for record in history["records"] if record["id"] != name]
        history["coverage"]["historical_records"] -= 1
        with self.assertRaisesRegex(ValueError, "archived profile coverage"):
            validate_documents(history, self.sources)

    def test_latency_estimate_cannot_fill_synchronized_decode_rate(self):
        history = copy.deepcopy(self.original)
        point = next(point for point in history["points"].values()
                     if point.get("reported_after_first_token_tok_s_estimate"))
        point["decode_tok_s_aggregate"] = point["reported_after_first_token_tok_s_estimate"]
        with self.assertRaisesRegex(ValueError, "legacy estimate"):
            validate_documents(history, self.sources)

    def test_credited_rate_cannot_move_to_citing_configuration(self):
        history = copy.deepcopy(self.original)
        summary = next(row for row in history["summaries"].values()
                       if row["configuration_binding"] == "referenced_run_only"
                       and not row["referenced_source_available"] and row["citing_configuration_ids"])
        summary["configuration_ids"] = list(summary["citing_configuration_ids"])
        with self.assertRaisesRegex(ValueError, "credited result transferred"):
            validate_documents(history, self.sources)

    def test_decode_numerator_must_reconstruct_rate(self):
        history = copy.deepcopy(self.original)
        point = next(point for point in history["points"].values() if point["shared_decode_valid"])
        point["shared_decode_accepted_tokens"] += 1
        with self.assertRaisesRegex(ValueError, "decode accounting"):
            validate_documents(history, self.sources)

    def test_whole_wave_elapsed_time_cannot_be_replaced_with_decode_time(self):
        history = copy.deepcopy(self.original)
        point = next(point for point in history["points"].values() if point["end_to_end_accounting_matches"])
        point["elapsed_seconds"] /= 2
        with self.assertRaisesRegex(ValueError, "whole-wave denominator"):
            validate_documents(history, self.sources)

    def test_configuration_changes_require_an_updated_digest(self):
        history = copy.deepcopy(self.original)
        config = next(iter(history["configs"].values()))
        config["settings"]["context"] = 12345
        with self.assertRaisesRegex(ValueError, "configuration digest"):
            validate_documents(history, self.sources)

    def test_public_coverage_rejects_host_inventory_metadata(self):
        history = copy.deepcopy(self.original)
        history["coverage"]["ui_profile_names"] = history["coverage"]["archived_profile_ids"]
        with self.assertRaisesRegex(ValueError, "host inventory metadata"):
            validate_documents(history, self.sources)

    def test_encoded_source_paths_cannot_publish_deployment_details(self):
        name, checksum = next(iter(self.sources))
        origin = {"file": name, "sha256": checksum, "json_pointer": "/reports/~1run~1internal-service~1job.json/config"}
        with self.assertRaisesRegex(ValueError, "deployment details"):
            receipt(origin, self.sources)

    def test_neutral_source_locations_require_one_unambiguous_locator(self):
        name, checksum = next(iter(self.sources))
        origin = {"file": name, "sha256": checksum, "source_location_id": "loc-" + "a" * 24}
        receipt(origin, self.sources)
        origin["json_pointer"] = "/other-object"
        with self.assertRaisesRegex(ValueError, "invalid source object locator"):
            receipt(origin, self.sources)


if __name__ == "__main__":
    unittest.main()
