# ad025-apex-awq-dflash2-pp3-fast-001

**Historical record. Legacy / incomplete measurements.**

Model family: Apex Flash 1 (GLM 5.3 Flash post-train).

Historical configurations are provided for comparison. The [recommended recipes](../../../README.md) include supported launch scripts.

Current recipes using the same recorded checkpoint repository: [apex-abliterated-awq-dflash2-pp3-balanced](../../../recipes/apex-abliterated-awq-dflash2-pp3-balanced/README.md). Context, cache and runtime versions can differ.

## Saved Configuration Versions

Each configuration ID identifies a distinct original settings record. Deployment fields are omitted; versions can have identical published settings after that omission. Upstream runtime commits remain unspecified where the source retained only an integration label.

| Configuration | Recorded artifact / source | Configured card counts | Context tokens | GPU pool tokens | Slots | Draft mode / tokens |
| --- | --- | --- | --- | --- | --- | --- |
| cfg-ddef0ee04e434a97be5b | [svbmrgd/apex-flash-1-abliterated-AWQ@7ea31e3d22](https://huggingface.co/svbmrgd/apex-flash-1-abliterated-AWQ/tree/7ea31e3d22c6622c999d3de74d1569efce815943) | 3 | 524,288 | Not recorded | 4 | dflash2 / 3 |

Card counts are saved configuration choices, not a claim that every allowed placement was measured. A derived view can differ from its pinned download source.

<details>
<summary>cfg-ddef0ee04e434a97be5b</summary>

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
    14,
    14
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

| Profile / Wave | Layout; Draft / Tokens | Requests | Input tokens/request | Accepted output tokens/request | Cache / Reused input tokens | Context / GPU pool tokens | Shared decode tok/s total | Client after-first-token estimate tok/s | Whole-wave output tok/s | Median TTFT, s | Source report |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [ad025-apex-awq-dflash2-pp3-fast-001](ad025-apex-awq-dflash2-pp3-fast-001.md)<br>wave-9cf961df92c1c4470108 | pipeline_parallel; dflash2 / 3 | 1 | 32,771 | 8,192 (budget 8,192) | repeated_input; reused - | 524,288 / - | Not recorded | 61.80 | Not recorded | 7.89 | Unspecified |
| [ad025-apex-awq-dflash2-pp3-fast-001](ad025-apex-awq-dflash2-pp3-fast-001.md)<br>wave-cae6b1aab9f694c6b4c7 | pipeline_parallel; dflash2 / 3 | 1 | 32,771 | 8,192 (budget 8,192) | cold; reused - | 524,288 / - | Not recorded | 51.35 | Not recorded | 16.76 | Unspecified |

Rates are whole-wave totals over the stated request count. A wave may span multiple independent model instances; [measurements.json](../measurements.json) retains their contributions and the exact configuration IDs. Do not interpret a multi-instance total as one card's rate.

A dash in shared decode means no qualified synchronized interval is available. Whole-wave throughput includes prefill and queueing. A valid decode interval can survive inside an overall failed or partial check; the source-report outcome is preserved. No rows are averaged.

## Additional Test Results

| Result / Source | Profile | Evidence type | Reported outcome | Retained values | Configuration binding |
| --- | --- | --- | --- | --- | --- |
| [result-950cfe1cdb7b636e3c0c](../observations.json)<br>source-797606345fa45914fcd85b71.json<br>`/profiles/apex-abliterated-awq-dflash2-pp3-fast/long_output` | [ad025-apex-awq-dflash2-pp3-fast-001](ad025-apex-awq-dflash2-pp3-fast-001.md)<br>[apex-abliterated-awq-dflash2-pp3-fast](apex-abliterated-awq-dflash2-pp3-fast.md) | test outcome | Outcome unspecified | actual_tokenizer_input=32,771 tokens; output_tokens=8,192 tokens; complete_answer_quality_test=false | Recorded configuration/job |
| [result-a2a35178de2c19ff7af7](../observations.json)<br>source-797606345fa45914fcd85b71.json<br>`/profiles/apex-abliterated-awq-dflash2-pp3-fast/long_output/waves/0` | [ad025-apex-awq-dflash2-pp3-fast-001](ad025-apex-awq-dflash2-pp3-fast-001.md)<br>[apex-abliterated-awq-dflash2-pp3-fast](apex-abliterated-awq-dflash2-pp3-fast.md) | performance detail | Outcome unspecified | Draft accepted / proposed: 5,629.00 / 7,689.00 tokens; fraction 0.7321; cache_hit_verified=false | Recorded configuration/job |
| [result-aa0e0ee85caad0bd65ff](../observations.json)<br>source-797606345fa45914fcd85b71.json<br>`/profiles/apex-abliterated-awq-dflash2-pp3-fast/long_output/waves/1` | [ad025-apex-awq-dflash2-pp3-fast-001](ad025-apex-awq-dflash2-pp3-fast-001.md)<br>[apex-abliterated-awq-dflash2-pp3-fast](apex-abliterated-awq-dflash2-pp3-fast.md) | performance detail | Outcome unspecified | Draft accepted / proposed: 6,038.00 / 6,462.00 tokens; fraction 0.9344 | Recorded configuration/job |

These are saved result records, including failures and bounded checks. Copies, individual requests, report summaries and regrading can overlap; their counts are not independent test repetitions. Open each result for exact values, units, configuration binding and source receipts.

There are 1 retained lifecycle records. Their states, exit codes and configuration IDs remain in [catalog.json](../catalog.json); they do not supply missing benchmark results.

[Full archive](../../README.md) | [All retained waves](../RESULTS.md) | [Data definitions](../DATA.md) | [Recommended recipes](../../../README.md)
