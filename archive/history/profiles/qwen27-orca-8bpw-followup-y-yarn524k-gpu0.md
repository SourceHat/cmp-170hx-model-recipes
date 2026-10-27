# qwen27-orca-8bpw-followup-y-yarn524k-gpu0

**Historical record. Rate summary only.**

Model family: Orca (Qwen 3.8 27B abliterated).

Recorded archive reason: Historical configuration; later measured variants are recorded separately.

Historical configurations are provided for comparison. The [recommended recipes](../../../README.md) include supported launch scripts.

Current recipes using the same recorded checkpoint repository: [qwen27-orca-mtp3-native](../../../recipes/qwen27-orca-mtp3-native/README.md). Context, cache and runtime versions can differ.

## Saved Configuration Versions

Each configuration ID identifies a distinct original settings record. Deployment fields are omitted; versions can have identical published settings after that omission. Upstream runtime commits remain unspecified where the source retained only an integration label.

| Configuration | Recorded artifact / source | Configured card counts | Context tokens | GPU pool tokens | Slots | Draft mode / tokens |
| --- | --- | --- | --- | --- | --- | --- |
| cfg-642d9cf86f7495246d8e | [Lygodactylus/Qwen3.8-27B-Uncensored-exl3-8bpw@3487b152b3](https://huggingface.co/Lygodactylus/Qwen3.8-27B-Uncensored-exl3-8bpw/tree/3487b152b302930e303dc4a2e99e7e976e3ad28f) (derived view) | 1 | 524,288 | 524,288 | 1 | mtp / 3 |
| cfg-c2078a3405e7126a029f | [Lygodactylus/Qwen3.8-27B-Uncensored-exl3-8bpw@3487b152b3](https://huggingface.co/Lygodactylus/Qwen3.8-27B-Uncensored-exl3-8bpw/tree/3487b152b302930e303dc4a2e99e7e976e3ad28f) (derived view) | 1 | 524,288 | 524,288 | 1 | mtp / 3 |

Card counts are saved configuration choices, not a claim that every allowed placement was measured. A derived view can differ from its pinned download source.

<details>
<summary>cfg-642d9cf86f7495246d8e</summary>

```json
{
  "kind": "tabby",
  "gpu_counts": [
    1
  ],
  "context": 524288,
  "cache_tokens": 524288,
  "cache_mode": "Q8",
  "draft_cache_mode": "Q8",
  "draft_mode": "mtp",
  "draft_tokens": 3,
  "max_sessions": 1,
  "chunk_size": 2048,
  "reserve_mib": 4096,
  "ram_kv_mib": 4096,
  "ram_recurrent_mib": 4096,
  "dynamic_draft": false,
  "power_watts": 200,
  "host_memory_gib": 40,
  "host_swap_gib": 0,
  "min_vram_mib_per_gpu": 60000,
  "min_effective_vram_mib": 60000,
  "model_repository": "Lygodactylus/Qwen3.8-27B-Uncensored-exl3-8bpw",
  "model_revision": "3487b152b302930e303dc4a2e99e7e976e3ad28f",
  "draft_repository": null,
  "draft_revision": null,
  "recorded_runtime_label": null,
  "served_model_label": "qwen27-orca-exl3-8bpw-yarn524k",
  "derived_model_view_used": true,
  "model_view_metadata_included": false,
  "power_watts_values_unordered": []
}
```

Pinned model revision recorded: yes. Source receipt labels, hashes and object locators are retained in [configurations.json](../configurations.json).

</details>

<details>
<summary>cfg-c2078a3405e7126a029f</summary>

```json
{
  "kind": "tabby",
  "gpu_counts": [
    1
  ],
  "context": 524288,
  "cache_tokens": 524288,
  "cache_mode": "Q8",
  "draft_cache_mode": "Q8",
  "draft_mode": "mtp",
  "draft_tokens": 3,
  "max_sessions": 1,
  "chunk_size": 2048,
  "reserve_mib": 4096,
  "ram_kv_mib": 4096,
  "ram_recurrent_mib": 4096,
  "dynamic_draft": false,
  "power_watts": 200,
  "host_memory_gib": 40,
  "host_swap_gib": 0,
  "min_vram_mib_per_gpu": 60000,
  "min_effective_vram_mib": 60000,
  "model_repository": "Lygodactylus/Qwen3.8-27B-Uncensored-exl3-8bpw",
  "model_revision": "3487b152b302930e303dc4a2e99e7e976e3ad28f",
  "draft_repository": null,
  "draft_revision": null,
  "recorded_runtime_label": null,
  "served_model_label": "qwen27-orca-exl3-8bpw-yarn524k",
  "derived_model_view_used": true,
  "model_view_metadata_included": false
}
```

Pinned model revision recorded: yes. Source receipt labels, hashes and object locators are retained in [configurations.json](../configurations.json).

</details>

## Retained Measurements

No detailed benchmark receipt is matched to this record. A saved definition or a successful job exit alone is not a performance measurement.

A dash in shared decode means no qualified synchronized interval is available. Whole-wave throughput includes prefill and queueing. A valid decode interval can survive inside an overall failed or partial check; the source-report outcome is preserved. No rows are averaged.

## Reported Rate Summaries

| Summary | Original field | Reported tok/s | Requests | Configuration binding |
| --- | --- | --- | --- | --- |
| summary-5c1b2ee8e06ee8904554 | single_generated_tps | 26.03 | 1 | referenced_run_only |
| summary-d2389a52c5de4a291869 | four_request_generated_tps | 62.09 | 4 | referenced_run_only |

These quoted values can overlap detailed waves. A referenced earlier run's rate is not transferred to the citing configuration. Missing input, request and timing-window evidence remains missing. See [rate-summaries.json](../rate-summaries.json).

## Bounded Checks

| Check | Reported outcome | Retained counts / flags |
| --- | --- | --- |
| check-9a28b9a1202d124ffcb7 | Pass | {"passed":true,"actual_input_tokens":[524147,524147],"context_limit":524288} |
| check-ab3d2b6ac32190b85767 | Pass | {"passed":true,"actual_input_tokens":[524147,524147],"context_limit":524288} |

These checks retain their reported scope. A context/allocation/retrieval check is not a general quality score or a speed qualification at that context. Exact flags and provenance are in [checks.json](../checks.json).

## Additional Test Results

| Result / Source | Profile | Evidence type | Reported outcome | Retained values | Configuration binding |
| --- | --- | --- | --- | --- | --- |
| [result-1825990eeb689db4e16f](../observations.json)<br>source-ab89fca7e0f49696d5258b56.json<br>`/profiles/22/current_config` | [qwen27-orca-8bpw-followup-y-yarn524k-gpu0](qwen27-orca-8bpw-followup-y-yarn524k-gpu0.md) | context allocation | Outcome unspecified | cache_tokens=524,288 tokens; context=524,288 tokens; reserve_mib=4,096 MiB | Recorded configuration/job |
| [result-2738c86b3dfe403e115a](../observations.json)<br>source-d0a5a9be710c227136a6efd5.json<br>`/phases/yarn524k/RAM_return/before_return/totals` | [qwen27-orca-8bpw-followup-y-yarn524k-gpu0](qwen27-orca-8bpw-followup-y-yarn524k-gpu0.md) | context allocation | Outcome unspecified | cached_tokens=0 tokens; generated_tokens=100 accepted tokens; prompt_tokens=556,965 tokens; recurrent_restores=0 checkpoints | Recorded configuration/job |
| [result-2e7264619d2fbabbe5f7](../observations.json)<br>source-d0a5a9be710c227136a6efd5.json<br>`/phases/yarn524k/trace_readiness/0` | [qwen27-orca-8bpw-followup-y-yarn524k-gpu0](qwen27-orca-8bpw-followup-y-yarn524k-gpu0.md) | test outcome | complete | generated_tokens=3 accepted tokens | Recorded configuration/job |
| [result-2ee1a9398efb208180a8](../observations.json)<br>source-d0a5a9be710c227136a6efd5.json<br>`/phases/yarn524k/RAM_return/before_pressure` | [qwen27-orca-8bpw-followup-y-yarn524k-gpu0](qwen27-orca-8bpw-followup-y-yarn524k-gpu0.md) | test outcome | Outcome unspecified | context=524,288 tokens | Recorded configuration/job |
| [result-302e34ad6c11bf8f35da](../observations.json)<br>source-d0a5a9be710c227136a6efd5.json<br>`/phases/yarn524k/RAM_return/before_pressure/cache` | [qwen27-orca-8bpw-followup-y-yarn524k-gpu0](qwen27-orca-8bpw-followup-y-yarn524k-gpu0.md) | test outcome | Outcome unspecified | cached_tokens=524,032 tokens | Recorded configuration/job |
| [result-48e6b6c778590eb0f32c](../observations.json)<br>source-d0a5a9be710c227136a6efd5.json<br>`/phases/yarn524k/RAM_return/after_return` | [qwen27-orca-8bpw-followup-y-yarn524k-gpu0](qwen27-orca-8bpw-followup-y-yarn524k-gpu0.md) | test outcome | Outcome unspecified | context=524,288 tokens | Recorded configuration/job |
| [result-50b1642a338c45837b5b](../observations.json)<br>source-d0a5a9be710c227136a6efd5.json<br>`/phases/yarn524k/RAM_return/after_return/cache` | [qwen27-orca-8bpw-followup-y-yarn524k-gpu0](qwen27-orca-8bpw-followup-y-yarn524k-gpu0.md) | test outcome | Outcome unspecified | cached_tokens=524,032 tokens | Recorded configuration/job |
| [result-5549fbf9e2d03abd0fcd](../observations.json)<br>source-d0a5a9be710c227136a6efd5.json<br>`/phases/yarn524k/RAM_return/after_return/totals` | [qwen27-orca-8bpw-followup-y-yarn524k-gpu0](qwen27-orca-8bpw-followup-y-yarn524k-gpu0.md) | context allocation | Outcome unspecified | cached_tokens=524,032 tokens; generated_tokens=165 accepted tokens; prompt_tokens=1,081,112 tokens; recurrent_restores=1 checkpoints | Recorded configuration/job |
| [result-8fb3978851d477498d81](../observations.json)<br>source-d0a5a9be710c227136a6efd5.json<br>`/phases/yarn524k/RAM_return/before_return` | [qwen27-orca-8bpw-followup-y-yarn524k-gpu0](qwen27-orca-8bpw-followup-y-yarn524k-gpu0.md) | test outcome | Outcome unspecified | context=524,288 tokens | Recorded configuration/job |
| [result-ca7505dd8ab453a7d46a](../observations.json)<br>source-d0a5a9be710c227136a6efd5.json<br>`/phases/yarn524k/RAM_return/before_pressure/totals` | [qwen27-orca-8bpw-followup-y-yarn524k-gpu0](qwen27-orca-8bpw-followup-y-yarn524k-gpu0.md) | context allocation | Outcome unspecified | cached_tokens=0 tokens; generated_tokens=68 accepted tokens; prompt_tokens=524,207 tokens; recurrent_restores=0 checkpoints | Recorded configuration/job |
| [result-f688aa7dc099979fe360](../observations.json)<br>source-d0a5a9be710c227136a6efd5.json<br>`/phases/yarn524k/RAM_return/before_return/cache` | [qwen27-orca-8bpw-followup-y-yarn524k-gpu0](qwen27-orca-8bpw-followup-y-yarn524k-gpu0.md) | test outcome | Outcome unspecified | cached_tokens=524,032 tokens | Recorded configuration/job |

These are saved result records, including failures and bounded checks. Copies, individual requests, report summaries and regrading can overlap; their counts are not independent test repetitions. Open each result for exact values, units, configuration binding and source receipts.

There are 1 retained lifecycle records. Their states, exit codes and configuration IDs remain in [catalog.json](../catalog.json); they do not supply missing benchmark results.

[Full archive](../../README.md) | [All retained waves](../RESULTS.md) | [Data definitions](../DATA.md) | [Recommended recipes](../../../README.md)
