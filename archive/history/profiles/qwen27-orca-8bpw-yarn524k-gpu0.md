# qwen27-orca-8bpw-yarn524k-gpu0

**Historical record. Definition; no matched test receipt.**

Model family: Orca (Qwen 3.8 27B abliterated).

Recorded archive reason: Historical preparation; later native and extended-context results are recorded separately.

Historical configurations are provided for comparison. The [recommended recipes](../../../README.md) include supported launch scripts.

Current recipes using the same recorded checkpoint repository: [qwen27-orca-mtp3-native](../../../recipes/qwen27-orca-mtp3-native/README.md). Context, cache and runtime versions can differ.

## Saved Configuration Versions

Each configuration ID identifies a distinct original settings record. Deployment fields are omitted; versions can have identical published settings after that omission. Upstream runtime commits remain unspecified where the source retained only an integration label.

| Configuration | Recorded artifact / source | Configured card counts | Context tokens | GPU pool tokens | Slots | Draft mode / tokens |
| --- | --- | --- | --- | --- | --- | --- |
| cfg-4d925ef8277c4933653c | [Lygodactylus/Qwen3.8-27B-Uncensored-exl3-8bpw@3487b152b3](https://huggingface.co/Lygodactylus/Qwen3.8-27B-Uncensored-exl3-8bpw/tree/3487b152b302930e303dc4a2e99e7e976e3ad28f) (derived view) | 1 | 524,288 | 524,288 | 1 | mtp / 3 |

Card counts are saved configuration choices, not a claim that every allowed placement was measured. A derived view can differ from its pinned download source.

<details>
<summary>cfg-4d925ef8277c4933653c</summary>

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
  "host_memory_gib": 40,
  "host_swap_gib": 0,
  "min_vram_mib_per_gpu": 60000,
  "min_effective_vram_mib": 60000,
  "model_repository": "Lygodactylus/Qwen3.8-27B-Uncensored-exl3-8bpw",
  "model_revision": "3487b152b302930e303dc4a2e99e7e976e3ad28f",
  "draft_repository": null,
  "draft_revision": null,
  "recorded_runtime_label": null,
  "served_model_label": "qwen27-orca-exl3-8bpw-yarn524k",
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
