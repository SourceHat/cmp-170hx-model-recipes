# glm-air-q8

**Historical record. Definition; no matched test receipt.**

Model family: GLM 4.5 Air.

Recorded archive reason: Incomplete model or configuration identity; retain only the bounded evidence recorded with this entry.

Historical configurations are provided for comparison. The [recommended recipes](../../../README.md) include supported launch scripts.

## Saved Configuration Versions

Each configuration ID identifies a distinct original settings record. Deployment fields are omitted; versions can have identical published settings after that omission. Upstream runtime commits remain unspecified where the source retained only an integration label.

| Configuration | Recorded artifact / source | Configured card counts | Context tokens | GPU pool tokens | Slots | Draft mode / tokens |
| --- | --- | --- | --- | --- | --- | --- |
| cfg-868fd167173427754aea | [unsloth/GLM-4.5-Air-GGUF@506d64aa8c](https://huggingface.co/unsloth/GLM-4.5-Air-GGUF/tree/506d64aa8c5cfe9dbbf00bc7a15739438f83204d) | 3<br>4 | 131,072 | Not recorded | 3 | unspecified / - |

Card counts are saved configuration choices, not a claim that every allowed placement was measured. A derived view can differ from its pinned download source.

<details>
<summary>cfg-868fd167173427754aea</summary>

```json
{
  "kind": "llama",
  "gpu_counts": [
    3,
    4
  ],
  "context": 131072,
  "max_sessions": 3,
  "power_watts": 200,
  "host_memory_gib": 16,
  "min_vram_mib_per_gpu": 36000,
  "min_vram_mib_single_gpu": 60000,
  "min_effective_vram_mib": 175000,
  "model_repository": "unsloth/GLM-4.5-Air-GGUF",
  "model_revision": "506d64aa8c5cfe9dbbf00bc7a15739438f83204d",
  "draft_repository": null,
  "draft_revision": null,
  "recorded_runtime_label": null,
  "served_model_label": "glm-4.5-air",
  "model_file_template": "@MODEL_ROOT@/GLM-4.5-Air-Q8_0-00001-of-00003.gguf"
}
```

Pinned model revision recorded: yes. Source receipt labels, hashes and object locators are retained in [configurations.json](../configurations.json).

</details>

## Retained Measurements

No detailed benchmark receipt is matched to this record. A saved definition or a successful job exit alone is not a performance measurement.

A dash in shared decode means no qualified synchronized interval is available. Whole-wave throughput includes prefill and queueing. A valid decode interval can survive inside an overall failed or partial check; the source-report outcome is preserved. No rows are averaged.

[Full archive](../../README.md) | [All retained waves](../RESULTS.md) | [Data definitions](../DATA.md) | [Recommended recipes](../../../README.md)
