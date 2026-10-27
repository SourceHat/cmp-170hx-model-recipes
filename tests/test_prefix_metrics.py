"""Numeric diagnostics preserve privacy and the original backend callback."""
import importlib.util
import json
from pathlib import Path
import tempfile
from types import SimpleNamespace
import unittest
from unittest.mock import patch

from test_prefix_diagnostics import pure_history, table


PATH = Path(__file__).resolve().parents[1] / 'runtimes/tabby/helpers/meshify_prefix_metrics.py'
SPEC = importlib.util.spec_from_file_location('numeric_prefix_metrics', PATH)
metrics = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(metrics)


class PrefixMetricsTests(unittest.TestCase):
    def values(self, resident_pages=20, checkpoint_pages=20):
        hashes = [str(i) for i in range(20)]
        history = pure_history()()
        history.completed_sequence(1, table(hashes).all_pages)
        state = {hashes[checkpoint_pages - 1]: {'position': checkpoint_pages * 256}} if checkpoint_pages else {}
        row = history.allocation(2, hashes, 5200, table(hashes[:resident_pages]), state)
        history.restored(row, checkpoint_pages * 256, None)
        return {'gen_tokens': 128, 'prefix_diagnostic': {'allocations': 1, 'rounds': [row]}}

    def test_complete_matching_history_has_no_cache_or_state_loss(self):
        flat = metrics.flatten_prefix_metrics(self.values())
        self.assertEqual(flat['prefix_previous_completed_tokens'], 5120)
        self.assertEqual(flat['prefix_resume_tokens'], 5120)
        self.assertEqual(flat['prefix_missing_kv_tokens'], 0)
        self.assertEqual(flat['prefix_state_gap_tokens'], 0)

    def test_missing_kv_and_missing_state_are_distinct(self):
        kv = metrics.flatten_prefix_metrics(self.values(8, 8))
        state = metrics.flatten_prefix_metrics(self.values(20, 8))
        self.assertEqual((kv['prefix_missing_kv_tokens'], kv['prefix_state_gap_tokens']), (3072, 0))
        self.assertEqual((state['prefix_missing_kv_tokens'], state['prefix_state_gap_tokens']), (0, 3072))

    def test_unknown_session_is_not_classified_as_unchanged_input(self):
        flat = metrics.flatten_prefix_metrics(self.values())
        self.assertEqual(flat['prefix_session_known'], 0)
        self.assertNotIn('prefix_input_changed', flat)

    def test_first_allocation_explains_prefill_after_output_resume(self):
        values = self.values()
        first = values['prefix_diagnostic']['rounds'][0]
        values['prefix_diagnostic'].update(allocations=2, rounds=[first, {'restored_position_tokens': 9999}])
        flat = metrics.flatten_prefix_metrics(values)
        self.assertEqual(flat['prefix_resume_tokens'], 5120)
        self.assertEqual(flat['prefix_allocation_count'], 2)

    def test_malformed_and_missing_fields_never_become_payloads(self):
        self.assertEqual(metrics.flatten_prefix_metrics({}), {'prefix_attribution_available': 0})
        for value in ('PRIVATE', True, float('nan'), float('inf'), -1):
            flat = metrics.flatten_prefix_metrics({'prefix_diagnostic': {'rounds': [{'input_tokens': value}]}})
            self.assertNotIn('prefix_input_tokens', flat)

    def test_numeric_logging_stays_private_with_payload_logging_disabled(self):
        calls = []
        backend = SimpleNamespace(log_metrics=lambda *a, **kw: calls.append((a, kw)) or 'original-result')
        values = self.values(8, 8)
        values.update(prompt_tokens=5200, cached_tokens=2048, prompt_time=0.25,
                      prompt='PRIVATE PROMPT', session_key='PRIVATE SESSION',
                      generated_text='PRIVATE OUTPUT', gen_time='PRIVATE TIME')
        values['prefix_diagnostic']['rounds'][0]['session_key'] = 'PRIVATE NESTED SESSION'
        with tempfile.TemporaryDirectory() as folder, patch.dict('os.environ', {'MESHIFY_MODEL_IO_LOGGING': '0'}):
            destination = Path(folder) / 'metrics.jsonl'
            observer = metrics.install(backend, destination)
            self.assertEqual(backend.log_metrics('caller', values, preserve=True), 'original-result')
            raw = destination.read_text()
            saved = json.loads(raw)
            self.assertNotIn('PRIVATE', raw)
            self.assertEqual(saved['prefix_missing_kv_tokens'], 3072)
            self.assertEqual(saved['prompt_time'], 0.25)
            self.assertNotIn('gen_time', saved)
            self.assertEqual(observer['write_errors'], 0)
        self.assertEqual(calls, [(('caller', values), {'preserve': True})])

    def test_diagnostic_io_failure_cannot_fail_the_request(self):
        calls = []
        backend = SimpleNamespace(log_metrics=lambda *a, **kw: calls.append(True) or 42)
        with tempfile.TemporaryDirectory() as folder:
            observer = metrics.install(backend, Path(folder) / 'missing/metrics.jsonl')
            self.assertEqual(backend.log_metrics(self.values()), 42)
            self.assertEqual(observer['write_errors'], 1)
        self.assertEqual(calls, [True])

    def test_disabled_numeric_logging_does_not_wrap_the_backend(self):
        original = lambda *a, **kw: 42
        backend = SimpleNamespace(log_metrics=original)
        with patch.dict('os.environ', {}, clear=True):
            self.assertIsNone(metrics.install(backend))
        self.assertIs(backend.log_metrics, original)


if __name__ == '__main__':
    unittest.main()
