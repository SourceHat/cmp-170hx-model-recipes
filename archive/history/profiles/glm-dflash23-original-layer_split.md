# glm-dflash23-original-layer_split

**Historical record. Additional test results; no matched decode wave.**

Model family: GLM 5.3 Flash.

The campaign inventory recorded status `speed_measured_capacity_pending`. The evidence sections retain any later results separately.

Historical configurations are provided for comparison. The [recommended recipes](../../../README.md) include supported launch scripts.

Current recipes using the same recorded checkpoint repository: [glm-5.3-flash-mtp1-tp3](../../../recipes/glm-5.3-flash-mtp1-tp3/README.md). Context, cache and runtime versions can differ.

## Saved Configuration Versions

Each configuration ID identifies a distinct original settings record. Deployment fields are omitted; versions can have identical published settings after that omission. Upstream runtime commits remain unspecified where the source retained only an integration label.

| Configuration | Recorded artifact / source | Configured card counts | Context tokens | GPU pool tokens | Slots | Draft mode / tokens |
| --- | --- | --- | --- | --- | --- | --- |
| cfg-e17395164b2bc20bf628 | [turboderp/GLM-5.3-Flash-exl3@2a30229e67](https://huggingface.co/turboderp/GLM-5.3-Flash-exl3/tree/2a30229e67012798ba9f0cd832bb78abf4c363d5) | 3 | 262,144 | 262,144 | 4 | dflash2 / 3 |

Card counts are saved configuration choices, not a claim that every allowed placement was measured. A derived view can differ from its pinned download source.

<details>
<summary>cfg-e17395164b2bc20bf628</summary>

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
| [result-0eeb3f3b98e3dd6d14f8](../observations.json)<br>source-d222d210cda0217790a6bf3a.json<br>`/` | [glm-dflash23-original-layer_split](glm-dflash23-original-layer_split.md) | correctness check | Pass | 4 response usage/timing records; matched_greedy_target_reference=false | Exact configuration unresolved |
| [result-7509b099890c4598e024](../observations.json)<br>source-e55a92a1742e783d94e9e8c3.json<br>`/experiments/16` | [glm-dflash23-original-layer_split](glm-dflash23-original-layer_split.md) | context allocation | Outcome unspecified | matched_workload_host_peak_bytes=70,083,031,040 bytes; per_card_peak_used_MiB_unordered=46,722.00<br>58,954.00<br>62,426.00 | Exact configuration unresolved |
| [result-77cf6d12e536f85fac8c](../observations.json)<br>source-e55a92a1742e783d94e9e8c3.json<br>`/experiments/16/speed/1` | [glm-dflash23-original-layer_split](glm-dflash23-original-layer_split.md) | performance detail | Outcome unspecified | cold_TTFT_median_seconds=155.25 s; configured_slots=4 requests; output_tokens=256 tokens; p50_inter_token_ms=61.78 ms; p95_inter_token_ms=237.55 ms; prompt_tokens=32,767 tokens; Draft accepted / proposed: 678 / 1,038 tokens; fraction 0.6532 | Exact configuration unresolved |
| [result-7825283c3da62f116342](../observations.json)<br>source-e55a92a1742e783d94e9e8c3.json<br>`/experiments/16/speed/1/backend_prefill/3` | [glm-dflash23-original-layer_split](glm-dflash23-original-layer_split.md) | test outcome | Outcome unspecified | backend_prefill_seconds=149.66 s; cached_prompt_tokens=0 tokens; prefill_tok_s=218.94 tokens/s; processed_prompt_tokens=32,767 tokens | Exact configuration unresolved |
| [result-813f00df1e8a2d0e5a7c](../observations.json)<br>source-e55a92a1742e783d94e9e8c3.json<br>`/experiments/16/speed/1/backend_prefill/2` | [glm-dflash23-original-layer_split](glm-dflash23-original-layer_split.md) | test outcome | Outcome unspecified | backend_prefill_seconds=150.39 s; cached_prompt_tokens=0 tokens; prefill_tok_s=217.88 tokens/s; processed_prompt_tokens=32,767 tokens | Exact configuration unresolved |
| [result-9be1c75bde6a0a81bb92](../observations.json)<br>source-e55a92a1742e783d94e9e8c3.json<br>`/experiments/16/speed/1/backend_prefill/1` | [glm-dflash23-original-layer_split](glm-dflash23-original-layer_split.md) | test outcome | Outcome unspecified | backend_prefill_seconds=151.55 s; cached_prompt_tokens=0 tokens; prefill_tok_s=216.21 tokens/s; processed_prompt_tokens=32,767 tokens | Exact configuration unresolved |
| [result-9c6470d95df54917fa10](../observations.json)<br>source-e55a92a1742e783d94e9e8c3.json<br>`/experiments/16/speed/1/backend_prefill/0` | [glm-dflash23-original-layer_split](glm-dflash23-original-layer_split.md) | test outcome | Outcome unspecified | backend_prefill_seconds=150.66 s; cached_prompt_tokens=0 tokens; prefill_tok_s=217.49 tokens/s; processed_prompt_tokens=32,767 tokens | Exact configuration unresolved |
| [result-9dc441d23a9f94293aa3](../observations.json)<br>source-a9e622d351a86c8b776605d4.json<br>`/experiments/25` | [glm-dflash23-original-layer_split](glm-dflash23-original-layer_split.md) | context allocation | Outcome unspecified | matched_workload_host_peak_bytes=70,083,031,040 bytes; per_card_peak_used_MiB_unordered=46,722.00<br>58,954.00<br>62,426.00 | Exact configuration unresolved |
| [result-deb72d9b9a18ce9b4583](../observations.json)<br>source-e55a92a1742e783d94e9e8c3.json<br>`/experiments/16/speed/0/backend_prefill/0` | [glm-dflash23-original-layer_split](glm-dflash23-original-layer_split.md) | test outcome | Outcome unspecified | backend_prefill_seconds=38.35 s; cached_prompt_tokens=0 tokens; prefill_tok_s=854.39 tokens/s; processed_prompt_tokens=32,766 tokens | Exact configuration unresolved |
| [result-eb940b8cb0bcc812970f](../observations.json)<br>source-e55a92a1742e783d94e9e8c3.json<br>`/experiments/16/speed/0` | [glm-dflash23-original-layer_split](glm-dflash23-original-layer_split.md) | performance detail | Outcome unspecified | cold_TTFT_median_seconds=38.53 s; configured_slots=4 requests; output_tokens=256 tokens; p50_inter_token_ms=18.71 ms; p95_inter_token_ms=60.63 ms; prompt_tokens=32,766 tokens; Draft accepted / proposed: 172 / 252 tokens; fraction 0.6825 | Exact configuration unresolved |

These are saved result records, including failures and bounded checks. Copies, individual requests, report summaries and regrading can overlap; their counts are not independent test repetitions. Open each result for exact values, units, configuration binding and source receipts.

[Full archive](../../README.md) | [All retained waves](../RESULTS.md) | [Data definitions](../DATA.md) | [Recommended recipes](../../../README.md)
