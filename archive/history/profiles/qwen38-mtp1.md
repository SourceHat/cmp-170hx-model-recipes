# qwen38-mtp1

**Historical record. Legacy / incomplete measurements.**

Model family: Qwen 3.8 27B.

Recorded archive reason: Fit, pilot or control configuration; measured serving variants have separate records.

Historical configurations are provided for comparison. The [recommended recipes](../../../README.md) include supported launch scripts.

Current recipes using the same recorded checkpoint repository: [qwen3.8-27b-exl3](../../../recipes/qwen3.8-27b-exl3/README.md). Context, cache and runtime versions can differ.

## Saved Configuration Versions

Each configuration ID identifies a distinct original settings record. Deployment fields are omitted; versions can have identical published settings after that omission. Upstream runtime commits remain unspecified where the source retained only an integration label.

| Configuration | Recorded artifact / source | Configured card counts | Context tokens | GPU pool tokens | Slots | Draft mode / tokens |
| --- | --- | --- | --- | --- | --- | --- |
| cfg-0ac2797af58c10315e4d | [turboderp/Qwen3.8-27B-exl3@9e4c23cfb2](https://huggingface.co/turboderp/Qwen3.8-27B-exl3/tree/9e4c23cfb23697165b8e2f6da2a1df995f66353c) | 1 | 262,144 | 786,432 | 16 | mtp / 1 |
| cfg-f9e4ba5588e19d03bca4 | [turboderp/Qwen3.8-27B-exl3@9e4c23cfb2](https://huggingface.co/turboderp/Qwen3.8-27B-exl3/tree/9e4c23cfb23697165b8e2f6da2a1df995f66353c) | 1 | 262,144 | 786,432 | 16 | mtp / 1 |

Card counts are saved configuration choices, not a claim that every allowed placement was measured. A derived view can differ from its pinned download source.

<details>
<summary>cfg-0ac2797af58c10315e4d</summary>

```json
{
  "kind": "tabby",
  "gpu_counts": [
    1
  ],
  "context": 262144,
  "cache_tokens": 786432,
  "cache_mode": "Q8",
  "draft_cache_mode": "Q8",
  "draft_mode": "mtp",
  "draft_tokens": 1,
  "max_sessions": 16,
  "chunk_size": 2048,
  "reserve_mib": 4096,
  "ram_kv_mib": 5120,
  "ram_recurrent_mib": 7168,
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

<details>
<summary>cfg-f9e4ba5588e19d03bca4</summary>

```json
{
  "kind": "tabby",
  "gpu_counts": [
    1
  ],
  "context": 262144,
  "cache_tokens": 786432,
  "cache_mode": "Q8",
  "draft_cache_mode": "Q8",
  "draft_mode": "mtp",
  "draft_tokens": 1,
  "max_sessions": 16,
  "chunk_size": 2048,
  "reserve_mib": 4096,
  "ram_kv_mib": 5120,
  "ram_recurrent_mib": 7168,
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

## Retained Measurements

| Profile / Wave | Layout; Draft / Tokens | Requests | Input tokens/request | Accepted output tokens/request | Cache / Reused input tokens | Context / GPU pool tokens | Shared decode tok/s total | Client after-first-token estimate tok/s | Whole-wave output tok/s | Median TTFT, s | Source report |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [qwen38-mtp1](qwen38-mtp1.md)<br>wave-4845356bcc9096bdaada | layout unspecified; mtp / 1 | 16 | 2,068 to 24,583 | 256 | cold; reused 0 | 262,144 / 786,432 | Not recorded | 86.60 | 48.87 | 58.61 | Pass |
| [qwen38-mtp1](qwen38-mtp1.md)<br>wave-7e8e72384f805a1add3e | layout unspecified; mtp / 1 | 16 | 2,346 to 24,866 | 256 | cached_prefix; reused 2,048 to 24,576 | 262,144 / 786,432 | Not recorded | 147.14 | 134.41 | 9.85 | Pass |

Rates are whole-wave totals over the stated request count. A wave may span multiple independent model instances; [measurements.json](../measurements.json) retains their contributions and the exact configuration IDs. Do not interpret a multi-instance total as one card's rate.

A dash in shared decode means no qualified synchronized interval is available. Whole-wave throughput includes prefill and queueing. A valid decode interval can survive inside an overall failed or partial check; the source-report outcome is preserved. No rows are averaged.

## Bounded Checks

| Check | Reported outcome | Retained counts / flags |
| --- | --- | --- |
| check-6f68a23958d4b61faf28 | Failed / partial | {"passed":false,"input_tokens":[24579,24579,16390,16390,2064,2064,2064,2064,2064,2064,2065,2065,2065,2065,2065,2065]} |
| check-807ad3f5d548342b5c54 | Pass | {"passed":true,"input_tokens":[24579,24579,16390,16390,2064,2064,2064,2064,2064,2064,2065,2065,2065,2065,2065,2065]} |
| check-b02c6fc1271fea27ad74 | Pass | {"passed":true} |

These checks retain their reported scope. A context/allocation/retrieval check is not a general quality score or a speed qualification at that context. Exact flags and provenance are in [checks.json](../checks.json).

## Additional Test Results

| Result / Source | Profile | Evidence type | Reported outcome | Retained values | Configuration binding |
| --- | --- | --- | --- | --- | --- |
| [result-12b8c3b503cd7fa423f0](../observations.json)<br>source-5c93e142a285c9fde7fe36b3.json<br>`/after_cold/cache` | [qwen38-mtp1](qwen38-mtp1.md) | test outcome | Outcome unspecified | cached_tokens=110,592 tokens | Recorded configuration/job |
| [result-3b54a2339b6b8825da14](../observations.json)<br>source-5c93e142a285c9fde7fe36b3.json<br>`/after_cold` | [qwen38-mtp1](qwen38-mtp1.md) | test outcome | Outcome unspecified | context=262,144 tokens | Recorded configuration/job |
| [result-8d267ad5ee150e81139c](../observations.json)<br>source-5c93e142a285c9fde7fe36b3.json<br>`/after_cold/totals` | [qwen38-mtp1](qwen38-mtp1.md) | context allocation | Outcome unspecified | cached_tokens=0 tokens; generated_tokens=4,096 accepted tokens; prompt_tokens=106,776 tokens; recurrent_restores=0 checkpoints | Recorded configuration/job |

These are saved result records, including failures and bounded checks. Copies, individual requests, report summaries and regrading can overlap; their counts are not independent test repetitions. Open each result for exact values, units, configuration binding and source receipts.

There are 2 retained lifecycle records. Their states, exit codes and configuration IDs remain in [catalog.json](../catalog.json); they do not supply missing benchmark results.

[Full archive](../../README.md) | [All retained waves](../RESULTS.md) | [Data definitions](../DATA.md) | [Recommended recipes](../../../README.md)
