# qwen-flash-next-int4-huge-p2p-pair01

**Historical record. Additional test results; no matched decode wave.**

Model family: Qwen 3.8 Flash Next.

Recorded archive reason: Failed copy-engine/CUMEM P2P candidate; tested pinned/huge host paths retained.

Historical configurations are provided for comparison. The [recommended recipes](../../../README.md) include supported launch scripts.

## Saved Configuration Versions

Each configuration ID identifies a distinct original settings record. Deployment fields are omitted; versions can have identical published settings after that omission. Upstream runtime commits remain unspecified where the source retained only an integration label.

| Configuration | Recorded artifact / source | Configured card counts | Context tokens | GPU pool tokens | Slots | Draft mode / tokens |
| --- | --- | --- | --- | --- | --- | --- |
| cfg-a44a96282d60e688f35b | [zankich/Qwen3.8-Flash-Next-W4A16-Merlin-INT4PLE-FP8KV@45d5db34e0](https://huggingface.co/zankich/Qwen3.8-Flash-Next-W4A16-Merlin-INT4PLE-FP8KV/tree/45d5db34e05a826d0ca150d4526bc29fd2958d63) | 2 | 32,768 | Not recorded | 4 | mtp / 3 |

Card counts are saved configuration choices, not a claim that every allowed placement was measured. A derived view can differ from its pinned download source.

<details>
<summary>cfg-a44a96282d60e688f35b</summary>

```json
{
  "kind": "vllm_qwen_int4",
  "gpu_counts": [
    2
  ],
  "context": 32768,
  "kv_dtype": "bfloat16",
  "draft_mode": "mtp",
  "draft_tokens": 3,
  "max_sessions": 4,
  "chunk_size": 1280,
  "ram_kv_mib": 8192,
  "power_watts": 200,
  "host_memory_gib": 80,
  "host_swap_gib": 0,
  "min_vram_mib_per_gpu": 65530,
  "min_effective_vram_mib": 128000,
  "tensor_parallel_size": 1,
  "pipeline_parallel_size": 2,
  "kv_cache_mib_per_gpu": 1024,
  "enforce_eager": true,
  "mamba_cache_mode": "align",
  "ple_backend": "pinned_int4",
  "ple_host_backing": "hugetlb_required",
  "nccl_transport": "pair01_write",
  "hugepage_sizes_mb": [
    2
  ],
  "hugepage_memory_gib": 28,
  "ordinary_memory_max_gib": 52,
  "model_repository": "zankich/Qwen3.8-Flash-Next-W4A16-Merlin-INT4PLE-FP8KV",
  "model_revision": "45d5db34e05a826d0ca150d4526bc29fd2958d63",
  "draft_repository": null,
  "draft_revision": null,
  "recorded_runtime_label": "qwen-int4-ple-pp2-r1",
  "served_model_label": "qwen3.8-flash-next"
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
| [result-89dfc4c8beb062cb2e9f](../observations.json)<br>source-1dd75531a7f73c95e8fb249d.json<br>`/phases/vllm_host_p2p/phases/huge_pair01_write` | [qwen-flash-next-int4-huge-p2p-pair01](qwen-flash-next-int4-huge-p2p-pair01.md) | test outcome | Failed / partial | passed=false | Recorded configuration/job |

These are saved result records, including failures and bounded checks. Copies, individual requests, report summaries and regrading can overlap; their counts are not independent test repetitions. Open each result for exact values, units, configuration binding and source receipts.

There are 1 retained lifecycle records. Their states, exit codes and configuration IDs remain in [catalog.json](../catalog.json); they do not supply missing benchmark results.

[Full archive](../../README.md) | [All retained waves](../RESULTS.md) | [Data definitions](../DATA.md) | [Recommended recipes](../../../README.md)
