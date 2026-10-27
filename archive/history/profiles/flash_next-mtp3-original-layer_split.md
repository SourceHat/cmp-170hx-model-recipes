# flash_next-mtp3-original-layer_split

**Historical record. Additional test results; no matched decode wave.**

Model family: Qwen 3.8 Flash Next.

The campaign inventory recorded status `speed_measured_capacity_pending`. The evidence sections retain any later results separately.

Historical configurations are provided for comparison. The [recommended recipes](../../../README.md) include supported launch scripts.

Current recipes using the same recorded checkpoint repository: [qwen-flash-next-mtp2-layer-split](../../../recipes/qwen-flash-next-mtp2-layer-split/README.md). Context, cache and runtime versions can differ.

## Saved Configuration Versions

Each configuration ID identifies a distinct original settings record. Deployment fields are omitted; versions can have identical published settings after that omission. Upstream runtime commits remain unspecified where the source retained only an integration label.

| Configuration | Recorded artifact / source | Configured card counts | Context tokens | GPU pool tokens | Slots | Draft mode / tokens |
| --- | --- | --- | --- | --- | --- | --- |
| cfg-cb5986eea254e0d865a3 | [turboderp/Qwen3.8-Flash-Next-exl3@d2e238feca](https://huggingface.co/turboderp/Qwen3.8-Flash-Next-exl3/tree/d2e238feca4c1c4d966943117356d8a42c2f4dcb) | 2 | 262,144 | 262,144 | 6 | mtp / 3 |

Card counts are saved configuration choices, not a claim that every allowed placement was measured. A derived view can differ from its pinned download source.

<details>
<summary>cfg-cb5986eea254e0d865a3</summary>

```json
{
  "kind": "tabby",
  "gpu_counts": [
    2
  ],
  "context": 262144,
  "cache_tokens": 262144,
  "cache_mode": "Q8",
  "draft_cache_mode": "Q8",
  "draft_mode": "mtp",
  "draft_tokens": 3,
  "max_sessions": 6,
  "chunk_size": 512,
  "reserve_mib": 2048,
  "ram_kv_mib": 8192,
  "ram_recurrent_mib": 16384,
  "ngram_ram": true,
  "dynamic_draft": false,
  "output_chunk_tokens": 4096,
  "power_watts": 200,
  "host_memory_gib": 80,
  "host_swap_gib": 0,
  "min_vram_mib_per_gpu": 65530,
  "min_effective_vram_mib": 131060,
  "parallelism": "layer_split",
  "transport": "host",
  "host_backing": "ordinary",
  "model_repository": "turboderp/Qwen3.8-Flash-Next-exl3",
  "model_revision": "d2e238feca4c1c4d966943117356d8a42c2f4dcb",
  "draft_repository": null,
  "draft_revision": null,
  "recorded_runtime_label": null,
  "served_model_label": "qwen3.8-flash-next"
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
| [result-25952bfe0e9137af6ef3](../observations.json)<br>source-697be02520d77b7a1029f323.json<br>`/variants/2` | [flash_next-mtp3-original-layer_split](flash_next-mtp3-original-layer_split.md) | test outcome | Outcome unspecified | host_cgroup_peak_bytes=63,934,984,192 bytes | Exact configuration unresolved |
| [result-3284e3daa12725d3f670](../observations.json)<br>source-e55a92a1742e783d94e9e8c3.json<br>`/experiments/1/speed/1/backend_prefill/1` | [flash_next-mtp1-original-layer_split](flash_next-mtp1-original-layer_split.md)<br>[flash_next-mtp3-original-layer_split](flash_next-mtp3-original-layer_split.md) | test outcome | Outcome unspecified | backend_prefill_seconds=145.14 s; cached_prompt_tokens=0 tokens; prefill_tok_s=225.78 tokens/s; processed_prompt_tokens=32,770 tokens | Exact configuration unresolved |
| [result-44a319f1f5623146b5fd](../observations.json)<br>source-e55a92a1742e783d94e9e8c3.json<br>`/experiments/3` | [flash_next-mtp3-original-layer_split](flash_next-mtp3-original-layer_split.md) | context allocation | Outcome unspecified | matched_workload_host_peak_bytes=63,934,984,192 bytes; per_card_peak_used_MiB_unordered=43,762.00<br>61,586.00 | Exact configuration unresolved |
| [result-476d9492d087448a46cb](../observations.json)<br>source-e55a92a1742e783d94e9e8c3.json<br>`/experiments/3/speed/1/backend_prefill/0` | [flash_next-mtp3-original-layer_split](flash_next-mtp3-original-layer_split.md) | test outcome | Outcome unspecified | backend_prefill_seconds=142.60 s; cached_prompt_tokens=0 tokens; prefill_tok_s=229.80 tokens/s; processed_prompt_tokens=32,770 tokens | Exact configuration unresolved |
| [result-58af3a80174edb33f527](../observations.json)<br>source-e55a92a1742e783d94e9e8c3.json<br>`/experiments/3/speed/1/backend_prefill/5` | [flash_next-mtp3-original-layer_split](flash_next-mtp3-original-layer_split.md) | test outcome | Outcome unspecified | backend_prefill_seconds=142.51 s; cached_prompt_tokens=0 tokens; prefill_tok_s=229.95 tokens/s; processed_prompt_tokens=32,770 tokens | Exact configuration unresolved |
| [result-95b92f1ef970310c6326](../observations.json)<br>source-a9e622d351a86c8b776605d4.json<br>`/experiments/5` | [flash_next-mtp3-original-layer_split](flash_next-mtp3-original-layer_split.md) | context allocation | Outcome unspecified | matched_workload_host_peak_bytes=63,934,984,192 bytes; per_card_peak_used_MiB_unordered=43,762.00<br>61,586.00 | Exact configuration unresolved |
| [result-99ebb4f3777f9f42f8b3](../observations.json)<br>source-e55a92a1742e783d94e9e8c3.json<br>`/experiments/3/speed/1` | [flash_next-mtp3-original-layer_split](flash_next-mtp3-original-layer_split.md) | performance detail | Outcome unspecified | cold_TTFT_median_seconds=147.93 s; configured_slots=6 requests; output_tokens=256 tokens; p50_inter_token_ms=34.26 ms; p95_inter_token_ms=131.55 ms; prompt_tokens=32,770 tokens; Draft accepted / proposed: 1,025 / 1,533 tokens; fraction 0.6686 | Exact configuration unresolved |
| [result-ce8424362d120cc1fa11](../observations.json)<br>source-e55a92a1742e783d94e9e8c3.json<br>`/experiments/3/speed/1/backend_prefill/4` | [flash_next-mtp3-original-layer_split](flash_next-mtp3-original-layer_split.md) | test outcome | Outcome unspecified | backend_prefill_seconds=142.90 s; cached_prompt_tokens=0 tokens; prefill_tok_s=229.32 tokens/s; processed_prompt_tokens=32,770 tokens | Exact configuration unresolved |
| [result-d35b3747d3905810f8b6](../observations.json)<br>source-0dd5c1a4ce5bf5ae6114c6fa.json<br>`/` | [flash_next-mtp3-original-layer_split](flash_next-mtp3-original-layer_split.md) | correctness check | Pass | 4 response usage/timing records | Exact configuration unresolved |
| [result-d3b4b638089ddc08e6e0](../observations.json)<br>source-e55a92a1742e783d94e9e8c3.json<br>`/experiments/3/speed/1/backend_prefill/3` | [flash_next-mtp3-original-layer_split](flash_next-mtp3-original-layer_split.md) | test outcome | Outcome unspecified | backend_prefill_seconds=144.62 s; cached_prompt_tokens=0 tokens; prefill_tok_s=226.59 tokens/s; processed_prompt_tokens=32,770 tokens | Exact configuration unresolved |
| [result-db2df47fad1c22ba537a](../observations.json)<br>source-e55a92a1742e783d94e9e8c3.json<br>`/experiments/2/speed/0/backend_prefill/0` | [flash_next-mtp2-original-layer_split](flash_next-mtp2-original-layer_split.md)<br>[flash_next-mtp3-original-layer_split](flash_next-mtp3-original-layer_split.md) | test outcome | Outcome unspecified | backend_prefill_seconds=24.50 s; cached_prompt_tokens=0 tokens; prefill_tok_s=1,337.51 tokens/s; processed_prompt_tokens=32,769 tokens | Exact configuration unresolved |
| [result-eada6e210bf7b508b1dc](../observations.json)<br>source-e55a92a1742e783d94e9e8c3.json<br>`/experiments/3/speed/0` | [flash_next-mtp3-original-layer_split](flash_next-mtp3-original-layer_split.md) | performance detail | Outcome unspecified | cold_TTFT_median_seconds=24.60 s; configured_slots=6 requests; output_tokens=256 tokens; p50_inter_token_ms=12.75 ms; p95_inter_token_ms=38.07 ms; prompt_tokens=32,769 tokens; Draft accepted / proposed: 164 / 276 tokens; fraction 0.5942 | Exact configuration unresolved |
| [result-f83cf83c007129eba59a](../observations.json)<br>source-e55a92a1742e783d94e9e8c3.json<br>`/experiments/3/speed/1/backend_prefill/2` | [flash_next-mtp3-original-layer_split](flash_next-mtp3-original-layer_split.md) | test outcome | Outcome unspecified | backend_prefill_seconds=145.02 s; cached_prompt_tokens=0 tokens; prefill_tok_s=225.97 tokens/s; processed_prompt_tokens=32,770 tokens | Exact configuration unresolved |

These are saved result records, including failures and bounded checks. Copies, individual requests, report summaries and regrading can overlap; their counts are not independent test repetitions. Open each result for exact values, units, configuration binding and source receipts.

[Full archive](../../README.md) | [All retained waves](../RESULTS.md) | [Data definitions](../DATA.md) | [Recommended recipes](../../../README.md)
