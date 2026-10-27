# deepseek-dspark5-tensor_parallel

**Historical record. Additional test results; no matched decode wave.**

Model family: DeepSeek.

The campaign inventory recorded status `completed`. The evidence sections retain any later results separately.

Historical configurations are provided for comparison. The [recommended recipes](../../../README.md) include supported launch scripts.

Current recipes using the same recorded checkpoint repository: [deepseek-v41-flash-dspark5-tp3](../../../recipes/deepseek-v41-flash-dspark5-tp3/README.md). Context, cache and runtime versions can differ.

## Saved Configuration Versions

Each configuration ID identifies a distinct original settings record. Deployment fields are omitted; versions can have identical published settings after that omission. Upstream runtime commits remain unspecified where the source retained only an integration label.

| Configuration | Recorded artifact / source | Configured card counts | Context tokens | GPU pool tokens | Slots | Draft mode / tokens |
| --- | --- | --- | --- | --- | --- | --- |
| cfg-00cc2a9f935a232cf6be | [sfxnz/DeepSeek-V4.1-Flash-EXL3@982b70452f](https://huggingface.co/sfxnz/DeepSeek-V4.1-Flash-EXL3/tree/982b70452f399814f56b46272fd30394ae10d58c) | 3 | 262,144 | Not recorded | 4 | dspark / 5 |

Card counts are saved configuration choices, not a claim that every allowed placement was measured. A derived view can differ from its pinned download source.

<details>
<summary>cfg-00cc2a9f935a232cf6be</summary>

```json
{
  "kind": "vllm_native",
  "gpu_counts": [
    3
  ],
  "context": 262144,
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
  "gpu_memory_utilization": 0.95,
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

## Additional Test Results

| Result / Source | Profile | Evidence type | Reported outcome | Retained values | Configuration binding |
| --- | --- | --- | --- | --- | --- |
| [result-1e534db3e70db3b6e83a](../observations.json)<br>source-e55a92a1742e783d94e9e8c3.json<br>`/experiments/26/independently_maximized_config` | [deepseek-dspark5-tensor_parallel](deepseek-dspark5-tensor_parallel.md) | test outcome | Outcome unspecified | context=524,288 tokens | Exact configuration unresolved |
| [result-306d0dd63ae4022e6ad6](../observations.json)<br>source-e55a92a1742e783d94e9e8c3.json<br>`/experiments/26/contexts/0` | [deepseek-dspark5-tensor_parallel](deepseek-dspark5-tensor_parallel.md) | context allocation | Outcome unspecified | context_tokens=524,288 tokens | Exact configuration unresolved |
| [result-48b665f3ff9356487948](../observations.json)<br>source-e55a92a1742e783d94e9e8c3.json<br>`/experiments/26` | [deepseek-dspark5-tensor_parallel](deepseek-dspark5-tensor_parallel.md) | context allocation | completed | matched_workload_host_peak_bytes=91,071,025,152 bytes; resident_pool_tokens=3,480,837 tokens; per_card_peak_used_MiB_unordered=61,852.00<br>61,852.00<br>61,854.00; capacity_boundary_measured=false; peak_prefill_and_concurrency_passed=false | Exact configuration unresolved |
| [result-ae90f7e5b965411e6748](../observations.json)<br>source-a9e622d351a86c8b776605d4.json<br>`/experiments/51` | [deepseek-dspark5-tensor_parallel](deepseek-dspark5-tensor_parallel.md) | context allocation | Outcome unspecified | matched_workload_host_peak_bytes=91,071,025,152 bytes; per_card_peak_used_MiB_unordered=61,852.00<br>61,852.00<br>61,854.00 | Exact configuration unresolved |
| [result-e168d7374eeee54467c9](../observations.json)<br>source-e55a92a1742e783d94e9e8c3.json<br>`/experiments/26/speed/1` | [deepseek-dspark5-tensor_parallel](deepseek-dspark5-tensor_parallel.md) | performance detail | Outcome unspecified | cold_TTFT_median_seconds=170.23 s; configured_slots=4 requests; output_tokens=256 tokens; p50_inter_token_ms=153.23 ms; p95_inter_token_ms=374.97 ms; prompt_tokens=32,764 tokens; Draft accepted / proposed: 663.00 / 1,820.00 tokens; fraction 0.3643 | Exact configuration unresolved |
| [result-ecfec6ed51f75fa1354f](../observations.json)<br>source-e55a92a1742e783d94e9e8c3.json<br>`/experiments/26/speed/0` | [deepseek-dspark5-tensor_parallel](deepseek-dspark5-tensor_parallel.md) | performance detail | Outcome unspecified | cold_TTFT_median_seconds=67.69 s; configured_slots=4 requests; output_tokens=256 tokens; p50_inter_token_ms=86.35 ms; p95_inter_token_ms=192.05 ms; prompt_tokens=32,764 tokens; Draft accepted / proposed: 163.00 / 465.00 tokens; fraction 0.3505 | Exact configuration unresolved |
| [result-f3d3b6f3e5b1a720a454](../observations.json)<br>source-06e65bbe238da422163343e9.json<br>`/correctness` | [deepseek-dspark5-tensor_parallel](deepseek-dspark5-tensor_parallel.md) | correctness check | Pass | 4 response usage/timing records | Exact configuration unresolved |

These are saved result records, including failures and bounded checks. Copies, individual requests, report summaries and regrading can overlap; their counts are not independent test repetitions. Open each result for exact values, units, configuration binding and source receipts.

[Full archive](../../README.md) | [All retained waves](../RESULTS.md) | [Data definitions](../DATA.md) | [Recommended recipes](../../../README.md)
