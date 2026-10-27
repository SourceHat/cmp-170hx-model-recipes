# qwen27-w8-mtp-single-card-validation

**Historical record. Bounded checks only.**

Model family: Qwen 3.8 27B.

Historical configurations are provided for comparison. The [recommended recipes](../../../README.md) include supported launch scripts.

## Saved Configuration Versions

Each configuration ID identifies a distinct original settings record. Deployment fields are omitted; versions can have identical published settings after that omission. Upstream runtime commits remain unspecified where the source retained only an integration label.

| Configuration | Recorded artifact / source | Configured card counts | Context tokens | GPU pool tokens | Slots | Draft mode / tokens |
| --- | --- | --- | --- | --- | --- | --- |
| cfg-f3ba9ded7e74d1d4d33c | [lued/Qwen3.8-27B-INT8-W8A16-MTP@7c12373712](https://huggingface.co/lued/Qwen3.8-27B-INT8-W8A16-MTP/tree/7c12373712d1363e2b76655cb3332c9c124627d7) | 3 | 32,768 | Not recorded | 4 | mtp / 3 |

Card counts are saved configuration choices, not a claim that every allowed placement was measured. A derived view can differ from its pinned download source.

<details>
<summary>cfg-f3ba9ded7e74d1d4d33c</summary>

```json
{
  "kind": "vllm_qwen27",
  "gpu_counts": [
    3
  ],
  "context": 32768,
  "kv_dtype": "bfloat16",
  "draft_mode": "mtp",
  "draft_tokens": 3,
  "max_sessions": 4,
  "chunk_size": 1024,
  "ram_kv_mib": 8192,
  "power_watts": 200,
  "host_memory_gib": 80,
  "host_swap_gib": 0,
  "min_vram_mib_per_gpu": 65530,
  "min_effective_vram_mib": 196000,
  "tensor_parallel_size": 1,
  "pipeline_parallel_size": 1,
  "kv_cache_mib_per_gpu": 4096,
  "enforce_eager": true,
  "mamba_cache_mode": "align",
  "model_repository": "lued/Qwen3.8-27B-INT8-W8A16-MTP",
  "model_revision": "7c12373712d1363e2b76655cb3332c9c124627d7",
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
| check-f605a488fd059ce03c22 | Pass | {"passed":true,"ram_restoration_qualified":true} |
| check-fda648c051e42a806aa0 | Failed / partial | {"passed":false,"ram_restoration_qualified":false} |

These checks retain their reported scope. A context/allocation/retrieval check is not a general quality score or a speed qualification at that context. Exact flags and provenance are in [checks.json](../checks.json).

## Additional Test Results

| Result / Source | Profile | Evidence type | Reported outcome | Retained values | Configuration binding |
| --- | --- | --- | --- | --- | --- |
| [result-05a2fcab0f45de9a9b53](../observations.json)<br>source-1a55990892c7bb4594650b38.json<br>`/` | [qwen27-w8-mtp-single-card-validation](qwen27-w8-mtp-single-card-validation.md) | test outcome | Pass | passed=true; ram_restoration_qualified=true | Recorded configuration/job |
| [result-06710d4d727122404a47](../observations.json)<br>source-e9bd7c1e081c351f2d5c53ed.json<br>`/phases/2` | [qwen27-w8-mtp-single-card-validation](qwen27-w8-mtp-single-card-validation.md) | test outcome | Failed / partial | passed=false | Recorded configuration/job |
| [result-66fdadcc23aefe36edd1](../observations.json)<br>source-e9bd7c1e081c351f2d5c53ed.json<br>`/` | [qwen27-w8-mtp-single-card-validation](qwen27-w8-mtp-single-card-validation.md) | test outcome | Failed / partial | ram_restoration_qualified=false | Recorded configuration/job |
| [result-c00b77a1eaf86d18f53b](../observations.json)<br>source-0f89573b07d12d8184d0e942.json<br>`/jobs/3` | [qwen27-w8-mtp-single-card-validation](qwen27-w8-mtp-single-card-validation.md) | test outcome | Failed / partial | passed=false | Recorded configuration/job |

These are saved result records, including failures and bounded checks. Copies, individual requests, report summaries and regrading can overlap; their counts are not independent test repetitions. Open each result for exact values, units, configuration binding and source receipts.

There are 2 retained lifecycle records. Their states, exit codes and configuration IDs remain in [catalog.json](../catalog.json); they do not supply missing benchmark results.

[Full archive](../../README.md) | [All retained waves](../RESULTS.md) | [Data definitions](../DATA.md) | [Recommended recipes](../../../README.md)
