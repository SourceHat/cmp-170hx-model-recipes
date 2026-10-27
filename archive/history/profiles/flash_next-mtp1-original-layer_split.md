# flash_next-mtp1-original-layer_split

**Historical record. Additional test results; no matched decode wave.**

Model family: Qwen 3.8 Flash Next.

The campaign inventory recorded status `speed_measured_capacity_pending`. The evidence sections retain any later results separately.

Historical configurations are provided for comparison. The [recommended recipes](../../../README.md) include supported launch scripts.

Current recipes using the same recorded checkpoint repository: [qwen-flash-next-mtp2-layer-split](../../../recipes/qwen-flash-next-mtp2-layer-split/README.md). Context, cache and runtime versions can differ.

## Saved Configuration Versions

Each configuration ID identifies a distinct original settings record. Deployment fields are omitted; versions can have identical published settings after that omission. Upstream runtime commits remain unspecified where the source retained only an integration label.

| Configuration | Recorded artifact / source | Configured card counts | Context tokens | GPU pool tokens | Slots | Draft mode / tokens |
| --- | --- | --- | --- | --- | --- | --- |
| cfg-0f21c462d1fd9081352d | [turboderp/Qwen3.8-Flash-Next-exl3@d2e238feca](https://huggingface.co/turboderp/Qwen3.8-Flash-Next-exl3/tree/d2e238feca4c1c4d966943117356d8a42c2f4dcb) | 2 | 262,144 | 262,144 | 6 | mtp / 1 |

Card counts are saved configuration choices, not a claim that every allowed placement was measured. A derived view can differ from its pinned download source.

<details>
<summary>cfg-0f21c462d1fd9081352d</summary>

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
  "draft_tokens": 1,
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
| [result-041bd5d10d1618fc3dc6](../observations.json)<br>source-e55a92a1742e783d94e9e8c3.json<br>`/experiments/1/speed/1/backend_prefill/4` | [flash_next-mtp1-original-layer_split](flash_next-mtp1-original-layer_split.md) | test outcome | Outcome unspecified | backend_prefill_seconds=142.84 s; cached_prompt_tokens=0 tokens; prefill_tok_s=229.42 tokens/s; processed_prompt_tokens=32,770 tokens | Exact configuration unresolved |
| [result-12d3b3a33a68d950a5ca](../observations.json)<br>source-e55a92a1742e783d94e9e8c3.json<br>`/experiments/1/speed/1/backend_prefill/2` | [flash_next-mtp1-original-layer_split](flash_next-mtp1-original-layer_split.md) | test outcome | Outcome unspecified | backend_prefill_seconds=144.99 s; cached_prompt_tokens=0 tokens; prefill_tok_s=226.02 tokens/s; processed_prompt_tokens=32,770 tokens | Exact configuration unresolved |
| [result-3284e3daa12725d3f670](../observations.json)<br>source-e55a92a1742e783d94e9e8c3.json<br>`/experiments/1/speed/1/backend_prefill/1` | [flash_next-mtp1-original-layer_split](flash_next-mtp1-original-layer_split.md)<br>[flash_next-mtp3-original-layer_split](flash_next-mtp3-original-layer_split.md) | test outcome | Outcome unspecified | backend_prefill_seconds=145.14 s; cached_prompt_tokens=0 tokens; prefill_tok_s=225.78 tokens/s; processed_prompt_tokens=32,770 tokens | Exact configuration unresolved |
| [result-367aff2de2a54dbb3ec3](../observations.json)<br>source-e55a92a1742e783d94e9e8c3.json<br>`/experiments/1/speed/1/backend_prefill/3` | [flash_next-mtp1-original-layer_split](flash_next-mtp1-original-layer_split.md) | test outcome | Outcome unspecified | backend_prefill_seconds=144.60 s; cached_prompt_tokens=0 tokens; prefill_tok_s=226.63 tokens/s; processed_prompt_tokens=32,770 tokens | Exact configuration unresolved |
| [result-3f96d525674a67513d53](../observations.json)<br>source-e55a92a1742e783d94e9e8c3.json<br>`/experiments/1/speed/1` | [flash_next-mtp1-original-layer_split](flash_next-mtp1-original-layer_split.md) | performance detail | Outcome unspecified | cold_TTFT_median_seconds=147.58 s; configured_slots=6 requests; output_tokens=256 tokens; p50_inter_token_ms=45.18 ms; p95_inter_token_ms=91.39 ms; prompt_tokens=32,770 tokens; Draft accepted / proposed: 715 / 821 tokens; fraction 0.8709 | Exact configuration unresolved |
| [result-5d0e7824a7f4904b50e7](../observations.json)<br>source-e55a92a1742e783d94e9e8c3.json<br>`/experiments/1/speed/1/backend_prefill/0` | [flash_next-mtp1-original-layer_split](flash_next-mtp1-original-layer_split.md) | test outcome | Outcome unspecified | backend_prefill_seconds=142.62 s; cached_prompt_tokens=0 tokens; prefill_tok_s=229.77 tokens/s; processed_prompt_tokens=32,770 tokens | Exact configuration unresolved |
| [result-6cc4732fbf8915483269](../observations.json)<br>source-e55a92a1742e783d94e9e8c3.json<br>`/experiments/1/speed/0` | [flash_next-mtp1-original-layer_split](flash_next-mtp1-original-layer_split.md) | performance detail | Outcome unspecified | cold_TTFT_median_seconds=24.58 s; configured_slots=6 requests; output_tokens=256 tokens; p50_inter_token_ms=14.54 ms; p95_inter_token_ms=28.42 ms; prompt_tokens=32,769 tokens; Draft accepted / proposed: 119 / 137 tokens; fraction 0.8686 | Exact configuration unresolved |
| [result-89032c27972bae679cd8](../observations.json)<br>source-e55a92a1742e783d94e9e8c3.json<br>`/experiments/1/speed/1/backend_prefill/5` | [flash_next-mtp1-original-layer_split](flash_next-mtp1-original-layer_split.md) | test outcome | Outcome unspecified | backend_prefill_seconds=142.45 s; cached_prompt_tokens=0 tokens; prefill_tok_s=230.05 tokens/s; processed_prompt_tokens=32,770 tokens | Exact configuration unresolved |
| [result-8b24341366c1229049ee](../observations.json)<br>source-697be02520d77b7a1029f323.json<br>`/variants/0` | [flash_next-mtp1-original-layer_split](flash_next-mtp1-original-layer_split.md) | test outcome | Outcome unspecified | host_cgroup_peak_bytes=63,991,816,192 bytes | Exact configuration unresolved |
| [result-a8a7e9e226d0299a3ef0](../observations.json)<br>source-467f8bbd0683404cee842f4f.json<br>`/` | [flash_next-mtp1-original-layer_split](flash_next-mtp1-original-layer_split.md) | correctness check | Pass | 4 response usage/timing records | Exact configuration unresolved |
| [result-bce619ed1d327d5e2b06](../observations.json)<br>source-e55a92a1742e783d94e9e8c3.json<br>`/experiments/1/speed/0/backend_prefill/0` | [flash_next-mtp1-original-layer_split](flash_next-mtp1-original-layer_split.md) | test outcome | Outcome unspecified | backend_prefill_seconds=24.49 s; cached_prompt_tokens=0 tokens; prefill_tok_s=1,338.06 tokens/s; processed_prompt_tokens=32,769 tokens | Exact configuration unresolved |
| [result-d45052032cf4da6696ae](../observations.json)<br>source-a9e622d351a86c8b776605d4.json<br>`/experiments/1` | [flash_next-mtp1-original-layer_split](flash_next-mtp1-original-layer_split.md) | context allocation | Outcome unspecified | matched_workload_host_peak_bytes=63,991,816,192 bytes; per_card_peak_used_MiB_unordered=41,190.00<br>62,838.00 | Exact configuration unresolved |
| [result-fe54e9a2253245bad77c](../observations.json)<br>source-e55a92a1742e783d94e9e8c3.json<br>`/experiments/1` | [flash_next-mtp1-original-layer_split](flash_next-mtp1-original-layer_split.md) | context allocation | Outcome unspecified | matched_workload_host_peak_bytes=63,991,816,192 bytes; per_card_peak_used_MiB_unordered=41,190.00<br>62,838.00 | Exact configuration unresolved |

These are saved result records, including failures and bounded checks. Copies, individual requests, report summaries and regrading can overlap; their counts are not independent test repetitions. Open each result for exact values, units, configuration binding and source receipts.

[Full archive](../../README.md) | [All retained waves](../RESULTS.md) | [Data definitions](../DATA.md) | [Recommended recipes](../../../README.md)
