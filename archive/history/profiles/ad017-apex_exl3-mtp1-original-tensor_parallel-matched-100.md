# ad017-apex_exl3-mtp1-original-tensor_parallel-matched-100

**Historical record. Decode interval measured.**

Model family: Apex Flash 1 (GLM 5.3 Flash post-train).

Historical configurations are provided for comparison. The [recommended recipes](../../../README.md) include supported launch scripts.

Current recipes using the same recorded checkpoint repository: [apex-abliterated-exl3-mtp1-tp3](../../../recipes/apex-abliterated-exl3-mtp1-tp3/README.md). Context, cache and runtime versions can differ.

## Saved Configuration Versions

Each configuration ID identifies a distinct original settings record. Deployment fields are omitted; versions can have identical published settings after that omission. Upstream runtime commits remain unspecified where the source retained only an integration label.

| Configuration | Recorded artifact / source | Configured card counts | Context tokens | GPU pool tokens | Slots | Draft mode / tokens |
| --- | --- | --- | --- | --- | --- | --- |
| cfg-c35259d2852f20be7b1b | [SloptimistPrime/apex-flash-1-abliterated-EXL3-4bit-DGX-Spark@a4c922dc57](https://huggingface.co/SloptimistPrime/apex-flash-1-abliterated-EXL3-4bit-DGX-Spark/tree/a4c922dc57dae44a9569ec82a08a2f311636e2a6) | 3 | 262,144 | 262,144 | 4 | mtp / 1 |

Card counts are saved configuration choices, not a claim that every allowed placement was measured. A derived view can differ from its pinned download source.

<details>
<summary>cfg-c35259d2852f20be7b1b</summary>

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
  "model_repository": "SloptimistPrime/apex-flash-1-abliterated-EXL3-4bit-DGX-Spark",
  "model_revision": "a4c922dc57dae44a9569ec82a08a2f311636e2a6",
  "draft_repository": null,
  "draft_revision": null,
  "recorded_runtime_label": null,
  "served_model_label": "apex-flash-1-abliterated-exl3-4bit-spark"
}
```

Pinned model revision recorded: yes. Source receipt labels, hashes and object locators are retained in [configurations.json](../configurations.json).

</details>

## Retained Measurements

| Profile / Wave | Layout; Draft / Tokens | Requests | Input tokens/request | Accepted output tokens/request | Cache / Reused input tokens | Context / GPU pool tokens | Shared decode tok/s total | Client after-first-token estimate tok/s | Whole-wave output tok/s | Median TTFT, s | Source report |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [ad017-apex_exl3-mtp1-original-tensor_parallel-matched-100](ad017-apex_exl3-mtp1-original-tensor_parallel-matched-100.md)<br>wave-117b9e609803dd0d076f | tensor_parallel; mtp / 1 | 1 | 32,766 | 256 (budget 256) | cached_prefix; reused 32,512 | 262,144 / 262,144 | 44.22 | Not recorded | 40.36 | 0.64 | Pass |
| [ad017-apex_exl3-mtp1-original-tensor_parallel-matched-100](ad017-apex_exl3-mtp1-original-tensor_parallel-matched-100.md)<br>wave-5e83f060c70a663fa497 | tensor_parallel; mtp / 1 | 4 | 32,767 | 256 (budget 256) | cached_prefix; reused 32,512 | 262,144 / 262,144 | 99.38 | Not recorded | 80.56 | 2.44 | Pass |
| [ad017-apex_exl3-mtp1-original-tensor_parallel-matched-100](ad017-apex_exl3-mtp1-original-tensor_parallel-matched-100.md)<br>wave-665146b32d5e7b42b7ad | tensor_parallel; mtp / 1 | 4 | 32,767 | 256 (budget 256) | cold; reused 0 | 262,144 / 262,144 | 95.28 | Not recorded | 4.83 | 200.95 | Pass |
| [ad017-apex_exl3-mtp1-original-tensor_parallel-matched-100](ad017-apex_exl3-mtp1-original-tensor_parallel-matched-100.md)<br>wave-a0bc52178f21e2a267ff | tensor_parallel; mtp / 1 | 1 | 32,766 | 256 (budget 256) | cold; reused 0 | 262,144 / 262,144 | 41.86 | Not recorded | 4.47 | 51.17 | Pass |

Rates are whole-wave totals over the stated request count. A wave may span multiple independent model instances; [measurements.json](../measurements.json) retains their contributions and the exact configuration IDs. Do not interpret a multi-instance total as one card's rate.

A dash in shared decode means no qualified synchronized interval is available. Whole-wave throughput includes prefill and queueing. A valid decode interval can survive inside an overall failed or partial check; the source-report outcome is preserved. No rows are averaged.

## Bounded Checks

| Check | Reported outcome | Retained counts / flags |
| --- | --- | --- |
| check-325576a16ab77467c4b8 | Pass | {"passed":true,"elapsed_seconds":57.24216277300002,"ttft_seconds":[51.172666932000084],"end_to_end_accepted_tok_s":4.4722279452507} |
| check-895f3ae460c19307da91 | Pass | {"passed":true,"elapsed_seconds":212.11060045299973,"ttft_seconds":[198.9485686099997,200.44256487300026,201.45184300799974,201.45151446399996],"end_to_end_accepted_tok_s":4.827670082556302} |
| check-8cc72f924211b91f34c6 | Pass | {"passed":true,"elapsed_seconds":212.11060045299973,"ttft_seconds":[198.9485686099997,200.44256487300026,201.45184300799974,201.45151446399996],"end_to_end_accepted_tok_s":4.827670082556302} |
| check-b2e65a5419ce716325e2 | Pass | {"passed":true,"elapsed_seconds":57.24216277300002,"ttft_seconds":[51.172666932000084],"end_to_end_accepted_tok_s":4.4722279452507} |

These checks retain their reported scope. A context/allocation/retrieval check is not a general quality score or a speed qualification at that context. Exact flags and provenance are in [checks.json](../checks.json).

## Additional Test Results

| Result / Source | Profile | Evidence type | Reported outcome | Retained values | Configuration binding |
| --- | --- | --- | --- | --- | --- |
| [result-3a9d694a9d7842406e75](../observations.json)<br>source-b5ce85b23063b71f50338af3.json<br>`/speed/0` | [ad017-apex_exl3-mtp1-original-tensor_parallel-matched-100](ad017-apex_exl3-mtp1-original-tensor_parallel-matched-100.md)<br>[apex_exl3-mtp1-original-tensor_parallel](apex_exl3-mtp1-original-tensor_parallel.md) | performance detail | Pass | elapsed_seconds=57.24 s; end_to_end_accepted_tok_s=4.47 accepted tokens/s; ttft_seconds=51.17 s; p50_ms=21.22 ms; p95_ms=40.72 ms; cold_prefill: per-request 641.46 tokens/s; Draft accepted / proposed: 118 / 138 tokens; fraction 0.8551 | Recorded configuration/job |
| [result-3b88241e723ef4b7599c](../observations.json)<br>source-b5ce85b23063b71f50338af3.json<br>`/speed/0/waves/1` | [ad017-apex_exl3-mtp1-original-tensor_parallel-matched-100](ad017-apex_exl3-mtp1-original-tensor_parallel-matched-100.md)<br>[apex_exl3-mtp1-original-tensor_parallel](apex_exl3-mtp1-original-tensor_parallel.md) | performance detail | Outcome unspecified | elapsed_seconds=6.34 s; end_to_end_accepted_tok_s=40.36 accepted tokens/s; output_tokens=256 tokens; ttft_seconds=0.64 s; p50_ms=21.22 ms; p95_ms=40.72 ms; prefill: per-request 540.43 tokens/s; Draft accepted / proposed: 118 / 138 tokens; fraction 0.8551 | Recorded configuration/job |
| [result-4caadf9567e80f198e50](../observations.json)<br>source-b5ce85b23063b71f50338af3.json<br>`/speed/1/waves/0` | [ad017-apex_exl3-mtp1-original-tensor_parallel-matched-100](ad017-apex_exl3-mtp1-original-tensor_parallel-matched-100.md)<br>[apex_exl3-mtp1-original-tensor_parallel](apex_exl3-mtp1-original-tensor_parallel.md) | performance detail | Outcome unspecified | elapsed_seconds=212.11 s; end_to_end_accepted_tok_s=4.83 accepted tokens/s; output_tokens=256 tokens; ttft_seconds=198.95<br>200.44<br>201.45<br>201.45 s; p50_ms=37.92 ms; p95_ms=76.77 ms; prefill: per-request 166.32 to 168.61 tokens/s; Draft accepted / proposed: 464 / 560 tokens; fraction 0.8286 | Recorded configuration/job |
| [result-6501f378531b147ef5aa](../observations.json)<br>source-a9e622d351a86c8b776605d4.json<br>`/managed_phase_timings/100` | [ad017-apex_exl3-mtp1-original-tensor_parallel-matched-100](ad017-apex_exl3-mtp1-original-tensor_parallel-matched-100.md) | test outcome | Outcome unspecified | wall_seconds=701.74 s | Recorded configuration/job |
| [result-6ad1b2d393447e6beef9](../observations.json)<br>source-b5ce85b23063b71f50338af3.json<br>`/speed/1/waves/1` | [ad017-apex_exl3-mtp1-original-tensor_parallel-matched-100](ad017-apex_exl3-mtp1-original-tensor_parallel-matched-100.md)<br>[apex_exl3-mtp1-original-tensor_parallel](apex_exl3-mtp1-original-tensor_parallel.md) | performance detail | Outcome unspecified | elapsed_seconds=12.71 s; end_to_end_accepted_tok_s=80.56 accepted tokens/s; output_tokens=256 tokens; ttft_seconds=0.74<br>2.44<br>2.44<br>2.44 s; p50_ms=37.34 ms; p95_ms=73.81 ms; prefill: per-request 274.19 to 542.55 tokens/s; Draft accepted / proposed: 470 / 554 tokens; fraction 0.8484 | Recorded configuration/job |
| [result-800077be9c877b3e4784](../observations.json)<br>source-b5ce85b23063b71f50338af3.json<br>`/speed/1` | [ad017-apex_exl3-mtp1-original-tensor_parallel-matched-100](ad017-apex_exl3-mtp1-original-tensor_parallel-matched-100.md)<br>[apex_exl3-mtp1-original-tensor_parallel](apex_exl3-mtp1-original-tensor_parallel.md) | performance detail | Pass | elapsed_seconds=212.11 s; end_to_end_accepted_tok_s=4.83 accepted tokens/s; ttft_seconds=198.95<br>200.44<br>201.45<br>201.45 s; p50_ms=37.34 ms; p95_ms=73.81 ms; cold_prefill: per-request 166.32 to 168.61 tokens/s; Draft accepted / proposed: 470 / 554 tokens; fraction 0.8484 | Recorded configuration/job |
| [result-8e2623f075963956447c](../observations.json)<br>source-b5ce85b23063b71f50338af3.json<br>`/capacity/trials/0` | [ad017-apex_exl3-mtp1-original-tensor_parallel-matched-100](ad017-apex_exl3-mtp1-original-tensor_parallel-matched-100.md)<br>[apex_exl3-mtp1-original-tensor_parallel](apex_exl3-mtp1-original-tensor_parallel.md) | context allocation | Outcome unspecified | resident_pool_tokens=262,144 tokens | Recorded configuration/job |
| [result-cd8490740e9b64417a44](../observations.json)<br>source-b5ce85b23063b71f50338af3.json<br>`/speed/0/waves/0` | [ad017-apex_exl3-mtp1-original-tensor_parallel-matched-100](ad017-apex_exl3-mtp1-original-tensor_parallel-matched-100.md)<br>[apex_exl3-mtp1-original-tensor_parallel](apex_exl3-mtp1-original-tensor_parallel.md) | performance detail | Outcome unspecified | elapsed_seconds=57.24 s; end_to_end_accepted_tok_s=4.47 accepted tokens/s; output_tokens=256 tokens; ttft_seconds=51.17 s; p50_ms=21.33 ms; p95_ms=43.12 ms; prefill: per-request 641.46 tokens/s; Draft accepted / proposed: 112 / 144 tokens; fraction 0.7778 | Recorded configuration/job |

These are saved result records, including failures and bounded checks. Copies, individual requests, report summaries and regrading can overlap; their counts are not independent test repetitions. Open each result for exact values, units, configuration binding and source receipts.

There are 1 retained lifecycle records. Their states, exit codes and configuration IDs remain in [catalog.json](../catalog.json); they do not supply missing benchmark results.

[Full archive](../../README.md) | [All retained waves](../RESULTS.md) | [Data definitions](../DATA.md) | [Recommended recipes](../../../README.md)
