# ad019-apex-awq-dflash2-3-pp3-balanced-171513-sizing-final-smoke-130

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
| check-3693932570c937332cde | Pass | {"passed":true,"configured_slots":4,"context_tokens":524288} |
| check-5b2b3fc2d91ad40e71b7 | Pass | {"passed":true,"configured_slots":4,"context_tokens":524288} |

These checks retain their reported scope. A context/allocation/retrieval check is not a general quality score or a speed qualification at that context. Exact flags and provenance are in [checks.json](../checks.json).

## Additional Test Results

| Result / Source | Profile | Evidence type | Reported outcome | Retained values | Configuration binding |
| --- | --- | --- | --- | --- | --- |
| [result-607ce09a1059bd03a679](../observations.json)<br>source-d483a94cc2fdbf31ec4c2f97.json<br>`/capacity/trials/1/peak_prefill` | [ad019-apex-awq-dflash2-3-pp3-balanced-171513-sizing-final-smoke-130](ad019-apex-awq-dflash2-3-pp3-balanced-171513-sizing-final-smoke-130.md)<br>[apex-awq-dflash2-3-pp3-balanced-171513](apex-awq-dflash2-3-pp3-balanced-171513.md) | context allocation | Pass | configured_slots=4 requests; context_tokens=524,288 tokens | Recorded configuration/job |
| [result-c2dc113688449bc7e060](../observations.json)<br>source-797606345fa45914fcd85b71.json<br>`/profiles/apex-abliterated-awq-dflash2-pp3-balanced/final` | [ad019-apex-awq-dflash2-3-pp3-balanced-171513-sizing-final-smoke-130](ad019-apex-awq-dflash2-3-pp3-balanced-171513-sizing-final-smoke-130.md)<br>[apex-abliterated-awq-dflash2-pp3-balanced](apex-abliterated-awq-dflash2-pp3-balanced.md)<br>[apex-awq-dflash2-3-pp3-balanced-171513](apex-awq-dflash2-3-pp3-balanced-171513.md) | context allocation | Outcome unspecified | actual_input_tokens=522,279 tokens; configured_slots=4 requests; context_limit=524,288 tokens; host_peak_bytes=76,023,042,048 bytes; resident_pool_tokens=1,400,157 tokens; per_card_peak_used_MiB_unordered=64,624.00<br>64,650.00<br>64,657.00; exact_boundary_measured=false | Recorded configuration/job |

These are saved result records, including failures and bounded checks. Copies, individual requests, report summaries and regrading can overlap; their counts are not independent test repetitions. Open each result for exact values, units, configuration binding and source receipts.

There are 1 retained lifecycle records. Their states, exit codes and configuration IDs remain in [catalog.json](../catalog.json); they do not supply missing benchmark results.

[Full archive](../../README.md) | [All retained waves](../RESULTS.md) | [Data definitions](../DATA.md) | [Recommended recipes](../../../README.md)
