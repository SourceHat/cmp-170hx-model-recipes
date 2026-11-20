# qwen-flash-next-int4-pinned-host-pair01

**Historical record. Decode interval measured.**

Model family: Qwen 3.8 Flash Next.

Historical configurations are provided for comparison. The [recommended recipes](../../../README.md) include supported launch scripts.

## Saved Configuration Versions

Each configuration ID identifies a distinct original settings record. Deployment fields are omitted; versions can have identical published settings after that omission. Upstream runtime commits remain unspecified where the source retained only an integration label.

| Configuration | Recorded artifact / source | Configured card counts | Context tokens | GPU pool tokens | Slots | Draft mode / tokens |
| --- | --- | --- | --- | --- | --- | --- |
| cfg-45390960e141254ab19f | [zankich/Qwen3.8-Flash-Next-W4A16-Merlin-INT4PLE-FP8KV@45d5db34e0](https://huggingface.co/zankich/Qwen3.8-Flash-Next-W4A16-Merlin-INT4PLE-FP8KV/tree/45d5db34e05a826d0ca150d4526bc29fd2958d63) | 2 | 32,768 | Not recorded | 4 | mtp / 3 |

Card counts are saved configuration choices, not a claim that every allowed placement was measured. A derived view can differ from its pinned download source.

<details>
<summary>cfg-45390960e141254ab19f</summary>

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
  "ple_host_backing": "pinned",
  "nccl_transport": "host",
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
| [qwen-flash-next-int4-pinned-host-pair01](qwen-flash-next-int4-pinned-host-pair01.md)<br>wave-01f293e0a7317edd902b | layout unspecified; mtp / 3 | 1 | 4,093 | 256 | unspecified; reused - | 32,768 / - | 87.48 | Not recorded | Not recorded | 1.03 | Failed / partial |
| [qwen-flash-next-int4-pinned-host-pair01](qwen-flash-next-int4-pinned-host-pair01.md)<br>wave-a022e5e66c48e823f906 | layout unspecified; mtp / 3 | 2 | 4,093 | 256 | unspecified; reused - | 32,768 / - | 183.17 | Not recorded | Not recorded | 0.74 | Failed / partial |

Rates are whole-wave totals over the stated request count. A wave may span multiple independent model instances; [measurements.json](../measurements.json) retains their contributions and the exact configuration IDs. Do not interpret a multi-instance total as one card's rate.

A dash in shared decode means no qualified synchronized interval is available. Whole-wave throughput includes prefill and queueing. A valid decode interval can survive inside an overall failed or partial check; the source-report outcome is preserved. No rows are averaged.

## Bounded Checks

| Check | Reported outcome | Retained counts / flags |
| --- | --- | --- |
| check-0296c04b6e7b46c25dc1 | Pass | {"concurrency":2,"passed":true,"wall_seconds":4.0162148349991185,"input_tokens":[4093,4093]} |
| check-46c7b2172e040dac3ecd | Pass | {"concurrency":2,"passed":true,"wall_seconds":4.0162148349991185,"input_tokens":[4093,4093]} |
| check-480150886e38660fe926 | Pass | {"concurrency":2,"passed":true,"wall_seconds":4.0162148349991185,"input_tokens":[4093,4093]} |
| check-53ece2a4e67a5a157ea3 | Pass | {"concurrency":1,"passed":true,"wall_seconds":3.949164968005789,"input_tokens":[4093]} |
| check-ba811a1499a6a15105ee | Pass | {"concurrency":1,"passed":true,"wall_seconds":3.949164968005789,"input_tokens":[4093]} |
| check-c3e19d2a975f19fafc7d | Pass | {"concurrency":1,"passed":true,"wall_seconds":3.949164968005789,"input_tokens":[4093]} |

These checks retain their reported scope. A context/allocation/retrieval check is not a general quality score or a speed qualification at that context. Exact flags and provenance are in [checks.json](../checks.json).

## Additional Test Results

| Result / Source | Profile | Evidence type | Reported outcome | Retained values | Configuration binding |
| --- | --- | --- | --- | --- | --- |
| [result-075acec4f8dfe2ef026b](../observations.json)<br>source-3b144178622ccb57c0f150f4.json<br>`/phases/vllm_host_p2p/phases/pinned_host` | [qwen-flash-next-int4-pinned-host-pair01](qwen-flash-next-int4-pinned-host-pair01.md) | test outcome | Failed / partial | passed=false | Recorded configuration/job |
| [result-2b3579869c75a01f2ac2](../observations.json)<br>source-1dd75531a7f73c95e8fb249d.json<br>`/phases/vllm_host_p2p/phases/pinned_host/client/measurements/0` | [qwen-flash-next-int4-pinned-host-pair01](qwen-flash-next-int4-pinned-host-pair01.md) | test outcome | Pass | concurrency=1 requests; input_tokens=4,093 tokens; wall_seconds=3.95 s | Recorded configuration/job |
| [result-7a7a1a47866bab21a342](../observations.json)<br>source-1dd75531a7f73c95e8fb249d.json<br>`/phases/vllm_host_p2p/phases/pinned_host/client/measurements/1/traces/1` | [qwen-flash-next-int4-pinned-host-pair01](qwen-flash-next-int4-pinned-host-pair01.md) | test outcome | complete | generated_tokens=256 accepted tokens | Recorded configuration/job |
| [result-b56b0e5738efa688d25e](../observations.json)<br>source-1dd75531a7f73c95e8fb249d.json<br>`/phases/vllm_host_p2p/phases/pinned_host/client/measurements/1/traces/0` | [qwen-flash-next-int4-pinned-host-pair01](qwen-flash-next-int4-pinned-host-pair01.md) | test outcome | complete | generated_tokens=256 accepted tokens | Recorded configuration/job |
| [result-fa99691af39fdbbdea58](../observations.json)<br>source-1dd75531a7f73c95e8fb249d.json<br>`/phases/vllm_host_p2p/phases/pinned_host/client/measurements/1` | [qwen-flash-next-int4-pinned-host-pair01](qwen-flash-next-int4-pinned-host-pair01.md) | test outcome | Pass | concurrency=2 requests; input_tokens=4,093 tokens; wall_seconds=4.02 s | Recorded configuration/job |
| [result-fc8716984a452a1a2190](../observations.json)<br>source-1dd75531a7f73c95e8fb249d.json<br>`/phases/vllm_host_p2p/phases/pinned_host/client/measurements/0/traces/0` | [qwen-flash-next-int4-pinned-host-pair01](qwen-flash-next-int4-pinned-host-pair01.md) | test outcome | complete | generated_tokens=256 accepted tokens | Recorded configuration/job |

These are saved result records, including failures and bounded checks. Copies, individual requests, report summaries and regrading can overlap; their counts are not independent test repetitions. Open each result for exact values, units, configuration binding and source receipts.

There are 3 retained lifecycle records. Their states, exit codes and configuration IDs remain in [catalog.json](../catalog.json); they do not supply missing benchmark results.

[Full archive](../../README.md) | [All retained waves](../RESULTS.md) | [Data definitions](../DATA.md) | [Recommended recipes](../../../README.md)
