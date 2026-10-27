# qwen-flash-next-int4-huge-sm-write-pair01

**Historical record. Decode interval measured.**

Model family: Qwen 3.8 Flash Next.

Recorded archive reason: Optional transport experiment; measured SM-write P2P was slower than host paths.

Historical configurations are provided for comparison. The [recommended recipes](../../../README.md) include supported launch scripts.

## Saved Configuration Versions

Each configuration ID identifies a distinct original settings record. Deployment fields are omitted; versions can have identical published settings after that omission. Upstream runtime commits remain unspecified where the source retained only an integration label.

| Configuration | Recorded artifact / source | Configured card counts | Context tokens | GPU pool tokens | Slots | Draft mode / tokens |
| --- | --- | --- | --- | --- | --- | --- |
| cfg-3591baaab5e68a56f380 | [zankich/Qwen3.8-Flash-Next-W4A16-Merlin-INT4PLE-FP8KV@45d5db34e0](https://huggingface.co/zankich/Qwen3.8-Flash-Next-W4A16-Merlin-INT4PLE-FP8KV/tree/45d5db34e05a826d0ca150d4526bc29fd2958d63) | 2 | 32,768 | Not recorded | 4 | mtp / 3 |

Card counts are saved configuration choices, not a claim that every allowed placement was measured. A derived view can differ from its pinned download source.

<details>
<summary>cfg-3591baaab5e68a56f380</summary>

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
  "ordinary_memory_max_gib": null,
  "model_repository": "zankich/Qwen3.8-Flash-Next-W4A16-Merlin-INT4PLE-FP8KV",
  "model_revision": "45d5db34e05a826d0ca150d4526bc29fd2958d63",
  "draft_repository": null,
  "draft_revision": null,
  "recorded_runtime_label": "qwen-int4-ple-sm-write-r1",
  "served_model_label": "qwen3.8-flash-next"
}
```

Pinned model revision recorded: yes. Source receipt labels, hashes and object locators are retained in [configurations.json](../configurations.json).

</details>

## Retained Measurements

| Profile / Wave | Layout; Draft / Tokens | Requests | Input tokens/request | Accepted output tokens/request | Cache / Reused input tokens | Context / GPU pool tokens | Shared decode tok/s total | Client after-first-token estimate tok/s | Whole-wave output tok/s | Median TTFT, s | Source report |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [qwen-flash-next-int4-huge-sm-write-pair01](qwen-flash-next-int4-huge-sm-write-pair01.md)<br>wave-04df049064d3b5845e6b | layout unspecified; mtp / 3 | 1 | 4,093 | 256 | unspecified; reused - | 32,768 / - | 66.20 | Not recorded | Not recorded | 5.10 | Pass |
| [qwen-flash-next-int4-huge-sm-write-pair01](qwen-flash-next-int4-huge-sm-write-pair01.md)<br>wave-f7941e82a724c4922b00 | layout unspecified; mtp / 3 | 2 | 4,093 | 256 | unspecified; reused - | 32,768 / - | 158.26 | Not recorded | Not recorded | 1.40 | Pass |

Rates are whole-wave totals over the stated request count. A wave may span multiple independent model instances; [measurements.json](../measurements.json) retains their contributions and the exact configuration IDs. Do not interpret a multi-instance total as one card's rate.

A dash in shared decode means no qualified synchronized interval is available. Whole-wave throughput includes prefill and queueing. A valid decode interval can survive inside an overall failed or partial check; the source-report outcome is preserved. No rows are averaged.

## Bounded Checks

| Check | Reported outcome | Retained counts / flags |
| --- | --- | --- |
| check-2aea9af0e6f30c5943cf | Pass | {"concurrency":2,"passed":true,"wall_seconds":5.7912330309991376,"input_tokens":[4093,4093]} |
| check-a275b1b1a88d8df722bc | Pass | {"concurrency":1,"passed":true,"wall_seconds":8.987835676998657,"input_tokens":[4093]} |
| check-a6f6bd4d84bf0e6dd141 | Pass | {"concurrency":1,"passed":true,"wall_seconds":8.987835676998657,"input_tokens":[4093]} |
| check-e64250779899afa2b2c3 | Pass | {"concurrency":2,"passed":true,"wall_seconds":5.7912330309991376,"input_tokens":[4093,4093]} |

These checks retain their reported scope. A context/allocation/retrieval check is not a general quality score or a speed qualification at that context. Exact flags and provenance are in [checks.json](../checks.json).

## Additional Test Results

| Result / Source | Profile | Evidence type | Reported outcome | Retained values | Configuration binding |
| --- | --- | --- | --- | --- | --- |
| [result-2d40d6cfdac0088144a7](../observations.json)<br>source-1dfa5c7268dbbb6a63ab6f36.json<br>`/client/measurements/0/traces/0` | [qwen-flash-next-int4-huge-sm-write-pair01](qwen-flash-next-int4-huge-sm-write-pair01.md) | test outcome | complete | generated_tokens=256 accepted tokens | Recorded configuration/job |
| [result-5c12dad72cd6b0c59324](../observations.json)<br>source-1dfa5c7268dbbb6a63ab6f36.json<br>`/client/measurements/1/traces/1` | [qwen-flash-next-int4-huge-sm-write-pair01](qwen-flash-next-int4-huge-sm-write-pair01.md) | test outcome | complete | generated_tokens=256 accepted tokens | Recorded configuration/job |
| [result-9c54a6461e53c07a760d](../observations.json)<br>source-1dfa5c7268dbbb6a63ab6f36.json<br>`/client/measurements/0` | [qwen-flash-next-int4-huge-sm-write-pair01](qwen-flash-next-int4-huge-sm-write-pair01.md) | test outcome | Pass | concurrency=1 requests; input_tokens=4,093 tokens; wall_seconds=8.99 s | Recorded configuration/job |
| [result-a2941a31aa65f500d257](../observations.json)<br>source-1dfa5c7268dbbb6a63ab6f36.json<br>`/client/measurements/1` | [qwen-flash-next-int4-huge-sm-write-pair01](qwen-flash-next-int4-huge-sm-write-pair01.md) | test outcome | Pass | concurrency=2 requests; input_tokens=4,093 tokens; wall_seconds=5.79 s | Recorded configuration/job |
| [result-e3f633ebc0b4362eea3f](../observations.json)<br>source-1dfa5c7268dbbb6a63ab6f36.json<br>`/client/measurements/1/traces/0` | [qwen-flash-next-int4-huge-sm-write-pair01](qwen-flash-next-int4-huge-sm-write-pair01.md) | test outcome | complete | generated_tokens=256 accepted tokens | Recorded configuration/job |

These are saved result records, including failures and bounded checks. Copies, individual requests, report summaries and regrading can overlap; their counts are not independent test repetitions. Open each result for exact values, units, configuration binding and source receipts.

There are 1 retained lifecycle records. Their states, exit codes and configuration IDs remain in [catalog.json](../catalog.json); they do not supply missing benchmark results.

[Full archive](../../README.md) | [All retained waves](../RESULTS.md) | [Data definitions](../DATA.md) | [Recommended recipes](../../../README.md)
