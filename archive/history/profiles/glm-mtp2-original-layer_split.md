# glm-mtp2-original-layer_split

**Historical record. Additional test results; no matched decode wave.**

Model family: GLM 5.3 Flash.

The campaign inventory recorded status `speed_measured_capacity_pending`. The evidence sections retain any later results separately.

Historical configurations are provided for comparison. The [recommended recipes](../../../README.md) include supported launch scripts.

Current recipes using the same recorded checkpoint repository: [glm-5.3-flash-mtp1-tp3](../../../recipes/glm-5.3-flash-mtp1-tp3/README.md). Context, cache and runtime versions can differ.

## Saved Configuration Versions

Each configuration ID identifies a distinct original settings record. Deployment fields are omitted; versions can have identical published settings after that omission. Upstream runtime commits remain unspecified where the source retained only an integration label.

| Configuration | Recorded artifact / source | Configured card counts | Context tokens | GPU pool tokens | Slots | Draft mode / tokens |
| --- | --- | --- | --- | --- | --- | --- |
| cfg-a901daedd6c029bc4f73 | [turboderp/GLM-5.3-Flash-exl3@2a30229e67](https://huggingface.co/turboderp/GLM-5.3-Flash-exl3/tree/2a30229e67012798ba9f0cd832bb78abf4c363d5) | 3 | 262,144 | 262,144 | 4 | mtp / 2 |

Card counts are saved configuration choices, not a claim that every allowed placement was measured. A derived view can differ from its pinned download source.

<details>
<summary>cfg-a901daedd6c029bc4f73</summary>

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
| [result-2349d1fda787223f9cdb](../observations.json)<br>source-e55a92a1742e783d94e9e8c3.json<br>`/experiments/12/speed/0` | [glm-mtp2-original-layer_split](glm-mtp2-original-layer_split.md) | performance detail | Outcome unspecified | cold_TTFT_median_seconds=39.81 s; configured_slots=4 requests; output_tokens=256 tokens; p50_inter_token_ms=20.89 ms; p95_inter_token_ms=60.39 ms; prompt_tokens=32,766 tokens; Draft accepted / proposed: 152 / 208 tokens; fraction 0.7308 | Exact configuration unresolved |
| [result-376bc99b3fd3cd26c75c](../observations.json)<br>source-e55a92a1742e783d94e9e8c3.json<br>`/experiments/12/speed/1/backend_prefill/3` | [glm-mtp2-original-layer_split](glm-mtp2-original-layer_split.md) | test outcome | Outcome unspecified | backend_prefill_seconds=150.86 s; cached_prompt_tokens=0 tokens; prefill_tok_s=217.20 tokens/s; processed_prompt_tokens=32,767 tokens | Exact configuration unresolved |
| [result-406cb8d360cf5d860a31](../observations.json)<br>source-e55a92a1742e783d94e9e8c3.json<br>`/experiments/12/speed/1/backend_prefill/2` | [glm-mtp2-original-layer_split](glm-mtp2-original-layer_split.md) | test outcome | Outcome unspecified | backend_prefill_seconds=151.60 s; cached_prompt_tokens=0 tokens; prefill_tok_s=216.14 tokens/s; processed_prompt_tokens=32,767 tokens | Exact configuration unresolved |
| [result-4da4514d35e8e0c4851d](../observations.json)<br>source-e55a92a1742e783d94e9e8c3.json<br>`/experiments/12/speed/1/backend_prefill/0` | [glm-mtp2-original-layer_split](glm-mtp2-original-layer_split.md) | test outcome | Outcome unspecified | backend_prefill_seconds=150.82 s; cached_prompt_tokens=0 tokens; prefill_tok_s=217.26 tokens/s; processed_prompt_tokens=32,767 tokens | Exact configuration unresolved |
| [result-74fd195b7a78c72d5893](../observations.json)<br>source-a9e622d351a86c8b776605d4.json<br>`/experiments/17` | [glm-mtp2-original-layer_split](glm-mtp2-original-layer_split.md) | context allocation | Outcome unspecified | matched_workload_host_peak_bytes=46,248,710,144 bytes; per_card_peak_used_MiB_unordered=43,298.00<br>61,042.00<br>61,800.00 | Exact configuration unresolved |
| [result-8a1b9691ac7d149719d0](../observations.json)<br>source-a2510fe8509439e7c5052e5e.json<br>`/` | [glm-mtp2-original-layer_split](glm-mtp2-original-layer_split.md) | correctness check | Pass | 4 response usage/timing records; matched_greedy_target_reference=false | Exact configuration unresolved |
| [result-988e9da04d60b0875ce1](../observations.json)<br>source-e55a92a1742e783d94e9e8c3.json<br>`/experiments/12/speed/1/backend_prefill/1` | [glm-mtp2-original-layer_split](glm-mtp2-original-layer_split.md) | test outcome | Outcome unspecified | backend_prefill_seconds=152.81 s; cached_prompt_tokens=0 tokens; prefill_tok_s=214.43 tokens/s; processed_prompt_tokens=32,767 tokens | Exact configuration unresolved |
| [result-d9c0ee00036a5da56120](../observations.json)<br>source-e55a92a1742e783d94e9e8c3.json<br>`/experiments/12/speed/0/backend_prefill/0` | [glm-mtp2-original-layer_split](glm-mtp2-original-layer_split.md) | test outcome | Outcome unspecified | backend_prefill_seconds=39.65 s; cached_prompt_tokens=0 tokens; prefill_tok_s=826.38 tokens/s; processed_prompt_tokens=32,766 tokens | Exact configuration unresolved |
| [result-f27247aa9e7b299f3388](../observations.json)<br>source-e55a92a1742e783d94e9e8c3.json<br>`/experiments/12/speed/1` | [glm-mtp2-original-layer_split](glm-mtp2-original-layer_split.md) | performance detail | Outcome unspecified | cold_TTFT_median_seconds=157.64 s; configured_slots=4 requests; output_tokens=256 tokens; p50_inter_token_ms=71.56 ms; p95_inter_token_ms=208.12 ms; prompt_tokens=32,767 tokens; Draft accepted / proposed: 594 / 860 tokens; fraction 0.6907 | Exact configuration unresolved |
| [result-f9ccc5cb27916fa2a089](../observations.json)<br>source-e55a92a1742e783d94e9e8c3.json<br>`/experiments/12` | [glm-mtp2-original-layer_split](glm-mtp2-original-layer_split.md) | context allocation | Outcome unspecified | matched_workload_host_peak_bytes=46,248,710,144 bytes; per_card_peak_used_MiB_unordered=43,298.00<br>61,042.00<br>61,800.00 | Exact configuration unresolved |

These are saved result records, including failures and bounded checks. Copies, individual requests, report summaries and regrading can overlap; their counts are not independent test repetitions. Open each result for exact values, units, configuration binding and source receipts.

[Full archive](../../README.md) | [All retained waves](../RESULTS.md) | [Data definitions](../DATA.md) | [Recommended recipes](../../../README.md)
