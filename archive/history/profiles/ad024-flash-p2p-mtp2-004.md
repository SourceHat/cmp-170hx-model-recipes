# ad024-flash-p2p-mtp2-004

**Historical record. Decode interval measured.**

Model family: Qwen 3.8 Flash Next.

Historical configurations are provided for comparison. The [recommended recipes](../../../README.md) include supported launch scripts.

Current recipes using the same recorded checkpoint repository: [qwen-flash-next-mtp2-layer-split](../../../recipes/qwen-flash-next-mtp2-layer-split/README.md). Context, cache and runtime versions can differ.

## Saved Configuration Versions

Each configuration ID identifies a distinct original settings record. Deployment fields are omitted; versions can have identical published settings after that omission. Upstream runtime commits remain unspecified where the source retained only an integration label.

| Configuration | Recorded artifact / source | Configured card counts | Context tokens | GPU pool tokens | Slots | Draft mode / tokens |
| --- | --- | --- | --- | --- | --- | --- |
| cfg-d8890e05a0443045c7a3 | [turboderp/Qwen3.8-Flash-Next-exl3@d2e238feca](https://huggingface.co/turboderp/Qwen3.8-Flash-Next-exl3/tree/d2e238feca4c1c4d966943117356d8a42c2f4dcb) | 2 | 262,144 | 262,144 | 6 | mtp / 2 |

Card counts are saved configuration choices, not a claim that every allowed placement was measured. A derived view can differ from its pinned download source.

<details>
<summary>cfg-d8890e05a0443045c7a3</summary>

```json
{
  "kind": "tabby",
  "gpu_counts": [
    2
  ],
  "context": 262144,
  "cache_tokens": 262144,
  "cache_mode": "Q8",
  "draft_cache_mode": "Q8",
  "draft_mode": "mtp",
  "draft_tokens": 2,
  "max_sessions": 6,
  "chunk_size": 512,
  "reserve_mib": 2048,
  "ram_kv_mib": 8192,
  "ram_recurrent_mib": 16384,
  "ngram_ram": true,
  "dynamic_draft": false,
  "output_chunk_tokens": 4096,
  "power_watts": 200,
  "host_memory_gib": 80,
  "host_swap_gib": 0,
  "min_vram_mib_per_gpu": 65530,
  "min_effective_vram_mib": 131060,
  "parallelism": "layer_split",
  "transport": "p2p",
  "host_backing": "ordinary",
  "model_repository": "turboderp/Qwen3.8-Flash-Next-exl3",
  "model_revision": "d2e238feca4c1c4d966943117356d8a42c2f4dcb",
  "draft_repository": null,
  "draft_revision": null,
  "recorded_runtime_label": null,
  "served_model_label": "qwen3.8-flash-next"
}
```

Pinned model revision recorded: yes. Source receipt labels, hashes and object locators are retained in [configurations.json](../configurations.json).

</details>

## Retained Measurements

| Profile / Wave | Layout; Draft / Tokens | Requests | Input tokens/request | Accepted output tokens/request | Cache / Reused input tokens | Context / GPU pool tokens | Shared decode tok/s total | Client after-first-token estimate tok/s | Whole-wave output tok/s | Median TTFT, s | Source report |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [ad024-flash-p2p-mtp2-004](ad024-flash-p2p-mtp2-004.md)<br>wave-03312b07b8ca18d4af5c | layer_split; mtp / 2 | 1 | 32,769 | 256 (budget 256) | cold; reused 0 | 262,144 / 262,144 | 76.62 | Not recorded | 9.28 | 24.30 | Pass |
| [ad024-flash-p2p-mtp2-004](ad024-flash-p2p-mtp2-004.md)<br>wave-b21689df1e5540e4f9b2 | layer_split; mtp / 2 | 6 | 32,770 | 512 (budget 512) | cached_prefix; reused 32,768 | 262,144 / 262,144 | 131.48 | Not recorded | 126.82 | 1.10 | Pass |
| [ad024-flash-p2p-mtp2-004](ad024-flash-p2p-mtp2-004.md)<br>wave-b5098ee3a3802f34461c | layer_split; mtp / 2 | 6 | 32,770 | 256 (budget 256) | cold; reused 0 | 262,144 / 262,144 | 137.28 | Not recorded | 9.79 | 145.72 | Pass |
| [ad024-flash-p2p-mtp2-004](ad024-flash-p2p-mtp2-004.md)<br>wave-f2c4f95a73743798729f | layer_split; mtp / 2 | 1 | 32,769 | 512 (budget 512) | repeated_input; reused 0 | 262,144 / 262,144 | 76.78 | Not recorded | 16.57 | 24.32 | Pass |

Rates are whole-wave totals over the stated request count. A wave may span multiple independent model instances; [measurements.json](../measurements.json) retains their contributions and the exact configuration IDs. Do not interpret a multi-instance total as one card's rate.

A dash in shared decode means no qualified synchronized interval is available. Whole-wave throughput includes prefill and queueing. A valid decode interval can survive inside an overall failed or partial check; the source-report outcome is preserved. No rows are averaged.

## Bounded Checks

| Check | Reported outcome | Retained counts / flags |
| --- | --- | --- |
| check-33b1047444e278c15405 | Pass | {"passed":true,"elapsed_seconds":156.84336297700065,"ttft_seconds":[138.89361933000328,145.72375273799844,145.72378326699982,145.72322376000375,145.87290782199852,145.87234372300009],"end_to_end_accepted_tok_s":9.793210059039842} |
| check-42f8ffef35110cea9bb9 | Pass | {"actual_long_request_prompt_tokens":2055,"passed":true,"configured_slots":6,"context_tokens":4096} |
| check-62d083c974817548de67 | Pass | {"actual_long_request_prompt_tokens":2055,"passed":true,"configured_slots":6,"context_tokens":4096} |
| check-8c4e73a55840ebf53fbd | Pass | {"passed":true,"elapsed_seconds":27.578110910006217,"ttft_seconds":[24.30128752699966],"end_to_end_accepted_tok_s":9.282724289397033} |

These checks retain their reported scope. A context/allocation/retrieval check is not a general quality score or a speed qualification at that context. Exact flags and provenance are in [checks.json](../checks.json).

## Additional Test Results

| Result / Source | Profile | Evidence type | Reported outcome | Retained values | Configuration binding |
| --- | --- | --- | --- | --- | --- |
| [result-2127c799d833d0232cb8](../observations.json)<br>source-ac5197c8bf1ed97db9cdb7bf.json<br>`/waves/0` | [ad024-flash-p2p-mtp2-004](ad024-flash-p2p-mtp2-004.md) | performance detail | Outcome unspecified | elapsed_seconds=156.84 s; end_to_end_accepted_tok_s=9.79 accepted tokens/s; output_tokens=256 tokens; ttft_seconds=138.89<br>145.72<br>145.72<br>145.72<br>145.87<br>145.87 s; p50_ms=37.48 ms; p95_ms=111.77 ms; prefill: per-request 229.24 to 236.10 tokens/s; Draft accepted / proposed: 921 / 1,230 tokens; fraction 0.7488 | Recorded configuration/job |
| [result-540a142c5480bd16824b](../observations.json)<br>source-ac5197c8bf1ed97db9cdb7bf.json<br>`/` | [ad024-flash-p2p-mtp2-004](ad024-flash-p2p-mtp2-004.md) | performance detail | Pass | elapsed_seconds=156.84 s; end_to_end_accepted_tok_s=9.79 accepted tokens/s; ttft_seconds=138.89<br>145.72<br>145.72<br>145.72<br>145.87<br>145.87 s; p50_ms=39.84 ms; p95_ms=117.93 ms; cold_prefill: per-request 229.24 to 236.10 tokens/s; Draft accepted / proposed: 1,871 / 2,402 tokens; fraction 0.7789 | Recorded configuration/job |
| [result-8d586bc17709d9e84e35](../observations.json)<br>source-a0ba79bc717f183241163f94.json<br>`/waves/0` | [ad024-flash-p2p-mtp2-004](ad024-flash-p2p-mtp2-004.md) | performance detail | Outcome unspecified | elapsed_seconds=27.58 s; end_to_end_accepted_tok_s=9.28 accepted tokens/s; output_tokens=256 tokens; ttft_seconds=24.30 s; p50_ms=11.54 ms; p95_ms=33.13 ms; prefill: per-request 1,353.53 tokens/s; Draft accepted / proposed: 158 / 196 tokens; fraction 0.8061 | Recorded configuration/job |
| [result-8fbbfdbf23ba5e50bc2f](../observations.json)<br>source-797606345fa45914fcd85b71.json<br>`/profiles/qwen-flash-next-mtp2-layer-split/p2p/correctness` | [ad024-flash-p2p-mtp2-004](ad024-flash-p2p-mtp2-004.md)<br>[qwen-flash-next-mtp2-layer-split](qwen-flash-next-mtp2-layer-split.md) | context allocation | Pass | actual_long_request_prompt_tokens=2,055 tokens; configured_slots=6 requests; context_tokens=4,096 tokens; 6 mixed-length request records | Recorded configuration/job |
| [result-bd38acd84ef396c9cf84](../observations.json)<br>source-a0ba79bc717f183241163f94.json<br>`/waves/1` | [ad024-flash-p2p-mtp2-004](ad024-flash-p2p-mtp2-004.md) | performance detail | Outcome unspecified | elapsed_seconds=30.90 s; end_to_end_accepted_tok_s=16.57 accepted tokens/s; output_tokens=512 tokens; ttft_seconds=24.32 s; p50_ms=11.48 ms; p95_ms=32.92 ms; prefill: per-request 1,354.09 tokens/s; Draft accepted / proposed: 316 / 392 tokens; fraction 0.8061 | Recorded configuration/job |
| [result-d58be219057b38c2ba00](../observations.json)<br>source-4407abdb7350915215995c37.json<br>`/tabby` | [ad024-flash-p2p-mtp2-004](ad024-flash-p2p-mtp2-004.md) | test outcome | Outcome unspecified | cache_tokens=262,144 tokens | Recorded configuration/job |
| [result-eb1c7ea5a1546b3d8764](../observations.json)<br>source-a0ba79bc717f183241163f94.json<br>`/` | [ad024-flash-p2p-mtp2-004](ad024-flash-p2p-mtp2-004.md) | performance detail | Pass | elapsed_seconds=27.58 s; end_to_end_accepted_tok_s=9.28 accepted tokens/s; ttft_seconds=24.30 s; p50_ms=11.48 ms; p95_ms=32.92 ms; cold_prefill: per-request 1,353.53 tokens/s; Draft accepted / proposed: 316 / 392 tokens; fraction 0.8061 | Recorded configuration/job |
| [result-fc9055b295f547f265eb](../observations.json)<br>source-ac5197c8bf1ed97db9cdb7bf.json<br>`/waves/1` | [ad024-flash-p2p-mtp2-004](ad024-flash-p2p-mtp2-004.md) | performance detail | Outcome unspecified | elapsed_seconds=24.22 s; end_to_end_accepted_tok_s=126.82 accepted tokens/s; output_tokens=512 tokens; ttft_seconds=0.31<br>1.10<br>1.10<br>1.10<br>1.21<br>1.21 s; p50_ms=39.84 ms; p95_ms=117.93 ms; prefill: per-request 50.00 to 100.00 tokens/s; Draft accepted / proposed: 1,871 / 2,402 tokens; fraction 0.7789 | Recorded configuration/job |

These are saved result records, including failures and bounded checks. Copies, individual requests, report summaries and regrading can overlap; their counts are not independent test repetitions. Open each result for exact values, units, configuration binding and source receipts.

There are 1 retained lifecycle records. Their states, exit codes and configuration IDs remain in [catalog.json](../catalog.json); they do not supply missing benchmark results.

[Full archive](../../README.md) | [All retained waves](../RESULTS.md) | [Data definitions](../DATA.md) | [Recommended recipes](../../../README.md)
