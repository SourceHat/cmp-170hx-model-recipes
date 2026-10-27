# apex_exl3-dflash23-small_exl3-layer_split

**Historical record. Additional test results; no matched decode wave.**

Model family: Apex Flash 1 (GLM 5.3 Flash post-train).

The campaign inventory recorded status `speed_measured_capacity_pending`. The evidence sections retain any later results separately.

Historical configurations are provided for comparison. The [recommended recipes](../../../README.md) include supported launch scripts.

Current recipes using the same recorded checkpoint repository: [apex-abliterated-exl3-mtp1-tp3](../../../recipes/apex-abliterated-exl3-mtp1-tp3/README.md). Context, cache and runtime versions can differ.

## Saved Configuration Versions

Each configuration ID identifies a distinct original settings record. Deployment fields are omitted; versions can have identical published settings after that omission. Upstream runtime commits remain unspecified where the source retained only an integration label.

| Configuration | Recorded artifact / source | Configured card counts | Context tokens | GPU pool tokens | Slots | Draft mode / tokens |
| --- | --- | --- | --- | --- | --- | --- |
| cfg-e3f8267d90ba3a74d817 | [SloptimistPrime/apex-flash-1-abliterated-EXL3-4bit-DGX-Spark@a4c922dc57](https://huggingface.co/SloptimistPrime/apex-flash-1-abliterated-EXL3-4bit-DGX-Spark/tree/a4c922dc57dae44a9569ec82a08a2f311636e2a6) | 3 | 262,144 | 262,144 | 4 | dflash2 / 3 |

Card counts are saved configuration choices, not a claim that every allowed placement was measured. A derived view can differ from its pinned download source.

<details>
<summary>cfg-e3f8267d90ba3a74d817</summary>

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
    3584
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
| [result-345789d80f6f4fda8a3d](../observations.json)<br>source-e55a92a1742e783d94e9e8c3.json<br>`/experiments/25/speed/1/backend_prefill/1` | [apex_exl3-dflash23-small_exl3-layer_split](apex_exl3-dflash23-small_exl3-layer_split.md) | test outcome | Outcome unspecified | backend_prefill_seconds=154.14 s; cached_prompt_tokens=0 tokens; prefill_tok_s=212.58 tokens/s; processed_prompt_tokens=32,767 tokens | Exact configuration unresolved |
| [result-40433d43e8eace90af04](../observations.json)<br>source-e55a92a1742e783d94e9e8c3.json<br>`/experiments/25/speed/0` | [apex_exl3-dflash23-small_exl3-layer_split](apex_exl3-dflash23-small_exl3-layer_split.md) | performance detail | Outcome unspecified | cold_TTFT_median_seconds=39.49 s; configured_slots=4 requests; output_tokens=256 tokens; p50_inter_token_ms=20.76 ms; p95_inter_token_ms=74.31 ms; prompt_tokens=32,766 tokens; Draft accepted / proposed: 167 / 267 tokens; fraction 0.6255 | Exact configuration unresolved |
| [result-431d6ed53c29b4dfc5c3](../observations.json)<br>source-a9e622d351a86c8b776605d4.json<br>`/experiments/49` | [apex_exl3-dflash23-small_exl3-layer_split](apex_exl3-dflash23-small_exl3-layer_split.md) | context allocation | Outcome unspecified | matched_workload_host_peak_bytes=63,336,652,800 bytes; per_card_peak_used_MiB_unordered=52,980.00<br>61,922.00<br>62,530.00 | Exact configuration unresolved |
| [result-92fa0bd9596d1069e877](../observations.json)<br>source-e55a92a1742e783d94e9e8c3.json<br>`/experiments/25/speed/1/backend_prefill/2` | [apex_exl3-dflash23-small_exl3-layer_split](apex_exl3-dflash23-small_exl3-layer_split.md) | test outcome | Outcome unspecified | backend_prefill_seconds=152.85 s; cached_prompt_tokens=0 tokens; prefill_tok_s=214.37 tokens/s; processed_prompt_tokens=32,767 tokens | Exact configuration unresolved |
| [result-9baec4bb3412655beb2f](../observations.json)<br>source-e55a92a1742e783d94e9e8c3.json<br>`/experiments/25/speed/1` | [apex_exl3-dflash23-small_exl3-layer_split](apex_exl3-dflash23-small_exl3-layer_split.md) | performance detail | Outcome unspecified | cold_TTFT_median_seconds=158.09 s; configured_slots=4 requests; output_tokens=256 tokens; p50_inter_token_ms=82.59 ms; p95_inter_token_ms=243.74 ms; prompt_tokens=32,767 tokens; Draft accepted / proposed: 625 / 1,197 tokens; fraction 0.5221 | Exact configuration unresolved |
| [result-9f9b6e2bd048ac6e2dae](../observations.json)<br>source-e55a92a1742e783d94e9e8c3.json<br>`/experiments/25/speed/1/backend_prefill/0` | [apex_exl3-dflash23-small_exl3-layer_split](apex_exl3-dflash23-small_exl3-layer_split.md) | test outcome | Outcome unspecified | backend_prefill_seconds=153.47 s; cached_prompt_tokens=0 tokens; prefill_tok_s=213.51 tokens/s; processed_prompt_tokens=32,767 tokens | Exact configuration unresolved |
| [result-a303ada4674e931d231f](../observations.json)<br>source-94bbce84627fe3a4ed02497f.json<br>`/` | [apex_exl3-dflash23-small_exl3-layer_split](apex_exl3-dflash23-small_exl3-layer_split.md) | correctness check | Pass | 4 response usage/timing records | Exact configuration unresolved |
| [result-b2761ebf3d9732cf54dd](../observations.json)<br>source-e55a92a1742e783d94e9e8c3.json<br>`/experiments/25/speed/0/backend_prefill/0` | [apex_exl3-dflash23-small_exl3-layer_split](apex_exl3-dflash23-small_exl3-layer_split.md) | test outcome | Outcome unspecified | backend_prefill_seconds=39.29 s; cached_prompt_tokens=0 tokens; prefill_tok_s=833.95 tokens/s; processed_prompt_tokens=32,766 tokens | Exact configuration unresolved |
| [result-d69724c09b222651a901](../observations.json)<br>source-e55a92a1742e783d94e9e8c3.json<br>`/experiments/25` | [apex_exl3-dflash23-small_exl3-layer_split](apex_exl3-dflash23-small_exl3-layer_split.md) | context allocation | Outcome unspecified | matched_workload_host_peak_bytes=63,336,652,800 bytes; per_card_peak_used_MiB_unordered=52,980.00<br>61,922.00<br>62,530.00 | Exact configuration unresolved |
| [result-d9e85eeaf2f7f54505c3](../observations.json)<br>source-e55a92a1742e783d94e9e8c3.json<br>`/experiments/25/speed/1/backend_prefill/3` | [apex_exl3-dflash23-small_exl3-layer_split](apex_exl3-dflash23-small_exl3-layer_split.md) | test outcome | Outcome unspecified | backend_prefill_seconds=152.05 s; cached_prompt_tokens=0 tokens; prefill_tok_s=215.50 tokens/s; processed_prompt_tokens=32,767 tokens | Exact configuration unresolved |

These are saved result records, including failures and bounded checks. Copies, individual requests, report summaries and regrading can overlap; their counts are not independent test repetitions. Open each result for exact values, units, configuration binding and source receipts.

[Full archive](../../README.md) | [All retained waves](../RESULTS.md) | [Data definitions](../DATA.md) | [Recommended recipes](../../../README.md)
