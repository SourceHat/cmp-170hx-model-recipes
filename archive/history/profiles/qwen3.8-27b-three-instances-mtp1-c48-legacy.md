# qwen3.8-27b-three-instances-mtp1-c48-legacy

**Historical record. Legacy / incomplete measurements.**

Model family: Qwen 3.8 27B.

Historical configurations are provided for comparison. The [recommended recipes](../../../README.md) include supported launch scripts.

## Saved Configuration Versions

Each configuration ID identifies a distinct original settings record. Deployment fields are omitted; versions can have identical published settings after that omission. Upstream runtime commits remain unspecified where the source retained only an integration label.

| Configuration | Recorded artifact / source | Configured card counts | Context tokens | GPU pool tokens | Slots | Draft mode / tokens |
| --- | --- | --- | --- | --- | --- | --- |
| cfg-20fa4ad1dbac96e7ddae | [turboderp/Qwen3.8-27B-exl3@9e4c23cfb2](https://huggingface.co/turboderp/Qwen3.8-27B-exl3/tree/9e4c23cfb23697165b8e2f6da2a1df995f66353c) | 1 | 262,144 | 917,504 | 16 | mtp / 1 |
| cfg-749153d62f172d15d851 | [turboderp/Qwen3.8-27B-exl3@9e4c23cfb2](https://huggingface.co/turboderp/Qwen3.8-27B-exl3/tree/9e4c23cfb23697165b8e2f6da2a1df995f66353c) | 1 | 262,144 | 917,504 | 16 | mtp / 1 |
| cfg-e7f101d736c27e6b9933 | [turboderp/Qwen3.8-27B-exl3@9e4c23cfb2](https://huggingface.co/turboderp/Qwen3.8-27B-exl3/tree/9e4c23cfb23697165b8e2f6da2a1df995f66353c) | 1 | 262,144 | 917,504 | 16 | mtp / 1 |

Card counts are saved configuration choices, not a claim that every allowed placement was measured. A derived view can differ from its pinned download source.

<details>
<summary>cfg-20fa4ad1dbac96e7ddae</summary>

```json
{
  "kind": "tabby",
  "gpu_counts": [
    1
  ],
  "context": 262144,
  "cache_tokens": 917504,
  "cache_mode": "Q8",
  "draft_cache_mode": "Q8",
  "draft_mode": "mtp",
  "draft_tokens": 1,
  "max_sessions": 16,
  "chunk_size": 2048,
  "reserve_mib": 4096,
  "ram_kv_mib": 10240,
  "ram_recurrent_mib": 7168,
  "dynamic_draft": false,
  "power_watts": 200,
  "host_memory_gib": 25,
  "host_swap_gib": 0,
  "min_vram_mib_per_gpu": 60000,
  "min_effective_vram_mib": 60000,
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

<details>
<summary>cfg-749153d62f172d15d851</summary>

```json
{
  "kind": "tabby",
  "gpu_counts": [
    1
  ],
  "context": 262144,
  "cache_tokens": 917504,
  "cache_mode": "Q8",
  "draft_cache_mode": "Q8",
  "draft_mode": "mtp",
  "draft_tokens": 1,
  "max_sessions": 16,
  "chunk_size": 2048,
  "reserve_mib": 4096,
  "ram_kv_mib": 10240,
  "ram_recurrent_mib": 7168,
  "dynamic_draft": false,
  "power_watts": 200,
  "host_memory_gib": 25,
  "host_swap_gib": 0,
  "min_vram_mib_per_gpu": 60000,
  "min_effective_vram_mib": 60000,
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

<details>
<summary>cfg-e7f101d736c27e6b9933</summary>

```json
{
  "kind": "tabby",
  "gpu_counts": [
    1
  ],
  "context": 262144,
  "cache_tokens": 917504,
  "cache_mode": "Q8",
  "draft_cache_mode": "Q8",
  "draft_mode": "mtp",
  "draft_tokens": 1,
  "max_sessions": 16,
  "chunk_size": 2048,
  "reserve_mib": 4096,
  "ram_kv_mib": 10240,
  "ram_recurrent_mib": 7168,
  "dynamic_draft": false,
  "power_watts": 200,
  "host_memory_gib": 25,
  "host_swap_gib": 0,
  "min_vram_mib_per_gpu": 60000,
  "min_effective_vram_mib": 60000,
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

| Profile / Wave | Layout; Draft / Tokens | Requests | Input tokens/request | Accepted output tokens/request | Cache / Reused input tokens | Context / GPU pool tokens | Shared decode tok/s total | Client after-first-token estimate tok/s | Whole-wave output tok/s | Median TTFT, s | Source report |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [qwen3.8-27b-three-instances-mtp1-c48-legacy](qwen3.8-27b-three-instances-mtp1-c48-legacy.md)<br>wave-1ede364a8ece4c250621 | layout unspecified; mtp / 1 | 48 (3 instances; 16 each) | 2,064 to 8,201 | 256 | cold; reused 0 | 262,144 / 917,504 | Not recorded | 448.85 | 270.89 | 26.44 | Pass |
| [qwen3.8-27b-three-instances-mtp1-c48-legacy](qwen3.8-27b-three-instances-mtp1-c48-legacy.md)<br>wave-80b46bec8045a45c3e27 | layout unspecified; mtp / 1 | 48 (3 instances; 16 each) | 2,340 to 8,482 | 256 | cached_prefix; reused 2,048 to 8,192 | 262,144 / 917,504 | Not recorded | 683.65 | 461.54 | 10.07 | Pass |

Rates are whole-wave totals over the stated request count. A wave may span multiple independent model instances; [measurements.json](../measurements.json) retains their contributions and the exact configuration IDs. Do not interpret a multi-instance total as one card's rate.

A dash in shared decode means no qualified synchronized interval is available. Whole-wave throughput includes prefill and queueing. A valid decode interval can survive inside an overall failed or partial check; the source-report outcome is preserved. No rows are averaged.

[Full archive](../../README.md) | [All retained waves](../RESULTS.md) | [Data definitions](../DATA.md) | [Recommended recipes](../../../README.md)
