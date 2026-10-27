# qwen-flash-next-int4-huge-host-pair01

**Historical record. Decode interval measured.**

Model family: Qwen 3.8 Flash Next.

Historical configurations are provided for comparison. The [recommended recipes](../../../README.md) include supported launch scripts.

## Saved Configuration Versions

Each configuration ID identifies a distinct original settings record. Deployment fields are omitted; versions can have identical published settings after that omission. Upstream runtime commits remain unspecified where the source retained only an integration label.

| Configuration | Recorded artifact / source | Configured card counts | Context tokens | GPU pool tokens | Slots | Draft mode / tokens |
| --- | --- | --- | --- | --- | --- | --- |
| cfg-1314be51c3c1ae41919c | [zankich/Qwen3.8-Flash-Next-W4A16-Merlin-INT4PLE-FP8KV@45d5db34e0](https://huggingface.co/zankich/Qwen3.8-Flash-Next-W4A16-Merlin-INT4PLE-FP8KV/tree/45d5db34e05a826d0ca150d4526bc29fd2958d63) | 2 | 32,768 | Not recorded | 4 | mtp / 3 |

Card counts are saved configuration choices, not a claim that every allowed placement was measured. A derived view can differ from its pinned download source.

<details>
<summary>cfg-1314be51c3c1ae41919c</summary>

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
  "nccl_transport": "host",
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

| Profile / Wave | Layout; Draft / Tokens | Requests | Input tokens/request | Accepted output tokens/request | Cache / Reused input tokens | Context / GPU pool tokens | Shared decode tok/s total | Client after-first-token estimate tok/s | Whole-wave output tok/s | Median TTFT, s | Source report |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [qwen-flash-next-int4-huge-host-pair01](qwen-flash-next-int4-huge-host-pair01.md)<br>wave-113f6019a33854a10b5c | layout unspecified; mtp / 3 | 2 | 4,093 | 256 | unspecified; reused - | 32,768 / - | 180.19 | Not recorded | Not recorded | 0.88 | Failed / partial |
| [qwen-flash-next-int4-huge-host-pair01](qwen-flash-next-int4-huge-host-pair01.md)<br>wave-8ec04958e89fac9130b2 | layout unspecified; mtp / 3 | 1 | 4,093 | 256 | unspecified; reused - | 32,768 / - | 101.85 | Not recorded | Not recorded | 1.01 | Failed / partial |

Rates are whole-wave totals over the stated request count. A wave may span multiple independent model instances; [measurements.json](../measurements.json) retains their contributions and the exact configuration IDs. Do not interpret a multi-instance total as one card's rate.

A dash in shared decode means no qualified synchronized interval is available. Whole-wave throughput includes prefill and queueing. A valid decode interval can survive inside an overall failed or partial check; the source-report outcome is preserved. No rows are averaged.

## Bounded Checks

| Check | Reported outcome | Retained counts / flags |
| --- | --- | --- |
| check-0bf844e5c57678335d72 | Pass | {"concurrency":1,"passed":true,"wall_seconds":3.5399801960011246,"input_tokens":[4093]} |
| check-c44f608d9195eb3407f4 | Pass | {"concurrency":2,"passed":true,"wall_seconds":3.9967964840034256,"input_tokens":[4093,4093]} |
| check-c60718fa34b78a06aa1f | Pass | {"concurrency":1,"passed":true,"wall_seconds":3.5399801960011246,"input_tokens":[4093]} |
| check-d073587c0c47d344abf3 | Pass | {"concurrency":2,"passed":true,"wall_seconds":3.9967964840034256,"input_tokens":[4093,4093]} |
| check-f3bc06906ddfe33b91fb | Pass | {"concurrency":1,"passed":true,"wall_seconds":3.5399801960011246,"input_tokens":[4093]} |
| check-faaf82c04aa28b2445bc | Pass | {"concurrency":2,"passed":true,"wall_seconds":3.9967964840034256,"input_tokens":[4093,4093]} |

These checks retain their reported scope. A context/allocation/retrieval check is not a general quality score or a speed qualification at that context. Exact flags and provenance are in [checks.json](../checks.json).

## Additional Test Results

| Result / Source | Profile | Evidence type | Reported outcome | Retained values | Configuration binding |
| --- | --- | --- | --- | --- | --- |
| [result-05379d24abb38006ea61](../observations.json)<br>source-1dd75531a7f73c95e8fb249d.json<br>`/phases/vllm_host_p2p/phases/huge_host/client/measurements/0/traces/0` | [qwen-flash-next-int4-huge-host-pair01](qwen-flash-next-int4-huge-host-pair01.md) | test outcome | complete | generated_tokens=256 accepted tokens | Recorded configuration/job |
| [result-3950ceb8789b55e3c452](../observations.json)<br>source-1dd75531a7f73c95e8fb249d.json<br>`/phases/vllm_host_p2p/phases/huge_host/client/measurements/1/traces/0` | [qwen-flash-next-int4-huge-host-pair01](qwen-flash-next-int4-huge-host-pair01.md) | test outcome | complete | generated_tokens=256 accepted tokens | Recorded configuration/job |
| [result-424dbfb24186693f5465](../observations.json)<br>source-1dd75531a7f73c95e8fb249d.json<br>`/phases/vllm_host_p2p/phases/huge_host/client/measurements/1` | [qwen-flash-next-int4-huge-host-pair01](qwen-flash-next-int4-huge-host-pair01.md) | test outcome | Pass | concurrency=2 requests; input_tokens=4,093 tokens; wall_seconds=4.00 s | Recorded configuration/job |
| [result-842c3a879f073dbbacbf](../observations.json)<br>source-1dd75531a7f73c95e8fb249d.json<br>`/phases/vllm_host_p2p/phases/huge_host/client/measurements/0` | [qwen-flash-next-int4-huge-host-pair01](qwen-flash-next-int4-huge-host-pair01.md) | test outcome | Pass | concurrency=1 requests; input_tokens=4,093 tokens; wall_seconds=3.54 s | Recorded configuration/job |
| [result-c5694b2d9c0d9f09a9bd](../observations.json)<br>source-1dd75531a7f73c95e8fb249d.json<br>`/phases/vllm_host_p2p/phases/huge_host/client/measurements/1/traces/1` | [qwen-flash-next-int4-huge-host-pair01](qwen-flash-next-int4-huge-host-pair01.md) | test outcome | complete | generated_tokens=256 accepted tokens | Recorded configuration/job |

These are saved result records, including failures and bounded checks. Copies, individual requests, report summaries and regrading can overlap; their counts are not independent test repetitions. Open each result for exact values, units, configuration binding and source receipts.

There are 1 retained lifecycle records. Their states, exit codes and configuration IDs remain in [catalog.json](../catalog.json); they do not supply missing benchmark results.

[Full archive](../../README.md) | [All retained waves](../RESULTS.md) | [Data definitions](../DATA.md) | [Recommended recipes](../../../README.md)
