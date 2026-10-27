# qwen27-w4-ordinary-single-card-validation

**Historical record. Bounded checks only.**

Model family: Qwen 3.8 27B.

Historical configurations are provided for comparison. The [recommended recipes](../../../README.md) include supported launch scripts.

## Saved Configuration Versions

Each configuration ID identifies a distinct original settings record. Deployment fields are omitted; versions can have identical published settings after that omission. Upstream runtime commits remain unspecified where the source retained only an integration label.

| Configuration | Recorded artifact / source | Configured card counts | Context tokens | GPU pool tokens | Slots | Draft mode / tokens |
| --- | --- | --- | --- | --- | --- | --- |
| cfg-9f9ab014c92e5c1d3f20 | [dbirks/Qwen3.8-27B-W4A16-AutoRound@1f05c441c4](https://huggingface.co/dbirks/Qwen3.8-27B-W4A16-AutoRound/tree/1f05c441c4e64ae0549de44fa9ea5a6d43610314) | 1 | 32,768 | Not recorded | 4 | disabled / 3 |

Card counts are saved configuration choices, not a claim that every allowed placement was measured. A derived view can differ from its pinned download source.

<details>
<summary>cfg-9f9ab014c92e5c1d3f20</summary>

```json
{
  "kind": "vllm_qwen27",
  "gpu_counts": [
    1
  ],
  "context": 32768,
  "kv_dtype": "bfloat16",
  "draft_mode": "disabled",
  "draft_tokens": 3,
  "max_sessions": 4,
  "chunk_size": 1024,
  "ram_kv_mib": 8192,
  "power_watts": 200,
  "host_memory_gib": 24,
  "host_swap_gib": 0,
  "min_vram_mib_per_gpu": 65530,
  "min_effective_vram_mib": 65530,
  "tensor_parallel_size": 1,
  "pipeline_parallel_size": 1,
  "kv_cache_mib_per_gpu": 4096,
  "enforce_eager": true,
  "mamba_cache_mode": "align",
  "model_repository": "dbirks/Qwen3.8-27B-W4A16-AutoRound",
  "model_revision": "1f05c441c4e64ae0549de44fa9ea5a6d43610314",
  "draft_repository": null,
  "draft_revision": null,
  "recorded_runtime_label": "qwen27-vllm-r1",
  "served_model_label": "qwen3.8-27b"
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
| check-0fd52d2a8a80c8dd72b4 | Failed / partial | {"passed":false,"ram_restoration_qualified":false} |
| check-236f3d0c8cbdd56086ed | Failed / partial | {"passed":false,"ram_restoration_qualified":false} |
| check-a6a2780ae6e6835a32ee | Pass | {"passed":true,"ram_restoration_qualified":true} |

These checks retain their reported scope. A context/allocation/retrieval check is not a general quality score or a speed qualification at that context. Exact flags and provenance are in [checks.json](../checks.json).

## Additional Test Results

| Result / Source | Profile | Evidence type | Reported outcome | Retained values | Configuration binding |
| --- | --- | --- | --- | --- | --- |
| [result-1d16888c25d5b5648052](../observations.json)<br>source-8600ee90f3cbd725dabb5179.json<br>`/` | [qwen27-w4-ordinary-single-card-validation](qwen27-w4-ordinary-single-card-validation.md) | test outcome | Failed / partial | ram_restoration_qualified=false | Recorded configuration/job |
| [result-3095bfee195f8aea174a](../observations.json)<br>source-6f8c9f6d334b561d56cfa85b.json<br>`/` | [qwen27-w4-ordinary-single-card-validation](qwen27-w4-ordinary-single-card-validation.md) | test outcome | Failed / partial | ram_restoration_qualified=false | Recorded configuration/job |
| [result-380259888a6b8d697798](../observations.json)<br>source-8600ee90f3cbd725dabb5179.json<br>`/phases/0` | [qwen27-w4-ordinary-single-card-validation](qwen27-w4-ordinary-single-card-validation.md) | test outcome | Failed / partial | passed=false | Recorded configuration/job |
| [result-76ad454910057fe0b863](../observations.json)<br>source-0f89573b07d12d8184d0e942.json<br>`/jobs/0` | [qwen27-w4-ordinary-single-card-validation](qwen27-w4-ordinary-single-card-validation.md) | test outcome | Failed / partial | passed=false | Recorded configuration/job |
| [result-b1c1f520fed2fb3a7b2e](../observations.json)<br>source-6f8c9f6d334b561d56cfa85b.json<br>`/phases/3` | [qwen27-w4-ordinary-single-card-validation](qwen27-w4-ordinary-single-card-validation.md) | test outcome | Failed / partial | passed=false | Recorded configuration/job |
| [result-c3f7f7452abb4301ca8a](../observations.json)<br>source-ad7f87a0b27327dc9d6185bd.json<br>`/` | [qwen27-w4-ordinary-single-card-validation](qwen27-w4-ordinary-single-card-validation.md) | test outcome | Pass | passed=true; ram_restoration_qualified=true | Recorded configuration/job |
| [result-da9330d1a9e7744c9fb8](../observations.json)<br>source-2cad8ccb5faeb73ec5c81ff6.json<br>`/jobs/0` | [qwen27-w4-ordinary-single-card-validation](qwen27-w4-ordinary-single-card-validation.md) | test outcome | Failed / partial | passed=false | Recorded configuration/job |

These are saved result records, including failures and bounded checks. Copies, individual requests, report summaries and regrading can overlap; their counts are not independent test repetitions. Open each result for exact values, units, configuration binding and source receipts.

There are 4 retained lifecycle records. Their states, exit codes and configuration IDs remain in [catalog.json](../catalog.json); they do not supply missing benchmark results.

[Full archive](../../README.md) | [All retained waves](../RESULTS.md) | [Data definitions](../DATA.md) | [Recommended recipes](../../../README.md)
