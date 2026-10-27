# glm53-validation

**Historical record. Legacy / incomplete measurements.**

Model family: GLM 5.3 Flash.

Recorded archive reason: Historical capacity, fit or control configuration; later DFlash2 and MTP variants have separate records.

Historical configurations are provided for comparison. The [recommended recipes](../../../README.md) include supported launch scripts.

Current recipes using the same recorded checkpoint repository: [glm-5.3-flash-mtp1-tp3](../../../recipes/glm-5.3-flash-mtp1-tp3/README.md). Context, cache and runtime versions can differ.

## Saved Configuration Versions

Each configuration ID identifies a distinct original settings record. Deployment fields are omitted; versions can have identical published settings after that omission. Upstream runtime commits remain unspecified where the source retained only an integration label.

| Configuration | Recorded artifact / source | Configured card counts | Context tokens | GPU pool tokens | Slots | Draft mode / tokens |
| --- | --- | --- | --- | --- | --- | --- |
| cfg-148059de28634ce67985 | [turboderp/GLM-5.3-Flash-exl3@2a30229e67](https://huggingface.co/turboderp/GLM-5.3-Flash-exl3/tree/2a30229e67012798ba9f0cd832bb78abf4c363d5) | 4 | 32,768 | 131,072 | 16 | mtp / 3 |
| cfg-1483fab3efe0775ba1e9 | [turboderp/GLM-5.3-Flash-exl3@2a30229e67](https://huggingface.co/turboderp/GLM-5.3-Flash-exl3/tree/2a30229e67012798ba9f0cd832bb78abf4c363d5) | 3 | 32,768 | 131,072 | 8 | dflash2 / 7 |
| cfg-194f555b298b983944c5 | [turboderp/GLM-5.3-Flash-exl3@2a30229e67](https://huggingface.co/turboderp/GLM-5.3-Flash-exl3/tree/2a30229e67012798ba9f0cd832bb78abf4c363d5) | 4 | 32,768 | 131,072 | 16 | dflash2 / 7 |
| cfg-76a1920cf9dbe0e277e4 | [turboderp/GLM-5.3-Flash-exl3@2a30229e67](https://huggingface.co/turboderp/GLM-5.3-Flash-exl3/tree/2a30229e67012798ba9f0cd832bb78abf4c363d5) | 4 | 32,768 | 131,072 | 4 | dflash2 / 7 |
| cfg-d352ff70aa170b228108 | [turboderp/GLM-5.3-Flash-exl3@2a30229e67](https://huggingface.co/turboderp/GLM-5.3-Flash-exl3/tree/2a30229e67012798ba9f0cd832bb78abf4c363d5) | 4 | 32,768 | 131,072 | 4 | dflash2 / 7 |

Card counts are saved configuration choices, not a claim that every allowed placement was measured. A derived view can differ from its pinned download source.

<details>
<summary>cfg-148059de28634ce67985</summary>

```json
{
  "kind": "tabby",
  "gpu_counts": [
    4
  ],
  "context": 32768,
  "cache_tokens": 131072,
  "cache_mode": "Q8",
  "draft_cache_mode": "Q8",
  "draft_mode": "mtp",
  "draft_tokens": 3,
  "max_sessions": 16,
  "chunk_size": 2048,
  "reserve_mib": 4096,
  "ram_kv_mib": 4096,
  "ram_recurrent_mib": 16384,
  "dynamic_draft": false,
  "power_watts": 200,
  "host_memory_gib": 80,
  "host_swap_gib": 0,
  "min_vram_mib_per_gpu": 40000,
  "min_effective_vram_mib": 230000,
  "model_repository": "turboderp/GLM-5.3-Flash-exl3",
  "model_revision": "2a30229e67012798ba9f0cd832bb78abf4c363d5",
  "draft_repository": null,
  "draft_revision": null,
  "recorded_runtime_label": null,
  "served_model_label": "glm-5.3-flash",
  "main_reserve_mib_values_unordered": [
    20480
  ]
}
```

Pinned model revision recorded: yes. Source receipt labels, hashes and object locators are retained in [configurations.json](../configurations.json).

</details>

<details>
<summary>cfg-1483fab3efe0775ba1e9</summary>

```json
{
  "kind": "tabby",
  "gpu_counts": [
    3
  ],
  "context": 32768,
  "cache_tokens": 131072,
  "cache_mode": "Q8",
  "draft_cache_mode": "Q8",
  "draft_mode": "dflash2",
  "draft_tokens": 7,
  "max_sessions": 8,
  "chunk_size": 2048,
  "reserve_mib": 4096,
  "ram_kv_mib": 4096,
  "ram_recurrent_mib": 16384,
  "dynamic_draft": false,
  "power_watts": 200,
  "host_memory_gib": 80,
  "host_swap_gib": 0,
  "min_vram_mib_per_gpu": 60000,
  "min_effective_vram_mib": 190000,
  "model_repository": "turboderp/GLM-5.3-Flash-exl3",
  "model_revision": "2a30229e67012798ba9f0cd832bb78abf4c363d5",
  "draft_repository": null,
  "draft_revision": null,
  "recorded_runtime_label": null,
  "served_model_label": "glm-5.3-flash"
}
```

Pinned model revision recorded: yes. Source receipt labels, hashes and object locators are retained in [configurations.json](../configurations.json).

</details>

<details>
<summary>cfg-194f555b298b983944c5</summary>

```json
{
  "kind": "tabby",
  "gpu_counts": [
    4
  ],
  "context": 32768,
  "cache_tokens": 131072,
  "cache_mode": "Q8",
  "draft_cache_mode": "Q8",
  "draft_mode": "dflash2",
  "draft_tokens": 7,
  "max_sessions": 16,
  "chunk_size": 2048,
  "reserve_mib": 4096,
  "ram_kv_mib": 4096,
  "ram_recurrent_mib": 16384,
  "dynamic_draft": false,
  "power_watts": 200,
  "host_memory_gib": 80,
  "host_swap_gib": 0,
  "min_vram_mib_per_gpu": 40000,
  "min_effective_vram_mib": 230000,
  "model_repository": "turboderp/GLM-5.3-Flash-exl3",
  "model_revision": "2a30229e67012798ba9f0cd832bb78abf4c363d5",
  "draft_repository": null,
  "draft_revision": null,
  "recorded_runtime_label": null,
  "served_model_label": "glm-5.3-flash",
  "main_reserve_mib_values_unordered": [
    20480
  ]
}
```

Pinned model revision recorded: yes. Source receipt labels, hashes and object locators are retained in [configurations.json](../configurations.json).

</details>

<details>
<summary>cfg-76a1920cf9dbe0e277e4</summary>

```json
{
  "kind": "tabby",
  "gpu_counts": [
    4
  ],
  "context": 32768,
  "cache_tokens": 131072,
  "cache_mode": "Q8",
  "draft_cache_mode": "Q8",
  "draft_mode": "dflash2",
  "draft_tokens": 7,
  "max_sessions": 4,
  "chunk_size": 2048,
  "reserve_mib": 4096,
  "ram_kv_mib": 4096,
  "ram_recurrent_mib": 4096,
  "dynamic_draft": false,
  "power_watts": 200,
  "host_memory_gib": 80,
  "host_swap_gib": 0,
  "min_vram_mib_per_gpu": 40000,
  "min_effective_vram_mib": 230000,
  "model_repository": "turboderp/GLM-5.3-Flash-exl3",
  "model_revision": "2a30229e67012798ba9f0cd832bb78abf4c363d5",
  "draft_repository": null,
  "draft_revision": null,
  "recorded_runtime_label": null,
  "served_model_label": "glm-5.3-flash",
  "main_reserve_mib_values_unordered": [
    20480
  ]
}
```

Pinned model revision recorded: yes. Source receipt labels, hashes and object locators are retained in [configurations.json](../configurations.json).

</details>

<details>
<summary>cfg-d352ff70aa170b228108</summary>

```json
{
  "kind": "tabby",
  "gpu_counts": [
    4
  ],
  "context": 32768,
  "cache_tokens": 131072,
  "cache_mode": "Q8",
  "draft_cache_mode": "Q8",
  "draft_mode": "dflash2",
  "draft_tokens": 7,
  "max_sessions": 4,
  "chunk_size": 2048,
  "reserve_mib": 4096,
  "ram_kv_mib": 4096,
  "ram_recurrent_mib": 4096,
  "dynamic_draft": false,
  "power_watts": 200,
  "host_memory_gib": 80,
  "host_swap_gib": 0,
  "min_vram_mib_per_gpu": 40000,
  "min_effective_vram_mib": 230000,
  "model_repository": "turboderp/GLM-5.3-Flash-exl3",
  "model_revision": "2a30229e67012798ba9f0cd832bb78abf4c363d5",
  "draft_repository": null,
  "draft_revision": null,
  "recorded_runtime_label": null,
  "served_model_label": "glm-5.3-flash"
}
```

Pinned model revision recorded: yes. Source receipt labels, hashes and object locators are retained in [configurations.json](../configurations.json).

</details>

## Retained Measurements

| Profile / Wave | Layout; Draft / Tokens | Requests | Input tokens/request | Accepted output tokens/request | Cache / Reused input tokens | Context / GPU pool tokens | Shared decode tok/s total | Client after-first-token estimate tok/s | Whole-wave output tok/s | Median TTFT, s | Source report |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [glm53-validation](glm53-validation.md)<br>wave-0174e21f927bab329891 | layout unspecified; dflash2 / 7 | 16 | 2,096 to 24,632 | 256 | cold; reused 0 | 32,768 / 131,072 | Not recorded | 80.33 | 27.82 | 110.71 | Pass |
| [glm53-validation](glm53-validation.md)<br>wave-077d1abee945345dc7d1 | layout unspecified; mtp / 3 | 16 | 2,366 to 24,876 | 256 | cached_prefix; reused 2,048 to 24,576 | 32,768 / 131,072 | Not recorded | 49.15 | 46.75 | 34.55 | Pass |
| [glm53-validation](glm53-validation.md)<br>wave-0bd7144d2a9546ed1f7e | layout unspecified; dflash2 / 7 | 8 | 4,276 to 4,288 | 128 | cached_prefix; reused 4,096 | 32,768 / 131,072 | Not recorded | 43.14 | 41.40 | 8.93 | Pass |
| [glm53-validation](glm53-validation.md)<br>wave-2ae211f6724ea28dc75c | layout unspecified; mtp / 3 | 4 | 24,610 | 64 to 105 | cold; reused 0 | 32,768 / 131,072 | Not recorded | 49.25 | 4.03 | 81.80 | Pass |
| [glm53-validation](glm53-validation.md)<br>wave-320ece82df93ab7c0bba | layout unspecified; dflash2 / 7 | 8 | 4,145 | 128 | cold; reused 0 | 32,768 / 131,072 | Not recorded | 25.75 | 17.43 | 36.86 | Pass |
| [glm53-validation](glm53-validation.md)<br>wave-3401dda1e94d2f78f6ad | layout unspecified; dflash2 / 7 | 4 | 24,536 | 59 to 105 | cold; reused 0 | 32,768 / 131,072 | Not recorded | 46.97 | 3.57 | 88.14 | Pass |
| [glm53-validation](glm53-validation.md)<br>wave-3874056966f14b1f48f6 | layout unspecified; dflash2 / 7 | 16 | 2,098 to 24,634 | 256 | cold; reused 0 | 32,768 / 131,072 | Not recorded | 46.24 | 28.45 | 90.65 | Pass |
| [glm53-validation](glm53-validation.md)<br>wave-3940a5083fac5e7a58ae | layout unspecified; dflash2 / 7 | 4 | 24,604 to 24,650 | 19 | cached_prefix; reused 24,576 | 32,768 / 131,072 | Not recorded | 33.00 | 22.95 | 3.25 | Pass |
| [glm53-validation](glm53-validation.md)<br>wave-413b97415a40f31a890f | layout unspecified; dflash2 / 7 | 4 | 24,620 to 24,676 | 19 | cached_prefix; reused 24,576 | 32,768 / 131,072 | Not recorded | 22.23 | 16.57 | 4.50 | Pass |
| [glm53-validation](glm53-validation.md)<br>wave-4d55278377407c61a063 | layout unspecified; dflash2 / 7 | 16 | 2,096 to 24,632 | 256 | cold; reused 0 | 32,768 / 131,072 | Not recorded | 54.82 | 24.75 | 113.48 | Pass |
| [glm53-validation](glm53-validation.md)<br>wave-4d746fede82f30beca25 | layout unspecified; dflash2 / 7 | 16 | 2,096 to 24,632 | 256 | cold; reused 0 | 32,768 / 131,072 | Not recorded | 44.75 | 23.59 | 116.61 | Pass |
| [glm53-validation](glm53-validation.md)<br>wave-51ea4973c454e3b35061 | layout unspecified; dflash2 / 7 | 16 | 2,357 to 24,892 | 256 | cached_prefix; reused 2,048 to 24,576 | 32,768 / 131,072 | Not recorded | 68.01 | 63.73 | 21.59 | Pass |
| [glm53-validation](glm53-validation.md)<br>wave-52ddb43c40e7c674416d | layout unspecified; dflash2 / 7 | 16 | 2,369 to 24,874 | 256 | cached_prefix; reused 2,048 to 24,576 | 32,768 / 131,072 | Not recorded | 57.18 | 54.66 | 31.32 | Pass |
| [glm53-validation](glm53-validation.md)<br>wave-5f217fdc7b89fcea7014 | layout unspecified; dflash2 / 7 | 16 | 2,366 to 24,874 | 256 | cached_prefix; reused 2,048 to 24,576 | 32,768 / 131,072 | Not recorded | 61.09 | 57.91 | 22.30 | Pass |
| [glm53-validation](glm53-validation.md)<br>wave-750c6e979d251ea472f7 | layout unspecified; mtp / 3 | 16 | 2,096 to 24,632 | 256 | cold; reused 0 | 32,768 / 131,072 | Not recorded | 39.40 | 23.43 | 110.85 | Pass |
| [glm53-validation](glm53-validation.md)<br>wave-804f37e3e067e1bc31c9 | layout unspecified; mtp / 3 | 16 | 2,366 to 24,890 | 256 | cached_prefix; reused 2,048 to 24,576 | 32,768 / 131,072 | Not recorded | 63.40 | 59.63 | 23.86 | Pass |
| [glm53-validation](glm53-validation.md)<br>wave-80d04af7999ad6ca3926 | layout unspecified; mtp / 3 | 16 | 2,096 to 24,632 | 256 | cold; reused 0 | 32,768 / 131,072 | Not recorded | 46.26 | 27.46 | 95.35 | Pass |
| [glm53-validation](glm53-validation.md)<br>wave-8a00fb328806403f9d90 | layout unspecified; dflash2 / 7 | 4 | 24,538 | 73 to 128 | cold; reused 0 | 32,768 / 131,072 | Not recorded | 73.17 | 4.16 | 88.35 | Pass |
| [glm53-validation](glm53-validation.md)<br>wave-8a5cff43c7a4e6778e0a | layout unspecified; mtp / 3 | 16 | 2,351 to 24,876 | 256 | cached_prefix; reused 2,048 to 24,576 | 32,768 / 131,072 | Not recorded | 75.94 | 70.63 | 17.92 | Pass |
| [glm53-validation](glm53-validation.md)<br>wave-8dd6ddb6e1e89b8c4ddf | layout unspecified; dflash2 / 7 | 4 | 4,405 to 4,416 | 256 | cached_prefix; reused 4,096 | 32,768 / 131,072 | Not recorded | 60.68 | 46.36 | 8.37 | Pass |
| [glm53-validation](glm53-validation.md)<br>wave-a3d9837495986f796f0b | layout unspecified; dflash2 / 7 | 16 | 2,098 to 24,634 | 256 | cold; reused 0 | 32,768 / 131,072 | Not recorded | 46.42 | 26.89 | 99.65 | Pass |
| [glm53-validation](glm53-validation.md)<br>wave-b8a5a90ad7a880d477b3 | layout unspecified; mtp / 3 | 16 | 2,096 to 24,632 | 256 | cold; reused 0 | 32,768 / 131,072 | Not recorded | 47.89 | 29.37 | 95.55 | Pass |
| [glm53-validation](glm53-validation.md)<br>wave-c20eac7dab4ed90cbfc2 | layout unspecified; dflash2 / 7 | 4 | 4,145 | 256 | cold; reused 0 | 32,768 / 131,072 | Not recorded | 50.20 | 26.23 | 23.18 | Pass |
| [glm53-validation](glm53-validation.md)<br>wave-e20501a21ef81675adbe | layout unspecified; mtp / 3 | 4 | 24,683 to 24,724 | 19 | cached_prefix; reused 24,576 | 32,768 / 131,072 | Not recorded | 21.65 | 16.90 | 3.91 | Pass |
| [glm53-validation](glm53-validation.md)<br>wave-e9fd00363933ab490c7c | layout unspecified; dflash2 / 7 | 16 | 2,366 to 24,890 | 256 | cached_prefix; reused 2,048 to 24,576 | 32,768 / 131,072 | Not recorded | 50.11 | 45.74 | 43.55 | Pass |
| [glm53-validation](glm53-validation.md)<br>wave-fbfb003ee4b10b4ad0cc | layout unspecified; dflash2 / 7 | 16 | 2,367 to 24,872 | 256 | cached_prefix; reused 2,048 to 24,576 | 32,768 / 131,072 | Not recorded | 66.64 | 62.87 | 32.77 | Pass |

Rates are whole-wave totals over the stated request count. A wave may span multiple independent model instances; [measurements.json](../measurements.json) retains their contributions and the exact configuration IDs. Do not interpret a multi-instance total as one card's rate.

A dash in shared decode means no qualified synchronized interval is available. Whole-wave throughput includes prefill and queueing. A valid decode interval can survive inside an overall failed or partial check; the source-report outcome is preserved. No rows are averaged.

## Bounded Checks

| Check | Reported outcome | Retained counts / flags |
| --- | --- | --- |
| check-01cb9364ce1bba7cee84 | Pass | {"passed":true,"replayed_history_tokens":[0,0,0,0],"input_tokens":[24534,24534,24534,24534]} |
| check-032e38a9bb6d8ef3a490 | Pass | {"passed":true,"input_tokens":[24630,24630,16440,16440,2094,2094,2094,2094,2094,2094,2094,2094,2094,2094,2094,2094]} |
| check-07c53d7ad0e7d627af01 | Pass | {"passed":true,"replayed_history_tokens":[34,34,34,34],"input_tokens":[24608,24608,24608,24608]} |
| check-0b7d3742eebaf9a394dc | Pass | {"passed":true} |
| check-0ce2e05f13231db979aa | Pass | {"passed":true,"input_tokens":[24630,24630,16440,16440,2094,2094,2094,2094,2094,2094,2094,2094,2094,2094,2094,2094]} |
| check-0f199522f542430edba9 | Pass | {"passed":true,"input_tokens":[24630,24630,16440,16440,2094,2094,2094,2094,2094,2094,2094,2094,2094,2094,2094,2094]} |
| check-128e230f7e34ebbcaeec | Pass | {"passed":true,"input_tokens":[24630,24630,16440,16440,2094,2094,2094,2094,2094,2094,2094,2094,2094,2094,2094,2094]} |
| check-1c68578cb342bbab44ce | Pass | {"passed":true,"input_tokens":[4143,4143,4143,4143,4143,4143,4143,4143]} |
| check-2d8bbbb263f668837e92 | Pass | {"passed":true} |
| check-4755c97a0c16436c600f | Pass | {"passed":true,"input_tokens":[24632,24632,16442,16442,2096,2096,2096,2096,2096,2096,2096,2096,2096,2096,2096,2096]} |
| check-5916211d1b805a4f618a | Failed / partial | {"passed":false} |
| check-79a2e2ebc599805ba9da | Pass | {"passed":true} |
| check-8a3c6f1e18e40a4414af | Pass | {"passed":true,"input_tokens":[24632,24632,16442,16442,2096,2096,2096,2096,2096,2096,2096,2096,2096,2096,2096,2096]} |
| check-8b827ba0d97d651ec8c5 | Pass | {"passed":true,"compact_tokens":26214,"context_tokens":32768} |
| check-998eef4eae71ebff56b8 | Pass | {"passed":true} |
| check-b4a73b66b8f0dffff247 | Pass | {"passed":true,"input_tokens":[24630,24630,16440,16440,2094,2094,2094,2094,2094,2094,2094,2094,2094,2094,2094,2094]} |
| check-cc42af33dcab8f061690 | Failed / partial | {"passed":false,"input_tokens":[4121,4121,4121,4121]} |
| check-d7ccc02ed2542073d3c6 | Pass | {"passed":true,"input_tokens":[4143,4143,4143,4143]} |
| check-d972bd5f657174c70e75 | Pass | {"passed":true,"input_tokens":[24630,24630,16440,16440,2094,2094,2094,2094,2094,2094,2094,2094,2094,2094,2094,2094]} |
| check-df7e79562b9abefca4a7 | Pass | {"passed":true,"replayed_history_tokens":[0,0,0,0],"input_tokens":[24536,24536,24536,24536]} |
| check-e6d03f27f2d4f16f2f01 | Pass | {"passed":true,"compact_tokens":26214,"context_tokens":32768} |

These checks retain their reported scope. A context/allocation/retrieval check is not a general quality score or a speed qualification at that context. Exact flags and provenance are in [checks.json](../checks.json).

## Additional Test Results

| Result / Source | Profile | Evidence type | Reported outcome | Retained values | Configuration binding |
| --- | --- | --- | --- | --- | --- |
| [result-0096711113fcaad0bf9f](../observations.json)<br>source-b9c356222faed9287b4b9735.json<br>`/last_runtime/cache` | [glm53-validation](glm53-validation.md) | test outcome | Outcome unspecified | cached_tokens=121,856 tokens | Recorded configuration/job |
| [result-0841c78dee827745ddae](../observations.json)<br>source-b9c356222faed9287b4b9735.json<br>`/last_runtime` | [glm53-validation](glm53-validation.md) | test outcome | Outcome unspecified | context=32,768 tokens | Recorded configuration/job |
| [result-08451678dfaee541eed6](../observations.json)<br>source-1daed8883b7352c1efcb8c5b.json<br>`/last_runtime/totals` | [glm53-validation](glm53-validation.md) | context allocation | Outcome unspecified | cached_tokens=319,488 tokens; generated_tokens=24,576 accepted tokens; prompt_tokens=656,516 tokens; recurrent_restores=48 checkpoints | Recorded configuration/job |
| [result-094fcb8ae450e9d9372a](../observations.json)<br>source-6c341ac102f58085bbec4ce5.json<br>`/after_cold/cache` | [glm53-validation](glm53-validation.md) | test outcome | Outcome unspecified | cached_tokens=128,256 tokens | Recorded configuration/job |
| [result-0a98ae683a9667ef5245](../observations.json)<br>source-d3112726a56ed4a4b24689a2.json<br>`/after_cold/totals` | [glm53-validation](glm53-validation.md) | context allocation | Outcome unspecified | cached_tokens=106,496 tokens; generated_tokens=12,288 accepted tokens; prompt_tokens=326,148 tokens; recurrent_restores=16 checkpoints | Recorded configuration/job |
| [result-0b6d869e3cdacae94fef](../observations.json)<br>source-6ba7a7c8d6cea666fbe1a73f.json<br>`/cache` | [glm53-validation](glm53-validation.md) | test outcome | Outcome unspecified | cached_tokens=0 tokens | Recorded configuration/job |
| [result-104f5497421aa2ac045c](../observations.json)<br>source-3b34047c4abe6cdbf63a25d5.json<br>`/last_runtime/totals` | [glm53-validation](glm53-validation.md) | context allocation | Outcome unspecified | cached_tokens=98,304 tokens; generated_tokens=7,168 accepted tokens; prompt_tokens=209,380 tokens; recurrent_restores=16 checkpoints | Recorded configuration/job |
| [result-166ea7253a5df952fbe6](../observations.json)<br>source-3df404ff157f9a1bc90a8f93.json<br>`/runs/0/cold` | [glm53-validation](glm53-validation.md) | test outcome | Outcome unspecified | end_to_end_output_tps=23.43 accepted tokens/s; generated_tokens=4,096 accepted tokens; wall_seconds=174.84 s | Recorded configuration/job |
| [result-1ddd52ebb7a71401cd9b](../observations.json)<br>source-6b252527b8bac27878e5516a.json<br>`/after_cold/totals` | [glm53-validation](glm53-validation.md) | context allocation | Outcome unspecified | cached_tokens=106,496 tokens; generated_tokens=12,301 accepted tokens; prompt_tokens=326,249 tokens; recurrent_restores=16 checkpoints | Recorded configuration/job |
| [result-1f857ea1b2b11da7981c](../observations.json)<br>source-29228a8889e306672794f140.json<br>`/after_cold/totals` | [glm53-validation](glm53-validation.md) | context allocation | Outcome unspecified | cached_tokens=0 tokens; generated_tokens=4,109 accepted tokens; prompt_tokens=107,420 tokens; recurrent_restores=0 checkpoints | Recorded configuration/job |
| [result-1f9413ade0d9670700b7](../observations.json)<br>source-d0721f0ef147f78852bbf9c1.json<br>`/after_burst/cache` | [glm53-validation](glm53-validation.md) | test outcome | Outcome unspecified | cached_tokens=129,280 tokens | Recorded configuration/job |
| [result-21e9efc26cf95182120c](../observations.json)<br>source-a0e99d6d3e3d7f7faa2ba981.json<br>`/runs/1/warm` | [glm53-validation](glm53-validation.md) | test outcome | Outcome unspecified | end_to_end_output_tps=57.91 accepted tokens/s; generated_tokens=4,096 accepted tokens; wall_seconds=70.73 s | Recorded configuration/job |
| [result-243048fc4f0b10a83aba](../observations.json)<br>source-315936d4a87c80ae09ebaa69.json<br>`/after_cold/totals` | [glm53-validation](glm53-validation.md) | context allocation | Outcome unspecified | cached_tokens=0 tokens; generated_tokens=1,108 accepted tokens; prompt_tokens=17,094 tokens; recurrent_restores=0 checkpoints | Recorded configuration/job |
| [result-2489e2210051325c6986](../observations.json)<br>source-908b866a0f00d6f4cbc46561.json<br>`/after_cold` | [glm53-validation](glm53-validation.md) | test outcome | Outcome unspecified | context=32,768 tokens | Recorded configuration/job |
| [result-29d0d40f326688dc8da2](../observations.json)<br>source-00c96d2509bab19c756bd94d.json<br>`/after_cold/totals` | [glm53-validation](glm53-validation.md) | context allocation | Outcome unspecified | cached_tokens=0 tokens; generated_tokens=4,109 accepted tokens; prompt_tokens=107,452 tokens; recurrent_restores=0 checkpoints | Recorded configuration/job |
| [result-2bfb39a16b772dc9e63d](../observations.json)<br>source-be47318d21b883be598753cf.json<br>`/after_burst/totals` | [glm53-validation](glm53-validation.md) | context allocation | Outcome unspecified | cached_tokens=319,488 tokens; generated_tokens=25,328 accepted tokens; prompt_tokens=952,107 tokens; recurrent_restores=48 checkpoints | Recorded configuration/job |
| [result-2e0b14dd9cfcd64026be](../observations.json)<br>source-fc8bbcd8800846bb2de74301.json<br>`/after_burst/totals` | [glm53-validation](glm53-validation.md) | context allocation | Outcome unspecified | cached_tokens=16,384 tokens; generated_tokens=2,642 accepted tokens; prompt_tokens=198,576 tokens; recurrent_restores=4 checkpoints | Recorded configuration/job |
| [result-325e7155dfcc92d289fa](../observations.json)<br>source-95970e8a8fa58cdf3db57b0a.json<br>`/cache` | [glm53-validation](glm53-validation.md) | test outcome | Outcome unspecified | cached_tokens=0 tokens | Recorded configuration/job |
| [result-3589bbd9775614b791c6](../observations.json)<br>source-84a296f9a57b3e4e910a7a5f.json<br>`/` | [glm53-validation](glm53-validation.md) | context allocation | Pass | compact_tokens=26,214 tokens; context_tokens=32,768 tokens | Recorded configuration/job |
| [result-41199ff7103e2d6be6b8](../observations.json)<br>source-e86353c4cbb88440f301c9d4.json<br>`/after_cold/cache` | [glm53-validation](glm53-validation.md) | test outcome | Outcome unspecified | cached_tokens=110,592 tokens | Recorded configuration/job |
| [result-449f6da88182e48f735c](../observations.json)<br>source-32696c46d8371d817ee2a9e2.json<br>`/runs/1/warm` | [glm53-validation](glm53-validation.md) | test outcome | Outcome unspecified | end_to_end_output_tps=63.73 accepted tokens/s; generated_tokens=4,096 accepted tokens; wall_seconds=64.27 s | Recorded configuration/job |
| [result-44d5393d397dfc7bf7f8](../observations.json)<br>source-3df404ff157f9a1bc90a8f93.json<br>`/runs/2/warm` | [glm53-validation](glm53-validation.md) | test outcome | Outcome unspecified | end_to_end_output_tps=70.63 accepted tokens/s; generated_tokens=4,096 accepted tokens; wall_seconds=57.99 s | Recorded configuration/job |
| [result-484d5a8c894a17d7676b](../observations.json)<br>source-1daed8883b7352c1efcb8c5b.json<br>`/last_runtime/cache` | [glm53-validation](glm53-validation.md) | test outcome | Outcome unspecified | cached_tokens=121,856 tokens | Recorded configuration/job |
| [result-48e23f18d8791570c676](../observations.json)<br>source-32696c46d8371d817ee2a9e2.json<br>`/runs/0/warm` | [glm53-validation](glm53-validation.md) | test outcome | Outcome unspecified | end_to_end_output_tps=54.66 accepted tokens/s; generated_tokens=4,096 accepted tokens; wall_seconds=74.94 s | Recorded configuration/job |
| [result-4987d85a52bfe92c195c](../observations.json)<br>source-34f4bbb95e3c8afc1ff9fb41.json<br>`/` | [glm53-validation](glm53-validation.md) | test outcome | Outcome unspecified | context=32,768 tokens | Recorded configuration/job |
| [result-4a3d49d09fc1921af18d](../observations.json)<br>source-84a296f9a57b3e4e910a7a5f.json<br>`/client_result` | [glm53-validation](glm53-validation.md) | test outcome | Outcome unspecified | elapsed_seconds=31.02 s | Recorded configuration/job |
| [result-4c7ede56354a8a102857](../observations.json)<br>source-dc86404f4933c4b5539c47b9.json<br>`/after_cold` | [glm53-validation](glm53-validation.md) | test outcome | Outcome unspecified | context=32,768 tokens | Recorded configuration/job |
| [result-4c8f688aa6e3ec5c57e5](../observations.json)<br>source-6719dd0517a962852e39565e.json<br>`/last_runtime/cache` | [glm53-validation](glm53-validation.md) | test outcome | Outcome unspecified | cached_tokens=129,792 tokens | Recorded configuration/job |
| [result-5a12b8ab228486165053](../observations.json)<br>source-3df404ff157f9a1bc90a8f93.json<br>`/runs/1/cold` | [glm53-validation](glm53-validation.md) | test outcome | Outcome unspecified | end_to_end_output_tps=27.46 accepted tokens/s; generated_tokens=4,096 accepted tokens; wall_seconds=149.18 s | Recorded configuration/job |
| [result-5b8020c910dac0fab248](../observations.json)<br>source-84a296f9a57b3e4e910a7a5f.json<br>`/verification` | [glm53-validation](glm53-validation.md) | test outcome | Outcome unspecified | elapsed_seconds=0.06 s | Recorded configuration/job |
| [result-5c7ce48225b5653aa46f](../observations.json)<br>source-3df404ff157f9a1bc90a8f93.json<br>`/runs/0/warm` | [glm53-validation](glm53-validation.md) | test outcome | Outcome unspecified | end_to_end_output_tps=46.75 accepted tokens/s; generated_tokens=4,096 accepted tokens; wall_seconds=87.62 s | Recorded configuration/job |
| [result-5ee839a4bec81fb0683e](../observations.json)<br>source-84a296f9a57b3e4e910a7a5f.json<br>`/verification` | [glm53-validation](glm53-validation.md) | test outcome | Outcome unspecified | elapsed_seconds=0.03 s | Recorded configuration/job |
| [result-5f153348afdda3f0c194](../observations.json)<br>source-5c1d5501c69f9b3c66f01b1d.json<br>`/` | [glm53-validation](glm53-validation.md) | test outcome | Outcome unspecified | context=32,768 tokens | Recorded configuration/job |
| [result-5fb27886eef5c23d0a6b](../observations.json)<br>source-f4c709360e3d49b847e94dc6.json<br>`/after_cold/totals` | [glm53-validation](glm53-validation.md) | context allocation | Outcome unspecified | cached_tokens=212,992 tokens; generated_tokens=20,480 accepted tokens; prompt_tokens=544,984 tokens; recurrent_restores=32 checkpoints | Recorded configuration/job |
| [result-64137ceec4dfc8310de0](../observations.json)<br>source-908b866a0f00d6f4cbc46561.json<br>`/after_cold/cache` | [glm53-validation](glm53-validation.md) | test outcome | Outcome unspecified | cached_tokens=124,416 tokens | Recorded configuration/job |
| [result-658ca142604df4eba4a1](../observations.json)<br>source-6ba7a7c8d6cea666fbe1a73f.json<br>`/totals` | [glm53-validation](glm53-validation.md) | context allocation | Outcome unspecified | cached_tokens=0 tokens; generated_tokens=0 accepted tokens; prompt_tokens=0 tokens; recurrent_restores=0 checkpoints | Recorded configuration/job |
| [result-674fc3c44f5ee6ea29f6](../observations.json)<br>source-34f4bbb95e3c8afc1ff9fb41.json<br>`/cache` | [glm53-validation](glm53-validation.md) | test outcome | Outcome unspecified | cached_tokens=0 tokens | Recorded configuration/job |
| [result-699a0632a044de6e7405](../observations.json)<br>source-be47318d21b883be598753cf.json<br>`/after_burst/cache` | [glm53-validation](glm53-validation.md) | test outcome | Outcome unspecified | cached_tokens=129,280 tokens | Recorded configuration/job |
| [result-6a426d54898b65a90475](../observations.json)<br>source-29228a8889e306672794f140.json<br>`/after_cold/cache` | [glm53-validation](glm53-validation.md) | test outcome | Outcome unspecified | cached_tokens=110,592 tokens | Recorded configuration/job |
| [result-6c57cdf59d4a60718e3b](../observations.json)<br>source-be47318d21b883be598753cf.json<br>`/after_cold` | [glm53-validation](glm53-validation.md) | test outcome | Outcome unspecified | context=32,768 tokens | Recorded configuration/job |
| [result-6e703dca9b6cdd7388a1](../observations.json)<br>source-b9c356222faed9287b4b9735.json<br>`/last_runtime/totals` | [glm53-validation](glm53-validation.md) | context allocation | Outcome unspecified | cached_tokens=212,992 tokens; generated_tokens=16,397 accepted tokens; prompt_tokens=437,966 tokens; recurrent_restores=32 checkpoints | Recorded configuration/job |
| [result-70a1bf6b07b8d95f3d03](../observations.json)<br>source-95970e8a8fa58cdf3db57b0a.json<br>`/` | [glm53-validation](glm53-validation.md) | test outcome | Outcome unspecified | context=32,768 tokens | Recorded configuration/job |
| [result-71712730545c2c128678](../observations.json)<br>source-29228a8889e306672794f140.json<br>`/after_cold` | [glm53-validation](glm53-validation.md) | test outcome | Outcome unspecified | context=32,768 tokens | Recorded configuration/job |
| [result-71cb201099a880e9628c](../observations.json)<br>source-6719dd0517a962852e39565e.json<br>`/last_runtime/totals` | [glm53-validation](glm53-validation.md) | context allocation | Outcome unspecified | cached_tokens=417,792 tokens; generated_tokens=25,404 accepted tokens; prompt_tokens=1,050,938 tokens; recurrent_restores=52 checkpoints | Recorded configuration/job |
| [result-7b0562e2598ce5d5b445](../observations.json)<br>source-d0721f0ef147f78852bbf9c1.json<br>`/after_cold/cache` | [glm53-validation](glm53-validation.md) | test outcome | Outcome unspecified | cached_tokens=128,000 tokens | Recorded configuration/job |
| [result-7d7124c8a321fac7bc2e](../observations.json)<br>source-dc86404f4933c4b5539c47b9.json<br>`/after_cold/totals` | [glm53-validation](glm53-validation.md) | context allocation | Outcome unspecified | cached_tokens=212,992 tokens; generated_tokens=20,493 accepted tokens; prompt_tokens=545,097 tokens; recurrent_restores=32 checkpoints | Recorded configuration/job |
| [result-7da45a9575174ea7a58c](../observations.json)<br>source-be47318d21b883be598753cf.json<br>`/after_cold/cache` | [glm53-validation](glm53-validation.md) | test outcome | Outcome unspecified | cached_tokens=124,928 tokens | Recorded configuration/job |
| [result-7f5a0e09dd261dd10204](../observations.json)<br>source-a0e99d6d3e3d7f7faa2ba981.json<br>`/runs/0/warm` | [glm53-validation](glm53-validation.md) | test outcome | Outcome unspecified | end_to_end_output_tps=45.74 accepted tokens/s; generated_tokens=4,096 accepted tokens; wall_seconds=89.55 s | Recorded configuration/job |
| [result-8234ec2006a8cdd135c0](../observations.json)<br>source-a0e99d6d3e3d7f7faa2ba981.json<br>`/runs/2/warm` | [glm53-validation](glm53-validation.md) | test outcome | Outcome unspecified | end_to_end_output_tps=62.87 accepted tokens/s; generated_tokens=4,096 accepted tokens; wall_seconds=65.15 s | Recorded configuration/job |
| [result-83e8e8dfeb302ebffd73](../observations.json)<br>source-95970e8a8fa58cdf3db57b0a.json<br>`/totals` | [glm53-validation](glm53-validation.md) | context allocation | Outcome unspecified | cached_tokens=0 tokens; generated_tokens=0 accepted tokens; prompt_tokens=0 tokens; recurrent_restores=0 checkpoints | Recorded configuration/job |
| [result-8453aee7a4c774cfa5a2](../observations.json)<br>source-34f4bbb95e3c8afc1ff9fb41.json<br>`/totals` | [glm53-validation](glm53-validation.md) | context allocation | Outcome unspecified | cached_tokens=0 tokens; generated_tokens=0 accepted tokens; prompt_tokens=0 tokens; recurrent_restores=0 checkpoints | Recorded configuration/job |
| [result-884579f4d947f1a67e05](../observations.json)<br>source-fc8bbcd8800846bb2de74301.json<br>`/after_cold/totals` | [glm53-validation](glm53-validation.md) | context allocation | Outcome unspecified | cached_tokens=16,384 tokens; generated_tokens=2,514 accepted tokens; prompt_tokens=132,888 tokens; recurrent_restores=4 checkpoints | Recorded configuration/job |
| [result-8a35686af660ccded279](../observations.json)<br>source-d3112726a56ed4a4b24689a2.json<br>`/after_cold` | [glm53-validation](glm53-validation.md) | test outcome | Outcome unspecified | context=32,768 tokens | Recorded configuration/job |
| [result-8e2d2eeca62812619e7c](../observations.json)<br>source-d0721f0ef147f78852bbf9c1.json<br>`/after_burst` | [glm53-validation](glm53-validation.md) | test outcome | Outcome unspecified | context=32,768 tokens | Recorded configuration/job |
| [result-8e7013d7be7b7fdf2188](../observations.json)<br>source-6c341ac102f58085bbec4ce5.json<br>`/after_cold/totals` | [glm53-validation](glm53-validation.md) | context allocation | Outcome unspecified | cached_tokens=236,288 tokens; generated_tokens=5,156 accepted tokens; prompt_tokens=593,482 tokens; recurrent_restores=18 checkpoints | Recorded configuration/job |
| [result-91ca8408182f7c2345e4](../observations.json)<br>source-f4c709360e3d49b847e94dc6.json<br>`/after_cold/cache` | [glm53-validation](glm53-validation.md) | test outcome | Outcome unspecified | cached_tokens=124,416 tokens | Recorded configuration/job |
| [result-93be8fea5a192383278b](../observations.json)<br>source-6ba7a7c8d6cea666fbe1a73f.json<br>`/` | [glm53-validation](glm53-validation.md) | test outcome | Outcome unspecified | context=32,768 tokens | Recorded configuration/job |
| [result-948f9612ac09ed4684d6](../observations.json)<br>source-908b866a0f00d6f4cbc46561.json<br>`/after_cold/totals` | [glm53-validation](glm53-validation.md) | context allocation | Outcome unspecified | cached_tokens=106,496 tokens; generated_tokens=12,301 accepted tokens; prompt_tokens=326,362 tokens; recurrent_restores=16 checkpoints | Recorded configuration/job |
| [result-9528cbb4b7e53c4e7ab7](../observations.json)<br>source-315936d4a87c80ae09ebaa69.json<br>`/after_cold` | [glm53-validation](glm53-validation.md) | test outcome | Outcome unspecified | context=32,768 tokens | Recorded configuration/job |
| [result-9882f0bed0dfc6760993](../observations.json)<br>source-f4c709360e3d49b847e94dc6.json<br>`/after_cold` | [glm53-validation](glm53-validation.md) | test outcome | Outcome unspecified | context=32,768 tokens | Recorded configuration/job |
| [result-98d90569c4ef8e5709d7](../observations.json)<br>source-d0721f0ef147f78852bbf9c1.json<br>`/after_cold/totals` | [glm53-validation](glm53-validation.md) | context allocation | Outcome unspecified | cached_tokens=137,984 tokens; generated_tokens=3,928 accepted tokens; prompt_tokens=428,888 tokens; recurrent_restores=14 checkpoints | Recorded configuration/job |
| [result-9d6efa15952dd03b0ffd](../observations.json)<br>source-d0721f0ef147f78852bbf9c1.json<br>`/after_burst/totals` | [glm53-validation](glm53-validation.md) | context allocation | Outcome unspecified | cached_tokens=137,984 tokens; generated_tokens=4,056 accepted tokens; prompt_tokens=461,808 tokens; recurrent_restores=14 checkpoints | Recorded configuration/job |
| [result-9e9a17926e0da7516230](../observations.json)<br>source-3b34047c4abe6cdbf63a25d5.json<br>`/last_runtime` | [glm53-validation](glm53-validation.md) | test outcome | Outcome unspecified | context=32,768 tokens | Recorded configuration/job |
| [result-9f3032d9add162de5c4c](../observations.json)<br>source-fc8bbcd8800846bb2de74301.json<br>`/after_burst/cache` | [glm53-validation](glm53-validation.md) | test outcome | Outcome unspecified | cached_tokens=129,536 tokens | Recorded configuration/job |
| [result-a708712db071082940cb](../observations.json)<br>source-84a296f9a57b3e4e910a7a5f.json<br>`/client_result` | [glm53-validation](glm53-validation.md) | test outcome | Outcome unspecified | elapsed_seconds=14.89 s | Recorded configuration/job |
| [result-a7799c0264e22f3a0783](../observations.json)<br>source-00c96d2509bab19c756bd94d.json<br>`/after_cold` | [glm53-validation](glm53-validation.md) | test outcome | Outcome unspecified | context=32,768 tokens | Recorded configuration/job |
| [result-b0d3528f21dccb70a1d3](../observations.json)<br>source-be47318d21b883be598753cf.json<br>`/after_cold/totals` | [glm53-validation](glm53-validation.md) | context allocation | Outcome unspecified | cached_tokens=319,488 tokens; generated_tokens=24,944 accepted tokens; prompt_tokens=755,043 tokens; recurrent_restores=48 checkpoints | Recorded configuration/job |
| [result-b15d82b6141380447133](../observations.json)<br>source-5c1d5501c69f9b3c66f01b1d.json<br>`/cache` | [glm53-validation](glm53-validation.md) | test outcome | Outcome unspecified | cached_tokens=0 tokens | Recorded configuration/job |
| [result-b454c6ed54c4cc982dd6](../observations.json)<br>source-5c1d5501c69f9b3c66f01b1d.json<br>`/totals` | [glm53-validation](glm53-validation.md) | context allocation | Outcome unspecified | cached_tokens=0 tokens; generated_tokens=0 accepted tokens; prompt_tokens=0 tokens; recurrent_restores=0 checkpoints | Recorded configuration/job |
| [result-b53b573d4bd1a5c46e3c](../observations.json)<br>source-d0721f0ef147f78852bbf9c1.json<br>`/after_cold` | [glm53-validation](glm53-validation.md) | test outcome | Outcome unspecified | context=32,768 tokens | Recorded configuration/job |
| [result-b551d47ad02d6ec420a8](../observations.json)<br>source-32696c46d8371d817ee2a9e2.json<br>`/runs/0/cold` | [glm53-validation](glm53-validation.md) | test outcome | Outcome unspecified | end_to_end_output_tps=26.89 accepted tokens/s; generated_tokens=4,096 accepted tokens; wall_seconds=152.34 s | Recorded configuration/job |
| [result-b7ad90eeb991a09434df](../observations.json)<br>source-be47318d21b883be598753cf.json<br>`/after_burst` | [glm53-validation](glm53-validation.md) | test outcome | Outcome unspecified | context=32,768 tokens | Recorded configuration/job |
| [result-bc968ac0b3c17899deac](../observations.json)<br>source-6c341ac102f58085bbec4ce5.json<br>`/after_cold` | [glm53-validation](glm53-validation.md) | test outcome | Outcome unspecified | context=32,768 tokens | Recorded configuration/job |
| [result-bf01d893ee5f400c451c](../observations.json)<br>source-fc8bbcd8800846bb2de74301.json<br>`/after_cold` | [glm53-validation](glm53-validation.md) | test outcome | Outcome unspecified | context=32,768 tokens | Recorded configuration/job |
| [result-cbefcb634a528df7dcd6](../observations.json)<br>source-a0e99d6d3e3d7f7faa2ba981.json<br>`/runs/0/cold` | [glm53-validation](glm53-validation.md) | test outcome | Outcome unspecified | end_to_end_output_tps=23.59 accepted tokens/s; generated_tokens=4,096 accepted tokens; wall_seconds=173.65 s | Recorded configuration/job |
| [result-d062b00fe0b6de6aec68](../observations.json)<br>source-6719dd0517a962852e39565e.json<br>`/last_runtime` | [glm53-validation](glm53-validation.md) | test outcome | Outcome unspecified | context=32,768 tokens | Recorded configuration/job |
| [result-d104b3393102f7762ad1](../observations.json)<br>source-3b34047c4abe6cdbf63a25d5.json<br>`/last_runtime/cache` | [glm53-validation](glm53-validation.md) | test outcome | Outcome unspecified | cached_tokens=115,200 tokens | Recorded configuration/job |
| [result-d3cebac7dff98c3fa6ba](../observations.json)<br>source-1daed8883b7352c1efcb8c5b.json<br>`/last_runtime` | [glm53-validation](glm53-validation.md) | test outcome | Outcome unspecified | context=32,768 tokens | Recorded configuration/job |
| [result-daee41a04d5c1a01c7b7](../observations.json)<br>source-3df404ff157f9a1bc90a8f93.json<br>`/runs/2/cold` | [glm53-validation](glm53-validation.md) | test outcome | Outcome unspecified | end_to_end_output_tps=29.37 accepted tokens/s; generated_tokens=4,096 accepted tokens; wall_seconds=139.47 s | Recorded configuration/job |
| [result-dcd585abd3babd9e8171](../observations.json)<br>source-fc8bbcd8800846bb2de74301.json<br>`/after_cold/cache` | [glm53-validation](glm53-validation.md) | test outcome | Outcome unspecified | cached_tokens=117,248 tokens | Recorded configuration/job |
| [result-dd20da1515a6d491b776](../observations.json)<br>source-32696c46d8371d817ee2a9e2.json<br>`/runs/1/cold` | [glm53-validation](glm53-validation.md) | test outcome | Outcome unspecified | end_to_end_output_tps=28.45 accepted tokens/s; generated_tokens=4,096 accepted tokens; wall_seconds=143.97 s | Recorded configuration/job |
| [result-df7be760fb8e535236d1](../observations.json)<br>source-e86353c4cbb88440f301c9d4.json<br>`/after_cold/totals` | [glm53-validation](glm53-validation.md) | context allocation | Outcome unspecified | cached_tokens=0 tokens; generated_tokens=4,096 accepted tokens; prompt_tokens=107,300 tokens; recurrent_restores=0 checkpoints | Recorded configuration/job |
| [result-e52687d489b811eedf10](../observations.json)<br>source-315936d4a87c80ae09ebaa69.json<br>`/after_cold/cache` | [glm53-validation](glm53-validation.md) | test outcome | Outcome unspecified | cached_tokens=17,408 tokens | Recorded configuration/job |
| [result-e53e94709f8aa2a7489c](../observations.json)<br>source-00c96d2509bab19c756bd94d.json<br>`/after_cold/cache` | [glm53-validation](glm53-validation.md) | test outcome | Outcome unspecified | cached_tokens=110,592 tokens | Recorded configuration/job |
| [result-ea5a05fc12d9b1bc36c4](../observations.json)<br>source-a0e99d6d3e3d7f7faa2ba981.json<br>`/runs/1/cold` | [glm53-validation](glm53-validation.md) | test outcome | Outcome unspecified | end_to_end_output_tps=24.75 accepted tokens/s; generated_tokens=4,096 accepted tokens; wall_seconds=165.51 s | Recorded configuration/job |
| [result-ef301aecb7790267db30](../observations.json)<br>source-d3112726a56ed4a4b24689a2.json<br>`/after_cold/cache` | [glm53-validation](glm53-validation.md) | test outcome | Outcome unspecified | cached_tokens=124,416 tokens | Recorded configuration/job |
| [result-f2e2c461144894231a58](../observations.json)<br>source-6b252527b8bac27878e5516a.json<br>`/after_cold/cache` | [glm53-validation](glm53-validation.md) | test outcome | Outcome unspecified | cached_tokens=124,416 tokens | Recorded configuration/job |
| [result-f5d54f7697531e036e95](../observations.json)<br>source-6b252527b8bac27878e5516a.json<br>`/after_cold` | [glm53-validation](glm53-validation.md) | test outcome | Outcome unspecified | context=32,768 tokens | Recorded configuration/job |
| [result-f7006aef3cd274eb5f57](../observations.json)<br>source-fc8bbcd8800846bb2de74301.json<br>`/after_burst` | [glm53-validation](glm53-validation.md) | test outcome | Outcome unspecified | context=32,768 tokens | Recorded configuration/job |
| [result-f896e7ae054b32c533a2](../observations.json)<br>source-3df404ff157f9a1bc90a8f93.json<br>`/runs/1/warm` | [glm53-validation](glm53-validation.md) | test outcome | Outcome unspecified | end_to_end_output_tps=59.63 accepted tokens/s; generated_tokens=4,096 accepted tokens; wall_seconds=68.69 s | Recorded configuration/job |
| [result-f8ad8e2ff129d5496557](../observations.json)<br>source-84a296f9a57b3e4e910a7a5f.json<br>`/` | [glm53-validation](glm53-validation.md) | context allocation | Pass | compact_tokens=26,214 tokens; context_tokens=32,768 tokens | Recorded configuration/job |
| [result-fc09b9406a377cdf75bb](../observations.json)<br>source-a0e99d6d3e3d7f7faa2ba981.json<br>`/runs/2/cold` | [glm53-validation](glm53-validation.md) | test outcome | Outcome unspecified | end_to_end_output_tps=27.82 accepted tokens/s; generated_tokens=4,096 accepted tokens; wall_seconds=147.21 s | Recorded configuration/job |
| [result-fdf554fd3f43f7eae821](../observations.json)<br>source-dc86404f4933c4b5539c47b9.json<br>`/after_cold/cache` | [glm53-validation](glm53-validation.md) | test outcome | Outcome unspecified | cached_tokens=124,416 tokens | Recorded configuration/job |
| [result-ffbdf83dbed3e1ed4331](../observations.json)<br>source-e86353c4cbb88440f301c9d4.json<br>`/after_cold` | [glm53-validation](glm53-validation.md) | test outcome | Outcome unspecified | context=32,768 tokens | Recorded configuration/job |

These are saved result records, including failures and bounded checks. Copies, individual requests, report summaries and regrading can overlap; their counts are not independent test repetitions. Open each result for exact values, units, configuration binding and source receipts.

There are 8 retained lifecycle records. Their states, exit codes and configuration IDs remain in [catalog.json](../catalog.json); they do not supply missing benchmark results.

[Full archive](../../README.md) | [All retained waves](../RESULTS.md) | [Data definitions](../DATA.md) | [Recommended recipes](../../../README.md)
