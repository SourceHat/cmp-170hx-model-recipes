# mimo-mtp1-original-tensor_parallel-completed

**Historical record. Bounded checks only.**

Model family: MiMo V2.6 Flash.

Historical configurations are provided for comparison. The [recommended recipes](../../../README.md) include supported launch scripts.

Current recipes using the same recorded checkpoint repository: [mimo-flash-mtp1-tp3](../../../recipes/mimo-flash-mtp1-tp3/README.md). Context, cache and runtime versions can differ.

## Saved Configuration Versions

Each configuration ID identifies a distinct original settings record. Deployment fields are omitted; versions can have identical published settings after that omission. Upstream runtime commits remain unspecified where the source retained only an integration label.

| Configuration | Recorded artifact / source | Configured card counts | Context tokens | GPU pool tokens | Slots | Draft mode / tokens |
| --- | --- | --- | --- | --- | --- | --- |
| cfg-c18c7aa3248c5b6fa5cf | [MikeRoz/MiMo-V2.6-Flash-MOPD-4.03bpw-h8-exl3@29c8351a8b](https://huggingface.co/MikeRoz/MiMo-V2.6-Flash-MOPD-4.03bpw-h8-exl3/tree/29c8351a8b5854ec385adaeba7bbe62c790d40ea) | 3 | 524,288 | 1,070,848 | 4 | mtp / 1 |

Card counts are saved configuration choices, not a claim that every allowed placement was measured. A derived view can differ from its pinned download source.

<details>
<summary>cfg-c18c7aa3248c5b6fa5cf</summary>

```json
{
  "kind": "tabby",
  "gpu_counts": [
    3
  ],
  "context": 524288,
  "cache_tokens": 1070848,
  "cache_mode": "Q8",
  "draft_cache_mode": "Q8",
  "draft_mode": "mtp",
  "draft_tokens": 1,
  "max_sessions": 4,
  "chunk_size": 512,
  "reserve_mib": 4096,
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
  "model_repository": "MikeRoz/MiMo-V2.6-Flash-MOPD-4.03bpw-h8-exl3",
  "model_revision": "29c8351a8b5854ec385adaeba7bbe62c790d40ea",
  "draft_repository": null,
  "draft_revision": null,
  "recorded_runtime_label": null,
  "served_model_label": "mimo-v2.6-flash",
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
| check-6a29d9c8164f466df066 | Pass | {"history_restoration_tested":false,"context_tokens":524288,"resident_pool_tokens":1070848,"passed":true,"retention_pressure_tested":false,"actual_long_request_prompt_tokens":522285,"useful_long_context_retrieval":true,"configured_slots":4} |
| check-9fe334a085613cb7a64a | Pass | {"reserve_mib":4096,"passed":true} |

These checks retain their reported scope. A context/allocation/retrieval check is not a general quality score or a speed qualification at that context. Exact flags and provenance are in [checks.json](../checks.json).

## Additional Test Results

| Result / Source | Profile | Evidence type | Reported outcome | Retained values | Configuration binding |
| --- | --- | --- | --- | --- | --- |
| [result-1715d35a3f88edfa8eea](../observations.json)<br>source-94b07b24e27af4961cf45d26.json<br>`/capacity/trials/1/context_smoke` | [record-26c850ec689cf58c6b67](record-26c850ec689cf58c6b67.md)<br>[mimo-mtp1-original-tensor_parallel-completed](mimo-mtp1-original-tensor_parallel-completed.md)<br>[mimo-mtp1-original-tensor_parallel-ctx524288-qualification](mimo-mtp1-original-tensor_parallel-ctx524288-qualification.md)<br>[mimo-mtp1-original-tensor_parallel](mimo-mtp1-original-tensor_parallel.md) | context allocation | Pass | actual_long_request_prompt_tokens=522,285 tokens; configured_slots=4 requests; context_tokens=524,288 tokens; resident_pool_tokens=1,070,848 tokens; 4 mixed-length request records; history_restoration_tested=false; retention_pressure_tested=false | Recorded configuration/job |
| [result-a12ae9868b07fe59b1c5](../observations.json)<br>source-94b07b24e27af4961cf45d26.json<br>`/capacity/prediction` | [record-26c850ec689cf58c6b67](record-26c850ec689cf58c6b67.md)<br>[mimo-mtp1-original-tensor_parallel-completed](mimo-mtp1-original-tensor_parallel-completed.md)<br>[mimo-mtp1-original-tensor_parallel](mimo-mtp1-original-tensor_parallel.md) | test outcome | Outcome unspecified | additional_margin_MiB=4,096 MiB | Recorded configuration/job |
| [result-a5c8ecc1848a85fae63f](../observations.json)<br>source-94b07b24e27af4961cf45d26.json<br>`/capacity` | [record-26c850ec689cf58c6b67](record-26c850ec689cf58c6b67.md)<br>[mimo-mtp1-original-tensor_parallel-completed](mimo-mtp1-original-tensor_parallel-completed.md)<br>[mimo-mtp1-original-tensor_parallel](mimo-mtp1-original-tensor_parallel.md) | context allocation | Outcome unspecified | maximum_resident_pool_tokens=1,070,848 tokens; planning_reserve_mib=4,096 MiB; cache_boundary_measured=false; final_maximum_context_concurrent_pressure_passed=false | Recorded configuration/job |
| [result-b2fe86912990e866de7a](../observations.json)<br>source-94b07b24e27af4961cf45d26.json<br>`/capacity/headroom_trials/0` | [record-26c850ec689cf58c6b67](record-26c850ec689cf58c6b67.md)<br>[mimo-mtp1-original-tensor_parallel-completed](mimo-mtp1-original-tensor_parallel-completed.md)<br>[mimo-mtp1-original-tensor_parallel](mimo-mtp1-original-tensor_parallel.md) | context allocation | Pass | reserve_mib=4,096 MiB | Recorded configuration/job |
| [result-ee16105ee6facde5249d](../observations.json)<br>source-94b07b24e27af4961cf45d26.json<br>`/capacity/trials/1` | [record-26c850ec689cf58c6b67](record-26c850ec689cf58c6b67.md)<br>[mimo-mtp1-original-tensor_parallel-completed](mimo-mtp1-original-tensor_parallel-completed.md)<br>[mimo-mtp1-original-tensor_parallel](mimo-mtp1-original-tensor_parallel.md) | context allocation | Outcome unspecified | context_tokens=524,288 tokens; resident_pool_tokens=1,070,848 tokens | Recorded configuration/job |

These are saved result records, including failures and bounded checks. Copies, individual requests, report summaries and regrading can overlap; their counts are not independent test repetitions. Open each result for exact values, units, configuration binding and source receipts.

[Full archive](../../README.md) | [All retained waves](../RESULTS.md) | [Data definitions](../DATA.md) | [Recommended recipes](../../../README.md)
