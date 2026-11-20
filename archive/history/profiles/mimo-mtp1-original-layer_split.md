# mimo-mtp1-original-layer_split

**Historical record. Additional test results; no matched decode wave.**

Model family: MiMo V2.6 Flash.

The campaign inventory recorded status `speed_measured_capacity_pending`. The evidence sections retain any later results separately.

Historical configurations are provided for comparison. The [recommended recipes](../../../README.md) include supported launch scripts.

Current recipes using the same recorded checkpoint repository: [mimo-flash-mtp1-tp3](../../../recipes/mimo-flash-mtp1-tp3/README.md). Context, cache and runtime versions can differ.

## Saved Configuration Versions

Each configuration ID identifies a distinct original settings record. Deployment fields are omitted; versions can have identical published settings after that omission. Upstream runtime commits remain unspecified where the source retained only an integration label.

| Configuration | Recorded artifact / source | Configured card counts | Context tokens | GPU pool tokens | Slots | Draft mode / tokens |
| --- | --- | --- | --- | --- | --- | --- |
| cfg-5c7d162a53b4f9641b0e | [MikeRoz/MiMo-V2.6-Flash-MOPD-4.03bpw-h8-exl3@29c8351a8b](https://huggingface.co/MikeRoz/MiMo-V2.6-Flash-MOPD-4.03bpw-h8-exl3/tree/29c8351a8b5854ec385adaeba7bbe62c790d40ea) | 3 | 262,144 | 262,144 | 4 | mtp / 1 |

Card counts are saved configuration choices, not a claim that every allowed placement was measured. A derived view can differ from its pinned download source.

<details>
<summary>cfg-5c7d162a53b4f9641b0e</summary>

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
| [result-1128d0f63c6f5cf5a362](../observations.json)<br>source-e55a92a1742e783d94e9e8c3.json<br>`/experiments/5/speed/1/backend_prefill/1` | [mimo-mtp1-original-layer_split](mimo-mtp1-original-layer_split.md) | test outcome | Outcome unspecified | backend_prefill_seconds=7.58 s; cached_prompt_tokens=0 tokens; prefill_tok_s=269.00 tokens/s; processed_prompt_tokens=2,039 tokens | Exact configuration unresolved |
| [result-31a4e1baf59cd5de4f6e](../observations.json)<br>source-e55a92a1742e783d94e9e8c3.json<br>`/experiments/5/speed/2/backend_prefill/0` | [mimo-mtp1-original-layer_split](mimo-mtp1-original-layer_split.md) | test outcome | Outcome unspecified | backend_prefill_seconds=41.68 s; cached_prompt_tokens=0 tokens; prefill_tok_s=786.11 tokens/s; processed_prompt_tokens=32,765 tokens | Exact configuration unresolved |
| [result-469a9200953ff0131d0f](../observations.json)<br>source-a9e622d351a86c8b776605d4.json<br>`/experiments/7` | [mimo-mtp1-original-layer_split](mimo-mtp1-original-layer_split.md) | context allocation | Outcome unspecified | matched_workload_host_peak_bytes=50,315,542,528 bytes; per_card_peak_used_MiB_unordered=40,950.00<br>61,984.00<br>62,572.00 | Exact configuration unresolved |
| [result-5cfb5f5020d8d1c24695](../observations.json)<br>source-e55a92a1742e783d94e9e8c3.json<br>`/experiments/5/speed/1/backend_prefill/2` | [mimo-mtp1-original-layer_split](mimo-mtp1-original-layer_split.md) | test outcome | Outcome unspecified | backend_prefill_seconds=6.88 s; cached_prompt_tokens=0 tokens; prefill_tok_s=296.37 tokens/s; processed_prompt_tokens=2,039 tokens | Exact configuration unresolved |
| [result-5e9ce53c80bc4be89e40](../observations.json)<br>source-e55a92a1742e783d94e9e8c3.json<br>`/experiments/5/speed/3/backend_prefill/1` | [mimo-mtp1-original-layer_split](mimo-mtp1-original-layer_split.md) | test outcome | Outcome unspecified | backend_prefill_seconds=163.09 s; cached_prompt_tokens=0 tokens; prefill_tok_s=200.91 tokens/s; processed_prompt_tokens=32,766 tokens | Exact configuration unresolved |
| [result-60f7af747a8f0e052516](../observations.json)<br>source-e55a92a1742e783d94e9e8c3.json<br>`/experiments/5/speed/0/backend_prefill/0` | [mimo-mtp1-original-layer_split](mimo-mtp1-original-layer_split.md) | test outcome | Outcome unspecified | backend_prefill_seconds=2.76 s; cached_prompt_tokens=0 tokens; prefill_tok_s=738.41 tokens/s; processed_prompt_tokens=2,038 tokens | Exact configuration unresolved |
| [result-7e3c8e9ba146a3eb9422](../observations.json)<br>source-e55a92a1742e783d94e9e8c3.json<br>`/experiments/5/speed/2` | [mimo-mtp1-original-layer_split](mimo-mtp1-original-layer_split.md) | performance detail | Outcome unspecified | cold_TTFT_median_seconds=41.80 s; configured_slots=4 requests; output_tokens=512 tokens; p50_inter_token_ms=27.55 ms; p95_inter_token_ms=51.74 ms; prompt_tokens=32,765 tokens; Draft accepted / proposed: 218 / 294 tokens; fraction 0.7415 | Exact configuration unresolved |
| [result-8765fe3a7e686687d33b](../observations.json)<br>source-e55a92a1742e783d94e9e8c3.json<br>`/experiments/5/speed/3/backend_prefill/0` | [mimo-mtp1-original-layer_split](mimo-mtp1-original-layer_split.md) | test outcome | Outcome unspecified | backend_prefill_seconds=158.45 s; cached_prompt_tokens=0 tokens; prefill_tok_s=206.79 tokens/s; processed_prompt_tokens=32,766 tokens | Exact configuration unresolved |
| [result-b3f38e8e3abe5e2f7cae](../observations.json)<br>source-e55a92a1742e783d94e9e8c3.json<br>`/experiments/5/speed/3` | [mimo-mtp1-original-layer_split](mimo-mtp1-original-layer_split.md) | performance detail | Outcome unspecified | cold_TTFT_median_seconds=167.30 s; configured_slots=4 requests; output_tokens=512 tokens; p50_inter_token_ms=64.08 ms; p95_inter_token_ms=126.12 ms; prompt_tokens=32,766 tokens; Draft accepted / proposed: 874 / 1,174 tokens; fraction 0.7445 | Exact configuration unresolved |
| [result-bafc32385004c5fb57a9](../observations.json)<br>source-e55a92a1742e783d94e9e8c3.json<br>`/experiments/5/speed/1` | [mimo-mtp1-original-layer_split](mimo-mtp1-original-layer_split.md) | performance detail | Outcome unspecified | cold_TTFT_median_seconds=10.93 s; configured_slots=4 requests; output_tokens=512 tokens; p50_inter_token_ms=45.46 ms; p95_inter_token_ms=89.34 ms; prompt_tokens=2,039 tokens; Draft accepted / proposed: 902 / 1,146 tokens; fraction 0.7871 | Exact configuration unresolved |
| [result-c4d38c4bebc85e3a4dc7](../observations.json)<br>source-e55a92a1742e783d94e9e8c3.json<br>`/experiments/5/speed/0` | [mimo-mtp1-original-layer_split](mimo-mtp1-original-layer_split.md) | performance detail | Outcome unspecified | cold_TTFT_median_seconds=2.80 s; configured_slots=4 requests; output_tokens=512 tokens; p50_inter_token_ms=21.95 ms; p95_inter_token_ms=42.42 ms; prompt_tokens=2,038 tokens; Draft accepted / proposed: 219 / 293 tokens; fraction 0.7474 | Exact configuration unresolved |
| [result-dd00f345c3ad81e8a059](../observations.json)<br>source-e55a92a1742e783d94e9e8c3.json<br>`/experiments/5/speed/3/backend_prefill/3` | [mimo-mtp1-original-layer_split](mimo-mtp1-original-layer_split.md) | test outcome | Outcome unspecified | backend_prefill_seconds=160.82 s; cached_prompt_tokens=0 tokens; prefill_tok_s=203.74 tokens/s; processed_prompt_tokens=32,766 tokens | Exact configuration unresolved |
| [result-e1325b5ed479192f3f7b](../observations.json)<br>source-e55a92a1742e783d94e9e8c3.json<br>`/experiments/5/speed/1/backend_prefill/0` | [mimo-mtp1-original-layer_split](mimo-mtp1-original-layer_split.md) | test outcome | Outcome unspecified | backend_prefill_seconds=5.20 s; cached_prompt_tokens=0 tokens; prefill_tok_s=392.12 tokens/s; processed_prompt_tokens=2,039 tokens | Exact configuration unresolved |
| [result-e43ac473e23587088184](../observations.json)<br>source-e55a92a1742e783d94e9e8c3.json<br>`/experiments/5/speed/3/backend_prefill/2` | [mimo-mtp1-original-layer_split](mimo-mtp1-original-layer_split.md) | test outcome | Outcome unspecified | backend_prefill_seconds=162.46 s; cached_prompt_tokens=0 tokens; prefill_tok_s=201.69 tokens/s; processed_prompt_tokens=32,766 tokens | Exact configuration unresolved |
| [result-e4a7dda172146e1956d1](../observations.json)<br>source-e55a92a1742e783d94e9e8c3.json<br>`/experiments/5/speed/1/backend_prefill/3` | [mimo-mtp1-original-layer_split](mimo-mtp1-original-layer_split.md) | test outcome | Outcome unspecified | backend_prefill_seconds=6.26 s; cached_prompt_tokens=0 tokens; prefill_tok_s=325.72 tokens/s; processed_prompt_tokens=2,039 tokens | Exact configuration unresolved |
| [result-e9366b369fdcb0cd8f21](../observations.json)<br>source-1b13c797cc839e8d49b5c82d.json<br>`/` | [mimo-mtp1-original-layer_split](mimo-mtp1-original-layer_split.md) | correctness check | Pass | 4 response usage/timing records | Exact configuration unresolved |
| [result-f13fc888a86f7390a7ea](../observations.json)<br>source-e55a92a1742e783d94e9e8c3.json<br>`/experiments/5` | [mimo-mtp1-original-layer_split](mimo-mtp1-original-layer_split.md) | context allocation | Outcome unspecified | matched_workload_host_peak_bytes=50,315,542,528 bytes; per_card_peak_used_MiB_unordered=40,950.00<br>61,984.00<br>62,572.00 | Exact configuration unresolved |

These are saved result records, including failures and bounded checks. Copies, individual requests, report summaries and regrading can overlap; their counts are not independent test repetitions. Open each result for exact values, units, configuration binding and source receipts.

[Full archive](../../README.md) | [All retained waves](../RESULTS.md) | [Data definitions](../DATA.md) | [Recommended recipes](../../../README.md)
