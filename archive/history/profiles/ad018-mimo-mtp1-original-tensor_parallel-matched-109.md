# ad018-mimo-mtp1-original-tensor_parallel-matched-109

**Historical record. Decode interval measured.**

Model family: MiMo V2.6 Flash.

Historical configurations are provided for comparison. The [recommended recipes](../../../README.md) include supported launch scripts.

Current recipes using the same recorded checkpoint repository: [mimo-flash-mtp1-tp3](../../../recipes/mimo-flash-mtp1-tp3/README.md). Context, cache and runtime versions can differ.

## Saved Configuration Versions

Each configuration ID identifies a distinct original settings record. Deployment fields are omitted; versions can have identical published settings after that omission. Upstream runtime commits remain unspecified where the source retained only an integration label.

| Configuration | Recorded artifact / source | Configured card counts | Context tokens | GPU pool tokens | Slots | Draft mode / tokens |
| --- | --- | --- | --- | --- | --- | --- |
| cfg-36219e8a1f3312977661 | [MikeRoz/MiMo-V2.6-Flash-MOPD-4.03bpw-h8-exl3@29c8351a8b](https://huggingface.co/MikeRoz/MiMo-V2.6-Flash-MOPD-4.03bpw-h8-exl3/tree/29c8351a8b5854ec385adaeba7bbe62c790d40ea) | 3 | 262,144 | 262,144 | 4 | mtp / 1 |

Card counts are saved configuration choices, not a claim that every allowed placement was measured. A derived view can differ from its pinned download source.

<details>
<summary>cfg-36219e8a1f3312977661</summary>

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
  "model_repository": "MikeRoz/MiMo-V2.6-Flash-MOPD-4.03bpw-h8-exl3",
  "model_revision": "29c8351a8b5854ec385adaeba7bbe62c790d40ea",
  "draft_repository": null,
  "draft_revision": null,
  "recorded_runtime_label": null,
  "served_model_label": "mimo-v2.6-flash"
}
```

Pinned model revision recorded: yes. Source receipt labels, hashes and object locators are retained in [configurations.json](../configurations.json).

</details>

## Retained Measurements

| Profile / Wave | Layout; Draft / Tokens | Requests | Input tokens/request | Accepted output tokens/request | Cache / Reused input tokens | Context / GPU pool tokens | Shared decode tok/s total | Client after-first-token estimate tok/s | Whole-wave output tok/s | Median TTFT, s | Source report |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [ad018-mimo-mtp1-original-tensor_parallel-matched-109](ad018-mimo-mtp1-original-tensor_parallel-matched-109.md)<br>wave-4797dc9319871e609a03 | tensor_parallel; mtp / 1 | 1 | 2,038 | 512 (budget 512) | cold; reused 0 | 262,144 / 262,144 | 52.66 | Not recorded | 33.78 | 5.50 | Pass |
| [ad018-mimo-mtp1-original-tensor_parallel-matched-109](ad018-mimo-mtp1-original-tensor_parallel-matched-109.md)<br>wave-70213616e5e1d815a069 | tensor_parallel; mtp / 1 | 1 | 32,765 | 512 (budget 512) | cached_prefix; reused 32,512 | 262,144 / 262,144 | 48.45 | Not recorded | 45.87 | 0.65 | Pass |
| [ad018-mimo-mtp1-original-tensor_parallel-matched-109](ad018-mimo-mtp1-original-tensor_parallel-matched-109.md)<br>wave-7184e6ebf579ec97221e | tensor_parallel; mtp / 1 | 4 | 2,039 | 512 (budget 512) | cached_prefix; reused 1,792 | 262,144 / 262,144 | 126.80 | Not recorded | 112.01 | 2.06 | Pass |
| [ad018-mimo-mtp1-original-tensor_parallel-matched-109](ad018-mimo-mtp1-original-tensor_parallel-matched-109.md)<br>wave-71885a8b04200a12c301 | tensor_parallel; mtp / 1 | 4 | 32,766 | 512 (budget 512) | cold; reused 0 | 262,144 / 262,144 | 86.52 | Not recorded | 9.23 | 197.79 | Pass |
| [ad018-mimo-mtp1-original-tensor_parallel-matched-109](ad018-mimo-mtp1-original-tensor_parallel-matched-109.md)<br>wave-75f126c0427c4b15709b | tensor_parallel; mtp / 1 | 1 | 32,765 | 512 (budget 512) | cold; reused 0 | 262,144 / 262,144 | 48.17 | Not recorded | 8.08 | 52.83 | Pass |
| [ad018-mimo-mtp1-original-tensor_parallel-matched-109](ad018-mimo-mtp1-original-tensor_parallel-matched-109.md)<br>wave-8129d74a843503c27588 | tensor_parallel; mtp / 1 | 4 | 2,039 | 512 (budget 512) | cold; reused 0 | 262,144 / 262,144 | 126.28 | Not recorded | 67.18 | 13.59 | Pass |
| [ad018-mimo-mtp1-original-tensor_parallel-matched-109](ad018-mimo-mtp1-original-tensor_parallel-matched-109.md)<br>wave-9ce811100f8ae917d047 | tensor_parallel; mtp / 1 | 4 | 32,766 | 512 (budget 512) | cached_prefix; reused 32,512 | 262,144 / 262,144 | 86.64 | Not recorded | 78.37 | 2.70 | Pass |
| [ad018-mimo-mtp1-original-tensor_parallel-matched-109](ad018-mimo-mtp1-original-tensor_parallel-matched-109.md)<br>wave-b2c7bf73fab5c06b42b6 | tensor_parallel; mtp / 1 | 1 | 2,038 | 512 (budget 512) | cached_prefix; reused 1,792 | 262,144 / 262,144 | 55.16 | Not recorded | 52.70 | 0.49 | Pass |

Rates are whole-wave totals over the stated request count. A wave may span multiple independent model instances; [measurements.json](../measurements.json) retains their contributions and the exact configuration IDs. Do not interpret a multi-instance total as one card's rate.

A dash in shared decode means no qualified synchronized interval is available. Whole-wave throughput includes prefill and queueing. A valid decode interval can survive inside an overall failed or partial check; the source-report outcome is preserved. No rows are averaged.

## Bounded Checks

| Check | Reported outcome | Retained counts / flags |
| --- | --- | --- |
| check-0e297f27f8902ba7750c | Pass | {"passed":true,"elapsed_seconds":30.484180931000083,"ttft_seconds":[9.380899370000407,13.594401233000099,13.594194321000032,13.654205705001004],"end_to_end_accepted_tok_s":67.18238566539081} |
| check-14baae4975fb902a0881 | Pass | {"passed":true,"elapsed_seconds":63.39867355000024,"ttft_seconds":[52.825041008998596],"end_to_end_accepted_tok_s":8.075878742103399} |
| check-195b749b6bf06fc6b1c1 | Pass | {"passed":true,"elapsed_seconds":15.155670604000989,"ttft_seconds":[5.501032748999933],"end_to_end_accepted_tok_s":33.78273475175923} |
| check-2a9e89d271861af7e5c4 | Pass | {"passed":true,"elapsed_seconds":63.39867355000024,"ttft_seconds":[52.825041008998596],"end_to_end_accepted_tok_s":8.075878742103399} |
| check-62214dee0b5b81b0eba8 | Pass | {"passed":true,"elapsed_seconds":221.95521602000008,"ttft_seconds":[195.70560271700015,197.22056841199992,198.36876043300072,198.3684315040009],"end_to_end_accepted_tok_s":9.227086602080384} |
| check-a074d9b3bea53576de85 | Pass | {"passed":true,"elapsed_seconds":221.95521602000008,"ttft_seconds":[195.70560271700015,197.22056841199992,198.36876043300072,198.3684315040009],"end_to_end_accepted_tok_s":9.227086602080384} |
| check-d45c330d88f9f0701f4b | Pass | {"passed":true,"elapsed_seconds":30.484180931000083,"ttft_seconds":[9.380899370000407,13.594401233000099,13.594194321000032,13.654205705001004],"end_to_end_accepted_tok_s":67.18238566539081} |
| check-e7b42c88cc2c20c43db5 | Pass | {"passed":true,"elapsed_seconds":15.155670604000989,"ttft_seconds":[5.501032748999933],"end_to_end_accepted_tok_s":33.78273475175923} |

These checks retain their reported scope. A context/allocation/retrieval check is not a general quality score or a speed qualification at that context. Exact flags and provenance are in [checks.json](../checks.json).

## Additional Test Results

| Result / Source | Profile | Evidence type | Reported outcome | Retained values | Configuration binding |
| --- | --- | --- | --- | --- | --- |
| [result-0355185945a52e7c2763](../observations.json)<br>source-a9e622d351a86c8b776605d4.json<br>`/managed_phase_timings/109` | [ad018-mimo-mtp1-original-tensor_parallel-matched-109](ad018-mimo-mtp1-original-tensor_parallel-matched-109.md) | test outcome | Outcome unspecified | wall_seconds=773.95 s | Recorded configuration/job |
| [result-333eef46945f8b77aefe](../observations.json)<br>source-94b07b24e27af4961cf45d26.json<br>`/speed/1/waves/0` | [ad018-mimo-mtp1-original-tensor_parallel-matched-109](ad018-mimo-mtp1-original-tensor_parallel-matched-109.md)<br>[mimo-mtp1-original-tensor_parallel](mimo-mtp1-original-tensor_parallel.md) | performance detail | Outcome unspecified | elapsed_seconds=30.48 s; end_to_end_accepted_tok_s=67.18 accepted tokens/s; output_tokens=512 tokens; ttft_seconds=9.38<br>13.59<br>13.59<br>13.65 s; p50_ms=29.43 ms; p95_ms=57.24 ms; prefill: per-request 222.60 to 431.08 tokens/s; Draft accepted / proposed: 931 / 1,117 tokens; fraction 0.8335 | Recorded configuration/job |
| [result-61458589c6b841cc2b42](../observations.json)<br>source-94b07b24e27af4961cf45d26.json<br>`/speed/1/waves/1` | [ad018-mimo-mtp1-original-tensor_parallel-matched-109](ad018-mimo-mtp1-original-tensor_parallel-matched-109.md)<br>[mimo-mtp1-original-tensor_parallel](mimo-mtp1-original-tensor_parallel.md) | performance detail | Outcome unspecified | elapsed_seconds=18.28 s; end_to_end_accepted_tok_s=112.01 accepted tokens/s; output_tokens=512 tokens; ttft_seconds=0.55<br>2.06<br>2.06<br>2.06 s; p50_ms=29.02 ms; p95_ms=56.98 ms; prefill: per-request 283.91 to 561.36 tokens/s; Draft accepted / proposed: 917 / 1,131 tokens; fraction 0.8108 | Recorded configuration/job |
| [result-674f696bcff3f84fc547](../observations.json)<br>source-94b07b24e27af4961cf45d26.json<br>`/speed/0/waves/0` | [ad018-mimo-mtp1-original-tensor_parallel-matched-109](ad018-mimo-mtp1-original-tensor_parallel-matched-109.md)<br>[mimo-mtp1-original-tensor_parallel](mimo-mtp1-original-tensor_parallel.md) | performance detail | Outcome unspecified | elapsed_seconds=15.16 s; end_to_end_accepted_tok_s=33.78 accepted tokens/s; output_tokens=512 tokens; ttft_seconds=5.50 s; p50_ms=17.30 ms; p95_ms=32.52 ms; prefill: per-request 373.94 tokens/s; Draft accepted / proposed: 225 / 287 tokens; fraction 0.7840 | Recorded configuration/job |
| [result-6f24c21b413fdac5b54c](../observations.json)<br>source-94b07b24e27af4961cf45d26.json<br>`/speed/2/waves/0` | [ad018-mimo-mtp1-original-tensor_parallel-matched-109](ad018-mimo-mtp1-original-tensor_parallel-matched-109.md)<br>[mimo-mtp1-original-tensor_parallel](mimo-mtp1-original-tensor_parallel.md) | performance detail | Outcome unspecified | elapsed_seconds=63.40 s; end_to_end_accepted_tok_s=8.08 accepted tokens/s; output_tokens=512 tokens; ttft_seconds=52.83 s; p50_ms=19.45 ms; p95_ms=35.90 ms; prefill: per-request 621.61 tokens/s; Draft accepted / proposed: 236 / 276 tokens; fraction 0.8551 | Recorded configuration/job |
| [result-8aa0f4509bd2bb6ccc24](../observations.json)<br>source-94b07b24e27af4961cf45d26.json<br>`/speed/3/waves/0` | [ad018-mimo-mtp1-original-tensor_parallel-matched-109](ad018-mimo-mtp1-original-tensor_parallel-matched-109.md)<br>[mimo-mtp1-original-tensor_parallel](mimo-mtp1-original-tensor_parallel.md) | performance detail | Outcome unspecified | elapsed_seconds=221.96 s; end_to_end_accepted_tok_s=9.23 accepted tokens/s; output_tokens=512 tokens; ttft_seconds=195.71<br>197.22<br>198.37<br>198.37 s; p50_ms=42.14 ms; p95_ms=81.48 ms; prefill: per-request 168.91 to 171.51 tokens/s; Draft accepted / proposed: 891 / 1,157 tokens; fraction 0.7701 | Recorded configuration/job |
| [result-8afee18837f75b42b6f4](../observations.json)<br>source-94b07b24e27af4961cf45d26.json<br>`/capacity/trials/0` | [ad018-mimo-mtp1-original-tensor_parallel-matched-109](ad018-mimo-mtp1-original-tensor_parallel-matched-109.md)<br>[mimo-mtp1-original-tensor_parallel](mimo-mtp1-original-tensor_parallel.md) | context allocation | Outcome unspecified | resident_pool_tokens=262,144 tokens | Recorded configuration/job |
| [result-96632ba01a93cbb4e45d](../observations.json)<br>source-94b07b24e27af4961cf45d26.json<br>`/speed/1` | [ad018-mimo-mtp1-original-tensor_parallel-matched-109](ad018-mimo-mtp1-original-tensor_parallel-matched-109.md)<br>[mimo-mtp1-original-tensor_parallel](mimo-mtp1-original-tensor_parallel.md) | performance detail | Pass | elapsed_seconds=30.48 s; end_to_end_accepted_tok_s=67.18 accepted tokens/s; ttft_seconds=9.38<br>13.59<br>13.59<br>13.65 s; p50_ms=29.02 ms; p95_ms=56.98 ms; cold_prefill: per-request 222.60 to 431.08 tokens/s; Draft accepted / proposed: 917 / 1,131 tokens; fraction 0.8108 | Recorded configuration/job |
| [result-b85d0d294f110175cc75](../observations.json)<br>source-94b07b24e27af4961cf45d26.json<br>`/speed/3` | [ad018-mimo-mtp1-original-tensor_parallel-matched-109](ad018-mimo-mtp1-original-tensor_parallel-matched-109.md)<br>[mimo-mtp1-original-tensor_parallel](mimo-mtp1-original-tensor_parallel.md) | performance detail | Pass | elapsed_seconds=221.96 s; end_to_end_accepted_tok_s=9.23 accepted tokens/s; ttft_seconds=195.71<br>197.22<br>198.37<br>198.37 s; p50_ms=42.07 ms; p95_ms=81.29 ms; cold_prefill: per-request 168.91 to 171.51 tokens/s; Draft accepted / proposed: 890 / 1,158 tokens; fraction 0.7686 | Recorded configuration/job |
| [result-bdc6fb760f71e556efed](../observations.json)<br>source-94b07b24e27af4961cf45d26.json<br>`/speed/2` | [ad018-mimo-mtp1-original-tensor_parallel-matched-109](ad018-mimo-mtp1-original-tensor_parallel-matched-109.md)<br>[mimo-mtp1-original-tensor_parallel](mimo-mtp1-original-tensor_parallel.md) | performance detail | Pass | elapsed_seconds=63.40 s; end_to_end_accepted_tok_s=8.08 accepted tokens/s; ttft_seconds=52.83 s; p50_ms=19.37 ms; p95_ms=35.57 ms; cold_prefill: per-request 621.61 tokens/s; Draft accepted / proposed: 236 / 276 tokens; fraction 0.8551 | Recorded configuration/job |
| [result-cc82448de7f530a6d908](../observations.json)<br>source-94b07b24e27af4961cf45d26.json<br>`/speed/3/waves/1` | [ad018-mimo-mtp1-original-tensor_parallel-matched-109](ad018-mimo-mtp1-original-tensor_parallel-matched-109.md)<br>[mimo-mtp1-original-tensor_parallel](mimo-mtp1-original-tensor_parallel.md) | performance detail | Outcome unspecified | elapsed_seconds=26.13 s; end_to_end_accepted_tok_s=78.37 accepted tokens/s; output_tokens=512 tokens; ttft_seconds=0.83<br>2.70<br>2.70<br>2.70 s; p50_ms=42.07 ms; p95_ms=81.29 ms; prefill: per-request 235.19 to 470.37 tokens/s; Draft accepted / proposed: 890 / 1,158 tokens; fraction 0.7686 | Recorded configuration/job |
| [result-ec142aef11d708a8af4d](../observations.json)<br>source-94b07b24e27af4961cf45d26.json<br>`/speed/0` | [ad018-mimo-mtp1-original-tensor_parallel-matched-109](ad018-mimo-mtp1-original-tensor_parallel-matched-109.md)<br>[mimo-mtp1-original-tensor_parallel](mimo-mtp1-original-tensor_parallel.md) | performance detail | Pass | elapsed_seconds=15.16 s; end_to_end_accepted_tok_s=33.78 accepted tokens/s; ttft_seconds=5.50 s; p50_ms=17.19 ms; p95_ms=32.20 ms; cold_prefill: per-request 373.94 tokens/s; Draft accepted / proposed: 238 / 274 tokens; fraction 0.8686 | Recorded configuration/job |
| [result-f2d31506dc243b51c59d](../observations.json)<br>source-94b07b24e27af4961cf45d26.json<br>`/speed/2/waves/1` | [ad018-mimo-mtp1-original-tensor_parallel-matched-109](ad018-mimo-mtp1-original-tensor_parallel-matched-109.md)<br>[mimo-mtp1-original-tensor_parallel](mimo-mtp1-original-tensor_parallel.md) | performance detail | Outcome unspecified | elapsed_seconds=11.16 s; end_to_end_accepted_tok_s=45.87 accepted tokens/s; output_tokens=512 tokens; ttft_seconds=0.65 s; p50_ms=19.37 ms; p95_ms=35.57 ms; prefill: per-request 468.52 tokens/s; Draft accepted / proposed: 236 / 276 tokens; fraction 0.8551 | Recorded configuration/job |
| [result-fe189920a62b8d3e344c](../observations.json)<br>source-94b07b24e27af4961cf45d26.json<br>`/speed/0/waves/1` | [ad018-mimo-mtp1-original-tensor_parallel-matched-109](ad018-mimo-mtp1-original-tensor_parallel-matched-109.md)<br>[mimo-mtp1-original-tensor_parallel](mimo-mtp1-original-tensor_parallel.md) | performance detail | Outcome unspecified | elapsed_seconds=9.72 s; end_to_end_accepted_tok_s=52.70 accepted tokens/s; output_tokens=512 tokens; ttft_seconds=0.49 s; p50_ms=17.19 ms; p95_ms=32.20 ms; prefill: per-request 572.09 tokens/s; Draft accepted / proposed: 238 / 274 tokens; fraction 0.8686 | Recorded configuration/job |

These are saved result records, including failures and bounded checks. Copies, individual requests, report summaries and regrading can overlap; their counts are not independent test repetitions. Open each result for exact values, units, configuration binding and source receipts.

There are 1 retained lifecycle records. Their states, exit codes and configuration IDs remain in [catalog.json](../catalog.json); they do not supply missing benchmark results.

[Full archive](../../README.md) | [All retained waves](../RESULTS.md) | [Data definitions](../DATA.md) | [Recommended recipes](../../../README.md)
