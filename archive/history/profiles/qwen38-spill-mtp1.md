# qwen38-spill-mtp1

**Historical record. Legacy / incomplete measurements.**

Model family: Qwen 3.8 27B.

Recorded archive reason: Fit, pilot or control configuration; measured serving variants have separate records.

Historical configurations are provided for comparison. The [recommended recipes](../../../README.md) include supported launch scripts.

Current recipes using the same recorded checkpoint repository: [qwen3.8-27b-exl3](../../../recipes/qwen3.8-27b-exl3/README.md). Context, cache and runtime versions can differ.

## Saved Configuration Versions

Each configuration ID identifies a distinct original settings record. Deployment fields are omitted; versions can have identical published settings after that omission. Upstream runtime commits remain unspecified where the source retained only an integration label.

| Configuration | Recorded artifact / source | Configured card counts | Context tokens | GPU pool tokens | Slots | Draft mode / tokens |
| --- | --- | --- | --- | --- | --- | --- |
| cfg-4910ba25cd4281b964cb | [turboderp/Qwen3.8-27B-exl3@9e4c23cfb2](https://huggingface.co/turboderp/Qwen3.8-27B-exl3/tree/9e4c23cfb23697165b8e2f6da2a1df995f66353c) | 1 | 32,768 | 131,072 | 16 | mtp / 1 |
| cfg-d546db1d5f4dfdf28383 | [turboderp/Qwen3.8-27B-exl3@9e4c23cfb2](https://huggingface.co/turboderp/Qwen3.8-27B-exl3/tree/9e4c23cfb23697165b8e2f6da2a1df995f66353c) | 1 | 32,768 | 131,072 | 16 | mtp / 1 |

Card counts are saved configuration choices, not a claim that every allowed placement was measured. A derived view can differ from its pinned download source.

<details>
<summary>cfg-4910ba25cd4281b964cb</summary>

```json
{
  "kind": "tabby",
  "gpu_counts": [
    1
  ],
  "context": 32768,
  "cache_tokens": 131072,
  "cache_mode": "Q8",
  "draft_cache_mode": "Q8",
  "draft_mode": "mtp",
  "draft_tokens": 1,
  "max_sessions": 16,
  "chunk_size": 2048,
  "reserve_mib": 4096,
  "ram_kv_mib": 4096,
  "ram_recurrent_mib": 4096,
  "dynamic_draft": false,
  "power_watts": 200,
  "host_memory_gib": 20,
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

<details>
<summary>cfg-d546db1d5f4dfdf28383</summary>

```json
{
  "kind": "tabby",
  "gpu_counts": [
    1
  ],
  "context": 32768,
  "cache_tokens": 131072,
  "cache_mode": "Q8",
  "draft_cache_mode": "Q8",
  "draft_mode": "mtp",
  "draft_tokens": 1,
  "max_sessions": 16,
  "chunk_size": 2048,
  "reserve_mib": 4096,
  "ram_kv_mib": 4096,
  "ram_recurrent_mib": 4096,
  "dynamic_draft": false,
  "power_watts": 200,
  "host_memory_gib": 20,
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

## Retained Measurements

| Profile / Wave | Layout; Draft / Tokens | Requests | Input tokens/request | Accepted output tokens/request | Cache / Reused input tokens | Context / GPU pool tokens | Shared decode tok/s total | Client after-first-token estimate tok/s | Whole-wave output tok/s | Median TTFT, s | Source report |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [qwen38-spill-mtp1](qwen38-spill-mtp1.md)<br>wave-cb6bbd48c2261afbf707 | layout unspecified; mtp / 1 | 4 | 24,791 | 35 | cached_prefix; reused 24,576 | 32,768 / 131,072 | Not recorded | 31.86 | 24.00 | 4.80 | Pass |
| [qwen38-spill-mtp1](qwen38-spill-mtp1.md)<br>wave-e62e2893f66c6b1be282 | layout unspecified; mtp / 1 | 4 | 24,636 | 137 | cold; reused 0 | 32,768 / 131,072 | Not recorded | 93.12 | 8.71 | 57.79 | Pass |

Rates are whole-wave totals over the stated request count. A wave may span multiple independent model instances; [measurements.json](../measurements.json) retains their contributions and the exact configuration IDs. Do not interpret a multi-instance total as one card's rate.

A dash in shared decode means no qualified synchronized interval is available. Whole-wave throughput includes prefill and queueing. A valid decode interval can survive inside an overall failed or partial check; the source-report outcome is preserved. No rows are averaged.

## Bounded Checks

| Check | Reported outcome | Retained counts / flags |
| --- | --- | --- |
| check-447295411989f1ce7153 | Pass | {"passed":true,"replayed_history_tokens":[60,60,60,60],"input_tokens":[24632,24632,24632,24632]} |

These checks retain their reported scope. A context/allocation/retrieval check is not a general quality score or a speed qualification at that context. Exact flags and provenance are in [checks.json](../checks.json).

## Additional Test Results

| Result / Source | Profile | Evidence type | Reported outcome | Retained values | Configuration binding |
| --- | --- | --- | --- | --- | --- |
| [result-06d376e5a2079fcad0f2](../observations.json)<br>source-7db479677278da434c6b048c.json<br>`/after_cold/totals` | [qwen38-spill-mtp1](qwen38-spill-mtp1.md) | context allocation | Outcome unspecified | cached_tokens=0 tokens; generated_tokens=548 accepted tokens; prompt_tokens=98,544 tokens; recurrent_restores=0 checkpoints | Recorded configuration/job |
| [result-5f89ba7c3915fc7a8d0b](../observations.json)<br>source-7db479677278da434c6b048c.json<br>`/after_cold` | [qwen38-spill-mtp1](qwen38-spill-mtp1.md) | test outcome | Outcome unspecified | context=32,768 tokens | Recorded configuration/job |
| [result-64e6ad3ed27316c490da](../observations.json)<br>source-7db479677278da434c6b048c.json<br>`/after_burst` | [qwen38-spill-mtp1](qwen38-spill-mtp1.md) | test outcome | Outcome unspecified | context=32,768 tokens | Recorded configuration/job |
| [result-6aab36fc1499ad056ce0](../observations.json)<br>source-7db479677278da434c6b048c.json<br>`/after_burst/totals` | [qwen38-spill-mtp1](qwen38-spill-mtp1.md) | context allocation | Outcome unspecified | cached_tokens=0 tokens; generated_tokens=804 accepted tokens; prompt_tokens=230,136 tokens; recurrent_restores=0 checkpoints | Recorded configuration/job |
| [result-844a0e2175eb7c0ba917](../observations.json)<br>source-7db479677278da434c6b048c.json<br>`/after_burst/cache` | [qwen38-spill-mtp1](qwen38-spill-mtp1.md) | test outcome | Outcome unspecified | cached_tokens=129,280 tokens | Recorded configuration/job |
| [result-c90814210d8fd834d37e](../observations.json)<br>source-7db479677278da434c6b048c.json<br>`/after_cold/cache` | [qwen38-spill-mtp1](qwen38-spill-mtp1.md) | test outcome | Outcome unspecified | cached_tokens=98,304 tokens | Recorded configuration/job |

These are saved result records, including failures and bounded checks. Copies, individual requests, report summaries and regrading can overlap; their counts are not independent test repetitions. Open each result for exact values, units, configuration binding and source receipts.

There are 1 retained lifecycle records. Their states, exit codes and configuration IDs remain in [catalog.json](../catalog.json); they do not supply missing benchmark results.

[Full archive](../../README.md) | [All retained waves](../RESULTS.md) | [Data definitions](../DATA.md) | [Recommended recipes](../../../README.md)
