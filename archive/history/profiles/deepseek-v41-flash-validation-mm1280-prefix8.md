# deepseek-v41-flash-validation-mm1280-prefix8

**Historical record. Rate summary only.**

Model family: DeepSeek.

Historical configurations are provided for comparison. The [recommended recipes](../../../README.md) include supported launch scripts.

Current recipes using the same recorded checkpoint repository: [deepseek-v41-flash-dspark5-tp3](../../../recipes/deepseek-v41-flash-dspark5-tp3/README.md). Context, cache and runtime versions can differ.

## Saved Configuration Versions

Each configuration ID identifies a distinct original settings record. Deployment fields are omitted; versions can have identical published settings after that omission. Upstream runtime commits remain unspecified where the source retained only an integration label.

| Configuration | Recorded artifact / source | Configured card counts | Context tokens | GPU pool tokens | Slots | Draft mode / tokens |
| --- | --- | --- | --- | --- | --- | --- |
| cfg-5bf846d20e2d93254186 | [sfxnz/DeepSeek-V4.1-Flash-EXL3@982b70452f](https://huggingface.co/sfxnz/DeepSeek-V4.1-Flash-EXL3/tree/982b70452f399814f56b46272fd30394ae10d58c) | 3 | 32,768 | Not recorded | 4 | dspark / 5 |

Card counts are saved configuration choices, not a claim that every allowed placement was measured. A derived view can differ from its pinned download source.

<details>
<summary>cfg-5bf846d20e2d93254186</summary>

```json
{
  "kind": "vllm_native",
  "gpu_counts": [
    3
  ],
  "context": 32768,
  "kv_dtype": "auto",
  "draft_mode": "dspark",
  "draft_tokens": 5,
  "max_sessions": 4,
  "chunk_size": 1280,
  "ram_kv_mib": 8192,
  "power_watts": 200,
  "host_memory_gib": 80,
  "host_swap_gib": 0,
  "min_vram_mib_per_gpu": 65530,
  "min_effective_vram_mib": 196000,
  "kv_cache_mib_per_gpu": 4096,
  "engram_row_cache_mib": 64,
  "enforce_eager": true,
  "prefix_match_unit": 8,
  "model_repository": "sfxnz/DeepSeek-V4.1-Flash-EXL3",
  "model_revision": "982b70452f399814f56b46272fd30394ae10d58c",
  "draft_repository": null,
  "draft_revision": null,
  "recorded_runtime_label": "deepseek-v41-sm80-r2",
  "served_model_label": "deepseek-v4.1-flash"
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
| summary-6691e7e682ec55874478 | DSpark_single_generation_tps | 24.80 | 1 | recorded_summary_context |
| summary-c335a1aa63feb4fe4064 | DSpark_four_generation_tps | 66.09 | 4 | recorded_summary_context |

These quoted values can overlap detailed waves. A referenced earlier run's rate is not transferred to the citing configuration. Missing input, request and timing-window evidence remains missing. See [rate-summaries.json](../rate-summaries.json).

## Additional Test Results

| Result / Source | Profile | Evidence type | Reported outcome | Retained values | Configuration binding |
| --- | --- | --- | --- | --- | --- |
| [result-28f0bb938c8202d3b958](../observations.json)<br>source-b2423e05a864a7c288d22898.json<br>`/` | [deepseek-v41-flash-validation-mm1280-prefix8](deepseek-v41-flash-validation-mm1280-prefix8.md) | test outcome | failed | See exact JSON for retained flags and timers | Recorded configuration/job |
| [result-5339a7c7d4edb99634d4](../observations.json)<br>source-ab89fca7e0f49696d5258b56.json<br>`/profiles/6/current_config` | [deepseek-v41-flash-validation-mm1280-prefix8](deepseek-v41-flash-validation-mm1280-prefix8.md) | test outcome | Outcome unspecified | context=32,768 tokens | Recorded configuration/job |
| [result-7440c93ed0fcd7cb8edd](../observations.json)<br>source-18356741c70c62414df88925.json<br>`/managed_history` | [deepseek-v41-flash-validation-mm1280-prefix8](deepseek-v41-flash-validation-mm1280-prefix8.md) | test outcome | failed | See exact JSON for retained flags and timers | Recorded configuration/job |
| [result-dc9f8381af23c2e1fad0](../observations.json)<br>source-0a34ccef4f5a78922944c267.json<br>`/` | [deepseek-v41-flash-validation-mm1280-prefix8](deepseek-v41-flash-validation-mm1280-prefix8.md) | test outcome | failed | See exact JSON for retained flags and timers | Recorded configuration/job |

These are saved result records, including failures and bounded checks. Copies, individual requests, report summaries and regrading can overlap; their counts are not independent test repetitions. Open each result for exact values, units, configuration binding and source receipts.

There are 6 retained lifecycle records. Their states, exit codes and configuration IDs remain in [catalog.json](../catalog.json); they do not supply missing benchmark results.

[Full archive](../../README.md) | [All retained waves](../RESULTS.md) | [Data definitions](../DATA.md) | [Recommended recipes](../../../README.md)
