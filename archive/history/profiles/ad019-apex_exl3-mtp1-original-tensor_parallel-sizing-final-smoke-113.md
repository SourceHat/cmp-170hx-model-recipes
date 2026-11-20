# ad019-apex_exl3-mtp1-original-tensor_parallel-sizing-final-smoke-113

**Historical record. Bounded checks only.**

Model family: Apex Flash 1 (GLM 5.3 Flash post-train).

Historical configurations are provided for comparison. The [recommended recipes](../../../README.md) include supported launch scripts.

Current recipes using the same recorded checkpoint repository: [apex-abliterated-exl3-mtp1-tp3](../../../recipes/apex-abliterated-exl3-mtp1-tp3/README.md). Context, cache and runtime versions can differ.

## Saved Configuration Versions

Each configuration ID identifies a distinct original settings record. Deployment fields are omitted; versions can have identical published settings after that omission. Upstream runtime commits remain unspecified where the source retained only an integration label.

| Configuration | Recorded artifact / source | Configured card counts | Context tokens | GPU pool tokens | Slots | Draft mode / tokens |
| --- | --- | --- | --- | --- | --- | --- |
| cfg-5921427b74f4d9895cf4 | [SloptimistPrime/apex-flash-1-abliterated-EXL3-4bit-DGX-Spark@a4c922dc57](https://huggingface.co/SloptimistPrime/apex-flash-1-abliterated-EXL3-4bit-DGX-Spark/tree/a4c922dc57dae44a9569ec82a08a2f311636e2a6) | 3 | 524,288 | 1,083,136 | 4 | mtp / 1 |
| cfg-a6d9a38d66a9992a2338 | [SloptimistPrime/apex-flash-1-abliterated-EXL3-4bit-DGX-Spark@a4c922dc57](https://huggingface.co/SloptimistPrime/apex-flash-1-abliterated-EXL3-4bit-DGX-Spark/tree/a4c922dc57dae44a9569ec82a08a2f311636e2a6) | 3 | 524,288 | 1,083,136 | 4 | mtp / 1 |

Card counts are saved configuration choices, not a claim that every allowed placement was measured. A derived view can differ from its pinned download source.

<details>
<summary>cfg-5921427b74f4d9895cf4</summary>

```json
{
  "kind": "tabby",
  "gpu_counts": [
    3
  ],
  "context": 524288,
  "cache_tokens": 1083136,
  "cache_mode": "Q8",
  "draft_cache_mode": "Q8",
  "draft_mode": "mtp",
  "draft_tokens": 1,
  "max_sessions": 4,
  "chunk_size": 512,
  "reserve_mib": 2048,
  "ram_kv_mib": 8192,
  "ram_recurrent_mib": 16384,
  "dynamic_draft": false,
  "output_chunk_tokens": 4096,
  "power_watts": 200,
  "host_memory_gib": 80,
  "host_swap_gib": 0,
  "min_vram_mib_per_gpu": 65530,
  "min_effective_vram_mib": 196590,
  "parallelism": "tensor_parallel",
  "transport": "host",
  "host_backing": "ordinary",
  "model_repository": "SloptimistPrime/apex-flash-1-abliterated-EXL3-4bit-DGX-Spark",
  "model_revision": "a4c922dc57dae44a9569ec82a08a2f311636e2a6",
  "draft_repository": null,
  "draft_revision": null,
  "recorded_runtime_label": null,
  "served_model_label": "apex-flash-1-abliterated-exl3-4bit-spark"
}
```

Pinned model revision recorded: yes. Source receipt labels, hashes and object locators are retained in [configurations.json](../configurations.json).

</details>

<details>
<summary>cfg-a6d9a38d66a9992a2338</summary>

```json
{
  "kind": "tabby",
  "gpu_counts": [
    3
  ],
  "context": 524288,
  "cache_tokens": 1083136,
  "cache_mode": "Q8",
  "draft_cache_mode": "Q8",
  "draft_mode": "mtp",
  "draft_tokens": 1,
  "max_sessions": 4,
  "chunk_size": 512,
  "reserve_mib": 2048,
  "ram_kv_mib": 8192,
  "ram_recurrent_mib": 16384,
  "dynamic_draft": false,
  "output_chunk_tokens": 4096,
  "power_watts": 200,
  "host_memory_gib": 80,
  "host_swap_gib": 0,
  "min_vram_mib_per_gpu": 65530,
  "min_effective_vram_mib": 196590,
  "parallelism": "tensor_parallel",
  "transport": "host",
  "host_backing": "ordinary",
  "model_repository": "SloptimistPrime/apex-flash-1-abliterated-EXL3-4bit-DGX-Spark",
  "model_revision": "a4c922dc57dae44a9569ec82a08a2f311636e2a6",
  "draft_repository": null,
  "draft_revision": null,
  "recorded_runtime_label": null,
  "served_model_label": "apex-flash-1-abliterated-exl3-4bit-spark",
  "main_reserve_mib_values_unordered": []
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
| check-65e5ab9b675dbc73159c | Pass | {"passed":true,"configured_slots":4,"context_tokens":524288} |
| check-e4cbe1a77cda94f1e084 | Pass | {"passed":true,"configured_slots":4,"context_tokens":524288} |

These checks retain their reported scope. A context/allocation/retrieval check is not a general quality score or a speed qualification at that context. Exact flags and provenance are in [checks.json](../checks.json).

## Additional Test Results

| Result / Source | Profile | Evidence type | Reported outcome | Retained values | Configuration binding |
| --- | --- | --- | --- | --- | --- |
| [result-5d7da08edaeb5dcf6bdd](../observations.json)<br>source-b5ce85b23063b71f50338af3.json<br>`/capacity/trials/1/peak_prefill` | [ad019-apex_exl3-mtp1-original-tensor_parallel-sizing-final-smoke-113](ad019-apex_exl3-mtp1-original-tensor_parallel-sizing-final-smoke-113.md)<br>[apex_exl3-mtp1-original-tensor_parallel](apex_exl3-mtp1-original-tensor_parallel.md) | context allocation | Pass | configured_slots=4 requests; context_tokens=524,288 tokens | Recorded configuration/job |
| [result-a870d17b3ec532e29db5](../observations.json)<br>source-797606345fa45914fcd85b71.json<br>`/profiles/apex-abliterated-exl3-mtp1-tp3/final` | [ad019-apex_exl3-mtp1-original-tensor_parallel-sizing-final-smoke-113](ad019-apex_exl3-mtp1-original-tensor_parallel-sizing-final-smoke-113.md)<br>[apex-abliterated-exl3-mtp1-tp3](apex-abliterated-exl3-mtp1-tp3.md)<br>[apex_exl3-mtp1-original-tensor_parallel](apex_exl3-mtp1-original-tensor_parallel.md) | context allocation | Outcome unspecified | actual_input_tokens=522,281 tokens; configured_slots=4 requests; context_limit=524,288 tokens; host_peak_bytes=68,634,304,512 bytes; resident_pool_tokens=1,083,136 tokens; per_card_peak_used_MiB_unordered=62,462.00<br>63,093.00<br>63,309.00; exact_boundary_measured=false | Recorded configuration/job |

These are saved result records, including failures and bounded checks. Copies, individual requests, report summaries and regrading can overlap; their counts are not independent test repetitions. Open each result for exact values, units, configuration binding and source receipts.

There are 1 retained lifecycle records. Their states, exit codes and configuration IDs remain in [catalog.json](../catalog.json); they do not supply missing benchmark results.

[Full archive](../../README.md) | [All retained waves](../RESULTS.md) | [Data definitions](../DATA.md) | [Recommended recipes](../../../README.md)
