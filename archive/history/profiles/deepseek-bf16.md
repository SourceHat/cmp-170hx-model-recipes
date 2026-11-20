# deepseek-bf16

**Historical record. Job history; no matched benchmark.**

Model family: DeepSeek.

Recorded archive reason: Incomplete model or configuration identity; retain only the bounded evidence recorded with this entry.

Historical configurations are provided for comparison. The [recommended recipes](../../../README.md) include supported launch scripts.

## Saved Configuration Versions

Each configuration ID identifies a distinct original settings record. Deployment fields are omitted; versions can have identical published settings after that omission. Upstream runtime commits remain unspecified where the source retained only an integration label.

| Configuration | Recorded artifact / source | Configured card counts | Context tokens | GPU pool tokens | Slots | Draft mode / tokens |
| --- | --- | --- | --- | --- | --- | --- |
| cfg-3e845a0bbdc2e2cedcf0 | [deepseek-ai/DeepSeek-V2-Lite-Chat@85864749cd](https://huggingface.co/deepseek-ai/DeepSeek-V2-Lite-Chat/tree/85864749cd611b4353ce1decdb286193298f64c7) | 1<br>2<br>4 | 32,768 | Not recorded | 3 | unspecified / - |

Card counts are saved configuration choices, not a claim that every allowed placement was measured. A derived view can differ from its pinned download source.

<details>
<summary>cfg-3e845a0bbdc2e2cedcf0</summary>

```json
{
  "kind": "vllm",
  "gpu_counts": [
    1,
    2,
    4
  ],
  "context": 32768,
  "kv_dtype": "auto",
  "max_sessions": 3,
  "power_watts": 200,
  "host_memory_gib": 20,
  "min_vram_mib_per_gpu": 60000,
  "gpu_memory_utilization": 0.9,
  "model_repository": "deepseek-ai/DeepSeek-V2-Lite-Chat",
  "model_revision": "85864749cd611b4353ce1decdb286193298f64c7",
  "draft_repository": null,
  "draft_revision": null,
  "recorded_runtime_label": null,
  "served_model_label": "deepseek-v2-lite"
}
```

Pinned model revision recorded: yes. Source receipt labels, hashes and object locators are retained in [configurations.json](../configurations.json).

</details>

## Retained Measurements

No detailed benchmark receipt is matched to this record. A saved definition or a successful job exit alone is not a performance measurement.

A dash in shared decode means no qualified synchronized interval is available. Whole-wave throughput includes prefill and queueing. A valid decode interval can survive inside an overall failed or partial check; the source-report outcome is preserved. No rows are averaged.

There are 1 retained lifecycle records. Their states, exit codes and configuration IDs remain in [catalog.json](../catalog.json); they do not supply missing benchmark results.

[Full archive](../../README.md) | [All retained waves](../RESULTS.md) | [Data definitions](../DATA.md) | [Recommended recipes](../../../README.md)
