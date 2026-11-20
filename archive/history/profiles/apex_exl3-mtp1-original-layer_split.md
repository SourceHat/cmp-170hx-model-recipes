# apex_exl3-mtp1-original-layer_split

**Historical record. Additional test results; no matched decode wave.**

Model family: Apex Flash 1 (GLM 5.3 Flash post-train).

The campaign inventory recorded status `speed_measured_capacity_pending`. The evidence sections retain any later results separately.

Historical configurations are provided for comparison. The [recommended recipes](../../../README.md) include supported launch scripts.

Current recipes using the same recorded checkpoint repository: [apex-abliterated-exl3-mtp1-tp3](../../../recipes/apex-abliterated-exl3-mtp1-tp3/README.md). Context, cache and runtime versions can differ.

## Saved Configuration Versions

Each configuration ID identifies a distinct original settings record. Deployment fields are omitted; versions can have identical published settings after that omission. Upstream runtime commits remain unspecified where the source retained only an integration label.

| Configuration | Recorded artifact / source | Configured card counts | Context tokens | GPU pool tokens | Slots | Draft mode / tokens |
| --- | --- | --- | --- | --- | --- | --- |
| cfg-44b446b451e933a942bb | [SloptimistPrime/apex-flash-1-abliterated-EXL3-4bit-DGX-Spark@a4c922dc57](https://huggingface.co/SloptimistPrime/apex-flash-1-abliterated-EXL3-4bit-DGX-Spark/tree/a4c922dc57dae44a9569ec82a08a2f311636e2a6) | 3 | 262,144 | 262,144 | 4 | mtp / 1 |

Card counts are saved configuration choices, not a claim that every allowed placement was measured. A derived view can differ from its pinned download source.

<details>
<summary>cfg-44b446b451e933a942bb</summary>

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
| [result-14dfa3ea0828cad17a23](../observations.json)<br>source-e55a92a1742e783d94e9e8c3.json<br>`/experiments/20/speed/1/backend_prefill/3` | [apex_exl3-mtp1-original-layer_split](apex_exl3-mtp1-original-layer_split.md) | test outcome | Outcome unspecified | backend_prefill_seconds=154.40 s; cached_prompt_tokens=0 tokens; prefill_tok_s=212.22 tokens/s; processed_prompt_tokens=32,767 tokens | Exact configuration unresolved |
| [result-20252972d33c109ffbfd](../observations.json)<br>source-e55a92a1742e783d94e9e8c3.json<br>`/experiments/20/speed/0/backend_prefill/0` | [apex_exl3-mtp1-original-layer_split](apex_exl3-mtp1-original-layer_split.md) | test outcome | Outcome unspecified | backend_prefill_seconds=39.53 s; cached_prompt_tokens=0 tokens; prefill_tok_s=828.89 tokens/s; processed_prompt_tokens=32,766 tokens | Exact configuration unresolved |
| [result-2c3ab59bc10e111982ce](../observations.json)<br>source-e55a92a1742e783d94e9e8c3.json<br>`/experiments/20/speed/1/backend_prefill/2` | [apex_exl3-mtp1-original-layer_split](apex_exl3-mtp1-original-layer_split.md) | test outcome | Outcome unspecified | backend_prefill_seconds=155.20 s; cached_prompt_tokens=0 tokens; prefill_tok_s=211.13 tokens/s; processed_prompt_tokens=32,767 tokens | Exact configuration unresolved |
| [result-2d450973c1eb50d7f97d](../observations.json)<br>source-e55a92a1742e783d94e9e8c3.json<br>`/experiments/20/speed/0` | [apex_exl3-mtp1-original-layer_split](apex_exl3-mtp1-original-layer_split.md) | performance detail | Outcome unspecified | cold_TTFT_median_seconds=39.65 s; configured_slots=4 requests; output_tokens=256 tokens; p50_inter_token_ms=26.62 ms; p95_inter_token_ms=51.87 ms; prompt_tokens=32,766 tokens; Draft accepted / proposed: 117 / 139 tokens; fraction 0.8417 | Exact configuration unresolved |
| [result-3790311e0b68bd2ee8ce](../observations.json)<br>source-e55a92a1742e783d94e9e8c3.json<br>`/experiments/20/speed/1/backend_prefill/0` | [apex_exl3-mtp1-original-layer_split](apex_exl3-mtp1-original-layer_split.md) | test outcome | Outcome unspecified | backend_prefill_seconds=155.70 s; cached_prompt_tokens=0 tokens; prefill_tok_s=210.45 tokens/s; processed_prompt_tokens=32,767 tokens | Exact configuration unresolved |
| [result-5a2d5afd6b968751f92c](../observations.json)<br>source-a9e622d351a86c8b776605d4.json<br>`/experiments/33` | [apex_exl3-mtp1-original-layer_split](apex_exl3-mtp1-original-layer_split.md) | context allocation | Outcome unspecified | matched_workload_host_peak_bytes=67,977,781,248 bytes; per_card_peak_used_MiB_unordered=53,370.00<br>59,690.00<br>61,438.00 | Exact configuration unresolved |
| [result-88d61cee6318cd919f97](../observations.json)<br>source-e55a92a1742e783d94e9e8c3.json<br>`/experiments/20/speed/1` | [apex_exl3-mtp1-original-layer_split](apex_exl3-mtp1-original-layer_split.md) | performance detail | Outcome unspecified | cold_TTFT_median_seconds=158.87 s; configured_slots=4 requests; output_tokens=256 tokens; p50_inter_token_ms=56.43 ms; p95_inter_token_ms=112.41 ms; prompt_tokens=32,767 tokens; Draft accepted / proposed: 470 / 554 tokens; fraction 0.8484 | Exact configuration unresolved |
| [result-a899c2b9a62f7e74615d](../observations.json)<br>source-e55a92a1742e783d94e9e8c3.json<br>`/experiments/20/speed/1/backend_prefill/1` | [apex_exl3-mtp1-original-layer_split](apex_exl3-mtp1-original-layer_split.md) | test outcome | Outcome unspecified | backend_prefill_seconds=156.01 s; cached_prompt_tokens=0 tokens; prefill_tok_s=210.03 tokens/s; processed_prompt_tokens=32,767 tokens | Exact configuration unresolved |
| [result-ec356c775753bc64e573](../observations.json)<br>source-cb8405400456be8eab1017e0.json<br>`/` | [apex_exl3-mtp1-original-layer_split](apex_exl3-mtp1-original-layer_split.md) | correctness check | Pass | 4 response usage/timing records | Exact configuration unresolved |
| [result-f5a25465d7749607eb0d](../observations.json)<br>source-e55a92a1742e783d94e9e8c3.json<br>`/experiments/20` | [apex_exl3-mtp1-original-layer_split](apex_exl3-mtp1-original-layer_split.md) | context allocation | Outcome unspecified | matched_workload_host_peak_bytes=67,977,781,248 bytes; per_card_peak_used_MiB_unordered=53,370.00<br>59,690.00<br>61,438.00 | Exact configuration unresolved |

These are saved result records, including failures and bounded checks. Copies, individual requests, report summaries and regrading can overlap; their counts are not independent test repetitions. Open each result for exact values, units, configuration binding and source receipts.

[Full archive](../../README.md) | [All retained waves](../RESULTS.md) | [Data definitions](../DATA.md) | [Recommended recipes](../../../README.md)
