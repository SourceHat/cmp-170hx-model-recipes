# glm-mtp1-original-tensor_parallel-completed

**Historical record. Bounded checks only.**

Model family: GLM 5.3 Flash.

Historical configurations are provided for comparison. The [recommended recipes](../../../README.md) include supported launch scripts.

Current recipes using the same recorded checkpoint repository: [glm-5.3-flash-mtp1-tp3](../../../recipes/glm-5.3-flash-mtp1-tp3/README.md). Context, cache and runtime versions can differ.

## Saved Configuration Versions

Each configuration ID identifies a distinct original settings record. Deployment fields are omitted; versions can have identical published settings after that omission. Upstream runtime commits remain unspecified where the source retained only an integration label.

| Configuration | Recorded artifact / source | Configured card counts | Context tokens | GPU pool tokens | Slots | Draft mode / tokens |
| --- | --- | --- | --- | --- | --- | --- |
| cfg-1dcc4997a4d7ab4f0703 | [turboderp/GLM-5.3-Flash-exl3@2a30229e67](https://huggingface.co/turboderp/GLM-5.3-Flash-exl3/tree/2a30229e67012798ba9f0cd832bb78abf4c363d5) | 3 | 524,288 | 1,829,376 | 4 | mtp / 1 |

Card counts are saved configuration choices, not a claim that every allowed placement was measured. A derived view can differ from its pinned download source.

<details>
<summary>cfg-1dcc4997a4d7ab4f0703</summary>

```json
{
  "kind": "tabby",
  "gpu_counts": [
    3
  ],
  "context": 524288,
  "cache_tokens": 1829376,
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
  "model_repository": "turboderp/GLM-5.3-Flash-exl3",
  "model_revision": "2a30229e67012798ba9f0cd832bb78abf4c363d5",
  "draft_repository": null,
  "draft_revision": null,
  "recorded_runtime_label": null,
  "served_model_label": "glm-5.3-flash",
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
| check-b75dcd49b332a0724af0 | Pass | {"reserve_mib":2048,"passed":true} |
| check-ca1ce09b873f4f759b64 | Pass | {"history_restoration_tested":false,"context_tokens":524288,"resident_pool_tokens":1829376,"passed":true,"retention_pressure_tested":false,"actual_long_request_prompt_tokens":522281,"useful_long_context_retrieval":true,"configured_slots":4} |

These checks retain their reported scope. A context/allocation/retrieval check is not a general quality score or a speed qualification at that context. Exact flags and provenance are in [checks.json](../checks.json).

## Additional Test Results

| Result / Source | Profile | Evidence type | Reported outcome | Retained values | Configuration binding |
| --- | --- | --- | --- | --- | --- |
| [result-2ae333be15ccc961b067](../observations.json)<br>source-7419c98729f86c1aed84b571.json<br>`/capacity/headroom_trials/0` | [record-26c850ec689cf58c6b67](record-26c850ec689cf58c6b67.md)<br>[glm-mtp1-original-tensor_parallel-completed](glm-mtp1-original-tensor_parallel-completed.md)<br>[glm-mtp1-original-tensor_parallel](glm-mtp1-original-tensor_parallel.md) | context allocation | Pass | reserve_mib=2,048 MiB | Recorded configuration/job |
| [result-5074dcec9d45551191c8](../observations.json)<br>source-7419c98729f86c1aed84b571.json<br>`/capacity/prediction` | [record-26c850ec689cf58c6b67](record-26c850ec689cf58c6b67.md)<br>[glm-mtp1-original-tensor_parallel-completed](glm-mtp1-original-tensor_parallel-completed.md)<br>[glm-mtp1-original-tensor_parallel](glm-mtp1-original-tensor_parallel.md) | test outcome | Outcome unspecified | additional_margin_MiB=2,048 MiB | Recorded configuration/job |
| [result-525193f7f672783d4017](../observations.json)<br>source-7419c98729f86c1aed84b571.json<br>`/capacity` | [record-26c850ec689cf58c6b67](record-26c850ec689cf58c6b67.md)<br>[glm-mtp1-original-tensor_parallel-completed](glm-mtp1-original-tensor_parallel-completed.md)<br>[glm-mtp1-original-tensor_parallel](glm-mtp1-original-tensor_parallel.md) | context allocation | Outcome unspecified | maximum_resident_pool_tokens=1,829,376 tokens; planning_reserve_mib=2,048 MiB; cache_boundary_measured=false; final_maximum_context_concurrent_pressure_passed=false | Recorded configuration/job |
| [result-7ad528710a50799eac3a](../observations.json)<br>source-7419c98729f86c1aed84b571.json<br>`/capacity/trials/1/context_smoke` | [record-26c850ec689cf58c6b67](record-26c850ec689cf58c6b67.md)<br>[glm-mtp1-original-tensor_parallel-completed](glm-mtp1-original-tensor_parallel-completed.md)<br>[glm-mtp1-original-tensor_parallel-ctx524288-qualification](glm-mtp1-original-tensor_parallel-ctx524288-qualification.md)<br>[glm-mtp1-original-tensor_parallel](glm-mtp1-original-tensor_parallel.md) | context allocation | Pass | actual_long_request_prompt_tokens=522,281 tokens; configured_slots=4 requests; context_tokens=524,288 tokens; resident_pool_tokens=1,829,376 tokens; 4 mixed-length request records; history_restoration_tested=false; retention_pressure_tested=false | Recorded configuration/job |
| [result-d83bd35086348f97cb20](../observations.json)<br>source-7419c98729f86c1aed84b571.json<br>`/capacity/trials/1` | [record-26c850ec689cf58c6b67](record-26c850ec689cf58c6b67.md)<br>[glm-mtp1-original-tensor_parallel-completed](glm-mtp1-original-tensor_parallel-completed.md)<br>[glm-mtp1-original-tensor_parallel](glm-mtp1-original-tensor_parallel.md) | context allocation | Outcome unspecified | context_tokens=524,288 tokens; resident_pool_tokens=1,829,376 tokens | Recorded configuration/job |

These are saved result records, including failures and bounded checks. Copies, individual requests, report summaries and regrading can overlap; their counts are not independent test repetitions. Open each result for exact values, units, configuration binding and source receipts.

[Full archive](../../README.md) | [All retained waves](../RESULTS.md) | [Data definitions](../DATA.md) | [Recommended recipes](../../../README.md)
