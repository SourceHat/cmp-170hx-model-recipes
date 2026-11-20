# qwen-q8-40gb

**Historical record. Definition; no matched test receipt.**

Model family: Qwen.

Recorded archive reason: Incomplete model or configuration identity; retain only the bounded evidence recorded with this entry.

Historical configurations are provided for comparison. The [recommended recipes](../../../README.md) include supported launch scripts.

## Saved Configuration Versions

Each configuration ID identifies a distinct original settings record. Deployment fields are omitted; versions can have identical published settings after that omission. Upstream runtime commits remain unspecified where the source retained only an integration label.

| Configuration | Recorded artifact / source | Configured card counts | Context tokens | GPU pool tokens | Slots | Draft mode / tokens |
| --- | --- | --- | --- | --- | --- | --- |
| cfg-1b132d2931bfe6aa2175 | qwen3.8-27b | 1 | 262,144 | Not recorded | 1 | unspecified / - |

Card counts are saved configuration choices, not a claim that every allowed placement was measured. A derived view can differ from its pinned download source.

<details>
<summary>cfg-1b132d2931bfe6aa2175</summary>

```json
{
  "kind": "llama",
  "gpu_counts": [
    1
  ],
  "context": 262144,
  "max_sessions": 1,
  "power_watts": 200,
  "host_memory_gib": 16,
  "min_vram_mib_per_gpu": 38000,
  "model_repository": null,
  "model_revision": null,
  "draft_repository": null,
  "draft_revision": null,
  "recorded_runtime_label": null,
  "served_model_label": "qwen3.8-27b",
  "model_file_template": "@MODEL_ROOT@/Qwen3.8-27B-Q8_0.gguf"
}
```

Pinned model revision recorded: no. Source receipt labels, hashes and object locators are retained in [configurations.json](../configurations.json).

</details>

## Retained Measurements

No detailed benchmark receipt is matched to this record. A saved definition or a successful job exit alone is not a performance measurement.

A dash in shared decode means no qualified synchronized interval is available. Whole-wave throughput includes prefill and queueing. A valid decode interval can survive inside an overall failed or partial check; the source-report outcome is preserved. No rows are averaged.

[Full archive](../../README.md) | [All retained waves](../RESULTS.md) | [Data definitions](../DATA.md) | [Recommended recipes](../../../README.md)
