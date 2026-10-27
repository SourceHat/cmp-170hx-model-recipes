# qwen-q8

**Historical record. Job history; no matched benchmark.**

Model family: Qwen 3.8 27B.

Recorded archive reason: Incomplete model or configuration identity; retain only the bounded evidence recorded with this entry.

Historical configurations are provided for comparison. The [recommended recipes](../../../README.md) include supported launch scripts.

## Saved Configuration Versions

Each configuration ID identifies a distinct original settings record. Deployment fields are omitted; versions can have identical published settings after that omission. Upstream runtime commits remain unspecified where the source retained only an integration label.

| Configuration | Recorded artifact / source | Configured card counts | Context tokens | GPU pool tokens | Slots | Draft mode / tokens |
| --- | --- | --- | --- | --- | --- | --- |
| cfg-af5ea8ca384969cb99b4 | [unsloth/Qwen3.8-27B-GGUF@4ca720788d](https://huggingface.co/unsloth/Qwen3.8-27B-GGUF/tree/4ca720788d1e01f1bff70c033e0d0028fd02e502) | 1<br>2<br>3<br>4 | 262,144 | Not recorded | 3 | unspecified / - |

Card counts are saved configuration choices, not a claim that every allowed placement was measured. A derived view can differ from its pinned download source.

<details>
<summary>cfg-af5ea8ca384969cb99b4</summary>

```json
{
  "kind": "llama",
  "gpu_counts": [
    1,
    2,
    3,
    4
  ],
  "context": 262144,
  "max_sessions": 3,
  "power_watts": 200,
  "host_memory_gib": 16,
  "min_vram_mib_per_gpu": 36000,
  "min_vram_mib_single_gpu": 60000,
  "min_effective_vram_mib": 60000,
  "model_repository": "unsloth/Qwen3.8-27B-GGUF",
  "model_revision": "4ca720788d1e01f1bff70c033e0d0028fd02e502",
  "draft_repository": null,
  "draft_revision": null,
  "recorded_runtime_label": null,
  "served_model_label": "qwen3.8-27b",
  "model_file_template": "@MODEL_ROOT@/Qwen3.8-27B-Q8_0.gguf"
}
```

Pinned model revision recorded: yes. Source receipt labels, hashes and object locators are retained in [configurations.json](../configurations.json).

</details>

## Retained Measurements

No detailed benchmark receipt is matched to this record. A saved definition or a successful job exit alone is not a performance measurement.

A dash in shared decode means no qualified synchronized interval is available. Whole-wave throughput includes prefill and queueing. A valid decode interval can survive inside an overall failed or partial check; the source-report outcome is preserved. No rows are averaged.

There are 2 retained lifecycle records. Their states, exit codes and configuration IDs remain in [catalog.json](../catalog.json); they do not supply missing benchmark results.

[Full archive](../../README.md) | [All retained waves](../RESULTS.md) | [Data definitions](../DATA.md) | [Recommended recipes](../../../README.md)
