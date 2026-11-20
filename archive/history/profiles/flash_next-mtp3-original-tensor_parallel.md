# flash_next-mtp3-original-tensor_parallel

**Historical record. Additional test results; no matched decode wave.**

Model family: Qwen 3.8 Flash Next.

The campaign inventory recorded status `completed`. The evidence sections retain any later results separately.

Historical configurations are provided for comparison. The [recommended recipes](../../../README.md) include supported launch scripts.

Current recipes using the same recorded checkpoint repository: [qwen-flash-next-mtp2-layer-split](../../../recipes/qwen-flash-next-mtp2-layer-split/README.md). Context, cache and runtime versions can differ.

## Saved Configuration Versions

Each configuration ID identifies a distinct original settings record. Deployment fields are omitted; versions can have identical published settings after that omission. Upstream runtime commits remain unspecified where the source retained only an integration label.

| Configuration | Recorded artifact / source | Configured card counts | Context tokens | GPU pool tokens | Slots | Draft mode / tokens |
| --- | --- | --- | --- | --- | --- | --- |
| cfg-7c59f75f8da1cc8ef3de | [turboderp/Qwen3.8-Flash-Next-exl3@d2e238feca](https://huggingface.co/turboderp/Qwen3.8-Flash-Next-exl3/tree/d2e238feca4c1c4d966943117356d8a42c2f4dcb) | 2 | 262,144 | 262,144 | 6 | mtp / 3 |

Card counts are saved configuration choices, not a claim that every allowed placement was measured. A derived view can differ from its pinned download source.

<details>
<summary>cfg-7c59f75f8da1cc8ef3de</summary>

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
  "parallelism": "tensor_parallel",
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
| [result-032760a02af6247ab236](../observations.json)<br>source-e55a92a1742e783d94e9e8c3.json<br>`/experiments/4/speed/1/backend_prefill/3` | [flash_next-mtp3-original-tensor_parallel](flash_next-mtp3-original-tensor_parallel.md) | test outcome | Outcome unspecified | backend_prefill_seconds=215.11 s; cached_prompt_tokens=0 tokens; prefill_tok_s=152.34 tokens/s; processed_prompt_tokens=32,770 tokens | Exact configuration unresolved |
| [result-099a29fdb246ef354f41](../observations.json)<br>source-e55a92a1742e783d94e9e8c3.json<br>`/experiments/4/speed/1` | [flash_next-mtp3-original-tensor_parallel](flash_next-mtp3-original-tensor_parallel.md) | performance detail | Outcome unspecified | cold_TTFT_median_seconds=219.55 s; configured_slots=6 requests; output_tokens=256 tokens; p50_inter_token_ms=39.36 ms; p95_inter_token_ms=126.28 ms; prompt_tokens=32,770 tokens; Draft accepted / proposed: 1,014 / 1,566 tokens; fraction 0.6475 | Exact configuration unresolved |
| [result-2099090b614b8388296b](../observations.json)<br>source-e55a92a1742e783d94e9e8c3.json<br>`/experiments/4/speed/1/backend_prefill/1` | [flash_next-mtp3-original-tensor_parallel](flash_next-mtp3-original-tensor_parallel.md) | test outcome | Outcome unspecified | backend_prefill_seconds=216.00 s; cached_prompt_tokens=0 tokens; prefill_tok_s=151.71 tokens/s; processed_prompt_tokens=32,770 tokens | Exact configuration unresolved |
| [result-2b51c2dc90b5f950926f](../observations.json)<br>source-e55a92a1742e783d94e9e8c3.json<br>`/experiments/4` | [flash_next-mtp3-original-tensor_parallel](flash_next-mtp3-original-tensor_parallel.md) | context allocation | completed | matched_workload_host_peak_bytes=71,804,846,080 bytes; planning_reserve_mib=2,048 MiB; resident_pool_tokens=1,143,296 tokens; per_card_peak_used_MiB_unordered=54,879.00<br>54,961.00; capacity_boundary_measured=false; peak_prefill_and_concurrency_passed=false | Exact configuration unresolved |
| [result-2d72f3a19e5bb6d1d805](../observations.json)<br>source-e55a92a1742e783d94e9e8c3.json<br>`/experiments/4/contexts/0` | [flash_next-mtp3-original-tensor_parallel](flash_next-mtp3-original-tensor_parallel.md) | context allocation | Outcome unspecified | context_tokens=524,288 tokens | Exact configuration unresolved |
| [result-3e1055d85f543096e0eb](../observations.json)<br>source-a9e622d351a86c8b776605d4.json<br>`/experiments/6` | [flash_next-mtp3-original-tensor_parallel](flash_next-mtp3-original-tensor_parallel.md) | context allocation | Outcome unspecified | matched_workload_host_peak_bytes=71,804,846,080 bytes; per_card_peak_used_MiB_unordered=54,879.00<br>54,961.00 | Exact configuration unresolved |
| [result-505b4c32b2dd5c1600e4](../observations.json)<br>source-e55a92a1742e783d94e9e8c3.json<br>`/experiments/4/speed/0` | [flash_next-mtp3-original-tensor_parallel](flash_next-mtp3-original-tensor_parallel.md) | performance detail | Outcome unspecified | cold_TTFT_median_seconds=36.46 s; configured_slots=6 requests; output_tokens=256 tokens; p50_inter_token_ms=10.34 ms; p95_inter_token_ms=39.89 ms; prompt_tokens=32,769 tokens; Draft accepted / proposed: 171 / 255 tokens; fraction 0.6706 | Exact configuration unresolved |
| [result-5ac256d69f24485a9c88](../observations.json)<br>source-e55a92a1742e783d94e9e8c3.json<br>`/experiments/4/speed/1/backend_prefill/2` | [flash_next-mtp3-original-tensor_parallel](flash_next-mtp3-original-tensor_parallel.md) | test outcome | Outcome unspecified | backend_prefill_seconds=215.66 s; cached_prompt_tokens=0 tokens; prefill_tok_s=151.95 tokens/s; processed_prompt_tokens=32,770 tokens | Exact configuration unresolved |
| [result-a76a427900cda6016127](../observations.json)<br>source-e55a92a1742e783d94e9e8c3.json<br>`/experiments/4/speed/1/backend_prefill/5` | [flash_next-mtp3-original-tensor_parallel](flash_next-mtp3-original-tensor_parallel.md) | test outcome | Outcome unspecified | backend_prefill_seconds=211.94 s; cached_prompt_tokens=0 tokens; prefill_tok_s=154.62 tokens/s; processed_prompt_tokens=32,770 tokens | Exact configuration unresolved |
| [result-a76f5e3367977342481f](../observations.json)<br>source-e55a92a1742e783d94e9e8c3.json<br>`/experiments/4/speed/1/backend_prefill/0` | [flash_next-mtp3-original-tensor_parallel](flash_next-mtp3-original-tensor_parallel.md) | test outcome | Outcome unspecified | backend_prefill_seconds=212.34 s; cached_prompt_tokens=0 tokens; prefill_tok_s=154.33 tokens/s; processed_prompt_tokens=32,770 tokens | Exact configuration unresolved |
| [result-bbdebd8a0e796f960b13](../observations.json)<br>source-e55a92a1742e783d94e9e8c3.json<br>`/experiments/4/independently_maximized_config` | [flash_next-mtp3-original-tensor_parallel](flash_next-mtp3-original-tensor_parallel.md) | context allocation | Outcome unspecified | cache_tokens=1,143,296 tokens; context=524,288 tokens; reserve_mib=2,048 MiB | Exact configuration unresolved |
| [result-d04d5f4b2aaf4fa50309](../observations.json)<br>source-e9709fe18fa406dbba87624f.json<br>`/correctness` | [flash_next-mtp3-original-tensor_parallel](flash_next-mtp3-original-tensor_parallel.md) | correctness check | Pass | 4 response usage/timing records | Exact configuration unresolved |
| [result-e31121ae74276909b440](../observations.json)<br>source-e55a92a1742e783d94e9e8c3.json<br>`/experiments/4/speed/0/backend_prefill/0` | [flash_next-mtp3-original-tensor_parallel](flash_next-mtp3-original-tensor_parallel.md) | test outcome | Outcome unspecified | backend_prefill_seconds=36.36 s; cached_prompt_tokens=0 tokens; prefill_tok_s=901.24 tokens/s; processed_prompt_tokens=32,769 tokens | Exact configuration unresolved |
| [result-f962d37ef7cc20cdef62](../observations.json)<br>source-e55a92a1742e783d94e9e8c3.json<br>`/experiments/4/speed/1/backend_prefill/4` | [flash_next-mtp3-original-tensor_parallel](flash_next-mtp3-original-tensor_parallel.md) | test outcome | Outcome unspecified | backend_prefill_seconds=212.49 s; cached_prompt_tokens=0 tokens; prefill_tok_s=154.22 tokens/s; processed_prompt_tokens=32,770 tokens | Exact configuration unresolved |

These are saved result records, including failures and bounded checks. Copies, individual requests, report summaries and regrading can overlap; their counts are not independent test repetitions. Open each result for exact values, units, configuration binding and source receipts.

[Full archive](../../README.md) | [All retained waves](../RESULTS.md) | [Data definitions](../DATA.md) | [Recommended recipes](../../../README.md)
