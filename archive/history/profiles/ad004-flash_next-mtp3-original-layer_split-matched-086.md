# ad004-flash_next-mtp3-original-layer_split-matched-086

**Historical record. Decode interval measured.**

Model family: Qwen 3.8 Flash Next.

Historical configurations are provided for comparison. The [recommended recipes](../../../README.md) include supported launch scripts.

Current recipes using the same recorded checkpoint repository: [qwen-flash-next-mtp2-layer-split](../../../recipes/qwen-flash-next-mtp2-layer-split/README.md). Context, cache and runtime versions can differ.

## Saved Configuration Versions

Each configuration ID identifies a distinct original settings record. Deployment fields are omitted; versions can have identical published settings after that omission. Upstream runtime commits remain unspecified where the source retained only an integration label.

| Configuration | Recorded artifact / source | Configured card counts | Context tokens | GPU pool tokens | Slots | Draft mode / tokens |
| --- | --- | --- | --- | --- | --- | --- |
| cfg-6959b266e334cf96d6a9 | [turboderp/Qwen3.8-Flash-Next-exl3@d2e238feca](https://huggingface.co/turboderp/Qwen3.8-Flash-Next-exl3/tree/d2e238feca4c1c4d966943117356d8a42c2f4dcb) | 2 | 262,144 | 262,144 | 6 | mtp / 3 |

Card counts are saved configuration choices, not a claim that every allowed placement was measured. A derived view can differ from its pinned download source.

<details>
<summary>cfg-6959b266e334cf96d6a9</summary>

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
| [ad004-flash_next-mtp3-original-layer_split-matched-086](ad004-flash_next-mtp3-original-layer_split-matched-086.md)<br>wave-12f6ceb0fabc954e108e | layer_split; mtp / 3 | 6 | 32,770 | 256 (budget 256) | cached_prefix; reused 32,768 | 262,144 / 262,144 | 140.02 | Not recorded | 129.80 | 1.24 | Pass |
| [ad004-flash_next-mtp3-original-layer_split-matched-086](ad004-flash_next-mtp3-original-layer_split-matched-086.md)<br>wave-99ccdfde75c08969109d | layer_split; mtp / 3 | 1 | 32,769 | 256 (budget 256) | repeated_input; reused 0 | 262,144 / 262,144 | 71.70 | Not recorded | 9.11 | 24.64 | Pass |
| [ad004-flash_next-mtp3-original-layer_split-matched-086](ad004-flash_next-mtp3-original-layer_split-matched-086.md)<br>wave-dade7442feef32e09291 | layer_split; mtp / 3 | 1 | 32,769 | 256 (budget 256) | cold; reused 0 | 262,144 / 262,144 | 71.78 | Not recorded | 9.11 | 24.60 | Pass |
| [ad004-flash_next-mtp3-original-layer_split-matched-086](ad004-flash_next-mtp3-original-layer_split-matched-086.md)<br>wave-fa7b5b02902f4d566e7b | layer_split; mtp / 3 | 6 | 32,770 | 256 (budget 256) | cold; reused 0 | 262,144 / 262,144 | 144.02 | Not recorded | 9.71 | 147.93 | Pass |

Rates are whole-wave totals over the stated request count. A wave may span multiple independent model instances; [measurements.json](../measurements.json) retains their contributions and the exact configuration IDs. Do not interpret a multi-instance total as one card's rate.

A dash in shared decode means no qualified synchronized interval is available. Whole-wave throughput includes prefill and queueing. A valid decode interval can survive inside an overall failed or partial check; the source-report outcome is preserved. No rows are averaged.

## Bounded Checks

| Check | Reported outcome | Retained counts / flags |
| --- | --- | --- |
| check-2b9505f84dd99dd63757 | Pass | {"passed":true,"elapsed_seconds":28.09587383300095,"ttft_seconds":[24.597334471000067],"end_to_end_accepted_tok_s":9.11165822859393} |
| check-8d9a9f17fd784039ec99 | Pass | {"passed":true,"elapsed_seconds":28.09587383300095,"ttft_seconds":[24.597334471000067],"end_to_end_accepted_tok_s":9.11165822859393} |
| check-a45a944a011d339ef505 | Pass | {"passed":true,"elapsed_seconds":158.24190351400466,"ttft_seconds":[142.70030783199763,147.65001067100093,147.9290596139981,147.92872813400027,147.92871490200196,147.928384578001],"end_to_end_accepted_tok_s":9.706657755567642} |
| check-bb65a47722256c906e5d | Pass | {"passed":true,"elapsed_seconds":158.24190351400466,"ttft_seconds":[142.70030783199763,147.65001067100093,147.9290596139981,147.92872813400027,147.92871490200196,147.928384578001],"end_to_end_accepted_tok_s":9.706657755567642} |

These checks retain their reported scope. A context/allocation/retrieval check is not a general quality score or a speed qualification at that context. Exact flags and provenance are in [checks.json](../checks.json).

## Additional Test Results

| Result / Source | Profile | Evidence type | Reported outcome | Retained values | Configuration binding |
| --- | --- | --- | --- | --- | --- |
| [result-11b5ca3f6c85176c60df](../observations.json)<br>source-ca16cb80743e38127fa3a10d.json<br>`/waves/0` | [ad004-flash_next-mtp3-original-layer_split-matched-086](ad004-flash_next-mtp3-original-layer_split-matched-086.md)<br>[record-26c850ec689cf58c6b67](record-26c850ec689cf58c6b67.md)<br>[flash_next-mtp3-original-layer_split](flash_next-mtp3-original-layer_split.md) | performance detail | Outcome unspecified | elapsed_seconds=28.10 s; end_to_end_accepted_tok_s=9.11 accepted tokens/s; output_tokens=256 tokens; ttft_seconds=24.60 s; p50_ms=12.85 ms; p95_ms=37.82 ms; prefill: per-request 1,337.51 tokens/s; Draft accepted / proposed: 164 / 276 tokens; fraction 0.5942 | Recorded configuration/job |
| [result-63bcd2c40966321f3fb9](../observations.json)<br>source-4a0c50d42a89ea759ca73efc.json<br>`/waves/0` | [ad004-flash_next-mtp3-original-layer_split-matched-086](ad004-flash_next-mtp3-original-layer_split-matched-086.md)<br>[record-26c850ec689cf58c6b67](record-26c850ec689cf58c6b67.md)<br>[flash_next-mtp3-original-layer_split](flash_next-mtp3-original-layer_split.md) | performance detail | Outcome unspecified | elapsed_seconds=158.24 s; end_to_end_accepted_tok_s=9.71 accepted tokens/s; output_tokens=256 tokens; ttft_seconds=142.70<br>147.65<br>147.93<br>147.93<br>147.93<br>147.93 s; p50_ms=33.81 ms; p95_ms=126.49 ms; prefill: per-request 225.78 to 229.95 tokens/s; Draft accepted / proposed: 1,031 / 1,515 tokens; fraction 0.6805 | Recorded configuration/job |
| [result-8556ffc658850a7bcdea](../observations.json)<br>source-4a0c50d42a89ea759ca73efc.json<br>`/waves/1` | [ad004-flash_next-mtp3-original-layer_split-matched-086](ad004-flash_next-mtp3-original-layer_split-matched-086.md)<br>[record-26c850ec689cf58c6b67](record-26c850ec689cf58c6b67.md)<br>[flash_next-mtp3-original-layer_split](flash_next-mtp3-original-layer_split.md) | performance detail | Outcome unspecified | elapsed_seconds=11.83 s; end_to_end_accepted_tok_s=129.80 accepted tokens/s; output_tokens=256 tokens; ttft_seconds=0.33<br>1.19<br>1.19<br>1.30<br>1.30<br>1.30 s; p50_ms=34.26 ms; p95_ms=131.55 ms; prefill: per-request 50.00 to 100.00 tokens/s; Draft accepted / proposed: 1,025 / 1,533 tokens; fraction 0.6686 | Recorded configuration/job |
| [result-85c3f98b066ab90cedc0](../observations.json)<br>source-ca16cb80743e38127fa3a10d.json<br>`/` | [ad004-flash_next-mtp3-original-layer_split-matched-086](ad004-flash_next-mtp3-original-layer_split-matched-086.md)<br>[record-26c850ec689cf58c6b67](record-26c850ec689cf58c6b67.md)<br>[flash_next-mtp3-original-layer_split](flash_next-mtp3-original-layer_split.md) | performance detail | Pass | elapsed_seconds=28.10 s; end_to_end_accepted_tok_s=9.11 accepted tokens/s; ttft_seconds=24.60 s; p50_ms=12.75 ms; p95_ms=38.07 ms; cold_prefill: per-request 1,337.51 tokens/s; Draft accepted / proposed: 164 / 276 tokens; fraction 0.5942 | Recorded configuration/job |
| [result-9bac52507910a04c7503](../observations.json)<br>source-ca16cb80743e38127fa3a10d.json<br>`/waves/1` | [ad004-flash_next-mtp3-original-layer_split-matched-086](ad004-flash_next-mtp3-original-layer_split-matched-086.md)<br>[record-26c850ec689cf58c6b67](record-26c850ec689cf58c6b67.md)<br>[flash_next-mtp3-original-layer_split](flash_next-mtp3-original-layer_split.md) | performance detail | Outcome unspecified | elapsed_seconds=28.11 s; end_to_end_accepted_tok_s=9.11 accepted tokens/s; output_tokens=256 tokens; ttft_seconds=24.64 s; p50_ms=12.75 ms; p95_ms=38.07 ms; prefill: per-request 1,336.96 tokens/s; Draft accepted / proposed: 164 / 276 tokens; fraction 0.5942 | Recorded configuration/job |
| [result-ac9af294401c795a31ee](../observations.json)<br>source-4a0c50d42a89ea759ca73efc.json<br>`/` | [ad004-flash_next-mtp3-original-layer_split-matched-086](ad004-flash_next-mtp3-original-layer_split-matched-086.md)<br>[record-26c850ec689cf58c6b67](record-26c850ec689cf58c6b67.md)<br>[flash_next-mtp3-original-layer_split](flash_next-mtp3-original-layer_split.md) | performance detail | Pass | elapsed_seconds=158.24 s; end_to_end_accepted_tok_s=9.71 accepted tokens/s; ttft_seconds=142.70<br>147.65<br>147.93<br>147.93<br>147.93<br>147.93 s; p50_ms=34.26 ms; p95_ms=131.55 ms; cold_prefill: per-request 225.78 to 229.95 tokens/s; Draft accepted / proposed: 1,025 / 1,533 tokens; fraction 0.6686 | Recorded configuration/job |
| [result-c8e9d17ec4e0e412c86c](../observations.json)<br>source-a9e622d351a86c8b776605d4.json<br>`/managed_phase_timings/86` | [ad004-flash_next-mtp3-original-layer_split-matched-086](ad004-flash_next-mtp3-original-layer_split-matched-086.md) | test outcome | Outcome unspecified | wall_seconds=508.60 s | Recorded configuration/job |

These are saved result records, including failures and bounded checks. Copies, individual requests, report summaries and regrading can overlap; their counts are not independent test repetitions. Open each result for exact values, units, configuration binding and source receipts.

There are 1 retained lifecycle records. Their states, exit codes and configuration IDs remain in [catalog.json](../catalog.json); they do not supply missing benchmark results.

[Full archive](../../README.md) | [All retained waves](../RESULTS.md) | [Data definitions](../DATA.md) | [Recommended recipes](../../../README.md)
