# ad024-flash_next-mtp2-original-layer_split-ad024-sizing-final-smoke-003

**Historical record. Decode interval measured.**

Model family: Qwen 3.8 Flash Next.

Historical configurations are provided for comparison. The [recommended recipes](../../../README.md) include supported launch scripts.

Current recipes using the same recorded checkpoint repository: [qwen-flash-next-mtp2-layer-split](../../../recipes/qwen-flash-next-mtp2-layer-split/README.md). Context, cache and runtime versions can differ.

## Saved Configuration Versions

Each configuration ID identifies a distinct original settings record. Deployment fields are omitted; versions can have identical published settings after that omission. Upstream runtime commits remain unspecified where the source retained only an integration label.

| Configuration | Recorded artifact / source | Configured card counts | Context tokens | GPU pool tokens | Slots | Draft mode / tokens |
| --- | --- | --- | --- | --- | --- | --- |
| cfg-658e32198a7ed4a0096c | [turboderp/Qwen3.8-Flash-Next-exl3@d2e238feca](https://huggingface.co/turboderp/Qwen3.8-Flash-Next-exl3/tree/d2e238feca4c1c4d966943117356d8a42c2f4dcb) (derived view) | 2 | 524,288 | 1,356,032 | 6 | mtp / 2 |
| cfg-7a49bba636890a739dc2 | [turboderp/Qwen3.8-Flash-Next-exl3@d2e238feca](https://huggingface.co/turboderp/Qwen3.8-Flash-Next-exl3/tree/d2e238feca4c1c4d966943117356d8a42c2f4dcb) (derived view) | 2 | 524,288 | 1,356,032 | 6 | mtp / 2 |

Card counts are saved configuration choices, not a claim that every allowed placement was measured. A derived view can differ from its pinned download source.

<details>
<summary>cfg-658e32198a7ed4a0096c</summary>

```json
{
  "kind": "tabby",
  "gpu_counts": [
    2
  ],
  "context": 524288,
  "cache_tokens": 1356032,
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
  "served_model_label": "qwen3.8-flash-next-yarn524k",
  "derived_model_view_used": true,
  "model_view_metadata_included": false,
  "main_reserve_mib_values_unordered": []
}
```

Pinned model revision recorded: yes. Source receipt labels, hashes and object locators are retained in [configurations.json](../configurations.json).

</details>

<details>
<summary>cfg-7a49bba636890a739dc2</summary>

```json
{
  "kind": "tabby",
  "gpu_counts": [
    2
  ],
  "context": 524288,
  "cache_tokens": 1356032,
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
  "served_model_label": "qwen3.8-flash-next-yarn524k",
  "derived_model_view_used": true,
  "model_view_metadata_included": false
}
```

Pinned model revision recorded: yes. Source receipt labels, hashes and object locators are retained in [configurations.json](../configurations.json).

</details>

## Retained Measurements

| Profile / Wave | Layout; Draft / Tokens | Requests | Input tokens/request | Accepted output tokens/request | Cache / Reused input tokens | Context / GPU pool tokens | Shared decode tok/s total | Client after-first-token estimate tok/s | Whole-wave output tok/s | Median TTFT, s | Source report |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [ad024-flash_next-mtp2-original-layer_split-ad024-sizing-final-smoke-003](ad024-flash_next-mtp2-original-layer_split-ad024-sizing-final-smoke-003.md)<br>wave-630b74118e872bc88fc9 | layer_split; mtp / 2 | 6 | 32,770 | 256 (budget 256) | cold; reused 0 | 524,288 / 1,356,032 | 136.23 | Not recorded | 9.61 | 148.91 | Pass |
| [ad024-flash_next-mtp2-original-layer_split-ad024-sizing-final-smoke-003](ad024-flash_next-mtp2-original-layer_split-ad024-sizing-final-smoke-003.md)<br>wave-718f2a503e4f78c427bb | layer_split; mtp / 2 | 6 | 32,770 | 512 (budget 512) | cached_prefix; reused 32,768 | 524,288 / 1,356,032 | 135.31 | Not recorded | 130.46 | 1.26 | Pass |
| [ad024-flash_next-mtp2-original-layer_split-ad024-sizing-final-smoke-003](ad024-flash_next-mtp2-original-layer_split-ad024-sizing-final-smoke-003.md)<br>wave-cda0dbab3428d6f89297 | layer_split; mtp / 2 | 1 | 32,769 | 256 (budget 256) | cold; reused 0 | 524,288 / 1,356,032 | 73.10 | Not recorded | 9.04 | 24.90 | Pass |
| [ad024-flash_next-mtp2-original-layer_split-ad024-sizing-final-smoke-003](ad024-flash_next-mtp2-original-layer_split-ad024-sizing-final-smoke-003.md)<br>wave-d7f3df57552b56aed3a4 | layer_split; mtp / 2 | 1 | 32,769 | 512 (budget 512) | repeated_input; reused 0 | 524,288 / 1,356,032 | 76.87 | Not recorded | 16.29 | 24.84 | Pass |

Rates are whole-wave totals over the stated request count. A wave may span multiple independent model instances; [measurements.json](../measurements.json) retains their contributions and the exact configuration IDs. Do not interpret a multi-instance total as one card's rate.

A dash in shared decode means no qualified synchronized interval is available. Whole-wave throughput includes prefill and queueing. A valid decode interval can survive inside an overall failed or partial check; the source-report outcome is preserved. No rows are averaged.

## Bounded Checks

| Check | Reported outcome | Retained counts / flags |
| --- | --- | --- |
| check-2214f89f26d72bf4603a | Pass | {"passed":true,"elapsed_seconds":28.319214335999277,"ttft_seconds":[24.895465247995162],"end_to_end_accepted_tok_s":9.039798808068406} |
| check-38a064b107b25b398f45 | Pass | {"passed":true,"configured_slots":6,"context_tokens":524288} |
| check-73d2e2217c9850351e46 | Pass | {"passed":true,"configured_slots":6,"context_tokens":524288} |
| check-8d16538350a9125a012e | Pass | {"passed":true,"elapsed_seconds":159.82273221099604,"ttft_seconds":[145.84402230600244,148.75378214000375,148.90838950299803,148.90805782700045,149.01335957999981,149.01304370899743],"end_to_end_accepted_tok_s":9.610647864361319} |
| check-e28544a667b529fd79a9 | Pass | {"passed":true,"configured_slots":6,"context_tokens":524288} |

These checks retain their reported scope. A context/allocation/retrieval check is not a general quality score or a speed qualification at that context. Exact flags and provenance are in [checks.json](../checks.json).

## Additional Test Results

| Result / Source | Profile | Evidence type | Reported outcome | Retained values | Configuration binding |
| --- | --- | --- | --- | --- | --- |
| [result-0301a9b5d931f4bedceb](../observations.json)<br>source-9c4d35b2493e99776fdf0550.json<br>`/tabby` | [ad024-flash_next-mtp2-original-layer_split-ad024-sizing-final-smoke-003](ad024-flash_next-mtp2-original-layer_split-ad024-sizing-final-smoke-003.md) | test outcome | Outcome unspecified | cache_tokens=1,356,032 tokens | Recorded configuration/job |
| [result-25b9d85453335f2ef02f](../observations.json)<br>source-f5a9859cdbd6041259777651.json<br>`/waves/0` | [ad024-flash_next-mtp2-original-layer_split-ad024-sizing-final-smoke-003](ad024-flash_next-mtp2-original-layer_split-ad024-sizing-final-smoke-003.md) | performance detail | Outcome unspecified | elapsed_seconds=159.82 s; end_to_end_accepted_tok_s=9.61 accepted tokens/s; output_tokens=256 tokens; ttft_seconds=145.84<br>148.75<br>148.91<br>148.91<br>149.01<br>149.01 s; p50_ms=38.14 ms; p95_ms=111.65 ms; prefill: per-request 224.64 to 231.28 tokens/s; Draft accepted / proposed: 939 / 1,194 tokens; fraction 0.7864 | Recorded configuration/job |
| [result-3182b075143960132a89](../observations.json)<br>source-c100d24c337382f80c423e5a.json<br>`/waves/1` | [ad024-flash_next-mtp2-original-layer_split-ad024-sizing-final-smoke-003](ad024-flash_next-mtp2-original-layer_split-ad024-sizing-final-smoke-003.md) | performance detail | Outcome unspecified | elapsed_seconds=31.44 s; end_to_end_accepted_tok_s=16.29 accepted tokens/s; output_tokens=512 tokens; ttft_seconds=24.84 s; p50_ms=11.71 ms; p95_ms=33.13 ms; prefill: per-request 1,324.54 tokens/s; Draft accepted / proposed: 320 / 384 tokens; fraction 0.8333 | Recorded configuration/job |
| [result-4f9220d20ee3c5d16d9d](../observations.json)<br>source-0be2db8b3e15bf29579d534a.json<br>`/trials/1/peak_prefill` | [ad024-flash_next-mtp2-original-layer_split-ad024-sizing-final-smoke-003](ad024-flash_next-mtp2-original-layer_split-ad024-sizing-final-smoke-003.md)<br>[flash_next-mtp2-original-layer_split](flash_next-mtp2-original-layer_split.md)<br>[flash_next-mtp2-original-layer_split-ad024-max](flash_next-mtp2-original-layer_split-ad024-max.md) | context allocation | Pass | configured_slots=6 requests; context_tokens=524,288 tokens | Recorded configuration/job |
| [result-53671e5a04a36161bc20](../observations.json)<br>source-f5a9859cdbd6041259777651.json<br>`/` | [ad024-flash_next-mtp2-original-layer_split-ad024-sizing-final-smoke-003](ad024-flash_next-mtp2-original-layer_split-ad024-sizing-final-smoke-003.md) | performance detail | Pass | elapsed_seconds=159.82 s; end_to_end_accepted_tok_s=9.61 accepted tokens/s; ttft_seconds=145.84<br>148.75<br>148.91<br>148.91<br>149.01<br>149.01 s; p50_ms=39.72 ms; p95_ms=115.67 ms; cold_prefill: per-request 224.64 to 231.28 tokens/s; Draft accepted / proposed: 1,910 / 2,324 tokens; fraction 0.8219 | Recorded configuration/job |
| [result-64aaa1c5eb19c47f8a17](../observations.json)<br>source-d7d16e78e8e5487e3f1f9243.json<br>`/context_smoke` | [ad024-flash_next-mtp2-original-layer_split-ad024-sizing-final-smoke-003](ad024-flash_next-mtp2-original-layer_split-ad024-sizing-final-smoke-003.md)<br>[flash_next-mtp2-original-layer_split-ad024-sizing-final-smoke-fit-phase](flash_next-mtp2-original-layer_split-ad024-sizing-final-smoke-fit-phase.md) | context allocation | Outcome unspecified | context_tokens=524,288 tokens | Recorded configuration/job |
| [result-86480a5eb83dae3a56e7](../observations.json)<br>source-f5a9859cdbd6041259777651.json<br>`/waves/1` | [ad024-flash_next-mtp2-original-layer_split-ad024-sizing-final-smoke-003](ad024-flash_next-mtp2-original-layer_split-ad024-sizing-final-smoke-003.md) | performance detail | Outcome unspecified | elapsed_seconds=23.55 s; end_to_end_accepted_tok_s=130.46 accepted tokens/s; output_tokens=512 tokens; ttft_seconds=0.32<br>1.16<br>1.26<br>1.26<br>1.26<br>1.26 s; p50_ms=39.72 ms; p95_ms=115.67 ms; prefill: per-request 50.00 to 100.00 tokens/s; Draft accepted / proposed: 1,910 / 2,324 tokens; fraction 0.8219 | Recorded configuration/job |
| [result-b0bae356b01437311163](../observations.json)<br>source-c100d24c337382f80c423e5a.json<br>`/` | [ad024-flash_next-mtp2-original-layer_split-ad024-sizing-final-smoke-003](ad024-flash_next-mtp2-original-layer_split-ad024-sizing-final-smoke-003.md) | performance detail | Pass | elapsed_seconds=28.32 s; end_to_end_accepted_tok_s=9.04 accepted tokens/s; ttft_seconds=24.90 s; p50_ms=11.71 ms; p95_ms=33.13 ms; cold_prefill: per-request 1,321.33 tokens/s; Draft accepted / proposed: 320 / 384 tokens; fraction 0.8333 | Recorded configuration/job |
| [result-bc3d87413f41ea308c03](../observations.json)<br>source-c100d24c337382f80c423e5a.json<br>`/waves/0` | [ad024-flash_next-mtp2-original-layer_split-ad024-sizing-final-smoke-003](ad024-flash_next-mtp2-original-layer_split-ad024-sizing-final-smoke-003.md) | performance detail | Outcome unspecified | elapsed_seconds=28.32 s; end_to_end_accepted_tok_s=9.04 accepted tokens/s; output_tokens=256 tokens; ttft_seconds=24.90 s; p50_ms=11.75 ms; p95_ms=33.75 ms; prefill: per-request 1,321.33 tokens/s; Draft accepted / proposed: 156 / 200 tokens; fraction 0.7800 | Recorded configuration/job |
| [result-dffa271deab2b6da0305](../observations.json)<br>source-d7d16e78e8e5487e3f1f9243.json<br>`/` | [ad024-flash_next-mtp2-original-layer_split-ad024-sizing-final-smoke-003](ad024-flash_next-mtp2-original-layer_split-ad024-sizing-final-smoke-003.md)<br>[flash_next-mtp2-original-layer_split-ad024-sizing-final-smoke-fit-phase](flash_next-mtp2-original-layer_split-ad024-sizing-final-smoke-fit-phase.md) | test outcome | passed | See exact JSON for retained flags and timers | Recorded configuration/job |

These are saved result records, including failures and bounded checks. Copies, individual requests, report summaries and regrading can overlap; their counts are not independent test repetitions. Open each result for exact values, units, configuration binding and source receipts.

There are 1 retained lifecycle records. Their states, exit codes and configuration IDs remain in [catalog.json](../catalog.json); they do not supply missing benchmark results.

[Full archive](../../README.md) | [All retained waves](../RESULTS.md) | [Data definitions](../DATA.md) | [Recommended recipes](../../../README.md)
