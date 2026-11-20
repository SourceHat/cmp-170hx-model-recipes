# qwen38-dflash2

**Historical record. Legacy / incomplete measurements.**

Model family: Qwen 3.8 27B.

Recorded archive reason: Base Qwen serving pilot; compare separately with the abliterated Orca and mathematical-overlay experiments.

Historical configurations are provided for comparison. The [recommended recipes](../../../README.md) include supported launch scripts.

Current recipes using the same recorded checkpoint repository: [qwen3.8-27b-exl3](../../../recipes/qwen3.8-27b-exl3/README.md). Context, cache and runtime versions can differ.

## Saved Configuration Versions

Each configuration ID identifies a distinct original settings record. Deployment fields are omitted; versions can have identical published settings after that omission. Upstream runtime commits remain unspecified where the source retained only an integration label.

| Configuration | Recorded artifact / source | Configured card counts | Context tokens | GPU pool tokens | Slots | Draft mode / tokens |
| --- | --- | --- | --- | --- | --- | --- |
| cfg-3a22b2b4735052e8a45e | [turboderp/Qwen3.8-27B-exl3@9e4c23cfb2](https://huggingface.co/turboderp/Qwen3.8-27B-exl3/tree/9e4c23cfb23697165b8e2f6da2a1df995f66353c) | 1 | 262,144 | 655,360 | 4 | dflash2 / 7 |
| cfg-5a25ad554ef696101cc7 | [turboderp/Qwen3.8-27B-exl3@9e4c23cfb2](https://huggingface.co/turboderp/Qwen3.8-27B-exl3/tree/9e4c23cfb23697165b8e2f6da2a1df995f66353c) | 1 | 262,144 | 655,360 | 4 | dflash2 / 7 |

Card counts are saved configuration choices, not a claim that every allowed placement was measured. A derived view can differ from its pinned download source.

<details>
<summary>cfg-3a22b2b4735052e8a45e</summary>

```json
{
  "kind": "tabby",
  "gpu_counts": [
    1
  ],
  "context": 262144,
  "cache_tokens": 655360,
  "cache_mode": "Q8",
  "draft_cache_mode": "Q8",
  "draft_mode": "dflash2",
  "draft_tokens": 7,
  "max_sessions": 4,
  "chunk_size": 2048,
  "reserve_mib": 4096,
  "ram_kv_mib": 5120,
  "ram_recurrent_mib": 7168,
  "dynamic_draft": false,
  "power_watts": 200,
  "host_memory_gib": 24,
  "host_swap_gib": 0,
  "min_vram_mib_per_gpu": 60000,
  "min_effective_vram_mib": 60000,
  "model_repository": "turboderp/Qwen3.8-27B-exl3",
  "model_revision": "9e4c23cfb23697165b8e2f6da2a1df995f66353c",
  "draft_repository": null,
  "draft_revision": null,
  "recorded_runtime_label": null,
  "served_model_label": "qwen3.8-27b",
  "power_watts_values_unordered": [
    150,
    175
  ]
}
```

Pinned model revision recorded: yes. Source receipt labels, hashes and object locators are retained in [configurations.json](../configurations.json).

</details>

<details>
<summary>cfg-5a25ad554ef696101cc7</summary>

```json
{
  "kind": "tabby",
  "gpu_counts": [
    1
  ],
  "context": 262144,
  "cache_tokens": 655360,
  "cache_mode": "Q8",
  "draft_cache_mode": "Q8",
  "draft_mode": "dflash2",
  "draft_tokens": 7,
  "max_sessions": 4,
  "chunk_size": 2048,
  "reserve_mib": 4096,
  "ram_kv_mib": 5120,
  "ram_recurrent_mib": 7168,
  "dynamic_draft": false,
  "power_watts": 200,
  "host_memory_gib": 24,
  "host_swap_gib": 0,
  "min_vram_mib_per_gpu": 60000,
  "min_effective_vram_mib": 60000,
  "model_repository": "turboderp/Qwen3.8-27B-exl3",
  "model_revision": "9e4c23cfb23697165b8e2f6da2a1df995f66353c",
  "draft_repository": null,
  "draft_revision": null,
  "recorded_runtime_label": null,
  "served_model_label": "qwen3.8-27b",
  "power_watts_values_unordered": []
}
```

Pinned model revision recorded: yes. Source receipt labels, hashes and object locators are retained in [configurations.json](../configurations.json).

</details>

## Retained Measurements

| Profile / Wave | Layout; Draft / Tokens | Requests | Input tokens/request | Accepted output tokens/request | Cache / Reused input tokens | Context / GPU pool tokens | Shared decode tok/s total | Client after-first-token estimate tok/s | Whole-wave output tok/s | Median TTFT, s | Source report |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [qwen38-dflash2](qwen38-dflash2.md)<br>wave-241d3a502dc2e610beb8 | layout unspecified; dflash2 / 7 | 16 | 2,349 to 24,863 | 256 | cached_prefix; reused 2,048 to 24,576 | 262,144 / 655,360 | Not recorded | 114.81 | 108.63 | 16.37 | Pass |
| [qwen38-dflash2](qwen38-dflash2.md)<br>wave-fe9cb5bca0f47e9dfc04 | layout unspecified; dflash2 / 7 | 16 | 2,068 to 24,583 | 256 | cold; reused 0 | 262,144 / 655,360 | Not recorded | 94.79 | 46.48 | 65.65 | Pass |

Rates are whole-wave totals over the stated request count. A wave may span multiple independent model instances; [measurements.json](../measurements.json) retains their contributions and the exact configuration IDs. Do not interpret a multi-instance total as one card's rate.

A dash in shared decode means no qualified synchronized interval is available. Whole-wave throughput includes prefill and queueing. A valid decode interval can survive inside an overall failed or partial check; the source-report outcome is preserved. No rows are averaged.

## Bounded Checks

| Check | Reported outcome | Retained counts / flags |
| --- | --- | --- |
| check-0d7703415a04c603542d | Pass | {"passed":true,"input_tokens":[24579,24579,16390,16390,2064,2064,2064,2064,2064,2064,2065,2065,2065,2065,2065,2065]} |
| check-8b6e1eda1c10a08f6222 | Pass | {"passed":true} |

These checks retain their reported scope. A context/allocation/retrieval check is not a general quality score or a speed qualification at that context. Exact flags and provenance are in [checks.json](../checks.json).

## Additional Test Results

| Result / Source | Profile | Evidence type | Reported outcome | Retained values | Configuration binding |
| --- | --- | --- | --- | --- | --- |
| [result-0f04a5b840ba92a814f8](../observations.json)<br>source-45ca7e428bc8307951804e8a.json<br>`/after_cold/cache` | [qwen38-dflash2](qwen38-dflash2.md) | test outcome | Outcome unspecified | cached_tokens=110,592 tokens | Recorded configuration/job |
| [result-bc93834f5352b2623092](../observations.json)<br>source-ab89fca7e0f49696d5258b56.json<br>`/profiles/25/current_config` | [qwen38-dflash2](qwen38-dflash2.md) | context allocation | Outcome unspecified | cache_tokens=655,360 tokens; context=262,144 tokens; reserve_mib=4,096 MiB | Recorded configuration/job |
| [result-db371fce480114713fd5](../observations.json)<br>source-45ca7e428bc8307951804e8a.json<br>`/after_cold/totals` | [qwen38-dflash2](qwen38-dflash2.md) | context allocation | Outcome unspecified | cached_tokens=0 tokens; generated_tokens=4,204 accepted tokens; prompt_tokens=106,982 tokens; recurrent_restores=0 checkpoints | Recorded configuration/job |
| [result-e3530f213595cf7ffa2e](../observations.json)<br>source-45ca7e428bc8307951804e8a.json<br>`/after_cold` | [qwen38-dflash2](qwen38-dflash2.md) | test outcome | Outcome unspecified | context=262,144 tokens | Recorded configuration/job |

These are saved result records, including failures and bounded checks. Copies, individual requests, report summaries and regrading can overlap; their counts are not independent test repetitions. Open each result for exact values, units, configuration binding and source receipts.

There are 1 retained lifecycle records. Their states, exit codes and configuration IDs remain in [catalog.json](../catalog.json); they do not supply missing benchmark results.

[Full archive](../../README.md) | [All retained waves](../RESULTS.md) | [Data definitions](../DATA.md) | [Recommended recipes](../../../README.md)
