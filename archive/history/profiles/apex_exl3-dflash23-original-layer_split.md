# apex_exl3-dflash23-original-layer_split

**Historical record. Additional test results; no matched decode wave.**

Model family: Apex Flash 1 (GLM 5.3 Flash post-train).

The campaign inventory recorded status `speed_measured_capacity_pending`. The evidence sections retain any later results separately.

Historical configurations are provided for comparison. The [recommended recipes](../../../README.md) include supported launch scripts.

Current recipes using the same recorded checkpoint repository: [apex-abliterated-exl3-mtp1-tp3](../../../recipes/apex-abliterated-exl3-mtp1-tp3/README.md). Context, cache and runtime versions can differ.

## Saved Configuration Versions

Each configuration ID identifies a distinct original settings record. Deployment fields are omitted; versions can have identical published settings after that omission. Upstream runtime commits remain unspecified where the source retained only an integration label.

| Configuration | Recorded artifact / source | Configured card counts | Context tokens | GPU pool tokens | Slots | Draft mode / tokens |
| --- | --- | --- | --- | --- | --- | --- |
| cfg-d2fd380b40bbc9daf693 | [SloptimistPrime/apex-flash-1-abliterated-EXL3-4bit-DGX-Spark@a4c922dc57](https://huggingface.co/SloptimistPrime/apex-flash-1-abliterated-EXL3-4bit-DGX-Spark/tree/a4c922dc57dae44a9569ec82a08a2f311636e2a6) | 3 | 262,144 | 262,144 | 4 | dflash2 / 3 |

Card counts are saved configuration choices, not a claim that every allowed placement was measured. A derived view can differ from its pinned download source.

<details>
<summary>cfg-d2fd380b40bbc9daf693</summary>

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
  "draft_mode": "dflash2",
  "draft_tokens": 3,
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
  "parallelism": "layer_split",
  "transport": "host",
  "host_backing": "ordinary",
  "model_repository": "SloptimistPrime/apex-flash-1-abliterated-EXL3-4bit-DGX-Spark",
  "model_revision": "a4c922dc57dae44a9569ec82a08a2f311636e2a6",
  "draft_repository": null,
  "draft_revision": null,
  "recorded_runtime_label": null,
  "served_model_label": "apex-flash-1-abliterated-exl3-4bit-spark",
  "main_reserve_mib_values_unordered": [
    2048,
    2560,
    3584
  ],
  "draft_split_mib_values_unordered": [
    3328,
    4864,
    5120
  ]
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
| [result-2a6c594ccef16c79cc86](../observations.json)<br>source-e55a92a1742e783d94e9e8c3.json<br>`/experiments/24/speed/1` | [apex_exl3-dflash23-original-layer_split](apex_exl3-dflash23-original-layer_split.md) | performance detail | Outcome unspecified | cold_TTFT_median_seconds=157.34 s; configured_slots=4 requests; output_tokens=256 tokens; p50_inter_token_ms=81.54 ms; p95_inter_token_ms=246.98 ms; prompt_tokens=32,767 tokens; Draft accepted / proposed: 632 / 1,176 tokens; fraction 0.5374 | Exact configuration unresolved |
| [result-4fed4440d3d55c5bd3e1](../observations.json)<br>source-e55a92a1742e783d94e9e8c3.json<br>`/experiments/24/speed/0/backend_prefill/0` | [apex_exl3-dflash23-original-layer_split](apex_exl3-dflash23-original-layer_split.md) | test outcome | Outcome unspecified | backend_prefill_seconds=39.26 s; cached_prompt_tokens=0 tokens; prefill_tok_s=834.59 tokens/s; processed_prompt_tokens=32,766 tokens | Exact configuration unresolved |
| [result-59ab33e5e198c0fd9fe5](../observations.json)<br>source-e55a92a1742e783d94e9e8c3.json<br>`/experiments/24` | [apex_exl3-dflash23-original-layer_split](apex_exl3-dflash23-original-layer_split.md) | context allocation | Outcome unspecified | matched_workload_host_peak_bytes=64,920,465,408 bytes; per_card_peak_used_MiB_unordered=53,816.00<br>61,216.00<br>62,120.00 | Exact configuration unresolved |
| [result-5f79adcd6675ab2b7be3](../observations.json)<br>source-a9e622d351a86c8b776605d4.json<br>`/experiments/43` | [apex_exl3-dflash23-original-layer_split](apex_exl3-dflash23-original-layer_split.md) | context allocation | Outcome unspecified | matched_workload_host_peak_bytes=64,920,465,408 bytes; per_card_peak_used_MiB_unordered=53,816.00<br>61,216.00<br>62,120.00 | Exact configuration unresolved |
| [result-6368f9e329687a292f67](../observations.json)<br>source-e55a92a1742e783d94e9e8c3.json<br>`/experiments/24/speed/1/backend_prefill/0` | [apex_exl3-dflash23-original-layer_split](apex_exl3-dflash23-original-layer_split.md) | test outcome | Outcome unspecified | backend_prefill_seconds=152.26 s; cached_prompt_tokens=0 tokens; prefill_tok_s=215.20 tokens/s; processed_prompt_tokens=32,767 tokens | Exact configuration unresolved |
| [result-68c1d4c388d01206f4e6](../observations.json)<br>source-e55a92a1742e783d94e9e8c3.json<br>`/experiments/24/speed/1/backend_prefill/1` | [apex_exl3-dflash23-original-layer_split](apex_exl3-dflash23-original-layer_split.md) | test outcome | Outcome unspecified | backend_prefill_seconds=153.87 s; cached_prompt_tokens=0 tokens; prefill_tok_s=212.95 tokens/s; processed_prompt_tokens=32,767 tokens | Exact configuration unresolved |
| [result-8771c476d99a73e90e37](../observations.json)<br>source-e55a92a1742e783d94e9e8c3.json<br>`/experiments/10/speed/1/backend_prefill/1` | [apex_exl3-dflash23-original-layer_split](apex_exl3-dflash23-original-layer_split.md)<br>[glm-mtp1-original-layer_split](glm-mtp1-original-layer_split.md) | test outcome | Outcome unspecified | backend_prefill_seconds=153.07 s; cached_prompt_tokens=0 tokens; prefill_tok_s=214.07 tokens/s; processed_prompt_tokens=32,767 tokens | Exact configuration unresolved |
| [result-8b75af017640b8c34daf](../observations.json)<br>source-e55a92a1742e783d94e9e8c3.json<br>`/experiments/24/speed/0` | [apex_exl3-dflash23-original-layer_split](apex_exl3-dflash23-original-layer_split.md) | performance detail | Outcome unspecified | cold_TTFT_median_seconds=39.39 s; configured_slots=4 requests; output_tokens=256 tokens; p50_inter_token_ms=25.11 ms; p95_inter_token_ms=74.80 ms; prompt_tokens=32,766 tokens; Draft accepted / proposed: 165 / 273 tokens; fraction 0.6044 | Exact configuration unresolved |
| [result-a3c1ca90b2026d91c1a6](../observations.json)<br>source-b21b23144259fd059c0d53ff.json<br>`/` | [apex_exl3-dflash23-original-layer_split](apex_exl3-dflash23-original-layer_split.md) | correctness check | Pass | 4 response usage/timing records | Exact configuration unresolved |
| [result-dc5a24ce8965e376a0d1](../observations.json)<br>source-e55a92a1742e783d94e9e8c3.json<br>`/experiments/24/speed/1/backend_prefill/3` | [apex_exl3-dflash23-original-layer_split](apex_exl3-dflash23-original-layer_split.md) | test outcome | Outcome unspecified | backend_prefill_seconds=150.62 s; cached_prompt_tokens=0 tokens; prefill_tok_s=217.55 tokens/s; processed_prompt_tokens=32,767 tokens | Exact configuration unresolved |

These are saved result records, including failures and bounded checks. Copies, individual requests, report summaries and regrading can overlap; their counts are not independent test repetitions. Open each result for exact values, units, configuration binding and source receipts.

[Full archive](../../README.md) | [All retained waves](../RESULTS.md) | [Data definitions](../DATA.md) | [Recommended recipes](../../../README.md)
