# mimo-dflash7-original-layer_split

**Historical record. Additional test results; no matched decode wave.**

Model family: MiMo V2.6 Flash.

The campaign inventory recorded status `speed_measured_capacity_pending`. The evidence sections retain any later results separately.

Historical configurations are provided for comparison. The [recommended recipes](../../../README.md) include supported launch scripts.

Current recipes using the same recorded checkpoint repository: [mimo-flash-mtp1-tp3](../../../recipes/mimo-flash-mtp1-tp3/README.md). Context, cache and runtime versions can differ.

## Saved Configuration Versions

Each configuration ID identifies a distinct original settings record. Deployment fields are omitted; versions can have identical published settings after that omission. Upstream runtime commits remain unspecified where the source retained only an integration label.

| Configuration | Recorded artifact / source | Configured card counts | Context tokens | GPU pool tokens | Slots | Draft mode / tokens |
| --- | --- | --- | --- | --- | --- | --- |
| cfg-217ff9c9b50e9f972525 | [MikeRoz/MiMo-V2.6-Flash-MOPD-4.03bpw-h8-exl3@29c8351a8b](https://huggingface.co/MikeRoz/MiMo-V2.6-Flash-MOPD-4.03bpw-h8-exl3/tree/29c8351a8b5854ec385adaeba7bbe62c790d40ea) | 3 | 262,144 | 262,144 | 4 | dflash / 7 |

Card counts are saved configuration choices, not a claim that every allowed placement was measured. A derived view can differ from its pinned download source.

<details>
<summary>cfg-217ff9c9b50e9f972525</summary>

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
  "draft_mode": "dflash",
  "draft_tokens": 7,
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
  "served_model_label": "mimo-v2.6-flash",
  "main_reserve_mib_values_unordered": [
    6144
  ]
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
| [result-04cf581a25c49625c628](../observations.json)<br>source-a9e622d351a86c8b776605d4.json<br>`/experiments/13` | [mimo-dflash7-original-layer_split](mimo-dflash7-original-layer_split.md) | context allocation | Outcome unspecified | matched_workload_host_peak_bytes=75,700,224,000 bytes; per_card_peak_used_MiB_unordered=41,262.00<br>59,890.00<br>62,572.00 | Exact configuration unresolved |
| [result-100889769dfdbfad3e11](../observations.json)<br>source-e55a92a1742e783d94e9e8c3.json<br>`/experiments/9/speed/3/backend_prefill/2` | [mimo-dflash7-original-layer_split](mimo-dflash7-original-layer_split.md) | test outcome | Outcome unspecified | backend_prefill_seconds=163.47 s; cached_prompt_tokens=0 tokens; prefill_tok_s=200.44 tokens/s; processed_prompt_tokens=32,766 tokens | Exact configuration unresolved |
| [result-1aae4d43ea98e1fc108c](../observations.json)<br>source-e55a92a1742e783d94e9e8c3.json<br>`/experiments/9/speed/1/backend_prefill/2` | [mimo-dflash7-original-layer_split](mimo-dflash7-original-layer_split.md) | test outcome | Outcome unspecified | backend_prefill_seconds=7.43 s; cached_prompt_tokens=0 tokens; prefill_tok_s=274.43 tokens/s; processed_prompt_tokens=2,039 tokens | Exact configuration unresolved |
| [result-31f755a6e6e4f1a76980](../observations.json)<br>source-e55a92a1742e783d94e9e8c3.json<br>`/experiments/9/speed/1/backend_prefill/3` | [mimo-dflash7-original-layer_split](mimo-dflash7-original-layer_split.md) | test outcome | Outcome unspecified | backend_prefill_seconds=6.81 s; cached_prompt_tokens=0 tokens; prefill_tok_s=299.41 tokens/s; processed_prompt_tokens=2,039 tokens | Exact configuration unresolved |
| [result-5367cdc7b6c4922f03e5](../observations.json)<br>source-e55a92a1742e783d94e9e8c3.json<br>`/experiments/9/speed/0` | [mimo-dflash7-original-layer_split](mimo-dflash7-original-layer_split.md) | performance detail | Outcome unspecified | cold_TTFT_median_seconds=2.78 s; configured_slots=4 requests; output_tokens=512 tokens; p50_inter_token_ms=26.69 ms; p95_inter_token_ms=78.48 ms; prompt_tokens=2,038 tokens; Draft accepted / proposed: 349 / 1,141 tokens; fraction 0.3059 | Exact configuration unresolved |
| [result-593030390d0a094cff30](../observations.json)<br>source-e55a92a1742e783d94e9e8c3.json<br>`/experiments/9/speed/3/backend_prefill/1` | [mimo-dflash7-original-layer_split](mimo-dflash7-original-layer_split.md) | test outcome | Outcome unspecified | backend_prefill_seconds=164.09 s; cached_prompt_tokens=0 tokens; prefill_tok_s=199.68 tokens/s; processed_prompt_tokens=32,766 tokens | Exact configuration unresolved |
| [result-5d5b3138b01cf082f9b2](../observations.json)<br>source-e55a92a1742e783d94e9e8c3.json<br>`/experiments/9/speed/0/backend_prefill/0` | [mimo-dflash7-original-layer_split](mimo-dflash7-original-layer_split.md) | test outcome | Outcome unspecified | backend_prefill_seconds=2.71 s; cached_prompt_tokens=0 tokens; prefill_tok_s=752.03 tokens/s; processed_prompt_tokens=2,038 tokens | Exact configuration unresolved |
| [result-6005adf07478be52ca14](../observations.json)<br>source-e55a92a1742e783d94e9e8c3.json<br>`/experiments/9/speed/3` | [mimo-dflash7-original-layer_split](mimo-dflash7-original-layer_split.md) | performance detail | Outcome unspecified | cold_TTFT_median_seconds=168.11 s; configured_slots=4 requests; output_tokens=512 tokens; p50_inter_token_ms=106.03 ms; p95_inter_token_ms=318.69 ms; prompt_tokens=32,766 tokens; Draft accepted / proposed: 1,421 / 4,389 tokens; fraction 0.3238 | Exact configuration unresolved |
| [result-64ae770d320646b38089](../observations.json)<br>source-e55a92a1742e783d94e9e8c3.json<br>`/experiments/9/speed/2` | [mimo-dflash7-original-layer_split](mimo-dflash7-original-layer_split.md) | performance detail | Outcome unspecified | cold_TTFT_median_seconds=41.98 s; configured_slots=4 requests; output_tokens=512 tokens; p50_inter_token_ms=51.41 ms; p95_inter_token_ms=120.07 ms; prompt_tokens=32,765 tokens; Draft accepted / proposed: 330 / 1,274 tokens; fraction 0.2590 | Exact configuration unresolved |
| [result-70c95a311af43b6401b2](../observations.json)<br>source-e55a92a1742e783d94e9e8c3.json<br>`/experiments/9/speed/1/backend_prefill/1` | [mimo-dflash7-original-layer_split](mimo-dflash7-original-layer_split.md) | test outcome | Outcome unspecified | backend_prefill_seconds=8.05 s; cached_prompt_tokens=0 tokens; prefill_tok_s=253.29 tokens/s; processed_prompt_tokens=2,039 tokens | Exact configuration unresolved |
| [result-77dd62a8b559b4c0d833](../observations.json)<br>source-e55a92a1742e783d94e9e8c3.json<br>`/experiments/9/speed/1` | [mimo-dflash7-original-layer_split](mimo-dflash7-original-layer_split.md) | performance detail | Outcome unspecified | cold_TTFT_median_seconds=11.35 s; configured_slots=4 requests; output_tokens=512 tokens; p50_inter_token_ms=78.53 ms; p95_inter_token_ms=229.74 ms; prompt_tokens=2,039 tokens; Draft accepted / proposed: 1,400 / 4,536 tokens; fraction 0.3086 | Exact configuration unresolved |
| [result-7880f69e5cf50ae9a67e](../observations.json)<br>source-e55a92a1742e783d94e9e8c3.json<br>`/experiments/9/speed/3/backend_prefill/3` | [mimo-dflash7-original-layer_split](mimo-dflash7-original-layer_split.md) | test outcome | Outcome unspecified | backend_prefill_seconds=162.05 s; cached_prompt_tokens=0 tokens; prefill_tok_s=202.20 tokens/s; processed_prompt_tokens=32,766 tokens | Exact configuration unresolved |
| [result-7f402a875b7d5d9ec9e9](../observations.json)<br>source-e55a92a1742e783d94e9e8c3.json<br>`/experiments/9/speed/2/backend_prefill/0` | [mimo-dflash7-original-layer_split](mimo-dflash7-original-layer_split.md) | test outcome | Outcome unspecified | backend_prefill_seconds=41.74 s; cached_prompt_tokens=0 tokens; prefill_tok_s=784.98 tokens/s; processed_prompt_tokens=32,765 tokens | Exact configuration unresolved |
| [result-a966f4fe9d6c98ed001e](../observations.json)<br>source-e55a92a1742e783d94e9e8c3.json<br>`/experiments/9/speed/3/backend_prefill/0` | [mimo-dflash7-original-layer_split](mimo-dflash7-original-layer_split.md) | test outcome | Outcome unspecified | backend_prefill_seconds=160.81 s; cached_prompt_tokens=0 tokens; prefill_tok_s=203.76 tokens/s; processed_prompt_tokens=32,766 tokens | Exact configuration unresolved |
| [result-b4b1f88a50f19e72523c](../observations.json)<br>source-e55a92a1742e783d94e9e8c3.json<br>`/experiments/9/speed/1/backend_prefill/0` | [mimo-dflash7-original-layer_split](mimo-dflash7-original-layer_split.md) | test outcome | Outcome unspecified | backend_prefill_seconds=6.92 s; cached_prompt_tokens=0 tokens; prefill_tok_s=294.65 tokens/s; processed_prompt_tokens=2,039 tokens | Exact configuration unresolved |
| [result-c4a00f71936e2837aa35](../observations.json)<br>source-0b85c12a4a3dcbef565261b0.json<br>`/` | [mimo-dflash7-original-layer_split](mimo-dflash7-original-layer_split.md) | correctness check | Pass | 4 response usage/timing records | Exact configuration unresolved |
| [result-cbef738615b1757a6e35](../observations.json)<br>source-e55a92a1742e783d94e9e8c3.json<br>`/experiments/9` | [mimo-dflash7-original-layer_split](mimo-dflash7-original-layer_split.md) | context allocation | Outcome unspecified | matched_workload_host_peak_bytes=75,700,224,000 bytes; per_card_peak_used_MiB_unordered=41,262.00<br>59,890.00<br>62,572.00 | Exact configuration unresolved |

These are saved result records, including failures and bounded checks. Copies, individual requests, report summaries and regrading can overlap; their counts are not independent test repetitions. Open each result for exact values, units, configuration binding and source receipts.

[Full archive](../../README.md) | [All retained waves](../RESULTS.md) | [Data definitions](../DATA.md) | [Recommended recipes](../../../README.md)
