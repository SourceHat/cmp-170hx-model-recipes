# qwen38-fit-mtp1

**Historical record. Legacy / incomplete measurements.**

Model family: Qwen 3.8 27B.

Recorded archive reason: Fit, pilot or control configuration; measured serving variants have separate records.

Historical configurations are provided for comparison. The [recommended recipes](../../../README.md) include supported launch scripts.

Current recipes using the same recorded checkpoint repository: [qwen3.8-27b-exl3](../../../recipes/qwen3.8-27b-exl3/README.md). Context, cache and runtime versions can differ.

## Saved Configuration Versions

Each configuration ID identifies a distinct original settings record. Deployment fields are omitted; versions can have identical published settings after that omission. Upstream runtime commits remain unspecified where the source retained only an integration label.

| Configuration | Recorded artifact / source | Configured card counts | Context tokens | GPU pool tokens | Slots | Draft mode / tokens |
| --- | --- | --- | --- | --- | --- | --- |
| cfg-20fa4ad1dbac96e7ddae | [turboderp/Qwen3.8-27B-exl3@9e4c23cfb2](https://huggingface.co/turboderp/Qwen3.8-27B-exl3/tree/9e4c23cfb23697165b8e2f6da2a1df995f66353c) | 1 | 262,144 | 917,504 | 16 | mtp / 1 |
| cfg-2feeae54e9e65f8f0e99 | [turboderp/Qwen3.8-27B-exl3@9e4c23cfb2](https://huggingface.co/turboderp/Qwen3.8-27B-exl3/tree/9e4c23cfb23697165b8e2f6da2a1df995f66353c) | 1 | 262,144 | 917,504 | 16 | mtp / 1 |
| cfg-495aba6df811ccdcc715 | [turboderp/Qwen3.8-27B-exl3@9e4c23cfb2](https://huggingface.co/turboderp/Qwen3.8-27B-exl3/tree/9e4c23cfb23697165b8e2f6da2a1df995f66353c) | 1 | 262,144 | 917,504 | 16 | mtp / 1 |
| cfg-624d83c815ef08c0967d | [turboderp/Qwen3.8-27B-exl3@9e4c23cfb2](https://huggingface.co/turboderp/Qwen3.8-27B-exl3/tree/9e4c23cfb23697165b8e2f6da2a1df995f66353c) | 1 | 262,144 | 917,504 | 16 | mtp / 1 |
| cfg-749153d62f172d15d851 | [turboderp/Qwen3.8-27B-exl3@9e4c23cfb2](https://huggingface.co/turboderp/Qwen3.8-27B-exl3/tree/9e4c23cfb23697165b8e2f6da2a1df995f66353c) | 1 | 262,144 | 917,504 | 16 | mtp / 1 |
| cfg-82da5091b359fe4f6ab7 | [turboderp/Qwen3.8-27B-exl3@9e4c23cfb2](https://huggingface.co/turboderp/Qwen3.8-27B-exl3/tree/9e4c23cfb23697165b8e2f6da2a1df995f66353c) | 1 | 262,144 | 983,040 | 16 | mtp / 1 |
| cfg-dc2f8d0214631a8a67c3 | [turboderp/Qwen3.8-27B-exl3@9e4c23cfb2](https://huggingface.co/turboderp/Qwen3.8-27B-exl3/tree/9e4c23cfb23697165b8e2f6da2a1df995f66353c) | 1 | 262,144 | 983,040 | 16 | mtp / 1 |
| cfg-e7f101d736c27e6b9933 | [turboderp/Qwen3.8-27B-exl3@9e4c23cfb2](https://huggingface.co/turboderp/Qwen3.8-27B-exl3/tree/9e4c23cfb23697165b8e2f6da2a1df995f66353c) | 1 | 262,144 | 917,504 | 16 | mtp / 1 |
| cfg-eed64e692dba3b4c4779 | [turboderp/Qwen3.8-27B-exl3@9e4c23cfb2](https://huggingface.co/turboderp/Qwen3.8-27B-exl3/tree/9e4c23cfb23697165b8e2f6da2a1df995f66353c) | 1 | 262,144 | 917,504 | 16 | mtp / 1 |

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
<summary>cfg-2feeae54e9e65f8f0e99</summary>

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
<summary>cfg-495aba6df811ccdcc715</summary>

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
<summary>cfg-624d83c815ef08c0967d</summary>

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
  "served_model_label": "qwen3.8-27b",
  "power_watts_values_unordered": []
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
<summary>cfg-82da5091b359fe4f6ab7</summary>

```json
{
  "kind": "tabby",
  "gpu_counts": [
    1
  ],
  "context": 262144,
  "cache_tokens": 983040,
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
<summary>cfg-dc2f8d0214631a8a67c3</summary>

```json
{
  "kind": "tabby",
  "gpu_counts": [
    1
  ],
  "context": 262144,
  "cache_tokens": 983040,
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

<details>
<summary>cfg-eed64e692dba3b4c4779</summary>

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
  "served_model_label": "qwen3.8-27b",
  "power_watts_values_unordered": [
    150,
    175
  ]
}
```

Pinned model revision recorded: yes. Source receipt labels, hashes and object locators are retained in [configurations.json](../configurations.json).

</details>

## Retained Measurements

| Profile / Wave | Layout; Draft / Tokens | Requests | Input tokens/request | Accepted output tokens/request | Cache / Reused input tokens | Context / GPU pool tokens | Shared decode tok/s total | Client after-first-token estimate tok/s | Whole-wave output tok/s | Median TTFT, s | Source report |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [qwen38-fit-mtp1](qwen38-fit-mtp1.md)<br>wave-03e12bc2556077fc884d | layout unspecified; mtp / 1 | 16 | 8,357 to 8,360 | 128 | cached_prefix; reused 8,192 | 262,144 / 917,504 | Not recorded | 109.25 | 104.85 | 9.03 | Pass |
| [qwen38-fit-mtp1](qwen38-fit-mtp1.md)<br>wave-21acd006c348e7e0c0f8 | layout unspecified; mtp / 1 | 2 | 261,698 | 128 | cold; reused 131,072 | 262,144 / 917,504 | Not recorded | 14.49 | 0.58 | 429.62 | Pass |
| [qwen38-fit-mtp1](qwen38-fit-mtp1.md)<br>wave-55515d78b6f329c3aa08 | layout unspecified; mtp / 1 | 2 | 131,130 | 128 | cold; reused 32,768 | 262,144 / 917,504 | Not recorded | 27.41 | 1.27 | 193.16 | Pass |
| [qwen38-fit-mtp1](qwen38-fit-mtp1.md)<br>wave-60d6ca9f19a0bb8bf604 | layout unspecified; mtp / 1 | 2 | 131,278 | 35 | cached_prefix; reused 131,072 | 262,144 / 917,504 | Not recorded | 44.78 | 16.39 | 2.71 | Pass |
| [qwen38-fit-mtp1](qwen38-fit-mtp1.md)<br>wave-65ab128d90a71dd5ab6b | layout unspecified; mtp / 1 | 4 | 32,971 | 35 | cached_prefix; reused 32,768 | 262,144 / 917,504 | Not recorded | 48.51 | 38.75 | 2.46 | Pass |
| [qwen38-fit-mtp1](qwen38-fit-mtp1.md)<br>wave-747f807c3b030a8968af | layout unspecified; mtp / 1 | 2 | 261,846 | 35 | cached_prefix; reused 261,632 | 262,144 / 917,504 | Not recorded | 15.84 | 9.81 | 3.92 | Pass |
| [qwen38-fit-mtp1](qwen38-fit-mtp1.md)<br>wave-76a67e38d65ec4059734 | layout unspecified; mtp / 1 | 1 | 131,132 | 141 | cold; reused 0 | 262,144 / 917,504 | Not recorded | 26.95 | 1.00 | 135.36 | Failed / partial |
| [qwen38-fit-mtp1](qwen38-fit-mtp1.md)<br>wave-8c853f47796854a07837 | layout unspecified; mtp / 1 | 4 | 131,130 | 128 | cold; reused 32,768 | 262,144 / 917,504 | Not recorded | 26.97 | 1.28 | 390.73 | Pass |
| [qwen38-fit-mtp1](qwen38-fit-mtp1.md)<br>wave-9eeb976c08d46f713490 | layout unspecified; mtp / 1 | 2 | 131,130 | 128 | cold; reused 0 | 262,144 / 917,504 | Not recorded | 39.62 | 1.11 | 224.94 | Pass |
| [qwen38-fit-mtp1](qwen38-fit-mtp1.md)<br>wave-9f6d9f5d9242ac8fba16 | layout unspecified; mtp / 1 | 2 | 131,277 | 35 | cached_prefix; reused 131,072 | 262,144 / 917,504 | Not recorded | 45.02 | 16.61 | 2.66 | Pass |
| [qwen38-fit-mtp1](qwen38-fit-mtp1.md)<br>wave-a796b957fe2375c73755 | layout unspecified; mtp / 1 | 1 | 131,132 | 141 | cold; reused 0 | 262,144 / 917,504 | Not recorded | 29.72 | 1.18 | 114.87 | Failed / partial |
| [qwen38-fit-mtp1](qwen38-fit-mtp1.md)<br>wave-c15a167d87ae28fd66db | layout unspecified; mtp / 1 | 2 | 261,845 | 35 | cached_prefix; reused 261,632 | 262,144 / 917,504 | Not recorded | 30.26 | 10.13 | 4.69 | Pass |
| [qwen38-fit-mtp1](qwen38-fit-mtp1.md)<br>wave-c42f0df89352ea78c062 | layout unspecified; mtp / 1 | 2 | 261,699 | 128 | cold; reused 131,072 | 262,144 / 917,504 | Not recorded | 11.28 | 0.56 | 439.17 | Pass |
| [qwen38-fit-mtp1](qwen38-fit-mtp1.md)<br>wave-c9662449c16ed20c9426 | layout unspecified; mtp / 1 | 2 | 131,277 | 35 | cached_prefix; reused 131,072 | 262,144 / 917,504 | Not recorded | 46.07 | 16.51 | 2.72 | Pass |
| [qwen38-fit-mtp1](qwen38-fit-mtp1.md)<br>wave-cd26a4442fcdff7cf0c8 | layout unspecified; mtp / 1 | 4 | 261,698 | 128 | cold; reused 131,072 | 262,144 / 917,504 | Not recorded | 1.86 | 0.57 | 657.97 | Pass |
| [qwen38-fit-mtp1](qwen38-fit-mtp1.md)<br>wave-cf7c3974ad0593d5aea1 | layout unspecified; mtp / 1 | 2 | 32,824 | 128 | cold; reused 0 | 262,144 / 917,504 | Not recorded | 68.29 | 6.16 | 37.81 | Pass |
| [qwen38-fit-mtp1](qwen38-fit-mtp1.md)<br>wave-d703b17b6f4e68088151 | layout unspecified; mtp / 1 | 2 | 32,971 | 35 | cached_prefix; reused 32,768 | 262,144 / 917,504 | Not recorded | 73.40 | 32.21 | 1.22 | Pass |
| [qwen38-fit-mtp1](qwen38-fit-mtp1.md)<br>wave-dc851ffd2f3b231bd767 | layout unspecified; mtp / 1 | 4 | 131,277 | 35 | cached_prefix; reused 131,072 | 262,144 / 917,504 | Not recorded | 22.29 | 18.07 | 5.63 | Pass |
| [qwen38-fit-mtp1](qwen38-fit-mtp1.md)<br>wave-f0d73c9773ea85cf39a5 | layout unspecified; mtp / 1 | 2 | 131,131 | 128 | cold; reused 0 | 262,144 / 917,504 | Not recorded | 27.53 | 1.08 | 229.47 | Pass |
| [qwen38-fit-mtp1](qwen38-fit-mtp1.md)<br>wave-fbb3f69873ecf02e28ce | layout unspecified; mtp / 1 | 4 | 261,845 | 35 | cached_prefix; reused 261,632 | 262,144 / 917,504 | Not recorded | 3.97 | 2.79 | 31.07 | Pass |
| [qwen38-fit-mtp1](qwen38-fit-mtp1.md)<br>wave-fce4ea0a053c6bf8c908 | layout unspecified; mtp / 1 | 4 | 32,824 | 128 | cold; reused 0 | 262,144 / 917,504 | Not recorded | 90.94 | 6.26 | 76.94 | Pass |
| [qwen38-fit-mtp1](qwen38-fit-mtp1.md)<br>wave-ff1030129276a6c6a4a4 | layout unspecified; mtp / 1 | 16 | 8,204 to 8,205 | 128 | cold; reused 0 | 262,144 / 917,504 | Not recorded | 45.48 | 25.76 | 71.04 | Pass |

Rates are whole-wave totals over the stated request count. A wave may span multiple independent model instances; [measurements.json](../measurements.json) retains their contributions and the exact configuration IDs. Do not interpret a multi-instance total as one card's rate.

A dash in shared decode means no qualified synchronized interval is available. Whole-wave throughput includes prefill and queueing. A valid decode interval can survive inside an overall failed or partial check; the source-report outcome is preserved. No rows are averaged.

## Bounded Checks

| Check | Reported outcome | Retained counts / flags |
| --- | --- | --- |
| check-056b6ddd0cce316d60be | Pass | {"passed":true,"input_tokens":[261694,261694],"replayed_history_tokens":[66,66],"extension_cached_tokens":[131072,131072]} |
| check-066825c35c885753a404 | Failed / partial | {"passed":false,"input_tokens":[261694,261694]} |
| check-0692b9ed02ea9d0d0250 | Failed / partial | {"passed":false,"compact_tokens":209715,"context_tokens":262144} |
| check-0b4fc5861f3fc4d19e6d | Pass | {"passed":true,"recurrent_restores":24,"restored_pages":3600} |
| check-23d4f95d39142514551f | Pass | {"passed":true,"recurrent_restores":20,"restored_pages":0} |
| check-44f64af6238b47d2e7f6 | Pass | {"passed":true,"input_tokens":[261695,261695],"replayed_history_tokens":[67,67],"extension_cached_tokens":[131072,131072]} |
| check-4ee67992265f30d89cc5 | Pass | {"passed":true,"input_tokens":[131126,131126],"replayed_history_tokens":[58,58],"extension_cached_tokens":[32768,32768]} |
| check-4fa04fa82c3b1fba318b | Pass | {"passed":true,"replayed_history_tokens":[58,58],"input_tokens":[131126,131126]} |
| check-583c97223f37a2efe5a0 | Pass | {"passed":true,"compact_tokens":209715,"context_tokens":262144} |
| check-5938fae71c05247451eb | Pass | {"passed":true} |
| check-5dd1896e439fc33b132d | Failed / partial | {"passed":false,"input_tokens":[131128]} |
| check-5f1f6bc76e36b4128dd5 | Pass | {"passed":true,"replayed_history_tokens":[56,56,56,56]} |
| check-659a94010dbb23502c06 | Pass | {"passed":true,"input_tokens":[8200,8200,8200,8200,8200,8200,8200,8200,8200,8200,8201,8201,8201,8201,8201,8201]} |
| check-66007d4fa5a4e9cb0484 | Pass | {"passed":true,"replayed_history_tokens":[66,66,66,66]} |
| check-6b6418f695bc200b6aa4 | Pass | {"passed":true,"replayed_history_tokens":[58,58]} |
| check-7a101299897bb6a59afc | Pass | {"passed":true,"replayed_history_tokens":[58,58,58,58]} |
| check-7debf9c83dd9bf207252 | Pass | {"passed":true,"input_tokens":[261694,261694,261694,261694],"replayed_history_tokens":[66,66,66,66],"extension_cached_tokens":[131072,131072,131072,131072]} |
| check-85fa778171011fa2b58c | Failed / partial | {"passed":false,"input_tokens":[131128]} |
| check-881d72d99ab02d57a78b | Pass | {"passed":true,"recurrent_restores":20,"restored_pages":0} |
| check-8f3ba5602bd215291290 | Pass | {"passed":true,"replayed_history_tokens":[56,56]} |
| check-93b15dc82dfd59bb1ebd | Failed / partial | {"passed":false,"compact_tokens":209715,"context_tokens":262144} |
| check-b08d1a050b9713c9cd7e | Pass | {"passed":true,"replayed_history_tokens":[56,56,56,56],"input_tokens":[32820,32820,32820,32820]} |
| check-b1df32b7cb6eeae12a79 | Pass | {"passed":true,"replayed_history_tokens":[66,66]} |
| check-b7b43de5496a88d8d509 | Pass | {"passed":true,"input_tokens":[131126,131126,131126,131126],"replayed_history_tokens":[58,58,58,58],"extension_cached_tokens":[32768,32768,32768,32768]} |
| check-b9ce3893ff7839b201a6 | Pass | {"passed":true,"replayed_history_tokens":[56,56],"input_tokens":[32820,32820]} |
| check-c152f04b6ed0001d5e92 | Pass | {"passed":true,"replayed_history_tokens":[58,58]} |
| check-c58758c2dcb404d157c3 | Pass | {"passed":true,"compact_tokens":209715,"context_tokens":262144} |
| check-d2fad3ab47d93fb4e208 | Pass | {"passed":true,"replayed_history_tokens":[67,67]} |
| check-e44170a22e441075ee2c | Pass | {"passed":true,"replayed_history_tokens":[59,59],"input_tokens":[131127,131127]} |
| check-e77ee0c6becc8137c176 | Pass | {"passed":true} |
| check-f45f2302f19977fa6453 | Pass | {"passed":true,"replayed_history_tokens":[59,59]} |

These checks retain their reported scope. A context/allocation/retrieval check is not a general quality score or a speed qualification at that context. Exact flags and provenance are in [checks.json](../checks.json).

## Additional Test Results

| Result / Source | Profile | Evidence type | Reported outcome | Retained values | Configuration binding |
| --- | --- | --- | --- | --- | --- |
| [result-052c3c6803fe24f75dae](../observations.json)<br>source-c2d567b03ac1b5f9ad0027ff.json<br>`/r10_thermals/1` | [qwen38-fit-mtp1](qwen38-fit-mtp1.md) | test outcome | Outcome unspecified | ram_peak_bytes=26,843,545,600 bytes | Recorded configuration/job |
| [result-0b15be06588cf0da254b](../observations.json)<br>source-a0d4ed04397f117c22969e0a.json<br>`/stages/0` | [qwen38-fit-mtp1](qwen38-fit-mtp1.md) | test outcome | Pass | replayed_history_tokens=59 tokens | Recorded configuration/job |
| [result-0b1cacd41f256e3755ab](../observations.json)<br>source-84a296f9a57b3e4e910a7a5f.json<br>`/` | [qwen38-fit-mtp1](qwen38-fit-mtp1.md) | context allocation | Failed / partial | compact_tokens=209,715 tokens; context_tokens=262,144 tokens | Recorded configuration/job |
| [result-0b9c4b2bfc274bb181c4](../observations.json)<br>source-c044dbe81365670cb4dec469.json<br>`/warm/replicas/0/rates` | [qwen38-fit-mtp1](qwen38-fit-mtp1.md) | test outcome | Outcome unspecified | end_to_end_output_tps=166.94 accepted tokens/s; generated_tokens=4,096 accepted tokens; wall_seconds=24.54 s | Recorded configuration/job |
| [result-0c669f3efe241cf1ce5f](../observations.json)<br>source-a0d4ed04397f117c22969e0a.json<br>`/stages/0/warm` | [qwen38-fit-mtp1](qwen38-fit-mtp1.md) | test outcome | Outcome unspecified | end_to_end_output_tps=16.39 accepted tokens/s; generated_tokens=70 accepted tokens; wall_seconds=4.27 s | Recorded configuration/job |
| [result-0d06ab9225ad7f9ab618](../observations.json)<br>source-02b38a04ec7bf58a6981ad37.json<br>`/stages/0/warm` | [qwen38-fit-mtp1](qwen38-fit-mtp1.md) | test outcome | Outcome unspecified | end_to_end_output_tps=32.21 accepted tokens/s; generated_tokens=70 accepted tokens; wall_seconds=2.17 s | Recorded configuration/job |
| [result-0f70f41f3bdb264cce0f](../observations.json)<br>source-58fbe0bf235179a3a1d7f89b.json<br>`/after_cold/totals` | [qwen38-fit-mtp1](qwen38-fit-mtp1.md) | context allocation | Outcome unspecified | cached_tokens=49,152 tokens; generated_tokens=7,012 accepted tokens; prompt_tokens=325,590 tokens; recurrent_restores=10 checkpoints | Recorded configuration/job |
| [result-1000f2114bb58d2a3bca](../observations.json)<br>source-0d78325eacad115901d82a8a.json<br>`/after_cold/totals` | [qwen38-fit-mtp1](qwen38-fit-mtp1.md) | context allocation | Outcome unspecified | cached_tokens=131,072 tokens; generated_tokens=1,094 accepted tokens; prompt_tokens=525,658 tokens; recurrent_restores=4 checkpoints | Recorded configuration/job |
| [result-137d8ec9bb4b12eb56df](../observations.json)<br>source-a19bebb57334019f8c6e26a6.json<br>`/stages/1/warm` | [qwen38-fit-mtp1](qwen38-fit-mtp1.md) | test outcome | Outcome unspecified | end_to_end_output_tps=18.07 accepted tokens/s; generated_tokens=140 accepted tokens; wall_seconds=7.75 s | Recorded configuration/job |
| [result-13d0983ecfa92ace588d](../observations.json)<br>source-a19bebb57334019f8c6e26a6.json<br>`/stages/2/warm` | [qwen38-fit-mtp1](qwen38-fit-mtp1.md) | test outcome | Outcome unspecified | end_to_end_output_tps=2.79 accepted tokens/s; generated_tokens=140 accepted tokens; wall_seconds=50.09 s | Recorded configuration/job |
| [result-1574058c25be160f4cd3](../observations.json)<br>source-84a296f9a57b3e4e910a7a5f.json<br>`/verification` | [qwen38-fit-mtp1](qwen38-fit-mtp1.md) | test outcome | Outcome unspecified | elapsed_seconds=0.06 s | Recorded configuration/job |
| [result-1832658674e0d674ca4e](../observations.json)<br>source-a0d4ed04397f117c22969e0a.json<br>`/stages/1` | [qwen38-fit-mtp1](qwen38-fit-mtp1.md) | test outcome | Pass | replayed_history_tokens=67 tokens | Recorded configuration/job |
| [result-1853cd4a7b558c390806](../observations.json)<br>source-4f7f033fcde00f98df0540dc.json<br>`/` | [qwen38-fit-mtp1](qwen38-fit-mtp1.md) | context allocation | Pass | recurrent_restores=20 checkpoints; restored_pages=0 pages | Recorded configuration/job |
| [result-185ed4bb608c7bc50516](../observations.json)<br>source-84a296f9a57b3e4e910a7a5f.json<br>`/client_result` | [qwen38-fit-mtp1](qwen38-fit-mtp1.md) | test outcome | Outcome unspecified | elapsed_seconds=92.46 s | Recorded configuration/job |
| [result-1c59bc8fc403c3441f22](../observations.json)<br>source-ed8b56691539ff8c26d5f503.json<br>`/after_cold` | [qwen38-fit-mtp1](qwen38-fit-mtp1.md) | test outcome | Outcome unspecified | context=262,144 tokens | Recorded configuration/job |
| [result-1d21f36f5c494bc03139](../observations.json)<br>source-84a296f9a57b3e4e910a7a5f.json<br>`/` | [qwen38-fit-mtp1](qwen38-fit-mtp1.md) | context allocation | Failed / partial | compact_tokens=209,715 tokens; context_tokens=262,144 tokens | Recorded configuration/job |
| [result-20755312e242206b118c](../observations.json)<br>source-58fbe0bf235179a3a1d7f89b.json<br>`/after_cold` | [qwen38-fit-mtp1](qwen38-fit-mtp1.md) | test outcome | Outcome unspecified | context=262,144 tokens | Recorded configuration/job |
| [result-2100d879b9f2333d09e0](../observations.json)<br>source-0d78325eacad115901d82a8a.json<br>`/after_burst` | [qwen38-fit-mtp1](qwen38-fit-mtp1.md) | test outcome | Outcome unspecified | context=262,144 tokens | Recorded configuration/job |
| [result-2574da3fc415beac900c](../observations.json)<br>source-0d78325eacad115901d82a8a.json<br>`/after_cold` | [qwen38-fit-mtp1](qwen38-fit-mtp1.md) | test outcome | Outcome unspecified | context=262,144 tokens | Recorded configuration/job |
| [result-2a0fc7a67bce4bfe59db](../observations.json)<br>source-a0d4ed04397f117c22969e0a.json<br>`/stages/1/warm` | [qwen38-fit-mtp1](qwen38-fit-mtp1.md) | test outcome | Outcome unspecified | end_to_end_output_tps=9.81 accepted tokens/s; generated_tokens=70 accepted tokens; wall_seconds=7.14 s | Recorded configuration/job |
| [result-2b3cbf5ca2cc30ec1aba](../observations.json)<br>source-c044dbe81365670cb4dec469.json<br>`/warm/replicas/2/rates` | [qwen38-fit-mtp1](qwen38-fit-mtp1.md) | test outcome | Outcome unspecified | end_to_end_output_tps=153.85 accepted tokens/s; generated_tokens=4,096 accepted tokens; wall_seconds=26.62 s | Recorded configuration/job |
| [result-2dacc642724b5df4cc15](../observations.json)<br>source-1eaf2704c29b670eeb8833ab.json<br>`/after_burst/totals` | [qwen38-fit-mtp1](qwen38-fit-mtp1.md) | context allocation | Outcome unspecified | cached_tokens=1,556,480 tokens; generated_tokens=3,352 accepted tokens; prompt_tokens=2,755,024 tokens; recurrent_restores=46 checkpoints | Recorded configuration/job |
| [result-2f291b15d222cff1728d](../observations.json)<br>source-a19bebb57334019f8c6e26a6.json<br>`/stages/1/cold` | [qwen38-fit-mtp1](qwen38-fit-mtp1.md) | test outcome | Outcome unspecified | end_to_end_output_tps=1.28 accepted tokens/s; generated_tokens=512 accepted tokens; wall_seconds=399.96 s | Recorded configuration/job |
| [result-301487a1b5ce87c27ca8](../observations.json)<br>source-8c03e975ff71fd71b4b9a63d.json<br>`/after_burst/totals` | [qwen38-fit-mtp1](qwen38-fit-mtp1.md) | context allocation | Outcome unspecified | cached_tokens=376,832 tokens; generated_tokens=2,188 accepted tokens; prompt_tokens=1,051,316 tokens; recurrent_restores=22 checkpoints | Recorded configuration/job |
| [result-31ae7093825760d39471](../observations.json)<br>source-cf0b37ec6cb49dfe73cb3ea0.json<br>`/after_cold/cache` | [qwen38-fit-mtp1](qwen38-fit-mtp1.md) | test outcome | Outcome unspecified | cached_tokens=454,656 tokens | Recorded configuration/job |
| [result-329f7b4f4a593cac4506](../observations.json)<br>source-e07c9918719df2d66e2e630a.json<br>`/after_cold` | [qwen38-fit-mtp1](qwen38-fit-mtp1.md) | test outcome | Outcome unspecified | context=262,144 tokens | Recorded configuration/job |
| [result-32c9ac7735adada8f135](../observations.json)<br>source-a19bebb57334019f8c6e26a6.json<br>`/stages/0` | [qwen38-fit-mtp1](qwen38-fit-mtp1.md) | test outcome | Pass | replayed_history_tokens=56 tokens | Recorded configuration/job |
| [result-34e73cc75d7bcc314ce9](../observations.json)<br>source-0d78325eacad115901d82a8a.json<br>`/after_burst/cache` | [qwen38-fit-mtp1](qwen38-fit-mtp1.md) | test outcome | Outcome unspecified | cached_tokens=393,216 tokens | Recorded configuration/job |
| [result-3a8f02a3d214d8cf657b](../observations.json)<br>source-8545401134d4c08e1c32286f.json<br>`/after_cold/cache` | [qwen38-fit-mtp1](qwen38-fit-mtp1.md) | test outcome | Outcome unspecified | cached_tokens=131,072 tokens | Recorded configuration/job |
| [result-3bf62434ccf96ca9a91f](../observations.json)<br>source-0a902e6b90235a08b4217ce4.json<br>`/after_burst/totals` | [qwen38-fit-mtp1](qwen38-fit-mtp1.md) | context allocation | Outcome unspecified | cached_tokens=0 tokens; generated_tokens=1,024 accepted tokens; prompt_tokens=263,104 tokens; recurrent_restores=0 checkpoints | Recorded configuration/job |
| [result-3cad9cfea8e93c9a8c21](../observations.json)<br>source-84a296f9a57b3e4e910a7a5f.json<br>`/` | [qwen38-fit-mtp1](qwen38-fit-mtp1.md) | context allocation | Pass | compact_tokens=209,715 tokens; context_tokens=262,144 tokens | Recorded configuration/job |
| [result-3f32241a2e0a79b59d66](../observations.json)<br>source-a820e2bfabbcec2bcea88429.json<br>`/after_burst/totals` | [qwen38-fit-mtp1](qwen38-fit-mtp1.md) | context allocation | Outcome unspecified | cached_tokens=704,512 tokens; generated_tokens=8,362 accepted tokens; prompt_tokens=1,375,156 tokens; recurrent_restores=30 checkpoints | Recorded configuration/job |
| [result-483db5bb80299f431637](../observations.json)<br>source-ed8b56691539ff8c26d5f503.json<br>`/after_cold/cache` | [qwen38-fit-mtp1](qwen38-fit-mtp1.md) | test outcome | Outcome unspecified | cached_tokens=131,072 tokens | Recorded configuration/job |
| [result-4b980ad4ef322fe15da1](../observations.json)<br>source-68979d04b005731921d4a781.json<br>`/after_cold/totals` | [qwen38-fit-mtp1](qwen38-fit-mtp1.md) | context allocation | Outcome unspecified | cached_tokens=0 tokens; generated_tokens=2,048 accepted tokens; prompt_tokens=131,270 tokens; recurrent_restores=0 checkpoints | Recorded configuration/job |
| [result-4bd814872a207761e9b2](../observations.json)<br>source-58fbe0bf235179a3a1d7f89b.json<br>`/after_burst/totals` | [qwen38-fit-mtp1](qwen38-fit-mtp1.md) | context allocation | Outcome unspecified | cached_tokens=49,152 tokens; generated_tokens=7,524 accepted tokens; prompt_tokens=457,398 tokens; recurrent_restores=10 checkpoints | Recorded configuration/job |
| [result-4bdb6d7abe38bdeab4e3](../observations.json)<br>source-1eaf2704c29b670eeb8833ab.json<br>`/after_cold/cache` | [qwen38-fit-mtp1](qwen38-fit-mtp1.md) | test outcome | Outcome unspecified | cached_tokens=914,688 tokens | Recorded configuration/job |
| [result-4db46c02e04b27eab070](../observations.json)<br>source-0a902e6b90235a08b4217ce4.json<br>`/after_burst/cache` | [qwen38-fit-mtp1](qwen38-fit-mtp1.md) | test outcome | Outcome unspecified | cached_tokens=262,144 tokens | Recorded configuration/job |
| [result-51c8613ccf7e8694bd96](../observations.json)<br>source-8c03e975ff71fd71b4b9a63d.json<br>`/after_burst` | [qwen38-fit-mtp1](qwen38-fit-mtp1.md) | test outcome | Outcome unspecified | context=262,144 tokens | Recorded configuration/job |
| [result-52be5077db01fa99c5ae](../observations.json)<br>source-1eaf2704c29b670eeb8833ab.json<br>`/after_burst` | [qwen38-fit-mtp1](qwen38-fit-mtp1.md) | test outcome | Outcome unspecified | context=262,144 tokens | Recorded configuration/job |
| [result-535db872512151040f71](../observations.json)<br>source-e07c9918719df2d66e2e630a.json<br>`/after_burst` | [qwen38-fit-mtp1](qwen38-fit-mtp1.md) | test outcome | Outcome unspecified | context=262,144 tokens | Recorded configuration/job |
| [result-54a6e75192c921443f50](../observations.json)<br>source-8c03e975ff71fd71b4b9a63d.json<br>`/after_cold/totals` | [qwen38-fit-mtp1](qwen38-fit-mtp1.md) | context allocation | Outcome unspecified | cached_tokens=262,144 tokens; generated_tokens=1,676 accepted tokens; prompt_tokens=919,508 tokens; recurrent_restores=8 checkpoints | Recorded configuration/job |
| [result-558acb2c44ab8b2a9e5b](../observations.json)<br>source-978df53f2efdf795516db8dc.json<br>`/after_cold/totals` | [qwen38-fit-mtp1](qwen38-fit-mtp1.md) | context allocation | Outcome unspecified | cached_tokens=0 tokens; generated_tokens=256 accepted tokens; prompt_tokens=65,648 tokens; recurrent_restores=0 checkpoints | Recorded configuration/job |
| [result-57a25f31cc57fe3b6517](../observations.json)<br>source-a820e2bfabbcec2bcea88429.json<br>`/after_burst` | [qwen38-fit-mtp1](qwen38-fit-mtp1.md) | test outcome | Outcome unspecified | context=262,144 tokens | Recorded configuration/job |
| [result-58be2087a8714c77ffe4](../observations.json)<br>source-84a296f9a57b3e4e910a7a5f.json<br>`/` | [qwen38-fit-mtp1](qwen38-fit-mtp1.md) | context allocation | Pass | compact_tokens=209,715 tokens; context_tokens=262,144 tokens | Recorded configuration/job |
| [result-5aaafaa00eb71a5fb88a](../observations.json)<br>source-84a296f9a57b3e4e910a7a5f.json<br>`/verification` | [qwen38-fit-mtp1](qwen38-fit-mtp1.md) | test outcome | Outcome unspecified | elapsed_seconds=0.03 s | Recorded configuration/job |
| [result-5ad89c40cf6cb7afd637](../observations.json)<br>source-a19bebb57334019f8c6e26a6.json<br>`/stages/2` | [qwen38-fit-mtp1](qwen38-fit-mtp1.md) | test outcome | Pass | replayed_history_tokens=66 tokens | Recorded configuration/job |
| [result-5e6936a94038073f1a67](../observations.json)<br>source-8c03e975ff71fd71b4b9a63d.json<br>`/after_cold` | [qwen38-fit-mtp1](qwen38-fit-mtp1.md) | test outcome | Outcome unspecified | context=262,144 tokens | Recorded configuration/job |
| [result-61e9ac2289ebf4a40eac](../observations.json)<br>source-1eaf2704c29b670eeb8833ab.json<br>`/after_cold` | [qwen38-fit-mtp1](qwen38-fit-mtp1.md) | test outcome | Outcome unspecified | context=262,144 tokens | Recorded configuration/job |
| [result-6238b143bc0bafd49522](../observations.json)<br>source-cf0b37ec6cb49dfe73cb3ea0.json<br>`/after_cold/totals` | [qwen38-fit-mtp1](qwen38-fit-mtp1.md) | context allocation | Outcome unspecified | cached_tokens=180,224 tokens; generated_tokens=12,544 accepted tokens; prompt_tokens=630,542 tokens; recurrent_restores=32 checkpoints | Recorded configuration/job |
| [result-67eeb886a5caab62e5a7](../observations.json)<br>source-c044dbe81365670cb4dec469.json<br>`/cold/replicas/1/rates` | [qwen38-fit-mtp1](qwen38-fit-mtp1.md) | test outcome | Outcome unspecified | end_to_end_output_tps=92.65 accepted tokens/s; generated_tokens=4,096 accepted tokens; wall_seconds=44.21 s | Recorded configuration/job |
| [result-6855260df920ae464b22](../observations.json)<br>source-84a296f9a57b3e4e910a7a5f.json<br>`/verification` | [qwen38-fit-mtp1](qwen38-fit-mtp1.md) | test outcome | Outcome unspecified | elapsed_seconds=0.06 s | Recorded configuration/job |
| [result-6e326ff1304229287681](../observations.json)<br>source-a820e2bfabbcec2bcea88429.json<br>`/after_cold` | [qwen38-fit-mtp1](qwen38-fit-mtp1.md) | test outcome | Outcome unspecified | context=262,144 tokens | Recorded configuration/job |
| [result-70c959ee3f98898fa8e2](../observations.json)<br>source-1eaf2704c29b670eeb8833ab.json<br>`/after_cold/totals` | [qwen38-fit-mtp1](qwen38-fit-mtp1.md) | context allocation | Outcome unspecified | cached_tokens=1,425,408 tokens; generated_tokens=2,840 accepted tokens; prompt_tokens=2,623,216 tokens; recurrent_restores=30 checkpoints | Recorded configuration/job |
| [result-71f0e07b2f88389d10aa](../observations.json)<br>source-8545401134d4c08e1c32286f.json<br>`/after_cold` | [qwen38-fit-mtp1](qwen38-fit-mtp1.md) | test outcome | Outcome unspecified | context=262,144 tokens | Recorded configuration/job |
| [result-731a98141fc239b130e7](../observations.json)<br>source-e07c9918719df2d66e2e630a.json<br>`/after_cold/cache` | [qwen38-fit-mtp1](qwen38-fit-mtp1.md) | test outcome | Outcome unspecified | cached_tokens=846,848 tokens | Recorded configuration/job |
| [result-734fdebc129fd0a76b1c](../observations.json)<br>source-c2d567b03ac1b5f9ad0027ff.json<br>`/r10_thermals/2` | [qwen38-fit-mtp1](qwen38-fit-mtp1.md) | test outcome | Outcome unspecified | ram_peak_bytes=20,368,670,720 bytes | Recorded configuration/job |
| [result-771a59bdd008486f3911](../observations.json)<br>source-4f7f033fcde00f98df0540dc.json<br>`/stages/0` | [qwen38-fit-mtp1](qwen38-fit-mtp1.md) | test outcome | Pass | replayed_history_tokens=58 tokens | Recorded configuration/job |
| [result-7d98eb33d359f6a6bbf3](../observations.json)<br>source-02b38a04ec7bf58a6981ad37.json<br>`/stages/1/warm` | [qwen38-fit-mtp1](qwen38-fit-mtp1.md) | test outcome | Outcome unspecified | end_to_end_output_tps=16.61 accepted tokens/s; generated_tokens=70 accepted tokens; wall_seconds=4.21 s | Recorded configuration/job |
| [result-819ee7ded90f55f99928](../observations.json)<br>source-a19bebb57334019f8c6e26a6.json<br>`/stages/0/warm` | [qwen38-fit-mtp1](qwen38-fit-mtp1.md) | test outcome | Outcome unspecified | end_to_end_output_tps=38.75 accepted tokens/s; generated_tokens=140 accepted tokens; wall_seconds=3.61 s | Recorded configuration/job |
| [result-828ac877d2761b934d4a](../observations.json)<br>source-ed8b56691539ff8c26d5f503.json<br>`/after_cold/totals` | [qwen38-fit-mtp1](qwen38-fit-mtp1.md) | context allocation | Outcome unspecified | cached_tokens=0 tokens; generated_tokens=141 accepted tokens; prompt_tokens=131,132 tokens; recurrent_restores=0 checkpoints | Recorded configuration/job |
| [result-85cdb9391f44da1a8492](../observations.json)<br>source-a19bebb57334019f8c6e26a6.json<br>`/stages/2/cold` | [qwen38-fit-mtp1](qwen38-fit-mtp1.md) | test outcome | Outcome unspecified | end_to_end_output_tps=0.57 accepted tokens/s; generated_tokens=512 accepted tokens; wall_seconds=902.93 s | Recorded configuration/job |
| [result-87aaea6a9d23da0b5c05](../observations.json)<br>source-68979d04b005731921d4a781.json<br>`/after_cold` | [qwen38-fit-mtp1](qwen38-fit-mtp1.md) | test outcome | Outcome unspecified | context=262,144 tokens | Recorded configuration/job |
| [result-87eae9b494fea0bb6353](../observations.json)<br>source-394f9547653a1180254c15d3.json<br>`/stages/0/cold` | [qwen38-fit-mtp1](qwen38-fit-mtp1.md) | test outcome | Outcome unspecified | end_to_end_output_tps=1.18 accepted tokens/s; generated_tokens=141 accepted tokens; wall_seconds=119.62 s | Recorded configuration/job |
| [result-8935727860f59e3145c5](../observations.json)<br>source-cf0b37ec6cb49dfe73cb3ea0.json<br>`/after_burst` | [qwen38-fit-mtp1](qwen38-fit-mtp1.md) | test outcome | Outcome unspecified | context=262,144 tokens | Recorded configuration/job |
| [result-896d14ce4800b9f77e48](../observations.json)<br>source-8545401134d4c08e1c32286f.json<br>`/after_cold/totals` | [qwen38-fit-mtp1](qwen38-fit-mtp1.md) | context allocation | Outcome unspecified | cached_tokens=0 tokens; generated_tokens=141 accepted tokens; prompt_tokens=131,132 tokens; recurrent_restores=0 checkpoints | Recorded configuration/job |
| [result-8da07d6e42575b8cb14f](../observations.json)<br>source-a0d4ed04397f117c22969e0a.json<br>`/stages/0/cold` | [qwen38-fit-mtp1](qwen38-fit-mtp1.md) | test outcome | Outcome unspecified | end_to_end_output_tps=1.08 accepted tokens/s; generated_tokens=256 accepted tokens; wall_seconds=237.13 s | Recorded configuration/job |
| [result-8ece5303a786ecee758c](../observations.json)<br>source-58fbe0bf235179a3a1d7f89b.json<br>`/after_burst` | [qwen38-fit-mtp1](qwen38-fit-mtp1.md) | test outcome | Outcome unspecified | context=262,144 tokens | Recorded configuration/job |
| [result-904f0df8c546037ae51a](../observations.json)<br>source-978df53f2efdf795516db8dc.json<br>`/after_burst/totals` | [qwen38-fit-mtp1](qwen38-fit-mtp1.md) | context allocation | Outcome unspecified | cached_tokens=0 tokens; generated_tokens=768 accepted tokens; prompt_tokens=197,456 tokens; recurrent_restores=0 checkpoints | Recorded configuration/job |
| [result-912d1a59021961feb55d](../observations.json)<br>source-58fbe0bf235179a3a1d7f89b.json<br>`/after_cold/cache` | [qwen38-fit-mtp1](qwen38-fit-mtp1.md) | test outcome | Outcome unspecified | cached_tokens=278,272 tokens | Recorded configuration/job |
| [result-9317437f86e7ec1ec560](../observations.json)<br>source-4f7f033fcde00f98df0540dc.json<br>`/stages/0/cold` | [qwen38-fit-mtp1](qwen38-fit-mtp1.md) | test outcome | Outcome unspecified | end_to_end_output_tps=1.11 accepted tokens/s; generated_tokens=256 accepted tokens; wall_seconds=231.17 s | Recorded configuration/job |
| [result-9749ad496d56afcd1dd3](../observations.json)<br>source-84a296f9a57b3e4e910a7a5f.json<br>`/client_result` | [qwen38-fit-mtp1](qwen38-fit-mtp1.md) | test outcome | Outcome unspecified | elapsed_seconds=0.77 s | Recorded configuration/job |
| [result-99c590b3bba1782c706f](../observations.json)<br>source-e07c9918719df2d66e2e630a.json<br>`/after_burst/cache` | [qwen38-fit-mtp1](qwen38-fit-mtp1.md) | test outcome | Outcome unspecified | cached_tokens=846,848 tokens | Recorded configuration/job |
| [result-9d72b9504edce7f19d14](../observations.json)<br>source-4f7f033fcde00f98df0540dc.json<br>`/stages/1/cold` | [qwen38-fit-mtp1](qwen38-fit-mtp1.md) | test outcome | Outcome unspecified | end_to_end_output_tps=0.58 accepted tokens/s; generated_tokens=256 accepted tokens; wall_seconds=442.87 s | Recorded configuration/job |
| [result-a0db00380289c04512f3](../observations.json)<br>source-a820e2bfabbcec2bcea88429.json<br>`/after_burst/cache` | [qwen38-fit-mtp1](qwen38-fit-mtp1.md) | test outcome | Outcome unspecified | cached_tokens=670,464 tokens | Recorded configuration/job |
| [result-a128145eea32cba7b289](../observations.json)<br>source-02b38a04ec7bf58a6981ad37.json<br>`/stages/1` | [qwen38-fit-mtp1](qwen38-fit-mtp1.md) | test outcome | Pass | replayed_history_tokens=58 tokens | Recorded configuration/job |
| [result-a2f9377a27ca0398a9f4](../observations.json)<br>source-8c03e975ff71fd71b4b9a63d.json<br>`/after_cold/cache` | [qwen38-fit-mtp1](qwen38-fit-mtp1.md) | test outcome | Outcome unspecified | cached_tokens=655,360 tokens | Recorded configuration/job |
| [result-a7ae6e1c6465ef226dcb](../observations.json)<br>source-1eaf2704c29b670eeb8833ab.json<br>`/after_burst/cache` | [qwen38-fit-mtp1](qwen38-fit-mtp1.md) | test outcome | Outcome unspecified | cached_tokens=911,872 tokens | Recorded configuration/job |
| [result-a9e339a37bce55be9b18](../observations.json)<br>source-0a902e6b90235a08b4217ce4.json<br>`/after_cold` | [qwen38-fit-mtp1](qwen38-fit-mtp1.md) | test outcome | Outcome unspecified | context=262,144 tokens | Recorded configuration/job |
| [result-aa47076d43ce74a8fed1](../observations.json)<br>source-0d78325eacad115901d82a8a.json<br>`/after_cold/cache` | [qwen38-fit-mtp1](qwen38-fit-mtp1.md) | test outcome | Outcome unspecified | cached_tokens=393,216 tokens | Recorded configuration/job |
| [result-abe6fc64c0bda660b258](../observations.json)<br>source-8c03e975ff71fd71b4b9a63d.json<br>`/after_burst/cache` | [qwen38-fit-mtp1](qwen38-fit-mtp1.md) | test outcome | Outcome unspecified | cached_tokens=655,360 tokens | Recorded configuration/job |
| [result-aef40f3bddc9abf58299](../observations.json)<br>source-cf0b37ec6cb49dfe73cb3ea0.json<br>`/after_burst/cache` | [qwen38-fit-mtp1](qwen38-fit-mtp1.md) | test outcome | Outcome unspecified | cached_tokens=585,728 tokens | Recorded configuration/job |
| [result-afcfebecc1702149fb22](../observations.json)<br>source-0a902e6b90235a08b4217ce4.json<br>`/after_cold/cache` | [qwen38-fit-mtp1](qwen38-fit-mtp1.md) | test outcome | Outcome unspecified | cached_tokens=131,072 tokens | Recorded configuration/job |
| [result-b1847fa9276dcbeb5f21](../observations.json)<br>source-0a902e6b90235a08b4217ce4.json<br>`/after_burst` | [qwen38-fit-mtp1](qwen38-fit-mtp1.md) | test outcome | Outcome unspecified | context=262,144 tokens | Recorded configuration/job |
| [result-b3103185329d28731048](../observations.json)<br>source-4f7f033fcde00f98df0540dc.json<br>`/stages/1` | [qwen38-fit-mtp1](qwen38-fit-mtp1.md) | test outcome | Pass | replayed_history_tokens=66 tokens | Recorded configuration/job |
| [result-b61efdf82214b0d9c35d](../observations.json)<br>source-58fbe0bf235179a3a1d7f89b.json<br>`/after_burst/cache` | [qwen38-fit-mtp1](qwen38-fit-mtp1.md) | test outcome | Outcome unspecified | cached_tokens=409,344 tokens | Recorded configuration/job |
| [result-ba304ff3b157b8f67a60](../observations.json)<br>source-978df53f2efdf795516db8dc.json<br>`/after_cold` | [qwen38-fit-mtp1](qwen38-fit-mtp1.md) | test outcome | Outcome unspecified | context=262,144 tokens | Recorded configuration/job |
| [result-bac2c121fe669d503431](../observations.json)<br>source-cf0b37ec6cb49dfe73cb3ea0.json<br>`/after_cold` | [qwen38-fit-mtp1](qwen38-fit-mtp1.md) | test outcome | Outcome unspecified | context=262,144 tokens | Recorded configuration/job |
| [result-c0dece70232839796c94](../observations.json)<br>source-a19bebb57334019f8c6e26a6.json<br>`/` | [qwen38-fit-mtp1](qwen38-fit-mtp1.md) | context allocation | Pass | recurrent_restores=24 checkpoints; restored_pages=3,600 pages | Recorded configuration/job |
| [result-c117275fbcf8793a38f1](../observations.json)<br>source-02b38a04ec7bf58a6981ad37.json<br>`/stages/0` | [qwen38-fit-mtp1](qwen38-fit-mtp1.md) | test outcome | Pass | replayed_history_tokens=56 tokens | Recorded configuration/job |
| [result-c4692efad05b0663e997](../observations.json)<br>source-84a296f9a57b3e4e910a7a5f.json<br>`/client_result` | [qwen38-fit-mtp1](qwen38-fit-mtp1.md) | test outcome | Outcome unspecified | elapsed_seconds=0.72 s | Recorded configuration/job |
| [result-c84b4578beb59d4922a1](../observations.json)<br>source-e07c9918719df2d66e2e630a.json<br>`/after_cold/totals` | [qwen38-fit-mtp1](qwen38-fit-mtp1.md) | context allocation | Outcome unspecified | cached_tokens=704,512 tokens; generated_tokens=13,382 accepted tokens; prompt_tokens=1,547,750 tokens; recurrent_restores=36 checkpoints | Recorded configuration/job |
| [result-c8a4b0b195fe3590236f](../observations.json)<br>source-a0d4ed04397f117c22969e0a.json<br>`/stages/1/cold` | [qwen38-fit-mtp1](qwen38-fit-mtp1.md) | test outcome | Outcome unspecified | end_to_end_output_tps=0.56 accepted tokens/s; generated_tokens=256 accepted tokens; wall_seconds=455.14 s | Recorded configuration/job |
| [result-cb69af278ae530960936](../observations.json)<br>source-978df53f2efdf795516db8dc.json<br>`/after_cold/cache` | [qwen38-fit-mtp1](qwen38-fit-mtp1.md) | test outcome | Outcome unspecified | cached_tokens=65,536 tokens | Recorded configuration/job |
| [result-cb770ce19ca8e542b13c](../observations.json)<br>source-c044dbe81365670cb4dec469.json<br>`/warm/replicas/1/rates` | [qwen38-fit-mtp1](qwen38-fit-mtp1.md) | test outcome | Outcome unspecified | end_to_end_output_tps=156.52 accepted tokens/s; generated_tokens=4,096 accepted tokens; wall_seconds=26.17 s | Recorded configuration/job |
| [result-cc48efeaf59e9d4fd2ff](../observations.json)<br>source-978df53f2efdf795516db8dc.json<br>`/after_burst/cache` | [qwen38-fit-mtp1](qwen38-fit-mtp1.md) | test outcome | Outcome unspecified | cached_tokens=196,608 tokens | Recorded configuration/job |
| [result-ccc02b01503b49a62ef9](../observations.json)<br>source-84a296f9a57b3e4e910a7a5f.json<br>`/client_result` | [qwen38-fit-mtp1](qwen38-fit-mtp1.md) | test outcome | Outcome unspecified | elapsed_seconds=77.05 s | Recorded configuration/job |
| [result-cd7084a06dbb803c11dd](../observations.json)<br>source-c2d567b03ac1b5f9ad0027ff.json<br>`/r10_thermals/0` | [qwen38-fit-mtp1](qwen38-fit-mtp1.md) | test outcome | Outcome unspecified | ram_peak_bytes=20,714,000,384 bytes | Recorded configuration/job |
| [result-ce061ae94239f67d7800](../observations.json)<br>source-e07c9918719df2d66e2e630a.json<br>`/after_burst/totals` | [qwen38-fit-mtp1](qwen38-fit-mtp1.md) | context allocation | Outcome unspecified | cached_tokens=835,584 tokens; generated_tokens=13,894 accepted tokens; prompt_tokens=1,679,004 tokens; recurrent_restores=52 checkpoints | Recorded configuration/job |
| [result-d0f0ba5cf6abdc7007de](../observations.json)<br>source-c044dbe81365670cb4dec469.json<br>`/cold/replicas/2/rates` | [qwen38-fit-mtp1](qwen38-fit-mtp1.md) | test outcome | Outcome unspecified | end_to_end_output_tps=90.30 accepted tokens/s; generated_tokens=4,096 accepted tokens; wall_seconds=45.36 s | Recorded configuration/job |
| [result-d220bb24ff00e7cddb61](../observations.json)<br>source-978df53f2efdf795516db8dc.json<br>`/after_burst` | [qwen38-fit-mtp1](qwen38-fit-mtp1.md) | test outcome | Outcome unspecified | context=262,144 tokens | Recorded configuration/job |
| [result-d535144e07175a293138](../observations.json)<br>source-a820e2bfabbcec2bcea88429.json<br>`/after_cold/totals` | [qwen38-fit-mtp1](qwen38-fit-mtp1.md) | context allocation | Outcome unspecified | cached_tokens=573,440 tokens; generated_tokens=7,850 accepted tokens; prompt_tokens=1,243,348 tokens; recurrent_restores=14 checkpoints | Recorded configuration/job |
| [result-d757a66b8c48a3b0b6ab](../observations.json)<br>source-68979d04b005731921d4a781.json<br>`/after_cold/cache` | [qwen38-fit-mtp1](qwen38-fit-mtp1.md) | test outcome | Outcome unspecified | cached_tokens=131,072 tokens | Recorded configuration/job |
| [result-de19f75c7324bb8d08df](../observations.json)<br>source-84a296f9a57b3e4e910a7a5f.json<br>`/verification` | [qwen38-fit-mtp1](qwen38-fit-mtp1.md) | test outcome | Outcome unspecified | elapsed_seconds=0.06 s | Recorded configuration/job |
| [result-df29e2b3d4a59d29ea45](../observations.json)<br>source-c044dbe81365670cb4dec469.json<br>`/cold/replicas/0/rates` | [qwen38-fit-mtp1](qwen38-fit-mtp1.md) | test outcome | Outcome unspecified | end_to_end_output_tps=96.13 accepted tokens/s; generated_tokens=4,096 accepted tokens; wall_seconds=42.61 s | Recorded configuration/job |
| [result-e0a89f2306999c81d01c](../observations.json)<br>source-a19bebb57334019f8c6e26a6.json<br>`/stages/0/cold` | [qwen38-fit-mtp1](qwen38-fit-mtp1.md) | test outcome | Outcome unspecified | end_to_end_output_tps=6.26 accepted tokens/s; generated_tokens=512 accepted tokens; wall_seconds=81.84 s | Recorded configuration/job |
| [result-e56a759b6f2a5f86ab02](../observations.json)<br>source-4f7f033fcde00f98df0540dc.json<br>`/stages/1/warm` | [qwen38-fit-mtp1](qwen38-fit-mtp1.md) | test outcome | Outcome unspecified | end_to_end_output_tps=10.13 accepted tokens/s; generated_tokens=70 accepted tokens; wall_seconds=6.91 s | Recorded configuration/job |
| [result-e6213a1871b93aed10ae](../observations.json)<br>source-a19bebb57334019f8c6e26a6.json<br>`/stages/1` | [qwen38-fit-mtp1](qwen38-fit-mtp1.md) | test outcome | Pass | replayed_history_tokens=58 tokens | Recorded configuration/job |
| [result-e8143ef8d50143bd255a](../observations.json)<br>source-cf0b37ec6cb49dfe73cb3ea0.json<br>`/after_burst/totals` | [qwen38-fit-mtp1](qwen38-fit-mtp1.md) | context allocation | Outcome unspecified | cached_tokens=180,224 tokens; generated_tokens=13,056 accepted tokens; prompt_tokens=761,796 tokens; recurrent_restores=32 checkpoints | Recorded configuration/job |
| [result-e8b69721b1c391dd51ee](../observations.json)<br>source-a0d4ed04397f117c22969e0a.json<br>`/` | [qwen38-fit-mtp1](qwen38-fit-mtp1.md) | context allocation | Pass | recurrent_restores=20 checkpoints; restored_pages=0 pages | Recorded configuration/job |
| [result-f0792aa1e9fce41ab00f](../observations.json)<br>source-0d78325eacad115901d82a8a.json<br>`/after_burst/totals` | [qwen38-fit-mtp1](qwen38-fit-mtp1.md) | context allocation | Outcome unspecified | cached_tokens=262,144 tokens; generated_tokens=1,606 accepted tokens; prompt_tokens=657,466 tokens; recurrent_restores=20 checkpoints | Recorded configuration/job |
| [result-f08ea1ad4acb901e4968](../observations.json)<br>source-02b38a04ec7bf58a6981ad37.json<br>`/stages/1/cold` | [qwen38-fit-mtp1](qwen38-fit-mtp1.md) | test outcome | Outcome unspecified | end_to_end_output_tps=1.27 accepted tokens/s; generated_tokens=256 accepted tokens; wall_seconds=200.82 s | Recorded configuration/job |
| [result-f0ca8b3859e29dc9636b](../observations.json)<br>source-3298d12f74e7ed1d195458e2.json<br>`/stages/0/cold` | [qwen38-fit-mtp1](qwen38-fit-mtp1.md) | test outcome | Outcome unspecified | end_to_end_output_tps=1.00 accepted tokens/s; generated_tokens=141 accepted tokens; wall_seconds=140.59 s | Recorded configuration/job |
| [result-f24e2c2178a8d0ed34b6](../observations.json)<br>source-0a902e6b90235a08b4217ce4.json<br>`/after_cold/totals` | [qwen38-fit-mtp1](qwen38-fit-mtp1.md) | context allocation | Outcome unspecified | cached_tokens=0 tokens; generated_tokens=512 accepted tokens; prompt_tokens=131,296 tokens; recurrent_restores=0 checkpoints | Recorded configuration/job |
| [result-f90e9bb6bd0e094e6bad](../observations.json)<br>source-02b38a04ec7bf58a6981ad37.json<br>`/stages/0/cold` | [qwen38-fit-mtp1](qwen38-fit-mtp1.md) | test outcome | Outcome unspecified | end_to_end_output_tps=6.16 accepted tokens/s; generated_tokens=256 accepted tokens; wall_seconds=41.56 s | Recorded configuration/job |
| [result-fee05946bc09e744e247](../observations.json)<br>source-a820e2bfabbcec2bcea88429.json<br>`/after_cold/cache` | [qwen38-fit-mtp1](qwen38-fit-mtp1.md) | test outcome | Outcome unspecified | cached_tokens=670,464 tokens | Recorded configuration/job |
| [result-ffbbae0847464f8b574c](../observations.json)<br>source-4f7f033fcde00f98df0540dc.json<br>`/stages/0/warm` | [qwen38-fit-mtp1](qwen38-fit-mtp1.md) | test outcome | Outcome unspecified | end_to_end_output_tps=16.51 accepted tokens/s; generated_tokens=70 accepted tokens; wall_seconds=4.24 s | Recorded configuration/job |

These are saved result records, including failures and bounded checks. Copies, individual requests, report summaries and regrading can overlap; their counts are not independent test repetitions. Open each result for exact values, units, configuration binding and source receipts.

There are 11 retained lifecycle records. Their states, exit codes and configuration IDs remain in [catalog.json](../catalog.json); they do not supply missing benchmark results.

[Full archive](../../README.md) | [All retained waves](../RESULTS.md) | [Data definitions](../DATA.md) | [Recommended recipes](../../../README.md)
