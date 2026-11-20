# qwen-flash-next-mtp2-layer-split

**Historical record. Additional test results; no matched decode wave.**

Model family: Qwen 3.8 Flash Next.

Historical configurations are provided for comparison. The [recommended recipes](../../../README.md) include supported launch scripts.

Current recipes using the same recorded checkpoint repository: [qwen-flash-next-mtp2-layer-split](../../../recipes/qwen-flash-next-mtp2-layer-split/README.md). Context, cache and runtime versions can differ.

## Saved Configuration Versions

Each configuration ID identifies a distinct original settings record. Deployment fields are omitted; versions can have identical published settings after that omission. Upstream runtime commits remain unspecified where the source retained only an integration label.

| Configuration | Recorded artifact / source | Configured card counts | Context tokens | GPU pool tokens | Slots | Draft mode / tokens |
| --- | --- | --- | --- | --- | --- | --- |
| cfg-03f6b388d8aaf03c6ec4 | [turboderp/Qwen3.8-Flash-Next-exl3@d2e238feca](https://huggingface.co/turboderp/Qwen3.8-Flash-Next-exl3/tree/d2e238feca4c1c4d966943117356d8a42c2f4dcb) | 2 | 262,144 | 1,356,032 | 6 | mtp / 2 |
| cfg-a934cd648727b84b8188 | [turboderp/Qwen3.8-Flash-Next-exl3@d2e238feca](https://huggingface.co/turboderp/Qwen3.8-Flash-Next-exl3/tree/d2e238feca4c1c4d966943117356d8a42c2f4dcb) | 2 | 262,144 | 1,356,032 | 6 | mtp / 2 |

Card counts are saved configuration choices, not a claim that every allowed placement was measured. A derived view can differ from its pinned download source.

<details>
<summary>cfg-03f6b388d8aaf03c6ec4</summary>

```json
{
  "kind": "tabby",
  "gpu_counts": [
    2
  ],
  "context": 262144,
  "cache_tokens": 1356032,
  "cache_mode": "Q8",
  "draft_cache_mode": "Q8",
  "draft_mode": "mtp",
  "draft_tokens": 2,
  "max_sessions": 6,
  "chunk_size": 512,
  "reserve_mib": 2048,
  "ram_kv_mib": 8192,
  "ram_recurrent_mib": 16384,
  "ngram_ram": true,
  "dynamic_draft": false,
  "output_chunk_tokens": 4096,
  "power_watts": 200,
  "host_memory_gib": 80,
  "host_swap_gib": 0,
  "min_vram_mib_per_gpu": 65530,
  "min_effective_vram_mib": 131060,
  "parallelism": "layer_split",
  "transport": "host",
  "host_backing": "ordinary",
  "model_repository": "turboderp/Qwen3.8-Flash-Next-exl3",
  "model_revision": "d2e238feca4c1c4d966943117356d8a42c2f4dcb",
  "draft_repository": null,
  "draft_revision": null,
  "recorded_runtime_label": null,
  "served_model_label": "qwen3.8-flash-next",
  "main_reserve_mib_values_unordered": []
}
```

Pinned model revision recorded: yes. Source receipt labels, hashes and object locators are retained in [configurations.json](../configurations.json).

</details>

<details>
<summary>cfg-a934cd648727b84b8188</summary>

```json
{
  "kind": "tabby",
  "gpu_counts": [
    2
  ],
  "context": 262144,
  "cache_tokens": 1356032,
  "cache_mode": "Q8",
  "draft_cache_mode": "Q8",
  "draft_mode": "mtp",
  "draft_tokens": 2,
  "max_sessions": 6,
  "chunk_size": 512,
  "reserve_mib": 2048,
  "ram_kv_mib": 8192,
  "ram_recurrent_mib": 16384,
  "ngram_ram": true,
  "dynamic_draft": false,
  "output_chunk_tokens": 4096,
  "power_watts": 200,
  "host_memory_gib": 80,
  "host_swap_gib": 0,
  "min_vram_mib_per_gpu": 65530,
  "min_effective_vram_mib": 131060,
  "parallelism": "layer_split",
  "transport": "host",
  "host_backing": "ordinary",
  "model_repository": "turboderp/Qwen3.8-Flash-Next-exl3",
  "model_revision": "d2e238feca4c1c4d966943117356d8a42c2f4dcb",
  "draft_repository": null,
  "draft_revision": null,
  "recorded_runtime_label": null,
  "served_model_label": "qwen3.8-flash-next",
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
| [result-4d6e15ddf7db14c57126](../observations.json)<br>source-797606345fa45914fcd85b71.json<br>`/profiles/qwen-flash-next-mtp2-layer-split` | [qwen-flash-next-mtp2-layer-split](qwen-flash-next-mtp2-layer-split.md) | context allocation | Outcome unspecified | pool=1,356,032 tokens; draft KV=1,909,293,056 bytes; main KV=22,911,516,672 bytes; allocator_reserved_GiB=60.67<br>59.59; free_GiB=2.81<br>2.63; peak_total_GiB=59.65<br>59.35 | Recorded configuration/job |
| [result-5c03d9af12e49230f1ed](../observations.json)<br>source-797606345fa45914fcd85b71.json<br>`/profiles/qwen-flash-next-mtp2-layer-split/old_speed/single-32768` | [qwen-flash-next-mtp2-layer-split](qwen-flash-next-mtp2-layer-split.md) | test outcome | Outcome unspecified | request_count=1 requests | Recorded configuration/job |
| [result-5d5e1bd798d991195640](../observations.json)<br>source-e656b2f801b18836fcba6eee.json<br>`/flash_final_ad026/cases/0/speed/concurrent` | [configuration-a934cd648727b84b8188](configuration-a934cd648727b84b8188.md)<br>[qwen-flash-next-mtp2-layer-split](qwen-flash-next-mtp2-layer-split.md) | test outcome | Outcome unspecified | request_count=6 requests | Recorded configuration/job |
| [result-7ffe26f1fc0b8767b7a8](../observations.json)<br>source-e656b2f801b18836fcba6eee.json<br>`/flash_final_ad026/cases/0/speed/single` | [configuration-a934cd648727b84b8188](configuration-a934cd648727b84b8188.md)<br>[qwen-flash-next-mtp2-layer-split](qwen-flash-next-mtp2-layer-split.md) | test outcome | Outcome unspecified | request_count=1 requests | Recorded configuration/job |
| [result-e58ff60e9f7aa74f93e7](../observations.json)<br>source-797606345fa45914fcd85b71.json<br>`/profiles/qwen-flash-next-mtp2-layer-split/final` | [qwen-flash-next-mtp2-layer-split](qwen-flash-next-mtp2-layer-split.md) | context allocation | Outcome unspecified | resident_pool_tokens=1,356,032 tokens | Recorded configuration/job |
| [result-f729dfa084ead77779cd](../observations.json)<br>source-797606345fa45914fcd85b71.json<br>`/profiles/qwen-flash-next-mtp2-layer-split/old_speed/concurrent-32768` | [qwen-flash-next-mtp2-layer-split](qwen-flash-next-mtp2-layer-split.md) | test outcome | Outcome unspecified | request_count=6 requests | Recorded configuration/job |

These are saved result records, including failures and bounded checks. Copies, individual requests, report summaries and regrading can overlap; their counts are not independent test repetitions. Open each result for exact values, units, configuration binding and source receipts.

[Full archive](../../README.md) | [All retained waves](../RESULTS.md) | [Data definitions](../DATA.md) | [Recommended recipes](../../../README.md)
