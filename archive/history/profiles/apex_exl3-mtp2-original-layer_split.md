# apex_exl3-mtp2-original-layer_split

**Historical record. Additional test results; no matched decode wave.**

Model family: Apex Flash 1 (GLM 5.3 Flash post-train).

The campaign inventory recorded status `speed_measured_capacity_pending`. The evidence sections retain any later results separately.

Historical configurations are provided for comparison. The [recommended recipes](../../../README.md) include supported launch scripts.

Current recipes using the same recorded checkpoint repository: [apex-abliterated-exl3-mtp1-tp3](../../../recipes/apex-abliterated-exl3-mtp1-tp3/README.md). Context, cache and runtime versions can differ.

## Saved Configuration Versions

Each configuration ID identifies a distinct original settings record. Deployment fields are omitted; versions can have identical published settings after that omission. Upstream runtime commits remain unspecified where the source retained only an integration label.

| Configuration | Recorded artifact / source | Configured card counts | Context tokens | GPU pool tokens | Slots | Draft mode / tokens |
| --- | --- | --- | --- | --- | --- | --- |
| cfg-cb8eacbfb0f1a64cc0de | [SloptimistPrime/apex-flash-1-abliterated-EXL3-4bit-DGX-Spark@a4c922dc57](https://huggingface.co/SloptimistPrime/apex-flash-1-abliterated-EXL3-4bit-DGX-Spark/tree/a4c922dc57dae44a9569ec82a08a2f311636e2a6) | 3 | 262,144 | 262,144 | 4 | mtp / 2 |

Card counts are saved configuration choices, not a claim that every allowed placement was measured. A derived view can differ from its pinned download source.

<details>
<summary>cfg-cb8eacbfb0f1a64cc0de</summary>

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
| [result-339b54241fe4ee59576b](../observations.json)<br>source-e55a92a1742e783d94e9e8c3.json<br>`/experiments/22/speed/1/backend_prefill/3` | [apex_exl3-mtp2-original-layer_split](apex_exl3-mtp2-original-layer_split.md) | test outcome | Outcome unspecified | backend_prefill_seconds=153.17 s; cached_prompt_tokens=0 tokens; prefill_tok_s=213.93 tokens/s; processed_prompt_tokens=32,767 tokens | Exact configuration unresolved |
| [result-63c5851a7a726c47b09a](../observations.json)<br>source-e55a92a1742e783d94e9e8c3.json<br>`/experiments/22/speed/1/backend_prefill/1` | [apex_exl3-mtp2-original-layer_split](apex_exl3-mtp2-original-layer_split.md) | test outcome | Outcome unspecified | backend_prefill_seconds=155.37 s; cached_prompt_tokens=0 tokens; prefill_tok_s=210.90 tokens/s; processed_prompt_tokens=32,767 tokens | Exact configuration unresolved |
| [result-6e764b315ea23e86e3b4](../observations.json)<br>source-a9e622d351a86c8b776605d4.json<br>`/experiments/35` | [apex_exl3-mtp2-original-layer_split](apex_exl3-mtp2-original-layer_split.md) | context allocation | Outcome unspecified | matched_workload_host_peak_bytes=66,388,115,456 bytes; per_card_peak_used_MiB_unordered=53,502.00<br>59,880.00<br>61,666.00 | Exact configuration unresolved |
| [result-9de73dbda9dfe241aa33](../observations.json)<br>source-e55a92a1742e783d94e9e8c3.json<br>`/experiments/22/speed/1` | [apex_exl3-mtp2-original-layer_split](apex_exl3-mtp2-original-layer_split.md) | performance detail | Outcome unspecified | cold_TTFT_median_seconds=159.39 s; configured_slots=4 requests; output_tokens=256 tokens; p50_inter_token_ms=72.36 ms; p95_inter_token_ms=211.55 ms; prompt_tokens=32,767 tokens; Draft accepted / proposed: 579 / 890 tokens; fraction 0.6506 | Exact configuration unresolved |
| [result-9df53957b533d6a793fe](../observations.json)<br>source-e55a92a1742e783d94e9e8c3.json<br>`/experiments/22/speed/0` | [apex_exl3-mtp2-original-layer_split](apex_exl3-mtp2-original-layer_split.md) | performance detail | Outcome unspecified | cold_TTFT_median_seconds=39.68 s; configured_slots=4 requests; output_tokens=256 tokens; p50_inter_token_ms=22.51 ms; p95_inter_token_ms=63.75 ms; prompt_tokens=32,766 tokens; Draft accepted / proposed: 147 / 218 tokens; fraction 0.6743 | Exact configuration unresolved |
| [result-a910f541d397f6e1151b](../observations.json)<br>source-e55a92a1742e783d94e9e8c3.json<br>`/experiments/22/speed/1/backend_prefill/2` | [apex_exl3-mtp2-original-layer_split](apex_exl3-mtp2-original-layer_split.md) | test outcome | Outcome unspecified | backend_prefill_seconds=153.98 s; cached_prompt_tokens=0 tokens; prefill_tok_s=212.80 tokens/s; processed_prompt_tokens=32,767 tokens | Exact configuration unresolved |
| [result-b3deed74666762f0a8b2](../observations.json)<br>source-1e5f0a0e14a33e2d93efba9f.json<br>`/` | [apex_exl3-mtp2-original-layer_split](apex_exl3-mtp2-original-layer_split.md) | correctness check | Pass | 4 response usage/timing records | Exact configuration unresolved |
| [result-d0285ebe2785354d1b40](../observations.json)<br>source-e55a92a1742e783d94e9e8c3.json<br>`/experiments/22/speed/0/backend_prefill/0` | [apex_exl3-mtp2-original-layer_split](apex_exl3-mtp2-original-layer_split.md) | test outcome | Outcome unspecified | backend_prefill_seconds=39.55 s; cached_prompt_tokens=0 tokens; prefill_tok_s=828.47 tokens/s; processed_prompt_tokens=32,766 tokens | Exact configuration unresolved |
| [result-d1d9f9edcb2ecca5dae2](../observations.json)<br>source-e55a92a1742e783d94e9e8c3.json<br>`/experiments/22` | [apex_exl3-mtp2-original-layer_split](apex_exl3-mtp2-original-layer_split.md) | context allocation | Outcome unspecified | matched_workload_host_peak_bytes=66,388,115,456 bytes; per_card_peak_used_MiB_unordered=53,502.00<br>59,880.00<br>61,666.00 | Exact configuration unresolved |
| [result-f53dc32a889900daa23a](../observations.json)<br>source-e55a92a1742e783d94e9e8c3.json<br>`/experiments/22/speed/1/backend_prefill/0` | [apex_exl3-mtp2-original-layer_split](apex_exl3-mtp2-original-layer_split.md) | test outcome | Outcome unspecified | backend_prefill_seconds=154.73 s; cached_prompt_tokens=0 tokens; prefill_tok_s=211.77 tokens/s; processed_prompt_tokens=32,767 tokens | Exact configuration unresolved |

These are saved result records, including failures and bounded checks. Copies, individual requests, report summaries and regrading can overlap; their counts are not independent test repetitions. Open each result for exact values, units, configuration binding and source receipts.

[Full archive](../../README.md) | [All retained waves](../RESULTS.md) | [Data definitions](../DATA.md) | [Recommended recipes](../../../README.md)
