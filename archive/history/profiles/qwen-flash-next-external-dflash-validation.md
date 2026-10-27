# qwen-flash-next-external-dflash-validation

**Historical record. Decode interval measured.**

Model family: Qwen 3.8 Flash Next.

Historical configurations are provided for comparison. The [recommended recipes](../../../README.md) include supported launch scripts.

## Saved Configuration Versions

Each configuration ID identifies a distinct original settings record. Deployment fields are omitted; versions can have identical published settings after that omission. Upstream runtime commits remain unspecified where the source retained only an integration label.

| Configuration | Recorded artifact / source | Configured card counts | Context tokens | GPU pool tokens | Slots | Draft mode / tokens |
| --- | --- | --- | --- | --- | --- | --- |
| cfg-515986bc4443035d2bc0 | [zankich/Qwen3.8-Flash-Next-W4A16-Merlin-INT4PLE-FP8KV@45d5db34e0](https://huggingface.co/zankich/Qwen3.8-Flash-Next-W4A16-Merlin-INT4PLE-FP8KV/tree/45d5db34e05a826d0ca150d4526bc29fd2958d63) | 3 | 32,768 | Not recorded | 4 | dflash / 5 |
| cfg-7da3add9bcf4c841bc15 | [zankich/Qwen3.8-Flash-Next-W4A16-Merlin-INT4PLE-FP8KV@45d5db34e0](https://huggingface.co/zankich/Qwen3.8-Flash-Next-W4A16-Merlin-INT4PLE-FP8KV/tree/45d5db34e05a826d0ca150d4526bc29fd2958d63) | 3 | 32,768 | Not recorded | 4 | dflash / 5 |

Card counts are saved configuration choices, not a claim that every allowed placement was measured. A derived view can differ from its pinned download source.

<details>
<summary>cfg-515986bc4443035d2bc0</summary>

```json
{
  "kind": "vllm_qwen_external",
  "gpu_counts": [
    3
  ],
  "context": 32768,
  "kv_dtype": "bfloat16",
  "draft_mode": "dflash",
  "draft_tokens": 5,
  "max_sessions": 4,
  "chunk_size": 1280,
  "ram_kv_mib": 8192,
  "power_watts": 200,
  "host_memory_gib": 80,
  "host_swap_gib": 0,
  "min_vram_mib_per_gpu": 65530,
  "min_effective_vram_mib": 196000,
  "tensor_parallel_size": 2,
  "pipeline_parallel_size": 1,
  "kv_cache_mib_per_gpu": 1024,
  "enforce_eager": true,
  "mamba_cache_mode": "align",
  "ple_backend": "pinned_int4",
  "model_repository": "zankich/Qwen3.8-Flash-Next-W4A16-Merlin-INT4PLE-FP8KV",
  "model_revision": "45d5db34e05a826d0ca150d4526bc29fd2958d63",
  "draft_repository": null,
  "draft_revision": "9cd660f9050c92fedc88cbe547bd53af0392abe1",
  "recorded_runtime_label": "qwen-flash-dflash-tp2-r1",
  "served_model_label": "qwen3.8-flash-next"
}
```

Pinned model revision recorded: yes. Source receipt labels, hashes and object locators are retained in [configurations.json](../configurations.json).

</details>

<details>
<summary>cfg-7da3add9bcf4c841bc15</summary>

```json
{
  "kind": "vllm_qwen_external",
  "gpu_counts": [
    3
  ],
  "context": 32768,
  "kv_dtype": "bfloat16",
  "draft_mode": "dflash",
  "draft_tokens": 5,
  "max_sessions": 4,
  "chunk_size": 1280,
  "ram_kv_mib": 8192,
  "power_watts": 200,
  "host_memory_gib": 80,
  "host_swap_gib": 0,
  "min_vram_mib_per_gpu": 65530,
  "min_effective_vram_mib": 196000,
  "tensor_parallel_size": 2,
  "pipeline_parallel_size": 1,
  "kv_cache_mib_per_gpu": 1536,
  "enforce_eager": true,
  "mamba_cache_mode": "align",
  "ple_backend": "pinned_int4",
  "model_repository": "zankich/Qwen3.8-Flash-Next-W4A16-Merlin-INT4PLE-FP8KV",
  "model_revision": "45d5db34e05a826d0ca150d4526bc29fd2958d63",
  "draft_repository": null,
  "draft_revision": "9cd660f9050c92fedc88cbe547bd53af0392abe1",
  "recorded_runtime_label": "qwen-flash-dflash-tp2-r1",
  "served_model_label": "qwen3.8-flash-next"
}
```

Pinned model revision recorded: yes. Source receipt labels, hashes and object locators are retained in [configurations.json](../configurations.json).

</details>

## Retained Measurements

| Profile / Wave | Layout; Draft / Tokens | Requests | Input tokens/request | Accepted output tokens/request | Cache / Reused input tokens | Context / GPU pool tokens | Shared decode tok/s total | Client after-first-token estimate tok/s | Whole-wave output tok/s | Median TTFT, s | Source report |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [qwen-flash-next-external-dflash-validation](qwen-flash-next-external-dflash-validation.md)<br>wave-95dd91efd9d62db760ee | layout unspecified; dflash / 5 | 2 | Not recorded | Not recorded | unspecified; reused - | 32,768 / - | 66.93 | Not recorded | Not recorded | Not recorded | Unspecified |
| [qwen-flash-next-external-dflash-validation](qwen-flash-next-external-dflash-validation.md)<br>wave-d02566205f05c83547fc | layout unspecified; dflash / 5 | 2 | Not recorded | Not recorded | unspecified; reused - | 32,768 / - | 64.86 | Not recorded | Not recorded | Not recorded | Unspecified |

Rates are whole-wave totals over the stated request count. A wave may span multiple independent model instances; [measurements.json](../measurements.json) retains their contributions and the exact configuration IDs. Do not interpret a multi-instance total as one card's rate.

A dash in shared decode means no qualified synchronized interval is available. Whole-wave throughput includes prefill and queueing. A valid decode interval can survive inside an overall failed or partial check; the source-report outcome is preserved. No rows are averaged.

## Reported Rate Summaries

| Summary | Original field | Reported tok/s | Requests | Configuration binding |
| --- | --- | --- | --- | --- |
| summary-d5baa3fef04834455113 | aggregate_generated_tok_s | 65.89 | Not recorded | recorded_summary_context |

These quoted values can overlap detailed waves. A referenced earlier run's rate is not transferred to the citing configuration. Missing input, request and timing-window evidence remains missing. See [rate-summaries.json](../rate-summaries.json).

## Bounded Checks

| Check | Reported outcome | Retained counts / flags |
| --- | --- | --- |
| check-19279e624c98f46a796c | Failed / partial | {"passed":false,"ram_restoration_qualified":false} |
| check-71f70190d6983938c655 | Failed / partial | {"passed":false,"ram_restoration_qualified":false} |
| check-77724490ff818b070d6c | Failed / partial | {"passed":false,"ram_restoration_qualified":false} |
| check-deff6b51ec2dc24ddd54 | Failed / partial | {"passed":false,"ram_restoration_qualified":false} |
| check-dfadad869d2d3d5d92aa | Failed / partial | {"passed":false,"ram_restoration_qualified":false} |
| check-e5f0a85d29847c201e0f | Failed / partial | {"passed":false,"ram_restoration_qualified":false} |
| check-f0d0147519416871aaf6 | Pass | {"passed":true,"ram_restoration_qualified":true} |

These checks retain their reported scope. A context/allocation/retrieval check is not a general quality score or a speed qualification at that context. Exact flags and provenance are in [checks.json](../checks.json).

## Additional Test Results

| Result / Source | Profile | Evidence type | Reported outcome | Retained values | Configuration binding |
| --- | --- | --- | --- | --- | --- |
| [result-0c0a64f6f0e4134a0d9f](../observations.json)<br>source-9d45a6abe8aaad72e7c69ef3.json<br>`/` | [qwen-flash-next-external-dflash-validation](qwen-flash-next-external-dflash-validation.md) | test outcome | Outcome unspecified | aggregate_generated_tok_s=65.89 accepted tokens/s; generated_tokens=1,981 accepted tokens | Recorded configuration/job |
| [result-17a9b6d7eba5d5b49db1](../observations.json)<br>source-8e1cf7d0cfceaf592806034b.json<br>`/jobs/1` | [qwen-flash-next-external-dflash-validation](qwen-flash-next-external-dflash-validation.md) | test outcome | Failed / partial | passed=false | Recorded configuration/job |
| [result-3435d994f38fdb7a58ad](../observations.json)<br>source-513c748682957835083561ab.json<br>`/` | [qwen-flash-next-external-dflash-validation](qwen-flash-next-external-dflash-validation.md) | test outcome | Pass | passed=true; ram_restoration_qualified=true | Recorded configuration/job |
| [result-3ad310fff854a1d398d1](../observations.json)<br>source-17227493eab143c084af7d6c.json<br>`/` | [qwen-flash-next-external-dflash-validation](qwen-flash-next-external-dflash-validation.md) | test outcome | Failed / partial | ram_restoration_qualified=false | Recorded configuration/job |
| [result-471b95d20c6faf30fffb](../observations.json)<br>source-ebcf423985fc8b2d459431a2.json<br>`/jobs/4` | [qwen-flash-next-external-dflash-validation](qwen-flash-next-external-dflash-validation.md) | test outcome | Failed / partial | passed=false | Recorded configuration/job |
| [result-556243000f7e27f5473f](../observations.json)<br>source-303431fbb5541133a214abd6.json<br>`/jobs/0` | [qwen-flash-next-external-dflash-validation](qwen-flash-next-external-dflash-validation.md) | test outcome | Failed / partial | passed=false | Recorded configuration/job |
| [result-6e018d593b8be1eadce8](../observations.json)<br>source-8a100466b54d5356bb553ef4.json<br>`/phases/2` | [qwen-flash-next-external-dflash-validation](qwen-flash-next-external-dflash-validation.md) | test outcome | Failed / partial | passed=false | Recorded configuration/job |
| [result-8ec9c90d1f9d14d74b8a](../observations.json)<br>source-c0031b8cc3011894b9cbb285.json<br>`/jobs/0` | [qwen-flash-next-external-dflash-validation](qwen-flash-next-external-dflash-validation.md) | test outcome | Failed / partial | passed=false | Recorded configuration/job |
| [result-9dad07b92390a9dda029](../observations.json)<br>source-b03b84b60daa6ddd30b907ce.json<br>`/` | [qwen-flash-next-external-dflash-validation](qwen-flash-next-external-dflash-validation.md) | test outcome | Failed / partial | ram_restoration_qualified=false | Recorded configuration/job |
| [result-bfd63ab6ced700588a1f](../observations.json)<br>source-63b2546803cf7e3403ff904e.json<br>`/` | [qwen-flash-next-external-dflash-validation](qwen-flash-next-external-dflash-validation.md) | test outcome | Failed / partial | ram_restoration_qualified=false | Recorded configuration/job |
| [result-c98074f616ea5d21529b](../observations.json)<br>source-8a100466b54d5356bb553ef4.json<br>`/` | [qwen-flash-next-external-dflash-validation](qwen-flash-next-external-dflash-validation.md) | test outcome | Failed / partial | ram_restoration_qualified=false | Recorded configuration/job |
| [result-ce4106330e61e73c4cf2](../observations.json)<br>source-9d45a6abe8aaad72e7c69ef3.json<br>`/waves/1` | [qwen-flash-next-external-dflash-validation](qwen-flash-next-external-dflash-validation.md) | test outcome | Outcome unspecified | generated_tokens=983 accepted tokens | Recorded configuration/job |
| [result-d0f25e08714828ae6bc6](../observations.json)<br>source-c8e8d1cdecf836164a9891f2.json<br>`/` | [qwen-flash-next-external-dflash-validation](qwen-flash-next-external-dflash-validation.md) | test outcome | Failed / partial | ram_restoration_qualified=false | Recorded configuration/job |
| [result-d5453bbc66eb232af141](../observations.json)<br>source-403c5e3ee000b092e66b438d.json<br>`/` | [qwen-flash-next-external-dflash-validation](qwen-flash-next-external-dflash-validation.md) | test outcome | Failed / partial | ram_restoration_qualified=false | Recorded configuration/job |
| [result-ed7e87938d9f85c583bf](../observations.json)<br>source-4d51df5e6fa2b61ef7ad5848.json<br>`/jobs/4` | [qwen-flash-next-external-dflash-validation](qwen-flash-next-external-dflash-validation.md) | test outcome | Failed / partial | passed=false | Recorded configuration/job |
| [result-eea8a876105d789080cf](../observations.json)<br>source-9d45a6abe8aaad72e7c69ef3.json<br>`/waves/0` | [qwen-flash-next-external-dflash-validation](qwen-flash-next-external-dflash-validation.md) | test outcome | Outcome unspecified | generated_tokens=998 accepted tokens | Recorded configuration/job |
| [result-f099024319739375b734](../observations.json)<br>source-f1b421da853c50ada8e61cf2.json<br>`/jobs/0` | [qwen-flash-next-external-dflash-validation](qwen-flash-next-external-dflash-validation.md) | test outcome | Failed / partial | passed=false | Recorded configuration/job |

These are saved result records, including failures and bounded checks. Copies, individual requests, report summaries and regrading can overlap; their counts are not independent test repetitions. Open each result for exact values, units, configuration binding and source receipts.

There are 8 retained lifecycle records. Their states, exit codes and configuration IDs remain in [catalog.json](../catalog.json); they do not supply missing benchmark results.

[Full archive](../../README.md) | [All retained waves](../RESULTS.md) | [Data definitions](../DATA.md) | [Recommended recipes](../../../README.md)
