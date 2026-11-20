# apex-flash-1-abliterated-validation-exl3-r1

**Historical record. Definition; no matched test receipt.**

Model family: Apex Flash 1 (GLM 5.3 Flash post-train).

Recorded archive reason: Conversion or extraction experiment with incomplete checkpoint qualification; tested Apex variants have separate records.

Historical configurations are provided for comparison. The [recommended recipes](../../../README.md) include supported launch scripts.

## Saved Configuration Versions

Each configuration ID identifies a distinct original settings record. Deployment fields are omitted; versions can have identical published settings after that omission. Upstream runtime commits remain unspecified where the source retained only an integration label.

| Configuration | Recorded artifact / source | Configured card counts | Context tokens | GPU pool tokens | Slots | Draft mode / tokens |
| --- | --- | --- | --- | --- | --- | --- |
| cfg-e74fd3692895573887e2 | [cantina-security/apex-flash-1-abliterated@cecb5eeb9c](https://huggingface.co/cantina-security/apex-flash-1-abliterated/tree/cecb5eeb9c6b32404a0dd930df81de2c239bdd84) | 3 | 32,768 | 131,072 | 4 | mtp / 1 |

Card counts are saved configuration choices, not a claim that every allowed placement was measured. A derived view can differ from its pinned download source.

<details>
<summary>cfg-e74fd3692895573887e2</summary>

```json
{
  "kind": "tabby",
  "gpu_counts": [
    3
  ],
  "context": 32768,
  "cache_tokens": 131072,
  "cache_mode": "Q8",
  "draft_cache_mode": "Q8",
  "draft_mode": "mtp",
  "draft_tokens": 1,
  "max_sessions": 4,
  "chunk_size": 256,
  "reserve_mib": 4096,
  "ram_kv_mib": 8192,
  "ram_recurrent_mib": 4096,
  "dynamic_draft": false,
  "power_watts": 200,
  "host_memory_gib": 80,
  "host_swap_gib": 0,
  "min_vram_mib_per_gpu": 65530,
  "min_effective_vram_mib": 196000,
  "model_repository": "cantina-security/apex-flash-1-abliterated",
  "model_revision": "cecb5eeb9c6b32404a0dd930df81de2c239bdd84",
  "draft_repository": null,
  "draft_revision": null,
  "recorded_runtime_label": null,
  "served_model_label": "apex-flash-1-abliterated-exl3-4.0hq-r1",
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

[Full archive](../../README.md) | [All retained waves](../RESULTS.md) | [Data definitions](../DATA.md) | [Recommended recipes](../../../README.md)
