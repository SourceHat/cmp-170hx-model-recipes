# qwen38-capacity64

**Historical record. Legacy / incomplete measurements.**

Model family: Qwen 3.8 27B.

Recorded archive reason: Fit, pilot or control configuration; measured serving variants have separate records.

Historical configurations are provided for comparison. The [recommended recipes](../../../README.md) include supported launch scripts.

Current recipes using the same recorded checkpoint repository: [qwen3.8-27b-exl3](../../../recipes/qwen3.8-27b-exl3/README.md). Context, cache and runtime versions can differ.

## Saved Configuration Versions

Each configuration ID identifies a distinct original settings record. Deployment fields are omitted; versions can have identical published settings after that omission. Upstream runtime commits remain unspecified where the source retained only an integration label.

| Configuration | Recorded artifact / source | Configured card counts | Context tokens | GPU pool tokens | Slots | Draft mode / tokens |
| --- | --- | --- | --- | --- | --- | --- |
| cfg-17bebde642487911f529 | [turboderp/Qwen3.8-27B-exl3@9e4c23cfb2](https://huggingface.co/turboderp/Qwen3.8-27B-exl3/tree/9e4c23cfb23697165b8e2f6da2a1df995f66353c) | 1 | 262,144 | 786,432 | 16 | mtp / 3 |
| cfg-20f9409889744172e670 | [turboderp/Qwen3.8-27B-exl3@9e4c23cfb2](https://huggingface.co/turboderp/Qwen3.8-27B-exl3/tree/9e4c23cfb23697165b8e2f6da2a1df995f66353c) | 1 | 262,144 | 786,432 | 16 | mtp / 3 |
| cfg-2d243775e48d82649b6b | [turboderp/Qwen3.8-27B-exl3@9e4c23cfb2](https://huggingface.co/turboderp/Qwen3.8-27B-exl3/tree/9e4c23cfb23697165b8e2f6da2a1df995f66353c) | 1 | 262,144 | 786,432 | 16 | mtp / 3 |
| cfg-56a2c96abbdc4a5b93b0 | [turboderp/Qwen3.8-27B-exl3@9e4c23cfb2](https://huggingface.co/turboderp/Qwen3.8-27B-exl3/tree/9e4c23cfb23697165b8e2f6da2a1df995f66353c) | 1 | 262,144 | 786,432 | 16 | mtp / 3 |
| cfg-68006053ab2e00d732d6 | [turboderp/Qwen3.8-27B-exl3@9e4c23cfb2](https://huggingface.co/turboderp/Qwen3.8-27B-exl3/tree/9e4c23cfb23697165b8e2f6da2a1df995f66353c) | 1 | 262,144 | 786,432 | 16 | mtp / 3 |
| cfg-68f0367a42c250f34ded | [turboderp/Qwen3.8-27B-exl3@9e4c23cfb2](https://huggingface.co/turboderp/Qwen3.8-27B-exl3/tree/9e4c23cfb23697165b8e2f6da2a1df995f66353c) | 1 | 262,144 | 786,432 | 16 | mtp / 3 |
| cfg-6ab0ec7b7d53073ed187 | [turboderp/Qwen3.8-27B-exl3@9e4c23cfb2](https://huggingface.co/turboderp/Qwen3.8-27B-exl3/tree/9e4c23cfb23697165b8e2f6da2a1df995f66353c) | 1 | 262,144 | 786,432 | 16 | mtp / 3 |
| cfg-cce39833f3db2a7027db | [turboderp/Qwen3.8-27B-exl3@9e4c23cfb2](https://huggingface.co/turboderp/Qwen3.8-27B-exl3/tree/9e4c23cfb23697165b8e2f6da2a1df995f66353c) | 1 | 262,144 | 786,432 | 16 | mtp / 3 |
| cfg-d35efc52d2d00b98fcb7 | [turboderp/Qwen3.8-27B-exl3@9e4c23cfb2](https://huggingface.co/turboderp/Qwen3.8-27B-exl3/tree/9e4c23cfb23697165b8e2f6da2a1df995f66353c) | 1 | 262,144 | 786,432 | 16 | mtp / 3 |

Card counts are saved configuration choices, not a claim that every allowed placement was measured. A derived view can differ from its pinned download source.

<details>
<summary>cfg-17bebde642487911f529</summary>

```json
{
  "kind": "tabby",
  "gpu_counts": [
    1
  ],
  "context": 262144,
  "cache_tokens": 786432,
  "cache_mode": "Q8",
  "draft_cache_mode": "Q8",
  "draft_mode": "mtp",
  "draft_tokens": 3,
  "max_sessions": 16,
  "chunk_size": 2048,
  "reserve_mib": 4096,
  "ram_kv_mib": 5120,
  "ram_recurrent_mib": 7168,
  "dynamic_draft": false,
  "power_watts": 200,
  "host_memory_gib": 20,
  "host_swap_gib": 0,
  "min_vram_mib_per_gpu": 60000,
  "min_effective_vram_mib": 60000,
  "model_repository": "turboderp/Qwen3.8-27B-exl3",
  "model_revision": "9e4c23cfb23697165b8e2f6da2a1df995f66353c",
  "draft_repository": null,
  "draft_revision": null,
  "recorded_runtime_label": null,
  "served_model_label": "qwen3.8-27b",
  "power_watts_values_unordered": []
}
```

Pinned model revision recorded: yes. Source receipt labels, hashes and object locators are retained in [configurations.json](../configurations.json).

</details>

<details>
<summary>cfg-20f9409889744172e670</summary>

```json
{
  "kind": "tabby",
  "gpu_counts": [
    1
  ],
  "context": 262144,
  "cache_tokens": 786432,
  "cache_mode": "Q8",
  "draft_cache_mode": "Q8",
  "draft_mode": "mtp",
  "draft_tokens": 3,
  "max_sessions": 16,
  "chunk_size": 2048,
  "reserve_mib": 4096,
  "ram_kv_mib": 5120,
  "ram_recurrent_mib": 7168,
  "dynamic_draft": false,
  "power_watts": 200,
  "host_memory_gib": 20,
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
<summary>cfg-2d243775e48d82649b6b</summary>

```json
{
  "kind": "tabby",
  "gpu_counts": [
    1
  ],
  "context": 262144,
  "cache_tokens": 786432,
  "cache_mode": "Q8",
  "draft_cache_mode": "Q8",
  "draft_mode": "mtp",
  "draft_tokens": 3,
  "max_sessions": 16,
  "chunk_size": 2048,
  "reserve_mib": 4096,
  "ram_kv_mib": 8192,
  "ram_recurrent_mib": 4096,
  "dynamic_draft": false,
  "power_watts": 200,
  "host_memory_gib": 20,
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
<summary>cfg-56a2c96abbdc4a5b93b0</summary>

```json
{
  "kind": "tabby",
  "gpu_counts": [
    1
  ],
  "context": 262144,
  "cache_tokens": 786432,
  "cache_mode": "Q8",
  "draft_cache_mode": "Q8",
  "draft_mode": "mtp",
  "draft_tokens": 3,
  "max_sessions": 16,
  "chunk_size": 2048,
  "reserve_mib": 4096,
  "ram_kv_mib": 5120,
  "ram_recurrent_mib": 7168,
  "dynamic_draft": false,
  "power_watts": 200,
  "host_memory_gib": 20,
  "host_swap_gib": 0,
  "min_vram_mib_per_gpu": 60000,
  "min_effective_vram_mib": 60000,
  "model_repository": "turboderp/Qwen3.8-27B-exl3",
  "model_revision": "9e4c23cfb23697165b8e2f6da2a1df995f66353c",
  "draft_repository": null,
  "draft_revision": null,
  "recorded_runtime_label": null,
  "served_model_label": "qwen3.8-27b",
  "power_watts_values_unordered": [
    150
  ]
}
```

Pinned model revision recorded: yes. Source receipt labels, hashes and object locators are retained in [configurations.json](../configurations.json).

</details>

<details>
<summary>cfg-68006053ab2e00d732d6</summary>

```json
{
  "kind": "tabby",
  "gpu_counts": [
    1
  ],
  "context": 262144,
  "cache_tokens": 786432,
  "cache_mode": "Q8",
  "draft_cache_mode": "Q8",
  "draft_mode": "mtp",
  "draft_tokens": 3,
  "max_sessions": 16,
  "chunk_size": 2048,
  "reserve_mib": 4096,
  "ram_kv_mib": 5120,
  "ram_recurrent_mib": 7168,
  "dynamic_draft": false,
  "power_watts": 200,
  "host_memory_gib": 20,
  "host_swap_gib": 0,
  "min_vram_mib_per_gpu": 60000,
  "min_effective_vram_mib": 60000,
  "model_repository": "turboderp/Qwen3.8-27B-exl3",
  "model_revision": "9e4c23cfb23697165b8e2f6da2a1df995f66353c",
  "draft_repository": null,
  "draft_revision": null,
  "recorded_runtime_label": null,
  "served_model_label": "qwen3.8-27b",
  "power_watts_values_unordered": [
    150,
    175
  ]
}
```

Pinned model revision recorded: yes. Source receipt labels, hashes and object locators are retained in [configurations.json](../configurations.json).

</details>

<details>
<summary>cfg-68f0367a42c250f34ded</summary>

```json
{
  "kind": "tabby",
  "gpu_counts": [
    1
  ],
  "context": 262144,
  "cache_tokens": 786432,
  "cache_mode": "Q8",
  "draft_cache_mode": "Q8",
  "draft_mode": "mtp",
  "draft_tokens": 3,
  "max_sessions": 16,
  "chunk_size": 2048,
  "reserve_mib": 4096,
  "ram_kv_mib": 5120,
  "ram_recurrent_mib": 7168,
  "dynamic_draft": false,
  "power_watts": 200,
  "host_memory_gib": 20,
  "host_swap_gib": 0,
  "min_vram_mib_per_gpu": 60000,
  "min_effective_vram_mib": 60000,
  "model_repository": "turboderp/Qwen3.8-27B-exl3",
  "model_revision": "9e4c23cfb23697165b8e2f6da2a1df995f66353c",
  "draft_repository": null,
  "draft_revision": null,
  "recorded_runtime_label": null,
  "served_model_label": "qwen3.8-27b",
  "power_watts_values_unordered": [
    150
  ]
}
```

Pinned model revision recorded: yes. Source receipt labels, hashes and object locators are retained in [configurations.json](../configurations.json).

</details>

<details>
<summary>cfg-6ab0ec7b7d53073ed187</summary>

```json
{
  "kind": "tabby",
  "gpu_counts": [
    1
  ],
  "context": 262144,
  "cache_tokens": 786432,
  "cache_mode": "Q8",
  "draft_cache_mode": "Q8",
  "draft_mode": "mtp",
  "draft_tokens": 3,
  "max_sessions": 16,
  "chunk_size": 2048,
  "reserve_mib": 4096,
  "ram_kv_mib": 5120,
  "ram_recurrent_mib": 7168,
  "dynamic_draft": false,
  "power_watts": 200,
  "host_memory_gib": 20,
  "host_swap_gib": 0,
  "min_vram_mib_per_gpu": 60000,
  "min_effective_vram_mib": 60000,
  "model_repository": "turboderp/Qwen3.8-27B-exl3",
  "model_revision": "9e4c23cfb23697165b8e2f6da2a1df995f66353c",
  "draft_repository": null,
  "draft_revision": null,
  "recorded_runtime_label": null,
  "served_model_label": "qwen3.8-27b",
  "power_watts_values_unordered": [
    150
  ]
}
```

Pinned model revision recorded: yes. Source receipt labels, hashes and object locators are retained in [configurations.json](../configurations.json).

</details>

<details>
<summary>cfg-cce39833f3db2a7027db</summary>

```json
{
  "kind": "tabby",
  "gpu_counts": [
    1
  ],
  "context": 262144,
  "cache_tokens": 786432,
  "cache_mode": "Q8",
  "draft_cache_mode": "Q8",
  "draft_mode": "mtp",
  "draft_tokens": 3,
  "max_sessions": 16,
  "chunk_size": 2048,
  "reserve_mib": 4096,
  "ram_kv_mib": 8192,
  "ram_recurrent_mib": 4096,
  "dynamic_draft": false,
  "power_watts": 200,
  "host_memory_gib": 20,
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
<summary>cfg-d35efc52d2d00b98fcb7</summary>

```json
{
  "kind": "tabby",
  "gpu_counts": [
    1
  ],
  "context": 262144,
  "cache_tokens": 786432,
  "cache_mode": "Q8",
  "draft_cache_mode": "Q8",
  "draft_mode": "mtp",
  "draft_tokens": 3,
  "max_sessions": 16,
  "chunk_size": 2048,
  "reserve_mib": 4096,
  "ram_kv_mib": 5120,
  "ram_recurrent_mib": 7168,
  "dynamic_draft": false,
  "power_watts": 200,
  "host_memory_gib": 20,
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
| [qwen38-capacity64](qwen38-capacity64.md)<br>wave-0051c76127753a10d7ec | layout unspecified; mtp / 3 | 2 | 32,982 | 35 | cached_prefix; reused 32,768 | 262,144 / 786,432 | Not recorded | 117.07 | 36.89 | 1.34 | Pass |
| [qwen38-capacity64](qwen38-capacity64.md)<br>wave-05789817127f4fd54f1d | layout unspecified; mtp / 3 | 16 | 2,335 to 24,865 | 256 | cached_prefix; reused 2,048 to 24,576 | 262,144 / 786,432 | Not recorded | 131.37 | 121.74 | 9.96 | Pass |
| [qwen38-capacity64](qwen38-capacity64.md)<br>wave-1e3e54bf9eaa3b490c42 | layout unspecified; mtp / 3 | 2 | 131,290 | 35 | cached_prefix; reused 131,072 | 262,144 / 786,432 | Not recorded | 55.28 | 17.70 | 2.69 | Pass |
| [qwen38-capacity64](qwen38-capacity64.md)<br>wave-20447bbdda5b353c27d7 | layout unspecified; mtp / 3 | 1 | 261,187 | 136 | cold; reused 131,072 | 262,144 / 786,432 | Not recorded | 20.63 | 0.60 | 220.54 | Pass |
| [qwen38-capacity64](qwen38-capacity64.md)<br>wave-454ae4bcceab44853992 | layout unspecified; mtp / 3 | 2 | 131,278 to 131,295 | 35 | cached_prefix; reused 131,072 | 262,144 / 786,432 | Not recorded | 57.62 | 15.95 | 3.25 | Pass |
| [qwen38-capacity64](qwen38-capacity64.md)<br>wave-4bb0cd2a58e08dd00ff5 | layout unspecified; mtp / 3 | 1 | 32,826 | 138 | cold; reused 0 | 262,144 / 786,432 | Not recorded | 52.75 | 6.37 | 19.03 | Pass |
| [qwen38-capacity64](qwen38-capacity64.md)<br>wave-51df6e8e2c6faafba4ae | layout unspecified; mtp / 3 | 2 | 32,830 | 138 | cold; reused 0 | 262,144 / 786,432 | Not recorded | 64.87 | 5.39 | 47.18 | Pass |
| [qwen38-capacity64](qwen38-capacity64.md)<br>wave-599cd68d1a013a9244d4 | layout unspecified; mtp / 3 | 2 | 131,131 | 141 | cold; reused 32,768 | 262,144 / 786,432 | Not recorded | 28.93 | 1.42 | 190.87 | Pass |
| [qwen38-capacity64](qwen38-capacity64.md)<br>wave-610ae57d97c68fcc7e44 | layout unspecified; mtp / 3 | 2 | 32,826 | 138 | cold; reused 0 | 262,144 / 786,432 | Not recorded | 73.04 | 6.69 | 37.62 | Pass |
| [qwen38-capacity64](qwen38-capacity64.md)<br>wave-730300ab214f280ec25f | layout unspecified; mtp / 3 | 2 | 261,134 | 130 | cold; reused 131,072 | 262,144 / 786,432 | Not recorded | 22.00 | 0.49 | 513.99 | Failed / partial |
| [qwen38-capacity64](qwen38-capacity64.md)<br>wave-7b5e7fdb3b5ef24f1084 | layout unspecified; mtp / 3 | 16 | 2,335 to 24,865 | 256 | cached_prefix; reused 2,048 to 24,576 | 262,144 / 786,432 | Not recorded | 124.32 | 115.65 | 12.69 | Pass |
| [qwen38-capacity64](qwen38-capacity64.md)<br>wave-8577072e836e277bcc48 | layout unspecified; mtp / 3 | 1 | 131,132 | 141 | cold; reused 32,768 | 262,144 / 786,432 | Not recorded | 34.59 | 1.38 | 97.81 | Pass |
| [qwen38-capacity64](qwen38-capacity64.md)<br>wave-8cdecef22971c9bd1593 | layout unspecified; mtp / 3 | 16 | 2,052 to 24,585 | 256 | cold; reused 0 | 262,144 / 786,432 | Not recorded | 102.83 | 48.83 | 63.64 | Pass |
| [qwen38-capacity64](qwen38-capacity64.md)<br>wave-998cf6424b6f4f9ba778 | layout unspecified; mtp / 3 | 16 | 2,052 to 24,585 | 256 | cold; reused 0 | 262,144 / 786,432 | Not recorded | 75.96 | 47.56 | 62.08 | Pass |
| [qwen38-capacity64](qwen38-capacity64.md)<br>wave-a777bbc790128eb63fab | layout unspecified; mtp / 3 | 2 | 32,825 | 138 | cold; reused 0 | 262,144 / 786,432 | Not recorded | 73.57 | 6.80 | 37.07 | Pass |
| [qwen38-capacity64](qwen38-capacity64.md)<br>wave-ae389f52d12b5f8e9e4d | layout unspecified; mtp / 3 | 1 | 131,291 | 35 | cached_prefix; reused 131,072 | 262,144 / 786,432 | Not recorded | 45.74 | 15.75 | 1.46 | Pass |
| [qwen38-capacity64](qwen38-capacity64.md)<br>wave-b0ef0b95ddf0a92520f0 | layout unspecified; mtp / 3 | 16 | 2,335 to 24,865 | 256 | cached_prefix; reused 2,048 to 24,576 | 262,144 / 786,432 | Not recorded | 124.93 | 118.32 | 16.81 | Pass |
| [qwen38-capacity64](qwen38-capacity64.md)<br>wave-b3ce47c0ac19ed6235db | layout unspecified; mtp / 3 | 2 | 131,281 to 131,299 | 35 | cached_prefix; reused 131,072 | 262,144 / 786,432 | Not recorded | 53.82 | 15.87 | 3.19 | Pass |
| [qwen38-capacity64](qwen38-capacity64.md)<br>wave-b93d68192c3fb68364dd | layout unspecified; mtp / 3 | 1 | 32,982 | 35 | cached_prefix; reused 32,768 | 262,144 / 786,432 | Not recorded | 64.47 | 30.36 | 0.61 | Pass |
| [qwen38-capacity64](qwen38-capacity64.md)<br>wave-bf707cd9c7c2a461c09a | layout unspecified; mtp / 3 | 2 | 131,137 | 126 to 144 | cold; reused 0 | 262,144 / 786,432 | Not recorded | 41.13 | 1.08 | 242.86 | Pass |
| [qwen38-capacity64](qwen38-capacity64.md)<br>wave-d7e289fa91c7f80efc6f | layout unspecified; mtp / 3 | 2 | 32,981 | 35 | cached_prefix; reused 32,768 | 262,144 / 786,432 | Not recorded | 104.72 | 39.18 | 1.16 | Pass |
| [qwen38-capacity64](qwen38-capacity64.md)<br>wave-e8e5e973680b9376b1be | layout unspecified; mtp / 3 | 2 | 131,136 | 124 to 141 | cold; reused 32,768 | 262,144 / 786,432 | Not recorded | 35.49 | 1.10 | 232.73 | Pass |
| [qwen38-capacity64](qwen38-capacity64.md)<br>wave-e93105899c7400849cef | layout unspecified; mtp / 3 | 16 | 2,052 to 24,585 | 256 | cold; reused 0 | 262,144 / 786,432 | Not recorded | 74.66 | 48.85 | 54.72 | Pass |
| [qwen38-capacity64](qwen38-capacity64.md)<br>wave-ea114bdfd76e8c60f368 | layout unspecified; mtp / 3 | 2 | 32,986 | 35 | cached_prefix; reused 32,768 | 262,144 / 786,432 | Not recorded | 107.08 | 33.83 | 1.42 | Pass |
| [qwen38-capacity64](qwen38-capacity64.md)<br>wave-f742d1572ca7ec8859d8 | layout unspecified; mtp / 3 | 1 | 261,341 | 35 | cached_prefix; reused 261,120 | 262,144 / 786,432 | Not recorded | 27.14 | 9.52 | 2.39 | Pass |

Rates are whole-wave totals over the stated request count. A wave may span multiple independent model instances; [measurements.json](../measurements.json) retains their contributions and the exact configuration IDs. Do not interpret a multi-instance total as one card's rate.

A dash in shared decode means no qualified synchronized interval is available. Whole-wave throughput includes prefill and queueing. A valid decode interval can survive inside an overall failed or partial check; the source-report outcome is preserved. No rows are averaged.

## Bounded Checks

| Check | Reported outcome | Retained counts / flags |
| --- | --- | --- |
| check-0455cece5a079c6c1b8b | Pass | {"passed":true,"replayed_history_tokens":[60]} |
| check-0aea411e9ee5739130ce | Pass | {"passed":true,"replayed_history_tokens":[58]} |
| check-215ca24eca604f6cbc74 | Failed / partial | {"passed":false,"input_tokens":[261130,261130]} |
| check-2340c50dd5fb72d4a674 | Pass | {"passed":true,"replayed_history_tokens":[64,64]} |
| check-38eb2dbcdbd885efac96 | Pass | {"passed":true,"input_tokens":[131132,131132],"replayed_history_tokens":[64,64],"extension_cached_tokens":[32768,32768]} |
| check-4f903fffcb53edfcec9f | Pass | {"passed":true,"replayed_history_tokens":[58,58]} |
| check-50e98fc2907071f40ce1 | Pass | {"passed":true,"replayed_history_tokens":[57,57],"input_tokens":[32821,32821]} |
| check-6be8a46cf6b87dcc0a1d | Pass | {"passed":true,"input_tokens":[131127,131127],"replayed_history_tokens":[59,59],"extension_cached_tokens":[32768,32768]} |
| check-7864ea4168288578678a | Pass | {"passed":true,"replayed_history_tokens":[58,58],"input_tokens":[32822,32822]} |
| check-7a39a72cec9761ac7504 | Pass | {"passed":true,"replayed_history_tokens":[65,65],"input_tokens":[131133,131133]} |
| check-83e8d5fb3e35aabc523e | Pass | {"passed":true,"input_tokens":[24581,24581,16392,16392,2066,2066,2066,2066,2066,2066,2048,2048,2048,2048,2048,2048]} |
| check-8ae6659419d0fa974790 | Pass | {"passed":true,"replayed_history_tokens":[62,62]} |
| check-8e95473da70f6cbbef74 | Pass | {"passed":true,"input_tokens":[24581,24581,16392,16392,2066,2066,2066,2066,2066,2066,2048,2048,2048,2048,2048,2048]} |
| check-9d37801695e5ac755871 | Failed / partial | {"passed":false,"input_tokens":[261131,261131]} |
| check-a06fb33afb9e8ff1b01c | Pass | {"passed":true,"replayed_history_tokens":[62,62],"input_tokens":[32826,32826]} |
| check-a1e024b844b9af369eba | Pass | {"passed":true,"replayed_history_tokens":[59,59]} |
| check-d25c0dbf29973645f7ca | Failed / partial | {"passed":false,"input_tokens":[261182,261182]} |
| check-da6e53ee3f78a8abb8e8 | Pass | {"passed":true,"input_tokens":[131128],"replayed_history_tokens":[60],"extension_cached_tokens":[32768]} |
| check-e06cddb329b882469479 | Failed / partial | {"passed":false,"input_tokens":[131128,131128]} |
| check-e2a73021b6cb99ccd388 | Pass | {"passed":true,"replayed_history_tokens":[57,57]} |
| check-e7138eff0c0af6131fd9 | Pass | {"passed":true,"replayed_history_tokens":[58],"input_tokens":[32822]} |
| check-edc65010cc76b4079d70 | Pass | {"passed":true,"replayed_history_tokens":[67]} |
| check-eed3e72bb63890e9d970 | Pass | {"passed":true,"input_tokens":[261183],"replayed_history_tokens":[67],"extension_cached_tokens":[131072]} |
| check-eed79484a9d5b874bb7d | Pass | {"passed":true,"recurrent_restores":18,"restored_pages":0} |
| check-f1c3c50d575f1b442a2d | Pass | {"passed":true,"replayed_history_tokens":[65,65]} |
| check-f708229b8999d749245b | Pass | {"passed":true,"input_tokens":[24581,24581,16392,16392,2066,2066,2066,2066,2066,2066,2048,2048,2048,2048,2048,2048]} |

These checks retain their reported scope. A context/allocation/retrieval check is not a general quality score or a speed qualification at that context. Exact flags and provenance are in [checks.json](../checks.json).

## Additional Test Results

| Result / Source | Profile | Evidence type | Reported outcome | Retained values | Configuration binding |
| --- | --- | --- | --- | --- | --- |
| [result-002e119679a84d48d384](../observations.json)<br>source-fd1742349b8ddc8f6fe7368e.json<br>`/after_burst` | [qwen38-capacity64](qwen38-capacity64.md) | test outcome | Outcome unspecified | context=262,144 tokens | Recorded configuration/job |
| [result-008461e6fe253a623105](../observations.json)<br>source-1f783c967afb25ac6717263c.json<br>`/after_cold` | [qwen38-capacity64](qwen38-capacity64.md) | test outcome | Outcome unspecified | context=262,144 tokens | Recorded configuration/job |
| [result-0181c0ad5154d8f29c08](../observations.json)<br>source-66c488c9058e2600c318ba67.json<br>`/after_burst/totals` | [qwen38-capacity64](qwen38-capacity64.md) | context allocation | Outcome unspecified | cached_tokens=0 tokens; generated_tokens=788 accepted tokens; prompt_tokens=196,994 tokens; recurrent_restores=0 checkpoints | Recorded configuration/job |
| [result-02079e0c39b9785bf7dd](../observations.json)<br>source-53e2dba11cabfbcbc909eaf4.json<br>`/stages/1/warm` | [qwen38-capacity64](qwen38-capacity64.md) | test outcome | Outcome unspecified | end_to_end_output_tps=17.70 accepted tokens/s; generated_tokens=70 accepted tokens; wall_seconds=3.95 s | Recorded configuration/job |
| [result-0617610d72b99d750103](../observations.json)<br>source-bcfbe96ad0f3f9bc73646eec.json<br>`/after_cold/totals` | [qwen38-capacity64](qwen38-capacity64.md) | context allocation | Outcome unspecified | cached_tokens=458,752 tokens; generated_tokens=1,509 accepted tokens; prompt_tokens=851,958 tokens; recurrent_restores=20 checkpoints | Recorded configuration/job |
| [result-064e856fdaa7b158cc38](../observations.json)<br>source-3a76d6c0fc41d8343f284f4c.json<br>`/after_burst` | [qwen38-capacity64](qwen38-capacity64.md) | test outcome | Outcome unspecified | context=262,144 tokens | Recorded configuration/job |
| [result-090c55c7dfa096127d20](../observations.json)<br>source-2ee831ba64205cb24f66a69b.json<br>`/after_cold` | [qwen38-capacity64](qwen38-capacity64.md) | test outcome | Outcome unspecified | context=262,144 tokens | Recorded configuration/job |
| [result-0f197364e85a599e547b](../observations.json)<br>source-3a76d6c0fc41d8343f284f4c.json<br>`/after_cold/cache` | [qwen38-capacity64](qwen38-capacity64.md) | test outcome | Outcome unspecified | cached_tokens=32,768 tokens | Recorded configuration/job |
| [result-10c412c3aecb0c194f12](../observations.json)<br>source-bcfbe96ad0f3f9bc73646eec.json<br>`/after_cold/cache` | [qwen38-capacity64](qwen38-capacity64.md) | test outcome | Outcome unspecified | cached_tokens=392,192 tokens | Recorded configuration/job |
| [result-138f7ffa0776d3f97470](../observations.json)<br>source-a89528264f4263aa35c04d41.json<br>`/stages/0/cold` | [qwen38-capacity64](qwen38-capacity64.md) | test outcome | Outcome unspecified | end_to_end_output_tps=5.39 accepted tokens/s; generated_tokens=276 accepted tokens; wall_seconds=51.21 s | Recorded configuration/job |
| [result-13df4954d47bb7c888e5](../observations.json)<br>source-fd1742349b8ddc8f6fe7368e.json<br>`/after_cold` | [qwen38-capacity64](qwen38-capacity64.md) | test outcome | Outcome unspecified | context=262,144 tokens | Recorded configuration/job |
| [result-1f91a7c6771262eb1c1e](../observations.json)<br>source-f9752a5fb4c2c082c660a583.json<br>`/after_cold/cache` | [qwen38-capacity64](qwen38-capacity64.md) | test outcome | Outcome unspecified | cached_tokens=339,968 tokens | Recorded configuration/job |
| [result-23d9d76c1e80b453ae74](../observations.json)<br>source-1f783c967afb25ac6717263c.json<br>`/after_burst/totals` | [qwen38-capacity64](qwen38-capacity64.md) | context allocation | Outcome unspecified | cached_tokens=0 tokens; generated_tokens=788 accepted tokens; prompt_tokens=196,904 tokens; recurrent_restores=0 checkpoints | Recorded configuration/job |
| [result-251b8244b43a7c79aaa7](../observations.json)<br>source-53e2dba11cabfbcbc909eaf4.json<br>`/stages/1` | [qwen38-capacity64](qwen38-capacity64.md) | test outcome | Pass | replayed_history_tokens=59 tokens | Recorded configuration/job |
| [result-25a118101e128023386c](../observations.json)<br>source-a89528264f4263aa35c04d41.json<br>`/stages/1` | [qwen38-capacity64](qwen38-capacity64.md) | test outcome | Pass | replayed_history_tokens=64 tokens | Recorded configuration/job |
| [result-29556a87b23fa4b5e22a](../observations.json)<br>source-0088ce922f6f0541940f193f.json<br>`/stages/0/warm` | [qwen38-capacity64](qwen38-capacity64.md) | test outcome | Outcome unspecified | end_to_end_output_tps=15.87 accepted tokens/s; generated_tokens=70 accepted tokens; wall_seconds=4.41 s | Recorded configuration/job |
| [result-2a0c142e9bd6c674bd99](../observations.json)<br>source-4f7ccf9e99cb0e2e0aead535.json<br>`/after_burst` | [qwen38-capacity64](qwen38-capacity64.md) | test outcome | Outcome unspecified | context=262,144 tokens | Recorded configuration/job |
| [result-2b2333abf8f582583975](../observations.json)<br>source-299761edd345030299e192e2.json<br>`/after_cold/cache` | [qwen38-capacity64](qwen38-capacity64.md) | test outcome | Outcome unspecified | cached_tokens=110,592 tokens | Recorded configuration/job |
| [result-2c5d6a99f1ee4ad10d30](../observations.json)<br>source-4f7ccf9e99cb0e2e0aead535.json<br>`/after_cold` | [qwen38-capacity64](qwen38-capacity64.md) | test outcome | Outcome unspecified | context=262,144 tokens | Recorded configuration/job |
| [result-2e5e706e44e4e3f9ebb7](../observations.json)<br>source-2ee831ba64205cb24f66a69b.json<br>`/after_burst/cache` | [qwen38-capacity64](qwen38-capacity64.md) | test outcome | Outcome unspecified | cached_tokens=393,216 tokens | Recorded configuration/job |
| [result-31bc554ad4f460b595a8](../observations.json)<br>source-f9752a5fb4c2c082c660a583.json<br>`/after_cold/totals` | [qwen38-capacity64](qwen38-capacity64.md) | context allocation | Outcome unspecified | cached_tokens=212,992 tokens; generated_tokens=20,480 accepted tokens; prompt_tokens=542,494 tokens; recurrent_restores=32 checkpoints | Recorded configuration/job |
| [result-350219d6fb7941bea055](../observations.json)<br>source-ebd1e055c23981e778167ad3.json<br>`/after_cold` | [qwen38-capacity64](qwen38-capacity64.md) | test outcome | Outcome unspecified | context=262,144 tokens | Recorded configuration/job |
| [result-3d8f493a5d328f773839](../observations.json)<br>source-0749fbc670e41eb383941368.json<br>`/stages/2` | [qwen38-capacity64](qwen38-capacity64.md) | test outcome | Pass | replayed_history_tokens=67 tokens | Recorded configuration/job |
| [result-4022ffe41f40110fb4d5](../observations.json)<br>source-a89528264f4263aa35c04d41.json<br>`/stages/1/cold` | [qwen38-capacity64](qwen38-capacity64.md) | test outcome | Outcome unspecified | end_to_end_output_tps=1.10 accepted tokens/s; generated_tokens=265 accepted tokens; wall_seconds=239.91 s | Recorded configuration/job |
| [result-40f966e7a8150d27e299](../observations.json)<br>source-2ee831ba64205cb24f66a69b.json<br>`/after_cold/cache` | [qwen38-capacity64](qwen38-capacity64.md) | test outcome | Outcome unspecified | cached_tokens=262,144 tokens | Recorded configuration/job |
| [result-43aa6e3652a4e1bdc745](../observations.json)<br>source-a89528264f4263aa35c04d41.json<br>`/stages/0/warm` | [qwen38-capacity64](qwen38-capacity64.md) | test outcome | Outcome unspecified | end_to_end_output_tps=33.83 accepted tokens/s; generated_tokens=70 accepted tokens; wall_seconds=2.07 s | Recorded configuration/job |
| [result-43d2a381924eb51656a2](../observations.json)<br>source-4f7ccf9e99cb0e2e0aead535.json<br>`/after_burst/cache` | [qwen38-capacity64](qwen38-capacity64.md) | test outcome | Outcome unspecified | cached_tokens=393,216 tokens | Recorded configuration/job |
| [result-441a891a641203f0a47c](../observations.json)<br>source-bcfbe96ad0f3f9bc73646eec.json<br>`/after_cold` | [qwen38-capacity64](qwen38-capacity64.md) | test outcome | Outcome unspecified | context=262,144 tokens | Recorded configuration/job |
| [result-459b699f06d6d5023944](../observations.json)<br>source-53e2dba11cabfbcbc909eaf4.json<br>`/stages/0/warm` | [qwen38-capacity64](qwen38-capacity64.md) | test outcome | Outcome unspecified | end_to_end_output_tps=39.18 accepted tokens/s; generated_tokens=70 accepted tokens; wall_seconds=1.79 s | Recorded configuration/job |
| [result-474ffd186fa1b84ed943](../observations.json)<br>source-0088ce922f6f0541940f193f.json<br>`/stages/0` | [qwen38-capacity64](qwen38-capacity64.md) | test outcome | Pass | replayed_history_tokens=65 tokens | Recorded configuration/job |
| [result-495e95171e1ccd450a58](../observations.json)<br>source-6178d8ef8dda3619ae08fe20.json<br>`/stages/0/cold` | [qwen38-capacity64](qwen38-capacity64.md) | test outcome | Outcome unspecified | end_to_end_output_tps=6.69 accepted tokens/s; generated_tokens=276 accepted tokens; wall_seconds=41.25 s | Recorded configuration/job |
| [result-49e135d38cbced0f1208](../observations.json)<br>source-c67c5067ae61ab454422b7e3.json<br>`/runs/2/warm` | [qwen38-capacity64](qwen38-capacity64.md) | test outcome | Outcome unspecified | end_to_end_output_tps=121.74 accepted tokens/s; generated_tokens=4,096 accepted tokens; wall_seconds=33.65 s | Recorded configuration/job |
| [result-52eeaaa3983602a144c5](../observations.json)<br>source-53e2dba11cabfbcbc909eaf4.json<br>`/stages/0/cold` | [qwen38-capacity64](qwen38-capacity64.md) | test outcome | Outcome unspecified | end_to_end_output_tps=6.80 accepted tokens/s; generated_tokens=276 accepted tokens; wall_seconds=40.59 s | Recorded configuration/job |
| [result-53f5c9a160f6b4583696](../observations.json)<br>source-2ee831ba64205cb24f66a69b.json<br>`/after_burst` | [qwen38-capacity64](qwen38-capacity64.md) | test outcome | Outcome unspecified | context=262,144 tokens | Recorded configuration/job |
| [result-54c95c80f0a055f5586b](../observations.json)<br>source-bcfbe96ad0f3f9bc73646eec.json<br>`/after_burst` | [qwen38-capacity64](qwen38-capacity64.md) | test outcome | Outcome unspecified | context=262,144 tokens | Recorded configuration/job |
| [result-552bf7f9ffe9f9ab5e28](../observations.json)<br>source-1f783c967afb25ac6717263c.json<br>`/after_cold/totals` | [qwen38-capacity64](qwen38-capacity64.md) | context allocation | Outcome unspecified | cached_tokens=0 tokens; generated_tokens=276 accepted tokens; prompt_tokens=65,650 tokens; recurrent_restores=0 checkpoints | Recorded configuration/job |
| [result-585da25cb51cf0c2e325](../observations.json)<br>source-2ee831ba64205cb24f66a69b.json<br>`/after_cold/totals` | [qwen38-capacity64](qwen38-capacity64.md) | context allocation | Outcome unspecified | cached_tokens=0 tokens; generated_tokens=270 accepted tokens; prompt_tokens=262,274 tokens; recurrent_restores=0 checkpoints | Recorded configuration/job |
| [result-5969e73de891d955b75d](../observations.json)<br>source-c67c5067ae61ab454422b7e3.json<br>`/runs/0/warm` | [qwen38-capacity64](qwen38-capacity64.md) | test outcome | Outcome unspecified | end_to_end_output_tps=118.32 accepted tokens/s; generated_tokens=4,096 accepted tokens; wall_seconds=34.62 s | Recorded configuration/job |
| [result-5a482d1b37364aca7381](../observations.json)<br>source-f12f590f9e81881753e1336c.json<br>`/after_burst` | [qwen38-capacity64](qwen38-capacity64.md) | test outcome | Outcome unspecified | context=262,144 tokens | Recorded configuration/job |
| [result-5bbd02636893e20c1cc5](../observations.json)<br>source-5230e9173393f28507b0dcd6.json<br>`/after_cold/totals` | [qwen38-capacity64](qwen38-capacity64.md) | context allocation | Outcome unspecified | cached_tokens=106,496 tokens; generated_tokens=12,288 accepted tokens; prompt_tokens=324,594 tokens; recurrent_restores=16 checkpoints | Recorded configuration/job |
| [result-5cf328c32ca751919e83](../observations.json)<br>source-ebd1e055c23981e778167ad3.json<br>`/after_burst/totals` | [qwen38-capacity64](qwen38-capacity64.md) | context allocation | Outcome unspecified | cached_tokens=262,144 tokens; generated_tokens=1,635 accepted tokens; prompt_tokens=656,572 tokens; recurrent_restores=20 checkpoints | Recorded configuration/job |
| [result-5deb062d28f5ca155795](../observations.json)<br>source-3a76d6c0fc41d8343f284f4c.json<br>`/after_cold` | [qwen38-capacity64](qwen38-capacity64.md) | test outcome | Outcome unspecified | context=262,144 tokens | Recorded configuration/job |
| [result-5e857bc33d082f7876d3](../observations.json)<br>source-fd1742349b8ddc8f6fe7368e.json<br>`/after_cold/totals` | [qwen38-capacity64](qwen38-capacity64.md) | context allocation | Outcome unspecified | cached_tokens=65,536 tokens; generated_tokens=826 accepted tokens; prompt_tokens=328,210 tokens; recurrent_restores=2 checkpoints | Recorded configuration/job |
| [result-5f8ae4369b3b1d07cd6d](../observations.json)<br>source-f12f590f9e81881753e1336c.json<br>`/after_cold/totals` | [qwen38-capacity64](qwen38-capacity64.md) | context allocation | Outcome unspecified | cached_tokens=0 tokens; generated_tokens=276 accepted tokens; prompt_tokens=65,652 tokens; recurrent_restores=0 checkpoints | Recorded configuration/job |
| [result-66a325fa657d704e8f93](../observations.json)<br>source-6178d8ef8dda3619ae08fe20.json<br>`/stages/0` | [qwen38-capacity64](qwen38-capacity64.md) | test outcome | Pass | replayed_history_tokens=58 tokens | Recorded configuration/job |
| [result-70f574e3ce601399fa2e](../observations.json)<br>source-c67c5067ae61ab454422b7e3.json<br>`/runs/1/warm` | [qwen38-capacity64](qwen38-capacity64.md) | test outcome | Outcome unspecified | end_to_end_output_tps=115.65 accepted tokens/s; generated_tokens=4,096 accepted tokens; wall_seconds=35.42 s | Recorded configuration/job |
| [result-73b82a16fd3dfb578036](../observations.json)<br>source-66c488c9058e2600c318ba67.json<br>`/after_cold/totals` | [qwen38-capacity64](qwen38-capacity64.md) | context allocation | Outcome unspecified | cached_tokens=0 tokens; generated_tokens=276 accepted tokens; prompt_tokens=65,660 tokens; recurrent_restores=0 checkpoints | Recorded configuration/job |
| [result-763aedad04fc3acb5ad1](../observations.json)<br>source-5230e9173393f28507b0dcd6.json<br>`/after_cold/cache` | [qwen38-capacity64](qwen38-capacity64.md) | test outcome | Outcome unspecified | cached_tokens=225,280 tokens | Recorded configuration/job |
| [result-77b0404f84116f1510f5](../observations.json)<br>source-1f783c967afb25ac6717263c.json<br>`/after_cold/cache` | [qwen38-capacity64](qwen38-capacity64.md) | test outcome | Outcome unspecified | cached_tokens=65,536 tokens | Recorded configuration/job |
| [result-7856e0944761fec6d575](../observations.json)<br>source-bcfbe96ad0f3f9bc73646eec.json<br>`/after_burst/totals` | [qwen38-capacity64](qwen38-capacity64.md) | context allocation | Outcome unspecified | cached_tokens=589,824 tokens; generated_tokens=2,021 accepted tokens; prompt_tokens=983,228 tokens; recurrent_restores=36 checkpoints | Recorded configuration/job |
| [result-7859eaf380013c5f3ccc](../observations.json)<br>source-bcfbe96ad0f3f9bc73646eec.json<br>`/after_burst/cache` | [qwen38-capacity64](qwen38-capacity64.md) | test outcome | Outcome unspecified | cached_tokens=392,192 tokens | Recorded configuration/job |
| [result-7cb4468f653ce5998222](../observations.json)<br>source-c67c5067ae61ab454422b7e3.json<br>`/runs/0/cold` | [qwen38-capacity64](qwen38-capacity64.md) | test outcome | Outcome unspecified | end_to_end_output_tps=48.83 accepted tokens/s; generated_tokens=4,096 accepted tokens; wall_seconds=83.89 s | Recorded configuration/job |
| [result-7d8a838245dc935b2373](../observations.json)<br>source-c67c5067ae61ab454422b7e3.json<br>`/runs/2/cold` | [qwen38-capacity64](qwen38-capacity64.md) | test outcome | Outcome unspecified | end_to_end_output_tps=48.85 accepted tokens/s; generated_tokens=4,096 accepted tokens; wall_seconds=83.85 s | Recorded configuration/job |
| [result-81bb7afcc29bc184fc89](../observations.json)<br>source-ebd1e055c23981e778167ad3.json<br>`/after_burst/cache` | [qwen38-capacity64](qwen38-capacity64.md) | test outcome | Outcome unspecified | cached_tokens=393,216 tokens | Recorded configuration/job |
| [result-84b24111cb0eb8ec0028](../observations.json)<br>source-a89528264f4263aa35c04d41.json<br>`/stages/1/warm` | [qwen38-capacity64](qwen38-capacity64.md) | test outcome | Outcome unspecified | end_to_end_output_tps=15.95 accepted tokens/s; generated_tokens=70 accepted tokens; wall_seconds=4.39 s | Recorded configuration/job |
| [result-8a18fe71448f78dd05ff](../observations.json)<br>source-f9752a5fb4c2c082c660a583.json<br>`/after_cold` | [qwen38-capacity64](qwen38-capacity64.md) | test outcome | Outcome unspecified | context=262,144 tokens | Recorded configuration/job |
| [result-958dc8bdacbd5938d1d9](../observations.json)<br>source-5230e9173393f28507b0dcd6.json<br>`/after_cold` | [qwen38-capacity64](qwen38-capacity64.md) | test outcome | Outcome unspecified | context=262,144 tokens | Recorded configuration/job |
| [result-95a11c878dac83f444b9](../observations.json)<br>source-66c488c9058e2600c318ba67.json<br>`/after_cold` | [qwen38-capacity64](qwen38-capacity64.md) | test outcome | Outcome unspecified | context=262,144 tokens | Recorded configuration/job |
| [result-95dc9562f0774e9e73a2](../observations.json)<br>source-f12f590f9e81881753e1336c.json<br>`/after_burst/totals` | [qwen38-capacity64](qwen38-capacity64.md) | context allocation | Outcome unspecified | cached_tokens=0 tokens; generated_tokens=788 accepted tokens; prompt_tokens=196,922 tokens; recurrent_restores=0 checkpoints | Recorded configuration/job |
| [result-95fd35397ef23b554227](../observations.json)<br>source-4f7ccf9e99cb0e2e0aead535.json<br>`/after_cold/totals` | [qwen38-capacity64](qwen38-capacity64.md) | context allocation | Outcome unspecified | cached_tokens=131,072 tokens; generated_tokens=1,140 accepted tokens; prompt_tokens=525,128 tokens; recurrent_restores=4 checkpoints | Recorded configuration/job |
| [result-9717ecb6a968592ce084](../observations.json)<br>source-c67c5067ae61ab454422b7e3.json<br>`/runs/1/cold` | [qwen38-capacity64](qwen38-capacity64.md) | test outcome | Outcome unspecified | end_to_end_output_tps=47.56 accepted tokens/s; generated_tokens=4,096 accepted tokens; wall_seconds=86.13 s | Recorded configuration/job |
| [result-98293112288b7bd5bee1](../observations.json)<br>source-f12f590f9e81881753e1336c.json<br>`/after_cold` | [qwen38-capacity64](qwen38-capacity64.md) | test outcome | Outcome unspecified | context=262,144 tokens | Recorded configuration/job |
| [result-9b6ce574c034a34fd2ec](../observations.json)<br>source-ebd1e055c23981e778167ad3.json<br>`/after_cold/cache` | [qwen38-capacity64](qwen38-capacity64.md) | test outcome | Outcome unspecified | cached_tokens=393,216 tokens | Recorded configuration/job |
| [result-a0c433be7974e932e96a](../observations.json)<br>source-0749fbc670e41eb383941368.json<br>`/stages/1` | [qwen38-capacity64](qwen38-capacity64.md) | test outcome | Pass | replayed_history_tokens=60 tokens | Recorded configuration/job |
| [result-a22ed542d883d2b2a418](../observations.json)<br>source-fd1742349b8ddc8f6fe7368e.json<br>`/after_burst/cache` | [qwen38-capacity64](qwen38-capacity64.md) | test outcome | Outcome unspecified | cached_tokens=262,144 tokens | Recorded configuration/job |
| [result-a6de021b2127aee9c299](../observations.json)<br>source-ebd1e055c23981e778167ad3.json<br>`/after_cold/totals` | [qwen38-capacity64](qwen38-capacity64.md) | context allocation | Outcome unspecified | cached_tokens=131,072 tokens; generated_tokens=1,123 accepted tokens; prompt_tokens=525,238 tokens; recurrent_restores=4 checkpoints | Recorded configuration/job |
| [result-aa693cb0cb471039ae33](../observations.json)<br>source-0749fbc670e41eb383941368.json<br>`/stages/0/warm` | [qwen38-capacity64](qwen38-capacity64.md) | test outcome | Outcome unspecified | end_to_end_output_tps=30.36 accepted tokens/s; generated_tokens=35 accepted tokens; wall_seconds=1.15 s | Recorded configuration/job |
| [result-adbdb150bbe59e84a04d](../observations.json)<br>source-a89528264f4263aa35c04d41.json<br>`/stages/2/cold` | [qwen38-capacity64](qwen38-capacity64.md) | test outcome | Outcome unspecified | end_to_end_output_tps=0.49 accepted tokens/s; generated_tokens=260 accepted tokens; wall_seconds=525.52 s | Recorded configuration/job |
| [result-b5a510b3a9e0dc62e24b](../observations.json)<br>source-1f783c967afb25ac6717263c.json<br>`/after_burst` | [qwen38-capacity64](qwen38-capacity64.md) | test outcome | Outcome unspecified | context=262,144 tokens | Recorded configuration/job |
| [result-bb4ce3f3ebaf59570b26](../observations.json)<br>source-3a76d6c0fc41d8343f284f4c.json<br>`/after_burst/cache` | [qwen38-capacity64](qwen38-capacity64.md) | test outcome | Outcome unspecified | cached_tokens=163,840 tokens | Recorded configuration/job |
| [result-bcebdd2d3b1020b5aad8](../observations.json)<br>source-3a76d6c0fc41d8343f284f4c.json<br>`/after_cold/totals` | [qwen38-capacity64](qwen38-capacity64.md) | context allocation | Outcome unspecified | cached_tokens=0 tokens; generated_tokens=138 accepted tokens; prompt_tokens=32,826 tokens; recurrent_restores=0 checkpoints | Recorded configuration/job |
| [result-bf684013c11837cd452d](../observations.json)<br>source-5b7d9e870991bce638bfc9f0.json<br>`/` | [qwen38-capacity64](qwen38-capacity64.md) | performance detail | Pass | cases: 3 requests | Recorded configuration/job |
| [result-c3282039cd482f3231a3](../observations.json)<br>source-66c488c9058e2600c318ba67.json<br>`/after_cold/cache` | [qwen38-capacity64](qwen38-capacity64.md) | test outcome | Outcome unspecified | cached_tokens=65,536 tokens | Recorded configuration/job |
| [result-c41f7724ce65788ef3ab](../observations.json)<br>source-66c488c9058e2600c318ba67.json<br>`/after_burst` | [qwen38-capacity64](qwen38-capacity64.md) | test outcome | Outcome unspecified | context=262,144 tokens | Recorded configuration/job |
| [result-ca473446785d8863890a](../observations.json)<br>source-3a76d6c0fc41d8343f284f4c.json<br>`/after_burst/totals` | [qwen38-capacity64](qwen38-capacity64.md) | context allocation | Outcome unspecified | cached_tokens=0 tokens; generated_tokens=650 accepted tokens; prompt_tokens=164,096 tokens; recurrent_restores=0 checkpoints | Recorded configuration/job |
| [result-cc7e0bbb11692e1113ef](../observations.json)<br>source-2ee831ba64205cb24f66a69b.json<br>`/after_burst/totals` | [qwen38-capacity64](qwen38-capacity64.md) | context allocation | Outcome unspecified | cached_tokens=0 tokens; generated_tokens=782 accepted tokens; prompt_tokens=393,624 tokens; recurrent_restores=0 checkpoints | Recorded configuration/job |
| [result-cd308e9b37c5298a6ca3](../observations.json)<br>source-a89528264f4263aa35c04d41.json<br>`/stages/0` | [qwen38-capacity64](qwen38-capacity64.md) | test outcome | Pass | replayed_history_tokens=62 tokens | Recorded configuration/job |
| [result-d09347066bdf6ec47f8c](../observations.json)<br>source-0749fbc670e41eb383941368.json<br>`/stages/0` | [qwen38-capacity64](qwen38-capacity64.md) | test outcome | Pass | replayed_history_tokens=58 tokens | Recorded configuration/job |
| [result-d13766dec49fe3fbd188](../observations.json)<br>source-0749fbc670e41eb383941368.json<br>`/stages/2/cold` | [qwen38-capacity64](qwen38-capacity64.md) | test outcome | Outcome unspecified | end_to_end_output_tps=0.60 accepted tokens/s; generated_tokens=136 accepted tokens; wall_seconds=227.13 s | Recorded configuration/job |
| [result-d425be3b18f3e7b39d83](../observations.json)<br>source-6178d8ef8dda3619ae08fe20.json<br>`/stages/0/warm` | [qwen38-capacity64](qwen38-capacity64.md) | test outcome | Outcome unspecified | end_to_end_output_tps=36.89 accepted tokens/s; generated_tokens=70 accepted tokens; wall_seconds=1.90 s | Recorded configuration/job |
| [result-d4b3264677c22f6e05f1](../observations.json)<br>source-0088ce922f6f0541940f193f.json<br>`/stages/0/cold` | [qwen38-capacity64](qwen38-capacity64.md) | test outcome | Outcome unspecified | end_to_end_output_tps=1.08 accepted tokens/s; generated_tokens=270 accepted tokens; wall_seconds=249.43 s | Recorded configuration/job |
| [result-d665308bded6f6421a41](../observations.json)<br>source-66c488c9058e2600c318ba67.json<br>`/after_burst/cache` | [qwen38-capacity64](qwen38-capacity64.md) | test outcome | Outcome unspecified | cached_tokens=196,608 tokens | Recorded configuration/job |
| [result-dbb26189b95c32b8afc8](../observations.json)<br>source-f12f590f9e81881753e1336c.json<br>`/after_cold/cache` | [qwen38-capacity64](qwen38-capacity64.md) | test outcome | Outcome unspecified | cached_tokens=65,536 tokens | Recorded configuration/job |
| [result-dbc4def0e3ccfba06868](../observations.json)<br>source-4f7ccf9e99cb0e2e0aead535.json<br>`/after_burst/totals` | [qwen38-capacity64](qwen38-capacity64.md) | context allocation | Outcome unspecified | cached_tokens=262,144 tokens; generated_tokens=1,652 accepted tokens; prompt_tokens=656,382 tokens; recurrent_restores=20 checkpoints | Recorded configuration/job |
| [result-df62d93c4b507e3024fa](../observations.json)<br>source-1f783c967afb25ac6717263c.json<br>`/after_burst/cache` | [qwen38-capacity64](qwen38-capacity64.md) | test outcome | Outcome unspecified | cached_tokens=196,608 tokens | Recorded configuration/job |
| [result-e17236d4250b152b4f26](../observations.json)<br>source-299761edd345030299e192e2.json<br>`/after_cold/totals` | [qwen38-capacity64](qwen38-capacity64.md) | context allocation | Outcome unspecified | cached_tokens=0 tokens; generated_tokens=4,096 accepted tokens; prompt_tokens=106,694 tokens; recurrent_restores=0 checkpoints | Recorded configuration/job |
| [result-e95c6f5254c24526b652](../observations.json)<br>source-299761edd345030299e192e2.json<br>`/after_cold` | [qwen38-capacity64](qwen38-capacity64.md) | test outcome | Outcome unspecified | context=262,144 tokens | Recorded configuration/job |
| [result-e9e0dd75e9b590724157](../observations.json)<br>source-53e2dba11cabfbcbc909eaf4.json<br>`/stages/0` | [qwen38-capacity64](qwen38-capacity64.md) | test outcome | Pass | replayed_history_tokens=57 tokens | Recorded configuration/job |
| [result-eba05353849424a176d7](../observations.json)<br>source-4f7ccf9e99cb0e2e0aead535.json<br>`/after_cold/cache` | [qwen38-capacity64](qwen38-capacity64.md) | test outcome | Outcome unspecified | cached_tokens=393,216 tokens | Recorded configuration/job |
| [result-ed06e72ea440b8b61aaa](../observations.json)<br>source-0749fbc670e41eb383941368.json<br>`/` | [qwen38-capacity64](qwen38-capacity64.md) | context allocation | Pass | recurrent_restores=18 checkpoints; restored_pages=0 pages | Recorded configuration/job |
| [result-f1007a0b57dbebd627e0](../observations.json)<br>source-53e2dba11cabfbcbc909eaf4.json<br>`/stages/1/cold` | [qwen38-capacity64](qwen38-capacity64.md) | test outcome | Outcome unspecified | end_to_end_output_tps=1.42 accepted tokens/s; generated_tokens=282 accepted tokens; wall_seconds=198.82 s | Recorded configuration/job |
| [result-f3ac3983c28249415fd7](../observations.json)<br>source-0749fbc670e41eb383941368.json<br>`/stages/2/warm` | [qwen38-capacity64](qwen38-capacity64.md) | test outcome | Outcome unspecified | end_to_end_output_tps=9.52 accepted tokens/s; generated_tokens=35 accepted tokens; wall_seconds=3.67 s | Recorded configuration/job |
| [result-f3f62b71d700c7480fd4](../observations.json)<br>source-ebd1e055c23981e778167ad3.json<br>`/after_burst` | [qwen38-capacity64](qwen38-capacity64.md) | test outcome | Outcome unspecified | context=262,144 tokens | Recorded configuration/job |
| [result-f716932f21d121406d34](../observations.json)<br>source-f12f590f9e81881753e1336c.json<br>`/after_burst/cache` | [qwen38-capacity64](qwen38-capacity64.md) | test outcome | Outcome unspecified | cached_tokens=196,608 tokens | Recorded configuration/job |
| [result-f7f40c5260b6a1c2cb56](../observations.json)<br>source-0749fbc670e41eb383941368.json<br>`/stages/1/cold` | [qwen38-capacity64](qwen38-capacity64.md) | test outcome | Outcome unspecified | end_to_end_output_tps=1.38 accepted tokens/s; generated_tokens=141 accepted tokens; wall_seconds=101.89 s | Recorded configuration/job |
| [result-f8d04475e91e4c769e71](../observations.json)<br>source-fd1742349b8ddc8f6fe7368e.json<br>`/after_burst/totals` | [qwen38-capacity64](qwen38-capacity64.md) | context allocation | Outcome unspecified | cached_tokens=196,608 tokens; generated_tokens=1,338 accepted tokens; prompt_tokens=459,480 tokens; recurrent_restores=18 checkpoints | Recorded configuration/job |
| [result-fdfef16a1e65e337b5f7](../observations.json)<br>source-0749fbc670e41eb383941368.json<br>`/stages/1/warm` | [qwen38-capacity64](qwen38-capacity64.md) | test outcome | Outcome unspecified | end_to_end_output_tps=15.75 accepted tokens/s; generated_tokens=35 accepted tokens; wall_seconds=2.22 s | Recorded configuration/job |
| [result-fe57d5f58e8f3f963b6e](../observations.json)<br>source-0749fbc670e41eb383941368.json<br>`/stages/0/cold` | [qwen38-capacity64](qwen38-capacity64.md) | test outcome | Outcome unspecified | end_to_end_output_tps=6.37 accepted tokens/s; generated_tokens=138 accepted tokens; wall_seconds=21.65 s | Recorded configuration/job |
| [result-ffa50dfcb257579b10cc](../observations.json)<br>source-fd1742349b8ddc8f6fe7368e.json<br>`/after_cold/cache` | [qwen38-capacity64](qwen38-capacity64.md) | test outcome | Outcome unspecified | cached_tokens=262,144 tokens | Recorded configuration/job |

These are saved result records, including failures and bounded checks. Copies, individual requests, report summaries and regrading can overlap; their counts are not independent test repetitions. Open each result for exact values, units, configuration binding and source receipts.

There are 8 retained lifecycle records. Their states, exit codes and configuration IDs remain in [catalog.json](../catalog.json); they do not supply missing benchmark results.

[Full archive](../../README.md) | [All retained waves](../RESULTS.md) | [Data definitions](../DATA.md) | [Recommended recipes](../../../README.md)
