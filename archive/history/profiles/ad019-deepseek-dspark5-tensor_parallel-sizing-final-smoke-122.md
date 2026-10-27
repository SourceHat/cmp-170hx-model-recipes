# ad019-deepseek-dspark5-tensor_parallel-sizing-final-smoke-122

**Historical record. Bounded checks only.**

Model family: DeepSeek.

Historical configurations are provided for comparison. The [recommended recipes](../../../README.md) include supported launch scripts.

Current recipes using the same recorded checkpoint repository: [deepseek-v41-flash-dspark5-tp3](../../../recipes/deepseek-v41-flash-dspark5-tp3/README.md). Context, cache and runtime versions can differ.

## Saved Configuration Versions

Each configuration ID identifies a distinct original settings record. Deployment fields are omitted; versions can have identical published settings after that omission. Upstream runtime commits remain unspecified where the source retained only an integration label.

| Configuration | Recorded artifact / source | Configured card counts | Context tokens | GPU pool tokens | Slots | Draft mode / tokens |
| --- | --- | --- | --- | --- | --- | --- |
| cfg-8fee0e4530faf1a30c5f | [sfxnz/DeepSeek-V4.1-Flash-EXL3@982b70452f](https://huggingface.co/sfxnz/DeepSeek-V4.1-Flash-EXL3/tree/982b70452f399814f56b46272fd30394ae10d58c) | 3 | 524,288 | Not recorded | 4 | dspark / 5 |

Card counts are saved configuration choices, not a claim that every allowed placement was measured. A derived view can differ from its pinned download source.

<details>
<summary>cfg-8fee0e4530faf1a30c5f</summary>

```json
{
  "kind": "vllm_native",
  "gpu_counts": [
    3
  ],
  "context": 524288,
  "kv_dtype": "fp8",
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
  "parallelism": "tensor_parallel",
  "engram_row_cache_mib": 64,
  "enforce_eager": true,
  "batch_invariant": true,
  "gpu_memory_utilization": 0.98391,
  "prefix_match_unit": 8,
  "transport": "host",
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
| check-ba9915a8cf7869d37567 | Pass | {"passed":true,"configured_slots":4,"context_tokens":524288} |
| check-f10d3bb978d6dfe42a29 | Pass | {"passed":true,"configured_slots":4,"context_tokens":524288} |

These checks retain their reported scope. A context/allocation/retrieval check is not a general quality score or a speed qualification at that context. Exact flags and provenance are in [checks.json](../checks.json).

## Additional Test Results

| Result / Source | Profile | Evidence type | Reported outcome | Retained values | Configuration binding |
| --- | --- | --- | --- | --- | --- |
| [result-2929d99ed912811ccf2c](../observations.json)<br>source-e55a92a1742e783d94e9e8c3.json<br>`/final_allocations/4` | [ad019-deepseek-dspark5-tensor_parallel-sizing-final-smoke-122](ad019-deepseek-dspark5-tensor_parallel-sizing-final-smoke-122.md)<br>[deepseek-dspark5-tensor_parallel](deepseek-dspark5-tensor_parallel.md) | context allocation | Outcome unspecified | actual_input_tokens=522,259 tokens; configured_slots=4 requests; context_limit=524,288 tokens; host_peak_bytes=84,707,561,472 bytes; resident_pool_tokens=3,480,837 tokens; per_card_peak_used_MiB_unordered=64,334.00<br>64,334.00<br>64,336.00; exact_boundary_measured=false | Recorded configuration/job |
| [result-93d4f8ca425efd9200d9](../observations.json)<br>source-06e65bbe238da422163343e9.json<br>`/capacity/trials/1/peak_prefill` | [ad019-deepseek-dspark5-tensor_parallel-sizing-final-smoke-122](ad019-deepseek-dspark5-tensor_parallel-sizing-final-smoke-122.md)<br>[deepseek-dspark5-tensor_parallel](deepseek-dspark5-tensor_parallel.md) | context allocation | Pass | configured_slots=4 requests; context_tokens=524,288 tokens | Recorded configuration/job |

These are saved result records, including failures and bounded checks. Copies, individual requests, report summaries and regrading can overlap; their counts are not independent test repetitions. Open each result for exact values, units, configuration binding and source receipts.

There are 1 retained lifecycle records. Their states, exit codes and configuration IDs remain in [catalog.json](../catalog.json); they do not supply missing benchmark results.

[Full archive](../../README.md) | [All retained waves](../RESULTS.md) | [Data definitions](../DATA.md) | [Recommended recipes](../../../README.md)
