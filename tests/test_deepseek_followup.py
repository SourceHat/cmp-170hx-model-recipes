"""Protect the separate DeepSeek cohort and its incomplete candidate evidence."""
from copy import deepcopy
import json
from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'scripts'))
from deepseek_followup import expected_tables, verify_data, verify_reference_profile


class DeepSeekFollowupTests(unittest.TestCase):
    def setUp(self):
        self.data = json.loads((ROOT / 'data/deepseek-1017-20261026/results.json').read_text())

    def test_reference_profile_and_every_csv_cell(self):
        self.assertTrue(verify_reference_profile(ROOT)['passed'])

    def test_candidate_missing_measurements_are_not_zero(self):
        changed = deepcopy(self.data)
        changed['candidate']['comparison'][-1]['candidate_generation_tokens_per_second'] = 0
        with self.assertRaises(AssertionError):
            verify_data(changed)

    def test_median_corruption_is_rejected(self):
        changed = deepcopy(self.data)
        changed['baseline']['primary_summary'][0]['generation_median_tokens_per_second'] += 1
        with self.assertRaises(AssertionError):
            verify_data(changed)

    def test_batch_completion_keeps_its_full_wall_time(self):
        changed = deepcopy(self.data)
        changed['baseline']['concurrent_batches'][0]['aggregate_completion_tokens_per_second'] += 1
        with self.assertRaises(AssertionError):
            verify_data(changed)

    def test_startup_repair_does_not_resolve_gpu_fault(self):
        changed = deepcopy(self.data)
        changed['deployment_verification']['gpu_stall_repair_proven'] = True
        with self.assertRaises(AssertionError):
            verify_data(changed)

    def test_incomplete_cells_remain_explicit_in_display_values(self):
        table = list(expected_tables(self.data).values())[-1]
        self.assertEqual(table[3][-1], '4 completed; next request failed')
        self.assertEqual(table[4][2:4], ['Unmeasured', 'Unmeasured'])


if __name__ == '__main__':
    unittest.main()
