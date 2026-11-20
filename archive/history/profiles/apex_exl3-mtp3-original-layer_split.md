# apex_exl3-mtp3-original-layer_split

**Historical record. Additional test results; no matched decode wave.**

Model family: Apex Flash 1 (GLM 5.3 Flash post-train).

The campaign inventory recorded status `speed_measured_capacity_pending`. The evidence sections retain any later results separately.

Historical configurations are provided for comparison. The [recommended recipes](../../../README.md) include supported launch scripts.

Current recipes using the same recorded checkpoint repository: [apex-abliterated-exl3-mtp1-tp3](../../../recipes/apex-abliterated-exl3-mtp1-tp3/README.md). Context, cache and runtime versions can differ.

## Saved Configuration Versions

Each configuration ID identifies a distinct original settings record. Deployment fields are omitted; versions can have identical published settings after that omission. Upstream runtime commits remain unspecified where the source retained only an integration label.

| Configuration | Recorded artifact / source | Configured card counts | Context tokens | GPU pool tokens | Slots | Draft mode / tokens |
| --- | --- | --- | --- | --- | --- | --- |
| cfg-369208568971a342a3d6 | [SloptimistPrime/apex-flash-1-abliterated-EXL3-4bit-DGX-Spark@a4c922dc57](https://huggingface.co/SloptimistPrime/apex-flash-1-abliterated-EXL3-4bit-DGX-Spark/tree/a4c922dc57dae44a9569ec82a08a2f311636e2a6) | 3 | 262,144 | 262,144 | 4 | mtp / 3 |

Card counts are saved configuration choices, not a claim that every allowed placement was measured. A derived view can differ from its pinned download source.

<details>
<summary>cfg-369208568971a342a3d6</summary>

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
  "model_repository": "SloptimistPrime/apex-flash-1-abliterated-EXL3-4bit-DGX-Spark",
  "model_revision": "a4c922dc57dae44a9569ec82a08a2f311636e2a6",
  "draft_repository": null,
  "draft_revision": null,
  "recorded_runtime_label": null,
  "served_model_label": "apex-flash-1-abliterated-exl3-4bit-spark"
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
| [result-1d7292cb3e5c46ce2a45](../observations.json)<br>source-e55a92a1742e783d94e9e8c3.json<br>`/experiments/23/speed/1/backend_prefill/1` | [apex_exl3-mtp3-original-layer_split](apex_exl3-mtp3-original-layer_split.md) | test outcome | Outcome unspecified | backend_prefill_seconds=154.64 s; cached_prompt_tokens=0 tokens; prefill_tok_s=211.89 tokens/s; processed_prompt_tokens=32,767 tokens | Exact configuration unresolved |
| [result-3194315857293f1deedf](../observations.json)<br>source-e55a92a1742e783d94e9e8c3.json<br>`/experiments/23/speed/0` | [apex_exl3-mtp3-original-layer_split](apex_exl3-mtp3-original-layer_split.md) | performance detail | Outcome unspecified | cold_TTFT_median_seconds=39.75 s; configured_slots=4 requests; output_tokens=256 tokens; p50_inter_token_ms=23.37 ms; p95_inter_token_ms=67.41 ms; prompt_tokens=32,766 tokens; Draft accepted / proposed: 170 / 258 tokens; fraction 0.6589 | Exact configuration unresolved |
| [result-580ff3b2fa0177e6d385](../observations.json)<br>source-e55a92a1742e783d94e9e8c3.json<br>`/experiments/23` | [apex_exl3-mtp3-original-layer_split](apex_exl3-mtp3-original-layer_split.md) | context allocation | Outcome unspecified | matched_workload_host_peak_bytes=66,349,072,384 bytes; per_card_peak_used_MiB_unordered=53,684.00<br>60,060.00<br>61,906.00 | Exact configuration unresolved |
| [result-846ac30243b6f519e31e](../observations.json)<br>source-ac3d94403162b9997736bdf4.json<br>`/` | [apex_exl3-mtp3-original-layer_split](apex_exl3-mtp3-original-layer_split.md) | correctness check | Pass | 4 response usage/timing records | Exact configuration unresolved |
| [result-a5d1d27b098efc8aaaa9](../observations.json)<br>source-e55a92a1742e783d94e9e8c3.json<br>`/experiments/23/speed/0/backend_prefill/0` | [apex_exl3-mtp3-original-layer_split](apex_exl3-mtp3-original-layer_split.md) | test outcome | Outcome unspecified | backend_prefill_seconds=39.61 s; cached_prompt_tokens=0 tokens; prefill_tok_s=827.22 tokens/s; processed_prompt_tokens=32,766 tokens | Exact configuration unresolved |
| [result-c2e3ccb477353925c7a2](../observations.json)<br>source-a9e622d351a86c8b776605d4.json<br>`/experiments/37` | [apex_exl3-mtp3-original-layer_split](apex_exl3-mtp3-original-layer_split.md) | context allocation | Outcome unspecified | matched_workload_host_peak_bytes=66,349,072,384 bytes; per_card_peak_used_MiB_unordered=53,684.00<br>60,060.00<br>61,906.00 | Exact configuration unresolved |
| [result-c8e28ed382d12e005e46](../observations.json)<br>source-e55a92a1742e783d94e9e8c3.json<br>`/experiments/23/speed/1` | [apex_exl3-mtp3-original-layer_split](apex_exl3-mtp3-original-layer_split.md) | performance detail | Outcome unspecified | cold_TTFT_median_seconds=158.72 s; configured_slots=4 requests; output_tokens=256 tokens; p50_inter_token_ms=80.91 ms; p95_inter_token_ms=235.33 ms; prompt_tokens=32,767 tokens; Draft accepted / proposed: 636 / 1,164 tokens; fraction 0.5464 | Exact configuration unresolved |
| [result-e3c5fa229c4c9839390a](../observations.json)<br>source-e55a92a1742e783d94e9e8c3.json<br>`/experiments/23/speed/1/backend_prefill/2` | [apex_exl3-mtp3-original-layer_split](apex_exl3-mtp3-original-layer_split.md) | test outcome | Outcome unspecified | backend_prefill_seconds=153.27 s; cached_prompt_tokens=0 tokens; prefill_tok_s=213.79 tokens/s; processed_prompt_tokens=32,767 tokens | Exact configuration unresolved |
| [result-ec1ef3e0be46399247aa](../observations.json)<br>source-e55a92a1742e783d94e9e8c3.json<br>`/experiments/23/speed/1/backend_prefill/0` | [apex_exl3-mtp3-original-layer_split](apex_exl3-mtp3-original-layer_split.md) | test outcome | Outcome unspecified | backend_prefill_seconds=152.86 s; cached_prompt_tokens=0 tokens; prefill_tok_s=214.36 tokens/s; processed_prompt_tokens=32,767 tokens | Exact configuration unresolved |
| [result-eed4a9322bc9793a6fa1](../observations.json)<br>source-e55a92a1742e783d94e9e8c3.json<br>`/experiments/23/speed/1/backend_prefill/3` | [apex_exl3-mtp3-original-layer_split](apex_exl3-mtp3-original-layer_split.md) | test outcome | Outcome unspecified | backend_prefill_seconds=152.47 s; cached_prompt_tokens=0 tokens; prefill_tok_s=214.91 tokens/s; processed_prompt_tokens=32,767 tokens | Exact configuration unresolved |

These are saved result records, including failures and bounded checks. Copies, individual requests, report summaries and regrading can overlap; their counts are not independent test repetitions. Open each result for exact values, units, configuration binding and source receipts.

[Full archive](../../README.md) | [All retained waves](../RESULTS.md) | [Data definitions](../DATA.md) | [Recommended recipes](../../../README.md)
