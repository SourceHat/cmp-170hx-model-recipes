# ad001-glm-mtp1-original-layer_split-matched-068

**Historical record. Decode interval measured.**

Model family: GLM 5.3 Flash.

Historical configurations are provided for comparison. The [recommended recipes](../../../README.md) include supported launch scripts.

Current recipes using the same recorded checkpoint repository: [glm-5.3-flash-mtp1-tp3](../../../recipes/glm-5.3-flash-mtp1-tp3/README.md). Context, cache and runtime versions can differ.

## Saved Configuration Versions

Each configuration ID identifies a distinct original settings record. Deployment fields are omitted; versions can have identical published settings after that omission. Upstream runtime commits remain unspecified where the source retained only an integration label.

| Configuration | Recorded artifact / source | Configured card counts | Context tokens | GPU pool tokens | Slots | Draft mode / tokens |
| --- | --- | --- | --- | --- | --- | --- |
| cfg-21c31a383be5bb23c955 | [turboderp/GLM-5.3-Flash-exl3@2a30229e67](https://huggingface.co/turboderp/GLM-5.3-Flash-exl3/tree/2a30229e67012798ba9f0cd832bb78abf4c363d5) | 3 | 262,144 | 262,144 | 4 | mtp / 1 |

Card counts are saved configuration choices, not a claim that every allowed placement was measured. A derived view can differ from its pinned download source.

<details>
<summary>cfg-21c31a383be5bb23c955</summary>

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
  "parallelism": "layer_split",
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
| [ad001-glm-mtp1-original-layer_split-matched-068](ad001-glm-mtp1-original-layer_split-matched-068.md)<br>wave-52674f12d8f07deb716b | layer_split; mtp / 1 | 1 | 32,766 | 256 (budget 256) | cached_prefix; reused 32,512 | 262,144 / 262,144 | 36.12 | Not recorded | 32.62 | 0.81 | Pass |
| [ad001-glm-mtp1-original-layer_split-matched-068](ad001-glm-mtp1-original-layer_split-matched-068.md)<br>wave-a916cadf06032151611c | layer_split; mtp / 1 | 4 | 32,767 | 256 (budget 256) | cached_prefix; reused 32,512 | 262,144 / 262,144 | 67.93 | Not recorded | 57.76 | 2.92 | Pass |
| [ad001-glm-mtp1-original-layer_split-matched-068](ad001-glm-mtp1-original-layer_split-matched-068.md)<br>wave-bb1b05e44e8c1431e337 | layer_split; mtp / 1 | 1 | 32,766 | 256 (budget 256) | cold; reused 0 | 262,144 / 262,144 | 35.29 | Not recorded | 5.50 | 39.39 | Pass |
| [ad001-glm-mtp1-original-layer_split-matched-068](ad001-glm-mtp1-original-layer_split-matched-068.md)<br>wave-f85b5150feef57df0472 | layer_split; mtp / 1 | 4 | 32,767 | 256 (budget 256) | cold; reused 0 | 262,144 / 262,144 | 66.81 | Not recorded | 5.93 | 157.48 | Pass |

Rates are whole-wave totals over the stated request count. A wave may span multiple independent model instances; [measurements.json](../measurements.json) retains their contributions and the exact configuration IDs. Do not interpret a multi-instance total as one card's rate.

A dash in shared decode means no qualified synchronized interval is available. Whole-wave throughput includes prefill and queueing. A valid decode interval can survive inside an overall failed or partial check; the source-report outcome is preserved. No rows are averaged.

## Bounded Checks

| Check | Reported outcome | Retained counts / flags |
| --- | --- | --- |
| check-1e8e7a21a9790e4038d6 | Pass | {"passed":true,"elapsed_seconds":46.5435669849976,"ttft_seconds":[39.388594846997876],"end_to_end_accepted_tok_s":5.500223050857201} |
| check-5fa4a7a16702bc49e9a2 | Pass | {"passed":true,"elapsed_seconds":46.5435669849976,"ttft_seconds":[39.388594846997876],"end_to_end_accepted_tok_s":5.500223050857201} |
| check-890bd4913405da9f78a3 | Pass | {"passed":true,"elapsed_seconds":172.67341449200467,"ttft_seconds":[151.27942703800363,157.48061742600112,157.48002206000092,157.4792035270002],"end_to_end_accepted_tok_s":5.9302701751311835} |
| check-d4a26987321b3c6b092b | Pass | {"passed":true,"elapsed_seconds":172.67341449200467,"ttft_seconds":[151.27942703800363,157.48061742600112,157.48002206000092,157.4792035270002],"end_to_end_accepted_tok_s":5.9302701751311835} |

These checks retain their reported scope. A context/allocation/retrieval check is not a general quality score or a speed qualification at that context. Exact flags and provenance are in [checks.json](../checks.json).

## Additional Test Results

| Result / Source | Profile | Evidence type | Reported outcome | Retained values | Configuration binding |
| --- | --- | --- | --- | --- | --- |
| [result-101c98863a8e013e2d92](../observations.json)<br>source-a9e622d351a86c8b776605d4.json<br>`/managed_phase_timings/68` | [ad001-glm-mtp1-original-layer_split-matched-068](ad001-glm-mtp1-original-layer_split-matched-068.md) | test outcome | Outcome unspecified | wall_seconds=581.33 s | Recorded configuration/job |
| [result-2b2776a1a33468df2669](../observations.json)<br>source-9619f1d392377118fd019af1.json<br>`/waves/1` | [ad001-glm-mtp1-original-layer_split-matched-068](ad001-glm-mtp1-original-layer_split-matched-068.md)<br>[record-26c850ec689cf58c6b67](record-26c850ec689cf58c6b67.md)<br>[glm-mtp1-original-layer_split](glm-mtp1-original-layer_split.md) | performance detail | Outcome unspecified | elapsed_seconds=7.85 s; end_to_end_accepted_tok_s=32.62 accepted tokens/s; output_tokens=256 tokens; ttft_seconds=0.81 s; p50_ms=25.89 ms; p95_ms=52.10 ms; prefill: per-request 453.57 tokens/s; Draft accepted / proposed: 112 / 144 tokens; fraction 0.7778 | Recorded configuration/job |
| [result-74db2c2fe34ff7d17fbb](../observations.json)<br>source-8098d9d30e75c1f5791d2fc7.json<br>`/waves/0` | [ad001-glm-mtp1-original-layer_split-matched-068](ad001-glm-mtp1-original-layer_split-matched-068.md)<br>[record-26c850ec689cf58c6b67](record-26c850ec689cf58c6b67.md)<br>[glm-mtp1-original-layer_split](glm-mtp1-original-layer_split.md) | performance detail | Outcome unspecified | elapsed_seconds=172.67 s; end_to_end_accepted_tok_s=5.93 accepted tokens/s; output_tokens=256 tokens; ttft_seconds=151.28<br>157.48<br>157.48<br>157.48 s; p50_ms=56.59 ms; p95_ms=112.39 ms; prefill: per-request 214.07 to 216.87 tokens/s; Draft accepted / proposed: 471 / 553 tokens; fraction 0.8517 | Recorded configuration/job |
| [result-7a30abe06f7f77e833b5](../observations.json)<br>source-8098d9d30e75c1f5791d2fc7.json<br>`/waves/1` | [ad001-glm-mtp1-original-layer_split-matched-068](ad001-glm-mtp1-original-layer_split-matched-068.md)<br>[record-26c850ec689cf58c6b67](record-26c850ec689cf58c6b67.md)<br>[glm-mtp1-original-layer_split](glm-mtp1-original-layer_split.md) | performance detail | Outcome unspecified | elapsed_seconds=17.73 s; end_to_end_accepted_tok_s=57.76 accepted tokens/s; output_tokens=256 tokens; ttft_seconds=0.94<br>2.88<br>2.96<br>2.96 s; p50_ms=57.33 ms; p95_ms=110.00 ms; prefill: per-request 277.17 to 566.67 tokens/s; Draft accepted / proposed: 472 / 552 tokens; fraction 0.8551 | Recorded configuration/job |
| [result-a72f02c0634e3368ee72](../observations.json)<br>source-8098d9d30e75c1f5791d2fc7.json<br>`/` | [ad001-glm-mtp1-original-layer_split-matched-068](ad001-glm-mtp1-original-layer_split-matched-068.md)<br>[record-26c850ec689cf58c6b67](record-26c850ec689cf58c6b67.md)<br>[glm-mtp1-original-layer_split](glm-mtp1-original-layer_split.md) | performance detail | Pass | elapsed_seconds=172.67 s; end_to_end_accepted_tok_s=5.93 accepted tokens/s; ttft_seconds=151.28<br>157.48<br>157.48<br>157.48 s; p50_ms=57.33 ms; p95_ms=110.00 ms; cold_prefill: per-request 214.07 to 216.87 tokens/s; Draft accepted / proposed: 472 / 552 tokens; fraction 0.8551 | Recorded configuration/job |
| [result-b969f904e3254cee6454](../observations.json)<br>source-9619f1d392377118fd019af1.json<br>`/waves/0` | [ad001-glm-mtp1-original-layer_split-matched-068](ad001-glm-mtp1-original-layer_split-matched-068.md)<br>[record-26c850ec689cf58c6b67](record-26c850ec689cf58c6b67.md)<br>[glm-mtp1-original-layer_split](glm-mtp1-original-layer_split.md) | performance detail | Outcome unspecified | elapsed_seconds=46.54 s; end_to_end_accepted_tok_s=5.50 accepted tokens/s; output_tokens=256 tokens; ttft_seconds=39.39 s; p50_ms=26.20 ms; p95_ms=53.03 ms; prefill: per-request 836.51 tokens/s; Draft accepted / proposed: 112 / 144 tokens; fraction 0.7778 | Recorded configuration/job |
| [result-c2e8402008c6d894b618](../observations.json)<br>source-9619f1d392377118fd019af1.json<br>`/` | [ad001-glm-mtp1-original-layer_split-matched-068](ad001-glm-mtp1-original-layer_split-matched-068.md)<br>[record-26c850ec689cf58c6b67](record-26c850ec689cf58c6b67.md)<br>[glm-mtp1-original-layer_split](glm-mtp1-original-layer_split.md) | performance detail | Pass | elapsed_seconds=46.54 s; end_to_end_accepted_tok_s=5.50 accepted tokens/s; ttft_seconds=39.39 s; p50_ms=25.89 ms; p95_ms=52.10 ms; cold_prefill: per-request 836.51 tokens/s; Draft accepted / proposed: 112 / 144 tokens; fraction 0.7778 | Recorded configuration/job |

These are saved result records, including failures and bounded checks. Copies, individual requests, report summaries and regrading can overlap; their counts are not independent test repetitions. Open each result for exact values, units, configuration binding and source receipts.

There are 1 retained lifecycle records. Their states, exit codes and configuration IDs remain in [catalog.json](../catalog.json); they do not supply missing benchmark results.

[Full archive](../../README.md) | [All retained waves](../RESULTS.md) | [Data definitions](../DATA.md) | [Recommended recipes](../../../README.md)
