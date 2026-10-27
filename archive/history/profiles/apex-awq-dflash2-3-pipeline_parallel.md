# apex-awq-dflash2-3-pipeline_parallel

**Historical record. Additional test results; no matched decode wave.**

Model family: Apex Flash 1 (GLM 5.3 Flash post-train).

The campaign inventory recorded status `completed`. The evidence sections retain any later results separately.

Historical configurations are provided for comparison. The [recommended recipes](../../../README.md) include supported launch scripts.

Current recipes using the same recorded checkpoint repository: [apex-abliterated-awq-dflash2-pp3-balanced](../../../recipes/apex-abliterated-awq-dflash2-pp3-balanced/README.md). Context, cache and runtime versions can differ.

## Saved Configuration Versions

Each configuration ID identifies a distinct original settings record. Deployment fields are omitted; versions can have identical published settings after that omission. Upstream runtime commits remain unspecified where the source retained only an integration label.

| Configuration | Recorded artifact / source | Configured card counts | Context tokens | GPU pool tokens | Slots | Draft mode / tokens |
| --- | --- | --- | --- | --- | --- | --- |
| cfg-2db0b43fd7b5cdfeb9db | [svbmrgd/apex-flash-1-abliterated-AWQ@7ea31e3d22](https://huggingface.co/svbmrgd/apex-flash-1-abliterated-AWQ/tree/7ea31e3d22c6622c999d3de74d1569efce815943) | 3 | 262,144 | Not recorded | 4 | dflash2 / 3 |

Card counts are saved configuration choices, not a claim that every allowed placement was measured. A derived view can differ from its pinned download source.

<details>
<summary>cfg-2db0b43fd7b5cdfeb9db</summary>

```json
{
  "kind": "vllm_apex_awq",
  "gpu_counts": [
    3
  ],
  "context": 262144,
  "kv_dtype": "fp8_e4m3",
  "draft_kv_dtype": "fp8_e4m3",
  "draft_mode": "dflash2",
  "draft_tokens": 3,
  "max_sessions": 4,
  "chunk_size": 1280,
  "ram_kv_mib": 8192,
  "power_watts": 200,
  "host_memory_gib": 80,
  "host_swap_gib": 0,
  "min_vram_mib_per_gpu": 65530,
  "min_effective_vram_mib": 196000,
  "parallelism": "pipeline_parallel",
  "tensor_parallel_size": 1,
  "pipeline_parallel_size": 3,
  "pipeline_layer_partition": [
    17,
    14,
    14
  ],
  "enforce_eager": true,
  "gpu_memory_utilization": 0.95,
  "transport": "host",
  "model_repository": "svbmrgd/apex-flash-1-abliterated-AWQ",
  "model_revision": "7ea31e3d22c6622c999d3de74d1569efce815943",
  "draft_repository": "incoai/GLM-5.3-Flash-DFlash2",
  "draft_revision": "bf582e4eacc1810f76656d1811693ff6c6737d2a",
  "recorded_runtime_label": "apex-awq-nope8-campaign-f",
  "served_model_label": "apex-flash-1-abliterated-awq",
  "draft_directory_template": "@DRAFT_ROOT@"
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
| [result-157eac8817c36366bcb8](../observations.json)<br>source-0a803908d68fc99fde3b2c65.json<br>`/` | [apex-awq-dflash2-3-pipeline_parallel](apex-awq-dflash2-3-pipeline_parallel.md) | correctness check | Failed / partial | 4 response usage/timing records; complete_checked_answers=false; matched_checked_target_answers=false; matched_greedy_target_reference=false | Exact configuration unresolved |
| [result-28985473fce622b34337](../observations.json)<br>source-9ccab0492e1ed10f4f94399f.json<br>`/` | [apex-awq-dflash2-3-pipeline_parallel](apex-awq-dflash2-3-pipeline_parallel.md) | correctness check | Failed / partial | 4 response usage/timing records; complete_checked_answers=false; matched_checked_target_answers=false; matched_greedy_target_reference=false | Exact configuration unresolved |
| [result-3b6568451e0ff99c4d1f](../observations.json)<br>source-e55a92a1742e783d94e9e8c3.json<br>`/experiments/27/speed/0` | [apex-awq-dflash2-3-pipeline_parallel](apex-awq-dflash2-3-pipeline_parallel.md) | performance detail | Outcome unspecified | cold_TTFT_median_seconds=36.04 s; configured_slots=4 requests; output_tokens=256 tokens; p50_inter_token_ms=17.78 ms; p95_inter_token_ms=54.45 ms; prompt_tokens=32,765 tokens; Draft accepted / proposed: 167.00 / 267.00 tokens; fraction 0.6255 | Exact configuration unresolved |
| [result-4b74ccb57d785fad6920](../observations.json)<br>source-a9e622d351a86c8b776605d4.json<br>`/experiments/54` | [apex-awq-dflash2-3-pipeline_parallel](apex-awq-dflash2-3-pipeline_parallel.md) | test outcome | Error recorded | See exact JSON for retained flags and timers | Exact configuration unresolved |
| [result-7af5a5f41a506bdfa623](../observations.json)<br>source-e55a92a1742e783d94e9e8c3.json<br>`/experiments/27/speed/1` | [apex-awq-dflash2-3-pipeline_parallel](apex-awq-dflash2-3-pipeline_parallel.md) | performance detail | Outcome unspecified | cold_TTFT_median_seconds=82.55 s; configured_slots=4 requests; output_tokens=256 tokens; p50_inter_token_ms=31.29 ms; p95_inter_token_ms=92.11 ms; prompt_tokens=32,766 tokens; Draft accepted / proposed: 638.00 / 1,164.00 tokens; fraction 0.5481 | Exact configuration unresolved |
| [result-938b23e590c805c1875f](../observations.json)<br>source-95ecc4554973170d19c9fea6.json<br>`/` | [apex-awq-dflash2-3-pipeline_parallel](apex-awq-dflash2-3-pipeline_parallel.md) | correctness check | Failed / partial | 4 response usage/timing records; complete_checked_answers=false; matched_checked_target_answers=false; matched_greedy_target_reference=false | Exact configuration unresolved |
| [result-c2e661add27135b9d0eb](../observations.json)<br>source-e55a92a1742e783d94e9e8c3.json<br>`/experiments/27` | [apex-awq-dflash2-3-pipeline_parallel](apex-awq-dflash2-3-pipeline_parallel.md) | context allocation | completed | matched_workload_host_peak_bytes=78,066,114,560 bytes; resident_pool_tokens=826,524 tokens; per_card_peak_used_MiB_unordered=64,648.00<br>64,656.00<br>64,657.00; capacity_boundary_measured=false; peak_prefill_and_concurrency_passed=false | Exact configuration unresolved |
| [result-c39a731afb689258027c](../observations.json)<br>source-e55a92a1742e783d94e9e8c3.json<br>`/experiments/27/contexts/0` | [apex-awq-dflash2-3-pipeline_parallel](apex-awq-dflash2-3-pipeline_parallel.md) | context allocation | Outcome unspecified | context_tokens=524,288 tokens | Exact configuration unresolved |
| [result-d514275a8e04c0add8e8](../observations.json)<br>source-b15d8fb978f8ef80623bcbc1.json<br>`/correctness` | [apex-awq-dflash2-3-pipeline_parallel](apex-awq-dflash2-3-pipeline_parallel.md) | correctness check | Pass | 4 response usage/timing records | Exact configuration unresolved |
| [result-ef414fbc030c2b0e723c](../observations.json)<br>source-e55a92a1742e783d94e9e8c3.json<br>`/experiments/27/independently_maximized_config` | [apex-awq-dflash2-3-pipeline_parallel](apex-awq-dflash2-3-pipeline_parallel.md) | test outcome | Outcome unspecified | context=524,288 tokens | Exact configuration unresolved |

These are saved result records, including failures and bounded checks. Copies, individual requests, report summaries and regrading can overlap; their counts are not independent test repetitions. Open each result for exact values, units, configuration binding and source receipts.

[Full archive](../../README.md) | [All retained waves](../RESULTS.md) | [Data definitions](../DATA.md) | [Recommended recipes](../../../README.md)
