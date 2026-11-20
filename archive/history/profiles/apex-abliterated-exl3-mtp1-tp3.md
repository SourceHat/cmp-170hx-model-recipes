# apex-abliterated-exl3-mtp1-tp3

**Historical record. Bounded checks only.**

Model family: Apex Flash 1 (GLM 5.3 Flash post-train).

Historical configurations are provided for comparison. The [recommended recipes](../../../README.md) include supported launch scripts.

Current recipes using the same recorded checkpoint repository: [apex-abliterated-exl3-mtp1-tp3](../../../recipes/apex-abliterated-exl3-mtp1-tp3/README.md). Context, cache and runtime versions can differ.

## Saved Configuration Versions

Each configuration ID identifies a distinct original settings record. Deployment fields are omitted; versions can have identical published settings after that omission. Upstream runtime commits remain unspecified where the source retained only an integration label.

| Configuration | Recorded artifact / source | Configured card counts | Context tokens | GPU pool tokens | Slots | Draft mode / tokens |
| --- | --- | --- | --- | --- | --- | --- |
| cfg-318b09c80823117e7b7c | [SloptimistPrime/apex-flash-1-abliterated-EXL3-4bit-DGX-Spark@a4c922dc57](https://huggingface.co/SloptimistPrime/apex-flash-1-abliterated-EXL3-4bit-DGX-Spark/tree/a4c922dc57dae44a9569ec82a08a2f311636e2a6) | 3 | 524,288 | 1,083,136 | 4 | mtp / 1 |
| cfg-408537e15316414089ab | [SloptimistPrime/apex-flash-1-abliterated-EXL3-4bit-DGX-Spark@a4c922dc57](https://huggingface.co/SloptimistPrime/apex-flash-1-abliterated-EXL3-4bit-DGX-Spark/tree/a4c922dc57dae44a9569ec82a08a2f311636e2a6) | 3 | 524,288 | 1,083,136 | 4 | mtp / 1 |
| cfg-a6d9a38d66a9992a2338 | [SloptimistPrime/apex-flash-1-abliterated-EXL3-4bit-DGX-Spark@a4c922dc57](https://huggingface.co/SloptimistPrime/apex-flash-1-abliterated-EXL3-4bit-DGX-Spark/tree/a4c922dc57dae44a9569ec82a08a2f311636e2a6) | 3 | 524,288 | 1,083,136 | 4 | mtp / 1 |
| cfg-aab55e422cc92e28c196 | [SloptimistPrime/apex-flash-1-abliterated-EXL3-4bit-DGX-Spark@a4c922dc57](https://huggingface.co/SloptimistPrime/apex-flash-1-abliterated-EXL3-4bit-DGX-Spark/tree/a4c922dc57dae44a9569ec82a08a2f311636e2a6) | 3 | 524,288 | 1,083,136 | 4 | mtp / 1 |

Card counts are saved configuration choices, not a claim that every allowed placement was measured. A derived view can differ from its pinned download source.

<details>
<summary>cfg-318b09c80823117e7b7c</summary>

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

<details>
<summary>cfg-408537e15316414089ab</summary>

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
  "host_memory_gib": 0,
  "host_swap_gib": 0,
  "min_vram_mib_per_gpu": 63800,
  "min_effective_vram_mib": 191400,
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

<details>
<summary>cfg-aab55e422cc92e28c196</summary>

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
  "ram_kv_mib": 0,
  "ram_recurrent_mib": 16384,
  "dynamic_draft": false,
  "output_chunk_tokens": 4096,
  "power_watts": 200,
  "host_memory_gib": 0,
  "host_swap_gib": 0,
  "min_vram_mib_per_gpu": 63800,
  "min_effective_vram_mib": 191400,
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

## Retained Measurements

No detailed benchmark receipt is matched to this record. A saved definition or a successful job exit alone is not a performance measurement.

A dash in shared decode means no qualified synchronized interval is available. Whole-wave throughput includes prefill and queueing. A valid decode interval can survive inside an overall failed or partial check; the source-report outcome is preserved. No rows are averaged.

## Bounded Checks

| Check | Reported outcome | Retained counts / flags |
| --- | --- | --- |
| check-72c8966e3e6ac865e2c5 | Pass | {"history_restoration_tested":false,"context_tokens":524288,"resident_pool_tokens":1083136,"passed":true,"retention_pressure_tested":false,"actual_long_request_prompt_tokens":522281,"useful_long_context_retrieval":true,"configured_slots":4} |

These checks retain their reported scope. A context/allocation/retrieval check is not a general quality score or a speed qualification at that context. Exact flags and provenance are in [checks.json](../checks.json).

## Additional Test Results

| Result / Source | Profile | Evidence type | Reported outcome | Retained values | Configuration binding |
| --- | --- | --- | --- | --- | --- |
| [result-21eb6654b19e6f4e9a99](../observations.json)<br>source-797606345fa45914fcd85b71.json<br>`/profiles/apex-abliterated-exl3-mtp1-tp3/old_speed/concurrent-32768` | [apex-abliterated-exl3-mtp1-tp3](apex-abliterated-exl3-mtp1-tp3.md) | test outcome | Outcome unspecified | request_count=4 requests | Recorded configuration/job |
| [result-2833cb0f0ed66314defe](../observations.json)<br>source-797606345fa45914fcd85b71.json<br>`/profiles/apex-abliterated-exl3-mtp1-tp3/quality` | [apex-abliterated-exl3-mtp1-tp3](apex-abliterated-exl3-mtp1-tp3.md) | quality evaluation | 7 / 8 tasks passed | coding: 1 / 2; tool: 2 / 2; agent: 2 / 2; reasoning: 2 / 2; Task latency median 3.63 s; n=8 | Recorded configuration/job |
| [result-2f6df3d9165ed4f838fb](../observations.json)<br>source-797606345fa45914fcd85b71.json<br>`/profiles/apex-abliterated-exl3-mtp1-tp3/context` | [record-26c850ec689cf58c6b67](record-26c850ec689cf58c6b67.md)<br>[apex-abliterated-exl3-mtp1-tp3](apex-abliterated-exl3-mtp1-tp3.md)<br>[apex_exl3-mtp1-original-tensor_parallel-completed](apex_exl3-mtp1-original-tensor_parallel-completed.md)<br>[apex_exl3-mtp1-original-tensor_parallel-ctx524288-qualification](apex_exl3-mtp1-original-tensor_parallel-ctx524288-qualification.md)<br>[apex_exl3-mtp1-original-tensor_parallel](apex_exl3-mtp1-original-tensor_parallel.md) | context allocation | Pass | actual_long_request_prompt_tokens=522,281 tokens; configured_slots=4 requests; context_tokens=524,288 tokens; resident_pool_tokens=1,083,136 tokens; 4 mixed-length request records; history_restoration_tested=false; retention_pressure_tested=false | Recorded configuration/job |
| [result-3c103e3b02ead51d94d8](../observations.json)<br>source-797606345fa45914fcd85b71.json<br>`/profiles/apex-abliterated-exl3-mtp1-tp3/old_speed/single-32768` | [apex-abliterated-exl3-mtp1-tp3](apex-abliterated-exl3-mtp1-tp3.md) | test outcome | Outcome unspecified | request_count=1 requests | Recorded configuration/job |
| [result-57d344de20c16a994111](../observations.json)<br>source-797606345fa45914fcd85b71.json<br>`/profiles/apex-abliterated-exl3-mtp1-tp3` | [apex-abliterated-exl3-mtp1-tp3](apex-abliterated-exl3-mtp1-tp3.md) | context allocation | Outcome unspecified | pool=1,083,136 tokens; draft KV=1,213,112,320 bytes; main KV=13,344,235,520 bytes; allocator_reserved_GiB=60.47<br>60.15<br>54.98; free_GiB=1.51<br>2.12<br>0.59; peak_total_GiB=61.61<br>61.00<br>61.83 | Recorded configuration/job |

These are saved result records, including failures and bounded checks. Copies, individual requests, report summaries and regrading can overlap; their counts are not independent test repetitions. Open each result for exact values, units, configuration binding and source receipts.

There are 3 retained lifecycle records. Their states, exit codes and configuration IDs remain in [catalog.json](../catalog.json); they do not supply missing benchmark results.

[Full archive](../../README.md) | [All retained waves](../RESULTS.md) | [Data definitions](../DATA.md) | [Recommended recipes](../../../README.md)
