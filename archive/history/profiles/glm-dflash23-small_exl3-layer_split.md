# glm-dflash23-small_exl3-layer_split

**Historical record. Additional test results; no matched decode wave.**

Model family: GLM 5.3 Flash.

The campaign inventory recorded status `speed_measured_capacity_pending`. The evidence sections retain any later results separately.

Historical configurations are provided for comparison. The [recommended recipes](../../../README.md) include supported launch scripts.

Current recipes using the same recorded checkpoint repository: [glm-5.3-flash-mtp1-tp3](../../../recipes/glm-5.3-flash-mtp1-tp3/README.md). Context, cache and runtime versions can differ.

## Saved Configuration Versions

Each configuration ID identifies a distinct original settings record. Deployment fields are omitted; versions can have identical published settings after that omission. Upstream runtime commits remain unspecified where the source retained only an integration label.

| Configuration | Recorded artifact / source | Configured card counts | Context tokens | GPU pool tokens | Slots | Draft mode / tokens |
| --- | --- | --- | --- | --- | --- | --- |
| cfg-b51547a2fd01366a18c9 | [turboderp/GLM-5.3-Flash-exl3@2a30229e67](https://huggingface.co/turboderp/GLM-5.3-Flash-exl3/tree/2a30229e67012798ba9f0cd832bb78abf4c363d5) | 3 | 262,144 | 262,144 | 4 | dflash2 / 3 |

Card counts are saved configuration choices, not a claim that every allowed placement was measured. A derived view can differ from its pinned download source.

<details>
<summary>cfg-b51547a2fd01366a18c9</summary>

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
| [result-35eb4ab8c2d873e9e34f](../observations.json)<br>source-e55a92a1742e783d94e9e8c3.json<br>`/experiments/19/speed/0/backend_prefill/0` | [glm-dflash23-small_exl3-layer_split](glm-dflash23-small_exl3-layer_split.md) | test outcome | Outcome unspecified | backend_prefill_seconds=38.62 s; cached_prompt_tokens=0 tokens; prefill_tok_s=848.42 tokens/s; processed_prompt_tokens=32,766 tokens | Exact configuration unresolved |
| [result-524bf21bfc8d79657ead](../observations.json)<br>source-e55a92a1742e783d94e9e8c3.json<br>`/experiments/19/speed/0` | [glm-dflash23-small_exl3-layer_split](glm-dflash23-small_exl3-layer_split.md) | performance detail | Outcome unspecified | cold_TTFT_median_seconds=38.74 s; configured_slots=4 requests; output_tokens=256 tokens; p50_inter_token_ms=19.08 ms; p95_inter_token_ms=70.88 ms; prompt_tokens=32,766 tokens; Draft accepted / proposed: 168 / 264 tokens; fraction 0.6364 | Exact configuration unresolved |
| [result-529ec91a306f760cde54](../observations.json)<br>source-e55a92a1742e783d94e9e8c3.json<br>`/experiments/19/speed/1/backend_prefill/0` | [glm-dflash23-small_exl3-layer_split](glm-dflash23-small_exl3-layer_split.md) | test outcome | Outcome unspecified | backend_prefill_seconds=152.32 s; cached_prompt_tokens=0 tokens; prefill_tok_s=215.12 tokens/s; processed_prompt_tokens=32,767 tokens | Exact configuration unresolved |
| [result-7fa426c3af45dcaf3858](../observations.json)<br>source-147867fab799ee4423c2c55b.json<br>`/` | [glm-dflash23-small_exl3-layer_split](glm-dflash23-small_exl3-layer_split.md) | correctness check | Pass | 4 response usage/timing records; matched_greedy_target_reference=false | Exact configuration unresolved |
| [result-8945b159d9171a7adbf7](../observations.json)<br>source-e55a92a1742e783d94e9e8c3.json<br>`/experiments/19/speed/1/backend_prefill/1` | [glm-dflash23-small_exl3-layer_split](glm-dflash23-small_exl3-layer_split.md) | test outcome | Outcome unspecified | backend_prefill_seconds=153.04 s; cached_prompt_tokens=0 tokens; prefill_tok_s=214.11 tokens/s; processed_prompt_tokens=32,767 tokens | Exact configuration unresolved |
| [result-8bfbabca7425c891373e](../observations.json)<br>source-a9e622d351a86c8b776605d4.json<br>`/experiments/31` | [glm-dflash23-small_exl3-layer_split](glm-dflash23-small_exl3-layer_split.md) | context allocation | Outcome unspecified | matched_workload_host_peak_bytes=69,880,909,824 bytes; per_card_peak_used_MiB_unordered=42,998.00<br>61,240.00<br>62,032.00 | Exact configuration unresolved |
| [result-8e9b6e82d94516b78cdf](../observations.json)<br>source-e55a92a1742e783d94e9e8c3.json<br>`/experiments/19/speed/1/backend_prefill/3` | [glm-dflash23-small_exl3-layer_split](glm-dflash23-small_exl3-layer_split.md) | test outcome | Outcome unspecified | backend_prefill_seconds=150.07 s; cached_prompt_tokens=0 tokens; prefill_tok_s=218.34 tokens/s; processed_prompt_tokens=32,767 tokens | Exact configuration unresolved |
| [result-94ed2a6a470135eebd54](../observations.json)<br>source-e55a92a1742e783d94e9e8c3.json<br>`/experiments/19/speed/1` | [glm-dflash23-small_exl3-layer_split](glm-dflash23-small_exl3-layer_split.md) | performance detail | Outcome unspecified | cold_TTFT_median_seconds=155.63 s; configured_slots=4 requests; output_tokens=256 tokens; p50_inter_token_ms=70.85 ms; p95_inter_token_ms=240.61 ms; prompt_tokens=32,767 tokens; Draft accepted / proposed: 660 / 1,092 tokens; fraction 0.6044 | Exact configuration unresolved |
| [result-b6ad0e6b5b4106daad6b](../observations.json)<br>source-e55a92a1742e783d94e9e8c3.json<br>`/experiments/19/speed/1/backend_prefill/2` | [glm-dflash23-small_exl3-layer_split](glm-dflash23-small_exl3-layer_split.md) | test outcome | Outcome unspecified | backend_prefill_seconds=152.30 s; cached_prompt_tokens=0 tokens; prefill_tok_s=215.15 tokens/s; processed_prompt_tokens=32,767 tokens | Exact configuration unresolved |
| [result-c11f5ffecdfa175e3713](../observations.json)<br>source-e55a92a1742e783d94e9e8c3.json<br>`/experiments/19` | [glm-dflash23-small_exl3-layer_split](glm-dflash23-small_exl3-layer_split.md) | context allocation | Outcome unspecified | matched_workload_host_peak_bytes=69,880,909,824 bytes; per_card_peak_used_MiB_unordered=42,998.00<br>61,240.00<br>62,032.00 | Exact configuration unresolved |

These are saved result records, including failures and bounded checks. Copies, individual requests, report summaries and regrading can overlap; their counts are not independent test repetitions. Open each result for exact values, units, configuration binding and source receipts.

[Full archive](../../README.md) | [All retained waves](../RESULTS.md) | [Data definitions](../DATA.md) | [Recommended recipes](../../../README.md)
