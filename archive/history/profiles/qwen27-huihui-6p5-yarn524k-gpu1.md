# qwen27-huihui-6p5-yarn524k-gpu1

**Historical record. Definition; no matched test receipt.**

Model family: Huihui Qwen 3.8 27B abliterated.

Recorded archive reason: Extended-context definition without a matched context receipt; Orca results do not qualify this checkpoint.

Historical configurations are provided for comparison. The [recommended recipes](../../../README.md) include supported launch scripts.

## Saved Configuration Versions

Each configuration ID identifies a distinct original settings record. Deployment fields are omitted; versions can have identical published settings after that omission. Upstream runtime commits remain unspecified where the source retained only an integration label.

| Configuration | Recorded artifact / source | Configured card counts | Context tokens | GPU pool tokens | Slots | Draft mode / tokens |
| --- | --- | --- | --- | --- | --- | --- |
| cfg-599c0b6b2e35e6a0b923 | [sakamakismile/Huihui-Qwen3.8-27B-abliterated-EXL3-6.5bpw@b4398c7154](https://huggingface.co/sakamakismile/Huihui-Qwen3.8-27B-abliterated-EXL3-6.5bpw/tree/b4398c715475e05798ca507f1651887159cccd39) (derived view) | 1 | 524,288 | 524,288 | 1 | mtp / 3 |

Card counts are saved configuration choices, not a claim that every allowed placement was measured. A derived view can differ from its pinned download source.

<details>
<summary>cfg-599c0b6b2e35e6a0b923</summary>

```json
{
  "kind": "tabby",
  "gpu_counts": [
    1
  ],
  "context": 524288,
  "cache_tokens": 524288,
  "cache_mode": "Q8",
  "draft_cache_mode": "Q8",
  "draft_mode": "mtp",
  "draft_tokens": 3,
  "max_sessions": 1,
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
  "served_model_label": "qwen27-huihui-exl3-6p5-yarn524k",
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

[Full archive](../../README.md) | [All retained waves](../RESULTS.md) | [Data definitions](../DATA.md) | [Recommended recipes](../../../README.md)
