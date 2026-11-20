# mimo-mtp3-original-layer_split

**Historical record. Additional test results; no matched decode wave.**

Model family: MiMo V2.6 Flash.

The campaign inventory recorded status `speed_measured_capacity_pending`. The evidence sections retain any later results separately.

Historical configurations are provided for comparison. The [recommended recipes](../../../README.md) include supported launch scripts.

Current recipes using the same recorded checkpoint repository: [mimo-flash-mtp1-tp3](../../../recipes/mimo-flash-mtp1-tp3/README.md). Context, cache and runtime versions can differ.

## Saved Configuration Versions

Each configuration ID identifies a distinct original settings record. Deployment fields are omitted; versions can have identical published settings after that omission. Upstream runtime commits remain unspecified where the source retained only an integration label.

| Configuration | Recorded artifact / source | Configured card counts | Context tokens | GPU pool tokens | Slots | Draft mode / tokens |
| --- | --- | --- | --- | --- | --- | --- |
| cfg-dbb2632a6db1ccc83d6c | [MikeRoz/MiMo-V2.6-Flash-MOPD-4.03bpw-h8-exl3@29c8351a8b](https://huggingface.co/MikeRoz/MiMo-V2.6-Flash-MOPD-4.03bpw-h8-exl3/tree/29c8351a8b5854ec385adaeba7bbe62c790d40ea) | 3 | 262,144 | 262,144 | 4 | mtp / 3 |

Card counts are saved configuration choices, not a claim that every allowed placement was measured. A derived view can differ from its pinned download source.

<details>
<summary>cfg-dbb2632a6db1ccc83d6c</summary>

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
| [result-08b10f4122906b907a4c](../observations.json)<br>source-e55a92a1742e783d94e9e8c3.json<br>`/experiments/8/speed/3/backend_prefill/2` | [mimo-mtp3-original-layer_split](mimo-mtp3-original-layer_split.md) | test outcome | Outcome unspecified | backend_prefill_seconds=163.28 s; cached_prompt_tokens=0 tokens; prefill_tok_s=200.67 tokens/s; processed_prompt_tokens=32,766 tokens | Exact configuration unresolved |
| [result-104842a17944a4a87de8](../observations.json)<br>source-e55a92a1742e783d94e9e8c3.json<br>`/experiments/8/speed/2` | [mimo-mtp3-original-layer_split](mimo-mtp3-original-layer_split.md) | performance detail | Outcome unspecified | cold_TTFT_median_seconds=41.95 s; configured_slots=4 requests; output_tokens=512 tokens; p50_inter_token_ms=27.42 ms; p95_inter_token_ms=76.03 ms; prompt_tokens=32,765 tokens; Draft accepted / proposed: 314 / 594 tokens; fraction 0.5286 | Exact configuration unresolved |
| [result-25e2073b7163dc578719](../observations.json)<br>source-29c9ca96e63e05f08bc3c742.json<br>`/` | [mimo-mtp3-original-layer_split](mimo-mtp3-original-layer_split.md) | correctness check | Pass | 4 response usage/timing records | Exact configuration unresolved |
| [result-4e42aa668e342e0d25f4](../observations.json)<br>source-e55a92a1742e783d94e9e8c3.json<br>`/experiments/8/speed/1/backend_prefill/3` | [mimo-mtp3-original-layer_split](mimo-mtp3-original-layer_split.md) | test outcome | Outcome unspecified | backend_prefill_seconds=6.40 s; cached_prompt_tokens=0 tokens; prefill_tok_s=318.59 tokens/s; processed_prompt_tokens=2,039 tokens | Exact configuration unresolved |
| [result-4eb764b38f2b050d33ea](../observations.json)<br>source-e55a92a1742e783d94e9e8c3.json<br>`/experiments/8/speed/2/backend_prefill/0` | [mimo-mtp3-original-layer_split](mimo-mtp3-original-layer_split.md) | test outcome | Outcome unspecified | backend_prefill_seconds=41.78 s; cached_prompt_tokens=0 tokens; prefill_tok_s=784.23 tokens/s; processed_prompt_tokens=32,765 tokens | Exact configuration unresolved |
| [result-51da5874d453bcb83b46](../observations.json)<br>source-e55a92a1742e783d94e9e8c3.json<br>`/experiments/8/speed/1/backend_prefill/1` | [mimo-mtp3-original-layer_split](mimo-mtp3-original-layer_split.md) | test outcome | Outcome unspecified | backend_prefill_seconds=7.66 s; cached_prompt_tokens=0 tokens; prefill_tok_s=266.19 tokens/s; processed_prompt_tokens=2,039 tokens | Exact configuration unresolved |
| [result-5b65e1325355c14b7aa1](../observations.json)<br>source-e55a92a1742e783d94e9e8c3.json<br>`/experiments/8/speed/3/backend_prefill/0` | [mimo-mtp3-original-layer_split](mimo-mtp3-original-layer_split.md) | test outcome | Outcome unspecified | backend_prefill_seconds=161.99 s; cached_prompt_tokens=0 tokens; prefill_tok_s=202.27 tokens/s; processed_prompt_tokens=32,766 tokens | Exact configuration unresolved |
| [result-60047d5acb98ba1af72c](../observations.json)<br>source-e55a92a1742e783d94e9e8c3.json<br>`/experiments/8/speed/1` | [mimo-mtp3-original-layer_split](mimo-mtp3-original-layer_split.md) | performance detail | Outcome unspecified | cold_TTFT_median_seconds=10.71 s; configured_slots=4 requests; output_tokens=512 tokens; p50_inter_token_ms=52.73 ms; p95_inter_token_ms=148.76 ms; prompt_tokens=2,039 tokens; Draft accepted / proposed: 1,265 / 2,349 tokens; fraction 0.5385 | Exact configuration unresolved |
| [result-7296d277ce31d4cd6f90](../observations.json)<br>source-e55a92a1742e783d94e9e8c3.json<br>`/experiments/8/speed/3/backend_prefill/1` | [mimo-mtp3-original-layer_split](mimo-mtp3-original-layer_split.md) | test outcome | Outcome unspecified | backend_prefill_seconds=163.66 s; cached_prompt_tokens=0 tokens; prefill_tok_s=200.21 tokens/s; processed_prompt_tokens=32,766 tokens | Exact configuration unresolved |
| [result-78664d91f35de6b9fb84](../observations.json)<br>source-e55a92a1742e783d94e9e8c3.json<br>`/experiments/8/speed/3` | [mimo-mtp3-original-layer_split](mimo-mtp3-original-layer_split.md) | performance detail | Outcome unspecified | cold_TTFT_median_seconds=167.54 s; configured_slots=4 requests; output_tokens=512 tokens; p50_inter_token_ms=106.86 ms; p95_inter_token_ms=245.34 ms; prompt_tokens=32,766 tokens; Draft accepted / proposed: 1,229 / 2,457 tokens; fraction 0.5002 | Exact configuration unresolved |
| [result-7ee6765eb715d0a34312](../observations.json)<br>source-e55a92a1742e783d94e9e8c3.json<br>`/experiments/8/speed/0/backend_prefill/0` | [mimo-mtp3-original-layer_split](mimo-mtp3-original-layer_split.md) | test outcome | Outcome unspecified | backend_prefill_seconds=2.69 s; cached_prompt_tokens=0 tokens; prefill_tok_s=757.62 tokens/s; processed_prompt_tokens=2,038 tokens | Exact configuration unresolved |
| [result-9cf2d1290378707cabc6](../observations.json)<br>source-e55a92a1742e783d94e9e8c3.json<br>`/experiments/8/speed/1/backend_prefill/2` | [mimo-mtp3-original-layer_split](mimo-mtp3-original-layer_split.md) | test outcome | Outcome unspecified | backend_prefill_seconds=7.01 s; cached_prompt_tokens=0 tokens; prefill_tok_s=290.87 tokens/s; processed_prompt_tokens=2,039 tokens | Exact configuration unresolved |
| [result-a3051d811eecc28626fb](../observations.json)<br>source-e55a92a1742e783d94e9e8c3.json<br>`/experiments/8` | [mimo-mtp3-original-layer_split](mimo-mtp3-original-layer_split.md) | context allocation | Outcome unspecified | matched_workload_host_peak_bytes=52,749,398,016 bytes; per_card_peak_used_MiB_unordered=40,950.00<br>60,608.00<br>61,984.00 | Exact configuration unresolved |
| [result-aa270576a120a80abf46](../observations.json)<br>source-a9e622d351a86c8b776605d4.json<br>`/experiments/11` | [mimo-mtp3-original-layer_split](mimo-mtp3-original-layer_split.md) | context allocation | Outcome unspecified | matched_workload_host_peak_bytes=52,749,398,016 bytes; per_card_peak_used_MiB_unordered=40,950.00<br>60,608.00<br>61,984.00 | Exact configuration unresolved |
| [result-d48b8e9cfded4bcb829c](../observations.json)<br>source-e55a92a1742e783d94e9e8c3.json<br>`/experiments/8/speed/3/backend_prefill/3` | [mimo-mtp3-original-layer_split](mimo-mtp3-original-layer_split.md) | test outcome | Outcome unspecified | backend_prefill_seconds=162.66 s; cached_prompt_tokens=0 tokens; prefill_tok_s=201.44 tokens/s; processed_prompt_tokens=32,766 tokens | Exact configuration unresolved |
| [result-e20b618d0e7d575200b7](../observations.json)<br>source-e55a92a1742e783d94e9e8c3.json<br>`/experiments/8/speed/0` | [mimo-mtp3-original-layer_split](mimo-mtp3-original-layer_split.md) | performance detail | Outcome unspecified | cold_TTFT_median_seconds=2.79 s; configured_slots=4 requests; output_tokens=512 tokens; p50_inter_token_ms=23.50 ms; p95_inter_token_ms=58.84 ms; prompt_tokens=2,038 tokens; Draft accepted / proposed: 306 / 618 tokens; fraction 0.4951 | Exact configuration unresolved |
| [result-e7f53ca222407a715df0](../observations.json)<br>source-e55a92a1742e783d94e9e8c3.json<br>`/experiments/8/speed/1/backend_prefill/0` | [mimo-mtp3-original-layer_split](mimo-mtp3-original-layer_split.md) | test outcome | Outcome unspecified | backend_prefill_seconds=5.24 s; cached_prompt_tokens=0 tokens; prefill_tok_s=389.12 tokens/s; processed_prompt_tokens=2,039 tokens | Exact configuration unresolved |

These are saved result records, including failures and bounded checks. Copies, individual requests, report summaries and regrading can overlap; their counts are not independent test repetitions. Open each result for exact values, units, configuration binding and source receipts.

[Full archive](../../README.md) | [All retained waves](../RESULTS.md) | [Data definitions](../DATA.md) | [Recommended recipes](../../../README.md)
