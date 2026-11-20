# mimo-mtp2-original-layer_split

**Historical record. Additional test results; no matched decode wave.**

Model family: MiMo V2.6 Flash.

The campaign inventory recorded status `speed_measured_capacity_pending`. The evidence sections retain any later results separately.

Historical configurations are provided for comparison. The [recommended recipes](../../../README.md) include supported launch scripts.

Current recipes using the same recorded checkpoint repository: [mimo-flash-mtp1-tp3](../../../recipes/mimo-flash-mtp1-tp3/README.md). Context, cache and runtime versions can differ.

## Saved Configuration Versions

Each configuration ID identifies a distinct original settings record. Deployment fields are omitted; versions can have identical published settings after that omission. Upstream runtime commits remain unspecified where the source retained only an integration label.

| Configuration | Recorded artifact / source | Configured card counts | Context tokens | GPU pool tokens | Slots | Draft mode / tokens |
| --- | --- | --- | --- | --- | --- | --- |
| cfg-442222ebf12c381d6a19 | [MikeRoz/MiMo-V2.6-Flash-MOPD-4.03bpw-h8-exl3@29c8351a8b](https://huggingface.co/MikeRoz/MiMo-V2.6-Flash-MOPD-4.03bpw-h8-exl3/tree/29c8351a8b5854ec385adaeba7bbe62c790d40ea) | 3 | 262,144 | 262,144 | 4 | mtp / 2 |

Card counts are saved configuration choices, not a claim that every allowed placement was measured. A derived view can differ from its pinned download source.

<details>
<summary>cfg-442222ebf12c381d6a19</summary>

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
  "model_repository": "MikeRoz/MiMo-V2.6-Flash-MOPD-4.03bpw-h8-exl3",
  "model_revision": "29c8351a8b5854ec385adaeba7bbe62c790d40ea",
  "draft_repository": null,
  "draft_revision": null,
  "recorded_runtime_label": null,
  "served_model_label": "mimo-v2.6-flash"
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
| [result-0a6a7a3eee0f5fb8052f](../observations.json)<br>source-e55a92a1742e783d94e9e8c3.json<br>`/experiments/7/speed/0` | [mimo-mtp2-original-layer_split](mimo-mtp2-original-layer_split.md) | performance detail | Outcome unspecified | cold_TTFT_median_seconds=2.85 s; configured_slots=4 requests; output_tokens=512 tokens; p50_inter_token_ms=19.46 ms; p95_inter_token_ms=51.52 ms; prompt_tokens=2,038 tokens; Draft accepted / proposed: 289 / 446 tokens; fraction 0.6480 | Exact configuration unresolved |
| [result-109ce832db71fc989ca7](../observations.json)<br>source-e55a92a1742e783d94e9e8c3.json<br>`/experiments/7/speed/3` | [mimo-mtp2-original-layer_split](mimo-mtp2-original-layer_split.md) | performance detail | Outcome unspecified | cold_TTFT_median_seconds=166.88 s; configured_slots=4 requests; output_tokens=512 tokens; p50_inter_token_ms=95.67 ms; p95_inter_token_ms=228.97 ms; prompt_tokens=32,766 tokens; Draft accepted / proposed: 1,121 / 1,854 tokens; fraction 0.6046 | Exact configuration unresolved |
| [result-1748d34c607e95b71511](../observations.json)<br>source-e55a92a1742e783d94e9e8c3.json<br>`/experiments/7/speed/3/backend_prefill/0` | [mimo-mtp2-original-layer_split](mimo-mtp2-original-layer_split.md) | test outcome | Outcome unspecified | backend_prefill_seconds=161.45 s; cached_prompt_tokens=0 tokens; prefill_tok_s=202.95 tokens/s; processed_prompt_tokens=32,766 tokens | Exact configuration unresolved |
| [result-22b91c2a40126f6aa952](../observations.json)<br>source-5e531a2489df25ad83c6c20e.json<br>`/` | [mimo-mtp2-original-layer_split](mimo-mtp2-original-layer_split.md) | correctness check | Pass | 4 response usage/timing records | Exact configuration unresolved |
| [result-42ad44fa1edfc559344b](../observations.json)<br>source-e55a92a1742e783d94e9e8c3.json<br>`/experiments/7/speed/1/backend_prefill/0` | [mimo-mtp2-original-layer_split](mimo-mtp2-original-layer_split.md) | test outcome | Outcome unspecified | backend_prefill_seconds=5.80 s; cached_prompt_tokens=0 tokens; prefill_tok_s=351.55 tokens/s; processed_prompt_tokens=2,039 tokens | Exact configuration unresolved |
| [result-5761fa61c65f78db7789](../observations.json)<br>source-e55a92a1742e783d94e9e8c3.json<br>`/experiments/7` | [mimo-mtp2-original-layer_split](mimo-mtp2-original-layer_split.md) | context allocation | Outcome unspecified | matched_workload_host_peak_bytes=45,176,320,000 bytes; per_card_peak_used_MiB_unordered=40,950.00<br>59,884.00<br>62,572.00 | Exact configuration unresolved |
| [result-7bd3b610a83bb6bfa077](../observations.json)<br>source-e55a92a1742e783d94e9e8c3.json<br>`/experiments/7/speed/2/backend_prefill/0` | [mimo-mtp2-original-layer_split](mimo-mtp2-original-layer_split.md) | test outcome | Outcome unspecified | backend_prefill_seconds=41.72 s; cached_prompt_tokens=0 tokens; prefill_tok_s=785.35 tokens/s; processed_prompt_tokens=32,765 tokens | Exact configuration unresolved |
| [result-7e18682843f1bd4dfe59](../observations.json)<br>source-e55a92a1742e783d94e9e8c3.json<br>`/experiments/7/speed/3/backend_prefill/2` | [mimo-mtp2-original-layer_split](mimo-mtp2-original-layer_split.md) | test outcome | Outcome unspecified | backend_prefill_seconds=162.75 s; cached_prompt_tokens=0 tokens; prefill_tok_s=201.33 tokens/s; processed_prompt_tokens=32,766 tokens | Exact configuration unresolved |
| [result-7fee2ec3f36a32014c26](../observations.json)<br>source-e55a92a1742e783d94e9e8c3.json<br>`/experiments/7/speed/1` | [mimo-mtp2-original-layer_split](mimo-mtp2-original-layer_split.md) | performance detail | Outcome unspecified | cold_TTFT_median_seconds=11.09 s; configured_slots=4 requests; output_tokens=512 tokens; p50_inter_token_ms=48.82 ms; p95_inter_token_ms=135.87 ms; prompt_tokens=2,039 tokens; Draft accepted / proposed: 1,154 / 1,788 tokens; fraction 0.6454 | Exact configuration unresolved |
| [result-814a0e635dd2f02d5bb9](../observations.json)<br>source-e55a92a1742e783d94e9e8c3.json<br>`/experiments/7/speed/3/backend_prefill/3` | [mimo-mtp2-original-layer_split](mimo-mtp2-original-layer_split.md) | test outcome | Outcome unspecified | backend_prefill_seconds=161.22 s; cached_prompt_tokens=0 tokens; prefill_tok_s=203.24 tokens/s; processed_prompt_tokens=32,766 tokens | Exact configuration unresolved |
| [result-93099f54053a5c7a5184](../observations.json)<br>source-e55a92a1742e783d94e9e8c3.json<br>`/experiments/7/speed/0/backend_prefill/0` | [mimo-mtp2-original-layer_split](mimo-mtp2-original-layer_split.md) | test outcome | Outcome unspecified | backend_prefill_seconds=2.79 s; cached_prompt_tokens=0 tokens; prefill_tok_s=730.47 tokens/s; processed_prompt_tokens=2,038 tokens | Exact configuration unresolved |
| [result-b5e83ba38d435bb71dab](../observations.json)<br>source-e55a92a1742e783d94e9e8c3.json<br>`/experiments/7/speed/1/backend_prefill/3` | [mimo-mtp2-original-layer_split](mimo-mtp2-original-layer_split.md) | test outcome | Outcome unspecified | backend_prefill_seconds=5.78 s; cached_prompt_tokens=0 tokens; prefill_tok_s=352.77 tokens/s; processed_prompt_tokens=2,039 tokens | Exact configuration unresolved |
| [result-b8fd8d8097780397248a](../observations.json)<br>source-a9e622d351a86c8b776605d4.json<br>`/experiments/9` | [mimo-mtp2-original-layer_split](mimo-mtp2-original-layer_split.md) | context allocation | Outcome unspecified | matched_workload_host_peak_bytes=45,176,320,000 bytes; per_card_peak_used_MiB_unordered=40,950.00<br>59,884.00<br>62,572.00 | Exact configuration unresolved |
| [result-c3cdd12a8b4c2507de5c](../observations.json)<br>source-e55a92a1742e783d94e9e8c3.json<br>`/experiments/7/speed/3/backend_prefill/1` | [mimo-mtp2-original-layer_split](mimo-mtp2-original-layer_split.md) | test outcome | Outcome unspecified | backend_prefill_seconds=163.33 s; cached_prompt_tokens=0 tokens; prefill_tok_s=200.61 tokens/s; processed_prompt_tokens=32,766 tokens | Exact configuration unresolved |
| [result-d090d6b07183473d08d9](../observations.json)<br>source-e55a92a1742e783d94e9e8c3.json<br>`/experiments/7/speed/1/backend_prefill/2` | [mimo-mtp2-original-layer_split](mimo-mtp2-original-layer_split.md) | test outcome | Outcome unspecified | backend_prefill_seconds=7.44 s; cached_prompt_tokens=0 tokens; prefill_tok_s=274.06 tokens/s; processed_prompt_tokens=2,039 tokens | Exact configuration unresolved |
| [result-da1e4f8876a63197c9ad](../observations.json)<br>source-e55a92a1742e783d94e9e8c3.json<br>`/experiments/7/speed/1/backend_prefill/1` | [mimo-mtp2-original-layer_split](mimo-mtp2-original-layer_split.md) | test outcome | Outcome unspecified | backend_prefill_seconds=8.06 s; cached_prompt_tokens=0 tokens; prefill_tok_s=252.98 tokens/s; processed_prompt_tokens=2,039 tokens | Exact configuration unresolved |
| [result-f67bfae376695b34198c](../observations.json)<br>source-e55a92a1742e783d94e9e8c3.json<br>`/experiments/7/speed/2` | [mimo-mtp2-original-layer_split](mimo-mtp2-original-layer_split.md) | performance detail | Outcome unspecified | cold_TTFT_median_seconds=41.86 s; configured_slots=4 requests; output_tokens=512 tokens; p50_inter_token_ms=28.24 ms; p95_inter_token_ms=69.01 ms; prompt_tokens=32,765 tokens; Draft accepted / proposed: 283 / 458 tokens; fraction 0.6179 | Exact configuration unresolved |

These are saved result records, including failures and bounded checks. Copies, individual requests, report summaries and regrading can overlap; their counts are not independent test repetitions. Open each result for exact values, units, configuration binding and source receipts.

[Full archive](../../README.md) | [All retained waves](../RESULTS.md) | [Data definitions](../DATA.md) | [Recommended recipes](../../../README.md)
