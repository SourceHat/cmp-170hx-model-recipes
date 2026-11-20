# qwen27-huihui-6p5-followup-y-native-gpu0

**Historical record. Rate summary only.**

Model family: Huihui Qwen 3.8 27B abliterated.

Recorded archive reason: Alternative abliterated checkpoint; compare with the retained Orca configurations.

Historical configurations are provided for comparison. The [recommended recipes](../../../README.md) include supported launch scripts.

## Saved Configuration Versions

Each configuration ID identifies a distinct original settings record. Deployment fields are omitted; versions can have identical published settings after that omission. Upstream runtime commits remain unspecified where the source retained only an integration label.

| Configuration | Recorded artifact / source | Configured card counts | Context tokens | GPU pool tokens | Slots | Draft mode / tokens |
| --- | --- | --- | --- | --- | --- | --- |
| cfg-4ad90882b4ed4a42be4d | [sakamakismile/Huihui-Qwen3.8-27B-abliterated-EXL3-6.5bpw@b4398c7154](https://huggingface.co/sakamakismile/Huihui-Qwen3.8-27B-abliterated-EXL3-6.5bpw/tree/b4398c715475e05798ca507f1651887159cccd39) (derived view) | 1 | 262,144 | 524,288 | 2 | mtp / 3 |
| cfg-82900b663a036cb64c31 | [sakamakismile/Huihui-Qwen3.8-27B-abliterated-EXL3-6.5bpw@b4398c7154](https://huggingface.co/sakamakismile/Huihui-Qwen3.8-27B-abliterated-EXL3-6.5bpw/tree/b4398c715475e05798ca507f1651887159cccd39) (derived view) | 1 | 262,144 | 524,288 | 2 | mtp / 3 |

Card counts are saved configuration choices, not a claim that every allowed placement was measured. A derived view can differ from its pinned download source.

<details>
<summary>cfg-4ad90882b4ed4a42be4d</summary>

```json
{
  "kind": "tabby",
  "gpu_counts": [
    1
  ],
  "context": 262144,
  "cache_tokens": 524288,
  "cache_mode": "Q8",
  "draft_cache_mode": "Q8",
  "draft_mode": "mtp",
  "draft_tokens": 3,
  "max_sessions": 2,
  "chunk_size": 2048,
  "reserve_mib": 4096,
  "ram_kv_mib": 4096,
  "ram_recurrent_mib": 4096,
  "dynamic_draft": false,
  "power_watts": 200,
  "host_memory_gib": 32,
  "host_swap_gib": 0,
  "min_vram_mib_per_gpu": 60000,
  "min_effective_vram_mib": 60000,
  "model_repository": "sakamakismile/Huihui-Qwen3.8-27B-abliterated-EXL3-6.5bpw",
  "model_revision": "b4398c715475e05798ca507f1651887159cccd39",
  "draft_repository": null,
  "draft_revision": null,
  "recorded_runtime_label": null,
  "served_model_label": "qwen27-huihui-exl3-6p5",
  "derived_model_view_used": true,
  "model_view_metadata_included": false,
  "power_watts_values_unordered": []
}
```

Pinned model revision recorded: yes. Source receipt labels, hashes and object locators are retained in [configurations.json](../configurations.json).

</details>

<details>
<summary>cfg-82900b663a036cb64c31</summary>

```json
{
  "kind": "tabby",
  "gpu_counts": [
    1
  ],
  "context": 262144,
  "cache_tokens": 524288,
  "cache_mode": "Q8",
  "draft_cache_mode": "Q8",
  "draft_mode": "mtp",
  "draft_tokens": 3,
  "max_sessions": 2,
  "chunk_size": 2048,
  "reserve_mib": 4096,
  "ram_kv_mib": 4096,
  "ram_recurrent_mib": 4096,
  "dynamic_draft": false,
  "power_watts": 200,
  "host_memory_gib": 32,
  "host_swap_gib": 0,
  "min_vram_mib_per_gpu": 60000,
  "min_effective_vram_mib": 60000,
  "model_repository": "sakamakismile/Huihui-Qwen3.8-27B-abliterated-EXL3-6.5bpw",
  "model_revision": "b4398c715475e05798ca507f1651887159cccd39",
  "draft_repository": null,
  "draft_revision": null,
  "recorded_runtime_label": null,
  "served_model_label": "qwen27-huihui-exl3-6p5",
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
| summary-5d286ad12b813fc8bfb0 | four_request_generated_tps | 55.30 | 4 | referenced_run_only |
| summary-c479ea493ba98f7cbd95 | single_generated_tps | 25.44 | 1 | referenced_run_only |

These quoted values can overlap detailed waves. A referenced earlier run's rate is not transferred to the citing configuration. Missing input, request and timing-window evidence remains missing. See [rate-summaries.json](../rate-summaries.json).

## Bounded Checks

| Check | Reported outcome | Retained counts / flags |
| --- | --- | --- |
| check-c88db614c7c8dc5b47c5 | Pass | {"passed":true,"actual_input_tokens":[261985,261985,261985,261985],"context_limit":262144} |
| check-df088cd0ad34a2427656 | Pass | {"passed":true,"actual_input_tokens":[261985,261985,261985,261985],"context_limit":262144} |

These checks retain their reported scope. A context/allocation/retrieval check is not a general quality score or a speed qualification at that context. Exact flags and provenance are in [checks.json](../checks.json).

## Additional Test Results

| Result / Source | Profile | Evidence type | Reported outcome | Retained values | Configuration binding |
| --- | --- | --- | --- | --- | --- |
| [result-0117d328fc80a08388b4](../observations.json)<br>source-f7d98939d8e8ede4bc1ca721.json<br>`/RAM_return/after_return/totals` | [qwen27-huihui-6p5-followup-y-native-gpu0](qwen27-huihui-6p5-followup-y-native-gpu0.md) | context allocation | Outcome unspecified | cached_tokens=261,888 tokens; generated_tokens=210 accepted tokens; prompt_tokens=818,771 tokens; recurrent_restores=1 checkpoints | Recorded configuration/job |
| [result-049930fe3df31b25b8cf](../observations.json)<br>source-f7d98939d8e8ede4bc1ca721.json<br>`/trace_readiness/0` | [qwen27-huihui-6p5-followup-y-native-gpu0](qwen27-huihui-6p5-followup-y-native-gpu0.md) | test outcome | complete | generated_tokens=3 accepted tokens | Recorded configuration/job |
| [result-049d68fa02f0918141b0](../observations.json)<br>source-f7d98939d8e8ede4bc1ca721.json<br>`/RAM_return/before_return` | [qwen27-huihui-6p5-followup-y-native-gpu0](qwen27-huihui-6p5-followup-y-native-gpu0.md) | test outcome | Outcome unspecified | context=262,144 tokens | Recorded configuration/job |
| [result-160a262aa52abe2993f7](../observations.json)<br>source-f7d98939d8e8ede4bc1ca721.json<br>`/RAM_return/before_return/totals` | [qwen27-huihui-6p5-followup-y-native-gpu0](qwen27-huihui-6p5-followup-y-native-gpu0.md) | context allocation | Outcome unspecified | cached_tokens=0 tokens; generated_tokens=150 accepted tokens; prompt_tokens=556,786 tokens; recurrent_restores=0 checkpoints | Recorded configuration/job |
| [result-169c11951e372456df2f](../observations.json)<br>source-f7d98939d8e8ede4bc1ca721.json<br>`/RAM_return/before_return/cache` | [qwen27-huihui-6p5-followup-y-native-gpu0](qwen27-huihui-6p5-followup-y-native-gpu0.md) | test outcome | Outcome unspecified | cached_tokens=523,776 tokens | Recorded configuration/job |
| [result-2dc6b1fd6a844a714605](../observations.json)<br>source-f7d98939d8e8ede4bc1ca721.json<br>`/RAM_return/after_return/cache` | [qwen27-huihui-6p5-followup-y-native-gpu0](qwen27-huihui-6p5-followup-y-native-gpu0.md) | test outcome | Outcome unspecified | cached_tokens=523,776 tokens | Recorded configuration/job |
| [result-467ce41d7e5dca0076a7](../observations.json)<br>source-f7d98939d8e8ede4bc1ca721.json<br>`/RAM_return/after_return` | [qwen27-huihui-6p5-followup-y-native-gpu0](qwen27-huihui-6p5-followup-y-native-gpu0.md) | test outcome | Outcome unspecified | context=262,144 tokens | Recorded configuration/job |
| [result-530da17bcaab1a159410](../observations.json)<br>source-f7d98939d8e8ede4bc1ca721.json<br>`/RAM_return/before_pressure/cache` | [qwen27-huihui-6p5-followup-y-native-gpu0](qwen27-huihui-6p5-followup-y-native-gpu0.md) | test outcome | Outcome unspecified | cached_tokens=523,776 tokens | Recorded configuration/job |
| [result-c698919e3b3c69920c00](../observations.json)<br>source-f7d98939d8e8ede4bc1ca721.json<br>`/RAM_return/before_pressure/totals` | [qwen27-huihui-6p5-followup-y-native-gpu0](qwen27-huihui-6p5-followup-y-native-gpu0.md) | context allocation | Outcome unspecified | cached_tokens=0 tokens; generated_tokens=118 accepted tokens; prompt_tokens=524,029 tokens; recurrent_restores=0 checkpoints | Recorded configuration/job |
| [result-e5ca7afee28f65c598e7](../observations.json)<br>source-f7d98939d8e8ede4bc1ca721.json<br>`/RAM_return/before_pressure` | [qwen27-huihui-6p5-followup-y-native-gpu0](qwen27-huihui-6p5-followup-y-native-gpu0.md) | test outcome | Outcome unspecified | context=262,144 tokens | Recorded configuration/job |

These are saved result records, including failures and bounded checks. Copies, individual requests, report summaries and regrading can overlap; their counts are not independent test repetitions. Open each result for exact values, units, configuration binding and source receipts.

There are 1 retained lifecycle records. Their states, exit codes and configuration IDs remain in [catalog.json](../catalog.json); they do not supply missing benchmark results.

[Full archive](../../README.md) | [All retained waves](../RESULTS.md) | [Data definitions](../DATA.md) | [Recommended recipes](../../../README.md)
