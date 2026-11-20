# glm53-capacity3-upper

**Historical record. Decode interval measured.**

Model family: GLM 5.3 Flash.

Recorded archive reason: Historical capacity, fit or control configuration; later DFlash2 and MTP variants have separate records.

Historical configurations are provided for comparison. The [recommended recipes](../../../README.md) include supported launch scripts.

Current recipes using the same recorded checkpoint repository: [glm-5.3-flash-mtp1-tp3](../../../recipes/glm-5.3-flash-mtp1-tp3/README.md). Context, cache and runtime versions can differ.

## Saved Configuration Versions

Each configuration ID identifies a distinct original settings record. Deployment fields are omitted; versions can have identical published settings after that omission. Upstream runtime commits remain unspecified where the source retained only an integration label.

| Configuration | Recorded artifact / source | Configured card counts | Context tokens | GPU pool tokens | Slots | Draft mode / tokens |
| --- | --- | --- | --- | --- | --- | --- |
| cfg-8a156d9ba072b55b36b7 | [turboderp/GLM-5.3-Flash-exl3@2a30229e67](https://huggingface.co/turboderp/GLM-5.3-Flash-exl3/tree/2a30229e67012798ba9f0cd832bb78abf4c363d5) | 3 | 500,000 | 1,048,576 | 8 | mtp / 1 |
| cfg-ee63ac1fcc5f0315f205 | [turboderp/GLM-5.3-Flash-exl3@2a30229e67](https://huggingface.co/turboderp/GLM-5.3-Flash-exl3/tree/2a30229e67012798ba9f0cd832bb78abf4c363d5) | 3 | 500,000 | 983,040 | 8 | mtp / 1 |

Card counts are saved configuration choices, not a claim that every allowed placement was measured. A derived view can differ from its pinned download source.

<details>
<summary>cfg-8a156d9ba072b55b36b7</summary>

```json
{
  "kind": "tabby",
  "gpu_counts": [
    3
  ],
  "context": 500000,
  "cache_tokens": 1048576,
  "cache_mode": "Q8",
  "draft_cache_mode": "Q8",
  "draft_mode": "mtp",
  "draft_tokens": 1,
  "max_sessions": 8,
  "chunk_size": 512,
  "reserve_mib": 2560,
  "ram_kv_mib": 32768,
  "ram_recurrent_mib": 16384,
  "dynamic_draft": false,
  "power_watts": 200,
  "host_memory_gib": 80,
  "host_swap_gib": 0,
  "min_vram_mib_per_gpu": 65530,
  "min_effective_vram_mib": 196000,
  "model_repository": "turboderp/GLM-5.3-Flash-exl3",
  "model_revision": "2a30229e67012798ba9f0cd832bb78abf4c363d5",
  "draft_repository": null,
  "draft_revision": null,
  "recorded_runtime_label": null,
  "served_model_label": "glm-5.3-flash",
  "main_reserve_mib_values_unordered": [
    4096,
    4096
  ]
}
```

Pinned model revision recorded: yes. Source receipt labels, hashes and object locators are retained in [configurations.json](../configurations.json).

</details>

<details>
<summary>cfg-ee63ac1fcc5f0315f205</summary>

```json
{
  "kind": "tabby",
  "gpu_counts": [
    3
  ],
  "context": 500000,
  "cache_tokens": 983040,
  "cache_mode": "Q8",
  "draft_cache_mode": "Q8",
  "draft_mode": "mtp",
  "draft_tokens": 1,
  "max_sessions": 8,
  "chunk_size": 512,
  "reserve_mib": 3072,
  "ram_kv_mib": 32768,
  "ram_recurrent_mib": 16384,
  "dynamic_draft": false,
  "power_watts": 200,
  "host_memory_gib": 80,
  "host_swap_gib": 0,
  "min_vram_mib_per_gpu": 65530,
  "min_effective_vram_mib": 196000,
  "model_repository": "turboderp/GLM-5.3-Flash-exl3",
  "model_revision": "2a30229e67012798ba9f0cd832bb78abf4c363d5",
  "draft_repository": null,
  "draft_revision": null,
  "recorded_runtime_label": null,
  "served_model_label": "glm-5.3-flash",
  "main_reserve_mib_values_unordered": [
    4096,
    4096
  ]
}
```

Pinned model revision recorded: yes. Source receipt labels, hashes and object locators are retained in [configurations.json](../configurations.json).

</details>

## Retained Measurements

| Profile / Wave | Layout; Draft / Tokens | Requests | Input tokens/request | Accepted output tokens/request | Cache / Reused input tokens | Context / GPU pool tokens | Shared decode tok/s total | Client after-first-token estimate tok/s | Whole-wave output tok/s | Median TTFT, s | Source report |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [glm53-capacity3-upper](glm53-capacity3-upper.md)<br>wave-5f1d511aa03762fc25f5 | layout unspecified; mtp / 1 | 1 | 5,185 | 1,024 | cached_prefix; reused 4,096 | 500,000 / 1,048,576 | Not recorded | Not recorded | 32.56 | 2.16 | Failed / partial |
| [glm53-capacity3-upper](glm53-capacity3-upper.md)<br>wave-733a16b30fbc033c07a6 | layout unspecified; mtp / 1 | 2 | 499,572 to 499,588 | 19 | cached_prefix; reused 499,456 | 500,000 / 1,048,576 | Not recorded | Not recorded | 7.55 | 3.43 | Pass |
| [glm53-capacity3-upper](glm53-capacity3-upper.md)<br>wave-80023f49fffdff846bfd | layout unspecified; mtp / 1 | 1 | 4,149 | 512 | cold; reused 0 | 500,000 / 1,048,576 | 37.79 | Not recorded | 26.42 | 5.91 | Pass |
| [glm53-capacity3-upper](glm53-capacity3-upper.md)<br>wave-8e03e0f004e23f827120 | layout unspecified; mtp / 1 | 8 | 2,098 to 8,254 | 512 | cold; reused 0 | 500,000 / 1,048,576 | 67.02 | Not recorded | 38.61 | 40.07 | Pass |
| [glm53-capacity3-upper](glm53-capacity3-upper.md)<br>wave-b0431d3e5ec6491f82e8 | layout unspecified; mtp / 1 | 1 | 4,148 | 1,024 | cold; reused 0 | 500,000 / 1,048,576 | 36.80 | Not recorded | 30.47 | 5.90 | Failed / partial |
| [glm53-capacity3-upper](glm53-capacity3-upper.md)<br>wave-b295c1a3918c6edcf36b | layout unspecified; mtp / 1 | 1 | 4,658 | 512 | cached_prefix; reused 4,096 | 500,000 / 1,048,576 | 37.80 | Not recorded | 34.45 | 1.47 | Pass |
| [glm53-capacity3-upper](glm53-capacity3-upper.md)<br>wave-d0965d3d6779828be469 | layout unspecified; mtp / 1 | 8 | 2,607 to 8,764 | 512 | cached_prefix; reused 2,048 to 8,192 | 500,000 / 1,048,576 | 63.24 | Not recorded | 54.61 | 10.62 | Pass |
| [glm53-capacity3-upper](glm53-capacity3-upper.md)<br>wave-f89ca56ca299a168d623 | layout unspecified; mtp / 1 | 2 | 499,524 | 39 to 55 | cold; reused 0 | 500,000 / 1,048,576 | Not recorded | Not recorded | 0.08 | 1,182.75 | Pass |

Rates are whole-wave totals over the stated request count. A wave may span multiple independent model instances; [measurements.json](../measurements.json) retains their contributions and the exact configuration IDs. Do not interpret a multi-instance total as one card's rate.

A dash in shared decode means no qualified synchronized interval is available. Whole-wave throughput includes prefill and queueing. A valid decode interval can survive inside an overall failed or partial check; the source-report outcome is preserved. No rows are averaged.

## Bounded Checks

| Check | Reported outcome | Retained counts / flags |
| --- | --- | --- |
| check-3fd796d0c269b6851ddd | Pass | {"passed":true,"recurrent_restores":2,"restored_pages":671} |
| check-72be88b518f1ada54efd | Pass | {"passed":true,"replayed_history_tokens":[68,68]} |
| check-8844a1f587f7110234f9 | Pass | {"passed":true} |
| check-8ab78805523e5ec08b6c | Pass | {"context":500000,"passed":true,"replayed_history_tokens":[68,68]} |
| check-b835d351d6246e40c3df | Pass | {"passed":true,"replayed_history_tokens":[68,68],"input_tokens":[499522,499522]} |

These checks retain their reported scope. A context/allocation/retrieval check is not a general quality score or a speed qualification at that context. Exact flags and provenance are in [checks.json](../checks.json).

## Additional Test Results

| Result / Source | Profile | Evidence type | Reported outcome | Retained values | Configuration binding |
| --- | --- | --- | --- | --- | --- |
| [result-066b21f6e09234227104](../observations.json)<br>source-8faef03ab51b268452622ea9.json<br>`/after_burst/cache` | [glm53-capacity3-upper](glm53-capacity3-upper.md) | test outcome | Outcome unspecified | cached_tokens=1,044,224 tokens | Recorded configuration/job |
| [result-1d4f0a0a5b124b363a23](../observations.json)<br>source-ecb3cb0d12e0011430beeea8.json<br>`/stages/0` | [glm53-capacity3-upper](glm53-capacity3-upper.md) | test outcome | Pass | replayed_history_tokens=68 tokens | Recorded configuration/job |
| [result-3fa613bb4bcd18d4b31e](../observations.json)<br>source-3e5c8c05e9b34c48d9f08471.json<br>`/totals` | [glm53-capacity3-upper](glm53-capacity3-upper.md) | context allocation | Outcome unspecified | cached_tokens=0 tokens; generated_tokens=0 accepted tokens; prompt_tokens=0 tokens; recurrent_restores=0 checkpoints | Recorded configuration/job |
| [result-6049d18bee7149b99dd0](../observations.json)<br>source-6988af215b04aaed11f1e161.json<br>`/` | [glm53-capacity3-upper](glm53-capacity3-upper.md) | test outcome | Outcome unspecified | host_memory_peak_bytes=83,221,233,664 bytes; rss_peak_bytes=49,244,073,984 bytes | Recorded configuration/job |
| [result-60cebebf5acd3799e410](../observations.json)<br>source-42585df0343f249016faa381.json<br>`/single/warm` | [glm53-capacity3-upper](glm53-capacity3-upper.md) | test outcome | Outcome unspecified | generated_tps=37.80 accepted tokens/s | Exact configuration unresolved |
| [result-6600c98511db2daa6e14](../observations.json)<br>source-8faef03ab51b268452622ea9.json<br>`/after_cold` | [glm53-capacity3-upper](glm53-capacity3-upper.md) | test outcome | Outcome unspecified | context=500,000 tokens | Recorded configuration/job |
| [result-700c65886358a3e08f0a](../observations.json)<br>source-ecb3cb0d12e0011430beeea8.json<br>`/stages/0/cold` | [glm53-capacity3-upper](glm53-capacity3-upper.md) | test outcome | Outcome unspecified | end_to_end_output_tps=0.08 accepted tokens/s; generated_tokens=94 accepted tokens; wall_seconds=1,185.16 s | Recorded configuration/job |
| [result-736e260a4374aa2fb90b](../observations.json)<br>source-1f7e912924ca8a7e935b5d50.json<br>`/` | [glm53-capacity3-upper](glm53-capacity3-upper.md) | test outcome | Pass | context=500,000 tokens; replayed_history_tokens=68 tokens | Recorded configuration/job |
| [result-87c86a69f06d62d04aa8](../observations.json)<br>source-42585df0343f249016faa381.json<br>`/eight_concurrent/warm` | [glm53-capacity3-upper](glm53-capacity3-upper.md) | test outcome | Outcome unspecified | generated_tps=63.24 accepted tokens/s | Exact configuration unresolved |
| [result-8a6e21b5ab94817633cd](../observations.json)<br>source-3e5c8c05e9b34c48d9f08471.json<br>`/cache` | [glm53-capacity3-upper](glm53-capacity3-upper.md) | test outcome | Outcome unspecified | cached_tokens=0 tokens | Recorded configuration/job |
| [result-8e7c8c67b7199c9c48a5](../observations.json)<br>source-42585df0343f249016faa381.json<br>`/single/cold` | [glm53-capacity3-upper](glm53-capacity3-upper.md) | test outcome | Outcome unspecified | generated_tps=37.79 accepted tokens/s | Exact configuration unresolved |
| [result-98343b0b42529c7d4e3f](../observations.json)<br>source-dfc9ee1889c68ecc7323c193.json<br>`/cold/replicas/0/rates` | [glm53-capacity3-upper](glm53-capacity3-upper.md) | test outcome | Outcome unspecified | end_to_end_output_tps=38.61 accepted tokens/s; generated_tokens=4,096 accepted tokens; wall_seconds=106.09 s | Recorded configuration/job |
| [result-9965135d293086f43300](../observations.json)<br>source-d54d32e250cac470627b9e16.json<br>`/warm/replicas/0/rates` | [glm53-capacity3-upper](glm53-capacity3-upper.md) | test outcome | Outcome unspecified | end_to_end_output_tps=32.56 accepted tokens/s; generated_tokens=1,024 accepted tokens; wall_seconds=31.45 s | Recorded configuration/job |
| [result-a26c9b2648ce90a86a4c](../observations.json)<br>source-7373a3eb1757264f923a91b6.json<br>`/cold/replicas/0/rates` | [glm53-capacity3-upper](glm53-capacity3-upper.md) | test outcome | Outcome unspecified | end_to_end_output_tps=26.42 accepted tokens/s; generated_tokens=512 accepted tokens; wall_seconds=19.38 s | Recorded configuration/job |
| [result-af5e2a6d2d9ad1ed385f](../observations.json)<br>source-8faef03ab51b268452622ea9.json<br>`/after_cold/totals` | [glm53-capacity3-upper](glm53-capacity3-upper.md) | context allocation | Outcome unspecified | cached_tokens=0 tokens; generated_tokens=172 accepted tokens; prompt_tokens=999,562 tokens; recurrent_restores=0 checkpoints | Recorded configuration/job |
| [result-b7b9ac9e1f61c5b6b8eb](../observations.json)<br>source-ecb3cb0d12e0011430beeea8.json<br>`/` | [glm53-capacity3-upper](glm53-capacity3-upper.md) | context allocation | Pass | recurrent_restores=2 checkpoints; restored_pages=671 pages | Recorded configuration/job |
| [result-bf10fb9c83e82bfa37b8](../observations.json)<br>source-8faef03ab51b268452622ea9.json<br>`/after_burst/totals` | [glm53-capacity3-upper](glm53-capacity3-upper.md) | context allocation | Outcome unspecified | cached_tokens=0 tokens; generated_tokens=684 accepted tokens; prompt_tokens=1,131,306 tokens; recurrent_restores=0 checkpoints | Recorded configuration/job |
| [result-c246d66bd45a5d22c0f4](../observations.json)<br>source-7373a3eb1757264f923a91b6.json<br>`/warm/replicas/0/rates` | [glm53-capacity3-upper](glm53-capacity3-upper.md) | test outcome | Outcome unspecified | end_to_end_output_tps=34.45 accepted tokens/s; generated_tokens=512 accepted tokens; wall_seconds=14.86 s | Recorded configuration/job |
| [result-cf90bb9e407e0e5974e8](../observations.json)<br>source-3e5c8c05e9b34c48d9f08471.json<br>`/` | [glm53-capacity3-upper](glm53-capacity3-upper.md) | test outcome | Outcome unspecified | context=500,000 tokens | Recorded configuration/job |
| [result-d343810496895fdb7871](../observations.json)<br>source-ecb3cb0d12e0011430beeea8.json<br>`/stages/0/warm` | [glm53-capacity3-upper](glm53-capacity3-upper.md) | test outcome | Outcome unspecified | end_to_end_output_tps=7.55 accepted tokens/s; generated_tokens=38 accepted tokens; wall_seconds=5.03 s | Recorded configuration/job |
| [result-d5f2f791b24bbf7d6dbc](../observations.json)<br>source-8faef03ab51b268452622ea9.json<br>`/after_cold/cache` | [glm53-capacity3-upper](glm53-capacity3-upper.md) | test outcome | Outcome unspecified | cached_tokens=998,912 tokens | Recorded configuration/job |
| [result-d884660562b9502110aa](../observations.json)<br>source-42585df0343f249016faa381.json<br>`/eight_concurrent/cold` | [glm53-capacity3-upper](glm53-capacity3-upper.md) | test outcome | Outcome unspecified | generated_tps=67.02 accepted tokens/s | Exact configuration unresolved |
| [result-ed055a2e7cacb444c279](../observations.json)<br>source-d54d32e250cac470627b9e16.json<br>`/cold/replicas/0/rates` | [glm53-capacity3-upper](glm53-capacity3-upper.md) | test outcome | Outcome unspecified | end_to_end_output_tps=30.47 accepted tokens/s; generated_tokens=1,024 accepted tokens; wall_seconds=33.61 s | Recorded configuration/job |
| [result-f01fa893e15bf60a5b46](../observations.json)<br>source-8faef03ab51b268452622ea9.json<br>`/after_burst` | [glm53-capacity3-upper](glm53-capacity3-upper.md) | test outcome | Outcome unspecified | context=500,000 tokens | Recorded configuration/job |
| [result-f25ab5ce965243521fdc](../observations.json)<br>source-dfc9ee1889c68ecc7323c193.json<br>`/warm/replicas/0/rates` | [glm53-capacity3-upper](glm53-capacity3-upper.md) | test outcome | Outcome unspecified | end_to_end_output_tps=54.61 accepted tokens/s; generated_tokens=4,096 accepted tokens; wall_seconds=75.00 s | Recorded configuration/job |

These are saved result records, including failures and bounded checks. Copies, individual requests, report summaries and regrading can overlap; their counts are not independent test repetitions. Open each result for exact values, units, configuration binding and source receipts.

There are 2 retained lifecycle records. Their states, exit codes and configuration IDs remain in [catalog.json](../catalog.json); they do not supply missing benchmark results.

[Full archive](../../README.md) | [All retained waves](../RESULTS.md) | [Data definitions](../DATA.md) | [Recommended recipes](../../../README.md)
