# deepseek-v41-flash-validation-mm1280

**Historical record. Additional test results; no matched decode wave.**

Model family: DeepSeek.

Recorded archive reason: Fit, pilot or control configuration; measured serving variants have separate records.

Historical configurations are provided for comparison. The [recommended recipes](../../../README.md) include supported launch scripts.

Current recipes using the same recorded checkpoint repository: [deepseek-v41-flash-dspark5-tp3](../../../recipes/deepseek-v41-flash-dspark5-tp3/README.md). Context, cache and runtime versions can differ.

## Saved Configuration Versions

Each configuration ID identifies a distinct original settings record. Deployment fields are omitted; versions can have identical published settings after that omission. Upstream runtime commits remain unspecified where the source retained only an integration label.

| Configuration | Recorded artifact / source | Configured card counts | Context tokens | GPU pool tokens | Slots | Draft mode / tokens |
| --- | --- | --- | --- | --- | --- | --- |
| cfg-654dea29c57c3c2ce909 | [sfxnz/DeepSeek-V4.1-Flash-EXL3@982b70452f](https://huggingface.co/sfxnz/DeepSeek-V4.1-Flash-EXL3/tree/982b70452f399814f56b46272fd30394ae10d58c) | 3 | 32,768 | Not recorded | 4 | dspark / 5 |

Card counts are saved configuration choices, not a claim that every allowed placement was measured. A derived view can differ from its pinned download source.

<details>
<summary>cfg-654dea29c57c3c2ce909</summary>

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

## Additional Test Results

| Result / Source | Profile | Evidence type | Reported outcome | Retained values | Configuration binding |
| --- | --- | --- | --- | --- | --- |
| [result-019e8115037128a1fc86](../observations.json)<br>source-1428fe7625701752cc6141c0.json<br>`/raw_history` | [deepseek-v41-flash-validation-mm1280](deepseek-v41-flash-validation-mm1280.md) | test outcome | failed | See exact JSON for retained flags and timers | Recorded configuration/job |
| [result-12a79750f08d511a3ea2](../observations.json)<br>source-611f5664cc895d382c670a9b.json<br>`/history` | [deepseek-v41-flash-validation-mm1280](deepseek-v41-flash-validation-mm1280.md) | test outcome | failed | See exact JSON for retained flags and timers | Recorded configuration/job |
| [result-43e07f7875f9e7867113](../observations.json)<br>source-ea39bbf011f8f94f94fc5902.json<br>`/history` | [deepseek-v41-flash-validation-mm1280](deepseek-v41-flash-validation-mm1280.md) | test outcome | failed | See exact JSON for retained flags and timers | Recorded configuration/job |
| [result-6acd196ee2f7478a6e4e](../observations.json)<br>source-c3a321cb2bbaee481008d2a1.json<br>`/history` | [deepseek-v41-flash-validation-mm1280](deepseek-v41-flash-validation-mm1280.md) | test outcome | failed | See exact JSON for retained flags and timers | Recorded configuration/job |
| [result-6eff08527174888b4a6b](../observations.json)<br>source-8f12531824e933188cf78718.json<br>`/history` | [deepseek-v41-flash-validation-mm1280](deepseek-v41-flash-validation-mm1280.md) | test outcome | failed | See exact JSON for retained flags and timers | Recorded configuration/job |
| [result-74fc790b8308918466e9](../observations.json)<br>source-c3a321cb2bbaee481008d2a1.json<br>`/` | [deepseek-v41-flash-validation-mm1280](deepseek-v41-flash-validation-mm1280.md) | test outcome | failed | See exact JSON for retained flags and timers | Recorded configuration/job |
| [result-7728b52cf163edf3c7dc](../observations.json)<br>source-c5c6a0b3e31a6764811a5e2c.json<br>`/history` | [deepseek-v41-flash-validation-mm1280](deepseek-v41-flash-validation-mm1280.md) | test outcome | failed | See exact JSON for retained flags and timers | Recorded configuration/job |
| [result-78fca22cba16484558d0](../observations.json)<br>source-8f12531824e933188cf78718.json<br>`/` | [deepseek-v41-flash-validation-mm1280](deepseek-v41-flash-validation-mm1280.md) | test outcome | failed | See exact JSON for retained flags and timers | Recorded configuration/job |
| [result-d15cfe94536a41d7ce15](../observations.json)<br>source-322eed4e66502df4c3aef455.json<br>`/history` | [deepseek-v41-flash-validation-mm1280](deepseek-v41-flash-validation-mm1280.md) | test outcome | failed | See exact JSON for retained flags and timers | Recorded configuration/job |
| [result-ffbe77f00d3147bb0874](../observations.json)<br>source-07cb1d3ed0d99d482468f911.json<br>`/` | [deepseek-v41-flash-validation-mm1280](deepseek-v41-flash-validation-mm1280.md) | test outcome | failed | See exact JSON for retained flags and timers | Recorded configuration/job |

These are saved result records, including failures and bounded checks. Copies, individual requests, report summaries and regrading can overlap; their counts are not independent test repetitions. Open each result for exact values, units, configuration binding and source receipts.

There are 8 retained lifecycle records. Their states, exit codes and configuration IDs remain in [catalog.json](../catalog.json); they do not supply missing benchmark results.

[Full archive](../../README.md) | [All retained waves](../RESULTS.md) | [Data definitions](../DATA.md) | [Recommended recipes](../../../README.md)
