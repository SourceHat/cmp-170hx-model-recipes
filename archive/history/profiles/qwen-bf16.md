# qwen-bf16

**Historical record. Definition; no matched test receipt.**

Model family: Qwen 3.8 27B.

Recorded archive reason: Incomplete model or configuration identity; retain only the bounded evidence recorded with this entry.

Historical configurations are provided for comparison. The [recommended recipes](../../../README.md) include supported launch scripts.

## Saved Configuration Versions

Each configuration ID identifies a distinct original settings record. Deployment fields are omitted; versions can have identical published settings after that omission. Upstream runtime commits remain unspecified where the source retained only an integration label.

| Configuration | Recorded artifact / source | Configured card counts | Context tokens | GPU pool tokens | Slots | Draft mode / tokens |
| --- | --- | --- | --- | --- | --- | --- |
| cfg-706fa69388973423cd49 | [Qwen/Qwen3.8-27B@1d4bf0f2ff](https://huggingface.co/Qwen/Qwen3.8-27B/tree/1d4bf0f2ff6012fd82039f2fa52739d0dd7c60c0) | 2<br>4 | 262,144 | Not recorded | 3 | unspecified / - |

Card counts are saved configuration choices, not a claim that every allowed placement was measured. A derived view can differ from its pinned download source.

<details>
<summary>cfg-706fa69388973423cd49</summary>

```json
{
  "kind": "vllm",
  "gpu_counts": [
    2,
    4
  ],
  "context": 262144,
  "kv_dtype": "auto",
  "max_sessions": 3,
  "power_watts": 200,
  "host_memory_gib": 20,
  "min_vram_mib_per_gpu": 36000,
  "min_effective_vram_mib": 105000,
  "gpu_memory_utilization": 0.9,
  "model_repository": "Qwen/Qwen3.8-27B",
  "model_revision": "1d4bf0f2ff6012fd82039f2fa52739d0dd7c60c0",
  "draft_repository": null,
  "draft_revision": null,
  "recorded_runtime_label": null,
  "served_model_label": "qwen3.8-27b",
  "native_arguments_template": [
    "--language-model-only",
    "--enable-prefix-caching"
  ]
}
```

Pinned model revision recorded: yes. Source receipt labels, hashes and object locators are retained in [configurations.json](../configurations.json).

</details>

## Retained Measurements

No detailed benchmark receipt is matched to this record. A saved definition or a successful job exit alone is not a performance measurement.

A dash in shared decode means no qualified synchronized interval is available. Whole-wave throughput includes prefill and queueing. A valid decode interval can survive inside an overall failed or partial check; the source-report outcome is preserved. No rows are averaged.

[Full archive](../../README.md) | [All retained waves](../RESULTS.md) | [Data definitions](../DATA.md) | [Recommended recipes](../../../README.md)
