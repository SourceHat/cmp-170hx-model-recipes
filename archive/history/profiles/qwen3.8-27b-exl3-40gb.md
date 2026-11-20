# qwen3.8-27b-exl3-40gb

**Historical record. Definition; no matched test receipt.**

Model family: Qwen 3.8 27B.

Recorded archive reason: Incomplete model or configuration identity; retain only the bounded evidence recorded with this entry.

Historical configurations are provided for comparison. The [recommended recipes](../../../README.md) include supported launch scripts.

Current recipes using the same recorded checkpoint repository: [qwen3.8-27b-exl3](../../../recipes/qwen3.8-27b-exl3/README.md). Context, cache and runtime versions can differ.

## Saved Configuration Versions

Each configuration ID identifies a distinct original settings record. Deployment fields are omitted; versions can have identical published settings after that omission. Upstream runtime commits remain unspecified where the source retained only an integration label.

| Configuration | Recorded artifact / source | Configured card counts | Context tokens | GPU pool tokens | Slots | Draft mode / tokens |
| --- | --- | --- | --- | --- | --- | --- |
| cfg-efaad651090b17b4bfd9 | [turboderp/Qwen3.8-27B-exl3@9e4c23cfb2](https://huggingface.co/turboderp/Qwen3.8-27B-exl3/tree/9e4c23cfb23697165b8e2f6da2a1df995f66353c) | 1 | 262,144 | 262,144 | 8 | mtp / 3 |

Card counts are saved configuration choices, not a claim that every allowed placement was measured. A derived view can differ from its pinned download source.

<details>
<summary>cfg-efaad651090b17b4bfd9</summary>

```json
{
  "kind": "tabby",
  "gpu_counts": [
    1
  ],
  "context": 262144,
  "cache_tokens": 262144,
  "cache_mode": "Q8",
  "draft_cache_mode": "Q8",
  "draft_mode": "mtp",
  "draft_tokens": 3,
  "max_sessions": 8,
  "chunk_size": 2048,
  "reserve_mib": 4096,
  "ram_kv_mib": 5120,
  "ram_recurrent_mib": 7168,
  "dynamic_draft": false,
  "power_watts": 200,
  "host_memory_gib": 20,
  "host_swap_gib": 0,
  "min_vram_mib_per_gpu": 40000,
  "min_effective_vram_mib": 40000,
  "model_repository": "turboderp/Qwen3.8-27B-exl3",
  "model_revision": "9e4c23cfb23697165b8e2f6da2a1df995f66353c",
  "draft_repository": null,
  "draft_revision": null,
  "recorded_runtime_label": null,
  "served_model_label": "qwen3.8-27b"
}
```

Pinned model revision recorded: yes. Source receipt labels, hashes and object locators are retained in [configurations.json](../configurations.json).

</details>

## Retained Measurements

No detailed benchmark receipt is matched to this record. A saved definition or a successful job exit alone is not a performance measurement.

A dash in shared decode means no qualified synchronized interval is available. Whole-wave throughput includes prefill and queueing. A valid decode interval can survive inside an overall failed or partial check; the source-report outcome is preserved. No rows are averaged.

[Full archive](../../README.md) | [All retained waves](../RESULTS.md) | [Data definitions](../DATA.md) | [Recommended recipes](../../../README.md)
