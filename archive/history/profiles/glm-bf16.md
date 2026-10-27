# glm-bf16

**Historical record. Definition; no matched test receipt.**

Model family: GLM 4.7 Flash.

Recorded archive reason: Incomplete model or configuration identity; retain only the bounded evidence recorded with this entry.

Historical configurations are provided for comparison. The [recommended recipes](../../../README.md) include supported launch scripts.

## Saved Configuration Versions

Each configuration ID identifies a distinct original settings record. Deployment fields are omitted; versions can have identical published settings after that omission. Upstream runtime commits remain unspecified where the source retained only an integration label.

| Configuration | Recorded artifact / source | Configured card counts | Context tokens | GPU pool tokens | Slots | Draft mode / tokens |
| --- | --- | --- | --- | --- | --- | --- |
| cfg-285a5f90469cb6bb5860 | [zai-org/GLM-4.7-Flash@7dd20894a6](https://huggingface.co/zai-org/GLM-4.7-Flash/tree/7dd20894a642a0aa287e9827cb1a1f7f91386b67) | 2<br>4 | 202,752 | Not recorded | 3 | unspecified / - |

Card counts are saved configuration choices, not a claim that every allowed placement was measured. A derived view can differ from its pinned download source.

<details>
<summary>cfg-285a5f90469cb6bb5860</summary>

```json
{
  "kind": "vllm",
  "gpu_counts": [
    2,
    4
  ],
  "context": 202752,
  "kv_dtype": "auto",
  "max_sessions": 3,
  "power_watts": 200,
  "host_memory_gib": 20,
  "min_vram_mib_per_gpu": 36000,
  "min_effective_vram_mib": 105000,
  "gpu_memory_utilization": 0.9,
  "model_repository": "zai-org/GLM-4.7-Flash",
  "model_revision": "7dd20894a642a0aa287e9827cb1a1f7f91386b67",
  "draft_repository": null,
  "draft_revision": null,
  "recorded_runtime_label": null,
  "served_model_label": "glm-4.7-flash"
}
```

Pinned model revision recorded: yes. Source receipt labels, hashes and object locators are retained in [configurations.json](../configurations.json).

</details>

## Retained Measurements

No detailed benchmark receipt is matched to this record. A saved definition or a successful job exit alone is not a performance measurement.

A dash in shared decode means no qualified synchronized interval is available. Whole-wave throughput includes prefill and queueing. A valid decode interval can survive inside an overall failed or partial check; the source-report outcome is preserved. No rows are averaged.

[Full archive](../../README.md) | [All retained waves](../RESULTS.md) | [Data definitions](../DATA.md) | [Recommended recipes](../../../README.md)
