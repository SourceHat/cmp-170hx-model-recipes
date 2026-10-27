"""Protect the unified public inventory and exact model identities."""
import json
import hashlib
from pathlib import Path
import re
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'scripts'))
from model_names import MODEL_NAMES, display_names


class CurrentInventoryTests(unittest.TestCase):
    def test_every_selected_configuration_has_one_discoverable_entry(self):
        catalog = json.loads((ROOT / 'catalog.json').read_text())
        entries = catalog['configurations']
        self.assertEqual(len(entries), 9)
        self.assertEqual({row['id'] for row in entries}, set(MODEL_NAMES))
        self.assertEqual(len({row['id'] for row in entries}), len(entries))
        readme = (ROOT / 'README.md').read_text()
        inventory = readme.split('## Serving Configurations', 1)[1].split('## Measured Performance', 1)[0]
        for entry in entries:
            self.assertTrue((ROOT / entry['configuration']).is_file())
            self.assertTrue((ROOT / entry['documentation']).is_file())
            self.assertEqual(entry['name'], MODEL_NAMES[entry['id']])
            self.assertIn(f"[{entry['name']}]({entry['documentation']})", inventory)
        native = next(row for row in entries if '1017' in row['id'])
        self.assertEqual(native['setup'], 'qualified-native-runtime')

    def test_current_pages_do_not_present_a_dated_addendum(self):
        paths = [ROOT / 'README.md', ROOT / 'docs/DEEPSEEK-1017.md',
                 ROOT / 'data/deepseek-1017-20261026/README.md',
                 ROOT / 'profiles/deepseek-v41-flash-1017-dspark5-tp4/README.md']
        for path in paths:
            text = path.read_text()
            self.assertNotRegex(text, r'(?i)follow.up|addendum|26 October|October 2026')
        readme = paths[0].read_text()
        self.assertIn('### Short-Output Comparisons', readme)
        self.assertIn('### DeepSeek V4.1 Flash 1017 TP4: Long Outputs', readme)
        self.assertIn('prefix reuse permitted', readme)
        self.assertIn('including prefill and scheduling', readme)

    def test_display_identity_is_complete_and_does_not_rewrite_source_paths(self):
        for path in (ROOT / 'recipes').glob('*/recipe.json'):
            recipe = json.loads(path.read_text())
            self.assertEqual(recipe['short_name'], MODEL_NAMES[recipe['id']])
        mimo = json.loads((ROOT / 'recipes/mimo-flash-mtp1-tp3/recipe.json').read_text())
        self.assertIn('MiMo-V2.6-Flash', mimo['model']['hf_repo'])
        for text in ['Orca', 'MiMo', 'GLM Flash', 'Flash Next',
                     'https://huggingface.co/MikeRoz/MiMo-V2.6-Flash-MOPD-4.03bpw-h8-exl3']:
            self.assertEqual(display_names(display_names(text)), display_names(text))
        figures = json.loads((ROOT / 'data/figure-label-adaptations.json').read_text())['figures']
        self.assertEqual(len(figures), 6)
        for figure in figures:
            content = (ROOT / figure['file']).read_bytes()
            self.assertEqual(hashlib.sha256(content).hexdigest(), figure['sha256'])
            self.assertNotIn('DeepSeek 1017', content.decode())
            self.assertNotRegex(content.decode(), r'(?i)follow.up|26 OCT(?:OBER)? 2026')
            self.assertTrue(figure['geometry_unchanged'])


if __name__ == '__main__':
    unittest.main()
