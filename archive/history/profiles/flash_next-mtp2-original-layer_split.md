# flash_next-mtp2-original-layer_split

**Historical record. Additional test results; no matched decode wave.**

Model family: Qwen 3.8 Flash Next.

The campaign inventory recorded status `speed_measured_capacity_pending`. The evidence sections retain any later results separately.

Historical configurations are provided for comparison. The [recommended recipes](../../../README.md) include supported launch scripts.

Current recipes using the same recorded checkpoint repository: [qwen-flash-next-mtp2-layer-split](../../../recipes/qwen-flash-next-mtp2-layer-split/README.md). Context, cache and runtime versions can differ.

## Saved Configuration Versions

Each configuration ID identifies a distinct original settings record. Deployment fields are omitted; versions can have identical published settings after that omission. Upstream runtime commits remain unspecified where the source retained only an integration label.

| Configuration | Recorded artifact / source | Configured card counts | Context tokens | GPU pool tokens | Slots | Draft mode / tokens |
| --- | --- | --- | --- | --- | --- | --- |
| cfg-5eccb9704af16395b9bd | [turboderp/Qwen3.8-Flash-Next-exl3@d2e238feca](https://huggingface.co/turboderp/Qwen3.8-Flash-Next-exl3/tree/d2e238feca4c1c4d966943117356d8a42c2f4dcb) | 2 | 262,144 | 262,144 | 6 | mtp / 2 |

Card counts are saved configuration choices, not a claim that every allowed placement was measured. A derived view can differ from its pinned download source.

<details>
<summary>cfg-5eccb9704af16395b9bd</summary>

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
  "draft_tokens": 2,
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
| [result-1c9d4043e68155eaa4e3](../observations.json)<br>source-e55a92a1742e783d94e9e8c3.json<br>`/experiments/2/speed/1` | [flash_next-mtp2-original-layer_split](flash_next-mtp2-original-layer_split.md) | performance detail | Outcome unspecified | cold_TTFT_median_seconds=147.64 s; configured_slots=6 requests; output_tokens=256 tokens; p50_inter_token_ms=38.78 ms; p95_inter_token_ms=115.09 ms; prompt_tokens=32,770 tokens; Draft accepted / proposed: 920 / 1,232 tokens; fraction 0.7468 | Exact configuration unresolved |
| [result-3277f0f26edf78954522](../observations.json)<br>source-e55a92a1742e783d94e9e8c3.json<br>`/experiments/2/speed/0` | [flash_next-mtp2-original-layer_split](flash_next-mtp2-original-layer_split.md) | performance detail | Outcome unspecified | cold_TTFT_median_seconds=24.59 s; configured_slots=6 requests; output_tokens=256 tokens; p50_inter_token_ms=11.58 ms; p95_inter_token_ms=33.08 ms; prompt_tokens=32,769 tokens; Draft accepted / proposed: 158 / 196 tokens; fraction 0.8061 | Exact configuration unresolved |
| [result-3518d0d242abc44abbe3](../observations.json)<br>source-e55a92a1742e783d94e9e8c3.json<br>`/experiments/2/speed/1/backend_prefill/4` | [flash_next-mtp2-original-layer_split](flash_next-mtp2-original-layer_split.md) | test outcome | Outcome unspecified | backend_prefill_seconds=143.49 s; cached_prompt_tokens=0 tokens; prefill_tok_s=228.38 tokens/s; processed_prompt_tokens=32,770 tokens | Exact configuration unresolved |
| [result-37f302a7fb8be4235f22](../observations.json)<br>source-e55a92a1742e783d94e9e8c3.json<br>`/experiments/2/speed/1/backend_prefill/5` | [flash_next-mtp2-original-layer_split](flash_next-mtp2-original-layer_split.md) | test outcome | Outcome unspecified | backend_prefill_seconds=141.43 s; cached_prompt_tokens=0 tokens; prefill_tok_s=231.70 tokens/s; processed_prompt_tokens=32,770 tokens | Exact configuration unresolved |
| [result-457cfa441f33391792ce](../observations.json)<br>source-e55a92a1742e783d94e9e8c3.json<br>`/experiments/2/speed/1/backend_prefill/0` | [flash_next-mtp2-original-layer_split](flash_next-mtp2-original-layer_split.md) | test outcome | Outcome unspecified | backend_prefill_seconds=141.36 s; cached_prompt_tokens=0 tokens; prefill_tok_s=231.82 tokens/s; processed_prompt_tokens=32,770 tokens | Exact configuration unresolved |
| [result-85a131aa29913d5eb6dc](../observations.json)<br>source-e55a92a1742e783d94e9e8c3.json<br>`/experiments/2` | [flash_next-mtp2-original-layer_split](flash_next-mtp2-original-layer_split.md) | context allocation | Outcome unspecified | matched_workload_host_peak_bytes=63,978,024,960 bytes; per_card_peak_used_MiB_unordered=43,492.00<br>61,316.00 | Exact configuration unresolved |
| [result-a2692c977bcd7a3d0d42](../observations.json)<br>source-e55a92a1742e783d94e9e8c3.json<br>`/experiments/2/speed/1/backend_prefill/2` | [flash_next-mtp2-original-layer_split](flash_next-mtp2-original-layer_split.md) | test outcome | Outcome unspecified | backend_prefill_seconds=144.81 s; cached_prompt_tokens=0 tokens; prefill_tok_s=226.30 tokens/s; processed_prompt_tokens=32,770 tokens | Exact configuration unresolved |
| [result-bcda86a133d45e399461](../observations.json)<br>source-2994c2194374f64151c130af.json<br>`/` | [flash_next-mtp2-original-layer_split](flash_next-mtp2-original-layer_split.md) | correctness check | Pass | 4 response usage/timing records | Exact configuration unresolved |
| [result-c048349c06369952bc50](../observations.json)<br>source-a9e622d351a86c8b776605d4.json<br>`/experiments/3` | [flash_next-mtp2-original-layer_split](flash_next-mtp2-original-layer_split.md) | context allocation | Outcome unspecified | matched_workload_host_peak_bytes=63,978,024,960 bytes; per_card_peak_used_MiB_unordered=43,492.00<br>61,316.00 | Exact configuration unresolved |
| [result-c2c5ecc41154dbb3d726](../observations.json)<br>source-697be02520d77b7a1029f323.json<br>`/variants/1` | [flash_next-mtp2-original-layer_split](flash_next-mtp2-original-layer_split.md) | test outcome | Outcome unspecified | host_cgroup_peak_bytes=63,978,024,960 bytes | Exact configuration unresolved |
| [result-db2df47fad1c22ba537a](../observations.json)<br>source-e55a92a1742e783d94e9e8c3.json<br>`/experiments/2/speed/0/backend_prefill/0` | [flash_next-mtp2-original-layer_split](flash_next-mtp2-original-layer_split.md)<br>[flash_next-mtp3-original-layer_split](flash_next-mtp3-original-layer_split.md) | test outcome | Outcome unspecified | backend_prefill_seconds=24.50 s; cached_prompt_tokens=0 tokens; prefill_tok_s=1,337.51 tokens/s; processed_prompt_tokens=32,769 tokens | Exact configuration unresolved |
| [result-e8a8f42a3c1c256d003e](../observations.json)<br>source-e55a92a1742e783d94e9e8c3.json<br>`/experiments/2/speed/1/backend_prefill/1` | [flash_next-mtp2-original-layer_split](flash_next-mtp2-original-layer_split.md) | test outcome | Outcome unspecified | backend_prefill_seconds=145.20 s; cached_prompt_tokens=0 tokens; prefill_tok_s=225.69 tokens/s; processed_prompt_tokens=32,770 tokens | Exact configuration unresolved |
| [result-f52612d07c948554d071](../observations.json)<br>source-e55a92a1742e783d94e9e8c3.json<br>`/experiments/2/speed/1/backend_prefill/3` | [flash_next-mtp2-original-layer_split](flash_next-mtp2-original-layer_split.md) | test outcome | Outcome unspecified | backend_prefill_seconds=143.88 s; cached_prompt_tokens=0 tokens; prefill_tok_s=227.76 tokens/s; processed_prompt_tokens=32,770 tokens | Exact configuration unresolved |

These are saved result records, including failures and bounded checks. Copies, individual requests, report summaries and regrading can overlap; their counts are not independent test repetitions. Open each result for exact values, units, configuration binding and source receipts.

[Full archive](../../README.md) | [All retained waves](../RESULTS.md) | [Data definitions](../DATA.md) | [Recommended recipes](../../../README.md)
