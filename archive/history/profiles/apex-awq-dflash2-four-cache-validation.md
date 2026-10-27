# apex-awq-dflash2-four-cache-validation

**Historical record. Additional test results; no matched decode wave.**

Model family: Apex Flash 1 (GLM 5.3 Flash post-train).

Recorded archive reason: Ordinary or four-card capacity comparison; speculative and other card-count configurations have separate records.

Historical configurations are provided for comparison. The [recommended recipes](../../../README.md) include supported launch scripts.

Current recipes using the same recorded checkpoint repository: [apex-abliterated-awq-dflash2-pp3-balanced](../../../recipes/apex-abliterated-awq-dflash2-pp3-balanced/README.md). Context, cache and runtime versions can differ.

## Saved Configuration Versions

Each configuration ID identifies a distinct original settings record. Deployment fields are omitted; versions can have identical published settings after that omission. Upstream runtime commits remain unspecified where the source retained only an integration label.

| Configuration | Recorded artifact / source | Configured card counts | Context tokens | GPU pool tokens | Slots | Draft mode / tokens |
| --- | --- | --- | --- | --- | --- | --- |
| cfg-532080020ac7f17a06d6 | [svbmrgd/apex-flash-1-abliterated-AWQ@7ea31e3d22](https://huggingface.co/svbmrgd/apex-flash-1-abliterated-AWQ/tree/7ea31e3d22c6622c999d3de74d1569efce815943) | 4 | 32,768 | Not recorded | 2 | dflash2 / 7 |

Card counts are saved configuration choices, not a claim that every allowed placement was measured. A derived view can differ from its pinned download source.

<details>
<summary>cfg-532080020ac7f17a06d6</summary>

```json
{
  "kind": "vllm_apex_awq",
  "gpu_counts": [
    4
  ],
  "context": 32768,
  "kv_dtype": "bfloat16",
  "draft_mode": "dflash2",
  "draft_tokens": 7,
  "max_sessions": 2,
  "chunk_size": 1280,
  "ram_kv_mib": 8192,
  "power_watts": 200,
  "host_memory_gib": 80,
  "host_swap_gib": 0,
  "min_vram_mib_per_gpu": 65530,
  "min_effective_vram_mib": 262120,
  "tensor_parallel_size": 1,
  "pipeline_parallel_size": 4,
  "pipeline_layer_partition": [
    12,
    11,
    11,
    11
  ],
  "kv_cache_mib_per_gpu": 4096,
  "enforce_eager": true,
  "mamba_cache_mode": "align",
  "model_repository": "svbmrgd/apex-flash-1-abliterated-AWQ",
  "model_revision": "7ea31e3d22c6622c999d3de74d1569efce815943",
  "draft_repository": "incoai/GLM-5.3-Flash-DFlash2",
  "draft_revision": "bf582e4eacc1810f76656d1811693ff6c6737d2a",
  "recorded_runtime_label": "apex-awq-dflash2-pp4-cache-r2",
  "served_model_label": "apex-flash-1-abliterated-awq-dflash2",
  "draft_directory_template": "@DRAFT_ROOT@"
}
```

Pinned model revision recorded: yes. Source receipt labels, hashes and object locators are retained in [configurations.json](../configurations.json).

</details>

## Retained Measurements

No detailed benchmark receipt is matched to this record. A saved definition or a successful job exit alone is not a performance measurement.

A dash in shared decode means no qualified synchronized interval is available. Whole-wave throughput includes prefill and queueing. A valid decode interval can survive inside an overall failed or partial check; the source-report outcome is preserved. No rows are averaged.

## Additional Test Results

| Result / Source | Profile | Evidence type | Reported outcome | Retained values | Configuration binding |
| --- | --- | --- | --- | --- | --- |
| [result-d4c6a332870d894d1482](../observations.json)<br>source-ab89fca7e0f49696d5258b56.json<br>`/profiles/0/current_config` | [apex-awq-dflash2-four-cache-validation](apex-awq-dflash2-four-cache-validation.md) | test outcome | Outcome unspecified | context=32,768 tokens | Recorded configuration/job |

These are saved result records, including failures and bounded checks. Copies, individual requests, report summaries and regrading can overlap; their counts are not independent test repetitions. Open each result for exact values, units, configuration binding and source receipts.

There are 3 retained lifecycle records. Their states, exit codes and configuration IDs remain in [catalog.json](../catalog.json); they do not supply missing benchmark results.

[Full archive](../../README.md) | [All retained waves](../RESULTS.md) | [Data definitions](../DATA.md) | [Recommended recipes](../../../README.md)
