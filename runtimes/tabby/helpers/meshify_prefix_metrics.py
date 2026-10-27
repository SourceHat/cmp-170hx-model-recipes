"""Anonymous numeric prefix attribution, independent of payload diagnostics."""
import functools
import json
import math
import os
from pathlib import Path
import time


FIELDS = {
    'input_tokens': 'prefix_input_tokens',
    'eligible_prefix_tokens': 'prefix_eligible_tokens',
    'previous_observed_prefix_tokens': 'prefix_previous_observed_tokens',
    'previous_completed_prefix_tokens': 'prefix_previous_completed_tokens',
    'resident_prefix_tokens': 'prefix_resident_tokens',
    'valid_checkpoint_tokens': 'prefix_checkpoint_tokens',
    'restored_position_tokens': 'prefix_resume_tokens',
    'previous_completed_kv_missing_tokens': 'prefix_missing_kv_tokens',
    'resident_kv_without_state_tokens': 'prefix_state_gap_tokens',
    'shared_checkpoint_target_tokens': 'prefix_checkpoint_target_tokens',
    'active_jobs_at_allocation': 'prefix_active_jobs',
    'active_decode_at_allocation': 'prefix_active_decoders',
}
METRIC_KEYS = frozenset(FIELDS.values()) | frozenset({
    'prefix_attribution_available', 'prefix_allocation_count',
    'prefix_budget_loss_tokens', 'prefix_stranded_loss_tokens',
    'prefix_ancestry_break_tokens', 'prefix_session_known', 'prefix_input_changed',
})
SERVING_KEYS = (
    'prompt_tokens', 'cached_tokens', 'gen_tokens', 'prompt_time', 'gen_time',
    'queue_time', 'total_time', 'gen_tokens_per_sec', 'draft_accept', 'draft_reject',
)


def number(value):
    return (isinstance(value, (int, float)) and not isinstance(value, bool)
            and math.isfinite(value) and value >= 0)


def flatten_prefix_metrics(values):
    diagnostic = values.get('prefix_diagnostic') if isinstance(values, dict) else None
    rounds = diagnostic.get('rounds') if isinstance(diagnostic, dict) else None
    if not isinstance(rounds, list) or not rounds or not isinstance(rounds[0], dict):
        return {'prefix_attribution_available': 0}
    # Initial allocation explains cold/warm prefill rather than later output resumptions.
    row = rounds[0]
    result = {'prefix_attribution_available': 1}
    if number(diagnostic.get('allocations')):
        result['prefix_allocation_count'] = diagnostic['allocations']
    for source, target in FIELDS.items():
        if number(row.get(source)):
            result[target] = row[source]
    losses = row.get('checkpoint_loss_tokens')
    if isinstance(losses, dict):
        for source, target in [('budget', 'prefix_budget_loss_tokens'),
                               ('stranded', 'prefix_stranded_loss_tokens')]:
            if number(losses.get(source)):
                result[target] = losses[source]
    if number(row.get('broken_ancestry_at_tokens')):
        result['prefix_ancestry_break_tokens'] = row['broken_ancestry_at_tokens']
    if isinstance(row.get('session_history_known'), bool):
        known = row['session_history_known']
        result['prefix_session_known'] = int(known)
        if known and isinstance(row.get('session_prefix_changed'), bool):
            result['prefix_input_changed'] = int(row['session_prefix_changed'])
    return result


def install(backend, path=None):
    """Optionally retain counts/timing without messages, fingerprints or identities."""
    destination = path or os.environ.get('MESHIFY_PREFIX_METRICS_PATH')
    if not destination:
        return None
    destination = Path(destination)
    original = backend.log_metrics
    observer = {'write_errors': 0}

    @functools.wraps(original)
    def observed(*args, **kwargs):
        values = next((value for value in (*args, *kwargs.values())
                       if isinstance(value, dict) and 'gen_tokens' in value), None)
        if values is not None:
            row = {'at': time.time(), **{k: values[k] for k in SERVING_KEYS
                                         if number(values.get(k))},
                   **flatten_prefix_metrics(values)}
            try:
                with destination.open('a') as output:
                    output.write(json.dumps(row, separators=(',', ':'), allow_nan=False) + '\n')
            except (OSError, ValueError):
                observer['write_errors'] += 1
        return original(*args, **kwargs)

    backend.log_metrics = observed
    return observer
