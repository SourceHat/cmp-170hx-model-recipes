# glm-dflash21-small_exl3-layer_split

**Historical record. Additional test results; no matched decode wave.**

Model family: GLM 5.3 Flash.

The campaign inventory recorded status `speed_measured_capacity_pending`. The evidence sections retain any later results separately.

Historical configurations are provided for comparison. The [recommended recipes](../../../README.md) include supported launch scripts.

Current recipes using the same recorded checkpoint repository: [glm-5.3-flash-mtp1-tp3](../../../recipes/glm-5.3-flash-mtp1-tp3/README.md). Context, cache and runtime versions can differ.

## Saved Configuration Versions

Each configuration ID identifies a distinct original settings record. Deployment fields are omitted; versions can have identical published settings after that omission. Upstream runtime commits remain unspecified where the source retained only an integration label.

| Configuration | Recorded artifact / source | Configured card counts | Context tokens | GPU pool tokens | Slots | Draft mode / tokens |
| --- | --- | --- | --- | --- | --- | --- |
| cfg-03b3367e9591b013b7ff | [turboderp/GLM-5.3-Flash-exl3@2a30229e67](https://huggingface.co/turboderp/GLM-5.3-Flash-exl3/tree/2a30229e67012798ba9f0cd832bb78abf4c363d5) | 3 | 262,144 | 262,144 | 4 | dflash2 / 1 |

Card counts are saved configuration choices, not a claim that every allowed placement was measured. A derived view can differ from its pinned download source.

<details>
<summary>cfg-03b3367e9591b013b7ff</summary>

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
  "parallelism": "layer_split",
  "transport": "host",
  "host_backing": "ordinary",
  "model_repository": "turboderp/GLM-5.3-Flash-exl3",
  "model_revision": "2a30229e67012798ba9f0cd832bb78abf4c363d5",
  "draft_repository": null,
  "draft_revision": null,
  "recorded_runtime_label": null,
  "served_model_label": "glm-5.3-flash",
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
| [result-11e50d2e845dbc434439](../observations.json)<br>source-a9e622d351a86c8b776605d4.json<br>`/experiments/27` | [glm-dflash21-small_exl3-layer_split](glm-dflash21-small_exl3-layer_split.md) | context allocation | Outcome unspecified | matched_workload_host_peak_bytes=69,921,832,960 bytes; per_card_peak_used_MiB_unordered=42,740.00<br>60,846.00<br>61,546.00 | Exact configuration unresolved |
| [result-18a31738b9c10abafb4a](../observations.json)<br>source-7de7e3b053e9644d16ceb09f.json<br>`/` | [glm-dflash21-small_exl3-layer_split](glm-dflash21-small_exl3-layer_split.md) | correctness check | Pass | 4 response usage/timing records; matched_greedy_target_reference=false | Exact configuration unresolved |
| [result-2a0cc5d503384b4bd5ca](../observations.json)<br>source-e55a92a1742e783d94e9e8c3.json<br>`/experiments/17/speed/0/backend_prefill/0` | [glm-dflash21-small_exl3-layer_split](glm-dflash21-small_exl3-layer_split.md) | test outcome | Outcome unspecified | backend_prefill_seconds=38.58 s; cached_prompt_tokens=0 tokens; prefill_tok_s=849.30 tokens/s; processed_prompt_tokens=32,766 tokens | Exact configuration unresolved |
| [result-5ebc241a62f078850413](../observations.json)<br>source-e55a92a1742e783d94e9e8c3.json<br>`/experiments/17/speed/1/backend_prefill/1` | [glm-dflash21-small_exl3-layer_split](glm-dflash21-small_exl3-layer_split.md) | test outcome | Outcome unspecified | backend_prefill_seconds=152.20 s; cached_prompt_tokens=0 tokens; prefill_tok_s=215.29 tokens/s; processed_prompt_tokens=32,767 tokens | Exact configuration unresolved |
| [result-68e5f41a86b63fb9ee2e](../observations.json)<br>source-e55a92a1742e783d94e9e8c3.json<br>`/experiments/17/speed/1/backend_prefill/2` | [glm-dflash21-small_exl3-layer_split](glm-dflash21-small_exl3-layer_split.md) | test outcome | Outcome unspecified | backend_prefill_seconds=151.47 s; cached_prompt_tokens=0 tokens; prefill_tok_s=216.33 tokens/s; processed_prompt_tokens=32,767 tokens | Exact configuration unresolved |
| [result-6f1b111052583e959263](../observations.json)<br>source-e55a92a1742e783d94e9e8c3.json<br>`/experiments/17/speed/0` | [glm-dflash21-small_exl3-layer_split](glm-dflash21-small_exl3-layer_split.md) | performance detail | Outcome unspecified | cold_TTFT_median_seconds=38.74 s; configured_slots=4 requests; output_tokens=256 tokens; p50_inter_token_ms=28.17 ms; p95_inter_token_ms=56.31 ms; prompt_tokens=32,766 tokens; Draft accepted / proposed: 113 / 143 tokens; fraction 0.7902 | Exact configuration unresolved |
| [result-89213658264a7432b42b](../observations.json)<br>source-e55a92a1742e783d94e9e8c3.json<br>`/experiments/17/speed/1` | [glm-dflash21-small_exl3-layer_split](glm-dflash21-small_exl3-layer_split.md) | performance detail | Outcome unspecified | cold_TTFT_median_seconds=155.45 s; configured_slots=4 requests; output_tokens=256 tokens; p50_inter_token_ms=61.23 ms; p95_inter_token_ms=122.31 ms; prompt_tokens=32,767 tokens; Draft accepted / proposed: 460 / 564 tokens; fraction 0.8156 | Exact configuration unresolved |
| [result-ea6fa1c9fdd3347d0a9c](../observations.json)<br>source-e55a92a1742e783d94e9e8c3.json<br>`/experiments/17/speed/1/backend_prefill/0` | [glm-dflash21-small_exl3-layer_split](glm-dflash21-small_exl3-layer_split.md) | test outcome | Outcome unspecified | backend_prefill_seconds=150.38 s; cached_prompt_tokens=0 tokens; prefill_tok_s=217.89 tokens/s; processed_prompt_tokens=32,767 tokens | Exact configuration unresolved |
| [result-fd9aa3db7bcaf6355022](../observations.json)<br>source-e55a92a1742e783d94e9e8c3.json<br>`/experiments/17/speed/1/backend_prefill/3` | [glm-dflash21-small_exl3-layer_split](glm-dflash21-small_exl3-layer_split.md) | test outcome | Outcome unspecified | backend_prefill_seconds=149.22 s; cached_prompt_tokens=0 tokens; prefill_tok_s=219.59 tokens/s; processed_prompt_tokens=32,767 tokens | Exact configuration unresolved |
| [result-ff54ad1a6a20a5f54330](../observations.json)<br>source-e55a92a1742e783d94e9e8c3.json<br>`/experiments/17` | [glm-dflash21-small_exl3-layer_split](glm-dflash21-small_exl3-layer_split.md) | context allocation | Outcome unspecified | matched_workload_host_peak_bytes=69,921,832,960 bytes; per_card_peak_used_MiB_unordered=42,740.00<br>60,846.00<br>61,546.00 | Exact configuration unresolved |

These are saved result records, including failures and bounded checks. Copies, individual requests, report summaries and regrading can overlap; their counts are not independent test repetitions. Open each result for exact values, units, configuration binding and source receipts.

[Full archive](../../README.md) | [All retained waves](../RESULTS.md) | [Data definitions](../DATA.md) | [Recommended recipes](../../../README.md)
