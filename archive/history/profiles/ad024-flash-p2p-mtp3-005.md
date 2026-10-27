# ad024-flash-p2p-mtp3-005

**Historical record. Decode interval measured.**

Model family: Qwen 3.8 Flash Next.

Historical configurations are provided for comparison. The [recommended recipes](../../../README.md) include supported launch scripts.

Current recipes using the same recorded checkpoint repository: [qwen-flash-next-mtp2-layer-split](../../../recipes/qwen-flash-next-mtp2-layer-split/README.md). Context, cache and runtime versions can differ.

## Saved Configuration Versions

Each configuration ID identifies a distinct original settings record. Deployment fields are omitted; versions can have identical published settings after that omission. Upstream runtime commits remain unspecified where the source retained only an integration label.

| Configuration | Recorded artifact / source | Configured card counts | Context tokens | GPU pool tokens | Slots | Draft mode / tokens |
| --- | --- | --- | --- | --- | --- | --- |
| cfg-558a50c8107131f8f6da | [turboderp/Qwen3.8-Flash-Next-exl3@d2e238feca](https://huggingface.co/turboderp/Qwen3.8-Flash-Next-exl3/tree/d2e238feca4c1c4d966943117356d8a42c2f4dcb) | 2 | 262,144 | 262,144 | 6 | mtp / 3 |

Card counts are saved configuration choices, not a claim that every allowed placement was measured. A derived view can differ from its pinned download source.

<details>
<summary>cfg-558a50c8107131f8f6da</summary>

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
  "draft_tokens": 3,
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
  "parallelism": "tensor_parallel",
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
| [ad024-flash-p2p-mtp3-005](ad024-flash-p2p-mtp3-005.md)<br>wave-1e6e15c9b036c5edac34 | tensor_parallel; mtp / 3 | 6 | 32,770 | 256 (budget 256) | cold; reused 0 | 262,144 / 262,144 | 146.48 | Not recorded | 6.71 | 218.40 | Pass |
| [ad024-flash-p2p-mtp3-005](ad024-flash-p2p-mtp3-005.md)<br>wave-2518e4ac2bdc657b2324 | tensor_parallel; mtp / 3 | 1 | 32,769 | 512 (budget 512) | repeated_input; reused 0 | 262,144 / 262,144 | 79.96 | Not recorded | 11.97 | 36.51 | Pass |
| [ad024-flash-p2p-mtp3-005](ad024-flash-p2p-mtp3-005.md)<br>wave-530b398d5e5536cbda7f | tensor_parallel; mtp / 3 | 1 | 32,769 | 256 (budget 256) | cold; reused 0 | 262,144 / 262,144 | 71.87 | Not recorded | 6.40 | 36.51 | Pass |
| [ad024-flash-p2p-mtp3-005](ad024-flash-p2p-mtp3-005.md)<br>wave-975933a4cafa40d5a94c | tensor_parallel; mtp / 3 | 6 | 32,770 | 512 (budget 512) | cached_prefix; reused 32,768 | 262,144 / 262,144 | 117.36 | Not recorded | 114.96 | 1.18 | Pass |

Rates are whole-wave totals over the stated request count. A wave may span multiple independent model instances; [measurements.json](../measurements.json) retains their contributions and the exact configuration IDs. Do not interpret a multi-instance total as one card's rate.

A dash in shared decode means no qualified synchronized interval is available. Whole-wave throughput includes prefill and queueing. A valid decode interval can survive inside an overall failed or partial check; the source-report outcome is preserved. No rows are averaged.

## Bounded Checks

| Check | Reported outcome | Retained counts / flags |
| --- | --- | --- |
| check-44ab02c6ff800c47e9bc | Pass | {"passed":true,"elapsed_seconds":228.97524353200424,"ttft_seconds":[212.90193020600418,217.8786761460069,217.8780707229962,218.93015646799904,218.92987710000307,218.92995492699993],"end_to_end_accepted_tok_s":6.708148777600539} |
| check-77efbfbc94f68cbf8bc3 | Pass | {"actual_long_request_prompt_tokens":2055,"passed":true,"configured_slots":6,"context_tokens":4096} |
| check-8b62d86051baad849495 | Pass | {"actual_long_request_prompt_tokens":2055,"passed":true,"configured_slots":6,"context_tokens":4096} |
| check-e224fc99faa3b02faf82 | Pass | {"passed":true,"elapsed_seconds":40.007509518000006,"ttft_seconds":[36.51371080500394],"end_to_end_accepted_tok_s":6.398798702649101} |

These checks retain their reported scope. A context/allocation/retrieval check is not a general quality score or a speed qualification at that context. Exact flags and provenance are in [checks.json](../checks.json).

## Additional Test Results

| Result / Source | Profile | Evidence type | Reported outcome | Retained values | Configuration binding |
| --- | --- | --- | --- | --- | --- |
| [result-1972092fa3c07d32a3ec](../observations.json)<br>source-1ff657483e3e79b3e7c4b6d6.json<br>`/waves/1` | [ad024-flash-p2p-mtp3-005](ad024-flash-p2p-mtp3-005.md) | performance detail | Outcome unspecified | elapsed_seconds=42.78 s; end_to_end_accepted_tok_s=11.97 accepted tokens/s; output_tokens=512 tokens; ttft_seconds=36.51 s; p50_ms=10.45 ms; p95_ms=39.57 ms; prefill: per-request 900.74 tokens/s; Draft accepted / proposed: 357 / 465 tokens; fraction 0.7677 | Recorded configuration/job |
| [result-1e15bcc97fa3a9983bd7](../observations.json)<br>source-f3f73d1a0649614a237bb507.json<br>`/` | [ad024-flash-p2p-mtp3-005](ad024-flash-p2p-mtp3-005.md) | performance detail | Pass | elapsed_seconds=228.98 s; end_to_end_accepted_tok_s=6.71 accepted tokens/s; ttft_seconds=212.90<br>217.88<br>217.88<br>218.93<br>218.93<br>218.93 s; p50_ms=40.12 ms; p95_ms=135.47 ms; cold_prefill: per-request 152.15 to 156.29 tokens/s; Draft accepted / proposed: 2,088 / 2,952 tokens; fraction 0.7073 | Recorded configuration/job |
| [result-1f34b2120a7eac4ee27e](../observations.json)<br>source-797606345fa45914fcd85b71.json<br>`/profiles/qwen-flash-next-mtp3-tp2-native/p2p/correctness` | [ad024-flash-p2p-mtp3-005](ad024-flash-p2p-mtp3-005.md)<br>[qwen-flash-next-mtp3-tp2-native](qwen-flash-next-mtp3-tp2-native.md) | context allocation | Pass | actual_long_request_prompt_tokens=2,055 tokens; configured_slots=6 requests; context_tokens=4,096 tokens; 6 mixed-length request records | Recorded configuration/job |
| [result-445c7fc9734fb76a348d](../observations.json)<br>source-f3f73d1a0649614a237bb507.json<br>`/waves/0` | [ad024-flash-p2p-mtp3-005](ad024-flash-p2p-mtp3-005.md) | performance detail | Outcome unspecified | elapsed_seconds=228.98 s; end_to_end_accepted_tok_s=6.71 accepted tokens/s; output_tokens=256 tokens; ttft_seconds=212.90<br>217.88<br>217.88<br>218.93<br>218.93<br>218.93 s; p50_ms=32.65 ms; p95_ms=126.07 ms; prefill: per-request 152.15 to 156.29 tokens/s; Draft accepted / proposed: 1,038 / 1,494 tokens; fraction 0.6948 | Recorded configuration/job |
| [result-83485ef6eb9a4208655d](../observations.json)<br>source-0d96f00578414557068766f9.json<br>`/tabby` | [ad024-flash-p2p-mtp3-005](ad024-flash-p2p-mtp3-005.md) | test outcome | Outcome unspecified | cache_tokens=262,144 tokens | Recorded configuration/job |
| [result-964ec7b1e68d2c723e98](../observations.json)<br>source-f3f73d1a0649614a237bb507.json<br>`/waves/1` | [ad024-flash-p2p-mtp3-005](ad024-flash-p2p-mtp3-005.md) | performance detail | Outcome unspecified | elapsed_seconds=26.72 s; end_to_end_accepted_tok_s=114.96 accepted tokens/s; output_tokens=512 tokens; ttft_seconds=0.47<br>1.07<br>1.18<br>1.18<br>1.18<br>1.18 s; p50_ms=40.12 ms; p95_ms=135.47 ms; prefill: per-request 40.00 to 100.00 tokens/s; Draft accepted / proposed: 2,088 / 2,952 tokens; fraction 0.7073 | Recorded configuration/job |
| [result-b9fd98d8390d81a8e47f](../observations.json)<br>source-1ff657483e3e79b3e7c4b6d6.json<br>`/waves/0` | [ad024-flash-p2p-mtp3-005](ad024-flash-p2p-mtp3-005.md) | performance detail | Outcome unspecified | elapsed_seconds=40.01 s; end_to_end_accepted_tok_s=6.40 accepted tokens/s; output_tokens=256 tokens; ttft_seconds=36.51 s; p50_ms=10.69 ms; p95_ms=41.28 ms; prefill: per-request 900.00 tokens/s; Draft accepted / proposed: 171 / 255 tokens; fraction 0.6706 | Recorded configuration/job |
| [result-cd8409f6e9d484b0fb35](../observations.json)<br>source-1ff657483e3e79b3e7c4b6d6.json<br>`/` | [ad024-flash-p2p-mtp3-005](ad024-flash-p2p-mtp3-005.md) | performance detail | Pass | elapsed_seconds=40.01 s; end_to_end_accepted_tok_s=6.40 accepted tokens/s; ttft_seconds=36.51 s; p50_ms=10.45 ms; p95_ms=39.57 ms; cold_prefill: per-request 900.00 tokens/s; Draft accepted / proposed: 357 / 465 tokens; fraction 0.7677 | Recorded configuration/job |

These are saved result records, including failures and bounded checks. Copies, individual requests, report summaries and regrading can overlap; their counts are not independent test repetitions. Open each result for exact values, units, configuration binding and source receipts.

There are 1 retained lifecycle records. Their states, exit codes and configuration IDs remain in [catalog.json](../catalog.json); they do not supply missing benchmark results.

[Full archive](../../README.md) | [All retained waves](../RESULTS.md) | [Data definitions](../DATA.md) | [Recommended recipes](../../../README.md)
