# ad025-apex-awq-dflash2-pp3-balanced-000

**Historical record. Legacy / incomplete measurements.**

Model family: Apex Flash 1 (GLM 5.3 Flash post-train).

Historical configurations are provided for comparison. The [recommended recipes](../../../README.md) include supported launch scripts.

Current recipes using the same recorded checkpoint repository: [apex-abliterated-awq-dflash2-pp3-balanced](../../../recipes/apex-abliterated-awq-dflash2-pp3-balanced/README.md). Context, cache and runtime versions can differ.

## Saved Configuration Versions

Each configuration ID identifies a distinct original settings record. Deployment fields are omitted; versions can have identical published settings after that omission. Upstream runtime commits remain unspecified where the source retained only an integration label.

| Configuration | Recorded artifact / source | Configured card counts | Context tokens | GPU pool tokens | Slots | Draft mode / tokens |
| --- | --- | --- | --- | --- | --- | --- |
| cfg-08bd8648f61e95abbd68 | [svbmrgd/apex-flash-1-abliterated-AWQ@7ea31e3d22](https://huggingface.co/svbmrgd/apex-flash-1-abliterated-AWQ/tree/7ea31e3d22c6622c999d3de74d1569efce815943) | 3 | 524,288 | Not recorded | 4 | dflash2 / 3 |

Card counts are saved configuration choices, not a claim that every allowed placement was measured. A derived view can differ from its pinned download source.

<details>
<summary>cfg-08bd8648f61e95abbd68</summary>

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

| Profile / Wave | Layout; Draft / Tokens | Requests | Input tokens/request | Accepted output tokens/request | Cache / Reused input tokens | Context / GPU pool tokens | Shared decode tok/s total | Client after-first-token estimate tok/s | Whole-wave output tok/s | Median TTFT, s | Source report |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [ad025-apex-awq-dflash2-pp3-balanced-000](ad025-apex-awq-dflash2-pp3-balanced-000.md)<br>wave-289c9ef4d8383eb4444e | pipeline_parallel; dflash2 / 3 | 1 | 32,771 | 8,192 (budget 8,192) | cold; reused - | 524,288 / - | Not recorded | 58.87 | Not recorded | 16.82 | Unspecified |
| [ad025-apex-awq-dflash2-pp3-balanced-000](ad025-apex-awq-dflash2-pp3-balanced-000.md)<br>wave-9ce336dec7b5789eb248 | pipeline_parallel; dflash2 / 3 | 1 | 32,771 | 8,192 (budget 8,192) | repeated_input; reused - | 524,288 / - | Not recorded | 62.32 | Not recorded | 8.15 | Unspecified |

Rates are whole-wave totals over the stated request count. A wave may span multiple independent model instances; [measurements.json](../measurements.json) retains their contributions and the exact configuration IDs. Do not interpret a multi-instance total as one card's rate.

A dash in shared decode means no qualified synchronized interval is available. Whole-wave throughput includes prefill and queueing. A valid decode interval can survive inside an overall failed or partial check; the source-report outcome is preserved. No rows are averaged.

## Additional Test Results

| Result / Source | Profile | Evidence type | Reported outcome | Retained values | Configuration binding |
| --- | --- | --- | --- | --- | --- |
| [result-5c5d7bd38f9fc4081b01](../observations.json)<br>source-797606345fa45914fcd85b71.json<br>`/profiles/apex-abliterated-awq-dflash2-pp3-balanced/long_output/waves/0` | [ad025-apex-awq-dflash2-pp3-balanced-000](ad025-apex-awq-dflash2-pp3-balanced-000.md)<br>[apex-abliterated-awq-dflash2-pp3-balanced](apex-abliterated-awq-dflash2-pp3-balanced.md) | performance detail | Outcome unspecified | Draft accepted / proposed: 5,876.00 / 6,951.00 tokens; fraction 0.8453; cache_hit_verified=false | Recorded configuration/job |
| [result-b8e47150873eaf7dd587](../observations.json)<br>source-797606345fa45914fcd85b71.json<br>`/profiles/apex-abliterated-awq-dflash2-pp3-balanced/long_output/waves/1` | [ad025-apex-awq-dflash2-pp3-balanced-000](ad025-apex-awq-dflash2-pp3-balanced-000.md)<br>[apex-abliterated-awq-dflash2-pp3-balanced](apex-abliterated-awq-dflash2-pp3-balanced.md) | performance detail | Outcome unspecified | Draft accepted / proposed: 6,039.00 / 6,462.00 tokens; fraction 0.9345 | Recorded configuration/job |
| [result-e04c9601d6963dcbcc1d](../observations.json)<br>source-797606345fa45914fcd85b71.json<br>`/profiles/apex-abliterated-awq-dflash2-pp3-balanced/raw_followup/quality` | [ad025-apex-awq-dflash2-pp3-balanced-000](ad025-apex-awq-dflash2-pp3-balanced-000.md)<br>[apex-abliterated-awq-dflash2-pp3-balanced](apex-abliterated-awq-dflash2-pp3-balanced.md) | quality evaluation | 8 / 8 tasks passed | Task latency median 3.21 s; n=8 | Recorded configuration/job |
| [result-f85b8398f2b7d4e21525](../observations.json)<br>source-797606345fa45914fcd85b71.json<br>`/profiles/apex-abliterated-awq-dflash2-pp3-balanced/long_output` | [ad025-apex-awq-dflash2-pp3-balanced-000](ad025-apex-awq-dflash2-pp3-balanced-000.md)<br>[apex-abliterated-awq-dflash2-pp3-balanced](apex-abliterated-awq-dflash2-pp3-balanced.md) | test outcome | Outcome unspecified | actual_tokenizer_input=32,771 tokens; output_tokens=8,192 tokens; complete_answer_quality_test=false | Recorded configuration/job |

These are saved result records, including failures and bounded checks. Copies, individual requests, report summaries and regrading can overlap; their counts are not independent test repetitions. Open each result for exact values, units, configuration binding and source receipts.

There are 1 retained lifecycle records. Their states, exit codes and configuration IDs remain in [catalog.json](../catalog.json); they do not supply missing benchmark results.

[Full archive](../../README.md) | [All retained waves](../RESULTS.md) | [Data definitions](../DATA.md) | [Recommended recipes](../../../README.md)
