# glm-dflash22-original-layer_split

**Historical record. Additional test results; no matched decode wave.**

Model family: GLM 5.3 Flash.

The campaign inventory recorded status `speed_measured_capacity_pending`. The evidence sections retain any later results separately.

Historical configurations are provided for comparison. The [recommended recipes](../../../README.md) include supported launch scripts.

Current recipes using the same recorded checkpoint repository: [glm-5.3-flash-mtp1-tp3](../../../recipes/glm-5.3-flash-mtp1-tp3/README.md). Context, cache and runtime versions can differ.

## Saved Configuration Versions

Each configuration ID identifies a distinct original settings record. Deployment fields are omitted; versions can have identical published settings after that omission. Upstream runtime commits remain unspecified where the source retained only an integration label.

| Configuration | Recorded artifact / source | Configured card counts | Context tokens | GPU pool tokens | Slots | Draft mode / tokens |
| --- | --- | --- | --- | --- | --- | --- |
| cfg-401c48f27ac1759d457d | [turboderp/GLM-5.3-Flash-exl3@2a30229e67](https://huggingface.co/turboderp/GLM-5.3-Flash-exl3/tree/2a30229e67012798ba9f0cd832bb78abf4c363d5) | 3 | 262,144 | 262,144 | 4 | dflash2 / 2 |

Card counts are saved configuration choices, not a claim that every allowed placement was measured. A derived view can differ from its pinned download source.

<details>
<summary>cfg-401c48f27ac1759d457d</summary>

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
| [result-0aa89f29a5e7be1aa475](../observations.json)<br>source-a9e622d351a86c8b776605d4.json<br>`/experiments/23` | [glm-dflash22-original-layer_split](glm-dflash22-original-layer_split.md) | context allocation | Outcome unspecified | matched_workload_host_peak_bytes=77,204,221,952 bytes; per_card_peak_used_MiB_unordered=43,010.00<br>62,110.00<br>62,184.00 | Exact configuration unresolved |
| [result-1b3ce8857af417b7fe78](../observations.json)<br>source-f2e637ea7f47ab03e891bce6.json<br>`/` | [glm-dflash22-original-layer_split](glm-dflash22-original-layer_split.md) | correctness check | Pass | 4 response usage/timing records; matched_greedy_target_reference=false | Exact configuration unresolved |
| [result-29e47d70b561e99b4ae9](../observations.json)<br>source-e55a92a1742e783d94e9e8c3.json<br>`/experiments/15/speed/1/backend_prefill/3` | [glm-dflash22-original-layer_split](glm-dflash22-original-layer_split.md) | test outcome | Outcome unspecified | backend_prefill_seconds=148.02 s; cached_prompt_tokens=0 tokens; prefill_tok_s=221.37 tokens/s; processed_prompt_tokens=32,767 tokens | Exact configuration unresolved |
| [result-606f2f354ffb4784739a](../observations.json)<br>source-e55a92a1742e783d94e9e8c3.json<br>`/experiments/15/speed/1` | [glm-dflash22-original-layer_split](glm-dflash22-original-layer_split.md) | performance detail | Outcome unspecified | cold_TTFT_median_seconds=153.69 s; configured_slots=4 requests; output_tokens=256 tokens; p50_inter_token_ms=73.40 ms; p95_inter_token_ms=215.70 ms; prompt_tokens=32,767 tokens; Draft accepted / proposed: 605 / 838 tokens; fraction 0.7220 | Exact configuration unresolved |
| [result-60bbb55272cb59e7ae7a](../observations.json)<br>source-e55a92a1742e783d94e9e8c3.json<br>`/experiments/15/speed/0` | [glm-dflash22-original-layer_split](glm-dflash22-original-layer_split.md) | performance detail | Outcome unspecified | cold_TTFT_median_seconds=38.27 s; configured_slots=4 requests; output_tokens=256 tokens; p50_inter_token_ms=21.91 ms; p95_inter_token_ms=60.69 ms; prompt_tokens=32,766 tokens; Draft accepted / proposed: 154 / 204 tokens; fraction 0.7549 | Exact configuration unresolved |
| [result-75d23eeec490880a8058](../observations.json)<br>source-e55a92a1742e783d94e9e8c3.json<br>`/experiments/15/speed/1/backend_prefill/0` | [glm-dflash22-original-layer_split](glm-dflash22-original-layer_split.md) | test outcome | Outcome unspecified | backend_prefill_seconds=147.91 s; cached_prompt_tokens=0 tokens; prefill_tok_s=221.53 tokens/s; processed_prompt_tokens=32,767 tokens | Exact configuration unresolved |
| [result-840251b9388a8a25d3e1](../observations.json)<br>source-e55a92a1742e783d94e9e8c3.json<br>`/experiments/15/speed/0/backend_prefill/0` | [glm-dflash22-original-layer_split](glm-dflash22-original-layer_split.md) | test outcome | Outcome unspecified | backend_prefill_seconds=38.10 s; cached_prompt_tokens=0 tokens; prefill_tok_s=860.00 tokens/s; processed_prompt_tokens=32,766 tokens | Exact configuration unresolved |
| [result-a3768cfefa258f301cb5](../observations.json)<br>source-e55a92a1742e783d94e9e8c3.json<br>`/experiments/15/speed/1/backend_prefill/2` | [glm-dflash22-original-layer_split](glm-dflash22-original-layer_split.md) | test outcome | Outcome unspecified | backend_prefill_seconds=148.74 s; cached_prompt_tokens=0 tokens; prefill_tok_s=220.30 tokens/s; processed_prompt_tokens=32,767 tokens | Exact configuration unresolved |
| [result-b13a0d6fc0379ee6e0ba](../observations.json)<br>source-e55a92a1742e783d94e9e8c3.json<br>`/experiments/15` | [glm-dflash22-original-layer_split](glm-dflash22-original-layer_split.md) | context allocation | Outcome unspecified | matched_workload_host_peak_bytes=77,204,221,952 bytes; per_card_peak_used_MiB_unordered=43,010.00<br>62,110.00<br>62,184.00 | Exact configuration unresolved |
| [result-c4277118453ef4ce32dc](../observations.json)<br>source-e55a92a1742e783d94e9e8c3.json<br>`/experiments/15/speed/1/backend_prefill/1` | [glm-dflash22-original-layer_split](glm-dflash22-original-layer_split.md) | test outcome | Outcome unspecified | backend_prefill_seconds=149.91 s; cached_prompt_tokens=0 tokens; prefill_tok_s=218.58 tokens/s; processed_prompt_tokens=32,767 tokens | Exact configuration unresolved |

These are saved result records, including failures and bounded checks. Copies, individual requests, report summaries and regrading can overlap; their counts are not independent test repetitions. Open each result for exact values, units, configuration binding and source receipts.

[Full archive](../../README.md) | [All retained waves](../RESULTS.md) | [Data definitions](../DATA.md) | [Recommended recipes](../../../README.md)
