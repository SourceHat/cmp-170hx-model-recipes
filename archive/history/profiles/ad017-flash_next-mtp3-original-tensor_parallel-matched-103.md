# ad017-flash_next-mtp3-original-tensor_parallel-matched-103

**Historical record. Decode interval measured.**

Model family: Qwen 3.8 Flash Next.

Historical configurations are provided for comparison. The [recommended recipes](../../../README.md) include supported launch scripts.

Current recipes using the same recorded checkpoint repository: [qwen-flash-next-mtp2-layer-split](../../../recipes/qwen-flash-next-mtp2-layer-split/README.md). Context, cache and runtime versions can differ.

## Saved Configuration Versions

Each configuration ID identifies a distinct original settings record. Deployment fields are omitted; versions can have identical published settings after that omission. Upstream runtime commits remain unspecified where the source retained only an integration label.

| Configuration | Recorded artifact / source | Configured card counts | Context tokens | GPU pool tokens | Slots | Draft mode / tokens |
| --- | --- | --- | --- | --- | --- | --- |
| cfg-fc50786056cdb965d531 | [turboderp/Qwen3.8-Flash-Next-exl3@d2e238feca](https://huggingface.co/turboderp/Qwen3.8-Flash-Next-exl3/tree/d2e238feca4c1c4d966943117356d8a42c2f4dcb) | 2 | 262,144 | 262,144 | 6 | mtp / 3 |

Card counts are saved configuration choices, not a claim that every allowed placement was measured. A derived view can differ from its pinned download source.

<details>
<summary>cfg-fc50786056cdb965d531</summary>

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
  "transport": "host",
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
| [ad017-flash_next-mtp3-original-tensor_parallel-matched-103](ad017-flash_next-mtp3-original-tensor_parallel-matched-103.md)<br>wave-023854cbc587dffa43a7 | tensor_parallel; mtp / 3 | 6 | 32,770 | 256 (budget 256) | cached_prefix; reused 32,768 | 262,144 / 262,144 | 142.19 | Not recorded | 129.26 | 1.22 | Pass |
| [ad017-flash_next-mtp3-original-tensor_parallel-matched-103](ad017-flash_next-mtp3-original-tensor_parallel-matched-103.md)<br>wave-994a7c61ab4bf4896213 | tensor_parallel; mtp / 3 | 1 | 32,769 | 256 (budget 256) | cold; reused 0 | 262,144 / 262,144 | 71.68 | Not recorded | 6.41 | 36.46 | Pass |
| [ad017-flash_next-mtp3-original-tensor_parallel-matched-103](ad017-flash_next-mtp3-original-tensor_parallel-matched-103.md)<br>wave-ee03da742c3cdb4b3bee | tensor_parallel; mtp / 3 | 6 | 32,770 | 256 (budget 256) | cold; reused 0 | 262,144 / 262,144 | 145.05 | Not recorded | 6.68 | 219.55 | Pass |
| [ad017-flash_next-mtp3-original-tensor_parallel-matched-103](ad017-flash_next-mtp3-original-tensor_parallel-matched-103.md)<br>wave-fe51eec2adfcef3029eb | tensor_parallel; mtp / 3 | 1 | 32,769 | 256 (budget 256) | repeated_input; reused 0 | 262,144 / 262,144 | 74.32 | Not recorded | 6.42 | 36.56 | Pass |

Rates are whole-wave totals over the stated request count. A wave may span multiple independent model instances; [measurements.json](../measurements.json) retains their contributions and the exact configuration IDs. Do not interpret a multi-instance total as one card's rate.

A dash in shared decode means no qualified synchronized interval is available. Whole-wave throughput includes prefill and queueing. A valid decode interval can survive inside an overall failed or partial check; the source-report outcome is preserved. No rows are averaged.

## Bounded Checks

| Check | Reported outcome | Retained counts / flags |
| --- | --- | --- |
| check-403625a42955808a6ba1 | Pass | {"passed":true,"elapsed_seconds":229.77516463499978,"ttft_seconds":[217.87757600900022,219.43715568000061,219.55459332200007,219.55425747400022,219.55391496999982,219.55357262500002],"end_to_end_accepted_tok_s":6.684795558475399} |
| check-55385cdbd2ea109a78dc | Pass | {"passed":true,"elapsed_seconds":39.96130963199994,"ttft_seconds":[36.458193767999546],"end_to_end_accepted_tok_s":6.406196452455655} |
| check-959b19d30cab489fa54b | Pass | {"passed":true,"elapsed_seconds":229.77516463499978,"ttft_seconds":[217.87757600900022,219.43715568000061,219.55459332200007,219.55425747400022,219.55391496999982,219.55357262500002],"end_to_end_accepted_tok_s":6.684795558475399} |
| check-97ff65cca2ff74e49350 | Pass | {"passed":true,"elapsed_seconds":39.96130963199994,"ttft_seconds":[36.458193767999546],"end_to_end_accepted_tok_s":6.406196452455655} |
| check-9a275afbe2f2ca1a869a | Pass | {"passed":true,"elapsed_seconds":39.96130963199994,"ttft_seconds":[36.458193767999546],"end_to_end_accepted_tok_s":6.406196452455655} |

These checks retain their reported scope. A context/allocation/retrieval check is not a general quality score or a speed qualification at that context. Exact flags and provenance are in [checks.json](../checks.json).

## Additional Test Results

| Result / Source | Profile | Evidence type | Reported outcome | Retained values | Configuration binding |
| --- | --- | --- | --- | --- | --- |
| [result-52f49cbc6ee7747d5300](../observations.json)<br>source-a9e622d351a86c8b776605d4.json<br>`/managed_phase_timings/103` | [ad017-flash_next-mtp3-original-tensor_parallel-matched-103](ad017-flash_next-mtp3-original-tensor_parallel-matched-103.md) | test outcome | Outcome unspecified | wall_seconds=699.54 s | Recorded configuration/job |
| [result-7f1e051a578c3f5ba3d2](../observations.json)<br>source-e9709fe18fa406dbba87624f.json<br>`/capacity/trials/0` | [ad017-flash_next-mtp3-original-tensor_parallel-matched-103](ad017-flash_next-mtp3-original-tensor_parallel-matched-103.md)<br>[flash_next-mtp3-original-tensor_parallel](flash_next-mtp3-original-tensor_parallel.md) | context allocation | Outcome unspecified | resident_pool_tokens=262,144 tokens | Recorded configuration/job |
| [result-9b677bb1f5d5afc7761a](../observations.json)<br>source-e9709fe18fa406dbba87624f.json<br>`/speed/0/waves/1` | [ad017-flash_next-mtp3-original-tensor_parallel-matched-103](ad017-flash_next-mtp3-original-tensor_parallel-matched-103.md)<br>[flash_next-mtp3-original-tensor_parallel](flash_next-mtp3-original-tensor_parallel.md) | performance detail | Outcome unspecified | elapsed_seconds=39.86 s; end_to_end_accepted_tok_s=6.42 accepted tokens/s; output_tokens=256 tokens; ttft_seconds=36.56 s; p50_ms=10.34 ms; p95_ms=39.89 ms; prefill: per-request 900.74 tokens/s; Draft accepted / proposed: 171 / 255 tokens; fraction 0.6706 | Recorded configuration/job |
| [result-a8745a9702fb474e1d14](../observations.json)<br>source-e9709fe18fa406dbba87624f.json<br>`/speed/1/waves/1` | [ad017-flash_next-mtp3-original-tensor_parallel-matched-103](ad017-flash_next-mtp3-original-tensor_parallel-matched-103.md)<br>[flash_next-mtp3-original-tensor_parallel](flash_next-mtp3-original-tensor_parallel.md) | performance detail | Outcome unspecified | elapsed_seconds=11.88 s; end_to_end_accepted_tok_s=129.26 accepted tokens/s; output_tokens=256 tokens; ttft_seconds=0.34<br>1.17<br>1.17<br>1.28<br>1.28<br>1.28 s; p50_ms=39.36 ms; p95_ms=126.28 ms; prefill: per-request 40.00 to 100.00 tokens/s; Draft accepted / proposed: 1,014 / 1,566 tokens; fraction 0.6475 | Recorded configuration/job |
| [result-b559863b00be8a65b6be](../observations.json)<br>source-e9709fe18fa406dbba87624f.json<br>`/speed/1/waves/0` | [ad017-flash_next-mtp3-original-tensor_parallel-matched-103](ad017-flash_next-mtp3-original-tensor_parallel-matched-103.md)<br>[flash_next-mtp3-original-tensor_parallel](flash_next-mtp3-original-tensor_parallel.md) | performance detail | Outcome unspecified | elapsed_seconds=229.78 s; end_to_end_accepted_tok_s=6.68 accepted tokens/s; output_tokens=256 tokens; ttft_seconds=217.88<br>219.44<br>219.55<br>219.55<br>219.55<br>219.55 s; p50_ms=33.78 ms; p95_ms=127.08 ms; prefill: per-request 151.71 to 154.62 tokens/s; Draft accepted / proposed: 1,039 / 1,491 tokens; fraction 0.6968 | Recorded configuration/job |
| [result-b6fe7fb221e009bdfa09](../observations.json)<br>source-e9709fe18fa406dbba87624f.json<br>`/speed/1` | [ad017-flash_next-mtp3-original-tensor_parallel-matched-103](ad017-flash_next-mtp3-original-tensor_parallel-matched-103.md)<br>[flash_next-mtp3-original-tensor_parallel](flash_next-mtp3-original-tensor_parallel.md) | performance detail | Pass | elapsed_seconds=229.78 s; end_to_end_accepted_tok_s=6.68 accepted tokens/s; ttft_seconds=217.88<br>219.44<br>219.55<br>219.55<br>219.55<br>219.55 s; p50_ms=39.36 ms; p95_ms=126.28 ms; cold_prefill: per-request 151.71 to 154.62 tokens/s; Draft accepted / proposed: 1,014 / 1,566 tokens; fraction 0.6475 | Recorded configuration/job |
| [result-d3975f089d18549c8383](../observations.json)<br>source-e9709fe18fa406dbba87624f.json<br>`/speed/0/waves/0` | [ad017-flash_next-mtp3-original-tensor_parallel-matched-103](ad017-flash_next-mtp3-original-tensor_parallel-matched-103.md)<br>[flash_next-mtp3-original-tensor_parallel](flash_next-mtp3-original-tensor_parallel.md) | performance detail | Outcome unspecified | elapsed_seconds=39.96 s; end_to_end_accepted_tok_s=6.41 accepted tokens/s; output_tokens=256 tokens; ttft_seconds=36.46 s; p50_ms=10.86 ms; p95_ms=40.99 ms; prefill: per-request 901.24 tokens/s; Draft accepted / proposed: 171 / 255 tokens; fraction 0.6706 | Recorded configuration/job |
| [result-f733530a30e43f56d3d2](../observations.json)<br>source-e9709fe18fa406dbba87624f.json<br>`/speed/0` | [ad017-flash_next-mtp3-original-tensor_parallel-matched-103](ad017-flash_next-mtp3-original-tensor_parallel-matched-103.md)<br>[flash_next-mtp3-original-tensor_parallel](flash_next-mtp3-original-tensor_parallel.md) | performance detail | Pass | elapsed_seconds=39.96 s; end_to_end_accepted_tok_s=6.41 accepted tokens/s; ttft_seconds=36.46 s; p50_ms=10.34 ms; p95_ms=39.89 ms; cold_prefill: per-request 901.24 tokens/s; Draft accepted / proposed: 171 / 255 tokens; fraction 0.6706 | Recorded configuration/job |

These are saved result records, including failures and bounded checks. Copies, individual requests, report summaries and regrading can overlap; their counts are not independent test repetitions. Open each result for exact values, units, configuration binding and source receipts.

There are 1 retained lifecycle records. Their states, exit codes and configuration IDs remain in [catalog.json](../catalog.json); they do not supply missing benchmark results.

[Full archive](../../README.md) | [All retained waves](../RESULTS.md) | [Data definitions](../DATA.md) | [Recommended recipes](../../../README.md)
