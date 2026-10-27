# apex-flash-1-gpu-delta-extract-r1

**Historical record. Job history; no matched benchmark.**

Model family: Apex Flash 1 (GLM 5.3 Flash post-train).

Recorded archive reason: Conversion or extraction experiment with incomplete checkpoint qualification; tested Apex variants have separate records.

Historical configurations are provided for comparison. The [recommended recipes](../../../README.md) include supported launch scripts.

## Saved Configuration Versions

Each configuration ID identifies a distinct original settings record. Deployment fields are omitted; versions can have identical published settings after that omission. Upstream runtime commits remain unspecified where the source retained only an integration label.

| Configuration | Recorded artifact / source | Configured card counts | Context tokens | GPU pool tokens | Slots | Draft mode / tokens |
| --- | --- | --- | --- | --- | --- | --- |
| cfg-4a1fbcd54b85f5f00939 | [cantina-security/apex-flash-1@28c647a6bd](https://huggingface.co/cantina-security/apex-flash-1/tree/28c647a6bd0444973a7ef3d940c24c67e64f52fe) | 1 | Not recorded | Not recorded | Not recorded | unspecified / - |
| cfg-89b59362f72582d326d2 | [cantina-security/apex-flash-1@28c647a6bd](https://huggingface.co/cantina-security/apex-flash-1/tree/28c647a6bd0444973a7ef3d940c24c67e64f52fe) | 1 | Not recorded | Not recorded | Not recorded | unspecified / - |

Card counts are saved configuration choices, not a claim that every allowed placement was measured. A derived view can differ from its pinned download source.

<details>
<summary>cfg-4a1fbcd54b85f5f00939</summary>

```json
{
  "kind": "command",
  "gpu_counts": [
    1
  ],
  "power_watts": 200,
  "host_memory_gib": 80,
  "host_swap_gib": 0,
  "min_vram_mib_single_gpu": 65530,
  "model_repository": "cantina-security/apex-flash-1",
  "model_revision": "28c647a6bd0444973a7ef3d940c24c67e64f52fe",
  "draft_repository": null,
  "draft_revision": null,
  "recorded_runtime_label": null,
  "served_model_label": null
}
```

Pinned model revision recorded: yes. Source receipt labels, hashes and object locators are retained in [configurations.json](../configurations.json).

</details>

<details>
<summary>cfg-89b59362f72582d326d2</summary>

```json
{
  "kind": "command",
  "gpu_counts": [
    1
  ],
  "power_watts": 200,
  "host_memory_gib": 80,
  "host_swap_gib": 0,
  "min_vram_mib_single_gpu": 65530,
  "model_repository": "cantina-security/apex-flash-1",
  "model_revision": "28c647a6bd0444973a7ef3d940c24c67e64f52fe",
  "draft_repository": null,
  "draft_revision": null,
  "recorded_runtime_label": null,
  "served_model_label": null
}
```

Pinned model revision recorded: yes. Source receipt labels, hashes and object locators are retained in [configurations.json](../configurations.json).

</details>

## Retained Measurements

No detailed benchmark receipt is matched to this record. A saved definition or a successful job exit alone is not a performance measurement.

A dash in shared decode means no qualified synchronized interval is available. Whole-wave throughput includes prefill and queueing. A valid decode interval can survive inside an overall failed or partial check; the source-report outcome is preserved. No rows are averaged.

There are 3 retained lifecycle records. Their states, exit codes and configuration IDs remain in [catalog.json](../catalog.json); they do not supply missing benchmark results.

[Full archive](../../README.md) | [All retained waves](../RESULTS.md) | [Data definitions](../DATA.md) | [Recommended recipes](../../../README.md)
