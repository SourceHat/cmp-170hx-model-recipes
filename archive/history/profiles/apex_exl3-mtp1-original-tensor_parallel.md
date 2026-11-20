# apex_exl3-mtp1-original-tensor_parallel

**Historical record. Additional test results; no matched decode wave.**

Model family: Apex Flash 1 (GLM 5.3 Flash post-train).

The campaign inventory recorded status `completed`. The evidence sections retain any later results separately.

Historical configurations are provided for comparison. The [recommended recipes](../../../README.md) include supported launch scripts.

Current recipes using the same recorded checkpoint repository: [apex-abliterated-exl3-mtp1-tp3](../../../recipes/apex-abliterated-exl3-mtp1-tp3/README.md). Context, cache and runtime versions can differ.

## Saved Configuration Versions

Each configuration ID identifies a distinct original settings record. Deployment fields are omitted; versions can have identical published settings after that omission. Upstream runtime commits remain unspecified where the source retained only an integration label.

| Configuration | Recorded artifact / source | Configured card counts | Context tokens | GPU pool tokens | Slots | Draft mode / tokens |
| --- | --- | --- | --- | --- | --- | --- |
| cfg-a89b98a3a3f6379769fd | [SloptimistPrime/apex-flash-1-abliterated-EXL3-4bit-DGX-Spark@a4c922dc57](https://huggingface.co/SloptimistPrime/apex-flash-1-abliterated-EXL3-4bit-DGX-Spark/tree/a4c922dc57dae44a9569ec82a08a2f311636e2a6) | 3 | 262,144 | 262,144 | 4 | mtp / 1 |

Card counts are saved configuration choices, not a claim that every allowed placement was measured. A derived view can differ from its pinned download source.

<details>
<summary>cfg-a89b98a3a3f6379769fd</summary>

```json
{
  "kind": "tabby",
  "gpu_counts": [
    3
  ],
  "context": 262144,
  "cache_tokens": 262144,
  "cache_mode": "Q8",
  "draft_cache_mode": "Q8",
  "draft_mode": "mtp",
  "draft_tokens": 1,
  "max_sessions": 4,
  "chunk_size": 512,
  "reserve_mib": 2048,
  "ram_kv_mib": 8192,
  "ram_recurrent_mib": 16384,
  "dynamic_draft": false,
  "output_chunk_tokens": 4096,
  "power_watts": 200,
  "host_memory_gib": 80,
  "host_swap_gib": 0,
  "min_vram_mib_per_gpu": 65530,
  "min_effective_vram_mib": 196590,
  "parallelism": "tensor_parallel",
  "transport": "host",
  "host_backing": "ordinary",
  "model_repository": "SloptimistPrime/apex-flash-1-abliterated-EXL3-4bit-DGX-Spark",
  "model_revision": "a4c922dc57dae44a9569ec82a08a2f311636e2a6",
  "draft_repository": null,
  "draft_revision": null,
  "recorded_runtime_label": null,
  "served_model_label": "apex-flash-1-abliterated-exl3-4bit-spark"
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
| [result-10871417c5f4c0d808ad](../observations.json)<br>source-e55a92a1742e783d94e9e8c3.json<br>`/experiments/21/speed/1/backend_prefill/2` | [apex_exl3-mtp1-original-tensor_parallel](apex_exl3-mtp1-original-tensor_parallel.md) | test outcome | Outcome unspecified | backend_prefill_seconds=195.51 s; cached_prompt_tokens=0 tokens; prefill_tok_s=167.60 tokens/s; processed_prompt_tokens=32,767 tokens | Exact configuration unresolved |
| [result-2b1d49646bd6ba731b2f](../observations.json)<br>source-e55a92a1742e783d94e9e8c3.json<br>`/experiments/21/speed/0/backend_prefill/0` | [apex_exl3-mtp1-original-tensor_parallel](apex_exl3-mtp1-original-tensor_parallel.md) | test outcome | Outcome unspecified | backend_prefill_seconds=51.08 s; cached_prompt_tokens=0 tokens; prefill_tok_s=641.46 tokens/s; processed_prompt_tokens=32,766 tokens | Exact configuration unresolved |
| [result-2c18fbe26a55b1e43b46](../observations.json)<br>source-e55a92a1742e783d94e9e8c3.json<br>`/experiments/21/speed/1/backend_prefill/0` | [apex_exl3-mtp1-original-tensor_parallel](apex_exl3-mtp1-original-tensor_parallel.md) | test outcome | Outcome unspecified | backend_prefill_seconds=194.34 s; cached_prompt_tokens=0 tokens; prefill_tok_s=168.61 tokens/s; processed_prompt_tokens=32,767 tokens | Exact configuration unresolved |
| [result-512f1966084a4af53638](../observations.json)<br>source-e55a92a1742e783d94e9e8c3.json<br>`/experiments/21` | [apex_exl3-mtp1-original-tensor_parallel](apex_exl3-mtp1-original-tensor_parallel.md) | context allocation | completed | matched_workload_host_peak_bytes=89,089,478,656 bytes; planning_reserve_mib=2,048 MiB; resident_pool_tokens=1,083,136 tokens; per_card_peak_used_MiB_unordered=58,598.00<br>58,829.00<br>59,883.00; capacity_boundary_measured=false; peak_prefill_and_concurrency_passed=false | Exact configuration unresolved |
| [result-5814e93619ffdc361892](../observations.json)<br>source-e55a92a1742e783d94e9e8c3.json<br>`/experiments/21/contexts/0` | [apex_exl3-mtp1-original-tensor_parallel](apex_exl3-mtp1-original-tensor_parallel.md) | context allocation | Outcome unspecified | context_tokens=524,288 tokens | Exact configuration unresolved |
| [result-5ec06fd65c23c96174f3](../observations.json)<br>source-e55a92a1742e783d94e9e8c3.json<br>`/experiments/21/speed/1/backend_prefill/1` | [apex_exl3-mtp1-original-tensor_parallel](apex_exl3-mtp1-original-tensor_parallel.md) | test outcome | Outcome unspecified | backend_prefill_seconds=197.01 s; cached_prompt_tokens=0 tokens; prefill_tok_s=166.32 tokens/s; processed_prompt_tokens=32,767 tokens | Exact configuration unresolved |
| [result-8bb7225b04de11d50d37](../observations.json)<br>source-e55a92a1742e783d94e9e8c3.json<br>`/experiments/21/speed/0` | [apex_exl3-mtp1-original-tensor_parallel](apex_exl3-mtp1-original-tensor_parallel.md) | performance detail | Outcome unspecified | cold_TTFT_median_seconds=51.17 s; configured_slots=4 requests; output_tokens=256 tokens; p50_inter_token_ms=21.22 ms; p95_inter_token_ms=40.72 ms; prompt_tokens=32,766 tokens; Draft accepted / proposed: 118 / 138 tokens; fraction 0.8551 | Exact configuration unresolved |
| [result-98f2d31810c419740b33](../observations.json)<br>source-e55a92a1742e783d94e9e8c3.json<br>`/experiments/21/speed/1` | [apex_exl3-mtp1-original-tensor_parallel](apex_exl3-mtp1-original-tensor_parallel.md) | performance detail | Outcome unspecified | cold_TTFT_median_seconds=200.95 s; configured_slots=4 requests; output_tokens=256 tokens; p50_inter_token_ms=37.34 ms; p95_inter_token_ms=73.81 ms; prompt_tokens=32,767 tokens; Draft accepted / proposed: 470 / 554 tokens; fraction 0.8484 | Exact configuration unresolved |
| [result-9957496869f628eaf7be](../observations.json)<br>source-e55a92a1742e783d94e9e8c3.json<br>`/experiments/21/independently_maximized_config` | [apex_exl3-mtp1-original-tensor_parallel](apex_exl3-mtp1-original-tensor_parallel.md) | context allocation | Outcome unspecified | cache_tokens=1,083,136 tokens; context=524,288 tokens; reserve_mib=2,048 MiB | Exact configuration unresolved |
| [result-a6fb12b2cd4d900fec95](../observations.json)<br>source-b5ce85b23063b71f50338af3.json<br>`/correctness` | [apex_exl3-mtp1-original-tensor_parallel](apex_exl3-mtp1-original-tensor_parallel.md) | correctness check | Pass | 4 response usage/timing records | Exact configuration unresolved |
| [result-a80453af42f86e628e36](../observations.json)<br>source-e55a92a1742e783d94e9e8c3.json<br>`/experiments/21/speed/1/backend_prefill/3` | [apex_exl3-mtp1-original-tensor_parallel](apex_exl3-mtp1-original-tensor_parallel.md) | test outcome | Outcome unspecified | backend_prefill_seconds=194.69 s; cached_prompt_tokens=0 tokens; prefill_tok_s=168.30 tokens/s; processed_prompt_tokens=32,767 tokens | Exact configuration unresolved |
| [result-c437fca72db67d6ab89a](../observations.json)<br>source-a9e622d351a86c8b776605d4.json<br>`/experiments/34` | [apex_exl3-mtp1-original-tensor_parallel](apex_exl3-mtp1-original-tensor_parallel.md) | context allocation | Outcome unspecified | matched_workload_host_peak_bytes=89,089,478,656 bytes; per_card_peak_used_MiB_unordered=58,598.00<br>58,829.00<br>59,883.00 | Exact configuration unresolved |

These are saved result records, including failures and bounded checks. Copies, individual requests, report summaries and regrading can overlap; their counts are not independent test repetitions. Open each result for exact values, units, configuration binding and source receipts.

[Full archive](../../README.md) | [All retained waves](../RESULTS.md) | [Data definitions](../DATA.md) | [Recommended recipes](../../../README.md)
