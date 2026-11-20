# ad017-glm-mtp1-original-tensor_parallel-matched-102

**Historical record. Decode interval measured.**

Model family: GLM 5.3 Flash.

Historical configurations are provided for comparison. The [recommended recipes](../../../README.md) include supported launch scripts.

Current recipes using the same recorded checkpoint repository: [glm-5.3-flash-mtp1-tp3](../../../recipes/glm-5.3-flash-mtp1-tp3/README.md). Context, cache and runtime versions can differ.

## Saved Configuration Versions

Each configuration ID identifies a distinct original settings record. Deployment fields are omitted; versions can have identical published settings after that omission. Upstream runtime commits remain unspecified where the source retained only an integration label.

| Configuration | Recorded artifact / source | Configured card counts | Context tokens | GPU pool tokens | Slots | Draft mode / tokens |
| --- | --- | --- | --- | --- | --- | --- |
| cfg-ed0c03a0fdd80db83109 | [turboderp/GLM-5.3-Flash-exl3@2a30229e67](https://huggingface.co/turboderp/GLM-5.3-Flash-exl3/tree/2a30229e67012798ba9f0cd832bb78abf4c363d5) | 3 | 262,144 | 262,144 | 4 | mtp / 1 |

Card counts are saved configuration choices, not a claim that every allowed placement was measured. A derived view can differ from its pinned download source.

<details>
<summary>cfg-ed0c03a0fdd80db83109</summary>

```json
{
  "kind": "tabby",
  "gpu_counts": [
    3
  ],
  "context": 262144,
  "cache_tokens": 262144,
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
  "served_model_label": "glm-5.3-flash"
}
```

Pinned model revision recorded: yes. Source receipt labels, hashes and object locators are retained in [configurations.json](../configurations.json).

</details>

## Retained Measurements

| Profile / Wave | Layout; Draft / Tokens | Requests | Input tokens/request | Accepted output tokens/request | Cache / Reused input tokens | Context / GPU pool tokens | Shared decode tok/s total | Client after-first-token estimate tok/s | Whole-wave output tok/s | Median TTFT, s | Source report |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [ad017-glm-mtp1-original-tensor_parallel-matched-102](ad017-glm-mtp1-original-tensor_parallel-matched-102.md)<br>wave-593f6c1c5b8d20a2a004 | tensor_parallel; mtp / 1 | 4 | 32,767 | 256 (budget 256) | cold; reused 0 | 262,144 / 262,144 | 98.59 | Not recorded | 4.88 | 199.40 | Pass |
| [ad017-glm-mtp1-original-tensor_parallel-matched-102](ad017-glm-mtp1-original-tensor_parallel-matched-102.md)<br>wave-66ba79c95bdd451c1508 | tensor_parallel; mtp / 1 | 1 | 32,766 | 256 (budget 256) | cached_prefix; reused 32,512 | 262,144 / 262,144 | 49.08 | Not recorded | 44.63 | 0.58 | Pass |
| [ad017-glm-mtp1-original-tensor_parallel-matched-102](ad017-glm-mtp1-original-tensor_parallel-matched-102.md)<br>wave-6bf3fab603cae2998784 | tensor_parallel; mtp / 1 | 4 | 32,767 | 256 (budget 256) | cached_prefix; reused 32,512 | 262,144 / 262,144 | 100.91 | Not recorded | 82.33 | 2.45 | Pass |
| [ad017-glm-mtp1-original-tensor_parallel-matched-102](ad017-glm-mtp1-original-tensor_parallel-matched-102.md)<br>wave-fe3ba0842df097f4cba4 | tensor_parallel; mtp / 1 | 1 | 32,766 | 256 (budget 256) | cold; reused 0 | 262,144 / 262,144 | 48.85 | Not recorded | 4.69 | 49.44 | Pass |

Rates are whole-wave totals over the stated request count. A wave may span multiple independent model instances; [measurements.json](../measurements.json) retains their contributions and the exact configuration IDs. Do not interpret a multi-instance total as one card's rate.

A dash in shared decode means no qualified synchronized interval is available. Whole-wave throughput includes prefill and queueing. A valid decode interval can survive inside an overall failed or partial check; the source-report outcome is preserved. No rows are averaged.

## Bounded Checks

| Check | Reported outcome | Retained counts / flags |
| --- | --- | --- |
| check-0cfb99e2e073bae91adb | Pass | {"passed":true,"elapsed_seconds":54.620165826000175,"ttft_seconds":[49.43951248999974],"end_to_end_accepted_tok_s":4.6869136358084695} |
| check-17b78732a6bf15565437 | Pass | {"passed":true,"elapsed_seconds":209.74457918500048,"ttft_seconds":[195.74116503500045,199.40169628900003,199.40138635999938,199.40103345000034],"end_to_end_accepted_tok_s":4.882128558358612} |
| check-641587af70c2ea9504c7 | Pass | {"passed":true,"elapsed_seconds":54.620165826000175,"ttft_seconds":[49.43951248999974],"end_to_end_accepted_tok_s":4.6869136358084695} |
| check-9762a08f4f5d9f36efac | Pass | {"passed":true,"elapsed_seconds":209.74457918500048,"ttft_seconds":[195.74116503500045,199.40169628900003,199.40138635999938,199.40103345000034],"end_to_end_accepted_tok_s":4.882128558358612} |

These checks retain their reported scope. A context/allocation/retrieval check is not a general quality score or a speed qualification at that context. Exact flags and provenance are in [checks.json](../checks.json).

## Additional Test Results

| Result / Source | Profile | Evidence type | Reported outcome | Retained values | Configuration binding |
| --- | --- | --- | --- | --- | --- |
| [result-30f64c9704d59b6a8db1](../observations.json)<br>source-7419c98729f86c1aed84b571.json<br>`/speed/1` | [ad017-glm-mtp1-original-tensor_parallel-matched-102](ad017-glm-mtp1-original-tensor_parallel-matched-102.md)<br>[glm-mtp1-original-tensor_parallel](glm-mtp1-original-tensor_parallel.md) | performance detail | Pass | elapsed_seconds=209.74 s; end_to_end_accepted_tok_s=4.88 accepted tokens/s; ttft_seconds=195.74<br>199.40<br>199.40<br>199.40 s; p50_ms=36.86 ms; p95_ms=72.67 ms; cold_prefill: per-request 167.82 to 169.51 tokens/s; Draft accepted / proposed: 474 / 550 tokens; fraction 0.8618 | Recorded configuration/job |
| [result-53977a672e7f915d72b6](../observations.json)<br>source-7419c98729f86c1aed84b571.json<br>`/capacity/trials/0` | [ad017-glm-mtp1-original-tensor_parallel-matched-102](ad017-glm-mtp1-original-tensor_parallel-matched-102.md)<br>[glm-mtp1-original-tensor_parallel](glm-mtp1-original-tensor_parallel.md) | context allocation | Outcome unspecified | resident_pool_tokens=262,144 tokens | Recorded configuration/job |
| [result-708219eaabb1e4641349](../observations.json)<br>source-7419c98729f86c1aed84b571.json<br>`/speed/0/waves/0` | [ad017-glm-mtp1-original-tensor_parallel-matched-102](ad017-glm-mtp1-original-tensor_parallel-matched-102.md)<br>[glm-mtp1-original-tensor_parallel](glm-mtp1-original-tensor_parallel.md) | performance detail | Outcome unspecified | elapsed_seconds=54.62 s; end_to_end_accepted_tok_s=4.69 accepted tokens/s; output_tokens=256 tokens; ttft_seconds=49.44 s; p50_ms=18.75 ms; p95_ms=36.70 ms; prefill: per-request 663.95 tokens/s; Draft accepted / proposed: 117 / 139 tokens; fraction 0.8417 | Recorded configuration/job |
| [result-85036ff5759d67a3ac23](../observations.json)<br>source-a9e622d351a86c8b776605d4.json<br>`/managed_phase_timings/102` | [ad017-glm-mtp1-original-tensor_parallel-matched-102](ad017-glm-mtp1-original-tensor_parallel-matched-102.md) | test outcome | Outcome unspecified | wall_seconds=623.76 s | Recorded configuration/job |
| [result-930b1edc46ee34687515](../observations.json)<br>source-7419c98729f86c1aed84b571.json<br>`/speed/0` | [ad017-glm-mtp1-original-tensor_parallel-matched-102](ad017-glm-mtp1-original-tensor_parallel-matched-102.md)<br>[glm-mtp1-original-tensor_parallel](glm-mtp1-original-tensor_parallel.md) | performance detail | Pass | elapsed_seconds=54.62 s; end_to_end_accepted_tok_s=4.69 accepted tokens/s; ttft_seconds=49.44 s; p50_ms=18.80 ms; p95_ms=36.77 ms; cold_prefill: per-request 663.95 tokens/s; Draft accepted / proposed: 117 / 139 tokens; fraction 0.8417 | Recorded configuration/job |
| [result-b243571b3de0fde308a0](../observations.json)<br>source-7419c98729f86c1aed84b571.json<br>`/speed/0/waves/1` | [ad017-glm-mtp1-original-tensor_parallel-matched-102](ad017-glm-mtp1-original-tensor_parallel-matched-102.md)<br>[glm-mtp1-original-tensor_parallel](glm-mtp1-original-tensor_parallel.md) | performance detail | Outcome unspecified | elapsed_seconds=5.74 s; end_to_end_accepted_tok_s=44.63 accepted tokens/s; output_tokens=256 tokens; ttft_seconds=0.58 s; p50_ms=18.80 ms; p95_ms=36.77 ms; prefill: per-request 552.17 tokens/s; Draft accepted / proposed: 117 / 139 tokens; fraction 0.8417 | Recorded configuration/job |
| [result-b2683de0a69721cba65f](../observations.json)<br>source-7419c98729f86c1aed84b571.json<br>`/speed/1/waves/1` | [ad017-glm-mtp1-original-tensor_parallel-matched-102](ad017-glm-mtp1-original-tensor_parallel-matched-102.md)<br>[glm-mtp1-original-tensor_parallel](glm-mtp1-original-tensor_parallel.md) | performance detail | Outcome unspecified | elapsed_seconds=12.44 s; end_to_end_accepted_tok_s=82.33 accepted tokens/s; output_tokens=256 tokens; ttft_seconds=0.70<br>2.45<br>2.45<br>2.45 s; p50_ms=36.86 ms; p95_ms=72.67 ms; prefill: per-request 277.17 to 554.35 tokens/s; Draft accepted / proposed: 474 / 550 tokens; fraction 0.8618 | Recorded configuration/job |
| [result-b7b51a4767dc23cd3006](../observations.json)<br>source-7419c98729f86c1aed84b571.json<br>`/speed/1/waves/0` | [ad017-glm-mtp1-original-tensor_parallel-matched-102](ad017-glm-mtp1-original-tensor_parallel-matched-102.md)<br>[glm-mtp1-original-tensor_parallel](glm-mtp1-original-tensor_parallel.md) | performance detail | Outcome unspecified | elapsed_seconds=209.74 s; end_to_end_accepted_tok_s=4.88 accepted tokens/s; output_tokens=256 tokens; ttft_seconds=195.74<br>199.40<br>199.40<br>199.40 s; p50_ms=36.87 ms; p95_ms=73.62 ms; prefill: per-request 167.82 to 169.51 tokens/s; Draft accepted / proposed: 462 / 562 tokens; fraction 0.8221 | Recorded configuration/job |

These are saved result records, including failures and bounded checks. Copies, individual requests, report summaries and regrading can overlap; their counts are not independent test repetitions. Open each result for exact values, units, configuration binding and source receipts.

There are 1 retained lifecycle records. Their states, exit codes and configuration IDs remain in [catalog.json](../catalog.json); they do not supply missing benchmark results.

[Full archive](../../README.md) | [All retained waves](../RESULTS.md) | [Data definitions](../DATA.md) | [Recommended recipes](../../../README.md)
