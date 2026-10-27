# apex-awq-dflash2-3-pp3-balanced-171513-completed

**Historical record. Bounded checks only.**

Model family: Apex Flash 1 (GLM 5.3 Flash post-train).

Historical configurations are provided for comparison. The [recommended recipes](../../../README.md) include supported launch scripts.

Current recipes using the same recorded checkpoint repository: [apex-abliterated-awq-dflash2-pp3-balanced](../../../recipes/apex-abliterated-awq-dflash2-pp3-balanced/README.md). Context, cache and runtime versions can differ.

## Saved Configuration Versions

Each configuration ID identifies a distinct original settings record. Deployment fields are omitted; versions can have identical published settings after that omission. Upstream runtime commits remain unspecified where the source retained only an integration label.

| Configuration | Recorded artifact / source | Configured card counts | Context tokens | GPU pool tokens | Slots | Draft mode / tokens |
| --- | --- | --- | --- | --- | --- | --- |
| cfg-536c7f237f6f8194bb3b | [svbmrgd/apex-flash-1-abliterated-AWQ@7ea31e3d22](https://huggingface.co/svbmrgd/apex-flash-1-abliterated-AWQ/tree/7ea31e3d22c6622c999d3de74d1569efce815943) | 3 | 524,288 | Not recorded | 4 | dflash2 / 3 |

Card counts are saved configuration choices, not a claim that every allowed placement was measured. A derived view can differ from its pinned download source.

<details>
<summary>cfg-536c7f237f6f8194bb3b</summary>

```json
{
  "kind": "vllm_apex_awq",
  "gpu_counts": [
    3
  ],
  "context": 524288,
  "kv_dtype": "fp8_e4m3",
  "draft_kv_dtype": "int8_per_token_head",
  "draft_mode": "dflash2",
  "draft_tokens": 3,
  "max_sessions": 4,
  "chunk_size": 512,
  "ram_kv_mib": 8192,
  "power_watts": 200,
  "host_memory_gib": 80,
  "host_swap_gib": 0,
  "min_vram_mib_per_gpu": 65530,
  "min_effective_vram_mib": 196000,
  "parallelism": "pipeline_parallel",
  "tensor_parallel_size": 1,
  "pipeline_parallel_size": 3,
  "pipeline_layer_partition": [
    17,
    15,
    13
  ],
  "enforce_eager": true,
  "gpu_memory_utilization": 0.985,
  "transport": "host",
  "model_repository": "svbmrgd/apex-flash-1-abliterated-AWQ",
  "model_revision": "7ea31e3d22c6622c999d3de74d1569efce815943",
  "draft_repository": "incoai/GLM-5.3-Flash-DFlash2",
  "draft_revision": "bf582e4eacc1810f76656d1811693ff6c6737d2a",
  "recorded_runtime_label": "apex-awq-nope8-campaign-f",
  "served_model_label": "apex-flash-1-abliterated-awq",
  "draft_directory_template": "@DRAFT_ROOT@"
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
| check-ed6ff30f406c63b267c6 | Pass | {"history_restoration_tested":false,"context_tokens":524288,"resident_pool_tokens":1400157,"passed":true,"retention_pressure_tested":false,"actual_long_request_prompt_tokens":522279,"useful_long_context_retrieval":true,"configured_slots":4} |

These checks retain their reported scope. A context/allocation/retrieval check is not a general quality score or a speed qualification at that context. Exact flags and provenance are in [checks.json](../checks.json).

## Additional Test Results

| Result / Source | Profile | Evidence type | Reported outcome | Retained values | Configuration binding |
| --- | --- | --- | --- | --- | --- |
| [result-1fe500dcb27d73a92416](../observations.json)<br>source-797606345fa45914fcd85b71.json<br>`/profiles/apex-abliterated-awq-dflash2-pp3-balanced/context` | [record-26c850ec689cf58c6b67](record-26c850ec689cf58c6b67.md)<br>[apex-abliterated-awq-dflash2-pp3-balanced](apex-abliterated-awq-dflash2-pp3-balanced.md)<br>[apex-awq-dflash2-3-pp3-balanced-171513-completed](apex-awq-dflash2-3-pp3-balanced-171513-completed.md)<br>[apex-awq-dflash2-3-pp3-balanced-171513-ctx524288-qualification](apex-awq-dflash2-3-pp3-balanced-171513-ctx524288-qualification.md)<br>[apex-awq-dflash2-3-pp3-balanced-171513](apex-awq-dflash2-3-pp3-balanced-171513.md) | context allocation | Pass | actual_long_request_prompt_tokens=522,279 tokens; configured_slots=4 requests; context_tokens=524,288 tokens; resident_pool_tokens=1,400,157 tokens; 4 mixed-length request records; history_restoration_tested=false; retention_pressure_tested=false | Recorded configuration/job |
| [result-66530144f7018c0ec80d](../observations.json)<br>source-d483a94cc2fdbf31ec4c2f97.json<br>`/capacity/prediction/runtime_startup_budget/startup_samples/2` | [record-26c850ec689cf58c6b67](record-26c850ec689cf58c6b67.md)<br>[apex-awq-dflash2-3-pp3-balanced-171513-completed](apex-awq-dflash2-3-pp3-balanced-171513-completed.md)<br>[apex-awq-dflash2-3-pp3-balanced-171513](apex-awq-dflash2-3-pp3-balanced-171513.md) | test outcome | Outcome unspecified | free_GiB=62.29 | Recorded configuration/job |
| [result-84862dd61ce2dac293de](../observations.json)<br>source-d483a94cc2fdbf31ec4c2f97.json<br>`/capacity/trials/1` | [record-26c850ec689cf58c6b67](record-26c850ec689cf58c6b67.md)<br>[apex-awq-dflash2-3-pp3-balanced-171513-completed](apex-awq-dflash2-3-pp3-balanced-171513-completed.md)<br>[apex-awq-dflash2-3-pp3-balanced-171513](apex-awq-dflash2-3-pp3-balanced-171513.md) | context allocation | Outcome unspecified | context_tokens=524,288 tokens; resident_pool_tokens=1,400,157 tokens | Recorded configuration/job |
| [result-965809fee92ef0674212](../observations.json)<br>source-d483a94cc2fdbf31ec4c2f97.json<br>`/capacity/prediction/runtime_startup_budget/startup_samples/0` | [record-26c850ec689cf58c6b67](record-26c850ec689cf58c6b67.md)<br>[apex-awq-dflash2-3-pp3-balanced-171513-completed](apex-awq-dflash2-3-pp3-balanced-171513-completed.md)<br>[apex-awq-dflash2-3-pp3-balanced-171513](apex-awq-dflash2-3-pp3-balanced-171513.md) | test outcome | Outcome unspecified | free_GiB=62.66 | Recorded configuration/job |
| [result-9d91c906a903af29f46a](../observations.json)<br>source-d483a94cc2fdbf31ec4c2f97.json<br>`/capacity/prediction` | [record-26c850ec689cf58c6b67](record-26c850ec689cf58c6b67.md)<br>[apex-awq-dflash2-3-pp3-balanced-171513-completed](apex-awq-dflash2-3-pp3-balanced-171513-completed.md)<br>[apex-awq-dflash2-3-pp3-balanced-171513](apex-awq-dflash2-3-pp3-balanced-171513.md) | test outcome | Outcome unspecified | additional_margin_MiB=512 MiB | Recorded configuration/job |
| [result-9e7cceacf3134a1a33f7](../observations.json)<br>source-d483a94cc2fdbf31ec4c2f97.json<br>`/capacity/prediction/runtime_startup_budget` | [record-26c850ec689cf58c6b67](record-26c850ec689cf58c6b67.md)<br>[apex-awq-dflash2-3-pp3-balanced-171513-completed](apex-awq-dflash2-3-pp3-balanced-171513-completed.md)<br>[apex-awq-dflash2-3-pp3-balanced-171513](apex-awq-dflash2-3-pp3-balanced-171513.md) | test outcome | Outcome unspecified | additional_margin_MiB=512 MiB | Recorded configuration/job |
| [result-f69428e922f4b11fccd3](../observations.json)<br>source-d483a94cc2fdbf31ec4c2f97.json<br>`/capacity` | [record-26c850ec689cf58c6b67](record-26c850ec689cf58c6b67.md)<br>[apex-awq-dflash2-3-pp3-balanced-171513-completed](apex-awq-dflash2-3-pp3-balanced-171513-completed.md)<br>[apex-awq-dflash2-3-pp3-balanced-171513](apex-awq-dflash2-3-pp3-balanced-171513.md) | context allocation | Outcome unspecified | maximum_resident_pool_tokens=1,400,157 tokens; cache_boundary_measured=false; final_maximum_context_concurrent_pressure_passed=false | Recorded configuration/job |
| [result-ffbcd465c09ba6390479](../observations.json)<br>source-d483a94cc2fdbf31ec4c2f97.json<br>`/capacity/prediction/runtime_startup_budget/startup_samples/1` | [record-26c850ec689cf58c6b67](record-26c850ec689cf58c6b67.md)<br>[apex-awq-dflash2-3-pp3-balanced-171513-completed](apex-awq-dflash2-3-pp3-balanced-171513-completed.md)<br>[apex-awq-dflash2-3-pp3-balanced-171513](apex-awq-dflash2-3-pp3-balanced-171513.md) | test outcome | Outcome unspecified | free_GiB=62.67 | Recorded configuration/job |

These are saved result records, including failures and bounded checks. Copies, individual requests, report summaries and regrading can overlap; their counts are not independent test repetitions. Open each result for exact values, units, configuration binding and source receipts.

[Full archive](../../README.md) | [All retained waves](../RESULTS.md) | [Data definitions](../DATA.md) | [Recommended recipes](../../../README.md)
