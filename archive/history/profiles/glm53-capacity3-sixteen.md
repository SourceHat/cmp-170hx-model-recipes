# glm53-capacity3-sixteen

**Historical record. Decode interval measured.**

Model family: GLM 5.3 Flash.

Recorded archive reason: Historical capacity, fit or control configuration; later DFlash2 and MTP variants have separate records.

Historical configurations are provided for comparison. The [recommended recipes](../../../README.md) include supported launch scripts.

Current recipes using the same recorded checkpoint repository: [glm-5.3-flash-mtp1-tp3](../../../recipes/glm-5.3-flash-mtp1-tp3/README.md). Context, cache and runtime versions can differ.

## Saved Configuration Versions

Each configuration ID identifies a distinct original settings record. Deployment fields are omitted; versions can have identical published settings after that omission. Upstream runtime commits remain unspecified where the source retained only an integration label.

| Configuration | Recorded artifact / source | Configured card counts | Context tokens | GPU pool tokens | Slots | Draft mode / tokens |
| --- | --- | --- | --- | --- | --- | --- |
| cfg-01c2d6858251c54b490b | [turboderp/GLM-5.3-Flash-exl3@2a30229e67](https://huggingface.co/turboderp/GLM-5.3-Flash-exl3/tree/2a30229e67012798ba9f0cd832bb78abf4c363d5) | 3 | 500,000 | 1,048,576 | 16 | mtp / 1 |

Card counts are saved configuration choices, not a claim that every allowed placement was measured. A derived view can differ from its pinned download source.

<details>
<summary>cfg-01c2d6858251c54b490b</summary>

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
  "max_sessions": 16,
  "chunk_size": 512,
  "reserve_mib": 1792,
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
| [glm53-capacity3-sixteen](glm53-capacity3-sixteen.md)<br>wave-0e29672caa8b709aa99c | layout unspecified; mtp / 1 | 16 | 2,605 to 8,769 | 512 | cached_prefix; reused 2,048 to 8,192 | 500,000 / 1,048,576 | 95.42 | Not recorded | 76.98 | 21.29 | Pass |
| [glm53-capacity3-sixteen](glm53-capacity3-sixteen.md)<br>wave-35e29ca8d14894578bbf | layout unspecified; mtp / 1 | 8 | 2,605 to 8,762 | 512 | cached_prefix; reused 2,048 to 8,192 | 500,000 / 1,048,576 | 63.73 | Not recorded | 55.01 | 10.63 | Pass |
| [glm53-capacity3-sixteen](glm53-capacity3-sixteen.md)<br>wave-70336e01426489a4a46a | layout unspecified; mtp / 1 | 16 | 2,098 to 8,254 | 512 | cold; reused 0 | 500,000 / 1,048,576 | 104.31 | Not recorded | 48.46 | 85.69 | Pass |
| [glm53-capacity3-sixteen](glm53-capacity3-sixteen.md)<br>wave-99728f7c33d11d5750b4 | layout unspecified; mtp / 1 | 4 | 2,098 to 8,254 | 512 | cold; reused 0 | 500,000 / 1,048,576 | 68.26 | Not recorded | 38.80 | 17.65 | Pass |
| [glm53-capacity3-sixteen](glm53-capacity3-sixteen.md)<br>wave-a33ec886839d24610077 | layout unspecified; mtp / 1 | 8 | 2,098 to 8,254 | 512 | cold; reused 0 | 500,000 / 1,048,576 | 66.95 | Not recorded | 38.61 | 38.54 | Pass |
| [glm53-capacity3-sixteen](glm53-capacity3-sixteen.md)<br>wave-d25286afbaea292ca58d | layout unspecified; mtp / 1 | 4 | 2,606 to 8,762 | 512 | cached_prefix; reused 2,048 to 8,192 | 500,000 / 1,048,576 | 67.16 | Not recorded | 57.33 | 5.43 | Pass |

Rates are whole-wave totals over the stated request count. A wave may span multiple independent model instances; [measurements.json](../measurements.json) retains their contributions and the exact configuration IDs. Do not interpret a multi-instance total as one card's rate.

A dash in shared decode means no qualified synchronized interval is available. Whole-wave throughput includes prefill and queueing. A valid decode interval can survive inside an overall failed or partial check; the source-report outcome is preserved. No rows are averaged.

## Bounded Checks

| Check | Reported outcome | Retained counts / flags |
| --- | --- | --- |
| check-8d41abbf715a51b6c1ab | Pass | {"passed":true} |

These checks retain their reported scope. A context/allocation/retrieval check is not a general quality score or a speed qualification at that context. Exact flags and provenance are in [checks.json](../checks.json).

## Additional Test Results

| Result / Source | Profile | Evidence type | Reported outcome | Retained values | Configuration binding |
| --- | --- | --- | --- | --- | --- |
| [result-4b6eab52b8cfc3e2f5ab](../observations.json)<br>source-7343fe9a78f54da1e37beb3b.json<br>`/warm/replicas/0/rates` | [glm53-capacity3-sixteen](glm53-capacity3-sixteen.md) | test outcome | Outcome unspecified | end_to_end_output_tps=55.01 accepted tokens/s; generated_tokens=4,096 accepted tokens; wall_seconds=74.46 s | Recorded configuration/job |
| [result-5b1e9a984ba93f716aee](../observations.json)<br>source-b32102effc387a94e2897608.json<br>`/cold/replicas/0/rates` | [glm53-capacity3-sixteen](glm53-capacity3-sixteen.md) | test outcome | Outcome unspecified | end_to_end_output_tps=38.80 accepted tokens/s; generated_tokens=2,048 accepted tokens; wall_seconds=52.78 s | Recorded configuration/job |
| [result-cb744725987aa1b025a0](../observations.json)<br>source-b32102effc387a94e2897608.json<br>`/warm/replicas/0/rates` | [glm53-capacity3-sixteen](glm53-capacity3-sixteen.md) | test outcome | Outcome unspecified | end_to_end_output_tps=57.33 accepted tokens/s; generated_tokens=2,048 accepted tokens; wall_seconds=35.72 s | Recorded configuration/job |
| [result-e3667ca190d10310ffe6](../observations.json)<br>source-7343fe9a78f54da1e37beb3b.json<br>`/cold/replicas/0/rates` | [glm53-capacity3-sixteen](glm53-capacity3-sixteen.md) | test outcome | Outcome unspecified | end_to_end_output_tps=38.61 accepted tokens/s; generated_tokens=4,096 accepted tokens; wall_seconds=106.09 s | Recorded configuration/job |
| [result-e9aeaaceeb8c7b5fbcd2](../observations.json)<br>source-25a347121e1dc14c941f2d28.json<br>`/warm/replicas/0/rates` | [glm53-capacity3-sixteen](glm53-capacity3-sixteen.md) | test outcome | Outcome unspecified | end_to_end_output_tps=76.98 accepted tokens/s; generated_tokens=8,192 accepted tokens; wall_seconds=106.41 s | Recorded configuration/job |
| [result-feb6927c25add770c741](../observations.json)<br>source-25a347121e1dc14c941f2d28.json<br>`/cold/replicas/0/rates` | [glm53-capacity3-sixteen](glm53-capacity3-sixteen.md) | test outcome | Outcome unspecified | end_to_end_output_tps=48.46 accepted tokens/s; generated_tokens=8,192 accepted tokens; wall_seconds=169.06 s | Recorded configuration/job |

These are saved result records, including failures and bounded checks. Copies, individual requests, report summaries and regrading can overlap; their counts are not independent test repetitions. Open each result for exact values, units, configuration binding and source receipts.

There are 1 retained lifecycle records. Their states, exit codes and configuration IDs remain in [catalog.json](../catalog.json); they do not supply missing benchmark results.

[Full archive](../../README.md) | [All retained waves](../RESULTS.md) | [Data definitions](../DATA.md) | [Recommended recipes](../../../README.md)
