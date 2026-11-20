# qwen27-huihui-6p5-native-gpu1

**Historical record. Additional test results; no matched decode wave.**

Model family: Huihui Qwen 3.8 27B abliterated.

Recorded archive reason: Historical preparation; later native and extended-context results are recorded separately.

Historical configurations are provided for comparison. The [recommended recipes](../../../README.md) include supported launch scripts.

## Saved Configuration Versions

Each configuration ID identifies a distinct original settings record. Deployment fields are omitted; versions can have identical published settings after that omission. Upstream runtime commits remain unspecified where the source retained only an integration label.

| Configuration | Recorded artifact / source | Configured card counts | Context tokens | GPU pool tokens | Slots | Draft mode / tokens |
| --- | --- | --- | --- | --- | --- | --- |
| cfg-617f2c05ce0d5d786e19 | [sakamakismile/Huihui-Qwen3.8-27B-abliterated-EXL3-6.5bpw@b4398c7154](https://huggingface.co/sakamakismile/Huihui-Qwen3.8-27B-abliterated-EXL3-6.5bpw/tree/b4398c715475e05798ca507f1651887159cccd39) (derived view) | 1 | 262,144 | 524,288 | 2 | mtp / 3 |
| cfg-7a3e137396d85c4fbf2f | [sakamakismile/Huihui-Qwen3.8-27B-abliterated-EXL3-6.5bpw@b4398c7154](https://huggingface.co/sakamakismile/Huihui-Qwen3.8-27B-abliterated-EXL3-6.5bpw/tree/b4398c715475e05798ca507f1651887159cccd39) (derived view) | 1 | 262,144 | 524,288 | 2 | mtp / 3 |

Card counts are saved configuration choices, not a claim that every allowed placement was measured. A derived view can differ from its pinned download source.

<details>
<summary>cfg-617f2c05ce0d5d786e19</summary>

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
  "max_sessions": 2,
  "chunk_size": 2048,
  "reserve_mib": 4096,
  "ram_kv_mib": 4096,
  "ram_recurrent_mib": 4096,
  "dynamic_draft": false,
  "power_watts": 200,
  "host_memory_gib": 32,
  "host_swap_gib": 0,
  "min_vram_mib_per_gpu": 60000,
  "min_effective_vram_mib": 60000,
  "model_repository": "sakamakismile/Huihui-Qwen3.8-27B-abliterated-EXL3-6.5bpw",
  "model_revision": "b4398c715475e05798ca507f1651887159cccd39",
  "draft_repository": null,
  "draft_revision": null,
  "recorded_runtime_label": null,
  "served_model_label": "qwen27-huihui-exl3-6p5",
  "derived_model_view_used": true,
  "model_view_metadata_included": false
}
```

Pinned model revision recorded: yes. Source receipt labels, hashes and object locators are retained in [configurations.json](../configurations.json).

</details>

<details>
<summary>cfg-7a3e137396d85c4fbf2f</summary>

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
  "max_sessions": 2,
  "chunk_size": 2048,
  "reserve_mib": 4096,
  "ram_kv_mib": 4096,
  "ram_recurrent_mib": 4096,
  "dynamic_draft": false,
  "power_watts": 200,
  "host_memory_gib": 32,
  "host_swap_gib": 0,
  "min_vram_mib_per_gpu": 60000,
  "min_effective_vram_mib": 60000,
  "model_repository": "sakamakismile/Huihui-Qwen3.8-27B-abliterated-EXL3-6.5bpw",
  "model_revision": "b4398c715475e05798ca507f1651887159cccd39",
  "draft_repository": null,
  "draft_revision": null,
  "recorded_runtime_label": null,
  "served_model_label": "qwen27-huihui-exl3-6p5",
  "derived_model_view_used": true,
  "model_view_metadata_included": false,
  "power_watts_values_unordered": []
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
| [result-8669865dbf3109e548e1](../observations.json)<br>source-6bfc3b4084d518d965011677.json<br>`/rows/1/traces/0` | [qwen27-huihui-6p5-native-gpu1](qwen27-huihui-6p5-native-gpu1.md) | test outcome | complete | generated_tokens=3 accepted tokens | Recorded configuration/job |

These are saved result records, including failures and bounded checks. Copies, individual requests, report summaries and regrading can overlap; their counts are not independent test repetitions. Open each result for exact values, units, configuration binding and source receipts.

There are 4 retained lifecycle records. Their states, exit codes and configuration IDs remain in [catalog.json](../catalog.json); they do not supply missing benchmark results.

[Full archive](../../README.md) | [All retained waves](../RESULTS.md) | [Data definitions](../DATA.md) | [Recommended recipes](../../../README.md)
