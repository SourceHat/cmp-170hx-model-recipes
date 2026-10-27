# qwen-flash-next-fp8-mtp-validation

**Historical record. Bounded checks only.**

Model family: Qwen 3.8 Flash Next.

Historical configurations are provided for comparison. The [recommended recipes](../../../README.md) include supported launch scripts.

## Saved Configuration Versions

Each configuration ID identifies a distinct original settings record. Deployment fields are omitted; versions can have identical published settings after that omission. Upstream runtime commits remain unspecified where the source retained only an integration label.

| Configuration | Recorded artifact / source | Configured card counts | Context tokens | GPU pool tokens | Slots | Draft mode / tokens |
| --- | --- | --- | --- | --- | --- | --- |
| cfg-eaff495f058dd36e47cc | [Qwen/Qwen3.8-Flash-Next-FP8@236dfdf285](https://huggingface.co/Qwen/Qwen3.8-Flash-Next-FP8/tree/236dfdf285828023ca3bcd3f37366c58a3469b13) | 3 | 32,768 | Not recorded | 4 | mtp / 3 |

Card counts are saved configuration choices, not a claim that every allowed placement was measured. A derived view can differ from its pinned download source.

<details>
<summary>cfg-eaff495f058dd36e47cc</summary>

```json
{
  "kind": "vllm_qwen",
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
  "pipeline_parallel_size": 3,
  "kv_cache_mib_per_gpu": 1024,
  "enforce_eager": true,
  "mamba_cache_mode": "align",
  "ple_backend": "staged_bf16",
  "model_repository": "Qwen/Qwen3.8-Flash-Next-FP8",
  "model_revision": "236dfdf285828023ca3bcd3f37366c58a3469b13",
  "draft_repository": null,
  "draft_revision": null,
  "recorded_runtime_label": "qwen-fp8-pp3-r1",
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
| check-6ba074ea74eda2025883 | Failed / partial | {"passed":false,"ram_restoration_qualified":false} |
| check-c7ac412e432d965c74e6 | Failed / partial | {"passed":false,"ram_restoration_qualified":false} |

These checks retain their reported scope. A context/allocation/retrieval check is not a general quality score or a speed qualification at that context. Exact flags and provenance are in [checks.json](../checks.json).

## Additional Test Results

| Result / Source | Profile | Evidence type | Reported outcome | Retained values | Configuration binding |
| --- | --- | --- | --- | --- | --- |
| [result-04fb22d37165b6c380f6](../observations.json)<br>source-c5eb7b9c854705a8cf897891.json<br>`/` | [qwen-flash-next-fp8-mtp-validation](qwen-flash-next-fp8-mtp-validation.md) | test outcome | Outcome unspecified | input_tokens=8,197 tokens | Recorded configuration/job |
| [result-2ae490a688c035e0298b](../observations.json)<br>source-a5a100a2e641246819fb7d60.json<br>`/phases/3` | [qwen-flash-next-fp8-mtp-validation](qwen-flash-next-fp8-mtp-validation.md) | test outcome | Failed / partial | passed=false | Recorded configuration/job |
| [result-54ddd1df16e8c7cebe58](../observations.json)<br>source-4d51df5e6fa2b61ef7ad5848.json<br>`/jobs/1` | [qwen-flash-next-fp8-mtp-validation](qwen-flash-next-fp8-mtp-validation.md) | test outcome | Failed / partial | passed=false | Recorded configuration/job |
| [result-5e513c3571da83a22856](../observations.json)<br>source-a5a100a2e641246819fb7d60.json<br>`/` | [qwen-flash-next-fp8-mtp-validation](qwen-flash-next-fp8-mtp-validation.md) | test outcome | Failed / partial | ram_restoration_qualified=false | Recorded configuration/job |
| [result-63cf2cec1e8ef74391bd](../observations.json)<br>source-c5eb7b9c854705a8cf897891.json<br>`/restoration` | [qwen-flash-next-fp8-mtp-validation](qwen-flash-next-fp8-mtp-validation.md) | test outcome | Outcome unspecified | restored_bytes=548,241,408 bytes; restored_external_prefix_tokens=13,312 tokens; stored_bytes_before_return=3,220,918,272 bytes | Recorded configuration/job |
| [result-7bcde9e6e7f550d73710](../observations.json)<br>source-b90d3ae38cb57fb5a57c7c06.json<br>`/` | [qwen-flash-next-fp8-mtp-validation](qwen-flash-next-fp8-mtp-validation.md) | test outcome | Failed / partial | ram_restoration_qualified=false | Recorded configuration/job |
| [result-8b5ca6b95f09d2c655be](../observations.json)<br>source-ebcf423985fc8b2d459431a2.json<br>`/jobs/1` | [qwen-flash-next-fp8-mtp-validation](qwen-flash-next-fp8-mtp-validation.md) | test outcome | Failed / partial | passed=false | Recorded configuration/job |

These are saved result records, including failures and bounded checks. Copies, individual requests, report summaries and regrading can overlap; their counts are not independent test repetitions. Open each result for exact values, units, configuration binding and source receipts.

There are 2 retained lifecycle records. Their states, exit codes and configuration IDs remain in [catalog.json](../catalog.json); they do not supply missing benchmark results.

[Full archive](../../README.md) | [All retained waves](../RESULTS.md) | [Data definitions](../DATA.md) | [Recommended recipes](../../../README.md)
