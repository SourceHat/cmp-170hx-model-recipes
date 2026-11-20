# qwen-flash-next-int4-ordinary-validation

**Historical record. Bounded checks only.**

Model family: Qwen 3.8 Flash Next.

Historical configurations are provided for comparison. The [recommended recipes](../../../README.md) include supported launch scripts.

## Saved Configuration Versions

Each configuration ID identifies a distinct original settings record. Deployment fields are omitted; versions can have identical published settings after that omission. Upstream runtime commits remain unspecified where the source retained only an integration label.

| Configuration | Recorded artifact / source | Configured card counts | Context tokens | GPU pool tokens | Slots | Draft mode / tokens |
| --- | --- | --- | --- | --- | --- | --- |
| cfg-b5cd95d89080588b25e6 | [zankich/Qwen3.8-Flash-Next-W4A16-Merlin-INT4PLE-FP8KV@45d5db34e0](https://huggingface.co/zankich/Qwen3.8-Flash-Next-W4A16-Merlin-INT4PLE-FP8KV/tree/45d5db34e05a826d0ca150d4526bc29fd2958d63) | 3 | 32,768 | Not recorded | 4 | disabled / 3 |

Card counts are saved configuration choices, not a claim that every allowed placement was measured. A derived view can differ from its pinned download source.

<details>
<summary>cfg-b5cd95d89080588b25e6</summary>

```json
{
  "kind": "vllm_qwen_int4",
  "gpu_counts": [
    3
  ],
  "context": 32768,
  "kv_dtype": "bfloat16",
  "draft_mode": "disabled",
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
| check-63bba5c1252eefbcc9a0 | Failed / partial | {"passed":false,"ram_restoration_qualified":false} |
| check-8a166646064ff698d56e | Failed / partial | {"passed":false,"ram_restoration_qualified":false} |
| check-916dcbf68b9d1b7d952b | Pass | {"passed":true,"ram_restoration_qualified":true} |
| check-e26085b24891bd3f74ee | Failed / partial | {"passed":false,"ram_restoration_qualified":false} |

These checks retain their reported scope. A context/allocation/retrieval check is not a general quality score or a speed qualification at that context. Exact flags and provenance are in [checks.json](../checks.json).

## Additional Test Results

| Result / Source | Profile | Evidence type | Reported outcome | Retained values | Configuration binding |
| --- | --- | --- | --- | --- | --- |
| [result-120540f55bb08f44b725](../observations.json)<br>source-4d51df5e6fa2b61ef7ad5848.json<br>`/jobs/2` | [qwen-flash-next-int4-ordinary-validation](qwen-flash-next-int4-ordinary-validation.md) | test outcome | Failed / partial | passed=false | Recorded configuration/job |
| [result-24b89967bb974f1f72f3](../observations.json)<br>source-ebcf423985fc8b2d459431a2.json<br>`/jobs/2` | [qwen-flash-next-int4-ordinary-validation](qwen-flash-next-int4-ordinary-validation.md) | test outcome | Failed / partial | passed=false | Recorded configuration/job |
| [result-af5e052e5b7fc70c93a9](../observations.json)<br>source-d3e02dfdc79e843b9b7aaaae.json<br>`/` | [qwen-flash-next-int4-ordinary-validation](qwen-flash-next-int4-ordinary-validation.md) | test outcome | Failed / partial | ram_restoration_qualified=false | Recorded configuration/job |
| [result-c29927236a660e8fa80e](../observations.json)<br>source-2e4c69e1bd07d0555e870bfa.json<br>`/` | [qwen-flash-next-int4-ordinary-validation](qwen-flash-next-int4-ordinary-validation.md) | test outcome | Pass | passed=true; ram_restoration_qualified=true | Recorded configuration/job |
| [result-c7889df21a6859475dcd](../observations.json)<br>source-62eb640405b353f856b2c5c1.json<br>`/` | [qwen-flash-next-int4-ordinary-validation](qwen-flash-next-int4-ordinary-validation.md) | test outcome | Failed / partial | ram_restoration_qualified=false | Recorded configuration/job |
| [result-c9009745c98b8384f334](../observations.json)<br>source-d12b8ae60fb790c5cab6c4aa.json<br>`/` | [qwen-flash-next-int4-ordinary-validation](qwen-flash-next-int4-ordinary-validation.md) | test outcome | Failed / partial | ram_restoration_qualified=false | Recorded configuration/job |
| [result-e69111007dff988f757b](../observations.json)<br>source-225a7304a5651deaecd85ab4.json<br>`/jobs/0` | [qwen-flash-next-int4-ordinary-validation](qwen-flash-next-int4-ordinary-validation.md) | test outcome | Failed / partial | passed=false | Recorded configuration/job |

These are saved result records, including failures and bounded checks. Copies, individual requests, report summaries and regrading can overlap; their counts are not independent test repetitions. Open each result for exact values, units, configuration binding and source receipts.

There are 4 retained lifecycle records. Their states, exit codes and configuration IDs remain in [catalog.json](../catalog.json); they do not supply missing benchmark results.

[Full archive](../../README.md) | [All retained waves](../RESULTS.md) | [Data definitions](../DATA.md) | [Recommended recipes](../../../README.md)
