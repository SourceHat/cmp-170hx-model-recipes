import importlib.util
import json
from pathlib import Path
import shutil
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("apex_capacity", ROOT / "scripts/apex_capacity.py")
capacity = importlib.util.module_from_spec(spec)
spec.loader.exec_module(capacity)


class ApexCapacityTests(unittest.TestCase):
    def test_two_loads_reproduce_capacity_and_keep_the_speed_cohort_separate(self):
        result = capacity.verify_capacity(ROOT)
        self.assertEqual(result["independent_loads"], 2)
        self.assertEqual(result["resident_pool_tokens"], 1374976)
        points = json.loads((ROOT / "recipes" / capacity.RECIPE / "benchmarks.json").read_text())["points"]
        headline = [point for point in points if point["headline_eligible"]]
        self.assertTrue(headline)
        self.assertTrue(all(point["tested_kv_pool_tokens"] != 1374976 for point in headline))
        self.assertTrue(all(value > .95 for value in result["distinct_history_pool_fractions"]))

    def fixture(self, temporary):
        root = Path(temporary)
        shutil.copytree(ROOT / capacity.DATA, root / capacity.DATA)
        shutil.copytree(ROOT / "recipes" / capacity.RECIPE, root / "recipes" / capacity.RECIPE)
        return root

    def test_altered_numerical_receipt_is_rejected(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = self.fixture(temporary)
            path = root / capacity.DATA / "qualification-report.json"
            data = json.loads(path.read_text())
            data["validated_pool_tokens"] += 256
            path.write_text(json.dumps(data))
            with self.assertRaisesRegex(ValueError, "Source identity"):
                capacity.verify_capacity(root)

    def test_changed_rank_order_cannot_reuse_the_qualification(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = self.fixture(temporary)
            path = root / "recipes" / capacity.RECIPE / "recipe.json"
            data = json.loads(path.read_text())
            data["engine_config"]["model"]["autosplit_reserve"].reverse()
            path.write_text(json.dumps(data))
            with self.assertRaisesRegex(ValueError, "placement"):
                capacity.verify_capacity(root)

    def test_derived_occupancy_cannot_be_inflated(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = self.fixture(temporary)
            path = root / capacity.DATA / "evidence.json"
            data = json.loads(path.read_text())
            data["independent_loads"][0]["pool_fraction"] = 1
            path.write_text(json.dumps(data))
            with self.assertRaisesRegex(ValueError, "Capacity evidence"):
                capacity.verify_capacity(root)
