# qwen38-validation

**Historical record. Legacy / incomplete measurements.**

Model family: Qwen 3.8 27B.

Recorded archive reason: Fit, pilot or control configuration; measured serving variants have separate records.

Historical configurations are provided for comparison. The [recommended recipes](../../../README.md) include supported launch scripts.

Current recipes using the same recorded checkpoint repository: [qwen3.8-27b-exl3](../../../recipes/qwen3.8-27b-exl3/README.md). Context, cache and runtime versions can differ.

## Saved Configuration Versions

Each configuration ID identifies a distinct original settings record. Deployment fields are omitted; versions can have identical published settings after that omission. Upstream runtime commits remain unspecified where the source retained only an integration label.

| Configuration | Recorded artifact / source | Configured card counts | Context tokens | GPU pool tokens | Slots | Draft mode / tokens |
| --- | --- | --- | --- | --- | --- | --- |
| cfg-0a1fcb6e740cc5bdefcc | [turboderp/Qwen3.8-27B-exl3@9e4c23cfb2](https://huggingface.co/turboderp/Qwen3.8-27B-exl3/tree/9e4c23cfb23697165b8e2f6da2a1df995f66353c) | 1 | 32,768 | 131,072 | 8 | mtp / 3 |
| cfg-148a997df4dfa7b4d8ef | [turboderp/Qwen3.8-27B-exl3@9e4c23cfb2](https://huggingface.co/turboderp/Qwen3.8-27B-exl3/tree/9e4c23cfb23697165b8e2f6da2a1df995f66353c) | 1 | 32,768 | 131,072 | 8 | mtp / 3 |
| cfg-3305c906590c2b5effd5 | [turboderp/Qwen3.8-27B-exl3@9e4c23cfb2](https://huggingface.co/turboderp/Qwen3.8-27B-exl3/tree/9e4c23cfb23697165b8e2f6da2a1df995f66353c) | 1 | 32,768 | 131,072 | 8 | mtp / 3 |
| cfg-5cdb39c85d3b5c1028cb | [turboderp/Qwen3.8-27B-exl3@9e4c23cfb2](https://huggingface.co/turboderp/Qwen3.8-27B-exl3/tree/9e4c23cfb23697165b8e2f6da2a1df995f66353c) | 1 | 32,768 | 131,072 | 8 | mtp / 3 |
| cfg-83a31336ae0a769fba61 | [turboderp/Qwen3.8-27B-exl3@9e4c23cfb2](https://huggingface.co/turboderp/Qwen3.8-27B-exl3/tree/9e4c23cfb23697165b8e2f6da2a1df995f66353c) | 1 | 32,768 | 131,072 | 8 | mtp / 3 |

Card counts are saved configuration choices, not a claim that every allowed placement was measured. A derived view can differ from its pinned download source.

<details>
<summary>cfg-0a1fcb6e740cc5bdefcc</summary>

```json
{
  "kind": "tabby",
  "gpu_counts": [
    1
  ],
  "context": 32768,
  "cache_tokens": 131072,
  "cache_mode": "Q8",
  "draft_cache_mode": "Q8",
  "draft_mode": "mtp",
  "draft_tokens": 3,
  "max_sessions": 8,
  "chunk_size": 2048,
  "reserve_mib": 4096,
  "ram_kv_mib": 4096,
  "ram_recurrent_mib": 4096,
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
  "served_model_label": "qwen3.8-27b",
  "power_watts_values_unordered": []
}
```

Pinned model revision recorded: yes. Source receipt labels, hashes and object locators are retained in [configurations.json](../configurations.json).

</details>

<details>
<summary>cfg-148a997df4dfa7b4d8ef</summary>

```json
{
  "kind": "tabby",
  "gpu_counts": [
    1
  ],
  "context": 32768,
  "cache_tokens": 131072,
  "cache_mode": "Q8",
  "draft_cache_mode": "Q8",
  "draft_mode": "mtp",
  "draft_tokens": 3,
  "max_sessions": 8,
  "chunk_size": 2048,
  "reserve_mib": 4096,
  "ram_kv_mib": 4096,
  "ram_recurrent_mib": 4096,
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

<details>
<summary>cfg-3305c906590c2b5effd5</summary>

```json
{
  "kind": "tabby",
  "gpu_counts": [
    1
  ],
  "context": 32768,
  "cache_tokens": 131072,
  "cache_mode": "Q8",
  "draft_cache_mode": "Q8",
  "draft_mode": "mtp",
  "draft_tokens": 3,
  "max_sessions": 8,
  "chunk_size": 2048,
  "reserve_mib": 4096,
  "ram_kv_mib": 4096,
  "ram_recurrent_mib": 4096,
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

<details>
<summary>cfg-5cdb39c85d3b5c1028cb</summary>

```json
{
  "kind": "tabby",
  "gpu_counts": [
    1
  ],
  "context": 32768,
  "cache_tokens": 131072,
  "cache_mode": "Q8",
  "draft_cache_mode": "Q8",
  "draft_mode": "mtp",
  "draft_tokens": 3,
  "max_sessions": 8,
  "chunk_size": 2048,
  "reserve_mib": 4096,
  "ram_kv_mib": 4096,
  "ram_recurrent_mib": 4096,
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

<details>
<summary>cfg-83a31336ae0a769fba61</summary>

```json
{
  "kind": "tabby",
  "gpu_counts": [
    1
  ],
  "context": 32768,
  "cache_tokens": 131072,
  "cache_mode": "Q8",
  "draft_cache_mode": "Q8",
  "draft_mode": "mtp",
  "draft_tokens": 3,
  "max_sessions": 8,
  "chunk_size": 2048,
  "reserve_mib": 4096,
  "ram_kv_mib": 4096,
  "ram_recurrent_mib": 4096,
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

| Profile / Wave | Layout; Draft / Tokens | Requests | Input tokens/request | Accepted output tokens/request | Cache / Reused input tokens | Context / GPU pool tokens | Shared decode tok/s total | Client after-first-token estimate tok/s | Whole-wave output tok/s | Median TTFT, s | Source report |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [qwen38-validation](qwen38-validation.md)<br>wave-158be43787d70aeb3e1d | layout unspecified; mtp / 3 | 4 | 24,636 | 128 | cold; reused 0 | 32,768 / 131,072 | Not recorded | 109.61 | 8.89 | 53.48 | Pass |
| [qwen38-validation](qwen38-validation.md)<br>wave-447dd92d263562ac954e | layout unspecified; mtp / 3 | 4 | 24,635 | 126 to 128 | cold; reused 0 | 32,768 / 131,072 | Not recorded | 123.06 | 8.87 | 53.46 | Failed / partial |
| [qwen38-validation](qwen38-validation.md)<br>wave-5c9ba3f4af375282f22a | layout unspecified; mtp / 3 | 8 | 2,069 to 8,206 | 256 | cold; reused 0 | 32,768 / 131,072 | Not recorded | 164.94 | 56.62 | 23.88 | Pass |
| [qwen38-validation](qwen38-validation.md)<br>wave-b1e28ff1fcc8b60a2b9f | layout unspecified; mtp / 3 | 8 | 2,352 to 8,489 | 256 | cached_prefix; reused 2,048 to 8,192 | 32,768 / 131,072 | Not recorded | 138.83 | 113.44 | 6.32 | Pass |
| [qwen38-validation](qwen38-validation.md)<br>wave-de008430a2f8abb85ab7 | layout unspecified; mtp / 3 | 4 | 24,783 | 35 | cached_prefix; reused 24,576 | 32,768 / 131,072 | Not recorded | 35.58 | 27.37 | 4.43 | Pass |
| [qwen38-validation](qwen38-validation.md)<br>wave-f63827cf0047fa56ee4b | layout unspecified; mtp / 3 | 4 | 24,779 to 24,782 | 35 | repeated_input; reused 0 to 24,576 | 32,768 / 131,072 | Not recorded | 3.22 | 3.13 | 44.00 | Failed / partial |

Rates are whole-wave totals over the stated request count. A wave may span multiple independent model instances; [measurements.json](../measurements.json) retains their contributions and the exact configuration IDs. Do not interpret a multi-instance total as one card's rate.

A dash in shared decode means no qualified synchronized interval is available. Whole-wave throughput includes prefill and queueing. A valid decode interval can survive inside an overall failed or partial check; the source-report outcome is preserved. No rows are averaged.

## Bounded Checks

| Check | Reported outcome | Retained counts / flags |
| --- | --- | --- |
| check-11e49f0684a5e1b5785d | Pass | {"passed":true} |
| check-20fb578ef0faebb7ac93 | Pass | {"passed":true} |
| check-2b8833469bdfc71784e5 | Pass | {"passed":true,"input_tokens":[8202,8202,4098,4098,2065,2065,2065,2065]} |
| check-3793c3c2bd15ce834e0e | Pass | {"passed":true,"replayed_history_tokens":[60,60,60,60],"input_tokens":[24632,24632,24632,24632]} |
| check-5f33f9c444c1e6786b5d | Failed / partial | {"passed":false,"input_tokens":[24631,24631,24631,24631]} |
| check-6ae4c2715898f5d63bc4 | Pass | {"passed":true} |
| check-af22f7b13206472c84d0 | Pass | {"passed":true} |
| check-cf63322c56ddfa6d9eda | Failed / partial | {"passed":false,"replayed_history_tokens":[59,24635],"input_tokens":[24631,24631,24631,24631]} |

These checks retain their reported scope. A context/allocation/retrieval check is not a general quality score or a speed qualification at that context. Exact flags and provenance are in [checks.json](../checks.json).

## Additional Test Results

| Result / Source | Profile | Evidence type | Reported outcome | Retained values | Configuration binding |
| --- | --- | --- | --- | --- | --- |
| [result-0a234cb0e9e63513a90a](../observations.json)<br>source-386ba962dd4c5680c463365b.json<br>`/after_cold/totals` | [qwen38-validation](qwen38-validation.md) | context allocation | Outcome unspecified | cached_tokens=768 tokens; generated_tokens=2,419 accepted tokens; prompt_tokens=34,782 tokens; recurrent_restores=3 checkpoints | Recorded configuration/job |
| [result-20e9f84d64a9cc236b90](../observations.json)<br>source-538f11b625d5bdbd332995ef.json<br>`/after_cold/cache` | [qwen38-validation](qwen38-validation.md) | test outcome | Outcome unspecified | cached_tokens=98,304 tokens | Recorded configuration/job |
| [result-2f10c14ed587910780f0](../observations.json)<br>source-57657f8008c7f3111de918b6.json<br>`/after_burst/totals` | [qwen38-validation](qwen38-validation.md) | context allocation | Outcome unspecified | cached_tokens=0 tokens; generated_tokens=768 accepted tokens; prompt_tokens=230,136 tokens; recurrent_restores=0 checkpoints | Recorded configuration/job |
| [result-3f4f7fd7d3533fdc9d81](../observations.json)<br>source-538f11b625d5bdbd332995ef.json<br>`/after_burst` | [qwen38-validation](qwen38-validation.md) | test outcome | Outcome unspecified | context=32,768 tokens | Recorded configuration/job |
| [result-47e37a8126746cd45f78](../observations.json)<br>source-57657f8008c7f3111de918b6.json<br>`/after_burst` | [qwen38-validation](qwen38-validation.md) | test outcome | Outcome unspecified | context=32,768 tokens | Recorded configuration/job |
| [result-4fe4387187a72e4d402d](../observations.json)<br>source-386ba962dd4c5680c463365b.json<br>`/after_cold/cache` | [qwen38-validation](qwen38-validation.md) | test outcome | Outcome unspecified | cached_tokens=35,072 tokens | Recorded configuration/job |
| [result-5699492ecc9e179d7660](../observations.json)<br>source-538f11b625d5bdbd332995ef.json<br>`/after_burst/cache` | [qwen38-validation](qwen38-validation.md) | test outcome | Outcome unspecified | cached_tokens=129,280 tokens | Recorded configuration/job |
| [result-777b2194879dd62d1d49](../observations.json)<br>source-57657f8008c7f3111de918b6.json<br>`/after_cold/totals` | [qwen38-validation](qwen38-validation.md) | context allocation | Outcome unspecified | cached_tokens=0 tokens; generated_tokens=512 accepted tokens; prompt_tokens=98,544 tokens; recurrent_restores=0 checkpoints | Recorded configuration/job |
| [result-79bc00452555e3005373](../observations.json)<br>source-538f11b625d5bdbd332995ef.json<br>`/after_cold/totals` | [qwen38-validation](qwen38-validation.md) | context allocation | Outcome unspecified | cached_tokens=0 tokens; generated_tokens=510 accepted tokens; prompt_tokens=98,540 tokens; recurrent_restores=0 checkpoints | Recorded configuration/job |
| [result-980c73538e258283e5ba](../observations.json)<br>source-538f11b625d5bdbd332995ef.json<br>`/after_cold` | [qwen38-validation](qwen38-validation.md) | test outcome | Outcome unspecified | context=32,768 tokens | Recorded configuration/job |
| [result-a0c108d239ba938b51f8](../observations.json)<br>source-386ba962dd4c5680c463365b.json<br>`/after_cold` | [qwen38-validation](qwen38-validation.md) | test outcome | Outcome unspecified | context=32,768 tokens | Recorded configuration/job |
| [result-ba756d28aa542e85c2c4](../observations.json)<br>source-57657f8008c7f3111de918b6.json<br>`/after_cold` | [qwen38-validation](qwen38-validation.md) | test outcome | Outcome unspecified | context=32,768 tokens | Recorded configuration/job |
| [result-e9b597985a6db4455b42](../observations.json)<br>source-538f11b625d5bdbd332995ef.json<br>`/after_burst/totals` | [qwen38-validation](qwen38-validation.md) | context allocation | Outcome unspecified | cached_tokens=0 tokens; generated_tokens=766 accepted tokens; prompt_tokens=230,124 tokens; recurrent_restores=0 checkpoints | Recorded configuration/job |

These are saved result records, including failures and bounded checks. Copies, individual requests, report summaries and regrading can overlap; their counts are not independent test repetitions. Open each result for exact values, units, configuration binding and source receipts.

There are 10 retained lifecycle records. Their states, exit codes and configuration IDs remain in [catalog.json](../catalog.json); they do not supply missing benchmark results.

[Full archive](../../README.md) | [All retained waves](../RESULTS.md) | [Data definitions](../DATA.md) | [Recommended recipes](../../../README.md)
