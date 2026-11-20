# ad024-orca-yarn-001

**Historical record. Decode interval measured.**

Model family: Orca (Qwen 3.8 27B abliterated).

Historical configurations are provided for comparison. The [recommended recipes](../../../README.md) include supported launch scripts.

Current recipes using the same recorded checkpoint repository: [qwen27-orca-mtp3-native](../../../recipes/qwen27-orca-mtp3-native/README.md). Context, cache and runtime versions can differ.

## Saved Configuration Versions

Each configuration ID identifies a distinct original settings record. Deployment fields are omitted; versions can have identical published settings after that omission. Upstream runtime commits remain unspecified where the source retained only an integration label.

| Configuration | Recorded artifact / source | Configured card counts | Context tokens | GPU pool tokens | Slots | Draft mode / tokens |
| --- | --- | --- | --- | --- | --- | --- |
| cfg-7dc398ad52692a1fce0e | [Lygodactylus/Qwen3.8-27B-Uncensored-exl3-8bpw@3487b152b3](https://huggingface.co/Lygodactylus/Qwen3.8-27B-Uncensored-exl3-8bpw/tree/3487b152b302930e303dc4a2e99e7e976e3ad28f) (derived view) | 1 | 524,288 | 866,560 | 8 | mtp / 3 |
| cfg-cc314dde4061de03f4bd | [Lygodactylus/Qwen3.8-27B-Uncensored-exl3-8bpw@3487b152b3](https://huggingface.co/Lygodactylus/Qwen3.8-27B-Uncensored-exl3-8bpw/tree/3487b152b302930e303dc4a2e99e7e976e3ad28f) (derived view) | 1 | 524,288 | 866,560 | 8 | mtp / 3 |

Card counts are saved configuration choices, not a claim that every allowed placement was measured. A derived view can differ from its pinned download source.

<details>
<summary>cfg-7dc398ad52692a1fce0e</summary>

```json
{
  "kind": "tabby",
  "gpu_counts": [
    1
  ],
  "context": 524288,
  "cache_tokens": 866560,
  "cache_mode": "Q8",
  "draft_cache_mode": "Q8",
  "draft_mode": "mtp",
  "draft_tokens": 3,
  "max_sessions": 8,
  "chunk_size": 512,
  "reserve_mib": 128,
  "ram_kv_mib": 8192,
  "ram_recurrent_mib": 16384,
  "dynamic_draft": false,
  "output_chunk_tokens": 4096,
  "power_watts": 200,
  "host_memory_gib": 80,
  "host_swap_gib": 0,
  "min_vram_mib_per_gpu": 65530,
  "min_effective_vram_mib": 65530,
  "parallelism": "layer_split",
  "transport": "host",
  "host_backing": "ordinary",
  "model_repository": "Lygodactylus/Qwen3.8-27B-Uncensored-exl3-8bpw",
  "model_revision": "3487b152b302930e303dc4a2e99e7e976e3ad28f",
  "draft_repository": null,
  "draft_revision": null,
  "recorded_runtime_label": null,
  "served_model_label": "qwen27-orca-exl3-8bpw-yarn524k",
  "derived_model_view_used": true,
  "model_view_metadata_included": false,
  "main_reserve_mib_values_unordered": []
}
```

Pinned model revision recorded: yes. Source receipt labels, hashes and object locators are retained in [configurations.json](../configurations.json).

</details>

<details>
<summary>cfg-cc314dde4061de03f4bd</summary>

```json
{
  "kind": "tabby",
  "gpu_counts": [
    1
  ],
  "context": 524288,
  "cache_tokens": 866560,
  "cache_mode": "Q8",
  "draft_cache_mode": "Q8",
  "draft_mode": "mtp",
  "draft_tokens": 3,
  "max_sessions": 8,
  "chunk_size": 512,
  "reserve_mib": 128,
  "ram_kv_mib": 8192,
  "ram_recurrent_mib": 16384,
  "dynamic_draft": false,
  "output_chunk_tokens": 4096,
  "power_watts": 200,
  "host_memory_gib": 80,
  "host_swap_gib": 0,
  "min_vram_mib_per_gpu": 65530,
  "min_effective_vram_mib": 65530,
  "parallelism": "layer_split",
  "transport": "host",
  "host_backing": "ordinary",
  "model_repository": "Lygodactylus/Qwen3.8-27B-Uncensored-exl3-8bpw",
  "model_revision": "3487b152b302930e303dc4a2e99e7e976e3ad28f",
  "draft_repository": null,
  "draft_revision": null,
  "recorded_runtime_label": null,
  "served_model_label": "qwen27-orca-exl3-8bpw-yarn524k",
  "derived_model_view_used": true,
  "model_view_metadata_included": false
}
```

Pinned model revision recorded: yes. Source receipt labels, hashes and object locators are retained in [configurations.json](../configurations.json).

</details>

## Retained Measurements

| Profile / Wave | Layout; Draft / Tokens | Requests | Input tokens/request | Accepted output tokens/request | Cache / Reused input tokens | Context / GPU pool tokens | Shared decode tok/s total | Client after-first-token estimate tok/s | Whole-wave output tok/s | Median TTFT, s | Source report |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [ad024-orca-yarn-001](ad024-orca-yarn-001.md)<br>wave-16e528b131b4d1cf8331 | layer_split; mtp / 3 | 8 | 32,770 | 256 (budget 256) | cold; reused 0 | 524,288 / 866,560 | 109.65 | Not recorded | 9.36 | 200.81 | Pass |
| [ad024-orca-yarn-001](ad024-orca-yarn-001.md)<br>wave-41f4d559355370e6a15a | layer_split; mtp / 3 | 1 | 32,769 | 512 (budget 512) | repeated_input; reused 0 | 524,288 / 866,560 | 50.12 | Not recorded | 14.62 | 24.90 | Pass |
| [ad024-orca-yarn-001](ad024-orca-yarn-001.md)<br>wave-713d95dfa3a0b47229e2 | layer_split; mtp / 3 | 8 | 2,027 | 256 (budget 256) | cold; reused 0 | 524,288 / 866,560 | 197.57 | Not recorded | 89.00 | 12.00 | Pass |
| [ad024-orca-yarn-001](ad024-orca-yarn-001.md)<br>wave-7fa36a2957826e73fd6a | layer_split; mtp / 3 | 1 | 2,026 | 512 (budget 512) | cached_prefix; reused 1,792 | 524,288 / 866,560 | 59.70 | Not recorded | 57.92 | 0.40 | Pass |
| [ad024-orca-yarn-001](ad024-orca-yarn-001.md)<br>wave-9834fa19db403db4ac09 | layer_split; mtp / 3 | 1 | 2,026 | 256 (budget 256) | cold; reused 0 | 524,288 / 866,560 | 57.20 | Not recorded | 42.94 | 1.61 | Pass |
| [ad024-orca-yarn-001](ad024-orca-yarn-001.md)<br>wave-a6048410759eaf548e73 | layer_split; mtp / 3 | 8 | 2,027 | 512 (budget 512) | cached_prefix; reused 1,792 | 524,288 / 866,560 | 204.77 | Not recorded | 179.31 | 3.28 | Pass |
| [ad024-orca-yarn-001](ad024-orca-yarn-001.md)<br>wave-c32a4abe5853747245bd | layer_split; mtp / 3 | 8 | 32,770 | 512 (budget 512) | cached_prefix; reused 32,768 | 524,288 / 866,560 | 112.06 | Not recorded | 108.12 | 2.04 | Pass |
| [ad024-orca-yarn-001](ad024-orca-yarn-001.md)<br>wave-d51228e98ab7aa44f218 | layer_split; mtp / 3 | 1 | 32,769 | 256 (budget 256) | cold; reused 0 | 524,288 / 866,560 | 48.00 | Not recorded | 8.53 | 24.82 | Pass |

Rates are whole-wave totals over the stated request count. A wave may span multiple independent model instances; [measurements.json](../measurements.json) retains their contributions and the exact configuration IDs. Do not interpret a multi-instance total as one card's rate.

A dash in shared decode means no qualified synchronized interval is available. Whole-wave throughput includes prefill and queueing. A valid decode interval can survive inside an overall failed or partial check; the source-report outcome is preserved. No rows are averaged.

## Bounded Checks

| Check | Reported outcome | Retained counts / flags |
| --- | --- | --- |
| check-2fccbf662650598f6329 | Pass | {"passed":true,"elapsed_seconds":218.72628038199764,"ttft_seconds":[194.3449155279959,199.27218240899674,200.81402907399752,200.81370170200535,200.81408546300372,200.81374422099907,201.01844442999572,201.0181243449988],"end_to_end_accepted_tok_s":9.363301000790765} |
| check-88cb17fe212db28203b2 | Pass | {"passed":true,"elapsed_seconds":5.961614462001307,"ttft_seconds":[1.6070672970017768],"end_to_end_accepted_tok_s":42.94138804709976} |
| check-9031988de2f938adb7d0 | Pass | {"passed":true,"elapsed_seconds":23.011728936995496,"ttft_seconds":[6.969335497000429,9.18684362500062,11.037290383996151,11.037192600997514,12.958745776995784,12.958593160998134,13.128676804997667,13.128506792003463],"end_to_end_accepted_tok_s":88.99809334653996} |
| check-d69ba21c155fd9754107 | Pass | {"passed":true,"elapsed_seconds":30.004583556001307,"ttft_seconds":[24.815826793994347],"end_to_end_accepted_tok_s":8.532029765458839} |

These checks retain their reported scope. A context/allocation/retrieval check is not a general quality score or a speed qualification at that context. Exact flags and provenance are in [checks.json](../checks.json).

## Additional Test Results

| Result / Source | Profile | Evidence type | Reported outcome | Retained values | Configuration binding |
| --- | --- | --- | --- | --- | --- |
| [result-16b83b8bcceeae5c7d68](../observations.json)<br>source-eb1d2f125b753efd6b5fc2e1.json<br>`/` | [ad024-orca-yarn-001](ad024-orca-yarn-001.md) | performance detail | Pass | elapsed_seconds=30.00 s; end_to_end_accepted_tok_s=8.53 accepted tokens/s; ttft_seconds=24.82 s; p50_ms=19.39 ms; p95_ms=57.94 ms; cold_prefill: per-request 1,326.68 tokens/s; Draft accepted / proposed: 338 / 522 tokens; fraction 0.6475 | Recorded configuration/job |
| [result-67612280159102f4bd85](../observations.json)<br>source-8599f2ae44956b6e2694f355.json<br>`/waves/1` | [ad024-orca-yarn-001](ad024-orca-yarn-001.md) | performance detail | Outcome unspecified | elapsed_seconds=37.88 s; end_to_end_accepted_tok_s=108.12 accepted tokens/s; output_tokens=512 tokens; ttft_seconds=0.46<br>1.74<br>1.73<br>2.04<br>2.04<br>2.04<br>2.04<br>2.04 s; p50_ms=67.64 ms; p95_ms=204.49 ms; prefill: per-request 25.00 to 50.00 tokens/s; Draft accepted / proposed: 2,676 / 4,260 tokens; fraction 0.6282 | Recorded configuration/job |
| [result-704f87e2b52846ecf274](../observations.json)<br>source-8599f2ae44956b6e2694f355.json<br>`/waves/0` | [ad024-orca-yarn-001](ad024-orca-yarn-001.md) | performance detail | Outcome unspecified | elapsed_seconds=218.73 s; end_to_end_accepted_tok_s=9.36 accepted tokens/s; output_tokens=256 tokens; ttft_seconds=194.34<br>199.27<br>200.81<br>200.81<br>200.81<br>200.81<br>201.02<br>201.02 s; p50_ms=67.56 ms; p95_ms=204.04 ms; prefill: per-request 166.48 to 171.53 tokens/s; Draft accepted / proposed: 1,329 / 2,157 tokens; fraction 0.6161 | Recorded configuration/job |
| [result-712463fa4ab072c86912](../observations.json)<br>source-d02c725b42c086dc3d743864.json<br>`/waves/0` | [ad024-orca-yarn-001](ad024-orca-yarn-001.md) | performance detail | Outcome unspecified | elapsed_seconds=23.01 s; end_to_end_accepted_tok_s=89.00 accepted tokens/s; output_tokens=256 tokens; ttft_seconds=6.97<br>9.19<br>11.04<br>11.04<br>12.96<br>12.96<br>13.13<br>13.13 s; p50_ms=36.64 ms; p95_ms=108.64 ms; prefill: per-request 224.97 to 442.58 tokens/s; Draft accepted / proposed: 1,335 / 2,139 tokens; fraction 0.6241 | Recorded configuration/job |
| [result-738cad8f844e2b784273](../observations.json)<br>source-8599f2ae44956b6e2694f355.json<br>`/` | [ad024-orca-yarn-001](ad024-orca-yarn-001.md) | performance detail | Pass | elapsed_seconds=218.73 s; end_to_end_accepted_tok_s=9.36 accepted tokens/s; ttft_seconds=194.34<br>199.27<br>200.81<br>200.81<br>200.81<br>200.81<br>201.02<br>201.02 s; p50_ms=67.64 ms; p95_ms=204.49 ms; cold_prefill: per-request 166.48 to 171.53 tokens/s; Draft accepted / proposed: 2,676 / 4,260 tokens; fraction 0.6282 | Recorded configuration/job |
| [result-7ba30f2b955adead0d6d](../observations.json)<br>source-eb1d2f125b753efd6b5fc2e1.json<br>`/waves/1` | [ad024-orca-yarn-001](ad024-orca-yarn-001.md) | performance detail | Outcome unspecified | elapsed_seconds=35.01 s; end_to_end_accepted_tok_s=14.62 accepted tokens/s; output_tokens=512 tokens; ttft_seconds=24.90 s; p50_ms=19.39 ms; p95_ms=57.94 ms; prefill: per-request 1,322.40 tokens/s; Draft accepted / proposed: 338 / 522 tokens; fraction 0.6475 | Recorded configuration/job |
| [result-841d365b55eb0eba45ff](../observations.json)<br>source-797606345fa45914fcd85b71.json<br>`/profiles/qwen27-orca-mtp3-yarn524k/raw_followup/final_geometry/stats/totals` | [ad024-orca-yarn-001](ad024-orca-yarn-001.md)<br>[qwen27-orca-mtp3-yarn524k](qwen27-orca-mtp3-yarn524k.md) | context allocation | Outcome unspecified | cached_tokens=278,272 tokens; generated_tokens=14,253 accepted tokens; prompt_tokens=627,685 tokens; recurrent_restores=17 checkpoints | Recorded configuration/job |
| [result-9671698c402f46c94c8e](../observations.json)<br>source-1457c5c1a6a2205288c3578d.json<br>`/` | [ad024-orca-yarn-001](ad024-orca-yarn-001.md) | performance detail | Pass | elapsed_seconds=5.96 s; end_to_end_accepted_tok_s=42.94 accepted tokens/s; ttft_seconds=1.61 s; p50_ms=15.73 ms; p95_ms=46.46 ms; cold_prefill: per-request 1,307.10 tokens/s; Draft accepted / proposed: 331 / 543 tokens; fraction 0.6096 | Recorded configuration/job |
| [result-a4874ec3d245f7d4f2f3](../observations.json)<br>source-797606345fa45914fcd85b71.json<br>`/profiles/qwen27-orca-mtp3-yarn524k/raw_followup/quality` | [ad024-orca-yarn-001](ad024-orca-yarn-001.md)<br>[qwen27-orca-mtp3-yarn524k](qwen27-orca-mtp3-yarn524k.md) | quality evaluation | 6 / 8 tasks passed | Task latency median 4.03 s; n=8 | Recorded configuration/job |
| [result-c436332ba76cb0f7ec78](../observations.json)<br>source-d02c725b42c086dc3d743864.json<br>`/waves/1` | [ad024-orca-yarn-001](ad024-orca-yarn-001.md) | performance detail | Outcome unspecified | elapsed_seconds=22.84 s; end_to_end_accepted_tok_s=179.31 accepted tokens/s; output_tokens=512 tokens; ttft_seconds=0.50<br>2.47<br>3.28<br>3.28<br>3.28<br>3.28<br>3.28<br>3.28 s; p50_ms=36.73 ms; p95_ms=109.64 ms; prefill: per-request 405.17 to 810.34 tokens/s; Draft accepted / proposed: 2,655 / 4,323 tokens; fraction 0.6142 | Recorded configuration/job |
| [result-cafe614e808ae26d5c63](../observations.json)<br>source-797606345fa45914fcd85b71.json<br>`/profiles/qwen27-orca-mtp3-yarn524k/raw_followup/final_geometry/stats/cache` | [ad024-orca-yarn-001](ad024-orca-yarn-001.md)<br>[qwen27-orca-mtp3-yarn524k](qwen27-orca-mtp3-yarn524k.md) | test outcome | Outcome unspecified | cached_tokens=320,256 tokens | Recorded configuration/job |
| [result-cdf13f5a9341161150a3](../observations.json)<br>source-94c03c1e5b9d2af5e9a505fb.json<br>`/tabby` | [ad024-orca-yarn-001](ad024-orca-yarn-001.md) | test outcome | Outcome unspecified | cache_tokens=866,560 tokens | Recorded configuration/job |
| [result-dfc649cc9e24f0319658](../observations.json)<br>source-797606345fa45914fcd85b71.json<br>`/profiles/qwen27-orca-mtp3-yarn524k/raw_followup/final_geometry/stats` | [ad024-orca-yarn-001](ad024-orca-yarn-001.md)<br>[qwen27-orca-mtp3-yarn524k](qwen27-orca-mtp3-yarn524k.md) | test outcome | Outcome unspecified | context=524,288 tokens | Recorded configuration/job |
| [result-e17a5592c650ebdfe43f](../observations.json)<br>source-d02c725b42c086dc3d743864.json<br>`/` | [ad024-orca-yarn-001](ad024-orca-yarn-001.md) | performance detail | Pass | elapsed_seconds=23.01 s; end_to_end_accepted_tok_s=89.00 accepted tokens/s; ttft_seconds=6.97<br>9.19<br>11.04<br>11.04<br>12.96<br>12.96<br>13.13<br>13.13 s; p50_ms=36.73 ms; p95_ms=109.64 ms; cold_prefill: per-request 224.97 to 442.58 tokens/s; Draft accepted / proposed: 2,655 / 4,323 tokens; fraction 0.6142 | Recorded configuration/job |
| [result-fad73c4e7873880b43b5](../observations.json)<br>source-1457c5c1a6a2205288c3578d.json<br>`/waves/0` | [ad024-orca-yarn-001](ad024-orca-yarn-001.md) | performance detail | Outcome unspecified | elapsed_seconds=5.96 s; end_to_end_accepted_tok_s=42.94 accepted tokens/s; output_tokens=256 tokens; ttft_seconds=1.61 s; p50_ms=15.69 ms; p95_ms=46.27 ms; prefill: per-request 1,307.10 tokens/s; Draft accepted / proposed: 163 / 279 tokens; fraction 0.5842 | Recorded configuration/job |
| [result-fb72b56a134c3199cd44](../observations.json)<br>source-eb1d2f125b753efd6b5fc2e1.json<br>`/waves/0` | [ad024-orca-yarn-001](ad024-orca-yarn-001.md) | performance detail | Outcome unspecified | elapsed_seconds=30.00 s; end_to_end_accepted_tok_s=8.53 accepted tokens/s; output_tokens=256 tokens; ttft_seconds=24.82 s; p50_ms=19.47 ms; p95_ms=57.85 ms; prefill: per-request 1,326.68 tokens/s; Draft accepted / proposed: 166 / 270 tokens; fraction 0.6148 | Recorded configuration/job |
| [result-fc257a96bf2616f4925a](../observations.json)<br>source-1457c5c1a6a2205288c3578d.json<br>`/waves/1` | [ad024-orca-yarn-001](ad024-orca-yarn-001.md) | performance detail | Outcome unspecified | elapsed_seconds=8.84 s; end_to_end_accepted_tok_s=57.92 accepted tokens/s; output_tokens=512 tokens; ttft_seconds=0.40 s; p50_ms=15.73 ms; p95_ms=46.46 ms; prefill: per-request 806.90 tokens/s; Draft accepted / proposed: 331 / 543 tokens; fraction 0.6096 | Recorded configuration/job |

These are saved result records, including failures and bounded checks. Copies, individual requests, report summaries and regrading can overlap; their counts are not independent test repetitions. Open each result for exact values, units, configuration binding and source receipts.

There are 1 retained lifecycle records. Their states, exit codes and configuration IDs remain in [catalog.json](../catalog.json); they do not supply missing benchmark results.

[Full archive](../../README.md) | [All retained waves](../RESULTS.md) | [Data definitions](../DATA.md) | [Recommended recipes](../../../README.md)
