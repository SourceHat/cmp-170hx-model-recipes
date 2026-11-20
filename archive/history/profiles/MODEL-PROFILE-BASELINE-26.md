# MODEL-PROFILE-BASELINE-26

**Historical record. Rate summary only.**

Model family: Qwen 3.8 27B.

Historical configurations are provided for comparison. The [recommended recipes](../../../README.md) include supported launch scripts.

Current recipes using the same recorded checkpoint repository: [qwen3.8-27b-exl3](../../../recipes/qwen3.8-27b-exl3/README.md). Context, cache and runtime versions can differ.

## Saved Configuration Versions

Each configuration ID identifies a distinct original settings record. Deployment fields are omitted; versions can have identical published settings after that omission. Upstream runtime commits remain unspecified where the source retained only an integration label.

| Configuration | Recorded artifact / source | Configured card counts | Context tokens | GPU pool tokens | Slots | Draft mode / tokens |
| --- | --- | --- | --- | --- | --- | --- |
| cfg-dfdf847a6f55dd3a5792 | [turboderp/Qwen3.8-27B-exl3@9e4c23cfb2](https://huggingface.co/turboderp/Qwen3.8-27B-exl3/tree/9e4c23cfb23697165b8e2f6da2a1df995f66353c) | 1 | 262,144 | 917,504 | 16 | mtp / 1 |

Card counts are saved configuration choices, not a claim that every allowed placement was measured. A derived view can differ from its pinned download source.

<details>
<summary>cfg-dfdf847a6f55dd3a5792</summary>

```json
{
  "kind": "tabby",
  "gpu_counts": [
    1
  ],
  "context": 262144,
  "cache_tokens": 917504,
  "cache_mode": "Q8",
  "draft_cache_mode": "Q8",
  "draft_mode": "mtp",
  "draft_tokens": 1,
  "max_sessions": 16,
  "chunk_size": 2048,
  "reserve_mib": 4096,
  "ram_kv_mib": 10240,
  "ram_recurrent_mib": 7168,
  "dynamic_draft": false,
  "power_watts": 200,
  "host_memory_gib": 25,
  "host_swap_gib": 0,
  "min_vram_mib_per_gpu": 60000,
  "min_effective_vram_mib": 60000,
  "model_repository": "turboderp/Qwen3.8-27B-exl3",
  "model_revision": "9e4c23cfb23697165b8e2f6da2a1df995f66353c",
  "draft_repository": null,
  "draft_revision": null,
  "recorded_runtime_label": null,
  "served_model_label": "qwen3.8-27b",
  "power_watts_values_unordered": []
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
| summary-51b6c86af9cc710706fc | single_stream_per_card_aggregate_tps | 134.73 | Not recorded | referenced_run_only |
| summary-e3f5bafb217f38a41802 | sixteen_streams_per_card_aggregate_tps | 718.76 | Not recorded | referenced_run_only |

These quoted values can overlap detailed waves. A referenced earlier run's rate is not transferred to the citing configuration. Missing input, request and timing-window evidence remains missing. See [rate-summaries.json](../rate-summaries.json).

## Additional Test Results

| Result / Source | Profile | Evidence type | Reported outcome | Retained values | Configuration binding |
| --- | --- | --- | --- | --- | --- |
| [result-0b3300ff6b31d2e84720](../observations.json)<br>source-ab89fca7e0f49696d5258b56.json<br>`/profiles/24/current_config/operational_validation` | [MODEL-PROFILE-BASELINE-26](MODEL-PROFILE-BASELINE-26.md)<br>[qwen3.8-27b-exl3](qwen3.8-27b-exl3.md) | context allocation | Outcome unspecified | context_tokens=262,144 tokens | Recorded configuration/job |
| [result-ff200e880e0d8dbc80d4](../observations.json)<br>source-ab89fca7e0f49696d5258b56.json<br>`/profiles/24/current_config` | [MODEL-PROFILE-BASELINE-26](MODEL-PROFILE-BASELINE-26.md)<br>[qwen3.8-27b-exl3](qwen3.8-27b-exl3.md) | context allocation | Outcome unspecified | cache_tokens=917,504 tokens; context=262,144 tokens; reserve_mib=4,096 MiB | Recorded configuration/job |

These are saved result records, including failures and bounded checks. Copies, individual requests, report summaries and regrading can overlap; their counts are not independent test repetitions. Open each result for exact values, units, configuration binding and source receipts.

[Full archive](../../README.md) | [All retained waves](../RESULTS.md) | [Data definitions](../DATA.md) | [Recommended recipes](../../../README.md)
