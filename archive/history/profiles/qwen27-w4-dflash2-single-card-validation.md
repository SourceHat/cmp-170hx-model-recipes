# qwen27-w4-dflash2-single-card-validation

**Historical record. Bounded checks only.**

Model family: Qwen 3.8 27B.

Historical configurations are provided for comparison. The [recommended recipes](../../../README.md) include supported launch scripts.

## Saved Configuration Versions

Each configuration ID identifies a distinct original settings record. Deployment fields are omitted; versions can have identical published settings after that omission. Upstream runtime commits remain unspecified where the source retained only an integration label.

| Configuration | Recorded artifact / source | Configured card counts | Context tokens | GPU pool tokens | Slots | Draft mode / tokens |
| --- | --- | --- | --- | --- | --- | --- |
| cfg-99542cbd93ed5c5eff8c | [dbirks/Qwen3.8-27B-W4A16-AutoRound@1f05c441c4](https://huggingface.co/dbirks/Qwen3.8-27B-W4A16-AutoRound/tree/1f05c441c4e64ae0549de44fa9ea5a6d43610314) | 1 | 32,768 | Not recorded | 4 | dflash2 / 7 |

Card counts are saved configuration choices, not a claim that every allowed placement was measured. A derived view can differ from its pinned download source.

<details>
<summary>cfg-99542cbd93ed5c5eff8c</summary>

```json
{
  "kind": "vllm_qwen27",
  "gpu_counts": [
    1
  ],
  "context": 32768,
  "kv_dtype": "bfloat16",
  "draft_mode": "dflash2",
  "draft_tokens": 7,
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
  "draft_revision": "4d30ec736ffc6b8688dc2ae2b502d9b48bdec279",
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
| check-0646de6a24768386d79a | Failed / partial | {"passed":false,"ram_restoration_qualified":false} |
| check-3f094b91878bb8cc0a39 | Failed / partial | {"passed":false,"ram_restoration_qualified":false} |
| check-fd1d9dc1e689d32a80de | Failed / partial | {"passed":false,"ram_restoration_qualified":false} |

These checks retain their reported scope. A context/allocation/retrieval check is not a general quality score or a speed qualification at that context. Exact flags and provenance are in [checks.json](../checks.json).

## Additional Test Results

| Result / Source | Profile | Evidence type | Reported outcome | Retained values | Configuration binding |
| --- | --- | --- | --- | --- | --- |
| [result-0d7ccf9e12fcc4135df7](../observations.json)<br>source-f5cd0e800e65f1be995837cf.json<br>`/` | [qwen27-w4-dflash2-single-card-validation](qwen27-w4-dflash2-single-card-validation.md) | test outcome | Failed / partial | ram_restoration_qualified=false | Recorded configuration/job |
| [result-349ba677a33be0945fec](../observations.json)<br>source-a1ebd7681e23c15a2ac6baca.json<br>`/jobs/1` | [qwen27-w4-dflash2-single-card-validation](qwen27-w4-dflash2-single-card-validation.md) | test outcome | Failed / partial | passed=false | Recorded configuration/job |
| [result-4a8e3e0b90e552e9c146](../observations.json)<br>source-5a12ece39ab89103f5da3d17.json<br>`/` | [qwen27-w4-dflash2-single-card-validation](qwen27-w4-dflash2-single-card-validation.md) | test outcome | Failed / partial | ram_restoration_qualified=false | Recorded configuration/job |
| [result-63204ea38fec64576f6c](../observations.json)<br>source-0f89573b07d12d8184d0e942.json<br>`/jobs/1` | [qwen27-w4-dflash2-single-card-validation](qwen27-w4-dflash2-single-card-validation.md) | test outcome | Failed / partial | passed=false | Recorded configuration/job |
| [result-73939dc07d1f5949ba14](../observations.json)<br>source-5a12ece39ab89103f5da3d17.json<br>`/phases/3` | [qwen27-w4-dflash2-single-card-validation](qwen27-w4-dflash2-single-card-validation.md) | test outcome | Failed / partial | passed=false | Recorded configuration/job |
| [result-9a31217fd3867a6c84d1](../observations.json)<br>source-3b496d931c3e8a19f16d140d.json<br>`/` | [qwen27-w4-dflash2-single-card-validation](qwen27-w4-dflash2-single-card-validation.md) | test outcome | Failed / partial | ram_restoration_qualified=false | Recorded configuration/job |
| [result-a35340a7885d115bec77](../observations.json)<br>source-3b496d931c3e8a19f16d140d.json<br>`/phases/2` | [qwen27-w4-dflash2-single-card-validation](qwen27-w4-dflash2-single-card-validation.md) | test outcome | Failed / partial | passed=false | Recorded configuration/job |
| [result-ad91ed7cc65e49d8fadb](../observations.json)<br>source-2cad8ccb5faeb73ec5c81ff6.json<br>`/jobs/1` | [qwen27-w4-dflash2-single-card-validation](qwen27-w4-dflash2-single-card-validation.md) | test outcome | Failed / partial | passed=false | Recorded configuration/job |
| [result-b845e6646deac02fcd96](../observations.json)<br>source-f5cd0e800e65f1be995837cf.json<br>`/phases/0` | [qwen27-w4-dflash2-single-card-validation](qwen27-w4-dflash2-single-card-validation.md) | test outcome | Failed / partial | passed=false | Recorded configuration/job |

These are saved result records, including failures and bounded checks. Copies, individual requests, report summaries and regrading can overlap; their counts are not independent test repetitions. Open each result for exact values, units, configuration binding and source receipts.

There are 3 retained lifecycle records. Their states, exit codes and configuration IDs remain in [catalog.json](../catalog.json); they do not supply missing benchmark results.

[Full archive](../../README.md) | [All retained waves](../RESULTS.md) | [Data definitions](../DATA.md) | [Recommended recipes](../../../README.md)
