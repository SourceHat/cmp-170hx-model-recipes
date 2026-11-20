# glm-dflash22-small_exl3-layer_split

**Historical record. Additional test results; no matched decode wave.**

Model family: GLM 5.3 Flash.

The campaign inventory recorded status `speed_measured_capacity_pending`. The evidence sections retain any later results separately.

Historical configurations are provided for comparison. The [recommended recipes](../../../README.md) include supported launch scripts.

Current recipes using the same recorded checkpoint repository: [glm-5.3-flash-mtp1-tp3](../../../recipes/glm-5.3-flash-mtp1-tp3/README.md). Context, cache and runtime versions can differ.

## Saved Configuration Versions

Each configuration ID identifies a distinct original settings record. Deployment fields are omitted; versions can have identical published settings after that omission. Upstream runtime commits remain unspecified where the source retained only an integration label.

| Configuration | Recorded artifact / source | Configured card counts | Context tokens | GPU pool tokens | Slots | Draft mode / tokens |
| --- | --- | --- | --- | --- | --- | --- |
| cfg-b3d13f1161eb29faa5f4 | [turboderp/GLM-5.3-Flash-exl3@2a30229e67](https://huggingface.co/turboderp/GLM-5.3-Flash-exl3/tree/2a30229e67012798ba9f0cd832bb78abf4c363d5) | 3 | 262,144 | 262,144 | 4 | dflash2 / 2 |

Card counts are saved configuration choices, not a claim that every allowed placement was measured. A derived view can differ from its pinned download source.

<details>
<summary>cfg-b3d13f1161eb29faa5f4</summary>

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
  "draft_tokens": 2,
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
| [result-3cc77c0b5cec6c3e8f9d](../observations.json)<br>source-e55a92a1742e783d94e9e8c3.json<br>`/experiments/18/speed/1/backend_prefill/2` | [glm-dflash22-small_exl3-layer_split](glm-dflash22-small_exl3-layer_split.md) | test outcome | Outcome unspecified | backend_prefill_seconds=151.42 s; cached_prompt_tokens=0 tokens; prefill_tok_s=216.40 tokens/s; processed_prompt_tokens=32,767 tokens | Exact configuration unresolved |
| [result-3f10f76f6482a4ce58b3](../observations.json)<br>source-e55a92a1742e783d94e9e8c3.json<br>`/experiments/18` | [glm-dflash22-small_exl3-layer_split](glm-dflash22-small_exl3-layer_split.md) | context allocation | Outcome unspecified | matched_workload_host_peak_bytes=69,917,339,648 bytes; per_card_peak_used_MiB_unordered=42,796.00<br>61,038.00<br>61,796.00 | Exact configuration unresolved |
| [result-4263373ba9dccab575cd](../observations.json)<br>source-e55a92a1742e783d94e9e8c3.json<br>`/experiments/18/speed/1` | [glm-dflash22-small_exl3-layer_split](glm-dflash22-small_exl3-layer_split.md) | performance detail | Outcome unspecified | cold_TTFT_median_seconds=155.90 s; configured_slots=4 requests; output_tokens=256 tokens; p50_inter_token_ms=74.25 ms; p95_inter_token_ms=219.71 ms; prompt_tokens=32,767 tokens; Draft accepted / proposed: 590 / 868 tokens; fraction 0.6797 | Exact configuration unresolved |
| [result-7627681c987706ccfe19](../observations.json)<br>source-e55a92a1742e783d94e9e8c3.json<br>`/experiments/18/speed/0` | [glm-dflash22-small_exl3-layer_split](glm-dflash22-small_exl3-layer_split.md) | performance detail | Outcome unspecified | cold_TTFT_median_seconds=38.94 s; configured_slots=4 requests; output_tokens=256 tokens; p50_inter_token_ms=21.97 ms; p95_inter_token_ms=64.08 ms; prompt_tokens=32,766 tokens; Draft accepted / proposed: 150 / 212 tokens; fraction 0.7075 | Exact configuration unresolved |
| [result-7f7c3a95450d82483805](../observations.json)<br>source-e55a92a1742e783d94e9e8c3.json<br>`/experiments/18/speed/0/backend_prefill/0` | [glm-dflash22-small_exl3-layer_split](glm-dflash22-small_exl3-layer_split.md) | test outcome | Outcome unspecified | backend_prefill_seconds=38.65 s; cached_prompt_tokens=0 tokens; prefill_tok_s=847.76 tokens/s; processed_prompt_tokens=32,766 tokens | Exact configuration unresolved |
| [result-80baa9c60d2aac10d0ef](../observations.json)<br>source-a9e622d351a86c8b776605d4.json<br>`/experiments/29` | [glm-dflash22-small_exl3-layer_split](glm-dflash22-small_exl3-layer_split.md) | context allocation | Outcome unspecified | matched_workload_host_peak_bytes=69,917,339,648 bytes; per_card_peak_used_MiB_unordered=42,796.00<br>61,038.00<br>61,796.00 | Exact configuration unresolved |
| [result-b8be329b82108f61db0f](../observations.json)<br>source-e55a92a1742e783d94e9e8c3.json<br>`/experiments/18/speed/1/backend_prefill/3` | [glm-dflash22-small_exl3-layer_split](glm-dflash22-small_exl3-layer_split.md) | test outcome | Outcome unspecified | backend_prefill_seconds=150.69 s; cached_prompt_tokens=0 tokens; prefill_tok_s=217.45 tokens/s; processed_prompt_tokens=32,767 tokens | Exact configuration unresolved |
| [result-d6d473e767ce90c1622f](../observations.json)<br>source-e55a92a1742e783d94e9e8c3.json<br>`/experiments/18/speed/1/backend_prefill/1` | [glm-dflash22-small_exl3-layer_split](glm-dflash22-small_exl3-layer_split.md) | test outcome | Outcome unspecified | backend_prefill_seconds=152.60 s; cached_prompt_tokens=0 tokens; prefill_tok_s=214.72 tokens/s; processed_prompt_tokens=32,767 tokens | Exact configuration unresolved |
| [result-d7a205a5f7e85d4bcf21](../observations.json)<br>source-f1e21f923fa477716745e960.json<br>`/` | [glm-dflash22-small_exl3-layer_split](glm-dflash22-small_exl3-layer_split.md) | correctness check | Pass | 4 response usage/timing records; matched_greedy_target_reference=false | Exact configuration unresolved |
| [result-eb1d2486c10420ac2bc9](../observations.json)<br>source-e55a92a1742e783d94e9e8c3.json<br>`/experiments/18/speed/1/backend_prefill/0` | [glm-dflash22-small_exl3-layer_split](glm-dflash22-small_exl3-layer_split.md) | test outcome | Outcome unspecified | backend_prefill_seconds=151.72 s; cached_prompt_tokens=0 tokens; prefill_tok_s=215.97 tokens/s; processed_prompt_tokens=32,767 tokens | Exact configuration unresolved |

These are saved result records, including failures and bounded checks. Copies, individual requests, report summaries and regrading can overlap; their counts are not independent test repetitions. Open each result for exact values, units, configuration binding and source receipts.

[Full archive](../../README.md) | [All retained waves](../RESULTS.md) | [Data definitions](../DATA.md) | [Recommended recipes](../../../README.md)
