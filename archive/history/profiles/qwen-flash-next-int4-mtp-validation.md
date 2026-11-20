# qwen-flash-next-int4-mtp-validation

**Historical record. Bounded checks only.**

Model family: Qwen 3.8 Flash Next.

Historical configurations are provided for comparison. The [recommended recipes](../../../README.md) include supported launch scripts.

## Saved Configuration Versions

Each configuration ID identifies a distinct original settings record. Deployment fields are omitted; versions can have identical published settings after that omission. Upstream runtime commits remain unspecified where the source retained only an integration label.

| Configuration | Recorded artifact / source | Configured card counts | Context tokens | GPU pool tokens | Slots | Draft mode / tokens |
| --- | --- | --- | --- | --- | --- | --- |
| cfg-3d839b750c324d70a9f3 | [zankich/Qwen3.8-Flash-Next-W4A16-Merlin-INT4PLE-FP8KV@45d5db34e0](https://huggingface.co/zankich/Qwen3.8-Flash-Next-W4A16-Merlin-INT4PLE-FP8KV/tree/45d5db34e05a826d0ca150d4526bc29fd2958d63) | 3 | 32,768 | Not recorded | 4 | mtp / 3 |

Card counts are saved configuration choices, not a claim that every allowed placement was measured. A derived view can differ from its pinned download source.

<details>
<summary>cfg-3d839b750c324d70a9f3</summary>

```json
{
  "kind": "vllm_qwen_int4",
  "gpu_counts": [
    3
  ],
  "context": 32768,
  "kv_dtype": "bfloat16",
  "draft_mode": "mtp",
  "draft_tokens": 3,
  "max_sessions": 4,
  "chunk_size": 1280,
  "ram_kv_mib": 8192,
  "power_watts": 200,
  "host_memory_gib": 80,
  "host_swap_gib": 0,
  "min_vram_mib_per_gpu": 65530,
  "min_effective_vram_mib": 196000,
  "tensor_parallel_size": 1,
  "pipeline_parallel_size": 2,
  "kv_cache_mib_per_gpu": 1024,
  "enforce_eager": true,
  "mamba_cache_mode": "align",
  "ple_backend": "pinned_int4",
  "model_repository": "zankich/Qwen3.8-Flash-Next-W4A16-Merlin-INT4PLE-FP8KV",
  "model_revision": "45d5db34e05a826d0ca150d4526bc29fd2958d63",
  "draft_repository": null,
  "draft_revision": null,
  "recorded_runtime_label": "qwen-int4-ple-pp2-r1",
  "served_model_label": "qwen3.8-flash-next"
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
| check-1af275cef8e6839cf9e8 | Failed / partial | {"passed":false,"ram_restoration_qualified":false} |
| check-48688f9f82f80605982a | Failed / partial | {"passed":false,"ram_restoration_qualified":false} |
| check-579cae3fb718588574bb | Pass | {"passed":true,"ram_restoration_qualified":true} |
| check-7ac433db2a5a0754b8d3 | Failed / partial | {"passed":false,"ram_restoration_qualified":false} |

These checks retain their reported scope. A context/allocation/retrieval check is not a general quality score or a speed qualification at that context. Exact flags and provenance are in [checks.json](../checks.json).

## Additional Test Results

| Result / Source | Profile | Evidence type | Reported outcome | Retained values | Configuration binding |
| --- | --- | --- | --- | --- | --- |
| [result-0eff48ee7b5fd440fbb5](../observations.json)<br>source-9b4a1340f8c6ed6cb6948ffa.json<br>`/` | [qwen-flash-next-int4-mtp-validation](qwen-flash-next-int4-mtp-validation.md) | test outcome | Failed / partial | ram_restoration_qualified=false | Recorded configuration/job |
| [result-2678299e38d147738fb8](../observations.json)<br>source-ebcf423985fc8b2d459431a2.json<br>`/jobs/3` | [qwen-flash-next-int4-mtp-validation](qwen-flash-next-int4-mtp-validation.md) | test outcome | Failed / partial | passed=false | Recorded configuration/job |
| [result-463c27d3ffe7c531e003](../observations.json)<br>source-3d0698092c93ee69135e71cf.json<br>`/jobs/1` | [qwen-flash-next-int4-mtp-validation](qwen-flash-next-int4-mtp-validation.md) | test outcome | Failed / partial | passed=false | Recorded configuration/job |
| [result-538a6d67bbce2e366ede](../observations.json)<br>source-bbc3edd21fa50aa1c23c4aa7.json<br>`/` | [qwen-flash-next-int4-mtp-validation](qwen-flash-next-int4-mtp-validation.md) | test outcome | Failed / partial | ram_restoration_qualified=false | Recorded configuration/job |
| [result-6f2d7e48262ccfdf126f](../observations.json)<br>source-b79a6beb8c0291f96d784d04.json<br>`/` | [qwen-flash-next-int4-mtp-validation](qwen-flash-next-int4-mtp-validation.md) | test outcome | Failed / partial | ram_restoration_qualified=false | Recorded configuration/job |
| [result-a9f58ee05a9c383db6f0](../observations.json)<br>source-4d51df5e6fa2b61ef7ad5848.json<br>`/jobs/3` | [qwen-flash-next-int4-mtp-validation](qwen-flash-next-int4-mtp-validation.md) | test outcome | Failed / partial | passed=false | Recorded configuration/job |
| [result-af6667253e5760cfe84e](../observations.json)<br>source-162269a6542e67b6d19a77a6.json<br>`/` | [qwen-flash-next-int4-mtp-validation](qwen-flash-next-int4-mtp-validation.md) | test outcome | Pass | passed=true; ram_restoration_qualified=true | Recorded configuration/job |

These are saved result records, including failures and bounded checks. Copies, individual requests, report summaries and regrading can overlap; their counts are not independent test repetitions. Open each result for exact values, units, configuration binding and source receipts.

There are 4 retained lifecycle records. Their states, exit codes and configuration IDs remain in [catalog.json](../catalog.json); they do not supply missing benchmark results.

[Full archive](../../README.md) | [All retained waves](../RESULTS.md) | [Data definitions](../DATA.md) | [Recommended recipes](../../../README.md)
