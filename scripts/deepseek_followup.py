"""Audit the frozen DeepSeek 1017 follow-up without inference dependencies."""
import csv
import json
import math
from pathlib import Path
import statistics


DATA_DIRECTORY = 'deepseek-1017-20261026'
COMPARISON_CAPTION = 'DeepSeek 1017: baseline and incomplete batched candidate'
TABLE_CAPTIONS = (
    'DeepSeek 1017: retained four-card baseline',
    'DeepSeek 1017: individual long-input requests',
    'DeepSeek 1017: four-request whole-batch completion',
    COMPARISON_CAPTION,
)
COLLECTIONS = {
    'baseline-primary.csv': ('baseline', 'primary_observations'),
    'baseline-summary.csv': ('baseline', 'primary_summary'),
    'baseline-long-context.csv': ('baseline', 'long_context_observations'),
    'baseline-concurrency.csv': ('baseline', 'concurrent_batches'),
    'baseline-concurrent-requests.csv': ('baseline', 'concurrent_request_observations'),
    'candidate-primary.csv': ('candidate', 'primary_observations'),
    'candidate-comparison.csv': ('candidate', 'comparison'),
    'candidate-attempts.csv': ('candidate', 'attempts'),
}


def collection(name, data):
    section, key = COLLECTIONS[name]
    return data[section][key]


def expected_tables(data):
    number = lambda value: f'{value:,.2f}'
    integer = lambda value: f'{value:,}'
    baseline = [[integer(r['input_target_tokens']), integer(r['output_tokens']),
                 number(r['generation_median_tokens_per_second']), str(r['observations'])]
                for r in data['baseline']['primary_summary']]
    long = [[integer(r['prompt_tokens']), integer(r['accepted_token_count']),
             number(r['ttft_seconds']), number(r['generation_tokens_per_second']),
             number(r['total_seconds'])] for r in data['baseline']['long_context_observations']]
    scenarios = {
        'short': 'Four requests, each targeting 8,192 input tokens',
        'near_full': 'Near-full input plus 8,192/16,384/32,768-target-input companions',
    }
    batches = [[scenarios[r['scenario']], str(r['requests']), integer(r['accepted_token_count']),
                number(r['total_seconds']), number(r['aggregate_completion_tokens_per_second'])]
               for r in data['baseline']['concurrent_batches']]
    comparisons = []
    for r in data['candidate']['comparison']:
        complete = r['status'] == 'complete_cell'
        missing = r['status'] == 'not_reached'
        observations = ('Not reached' if missing else '5 of 5 completed' if complete
                        else '4 completed; next request failed')
        comparisons.append([
            integer(r['input_target_tokens']) + ' / ' + integer(r['output_tokens']),
            number(r['baseline_generation_tokens_per_second']),
            'Unmeasured' if missing else number(r['candidate_generation_tokens_per_second']),
            'Unmeasured' if missing else f"{r['generation_change_percent']:+.2f}%",
            observations,
        ])
    return dict(zip(TABLE_CAPTIONS, (baseline, long, batches, comparisons)))


def verify_data(data):
    assert data['decision'] == 'retain_baseline'
    assert data['candidate_adopted'] is False and data['qualifying_speedup_achieved'] is False
    config, protocol = data['configuration'], data['protocol']
    assert config['revision'] == 'afc7aa0aab98ee735c0f54e0a122019af1ac08f1'
    assert config['gpu_counts'] == [4] and config['context'] == 524288
    assert config['max_sessions'] == 4 and config['ram_kv_mib'] == 8192
    assert config['baseline_engram_io'] == 'serial' and config['candidate_engram_io'] == 'batched'
    assert protocol['prefix_reuse_permitted'] and not protocol['prefix_cache_flush_between_cases']
    assert not protocol['historical_tp3_results_directly_comparable']
    assert not protocol['between_run_baseline_drift_measured']
    assert protocol['prior_baseline_attempts_also_stalled']
    baseline, candidate = data['baseline'], data['candidate']
    assert len(baseline['primary_observations']) == baseline['successful_primary_observations'] == 30
    assert len(baseline['long_context_observations']) == 2
    assert len(baseline['concurrent_request_observations']) == 8
    assert baseline['successful_measured_requests'] == 30 + 2 + 8

    def observations(rows, summary, rate_key, count):
        assert len(rows) == count and all(r['success'] for r in rows)
        rates = [r['generation_tokens_per_second'] for r in rows]
        median = statistics.median(rates)
        assert summary[rate_key] == median
        return median, 2 * statistics.median(abs(r - median) for r in rates) / median

    for summary in baseline['primary_summary']:
        selected = [r for r in baseline['primary_observations']
                    if r['input_target_tokens'] == summary['input_target_tokens']
                    and r['output_ceiling'] == summary['output_tokens']]
        _, noise = observations(selected, summary, 'generation_median_tokens_per_second', 5)
        assert summary['relative_noise_2mad_over_median'] == noise
        assert summary['ttft_median_seconds'] == statistics.median(r['ttft_seconds'] for r in selected)
        assert summary['generation_min_tokens_per_second'] == min(r['generation_tokens_per_second'] for r in selected)
        assert summary['generation_max_tokens_per_second'] == max(r['generation_tokens_per_second'] for r in selected)
        assert all(r['accepted_token_count'] == summary['output_tokens'] for r in selected)
    for batch in baseline['concurrent_batches']:
        rows = [r for r in baseline['concurrent_request_observations'] if r['scenario'] == batch['scenario']]
        assert len(rows) == batch['requests'] == 4 and all(r['success'] for r in rows)
        assert all(r['accepted_token_count'] == 8192 for r in rows)
        assert sum(r['accepted_token_count'] for r in rows) == batch['accepted_token_count'] == 32768
        assert batch['throughput_includes_prefill'] and batch['prefix_reuse_permitted']
        assert math.isclose(batch['aggregate_completion_tokens_per_second'], 32768 / batch['total_seconds'], abs_tol=1e-12)
        assert batch['follows_individual_near_full_request'] == (batch['scenario'] == 'near_full')
        assert batch['per_request_generation_min_tokens_per_second'] == min(r['generation_tokens_per_second'] for r in rows)
        assert batch['per_request_generation_max_tokens_per_second'] == max(r['generation_tokens_per_second'] for r in rows)
    assert sum(r['success'] for r in candidate['primary_observations']) == 19
    assert len(candidate['primary_observations']) == 20
    assert candidate['primary_observations'][-1]['accepted_token_count'] == 3343
    assert candidate['attempts'][0]['accepted_token_count'] == 625
    for row, count in zip(candidate['comparison'], (5, 5, 5, 4, 0, 0), strict=True):
        assert row['candidate_successful_observations'] == count
        if not count:
            assert row['status'] == 'not_reached'
            assert row['candidate_generation_tokens_per_second'] is row['generation_change_percent'] is None
            continue
        samples = [r for r in candidate['primary_observations'] if r['success']
                   and r['input_target_tokens'] == row['input_target_tokens']
                   and r['output_ceiling'] == row['output_tokens']]
        median, noise = observations(samples, row, 'candidate_generation_tokens_per_second', count)
        assert row['candidate_relative_noise_2mad_over_median'] == noise
        assert math.isclose(row['generation_change_percent'],
                            100 * (median / row['baseline_generation_tokens_per_second'] - 1), abs_tol=1e-12)
        assert (row['status'] == 'complete_cell') == (count == 5)
    assert candidate['overall_generation_gain_percent'] is None
    assert candidate['concurrency_performance'] is candidate['long_context_performance'] is None
    deployment = data['deployment_verification']
    assert deployment['fresh_launch_passed'] and deployment['inference']['accepted_token_count'] == 256
    assert deployment['additional_primary_observations'] == deployment['additional_capacity_observations'] == 0
    assert not deployment['gpu_stall_repair_proven']
    assert len(deployment['correctness_checks']) == 4 and all(r['passed'] for r in deployment['correctness_checks'])


def verify_csvs(folder, data):
    checked = 0
    for name in COLLECTIONS:
        expected = collection(name, data)
        with (Path(folder) / name).open(newline='') as stream:
            reader = csv.DictReader(stream)
            rows, columns = list(reader), reader.fieldnames
        assert len(rows) == len(expected) and set(columns) == set().union(*(r.keys() for r in expected)), name
        for row, original in zip(rows, expected, strict=True):
            for key in columns:
                text, value = row[key], original.get(key)
                if value is None:
                    assert text == ''
                elif isinstance(value, bool):
                    assert text in (str(value), str(value).lower())
                elif isinstance(value, (dict, list)):
                    assert json.loads(text) == value
                elif isinstance(value, (float, int)):
                    assert float(text) == value
                else:
                    assert text == value
                checked += 1
    return checked


def verify_reference_profile(root):
    root = Path(root)
    name = 'deepseek-v41-flash-1017-dspark5-tp4'
    folder = root / 'profiles' / name
    data = json.loads((root / 'data' / DATA_DIRECTORY / 'results.json').read_text())
    profile = json.loads((folder / 'profile.json').read_text())
    metadata = json.loads((folder / 'metadata.json').read_text())
    verify_data(data)
    cells = verify_csvs(root / 'data' / DATA_DIRECTORY, data)
    for key in ('model', 'revision', 'base_model', 'base_revision', 'artifact_format',
                'context', 'max_sessions', 'chunk_size', 'ram_kv_mib', 'engram_row_cache_mib',
                'kv_dtype', 'enforce_eager', 'draft_mode', 'draft_tokens', 'power_watts',
                'gpu_counts', 'parallelism', 'gpu_memory_utilization', 'transport'):
        assert profile[key] == data['configuration'][key], key
    assert profile['performance'] == dict(engine='baseline', profile_steps=0)
    assert profile['batch_invariant'] is False
    assert profile['artifact_directory'] == '@MODEL_DIRECTORY@'
    assert profile['engram_directory'] == '@ENGRAM_DIRECTORY@' and profile['port'] == '@PORT@'
    assert metadata['source_profile_sha256'] == data['configuration']['profile_sha256_after_startup_repair']
    assert metadata['kv']['literal_resident_token_pool'] is None
    assert metadata['runtime']['uses_original_tp3_docker_launcher'] is False
    assert metadata['runtime']['clean_container_gpu_requalified'] is False
    assert metadata['qualification']['gpu_stall_cause_resolved'] is False
    entries = json.loads((root / 'catalog.json').read_text())['reference_profiles']
    assert entries == [dict(id=name, path=f'profiles/{name}/profile.json',
                            metadata=f'profiles/{name}/metadata.json', documentation=f'profiles/{name}/README.md')]
    return dict(passed=True, reference_profile=name, csv_cells_checked=cells)


def verify_followup(root):
    root = Path(root)
    data = json.loads((root / 'data' / DATA_DIRECTORY / 'results.json').read_text())
    verify_data(data)
    verify_csvs(root / 'data' / DATA_DIRECTORY, data)
    article = json.loads((root / 'article.json').read_text())
    tables = {b['caption']: b for b in article['blocks'] if b['type'] == 'table'}
    checked = []
    for caption, rows in expected_tables(data).items():
        assert tables[caption]['rows'] == rows, caption
        checked.append(dict(caption=caption, rows=len(rows), cells=sum(map(len, rows)),
                            cells_containing_numbers=sum(any(c.isdigit() for c in cell) for row in rows for cell in row)))
    assert tables[COMPARISON_CAPTION]['emphasizedCells'] == [[0, 1], [1, 2], [2, 1]]
    assert not any(tables[c].get('emphasizedCells') for c in TABLE_CAPTIONS[:3])
    text = '\n'.join(b.get('text', '') for b in article['blocks'])
    for phrase in ('Prefix caching was enabled', 'Earlier baseline attempts had also',
                   'between-run baseline', 'intermittent GPU stall remains'):
        assert phrase in text, phrase
    assert len([b for b in article['blocks'] if b['type'] == 'figure'
                and DATA_DIRECTORY in b['image']['src']]) == 3
    return dict(passed=True, baseline_primary_observations=30, baseline_measured_requests=40,
                candidate_completed_observations=19, tables=checked,
                candidate_adopted=False, numerical_scope='Saved observations and summary arithmetic; original stream timing is source-verified separately.')


if __name__ == '__main__':
    print(json.dumps(verify_reference_profile(Path(__file__).resolve().parents[1]), indent=2))
