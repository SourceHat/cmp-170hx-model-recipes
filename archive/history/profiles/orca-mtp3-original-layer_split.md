# orca-mtp3-original-layer_split

**Historical record. Additional test results; no matched decode wave.**

Model family: Orca (Qwen 3.8 27B abliterated).

The campaign inventory recorded status `completed`. The evidence sections retain any later results separately.

Historical configurations are provided for comparison. The [recommended recipes](../../../README.md) include supported launch scripts.

Current recipes using the same recorded checkpoint repository: [qwen27-orca-mtp3-native](../../../recipes/qwen27-orca-mtp3-native/README.md). Context, cache and runtime versions can differ.

## Saved Configuration Versions

Each configuration ID identifies a distinct original settings record. Deployment fields are omitted; versions can have identical published settings after that omission. Upstream runtime commits remain unspecified where the source retained only an integration label.

| Configuration | Recorded artifact / source | Configured card counts | Context tokens | GPU pool tokens | Slots | Draft mode / tokens |
| --- | --- | --- | --- | --- | --- | --- |
| cfg-cfacc4d48f8d520ba24b | [Lygodactylus/Qwen3.8-27B-Uncensored-exl3-8bpw@3487b152b3](https://huggingface.co/Lygodactylus/Qwen3.8-27B-Uncensored-exl3-8bpw/tree/3487b152b302930e303dc4a2e99e7e976e3ad28f) | 1 | 262,144 | 524,288 | 8 | mtp / 3 |

Card counts are saved configuration choices, not a claim that every allowed placement was measured. A derived view can differ from its pinned download source.

<details>
<summary>cfg-cfacc4d48f8d520ba24b</summary>

```json
{
  "kind": "tabby",
  "gpu_counts": [
    1
  ],
  "context": 262144,
  "cache_tokens": 524288,
  "cache_mode": "Q8",
  "draft_cache_mode": "Q8",
  "draft_mode": "mtp",
  "draft_tokens": 3,
  "max_sessions": 8,
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
  "min_effective_vram_mib": 65530,
  "parallelism": "layer_split",
  "transport": "host",
  "host_backing": "ordinary",
  "model_repository": "Lygodactylus/Qwen3.8-27B-Uncensored-exl3-8bpw",
  "model_revision": "3487b152b302930e303dc4a2e99e7e976e3ad28f",
  "draft_repository": null,
  "draft_revision": null,
  "recorded_runtime_label": null,
  "served_model_label": "qwen27-orca-exl3-8bpw",
  "main_reserve_mib_values_unordered": []
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
| [result-13b327fe28f4c3c006d8](../observations.json)<br>source-e55a92a1742e783d94e9e8c3.json<br>`/experiments/0/speed/1/backend_prefill/7` | [orca-mtp3-original-layer_split](orca-mtp3-original-layer_split.md) | test outcome | Outcome unspecified | backend_prefill_seconds=6.27 s; cached_prompt_tokens=0 tokens; prefill_tok_s=323.29 tokens/s; processed_prompt_tokens=2,027 tokens | Exact configuration unresolved |
| [result-16517404c7313cb78e67](../observations.json)<br>source-e55a92a1742e783d94e9e8c3.json<br>`/experiments/0/speed/1/backend_prefill/0` | [orca-mtp3-original-layer_split](orca-mtp3-original-layer_split.md) | test outcome | Outcome unspecified | backend_prefill_seconds=4.54 s; cached_prompt_tokens=0 tokens; prefill_tok_s=446.48 tokens/s; processed_prompt_tokens=2,027 tokens | Exact configuration unresolved |
| [result-1ed1341c24b3b9385fa2](../observations.json)<br>source-e55a92a1742e783d94e9e8c3.json<br>`/experiments/0/speed/1/backend_prefill/5` | [orca-mtp3-original-layer_split](orca-mtp3-original-layer_split.md) | test outcome | Outcome unspecified | backend_prefill_seconds=7.86 s; cached_prompt_tokens=0 tokens; prefill_tok_s=257.89 tokens/s; processed_prompt_tokens=2,027 tokens | Exact configuration unresolved |
| [result-231446ad73bcc774e27f](../observations.json)<br>source-e55a92a1742e783d94e9e8c3.json<br>`/experiments/0/speed/0` | [orca-mtp3-original-layer_split](orca-mtp3-original-layer_split.md) | performance detail | Outcome unspecified | cold_TTFT_median_seconds=1.69 s; configured_slots=8 requests; output_tokens=512 tokens; p50_inter_token_ms=12.26 ms; p95_inter_token_ms=46.75 ms; prompt_tokens=2,026 tokens; Draft accepted / proposed: 341 / 513 tokens; fraction 0.6647 | Exact configuration unresolved |
| [result-2b01b80d817d6c0a288d](../observations.json)<br>source-e55a92a1742e783d94e9e8c3.json<br>`/experiments/0/speed/1/backend_prefill/3` | [orca-mtp3-original-layer_split](orca-mtp3-original-layer_split.md) | test outcome | Outcome unspecified | backend_prefill_seconds=8.61 s; cached_prompt_tokens=0 tokens; prefill_tok_s=235.42 tokens/s; processed_prompt_tokens=2,027 tokens | Exact configuration unresolved |
| [result-40de5593ce1be1150348](../observations.json)<br>source-e55a92a1742e783d94e9e8c3.json<br>`/experiments/0` | [orca-mtp3-original-layer_split](orca-mtp3-original-layer_split.md) | context allocation | completed | matched_workload_host_peak_bytes=34,678,824,960 bytes; planning_reserve_mib=128 MiB; resident_pool_tokens=866,560 tokens; per_card_peak_used_MiB_unordered=50,302.00 | Exact configuration unresolved |
| [result-45384800dfac186b5c1b](../observations.json)<br>source-e55a92a1742e783d94e9e8c3.json<br>`/experiments/0/contexts/0` | [orca-mtp3-original-layer_split](orca-mtp3-original-layer_split.md) | context allocation | Outcome unspecified | context_tokens=262,144 tokens | Exact configuration unresolved |
| [result-47dfd112dc5233f84d42](../observations.json)<br>source-e55a92a1742e783d94e9e8c3.json<br>`/experiments/0/speed/3/backend_prefill/3` | [orca-mtp3-original-layer_split](orca-mtp3-original-layer_split.md) | test outcome | Outcome unspecified | backend_prefill_seconds=195.32 s; cached_prompt_tokens=0 tokens; prefill_tok_s=167.78 tokens/s; processed_prompt_tokens=32,770 tokens | Exact configuration unresolved |
| [result-4fc4b5170ae0467becbf](../observations.json)<br>source-b792a6ab248fc2780330c3d7.json<br>`/capacity/trials/0` | [orca-mtp3-original-layer_split](orca-mtp3-original-layer_split.md) | context allocation | Outcome unspecified | resident_pool_tokens=524,288 tokens | Recorded configuration/job |
| [result-52ac1fc5356469461237](../observations.json)<br>source-1b88b19bb8d1f6b6f26ce856.json<br>`/final_allocations/orca-mtp3-original-layer_split/allocator_GPUs/0` | [orca-mtp3-original-layer_split](orca-mtp3-original-layer_split.md) | test outcome | Outcome unspecified | allocated_bytes=63,913,977,856 bytes; free_bytes=522,125,312 bytes; peak_allocated_bytes=66,180,146,176 bytes; peak_reserved_bytes=66,202,894,336 bytes; reserved_bytes=66,202,894,336 bytes | Exact configuration unresolved |
| [result-563a4ef9b9bbb03c5509](../observations.json)<br>source-e55a92a1742e783d94e9e8c3.json<br>`/experiments/0/speed/1/backend_prefill/6` | [orca-mtp3-original-layer_split](orca-mtp3-original-layer_split.md) | test outcome | Outcome unspecified | backend_prefill_seconds=6.59 s; cached_prompt_tokens=0 tokens; prefill_tok_s=307.59 tokens/s; processed_prompt_tokens=2,027 tokens | Exact configuration unresolved |
| [result-5b78787644b9c6f98324](../observations.json)<br>source-e55a92a1742e783d94e9e8c3.json<br>`/experiments/0/speed/2` | [orca-mtp3-original-layer_split](orca-mtp3-original-layer_split.md) | performance detail | Outcome unspecified | cold_TTFT_median_seconds=24.69 s; configured_slots=8 requests; output_tokens=512 tokens; p50_inter_token_ms=19.70 ms; p95_inter_token_ms=58.17 ms; prompt_tokens=32,769 tokens; Draft accepted / proposed: 325 / 561 tokens; fraction 0.5793 | Exact configuration unresolved |
| [result-6417d7da12c6855b6405](../observations.json)<br>source-e55a92a1742e783d94e9e8c3.json<br>`/experiments/0/speed/0/backend_prefill/0` | [orca-mtp3-original-layer_split](orca-mtp3-original-layer_split.md) | test outcome | Outcome unspecified | backend_prefill_seconds=1.58 s; cached_prompt_tokens=0 tokens; prefill_tok_s=1,282.28 tokens/s; processed_prompt_tokens=2,026 tokens | Exact configuration unresolved |
| [result-69bf16baceebf99d4381](../observations.json)<br>source-e55a92a1742e783d94e9e8c3.json<br>`/experiments/0/contexts/1` | [orca-mtp3-original-layer_split](orca-mtp3-original-layer_split.md) | context allocation | Outcome unspecified | context_tokens=524,288 tokens | Exact configuration unresolved |
| [result-6e38c9bbabf25dc30247](../observations.json)<br>source-e55a92a1742e783d94e9e8c3.json<br>`/experiments/0/speed/3/backend_prefill/2` | [orca-mtp3-original-layer_split](orca-mtp3-original-layer_split.md) | test outcome | Outcome unspecified | backend_prefill_seconds=195.19 s; cached_prompt_tokens=0 tokens; prefill_tok_s=167.89 tokens/s; processed_prompt_tokens=32,770 tokens | Exact configuration unresolved |
| [result-71edfbae113e21b53039](../observations.json)<br>source-e55a92a1742e783d94e9e8c3.json<br>`/experiments/0/independently_maximized_config` | [orca-mtp3-original-layer_split](orca-mtp3-original-layer_split.md) | context allocation | Outcome unspecified | cache_tokens=866,560 tokens; context=262,144 tokens; reserve_mib=128 MiB | Exact configuration unresolved |
| [result-746e51c32e1a19355c28](../observations.json)<br>source-a9e622d351a86c8b776605d4.json<br>`/experiments/0` | [orca-mtp3-original-layer_split](orca-mtp3-original-layer_split.md) | context allocation | completed | matched_workload_host_peak_bytes=34,678,824,960 bytes; planning_reserve_mib=128 MiB; resident_pool_tokens=866,560 tokens; per_card_peak_used_MiB_unordered=50,302.00 | Exact configuration unresolved |
| [result-76d9ec6ae5d141090814](../observations.json)<br>source-e55a92a1742e783d94e9e8c3.json<br>`/experiments/0/speed/3/backend_prefill/0` | [orca-mtp3-original-layer_split](orca-mtp3-original-layer_split.md) | test outcome | Outcome unspecified | backend_prefill_seconds=186.31 s; cached_prompt_tokens=0 tokens; prefill_tok_s=175.89 tokens/s; processed_prompt_tokens=32,770 tokens | Exact configuration unresolved |
| [result-7989e2fc37bbc30ef031](../observations.json)<br>source-b792a6ab248fc2780330c3d7.json<br>`/correctness` | [orca-mtp3-original-layer_split](orca-mtp3-original-layer_split.md) | correctness check | Pass | 4 response usage/timing records | Exact configuration unresolved |
| [result-8a913f3a2d9b13f0506e](../observations.json)<br>source-e55a92a1742e783d94e9e8c3.json<br>`/experiments/0/speed/3/backend_prefill/1` | [orca-mtp3-original-layer_split](orca-mtp3-original-layer_split.md) | test outcome | Outcome unspecified | backend_prefill_seconds=193.84 s; cached_prompt_tokens=0 tokens; prefill_tok_s=169.06 tokens/s; processed_prompt_tokens=32,770 tokens | Exact configuration unresolved |
| [result-914014d2995322c4a473](../observations.json)<br>source-e55a92a1742e783d94e9e8c3.json<br>`/experiments/0/speed/3/backend_prefill/7` | [orca-mtp3-original-layer_split](orca-mtp3-original-layer_split.md) | test outcome | Outcome unspecified | backend_prefill_seconds=190.78 s; cached_prompt_tokens=0 tokens; prefill_tok_s=171.77 tokens/s; processed_prompt_tokens=32,770 tokens | Exact configuration unresolved |
| [result-935df64e4774febf73e9](../observations.json)<br>source-e55a92a1742e783d94e9e8c3.json<br>`/experiments/0/speed/1/backend_prefill/4` | [orca-mtp3-original-layer_split](orca-mtp3-original-layer_split.md) | test outcome | Outcome unspecified | backend_prefill_seconds=8.18 s; cached_prompt_tokens=0 tokens; prefill_tok_s=247.80 tokens/s; processed_prompt_tokens=2,027 tokens | Exact configuration unresolved |
| [result-b169bc88cf9db221216b](../observations.json)<br>source-e55a92a1742e783d94e9e8c3.json<br>`/experiments/0/speed/1/backend_prefill/1` | [orca-mtp3-original-layer_split](orca-mtp3-original-layer_split.md) | test outcome | Outcome unspecified | backend_prefill_seconds=8.04 s; cached_prompt_tokens=0 tokens; prefill_tok_s=252.11 tokens/s; processed_prompt_tokens=2,027 tokens | Exact configuration unresolved |
| [result-b197f473ab83db4889a9](../observations.json)<br>source-e55a92a1742e783d94e9e8c3.json<br>`/experiments/0/speed/1` | [orca-mtp3-original-layer_split](orca-mtp3-original-layer_split.md) | performance detail | Outcome unspecified | cold_TTFT_median_seconds=11.59 s; configured_slots=8 requests; output_tokens=512 tokens; p50_inter_token_ms=36.76 ms; p95_inter_token_ms=109.83 ms; prompt_tokens=2,027 tokens; Draft accepted / proposed: 2,630 / 4,398 tokens; fraction 0.5980 | Exact configuration unresolved |
| [result-bc9008aae5c27ac1f657](../observations.json)<br>source-1b88b19bb8d1f6b6f26ce856.json<br>`/final_allocations/orca-mtp3-original-layer_split` | [orca-mtp3-original-layer_split](orca-mtp3-original-layer_split.md) | context allocation | Outcome unspecified | actual_input_tokens=516,139 tokens; configured_slots=8 requests; context_limit=524,288 tokens; resident_pool_tokens=866,560 tokens | Exact configuration unresolved |
| [result-bca3718cf1de0cc4ef78](../observations.json)<br>source-69b3837adcee61f206441871.json<br>`/` | [orca-mtp3-original-layer_split](orca-mtp3-original-layer_split.md) | correctness check | Pass | 4 response usage/timing records | Exact configuration unresolved |
| [result-bd8c6acd079df663f349](../observations.json)<br>source-e55a92a1742e783d94e9e8c3.json<br>`/experiments/0/speed/3/backend_prefill/5` | [orca-mtp3-original-layer_split](orca-mtp3-original-layer_split.md) | test outcome | Outcome unspecified | backend_prefill_seconds=193.63 s; cached_prompt_tokens=0 tokens; prefill_tok_s=169.24 tokens/s; processed_prompt_tokens=32,770 tokens | Exact configuration unresolved |
| [result-c0ce0a19b6118c0ef643](../observations.json)<br>source-e55a92a1742e783d94e9e8c3.json<br>`/experiments/0/speed/3/backend_prefill/6` | [orca-mtp3-original-layer_split](orca-mtp3-original-layer_split.md) | test outcome | Outcome unspecified | backend_prefill_seconds=193.29 s; cached_prompt_tokens=0 tokens; prefill_tok_s=169.54 tokens/s; processed_prompt_tokens=32,770 tokens | Exact configuration unresolved |
| [result-cca3435ccccadec2f972](../observations.json)<br>source-e55a92a1742e783d94e9e8c3.json<br>`/experiments/0/speed/3/backend_prefill/4` | [orca-mtp3-original-layer_split](orca-mtp3-original-layer_split.md) | test outcome | Outcome unspecified | backend_prefill_seconds=194.99 s; cached_prompt_tokens=0 tokens; prefill_tok_s=168.06 tokens/s; processed_prompt_tokens=32,770 tokens | Exact configuration unresolved |
| [result-e0605fe19db1d7dfde1c](../observations.json)<br>source-e55a92a1742e783d94e9e8c3.json<br>`/experiments/0/speed/1/backend_prefill/2` | [orca-mtp3-original-layer_split](orca-mtp3-original-layer_split.md) | test outcome | Outcome unspecified | backend_prefill_seconds=8.94 s; cached_prompt_tokens=0 tokens; prefill_tok_s=226.73 tokens/s; processed_prompt_tokens=2,027 tokens | Exact configuration unresolved |
| [result-e3892848c6ad9dd4fdc3](../observations.json)<br>source-e55a92a1742e783d94e9e8c3.json<br>`/experiments/0/speed/2/backend_prefill/0` | [orca-mtp3-original-layer_split](orca-mtp3-original-layer_split.md) | test outcome | Outcome unspecified | backend_prefill_seconds=24.58 s; cached_prompt_tokens=0 tokens; prefill_tok_s=1,333.16 tokens/s; processed_prompt_tokens=32,769 tokens | Exact configuration unresolved |
| [result-f6babba1a488a6d00d5d](../observations.json)<br>source-e55a92a1742e783d94e9e8c3.json<br>`/experiments/0/speed/3` | [orca-mtp3-original-layer_split](orca-mtp3-original-layer_split.md) | performance detail | Outcome unspecified | cold_TTFT_median_seconds=200.43 s; configured_slots=8 requests; output_tokens=512 tokens; p50_inter_token_ms=67.79 ms; p95_inter_token_ms=206.10 ms; prompt_tokens=32,770 tokens; Draft accepted / proposed: 2,693 / 4,209 tokens; fraction 0.6398 | Exact configuration unresolved |

These are saved result records, including failures and bounded checks. Copies, individual requests, report summaries and regrading can overlap; their counts are not independent test repetitions. Open each result for exact values, units, configuration binding and source receipts.

[Full archive](../../README.md) | [All retained waves](../RESULTS.md) | [Data definitions](../DATA.md) | [Recommended recipes](../../../README.md)
