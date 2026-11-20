# qwen38-capacity40

**Historical record. Legacy / incomplete measurements.**

Model family: Qwen 3.8 27B.

Recorded archive reason: Fit, pilot or control configuration; measured serving variants have separate records.

Historical configurations are provided for comparison. The [recommended recipes](../../../README.md) include supported launch scripts.

Current recipes using the same recorded checkpoint repository: [qwen3.8-27b-exl3](../../../recipes/qwen3.8-27b-exl3/README.md). Context, cache and runtime versions can differ.

## Saved Configuration Versions

Each configuration ID identifies a distinct original settings record. Deployment fields are omitted; versions can have identical published settings after that omission. Upstream runtime commits remain unspecified where the source retained only an integration label.

| Configuration | Recorded artifact / source | Configured card counts | Context tokens | GPU pool tokens | Slots | Draft mode / tokens |
| --- | --- | --- | --- | --- | --- | --- |
| cfg-15ade383b05e17bd95d4 | [turboderp/Qwen3.8-27B-exl3@9e4c23cfb2](https://huggingface.co/turboderp/Qwen3.8-27B-exl3/tree/9e4c23cfb23697165b8e2f6da2a1df995f66353c) | 1 | 262,144 | 262,144 | 8 | mtp / 3 |
| cfg-17fd44b5b3c1fac21309 | [turboderp/Qwen3.8-27B-exl3@9e4c23cfb2](https://huggingface.co/turboderp/Qwen3.8-27B-exl3/tree/9e4c23cfb23697165b8e2f6da2a1df995f66353c) | 1 | 262,144 | 262,144 | 8 | mtp / 3 |

Card counts are saved configuration choices, not a claim that every allowed placement was measured. A derived view can differ from its pinned download source.

<details>
<summary>cfg-15ade383b05e17bd95d4</summary>

```json
{
  "kind": "tabby",
  "gpu_counts": [
    1
  ],
  "context": 262144,
  "cache_tokens": 262144,
  "cache_mode": "Q8",
  "draft_cache_mode": "Q8",
  "draft_mode": "mtp",
  "draft_tokens": 3,
  "max_sessions": 8,
  "chunk_size": 2048,
  "reserve_mib": 4096,
  "ram_kv_mib": 8192,
  "ram_recurrent_mib": 4096,
  "dynamic_draft": false,
  "power_watts": 200,
  "host_memory_gib": 20,
  "host_swap_gib": 0,
  "min_vram_mib_per_gpu": 40000,
  "min_effective_vram_mib": 40000,
  "model_repository": "turboderp/Qwen3.8-27B-exl3",
  "model_revision": "9e4c23cfb23697165b8e2f6da2a1df995f66353c",
  "draft_repository": null,
  "draft_revision": null,
  "recorded_runtime_label": null,
  "served_model_label": "qwen3.8-27b"
}
```

Pinned model revision recorded: yes. Source receipt labels, hashes and object locators are retained in [configurations.json](../configurations.json).

</details>

<details>
<summary>cfg-17fd44b5b3c1fac21309</summary>

```json
{
  "kind": "tabby",
  "gpu_counts": [
    1
  ],
  "context": 262144,
  "cache_tokens": 262144,
  "cache_mode": "Q8",
  "draft_cache_mode": "Q8",
  "draft_mode": "mtp",
  "draft_tokens": 3,
  "max_sessions": 8,
  "chunk_size": 2048,
  "reserve_mib": 4096,
  "ram_kv_mib": 5120,
  "ram_recurrent_mib": 7168,
  "dynamic_draft": false,
  "power_watts": 200,
  "host_memory_gib": 20,
  "host_swap_gib": 0,
  "min_vram_mib_per_gpu": 40000,
  "min_effective_vram_mib": 40000,
  "model_repository": "turboderp/Qwen3.8-27B-exl3",
  "model_revision": "9e4c23cfb23697165b8e2f6da2a1df995f66353c",
  "draft_repository": null,
  "draft_revision": null,
  "recorded_runtime_label": null,
  "served_model_label": "qwen3.8-27b"
}
```

Pinned model revision recorded: yes. Source receipt labels, hashes and object locators are retained in [configurations.json](../configurations.json).

</details>

## Retained Measurements

| Profile / Wave | Layout; Draft / Tokens | Requests | Input tokens/request | Accepted output tokens/request | Cache / Reused input tokens | Context / GPU pool tokens | Shared decode tok/s total | Client after-first-token estimate tok/s | Whole-wave output tok/s | Median TTFT, s | Source report |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [qwen38-capacity40](qwen38-capacity40.md)<br>wave-24a3a6f55ea8293f9b4b | layout unspecified; mtp / 3 | 1 | 32,826 | 138 | cold; reused 0 | 262,144 / 262,144 | Not recorded | 48.50 | 6.16 | 19.57 | Failed / partial |

Rates are whole-wave totals over the stated request count. A wave may span multiple independent model instances; [measurements.json](../measurements.json) retains their contributions and the exact configuration IDs. Do not interpret a multi-instance total as one card's rate.

A dash in shared decode means no qualified synchronized interval is available. Whole-wave throughput includes prefill and queueing. A valid decode interval can survive inside an overall failed or partial check; the source-report outcome is preserved. No rows are averaged.

## Bounded Checks

| Check | Reported outcome | Retained counts / flags |
| --- | --- | --- |
| check-805e4ca0f606761c3336 | Failed / partial | {"passed":false,"input_tokens":[32822]} |

These checks retain their reported scope. A context/allocation/retrieval check is not a general quality score or a speed qualification at that context. Exact flags and provenance are in [checks.json](../checks.json).

## Additional Test Results

| Result / Source | Profile | Evidence type | Reported outcome | Retained values | Configuration binding |
| --- | --- | --- | --- | --- | --- |
| [result-0e67c9090de34644c59d](../observations.json)<br>source-66f7e43e7db70ea9792b107f.json<br>`/after_cold/cache` | [qwen38-capacity40](qwen38-capacity40.md) | test outcome | Outcome unspecified | cached_tokens=32,768 tokens | Recorded configuration/job |
| [result-5fb2924f65c7c7e57cc0](../observations.json)<br>source-e1e96a1fdfc115f24c4ac265.json<br>`/stages/0/cold` | [qwen38-capacity40](qwen38-capacity40.md) | test outcome | Outcome unspecified | end_to_end_output_tps=6.16 accepted tokens/s; generated_tokens=138 accepted tokens; wall_seconds=22.41 s | Recorded configuration/job |
| [result-7dc914385854b81cac5f](../observations.json)<br>source-66f7e43e7db70ea9792b107f.json<br>`/after_cold` | [qwen38-capacity40](qwen38-capacity40.md) | test outcome | Outcome unspecified | context=262,144 tokens | Recorded configuration/job |
| [result-e6aff71facaee2f0594e](../observations.json)<br>source-66f7e43e7db70ea9792b107f.json<br>`/after_cold/totals` | [qwen38-capacity40](qwen38-capacity40.md) | context allocation | Outcome unspecified | cached_tokens=0 tokens; generated_tokens=138 accepted tokens; prompt_tokens=32,826 tokens; recurrent_restores=0 checkpoints | Recorded configuration/job |

These are saved result records, including failures and bounded checks. Copies, individual requests, report summaries and regrading can overlap; their counts are not independent test repetitions. Open each result for exact values, units, configuration binding and source receipts.

There are 2 retained lifecycle records. Their states, exit codes and configuration IDs remain in [catalog.json](../catalog.json); they do not supply missing benchmark results.

[Full archive](../../README.md) | [All retained waves](../RESULTS.md) | [Data definitions](../DATA.md) | [Recommended recipes](../../../README.md)
