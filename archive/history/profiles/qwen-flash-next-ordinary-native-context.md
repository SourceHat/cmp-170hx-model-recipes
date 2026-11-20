# qwen-flash-next-ordinary-native-context

**Historical record. Additional test results; no matched decode wave.**

Model family: Qwen 3.8 Flash Next.

Recorded archive reason: Ordinary comparison control; speculative choices retained.

Historical configurations are provided for comparison. The [recommended recipes](../../../README.md) include supported launch scripts.

Current recipes using the same recorded checkpoint repository: [qwen-flash-next-mtp2-layer-split](../../../recipes/qwen-flash-next-mtp2-layer-split/README.md). Context, cache and runtime versions can differ.

## Saved Configuration Versions

Each configuration ID identifies a distinct original settings record. Deployment fields are omitted; versions can have identical published settings after that omission. Upstream runtime commits remain unspecified where the source retained only an integration label.

| Configuration | Recorded artifact / source | Configured card counts | Context tokens | GPU pool tokens | Slots | Draft mode / tokens |
| --- | --- | --- | --- | --- | --- | --- |
| cfg-5e87a220e25c2d27302d | [turboderp/Qwen3.8-Flash-Next-exl3@d2e238feca](https://huggingface.co/turboderp/Qwen3.8-Flash-Next-exl3/tree/d2e238feca4c1c4d966943117356d8a42c2f4dcb) | 3 | 262,144 | 4,194,304 | 16 | disabled / 1 |
| cfg-97301bfcadb83cb0b580 | [turboderp/Qwen3.8-Flash-Next-exl3@d2e238feca](https://huggingface.co/turboderp/Qwen3.8-Flash-Next-exl3/tree/d2e238feca4c1c4d966943117356d8a42c2f4dcb) | 3 | 262,144 | 4,194,304 | 16 | disabled / 1 |

Card counts are saved configuration choices, not a claim that every allowed placement was measured. A derived view can differ from its pinned download source.

<details>
<summary>cfg-5e87a220e25c2d27302d</summary>

```json
{
  "kind": "tabby",
  "gpu_counts": [
    3
  ],
  "context": 262144,
  "cache_tokens": 4194304,
  "cache_mode": "Q8",
  "draft_cache_mode": "Q8",
  "draft_mode": "disabled",
  "draft_tokens": 1,
  "max_sessions": 16,
  "chunk_size": 512,
  "reserve_mib": 4096,
  "ram_kv_mib": 8192,
  "ram_recurrent_mib": 16384,
  "ngram_ram": true,
  "dynamic_draft": false,
  "power_watts": 200,
  "host_memory_gib": 80,
  "host_swap_gib": 0,
  "min_vram_mib_per_gpu": 65530,
  "min_effective_vram_mib": 196000,
  "model_repository": "turboderp/Qwen3.8-Flash-Next-exl3",
  "model_revision": "d2e238feca4c1c4d966943117356d8a42c2f4dcb",
  "draft_repository": null,
  "draft_revision": null,
  "recorded_runtime_label": null,
  "served_model_label": "qwen3.8-flash-next",
  "main_reserve_mib_values_unordered": [
    6144
  ]
}
```

Pinned model revision recorded: yes. Source receipt labels, hashes and object locators are retained in [configurations.json](../configurations.json).

</details>

<details>
<summary>cfg-97301bfcadb83cb0b580</summary>

```json
{
  "kind": "tabby",
  "gpu_counts": [
    3
  ],
  "context": 262144,
  "cache_tokens": 4194304,
  "cache_mode": "Q8",
  "draft_cache_mode": "Q8",
  "draft_mode": "disabled",
  "draft_tokens": 1,
  "max_sessions": 16,
  "chunk_size": 512,
  "reserve_mib": 4096,
  "ram_kv_mib": 8192,
  "ram_recurrent_mib": 16384,
  "ngram_ram": true,
  "dynamic_draft": false,
  "power_watts": 200,
  "host_memory_gib": 80,
  "host_swap_gib": 0,
  "min_vram_mib_per_gpu": 65530,
  "min_effective_vram_mib": 196000,
  "model_repository": "turboderp/Qwen3.8-Flash-Next-exl3",
  "model_revision": "d2e238feca4c1c4d966943117356d8a42c2f4dcb",
  "draft_repository": null,
  "draft_revision": null,
  "recorded_runtime_label": null,
  "served_model_label": "qwen3.8-flash-next",
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
| [result-2d88511c42f88c2d134a](../observations.json)<br>source-90ba7057ee2f419a7c91fcc1.json<br>`/original_job/tabby` | [qwen-flash-next-ordinary-native-context](qwen-flash-next-ordinary-native-context.md) | test outcome | Outcome unspecified | cache_tokens=4,194,304 tokens | Recorded configuration/job |

These are saved result records, including failures and bounded checks. Copies, individual requests, report summaries and regrading can overlap; their counts are not independent test repetitions. Open each result for exact values, units, configuration binding and source receipts.

There are 1 retained lifecycle records. Their states, exit codes and configuration IDs remain in [catalog.json](../catalog.json); they do not supply missing benchmark results.

[Full archive](../../README.md) | [All retained waves](../RESULTS.md) | [Data definitions](../DATA.md) | [Recommended recipes](../../../README.md)
