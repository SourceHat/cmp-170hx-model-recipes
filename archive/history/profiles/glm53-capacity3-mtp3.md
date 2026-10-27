# glm53-capacity3-mtp3

**Historical record. Decode interval measured.**

Model family: GLM 5.3 Flash.

Recorded archive reason: Historical capacity, fit or control configuration; later DFlash2 and MTP variants have separate records.

Historical configurations are provided for comparison. The [recommended recipes](../../../README.md) include supported launch scripts.

Current recipes using the same recorded checkpoint repository: [glm-5.3-flash-mtp1-tp3](../../../recipes/glm-5.3-flash-mtp1-tp3/README.md). Context, cache and runtime versions can differ.

## Saved Configuration Versions

Each configuration ID identifies a distinct original settings record. Deployment fields are omitted; versions can have identical published settings after that omission. Upstream runtime commits remain unspecified where the source retained only an integration label.

| Configuration | Recorded artifact / source | Configured card counts | Context tokens | GPU pool tokens | Slots | Draft mode / tokens |
| --- | --- | --- | --- | --- | --- | --- |
| cfg-611abf7cbfbfcbad4a12 | [turboderp/GLM-5.3-Flash-exl3@2a30229e67](https://huggingface.co/turboderp/GLM-5.3-Flash-exl3/tree/2a30229e67012798ba9f0cd832bb78abf4c363d5) | 3 | 500,000 | 1,048,576 | 8 | mtp / 3 |

Card counts are saved configuration choices, not a claim that every allowed placement was measured. A derived view can differ from its pinned download source.

<details>
<summary>cfg-611abf7cbfbfcbad4a12</summary>

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
  "draft_tokens": 3,
  "max_sessions": 8,
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
| [glm53-capacity3-mtp3](glm53-capacity3-mtp3.md)<br>wave-06be4a094fbd398b1162 | layout unspecified; mtp / 3 | 4 | 2,611 to 8,764 | 512 | cached_prefix; reused 2,048 to 8,192 | 500,000 / 1,048,576 | 55.63 | Not recorded | 48.76 | 5.74 | Pass |
| [glm53-capacity3-mtp3](glm53-capacity3-mtp3.md)<br>wave-7522c275ccaf95a35afb | layout unspecified; mtp / 3 | 4 | 2,099 to 8,255 | 512 | cold; reused 0 | 500,000 / 1,048,576 | 58.09 | Not recorded | 30.82 | 28.51 | Pass |
| [glm53-capacity3-mtp3](glm53-capacity3-mtp3.md)<br>wave-7ca9b191e04231b028cc | layout unspecified; mtp / 3 | 8 | 2,607 to 8,768 | 512 | cached_prefix; reused 2,048 to 8,192 | 500,000 / 1,048,576 | 86.50 | Not recorded | 70.43 | 10.74 | Pass |
| [glm53-capacity3-mtp3](glm53-capacity3-mtp3.md)<br>wave-898bf5aa0243fbd455b9 | layout unspecified; mtp / 3 | 8 | 2,099 to 8,255 | 512 | cold; reused 0 | 500,000 / 1,048,576 | 94.00 | Not recorded | 45.48 | 40.39 | Pass |

Rates are whole-wave totals over the stated request count. A wave may span multiple independent model instances; [measurements.json](../measurements.json) retains their contributions and the exact configuration IDs. Do not interpret a multi-instance total as one card's rate.

A dash in shared decode means no qualified synchronized interval is available. Whole-wave throughput includes prefill and queueing. A valid decode interval can survive inside an overall failed or partial check; the source-report outcome is preserved. No rows are averaged.

## Bounded Checks

| Check | Reported outcome | Retained counts / flags |
| --- | --- | --- |
| check-b3501b3cbf2cad038575 | Pass | {"passed":true} |

These checks retain their reported scope. A context/allocation/retrieval check is not a general quality score or a speed qualification at that context. Exact flags and provenance are in [checks.json](../checks.json).

## Additional Test Results

| Result / Source | Profile | Evidence type | Reported outcome | Retained values | Configuration binding |
| --- | --- | --- | --- | --- | --- |
| [result-11c0499071bb7a9358b5](../observations.json)<br>source-7500e73938d9cde8c2606813.json<br>`/warm/replicas/0/rates` | [glm53-capacity3-mtp3](glm53-capacity3-mtp3.md) | test outcome | Outcome unspecified | end_to_end_output_tps=70.43 accepted tokens/s; generated_tokens=4,096 accepted tokens; wall_seconds=58.15 s | Recorded configuration/job |
| [result-64027287de44aa2d709c](../observations.json)<br>source-771164f920a9d1c4ca64bc86.json<br>`/cold/replicas/0/rates` | [glm53-capacity3-mtp3](glm53-capacity3-mtp3.md) | test outcome | Outcome unspecified | end_to_end_output_tps=30.82 accepted tokens/s; generated_tokens=2,048 accepted tokens; wall_seconds=66.45 s | Recorded configuration/job |
| [result-82a224ac9ac2e5b20666](../observations.json)<br>source-771164f920a9d1c4ca64bc86.json<br>`/warm/replicas/0/rates` | [glm53-capacity3-mtp3](glm53-capacity3-mtp3.md) | test outcome | Outcome unspecified | end_to_end_output_tps=48.76 accepted tokens/s; generated_tokens=2,048 accepted tokens; wall_seconds=42.00 s | Recorded configuration/job |
| [result-f522fb14fea2d44a5ac7](../observations.json)<br>source-7500e73938d9cde8c2606813.json<br>`/cold/replicas/0/rates` | [glm53-capacity3-mtp3](glm53-capacity3-mtp3.md) | test outcome | Outcome unspecified | end_to_end_output_tps=45.48 accepted tokens/s; generated_tokens=4,096 accepted tokens; wall_seconds=90.06 s | Recorded configuration/job |

These are saved result records, including failures and bounded checks. Copies, individual requests, report summaries and regrading can overlap; their counts are not independent test repetitions. Open each result for exact values, units, configuration binding and source receipts.

There are 1 retained lifecycle records. Their states, exit codes and configuration IDs remain in [catalog.json](../catalog.json); they do not supply missing benchmark results.

[Full archive](../../README.md) | [All retained waves](../RESULTS.md) | [Data definitions](../DATA.md) | [Recommended recipes](../../../README.md)
