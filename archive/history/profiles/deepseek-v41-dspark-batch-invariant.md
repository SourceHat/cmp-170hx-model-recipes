# deepseek-v41-dspark-batch-invariant

**Historical record. Decode interval measured.**

Model family: DeepSeek.

Historical configurations are provided for comparison. The [recommended recipes](../../../README.md) include supported launch scripts.

Current recipes using the same recorded checkpoint repository: [deepseek-v41-flash-dspark5-tp3](../../../recipes/deepseek-v41-flash-dspark5-tp3/README.md). Context, cache and runtime versions can differ.

## Saved Configuration Versions

Each configuration ID identifies a distinct original settings record. Deployment fields are omitted; versions can have identical published settings after that omission. Upstream runtime commits remain unspecified where the source retained only an integration label.

| Configuration | Recorded artifact / source | Configured card counts | Context tokens | GPU pool tokens | Slots | Draft mode / tokens |
| --- | --- | --- | --- | --- | --- | --- |
| cfg-09ab4599a930d6764383 | [sfxnz/DeepSeek-V4.1-Flash-EXL3@982b70452f](https://huggingface.co/sfxnz/DeepSeek-V4.1-Flash-EXL3/tree/982b70452f399814f56b46272fd30394ae10d58c) | 3 | 500,000 | Not recorded | 4 | dspark / 5 |
| cfg-ef1404ed27b48d3d9e42 | [sfxnz/DeepSeek-V4.1-Flash-EXL3@982b70452f](https://huggingface.co/sfxnz/DeepSeek-V4.1-Flash-EXL3/tree/982b70452f399814f56b46272fd30394ae10d58c) | 3 | 32,768 | Not recorded | 4 | dspark / 5 |

Card counts are saved configuration choices, not a claim that every allowed placement was measured. A derived view can differ from its pinned download source.

<details>
<summary>cfg-09ab4599a930d6764383</summary>

```json
{
  "kind": "vllm_native",
  "gpu_counts": [
    3
  ],
  "context": 500000,
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
<summary>cfg-ef1404ed27b48d3d9e42</summary>

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

| Profile / Wave | Layout; Draft / Tokens | Requests | Input tokens/request | Accepted output tokens/request | Cache / Reused input tokens | Context / GPU pool tokens | Shared decode tok/s total | Client after-first-token estimate tok/s | Whole-wave output tok/s | Median TTFT, s | Source report |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [deepseek-v41-dspark-batch-invariant](deepseek-v41-dspark-batch-invariant.md)<br>wave-b7bde00e0f66c75d5ba7 | layout unspecified; dspark / 5 | 1 | Not recorded | Not recorded | unspecified; reused - | 32,768 / - | 14.10 | Not recorded | Not recorded | Not recorded | Unspecified |

Rates are whole-wave totals over the stated request count. A wave may span multiple independent model instances; [measurements.json](../measurements.json) retains their contributions and the exact configuration IDs. Do not interpret a multi-instance total as one card's rate.

A dash in shared decode means no qualified synchronized interval is available. Whole-wave throughput includes prefill and queueing. A valid decode interval can survive inside an overall failed or partial check; the source-report outcome is preserved. No rows are averaged.

## Bounded Checks

| Check | Reported outcome | Retained counts / flags |
| --- | --- | --- |
| check-fafd14487dae306ddf77 | Failed / partial | {"passed":false,"ram_restoration_qualified":false} |

These checks retain their reported scope. A context/allocation/retrieval check is not a general quality score or a speed qualification at that context. Exact flags and provenance are in [checks.json](../checks.json).

## Additional Test Results

| Result / Source | Profile | Evidence type | Reported outcome | Retained values | Configuration binding |
| --- | --- | --- | --- | --- | --- |
| [result-00d122eaa5adca9fd342](../observations.json)<br>source-049677734e09e5c0a9c64da8.json<br>`/` | [deepseek-v41-dspark-batch-invariant](deepseek-v41-dspark-batch-invariant.md) | test outcome | Failed / partial | ram_restoration_qualified=false | Recorded configuration/job |
| [result-1838f589a10494b9aff9](../observations.json)<br>source-8e1aa927bd11aeb4ea17c6c3.json<br>`/jobs/2` | [deepseek-v41-dspark-batch-invariant](deepseek-v41-dspark-batch-invariant.md) | test outcome | Failed / partial | passed=false | Recorded configuration/job |
| [result-1e555dadcbbf33672e40](../observations.json)<br>source-006df97a47d80e2e8582c1da.json<br>`/quarantine_status` | [deepseek-v41-dspark-batch-invariant](deepseek-v41-dspark-batch-invariant.md) | test outcome | Outcome unspecified | held_bytes=2,097,152 bytes | Recorded configuration/job |
| [result-78bf5c4c086bb46db5f1](../observations.json)<br>source-049677734e09e5c0a9c64da8.json<br>`/phases/4` | [deepseek-v41-dspark-batch-invariant](deepseek-v41-dspark-batch-invariant.md) | test outcome | Failed / partial | passed=false | Recorded configuration/job |
| [result-b70ad56cf746d222fb81](../observations.json)<br>source-ab89fca7e0f49696d5258b56.json<br>`/profiles/5/current_config` | [deepseek-v41-dspark-batch-invariant](deepseek-v41-dspark-batch-invariant.md) | test outcome | Outcome unspecified | context=500,000 tokens | Recorded configuration/job |

These are saved result records, including failures and bounded checks. Copies, individual requests, report summaries and regrading can overlap; their counts are not independent test repetitions. Open each result for exact values, units, configuration binding and source receipts.

There are 5 retained lifecycle records. Their states, exit codes and configuration IDs remain in [catalog.json](../catalog.json); they do not supply missing benchmark results.

[Full archive](../../README.md) | [All retained waves](../RESULTS.md) | [Data definitions](../DATA.md) | [Recommended recipes](../../../README.md)
