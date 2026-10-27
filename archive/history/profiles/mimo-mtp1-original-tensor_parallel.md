# mimo-mtp1-original-tensor_parallel

**Historical record. Additional test results; no matched decode wave.**

Model family: MiMo V2.6 Flash.

The campaign inventory recorded status `completed`. The evidence sections retain any later results separately.

Historical configurations are provided for comparison. The [recommended recipes](../../../README.md) include supported launch scripts.

Current recipes using the same recorded checkpoint repository: [mimo-flash-mtp1-tp3](../../../recipes/mimo-flash-mtp1-tp3/README.md). Context, cache and runtime versions can differ.

## Saved Configuration Versions

Each configuration ID identifies a distinct original settings record. Deployment fields are omitted; versions can have identical published settings after that omission. Upstream runtime commits remain unspecified where the source retained only an integration label.

| Configuration | Recorded artifact / source | Configured card counts | Context tokens | GPU pool tokens | Slots | Draft mode / tokens |
| --- | --- | --- | --- | --- | --- | --- |
| cfg-9d0d203a92e0b0c2fcbe | [MikeRoz/MiMo-V2.6-Flash-MOPD-4.03bpw-h8-exl3@29c8351a8b](https://huggingface.co/MikeRoz/MiMo-V2.6-Flash-MOPD-4.03bpw-h8-exl3/tree/29c8351a8b5854ec385adaeba7bbe62c790d40ea) | 3 | 262,144 | 262,144 | 4 | mtp / 1 |

Card counts are saved configuration choices, not a claim that every allowed placement was measured. A derived view can differ from its pinned download source.

<details>
<summary>cfg-9d0d203a92e0b0c2fcbe</summary>

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
  "parallelism": "tensor_parallel",
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
| [result-087e7b3bfc5a7790a7f2](../observations.json)<br>source-e55a92a1742e783d94e9e8c3.json<br>`/experiments/6/speed/1/backend_prefill/1` | [mimo-mtp1-original-tensor_parallel](mimo-mtp1-original-tensor_parallel.md) | test outcome | Outcome unspecified | backend_prefill_seconds=9.16 s; cached_prompt_tokens=0 tokens; prefill_tok_s=222.60 tokens/s; processed_prompt_tokens=2,039 tokens | Exact configuration unresolved |
| [result-11a1851db734cc94eb1c](../observations.json)<br>source-e55a92a1742e783d94e9e8c3.json<br>`/experiments/6/speed/1/backend_prefill/3` | [mimo-mtp1-original-tensor_parallel](mimo-mtp1-original-tensor_parallel.md) | test outcome | Outcome unspecified | backend_prefill_seconds=7.26 s; cached_prompt_tokens=0 tokens; prefill_tok_s=280.85 tokens/s; processed_prompt_tokens=2,039 tokens | Exact configuration unresolved |
| [result-126957d5318633a7f418](../observations.json)<br>source-e55a92a1742e783d94e9e8c3.json<br>`/experiments/6/independently_maximized_config` | [mimo-mtp1-original-tensor_parallel](mimo-mtp1-original-tensor_parallel.md) | context allocation | Outcome unspecified | cache_tokens=1,070,848 tokens; context=524,288 tokens; reserve_mib=4,096 MiB | Exact configuration unresolved |
| [result-1c51ee086b66c873919a](../observations.json)<br>source-94b07b24e27af4961cf45d26.json<br>`/correctness` | [mimo-mtp1-original-tensor_parallel](mimo-mtp1-original-tensor_parallel.md) | correctness check | Pass | 4 response usage/timing records | Exact configuration unresolved |
| [result-200319d93c95d1e38b7d](../observations.json)<br>source-e55a92a1742e783d94e9e8c3.json<br>`/experiments/6/speed/0` | [mimo-mtp1-original-tensor_parallel](mimo-mtp1-original-tensor_parallel.md) | performance detail | Outcome unspecified | cold_TTFT_median_seconds=5.50 s; configured_slots=4 requests; output_tokens=512 tokens; p50_inter_token_ms=17.19 ms; p95_inter_token_ms=32.20 ms; prompt_tokens=2,038 tokens; Draft accepted / proposed: 238 / 274 tokens; fraction 0.8686 | Exact configuration unresolved |
| [result-3c4eff1058a42c2a113e](../observations.json)<br>source-e55a92a1742e783d94e9e8c3.json<br>`/experiments/6/speed/3/backend_prefill/1` | [mimo-mtp1-original-tensor_parallel](mimo-mtp1-original-tensor_parallel.md) | test outcome | Outcome unspecified | backend_prefill_seconds=193.98 s; cached_prompt_tokens=0 tokens; prefill_tok_s=168.91 tokens/s; processed_prompt_tokens=32,766 tokens | Exact configuration unresolved |
| [result-507f56fc1201009c15ed](../observations.json)<br>source-e55a92a1742e783d94e9e8c3.json<br>`/experiments/6/speed/1/backend_prefill/0` | [mimo-mtp1-original-tensor_parallel](mimo-mtp1-original-tensor_parallel.md) | test outcome | Outcome unspecified | backend_prefill_seconds=4.73 s; cached_prompt_tokens=0 tokens; prefill_tok_s=431.08 tokens/s; processed_prompt_tokens=2,039 tokens | Exact configuration unresolved |
| [result-757ec68cfb25f93bbc26](../observations.json)<br>source-e55a92a1742e783d94e9e8c3.json<br>`/experiments/6/speed/3` | [mimo-mtp1-original-tensor_parallel](mimo-mtp1-original-tensor_parallel.md) | performance detail | Outcome unspecified | cold_TTFT_median_seconds=197.79 s; configured_slots=4 requests; output_tokens=512 tokens; p50_inter_token_ms=42.07 ms; p95_inter_token_ms=81.29 ms; prompt_tokens=32,766 tokens; Draft accepted / proposed: 890 / 1,158 tokens; fraction 0.7686 | Exact configuration unresolved |
| [result-7cda9029a60d11844d6e](../observations.json)<br>source-e55a92a1742e783d94e9e8c3.json<br>`/experiments/6/speed/3/backend_prefill/2` | [mimo-mtp1-original-tensor_parallel](mimo-mtp1-original-tensor_parallel.md) | test outcome | Outcome unspecified | backend_prefill_seconds=192.79 s; cached_prompt_tokens=0 tokens; prefill_tok_s=169.96 tokens/s; processed_prompt_tokens=32,766 tokens | Exact configuration unresolved |
| [result-84847c9be042b64bb2f9](../observations.json)<br>source-e55a92a1742e783d94e9e8c3.json<br>`/experiments/6` | [mimo-mtp1-original-tensor_parallel](mimo-mtp1-original-tensor_parallel.md) | context allocation | completed | matched_workload_host_peak_bytes=85,144,363,008 bytes; planning_reserve_mib=4,096 MiB; resident_pool_tokens=1,070,848 tokens; per_card_peak_used_MiB_unordered=53,674.00<br>54,235.00<br>54,869.00; capacity_boundary_measured=false; peak_prefill_and_concurrency_passed=false | Exact configuration unresolved |
| [result-894cf04fd879cfe1da91](../observations.json)<br>source-a9e622d351a86c8b776605d4.json<br>`/experiments/8` | [mimo-mtp1-original-tensor_parallel](mimo-mtp1-original-tensor_parallel.md) | context allocation | Outcome unspecified | matched_workload_host_peak_bytes=85,144,363,008 bytes; per_card_peak_used_MiB_unordered=53,674.00<br>54,235.00<br>54,869.00 | Exact configuration unresolved |
| [result-98e77275c17511914a74](../observations.json)<br>source-e55a92a1742e783d94e9e8c3.json<br>`/experiments/6/speed/1` | [mimo-mtp1-original-tensor_parallel](mimo-mtp1-original-tensor_parallel.md) | performance detail | Outcome unspecified | cold_TTFT_median_seconds=13.59 s; configured_slots=4 requests; output_tokens=512 tokens; p50_inter_token_ms=29.02 ms; p95_inter_token_ms=56.98 ms; prompt_tokens=2,039 tokens; Draft accepted / proposed: 917 / 1,131 tokens; fraction 0.8108 | Exact configuration unresolved |
| [result-d3d31fddbdd253f3b3fe](../observations.json)<br>source-e55a92a1742e783d94e9e8c3.json<br>`/experiments/6/speed/2` | [mimo-mtp1-original-tensor_parallel](mimo-mtp1-original-tensor_parallel.md) | performance detail | Outcome unspecified | cold_TTFT_median_seconds=52.83 s; configured_slots=4 requests; output_tokens=512 tokens; p50_inter_token_ms=19.37 ms; p95_inter_token_ms=35.57 ms; prompt_tokens=32,765 tokens; Draft accepted / proposed: 236 / 276 tokens; fraction 0.8551 | Exact configuration unresolved |
| [result-d553c5f0610724a340c9](../observations.json)<br>source-e55a92a1742e783d94e9e8c3.json<br>`/experiments/6/speed/0/backend_prefill/0` | [mimo-mtp1-original-tensor_parallel](mimo-mtp1-original-tensor_parallel.md) | test outcome | Outcome unspecified | backend_prefill_seconds=5.45 s; cached_prompt_tokens=0 tokens; prefill_tok_s=373.94 tokens/s; processed_prompt_tokens=2,038 tokens | Exact configuration unresolved |
| [result-dec6f6c8890eb96918af](../observations.json)<br>source-e55a92a1742e783d94e9e8c3.json<br>`/experiments/6/speed/1/backend_prefill/2` | [mimo-mtp1-original-tensor_parallel](mimo-mtp1-original-tensor_parallel.md) | test outcome | Outcome unspecified | backend_prefill_seconds=8.39 s; cached_prompt_tokens=0 tokens; prefill_tok_s=243.03 tokens/s; processed_prompt_tokens=2,039 tokens | Exact configuration unresolved |
| [result-e0b39c4e112508d30081](../observations.json)<br>source-e55a92a1742e783d94e9e8c3.json<br>`/experiments/6/speed/3/backend_prefill/3` | [mimo-mtp1-original-tensor_parallel](mimo-mtp1-original-tensor_parallel.md) | test outcome | Outcome unspecified | backend_prefill_seconds=192.03 s; cached_prompt_tokens=0 tokens; prefill_tok_s=170.63 tokens/s; processed_prompt_tokens=32,766 tokens | Exact configuration unresolved |
| [result-e2bfd3b6ad4d732b86e6](../observations.json)<br>source-e55a92a1742e783d94e9e8c3.json<br>`/experiments/6/speed/2/backend_prefill/0` | [mimo-mtp1-original-tensor_parallel](mimo-mtp1-original-tensor_parallel.md) | test outcome | Outcome unspecified | backend_prefill_seconds=52.71 s; cached_prompt_tokens=0 tokens; prefill_tok_s=621.61 tokens/s; processed_prompt_tokens=32,765 tokens | Exact configuration unresolved |
| [result-f2f13fbdfa1500ce9a2c](../observations.json)<br>source-e55a92a1742e783d94e9e8c3.json<br>`/experiments/6/contexts/0` | [mimo-mtp1-original-tensor_parallel](mimo-mtp1-original-tensor_parallel.md) | context allocation | Outcome unspecified | context_tokens=524,288 tokens | Exact configuration unresolved |
| [result-ffdb1a51dcc29b265b68](../observations.json)<br>source-e55a92a1742e783d94e9e8c3.json<br>`/experiments/6/speed/3/backend_prefill/0` | [mimo-mtp1-original-tensor_parallel](mimo-mtp1-original-tensor_parallel.md) | test outcome | Outcome unspecified | backend_prefill_seconds=191.04 s; cached_prompt_tokens=0 tokens; prefill_tok_s=171.51 tokens/s; processed_prompt_tokens=32,766 tokens | Exact configuration unresolved |

These are saved result records, including failures and bounded checks. Copies, individual requests, report summaries and regrading can overlap; their counts are not independent test repetitions. Open each result for exact values, units, configuration binding and source receipts.

[Full archive](../../README.md) | [All retained waves](../RESULTS.md) | [Data definitions](../DATA.md) | [Recommended recipes](../../../README.md)
