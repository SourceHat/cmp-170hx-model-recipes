# glm-dflash21-original-layer_split

**Historical record. Additional test results; no matched decode wave.**

Model family: GLM 5.3 Flash.

The campaign inventory recorded status `speed_measured_capacity_pending`. The evidence sections retain any later results separately.

Historical configurations are provided for comparison. The [recommended recipes](../../../README.md) include supported launch scripts.

Current recipes using the same recorded checkpoint repository: [glm-5.3-flash-mtp1-tp3](../../../recipes/glm-5.3-flash-mtp1-tp3/README.md). Context, cache and runtime versions can differ.

## Saved Configuration Versions

Each configuration ID identifies a distinct original settings record. Deployment fields are omitted; versions can have identical published settings after that omission. Upstream runtime commits remain unspecified where the source retained only an integration label.

| Configuration | Recorded artifact / source | Configured card counts | Context tokens | GPU pool tokens | Slots | Draft mode / tokens |
| --- | --- | --- | --- | --- | --- | --- |
| cfg-d3aeb0a10e876985eb19 | [turboderp/GLM-5.3-Flash-exl3@2a30229e67](https://huggingface.co/turboderp/GLM-5.3-Flash-exl3/tree/2a30229e67012798ba9f0cd832bb78abf4c363d5) | 3 | 262,144 | 262,144 | 4 | dflash2 / 1 |

Card counts are saved configuration choices, not a claim that every allowed placement was measured. A derived view can differ from its pinned download source.

<details>
<summary>cfg-d3aeb0a10e876985eb19</summary>

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
| [result-1a3c12cbd0a53bf6936c](../observations.json)<br>source-a9e622d351a86c8b776605d4.json<br>`/experiments/21` | [glm-dflash21-original-layer_split](glm-dflash21-original-layer_split.md) | context allocation | Outcome unspecified | matched_workload_host_peak_bytes=78,528,040,960 bytes; per_card_peak_used_MiB_unordered=42,860.00<br>61,906.00<br>61,958.00 | Exact configuration unresolved |
| [result-4289658de9a6df83588b](../observations.json)<br>source-e55a92a1742e783d94e9e8c3.json<br>`/experiments/14/speed/1` | [glm-dflash21-original-layer_split](glm-dflash21-original-layer_split.md) | performance detail | Outcome unspecified | cold_TTFT_median_seconds=153.63 s; configured_slots=4 requests; output_tokens=256 tokens; p50_inter_token_ms=63.36 ms; p95_inter_token_ms=126.15 ms; prompt_tokens=32,767 tokens; Draft accepted / proposed: 472 / 552 tokens; fraction 0.8551 | Exact configuration unresolved |
| [result-65314a50a591ae83a22c](../observations.json)<br>source-5834c1de2cc8e02f1d165a4c.json<br>`/` | [glm-dflash21-original-layer_split](glm-dflash21-original-layer_split.md) | correctness check | Pass | 4 response usage/timing records; matched_greedy_target_reference=false | Exact configuration unresolved |
| [result-9177e695b4bfbf4178be](../observations.json)<br>source-e55a92a1742e783d94e9e8c3.json<br>`/experiments/14/speed/1/backend_prefill/0` | [glm-dflash21-original-layer_split](glm-dflash21-original-layer_split.md) | test outcome | Outcome unspecified | backend_prefill_seconds=148.01 s; cached_prompt_tokens=0 tokens; prefill_tok_s=221.38 tokens/s; processed_prompt_tokens=32,767 tokens | Exact configuration unresolved |
| [result-a131d9b4043dd3c556d4](../observations.json)<br>source-e55a92a1742e783d94e9e8c3.json<br>`/experiments/14/speed/0` | [glm-dflash21-original-layer_split](glm-dflash21-original-layer_split.md) | performance detail | Outcome unspecified | cold_TTFT_median_seconds=38.24 s; configured_slots=4 requests; output_tokens=256 tokens; p50_inter_token_ms=28.48 ms; p95_inter_token_ms=57.56 ms; prompt_tokens=32,766 tokens; Draft accepted / proposed: 115 / 141 tokens; fraction 0.8156 | Exact configuration unresolved |
| [result-acd06ad4ccf68427df07](../observations.json)<br>source-e55a92a1742e783d94e9e8c3.json<br>`/experiments/14/speed/1/backend_prefill/3` | [glm-dflash21-original-layer_split](glm-dflash21-original-layer_split.md) | test outcome | Outcome unspecified | backend_prefill_seconds=148.05 s; cached_prompt_tokens=0 tokens; prefill_tok_s=221.32 tokens/s; processed_prompt_tokens=32,767 tokens | Exact configuration unresolved |
| [result-ae9ab94c31a9118a43dd](../observations.json)<br>source-e55a92a1742e783d94e9e8c3.json<br>`/experiments/14/speed/0/backend_prefill/0` | [glm-dflash21-original-layer_split](glm-dflash21-original-layer_split.md) | test outcome | Outcome unspecified | backend_prefill_seconds=38.12 s; cached_prompt_tokens=0 tokens; prefill_tok_s=859.55 tokens/s; processed_prompt_tokens=32,766 tokens | Exact configuration unresolved |
| [result-bc27fa69e5eab199f31b](../observations.json)<br>source-e55a92a1742e783d94e9e8c3.json<br>`/experiments/14/speed/1/backend_prefill/1` | [glm-dflash21-original-layer_split](glm-dflash21-original-layer_split.md) | test outcome | Outcome unspecified | backend_prefill_seconds=149.95 s; cached_prompt_tokens=0 tokens; prefill_tok_s=218.52 tokens/s; processed_prompt_tokens=32,767 tokens | Exact configuration unresolved |
| [result-da9811df7adb335f9d45](../observations.json)<br>source-e55a92a1742e783d94e9e8c3.json<br>`/experiments/14/speed/1/backend_prefill/2` | [glm-dflash21-original-layer_split](glm-dflash21-original-layer_split.md) | test outcome | Outcome unspecified | backend_prefill_seconds=148.78 s; cached_prompt_tokens=0 tokens; prefill_tok_s=220.24 tokens/s; processed_prompt_tokens=32,767 tokens | Exact configuration unresolved |
| [result-dd6a623ef0476fd6feee](../observations.json)<br>source-e55a92a1742e783d94e9e8c3.json<br>`/experiments/14` | [glm-dflash21-original-layer_split](glm-dflash21-original-layer_split.md) | context allocation | Outcome unspecified | matched_workload_host_peak_bytes=78,528,040,960 bytes; per_card_peak_used_MiB_unordered=42,860.00<br>61,906.00<br>61,958.00 | Exact configuration unresolved |

These are saved result records, including failures and bounded checks. Copies, individual requests, report summaries and regrading can overlap; their counts are not independent test repetitions. Open each result for exact values, units, configuration binding and source receipts.

[Full archive](../../README.md) | [All retained waves](../RESULTS.md) | [Data definitions](../DATA.md) | [Recommended recipes](../../../README.md)
