# glm-mtp3-original-layer_split

**Historical record. Additional test results; no matched decode wave.**

Model family: GLM 5.3 Flash.

The campaign inventory recorded status `speed_measured_capacity_pending`. The evidence sections retain any later results separately.

Historical configurations are provided for comparison. The [recommended recipes](../../../README.md) include supported launch scripts.

Current recipes using the same recorded checkpoint repository: [glm-5.3-flash-mtp1-tp3](../../../recipes/glm-5.3-flash-mtp1-tp3/README.md). Context, cache and runtime versions can differ.

## Saved Configuration Versions

Each configuration ID identifies a distinct original settings record. Deployment fields are omitted; versions can have identical published settings after that omission. Upstream runtime commits remain unspecified where the source retained only an integration label.

| Configuration | Recorded artifact / source | Configured card counts | Context tokens | GPU pool tokens | Slots | Draft mode / tokens |
| --- | --- | --- | --- | --- | --- | --- |
| cfg-94af9a6b84c0ee54fa8a | [turboderp/GLM-5.3-Flash-exl3@2a30229e67](https://huggingface.co/turboderp/GLM-5.3-Flash-exl3/tree/2a30229e67012798ba9f0cd832bb78abf4c363d5) | 3 | 262,144 | 262,144 | 4 | mtp / 3 |

Card counts are saved configuration choices, not a claim that every allowed placement was measured. A derived view can differ from its pinned download source.

<details>
<summary>cfg-94af9a6b84c0ee54fa8a</summary>

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
  "served_model_label": "glm-5.3-flash"
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
| [result-0384597b6fd44c1c0235](../observations.json)<br>source-e55a92a1742e783d94e9e8c3.json<br>`/experiments/13/speed/1/backend_prefill/1` | [glm-mtp3-original-layer_split](glm-mtp3-original-layer_split.md) | test outcome | Outcome unspecified | backend_prefill_seconds=151.91 s; cached_prompt_tokens=0 tokens; prefill_tok_s=215.70 tokens/s; processed_prompt_tokens=32,767 tokens | Exact configuration unresolved |
| [result-306e5d034ed77f3b5bc2](../observations.json)<br>source-e55a92a1742e783d94e9e8c3.json<br>`/experiments/13/speed/1` | [glm-mtp3-original-layer_split](glm-mtp3-original-layer_split.md) | performance detail | Outcome unspecified | cold_TTFT_median_seconds=155.43 s; configured_slots=4 requests; output_tokens=256 tokens; p50_inter_token_ms=73.94 ms; p95_inter_token_ms=226.76 ms; prompt_tokens=32,767 tokens; Draft accepted / proposed: 667 / 1,071 tokens; fraction 0.6228 | Exact configuration unresolved |
| [result-6b0d6817a040f9ae6ae4](../observations.json)<br>source-e55a92a1742e783d94e9e8c3.json<br>`/experiments/13/speed/1/backend_prefill/0` | [glm-mtp3-original-layer_split](glm-mtp3-original-layer_split.md) | test outcome | Outcome unspecified | backend_prefill_seconds=151.01 s; cached_prompt_tokens=0 tokens; prefill_tok_s=216.99 tokens/s; processed_prompt_tokens=32,767 tokens | Exact configuration unresolved |
| [result-6fb62646a394a662d99f](../observations.json)<br>source-e55a92a1742e783d94e9e8c3.json<br>`/experiments/13/speed/1/backend_prefill/3` | [glm-mtp3-original-layer_split](glm-mtp3-original-layer_split.md) | test outcome | Outcome unspecified | backend_prefill_seconds=149.99 s; cached_prompt_tokens=0 tokens; prefill_tok_s=218.46 tokens/s; processed_prompt_tokens=32,767 tokens | Exact configuration unresolved |
| [result-938595307f376e537dce](../observations.json)<br>source-a9e622d351a86c8b776605d4.json<br>`/experiments/19` | [glm-mtp3-original-layer_split](glm-mtp3-original-layer_split.md) | context allocation | Outcome unspecified | matched_workload_host_peak_bytes=70,147,543,040 bytes; per_card_peak_used_MiB_unordered=43,500.00<br>61,244.00<br>62,036.00 | Exact configuration unresolved |
| [result-ad48a4d89d8927aba4d5](../observations.json)<br>source-e55a92a1742e783d94e9e8c3.json<br>`/experiments/13/speed/0` | [glm-mtp3-original-layer_split](glm-mtp3-original-layer_split.md) | performance detail | Outcome unspecified | cold_TTFT_median_seconds=38.74 s; configured_slots=4 requests; output_tokens=256 tokens; p50_inter_token_ms=21.79 ms; p95_inter_token_ms=63.97 ms; prompt_tokens=32,766 tokens; Draft accepted / proposed: 170 / 258 tokens; fraction 0.6589 | Exact configuration unresolved |
| [result-b09f592130ea4970c882](../observations.json)<br>source-e55a92a1742e783d94e9e8c3.json<br>`/experiments/13` | [glm-mtp3-original-layer_split](glm-mtp3-original-layer_split.md) | context allocation | Outcome unspecified | matched_workload_host_peak_bytes=70,147,543,040 bytes; per_card_peak_used_MiB_unordered=43,500.00<br>61,244.00<br>62,036.00 | Exact configuration unresolved |
| [result-b15a37ec93eaa3bfb540](../observations.json)<br>source-89ac8a3f45d94ea16bb69207.json<br>`/` | [glm-mtp3-original-layer_split](glm-mtp3-original-layer_split.md) | correctness check | Pass | 4 response usage/timing records; matched_greedy_target_reference=false | Exact configuration unresolved |
| [result-b1e50f84a51910ba606f](../observations.json)<br>source-e55a92a1742e783d94e9e8c3.json<br>`/experiments/13/speed/0/backend_prefill/0` | [glm-mtp3-original-layer_split](glm-mtp3-original-layer_split.md) | test outcome | Outcome unspecified | backend_prefill_seconds=38.56 s; cached_prompt_tokens=0 tokens; prefill_tok_s=849.74 tokens/s; processed_prompt_tokens=32,766 tokens | Exact configuration unresolved |
| [result-cc94d3375dce95967458](../observations.json)<br>source-e55a92a1742e783d94e9e8c3.json<br>`/experiments/13/speed/1/backend_prefill/2` | [glm-mtp3-original-layer_split](glm-mtp3-original-layer_split.md) | test outcome | Outcome unspecified | backend_prefill_seconds=150.72 s; cached_prompt_tokens=0 tokens; prefill_tok_s=217.40 tokens/s; processed_prompt_tokens=32,767 tokens | Exact configuration unresolved |

These are saved result records, including failures and bounded checks. Copies, individual requests, report summaries and regrading can overlap; their counts are not independent test repetitions. Open each result for exact values, units, configuration binding and source receipts.

[Full archive](../../README.md) | [All retained waves](../RESULTS.md) | [Data definitions](../DATA.md) | [Recommended recipes](../../../README.md)
