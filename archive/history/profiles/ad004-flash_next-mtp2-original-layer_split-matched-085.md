# ad004-flash_next-mtp2-original-layer_split-matched-085

**Historical record. Decode interval measured.**

Model family: Qwen 3.8 Flash Next.

Historical configurations are provided for comparison. The [recommended recipes](../../../README.md) include supported launch scripts.

Current recipes using the same recorded checkpoint repository: [qwen-flash-next-mtp2-layer-split](../../../recipes/qwen-flash-next-mtp2-layer-split/README.md). Context, cache and runtime versions can differ.

## Saved Configuration Versions

Each configuration ID identifies a distinct original settings record. Deployment fields are omitted; versions can have identical published settings after that omission. Upstream runtime commits remain unspecified where the source retained only an integration label.

| Configuration | Recorded artifact / source | Configured card counts | Context tokens | GPU pool tokens | Slots | Draft mode / tokens |
| --- | --- | --- | --- | --- | --- | --- |
| cfg-0cd6a509c461b76c550a | [turboderp/Qwen3.8-Flash-Next-exl3@d2e238feca](https://huggingface.co/turboderp/Qwen3.8-Flash-Next-exl3/tree/d2e238feca4c1c4d966943117356d8a42c2f4dcb) | 2 | 262,144 | 262,144 | 6 | mtp / 2 |

Card counts are saved configuration choices, not a claim that every allowed placement was measured. A derived view can differ from its pinned download source.

<details>
<summary>cfg-0cd6a509c461b76c550a</summary>

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
| [ad004-flash_next-mtp2-original-layer_split-matched-085](ad004-flash_next-mtp2-original-layer_split-matched-085.md)<br>wave-5bd548612aea233f9e75 | layer_split; mtp / 2 | 1 | 32,769 | 256 (budget 256) | repeated_input; reused 0 | 262,144 / 262,144 | 76.33 | Not recorded | 9.18 | 24.63 | Pass |
| [ad004-flash_next-mtp2-original-layer_split-matched-085](ad004-flash_next-mtp2-original-layer_split-matched-085.md)<br>wave-7b291c9b5b08a7c3c0fa | layer_split; mtp / 2 | 1 | 32,769 | 256 (budget 256) | cold; reused 0 | 262,144 / 262,144 | 76.31 | Not recorded | 9.18 | 24.59 | Pass |
| [ad004-flash_next-mtp2-original-layer_split-matched-085](ad004-flash_next-mtp2-original-layer_split-matched-085.md)<br>wave-c0dd8e8168eb44cd2ba6 | layer_split; mtp / 2 | 6 | 32,770 | 256 (budget 256) | cached_prefix; reused 32,768 | 262,144 / 262,144 | 130.23 | Not recorded | 121.15 | 1.21 | Pass |
| [ad004-flash_next-mtp2-original-layer_split-matched-085](ad004-flash_next-mtp2-original-layer_split-matched-085.md)<br>wave-fdb556ed911868a70912 | layer_split; mtp / 2 | 6 | 32,770 | 256 (budget 256) | cold; reused 0 | 262,144 / 262,144 | 132.77 | Not recorded | 9.66 | 147.64 | Pass |

Rates are whole-wave totals over the stated request count. A wave may span multiple independent model instances; [measurements.json](../measurements.json) retains their contributions and the exact configuration IDs. Do not interpret a multi-instance total as one card's rate.

A dash in shared decode means no qualified synchronized interval is available. Whole-wave throughput includes prefill and queueing. A valid decode interval can survive inside an overall failed or partial check; the source-report outcome is preserved. No rows are averaged.

## Bounded Checks

| Check | Reported outcome | Retained counts / flags |
| --- | --- | --- |
| check-6ce1f7fa509d11736aa1 | Pass | {"passed":true,"elapsed_seconds":27.88211463499465,"ttft_seconds":[24.591831065001315],"end_to_end_accepted_tok_s":9.181513072136077} |
| check-7a1390e8615a0fa1ee39 | Pass | {"passed":true,"elapsed_seconds":159.02001253899653,"ttft_seconds":[143.43493501500052,147.63644242700684,147.6361319320058,147.63643830199726,147.6359352129948,147.97733864199836],"end_to_end_accepted_tok_s":9.659161607872004} |
| check-9d5de2a15b9589d81909 | Pass | {"passed":true,"elapsed_seconds":159.02001253899653,"ttft_seconds":[143.43493501500052,147.63644242700684,147.6361319320058,147.63643830199726,147.6359352129948,147.97733864199836],"end_to_end_accepted_tok_s":9.659161607872004} |
| check-aa00e5270231bb641ffe | Pass | {"passed":true,"elapsed_seconds":27.88211463499465,"ttft_seconds":[24.591831065001315],"end_to_end_accepted_tok_s":9.181513072136077} |

These checks retain their reported scope. A context/allocation/retrieval check is not a general quality score or a speed qualification at that context. Exact flags and provenance are in [checks.json](../checks.json).

## Additional Test Results

| Result / Source | Profile | Evidence type | Reported outcome | Retained values | Configuration binding |
| --- | --- | --- | --- | --- | --- |
| [result-2ce22c70a50ecc6ad64d](../observations.json)<br>source-d2ae5222ec5e65ffa4fe7aa4.json<br>`/waves/0` | [ad004-flash_next-mtp2-original-layer_split-matched-085](ad004-flash_next-mtp2-original-layer_split-matched-085.md)<br>[record-26c850ec689cf58c6b67](record-26c850ec689cf58c6b67.md)<br>[flash_next-mtp2-original-layer_split](flash_next-mtp2-original-layer_split.md) | performance detail | Outcome unspecified | elapsed_seconds=159.02 s; end_to_end_accepted_tok_s=9.66 accepted tokens/s; output_tokens=256 tokens; ttft_seconds=143.43<br>147.64<br>147.64<br>147.64<br>147.64<br>147.98 s; p50_ms=39.48 ms; p95_ms=117.01 ms; prefill: per-request 225.69 to 231.82 tokens/s; Draft accepted / proposed: 924 / 1,224 tokens; fraction 0.7549 | Recorded configuration/job |
| [result-551686efd9e96978024e](../observations.json)<br>source-7903eda2277dc84d4a059fa3.json<br>`/waves/0` | [ad004-flash_next-mtp2-original-layer_split-matched-085](ad004-flash_next-mtp2-original-layer_split-matched-085.md)<br>[record-26c850ec689cf58c6b67](record-26c850ec689cf58c6b67.md)<br>[flash_next-mtp2-original-layer_split](flash_next-mtp2-original-layer_split.md) | performance detail | Outcome unspecified | elapsed_seconds=27.88 s; end_to_end_accepted_tok_s=9.18 accepted tokens/s; output_tokens=256 tokens; ttft_seconds=24.59 s; p50_ms=11.56 ms; p95_ms=33.13 ms; prefill: per-request 1,337.51 tokens/s; Draft accepted / proposed: 158 / 196 tokens; fraction 0.8061 | Recorded configuration/job |
| [result-5e52807f0c67f430c7d8](../observations.json)<br>source-b9e375fa31acc61379151330.json<br>`/tabby` | [ad004-flash_next-mtp2-original-layer_split-matched-085](ad004-flash_next-mtp2-original-layer_split-matched-085.md) | test outcome | Outcome unspecified | cache_tokens=262,144 tokens | Recorded configuration/job |
| [result-755d9747a0acdc5cd7e6](../observations.json)<br>source-a9e622d351a86c8b776605d4.json<br>`/managed_phase_timings/85` | [ad004-flash_next-mtp2-original-layer_split-matched-085](ad004-flash_next-mtp2-original-layer_split-matched-085.md) | test outcome | Outcome unspecified | wall_seconds=512.83 s | Recorded configuration/job |
| [result-76d97ba07a331f8c69cc](../observations.json)<br>source-7903eda2277dc84d4a059fa3.json<br>`/` | [ad004-flash_next-mtp2-original-layer_split-matched-085](ad004-flash_next-mtp2-original-layer_split-matched-085.md)<br>[record-26c850ec689cf58c6b67](record-26c850ec689cf58c6b67.md)<br>[flash_next-mtp2-original-layer_split](flash_next-mtp2-original-layer_split.md) | performance detail | Pass | elapsed_seconds=27.88 s; end_to_end_accepted_tok_s=9.18 accepted tokens/s; ttft_seconds=24.59 s; p50_ms=11.58 ms; p95_ms=33.08 ms; cold_prefill: per-request 1,337.51 tokens/s; Draft accepted / proposed: 158 / 196 tokens; fraction 0.8061 | Recorded configuration/job |
| [result-8508b655138014899f1a](../observations.json)<br>source-d2ae5222ec5e65ffa4fe7aa4.json<br>`/waves/1` | [ad004-flash_next-mtp2-original-layer_split-matched-085](ad004-flash_next-mtp2-original-layer_split-matched-085.md)<br>[record-26c850ec689cf58c6b67](record-26c850ec689cf58c6b67.md)<br>[flash_next-mtp2-original-layer_split](flash_next-mtp2-original-layer_split.md) | performance detail | Outcome unspecified | elapsed_seconds=12.68 s; end_to_end_accepted_tok_s=121.15 accepted tokens/s; output_tokens=256 tokens; ttft_seconds=0.31<br>1.11<br>1.21<br>1.21<br>1.21<br>1.21 s; p50_ms=38.78 ms; p95_ms=115.09 ms; prefill: per-request 50.00 to 100.00 tokens/s; Draft accepted / proposed: 920 / 1,232 tokens; fraction 0.7468 | Recorded configuration/job |
| [result-e96a1d40418f13ad045e](../observations.json)<br>source-7903eda2277dc84d4a059fa3.json<br>`/waves/1` | [ad004-flash_next-mtp2-original-layer_split-matched-085](ad004-flash_next-mtp2-original-layer_split-matched-085.md)<br>[record-26c850ec689cf58c6b67](record-26c850ec689cf58c6b67.md)<br>[flash_next-mtp2-original-layer_split](flash_next-mtp2-original-layer_split.md) | performance detail | Outcome unspecified | elapsed_seconds=27.89 s; end_to_end_accepted_tok_s=9.18 accepted tokens/s; output_tokens=256 tokens; ttft_seconds=24.63 s; p50_ms=11.58 ms; p95_ms=33.08 ms; prefill: per-request 1,336.96 tokens/s; Draft accepted / proposed: 158 / 196 tokens; fraction 0.8061 | Recorded configuration/job |
| [result-ed158f6e587ed8ff6109](../observations.json)<br>source-d2ae5222ec5e65ffa4fe7aa4.json<br>`/` | [ad004-flash_next-mtp2-original-layer_split-matched-085](ad004-flash_next-mtp2-original-layer_split-matched-085.md)<br>[record-26c850ec689cf58c6b67](record-26c850ec689cf58c6b67.md)<br>[flash_next-mtp2-original-layer_split](flash_next-mtp2-original-layer_split.md) | performance detail | Pass | elapsed_seconds=159.02 s; end_to_end_accepted_tok_s=9.66 accepted tokens/s; ttft_seconds=143.43<br>147.64<br>147.64<br>147.64<br>147.64<br>147.98 s; p50_ms=38.78 ms; p95_ms=115.09 ms; cold_prefill: per-request 225.69 to 231.82 tokens/s; Draft accepted / proposed: 920 / 1,232 tokens; fraction 0.7468 | Recorded configuration/job |
| [result-fd023fcbc1b9b97f4022](../observations.json)<br>source-0be2db8b3e15bf29579d534a.json<br>`/trials/0` | [ad004-flash_next-mtp2-original-layer_split-matched-085](ad004-flash_next-mtp2-original-layer_split-matched-085.md)<br>[flash_next-mtp2-original-layer_split-ad024-max](flash_next-mtp2-original-layer_split-ad024-max.md) | context allocation | Outcome unspecified | resident_pool_tokens=262,144 tokens | Recorded configuration/job |

These are saved result records, including failures and bounded checks. Copies, individual requests, report summaries and regrading can overlap; their counts are not independent test repetitions. Open each result for exact values, units, configuration binding and source receipts.

There are 1 retained lifecycle records. Their states, exit codes and configuration IDs remain in [catalog.json](../catalog.json); they do not supply missing benchmark results.

[Full archive](../../README.md) | [All retained waves](../RESULTS.md) | [Data definitions](../DATA.md) | [Recommended recipes](../../../README.md)
