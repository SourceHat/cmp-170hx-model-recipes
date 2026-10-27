# deepseek-v41-ordinary-control-batch-invariant

**Historical record. Bounded checks only.**

Model family: DeepSeek.

Recorded archive reason: Ordinary comparison control; DSpark retained.

Historical configurations are provided for comparison. The [recommended recipes](../../../README.md) include supported launch scripts.

Current recipes using the same recorded checkpoint repository: [deepseek-v41-flash-dspark5-tp3](../../../recipes/deepseek-v41-flash-dspark5-tp3/README.md). Context, cache and runtime versions can differ.

## Saved Configuration Versions

Each configuration ID identifies a distinct original settings record. Deployment fields are omitted; versions can have identical published settings after that omission. Upstream runtime commits remain unspecified where the source retained only an integration label.

| Configuration | Recorded artifact / source | Configured card counts | Context tokens | GPU pool tokens | Slots | Draft mode / tokens |
| --- | --- | --- | --- | --- | --- | --- |
| cfg-920905bbb20af91aded1 | [sfxnz/DeepSeek-V4.1-Flash-EXL3@982b70452f](https://huggingface.co/sfxnz/DeepSeek-V4.1-Flash-EXL3/tree/982b70452f399814f56b46272fd30394ae10d58c) | 3 | 32,768 | Not recorded | 4 | disabled / 5 |
| cfg-b555cebab553806248b0 | [sfxnz/DeepSeek-V4.1-Flash-EXL3@982b70452f](https://huggingface.co/sfxnz/DeepSeek-V4.1-Flash-EXL3/tree/982b70452f399814f56b46272fd30394ae10d58c) | 3 | 500,000 | Not recorded | 4 | disabled / 5 |

Card counts are saved configuration choices, not a claim that every allowed placement was measured. A derived view can differ from its pinned download source.

<details>
<summary>cfg-920905bbb20af91aded1</summary>

```json
{
  "kind": "vllm_native",
  "gpu_counts": [
    3
  ],
  "context": 32768,
  "kv_dtype": "auto",
  "draft_mode": "disabled",
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
  "batch_invariant": true,
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

<details>
<summary>cfg-b555cebab553806248b0</summary>

```json
{
  "kind": "vllm_native",
  "gpu_counts": [
    3
  ],
  "context": 500000,
  "kv_dtype": "auto",
  "draft_mode": "disabled",
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
  "batch_invariant": true,
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

## Bounded Checks

| Check | Reported outcome | Retained counts / flags |
| --- | --- | --- |
| check-a250e9e9af29b05f506c | Failed / partial | {"passed":false,"ram_restoration_qualified":false} |

These checks retain their reported scope. A context/allocation/retrieval check is not a general quality score or a speed qualification at that context. Exact flags and provenance are in [checks.json](../checks.json).

## Additional Test Results

| Result / Source | Profile | Evidence type | Reported outcome | Retained values | Configuration binding |
| --- | --- | --- | --- | --- | --- |
| [result-21f7b8100951152e3155](../observations.json)<br>source-39578503da828bbf6ed8eb8f.json<br>`/phases/4` | [deepseek-v41-ordinary-control-batch-invariant](deepseek-v41-ordinary-control-batch-invariant.md) | test outcome | Failed / partial | passed=false | Recorded configuration/job |
| [result-462aa5dcacd70a1f2f0f](../observations.json)<br>source-e7febe73e2e59145369cf778.json<br>`/quarantine_status` | [deepseek-v41-ordinary-control-batch-invariant](deepseek-v41-ordinary-control-batch-invariant.md) | test outcome | Outcome unspecified | held_bytes=2,097,152 bytes | Recorded configuration/job |
| [result-4f08c33992c07a827ccd](../observations.json)<br>source-8e1aa927bd11aeb4ea17c6c3.json<br>`/jobs/1` | [deepseek-v41-ordinary-control-batch-invariant](deepseek-v41-ordinary-control-batch-invariant.md) | test outcome | Failed / partial | passed=false | Recorded configuration/job |
| [result-5ff8a4e6205ab50249bb](../observations.json)<br>source-0c82bf1bbdb109f07bc19c05.json<br>`/quarantine_status` | [deepseek-v41-ordinary-control-batch-invariant](deepseek-v41-ordinary-control-batch-invariant.md) | test outcome | Outcome unspecified | held_bytes=2,097,152 bytes | Recorded configuration/job |
| [result-6384d8a374444214e601](../observations.json)<br>source-39578503da828bbf6ed8eb8f.json<br>`/` | [deepseek-v41-ordinary-control-batch-invariant](deepseek-v41-ordinary-control-batch-invariant.md) | test outcome | Failed / partial | ram_restoration_qualified=false | Recorded configuration/job |
| [result-68bec780ec316fd24254](../observations.json)<br>source-e7febe73e2e59145369cf778.json<br>`/` | [deepseek-v41-ordinary-control-batch-invariant](deepseek-v41-ordinary-control-batch-invariant.md) | test outcome | Error recorded | See exact JSON for retained flags and timers | Recorded configuration/job |

These are saved result records, including failures and bounded checks. Copies, individual requests, report summaries and regrading can overlap; their counts are not independent test repetitions. Open each result for exact values, units, configuration binding and source receipts.

There are 6 retained lifecycle records. Their states, exit codes and configuration IDs remain in [catalog.json](../catalog.json); they do not supply missing benchmark results.

[Full archive](../../README.md) | [All retained waves](../RESULTS.md) | [Data definitions](../DATA.md) | [Recommended recipes](../../../README.md)
