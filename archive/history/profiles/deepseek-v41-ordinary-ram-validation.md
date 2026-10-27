# deepseek-v41-ordinary-ram-validation

**Historical record. Bounded checks only.**

Model family: DeepSeek.

Historical configurations are provided for comparison. The [recommended recipes](../../../README.md) include supported launch scripts.

Current recipes using the same recorded checkpoint repository: [deepseek-v41-flash-dspark5-tp3](../../../recipes/deepseek-v41-flash-dspark5-tp3/README.md). Context, cache and runtime versions can differ.

## Saved Configuration Versions

Each configuration ID identifies a distinct original settings record. Deployment fields are omitted; versions can have identical published settings after that omission. Upstream runtime commits remain unspecified where the source retained only an integration label.

| Configuration | Recorded artifact / source | Configured card counts | Context tokens | GPU pool tokens | Slots | Draft mode / tokens |
| --- | --- | --- | --- | --- | --- | --- |
| cfg-090bf1ab4cd380f0618c | [sfxnz/DeepSeek-V4.1-Flash-EXL3@982b70452f](https://huggingface.co/sfxnz/DeepSeek-V4.1-Flash-EXL3/tree/982b70452f399814f56b46272fd30394ae10d58c) | 3 | 32,768 | Not recorded | 4 | disabled / 5 |
| cfg-b81ba37cc5d35fd09840 | [sfxnz/DeepSeek-V4.1-Flash-EXL3@982b70452f](https://huggingface.co/sfxnz/DeepSeek-V4.1-Flash-EXL3/tree/982b70452f399814f56b46272fd30394ae10d58c) | 3 | 32,768 | Not recorded | 4 | disabled / 5 |
| cfg-cea610810f59f756b971 | [sfxnz/DeepSeek-V4.1-Flash-EXL3@982b70452f](https://huggingface.co/sfxnz/DeepSeek-V4.1-Flash-EXL3/tree/982b70452f399814f56b46272fd30394ae10d58c) | 3 | 32,768 | Not recorded | 4 | disabled / 5 |

Card counts are saved configuration choices, not a claim that every allowed placement was measured. A derived view can differ from its pinned download source.

<details>
<summary>cfg-090bf1ab4cd380f0618c</summary>

```json
{
  "kind": "vllm_native",
  "gpu_counts": [
    3
  ],
  "context": 32768,
  "kv_dtype": "auto",
  "draft_mode": "disabled",
  "draft_tokens": 5,
  "max_sessions": 4,
  "chunk_size": 1280,
  "ram_kv_mib": 8192,
  "power_watts": 200,
  "host_memory_gib": 80,
  "host_swap_gib": 0,
  "min_vram_mib_per_gpu": 65530,
  "min_effective_vram_mib": 196000,
  "kv_cache_mib_per_gpu": 1024,
  "engram_row_cache_mib": 64,
  "enforce_eager": true,
  "batch_invariant": true,
  "prefix_match_unit": 8,
  "model_repository": "sfxnz/DeepSeek-V4.1-Flash-EXL3",
  "model_revision": "982b70452f399814f56b46272fd30394ae10d58c",
  "draft_repository": null,
  "draft_revision": null,
  "recorded_runtime_label": "deepseek-v41-sm80-r2",
  "served_model_label": "deepseek-v4.1-flash"
}
```

Pinned model revision recorded: yes. Source receipt labels, hashes and object locators are retained in [configurations.json](../configurations.json).

</details>

<details>
<summary>cfg-b81ba37cc5d35fd09840</summary>

```json
{
  "kind": "vllm_native",
  "gpu_counts": [
    3
  ],
  "context": 32768,
  "kv_dtype": "auto",
  "draft_mode": "disabled",
  "draft_tokens": 5,
  "max_sessions": 4,
  "chunk_size": 1280,
  "ram_kv_mib": 8192,
  "power_watts": 200,
  "host_memory_gib": 80,
  "host_swap_gib": 0,
  "min_vram_mib_per_gpu": 65530,
  "min_effective_vram_mib": 196000,
  "kv_cache_mib_per_gpu": 256,
  "engram_row_cache_mib": 64,
  "enforce_eager": true,
  "batch_invariant": true,
  "prefix_match_unit": 8,
  "model_repository": "sfxnz/DeepSeek-V4.1-Flash-EXL3",
  "model_revision": "982b70452f399814f56b46272fd30394ae10d58c",
  "draft_repository": null,
  "draft_revision": null,
  "recorded_runtime_label": "deepseek-v41-sm80-r2",
  "served_model_label": "deepseek-v4.1-flash"
}
```

Pinned model revision recorded: yes. Source receipt labels, hashes and object locators are retained in [configurations.json](../configurations.json).

</details>

<details>
<summary>cfg-cea610810f59f756b971</summary>

```json
{
  "kind": "vllm_native",
  "gpu_counts": [
    3
  ],
  "context": 32768,
  "kv_dtype": "auto",
  "draft_mode": "disabled",
  "draft_tokens": 5,
  "max_sessions": 4,
  "chunk_size": 1280,
  "ram_kv_mib": 8192,
  "power_watts": 200,
  "host_memory_gib": 80,
  "host_swap_gib": 0,
  "min_vram_mib_per_gpu": 65530,
  "min_effective_vram_mib": 196000,
  "kv_cache_mib_per_gpu": 1024,
  "engram_row_cache_mib": 64,
  "enforce_eager": true,
  "prefix_match_unit": 8,
  "model_repository": "sfxnz/DeepSeek-V4.1-Flash-EXL3",
  "model_revision": "982b70452f399814f56b46272fd30394ae10d58c",
  "draft_repository": null,
  "draft_revision": null,
  "recorded_runtime_label": "deepseek-v41-sm80-r2",
  "served_model_label": "deepseek-v4.1-flash"
}
```

Pinned model revision recorded: yes. Source receipt labels, hashes and object locators are retained in [configurations.json](../configurations.json).

</details>

## Retained Measurements

No detailed benchmark receipt is matched to this record. A saved definition or a successful job exit alone is not a performance measurement.

A dash in shared decode means no qualified synchronized interval is available. Whole-wave throughput includes prefill and queueing. A valid decode interval can survive inside an overall failed or partial check; the source-report outcome is preserved. No rows are averaged.

## Bounded Checks

| Check | Reported outcome | Retained counts / flags |
| --- | --- | --- |
| check-0adb25df9049a59d63e0 | Failed / partial | {"passed":false,"ram_restoration_qualified":false} |
| check-1e00a4c6bab7ba1e799e | Failed / partial | {"passed":false,"ram_restoration_qualified":false} |
| check-822ebac4b7f0babccce7 | Failed / partial | {"passed":false,"ram_restoration_qualified":false} |
| check-cca2e7c787e65f603531 | Failed / partial | {"passed":false,"ram_restoration_qualified":false} |
| check-f0af7cdd6658f2d5121e | Pass | {"passed":true,"ram_restoration_qualified":true} |

These checks retain their reported scope. A context/allocation/retrieval check is not a general quality score or a speed qualification at that context. Exact flags and provenance are in [checks.json](../checks.json).

## Additional Test Results

| Result / Source | Profile | Evidence type | Reported outcome | Retained values | Configuration binding |
| --- | --- | --- | --- | --- | --- |
| [result-36bef71f70237f237d2d](../observations.json)<br>source-f6b75dacb0690c7df8cc90f1.json<br>`/jobs/0` | [deepseek-v41-ordinary-ram-validation](deepseek-v41-ordinary-ram-validation.md) | test outcome | Failed / partial | passed=false | Recorded configuration/job |
| [result-415813e9c0e02cf6559e](../observations.json)<br>source-db42c511d435997022631690.json<br>`/` | [deepseek-v41-ordinary-ram-validation](deepseek-v41-ordinary-ram-validation.md) | test outcome | Failed / partial | ram_restoration_qualified=false | Recorded configuration/job |
| [result-4c973091edd9a269fce9](../observations.json)<br>source-cd7066ee034c0c69bc01e31f.json<br>`/phases/1` | [deepseek-v41-ordinary-ram-validation](deepseek-v41-ordinary-ram-validation.md) | test outcome | Failed / partial | passed=false | Recorded configuration/job |
| [result-5eaf36c7e374cb7a4712](../observations.json)<br>source-c3fec74d3057f8de78f4e905.json<br>`/` | [deepseek-v41-ordinary-ram-validation](deepseek-v41-ordinary-ram-validation.md) | test outcome | Pass | passed=true; ram_restoration_qualified=true | Recorded configuration/job |
| [result-777f4ab8e621f15ecf84](../observations.json)<br>source-cacd3ff2d56445bae2740142.json<br>`/phases/0` | [deepseek-v41-ordinary-ram-validation](deepseek-v41-ordinary-ram-validation.md) | test outcome | Failed / partial | passed=false | Recorded configuration/job |
| [result-979204741b4e730ea186](../observations.json)<br>source-598259b97d00073d18a4a92c.json<br>`/` | [deepseek-v41-ordinary-ram-validation](deepseek-v41-ordinary-ram-validation.md) | test outcome | Failed / partial | ram_restoration_qualified=false | Recorded configuration/job |
| [result-a154661c1248f2bf149b](../observations.json)<br>source-cacd3ff2d56445bae2740142.json<br>`/` | [deepseek-v41-ordinary-ram-validation](deepseek-v41-ordinary-ram-validation.md) | test outcome | Failed / partial | ram_restoration_qualified=false | Recorded configuration/job |
| [result-b1f6526b53d3f5efe71d](../observations.json)<br>source-c0031b8cc3011894b9cbb285.json<br>`/jobs/2` | [deepseek-v41-ordinary-ram-validation](deepseek-v41-ordinary-ram-validation.md) | test outcome | Failed / partial | passed=false | Recorded configuration/job |
| [result-bd8d0d39e363abb5dc58](../observations.json)<br>source-8e1cf7d0cfceaf592806034b.json<br>`/jobs/3` | [deepseek-v41-ordinary-ram-validation](deepseek-v41-ordinary-ram-validation.md) | test outcome | Failed / partial | passed=false | Recorded configuration/job |
| [result-c376533d47af5487327b](../observations.json)<br>source-cd7066ee034c0c69bc01e31f.json<br>`/` | [deepseek-v41-ordinary-ram-validation](deepseek-v41-ordinary-ram-validation.md) | test outcome | Failed / partial | ram_restoration_qualified=false | Recorded configuration/job |
| [result-eeb51383e4dbce9c4368](../observations.json)<br>source-96b9a6f1a141638910e5aaa8.json<br>`/jobs/2` | [deepseek-v41-ordinary-ram-validation](deepseek-v41-ordinary-ram-validation.md) | test outcome | Failed / partial | passed=false | Recorded configuration/job |
| [result-fb4e96eb0f262cb8efb9](../observations.json)<br>source-db42c511d435997022631690.json<br>`/phases/1` | [deepseek-v41-ordinary-ram-validation](deepseek-v41-ordinary-ram-validation.md) | test outcome | Failed / partial | passed=false | Recorded configuration/job |

These are saved result records, including failures and bounded checks. Copies, individual requests, report summaries and regrading can overlap; their counts are not independent test repetitions. Open each result for exact values, units, configuration binding and source receipts.

There are 5 retained lifecycle records. Their states, exit codes and configuration IDs remain in [catalog.json](../catalog.json); they do not supply missing benchmark results.

[Full archive](../../README.md) | [All retained waves](../RESULTS.md) | [Data definitions](../DATA.md) | [Recommended recipes](../../../README.md)
