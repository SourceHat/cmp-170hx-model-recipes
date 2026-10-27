import copy
import json
from pathlib import Path
import sys
import unittest

REPO = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO / "scripts"))
from validate_archive import validate_archive, validate_record


class ArchiveTests(unittest.TestCase):
    def records(self, name):
        folder = REPO / "archive" / name
        records = [json.loads((folder / filename).read_text()) for filename in
                   ("profile.json", "benchmarks.json", "evidence.json", "engine-config.json")]
        comparison = json.loads((REPO / "data/runtime-trials.json").read_text())["cases"][name]
        return [*records, comparison]

    def test_archive_preserves_four_distinct_waves(self):
        active = {row["id"] for row in json.loads((REPO / "catalog.json").read_text())["recipes"]}
        self.assertEqual(validate_archive(REPO, active), (2, 4))

    def test_iq4_whole_wave_rate_cannot_be_reported_as_decode(self):
        records = self.records("strata-q4-single")
        point = records[1]["points"][1]
        point["decode_tok_s_aggregate"] = point["end_to_end_accepted_tok_s"]
        with self.assertRaisesRegex(ValueError, "unqualified decode"):
            validate_record(*records)

    def test_resident_pool_cannot_include_host_capacity(self):
        records = self.records("strata-q6-split")
        kv = records[0]["serving"]["kv"]
        kv["resident_batch_gpu_tokens"] = kv["logical_batch_tokens"]
        with self.assertRaisesRegex(ValueError, "KV capacity"):
            validate_record(*records)

    def test_whole_wave_rate_must_use_all_outputs_and_elapsed_time(self):
        records = self.records("strata-q6-split")
        records[1]["points"][1]["elapsed_seconds"] /= 6
        with self.assertRaisesRegex(ValueError, "throughput denominator"):
            validate_record(*records)

    def test_archived_runtime_cannot_claim_supported_launcher(self):
        records = self.records("strata-q4-single")
        records[0]["launcher_supported"] = True
        with self.assertRaisesRegex(ValueError, "launcher support"):
            validate_record(*records)

    def test_credentials_and_listener_values_remain_placeholders(self):
        original = self.records("strata-q4-single")
        for field, value in (("api_key", "example-value"), ("host", "0.0.0.0"), ("port", 9000)):
            records = copy.deepcopy(original)
            records[3][field] = value
            with self.subTest(field=field), self.assertRaisesRegex(ValueError, "placeholders"):
                validate_record(*records)


if __name__ == "__main__":
    unittest.main()
