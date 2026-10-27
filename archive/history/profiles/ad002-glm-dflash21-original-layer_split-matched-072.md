# ad002-glm-dflash21-original-layer_split-matched-072

**Historical record. Decode interval measured.**

Model family: GLM 5.3 Flash.

Historical configurations are provided for comparison. The [recommended recipes](../../../README.md) include supported launch scripts.

Current recipes using the same recorded checkpoint repository: [glm-5.3-flash-mtp1-tp3](../../../recipes/glm-5.3-flash-mtp1-tp3/README.md). Context, cache and runtime versions can differ.

## Saved Configuration Versions

Each configuration ID identifies a distinct original settings record. Deployment fields are omitted; versions can have identical published settings after that omission. Upstream runtime commits remain unspecified where the source retained only an integration label.

| Configuration | Recorded artifact / source | Configured card counts | Context tokens | GPU pool tokens | Slots | Draft mode / tokens |
| --- | --- | --- | --- | --- | --- | --- |
| cfg-b4bf6331108acc44d549 | [turboderp/GLM-5.3-Flash-exl3@2a30229e67](https://huggingface.co/turboderp/GLM-5.3-Flash-exl3/tree/2a30229e67012798ba9f0cd832bb78abf4c363d5) | 3 | 262,144 | 262,144 | 4 | dflash2 / 1 |

Card counts are saved configuration choices, not a claim that every allowed placement was measured. A derived view can differ from its pinned download source.

<details>
<summary>cfg-b4bf6331108acc44d549</summary>

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
  "draft_mode": "dflash2",
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
  "served_model_label": "glm-5.3-flash",
  "main_reserve_mib_values_unordered": [
    2048,
    2560,
    3584
  ],
  "draft_split_mib_values_unordered": [
    3328,
    4864,
    5120
  ]
}
```

Pinned model revision recorded: yes. Source receipt labels, hashes and object locators are retained in [configurations.json](../configurations.json).

</details>

## Retained Measurements

| Profile / Wave | Layout; Draft / Tokens | Requests | Input tokens/request | Accepted output tokens/request | Cache / Reused input tokens | Context / GPU pool tokens | Shared decode tok/s total | Client after-first-token estimate tok/s | Whole-wave output tok/s | Median TTFT, s | Source report |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [ad002-glm-dflash21-original-layer_split-matched-072](ad002-glm-dflash21-original-layer_split-matched-072.md)<br>wave-6d96863c1465d2d89cec | layer_split; dflash2 / 1 | 4 | 32,767 | 256 (budget 256) | cached_prefix; reused 32,512 | 262,144 / 262,144 | 60.34 | Not recorded | 52.48 | 2.74 | Pass |
| [ad002-glm-dflash21-original-layer_split-matched-072](ad002-glm-dflash21-original-layer_split-matched-072.md)<br>wave-7d39d402070569b1b99f | layer_split; dflash2 / 1 | 1 | 32,766 | 256 (budget 256) | cold; reused 0 | 262,144 / 262,144 | 32.90 | Not recorded | 5.57 | 38.24 | Pass |
| [ad002-glm-dflash21-original-layer_split-matched-072](ad002-glm-dflash21-original-layer_split-matched-072.md)<br>wave-92e2dbfd0489e2b21213 | layer_split; dflash2 / 1 | 1 | 32,766 | 256 (budget 256) | cached_prefix; reused 32,512 | 262,144 / 262,144 | 33.20 | Not recorded | 30.70 | 0.72 | Pass |
| [ad002-glm-dflash21-original-layer_split-matched-072](ad002-glm-dflash21-original-layer_split-matched-072.md)<br>wave-d52504f457dce7f03816 | layer_split; dflash2 / 1 | 4 | 32,767 | 256 (budget 256) | cold; reused 0 | 262,144 / 262,144 | 57.68 | Not recorded | 5.96 | 153.63 | Pass |

Rates are whole-wave totals over the stated request count. A wave may span multiple independent model instances; [measurements.json](../measurements.json) retains their contributions and the exact configuration IDs. Do not interpret a multi-instance total as one card's rate.

A dash in shared decode means no qualified synchronized interval is available. Whole-wave throughput includes prefill and queueing. A valid decode interval can survive inside an overall failed or partial check; the source-report outcome is preserved. No rows are averaged.

## Bounded Checks

| Check | Reported outcome | Retained counts / flags |
| --- | --- | --- |
| check-1fb995af469538eb0932 | Pass | {"passed":true,"elapsed_seconds":45.92746942999656,"ttft_seconds":[38.23578264000389],"end_to_end_accepted_tok_s":5.574006214085006} |
| check-690231d7d5669793374b | Pass | {"passed":true,"elapsed_seconds":45.92746942999656,"ttft_seconds":[38.23578264000389],"end_to_end_accepted_tok_s":5.574006214085006} |
| check-a8b71566ea1c9a61e2d9 | Pass | {"passed":true,"elapsed_seconds":171.71923994700046,"ttft_seconds":[151.66197806200216,153.13560037299612,154.13301737599977,154.12635691700416],"end_to_end_accepted_tok_s":5.963222294228928} |
| check-c25fb18c7ccc8a9b00cd | Pass | {"passed":true,"elapsed_seconds":171.71923994700046,"ttft_seconds":[151.66197806200216,153.13560037299612,154.13301737599977,154.12635691700416],"end_to_end_accepted_tok_s":5.963222294228928} |

These checks retain their reported scope. A context/allocation/retrieval check is not a general quality score or a speed qualification at that context. Exact flags and provenance are in [checks.json](../checks.json).

## Additional Test Results

| Result / Source | Profile | Evidence type | Reported outcome | Retained values | Configuration binding |
| --- | --- | --- | --- | --- | --- |
| [result-00c0c167f2f4195d0c91](../observations.json)<br>source-817f35fdedbbac20cfb57bc8.json<br>`/` | [ad002-glm-dflash21-original-layer_split-matched-072](ad002-glm-dflash21-original-layer_split-matched-072.md)<br>[record-26c850ec689cf58c6b67](record-26c850ec689cf58c6b67.md)<br>[glm-dflash21-original-layer_split](glm-dflash21-original-layer_split.md) | performance detail | Pass | elapsed_seconds=45.93 s; end_to_end_accepted_tok_s=5.57 accepted tokens/s; ttft_seconds=38.24 s; p50_ms=28.48 ms; p95_ms=57.56 ms; cold_prefill: per-request 859.55 tokens/s; Draft accepted / proposed: 115 / 141 tokens; fraction 0.8156 | Recorded configuration/job |
| [result-2178b8d01f9ef5fc0c69](../observations.json)<br>source-4b80b0f7c5867eb0d5f52a37.json<br>`/waves/1` | [ad002-glm-dflash21-original-layer_split-matched-072](ad002-glm-dflash21-original-layer_split-matched-072.md)<br>[record-26c850ec689cf58c6b67](record-26c850ec689cf58c6b67.md)<br>[glm-dflash21-original-layer_split](glm-dflash21-original-layer_split.md) | performance detail | Outcome unspecified | elapsed_seconds=19.51 s; end_to_end_accepted_tok_s=52.48 accepted tokens/s; output_tokens=256 tokens; ttft_seconds=0.91<br>2.75<br>2.74<br>2.74 s; p50_ms=63.36 ms; p95_ms=126.15 ms; prefill: per-request 286.52 to 579.55 tokens/s; Draft accepted / proposed: 472 / 552 tokens; fraction 0.8551 | Recorded configuration/job |
| [result-630bb3522387b2c38266](../observations.json)<br>source-4b80b0f7c5867eb0d5f52a37.json<br>`/waves/0` | [ad002-glm-dflash21-original-layer_split-matched-072](ad002-glm-dflash21-original-layer_split-matched-072.md)<br>[record-26c850ec689cf58c6b67](record-26c850ec689cf58c6b67.md)<br>[glm-dflash21-original-layer_split](glm-dflash21-original-layer_split.md) | performance detail | Outcome unspecified | elapsed_seconds=171.72 s; end_to_end_accepted_tok_s=5.96 accepted tokens/s; output_tokens=256 tokens; ttft_seconds=151.66<br>153.14<br>154.13<br>154.13 s; p50_ms=63.97 ms; p95_ms=127.94 ms; prefill: per-request 218.52 to 221.38 tokens/s; Draft accepted / proposed: 464 / 560 tokens; fraction 0.8286 | Recorded configuration/job |
| [result-ac070e522e02d8c255e8](../observations.json)<br>source-817f35fdedbbac20cfb57bc8.json<br>`/waves/0` | [ad002-glm-dflash21-original-layer_split-matched-072](ad002-glm-dflash21-original-layer_split-matched-072.md)<br>[record-26c850ec689cf58c6b67](record-26c850ec689cf58c6b67.md)<br>[glm-dflash21-original-layer_split](glm-dflash21-original-layer_split.md) | performance detail | Outcome unspecified | elapsed_seconds=45.93 s; end_to_end_accepted_tok_s=5.57 accepted tokens/s; output_tokens=256 tokens; ttft_seconds=38.24 s; p50_ms=28.43 ms; p95_ms=57.23 ms; prefill: per-request 859.55 tokens/s; Draft accepted / proposed: 115 / 141 tokens; fraction 0.8156 | Recorded configuration/job |
| [result-d24d8740eb9953985992](../observations.json)<br>source-817f35fdedbbac20cfb57bc8.json<br>`/waves/1` | [ad002-glm-dflash21-original-layer_split-matched-072](ad002-glm-dflash21-original-layer_split-matched-072.md)<br>[record-26c850ec689cf58c6b67](record-26c850ec689cf58c6b67.md)<br>[glm-dflash21-original-layer_split](glm-dflash21-original-layer_split.md) | performance detail | Outcome unspecified | elapsed_seconds=8.34 s; end_to_end_accepted_tok_s=30.70 accepted tokens/s; output_tokens=256 tokens; ttft_seconds=0.72 s; p50_ms=28.48 ms; p95_ms=57.56 ms; prefill: per-request 488.46 tokens/s; Draft accepted / proposed: 115 / 141 tokens; fraction 0.8156 | Recorded configuration/job |
| [result-d2c73fcc2058a182738d](../observations.json)<br>source-4b80b0f7c5867eb0d5f52a37.json<br>`/` | [ad002-glm-dflash21-original-layer_split-matched-072](ad002-glm-dflash21-original-layer_split-matched-072.md)<br>[record-26c850ec689cf58c6b67](record-26c850ec689cf58c6b67.md)<br>[glm-dflash21-original-layer_split](glm-dflash21-original-layer_split.md) | performance detail | Pass | elapsed_seconds=171.72 s; end_to_end_accepted_tok_s=5.96 accepted tokens/s; ttft_seconds=151.66<br>153.14<br>154.13<br>154.13 s; p50_ms=63.36 ms; p95_ms=126.15 ms; cold_prefill: per-request 218.52 to 221.38 tokens/s; Draft accepted / proposed: 472 / 552 tokens; fraction 0.8551 | Recorded configuration/job |
| [result-fcd25d6fdcf555bd622a](../observations.json)<br>source-a9e622d351a86c8b776605d4.json<br>`/managed_phase_timings/72` | [ad002-glm-dflash21-original-layer_split-matched-072](ad002-glm-dflash21-original-layer_split-matched-072.md) | test outcome | Outcome unspecified | wall_seconds=563.49 s | Recorded configuration/job |

These are saved result records, including failures and bounded checks. Copies, individual requests, report summaries and regrading can overlap; their counts are not independent test repetitions. Open each result for exact values, units, configuration binding and source receipts.

There are 1 retained lifecycle records. Their states, exit codes and configuration IDs remain in [catalog.json](../catalog.json); they do not supply missing benchmark results.

[Full archive](../../README.md) | [All retained waves](../RESULTS.md) | [Data definitions](../DATA.md) | [Recommended recipes](../../../README.md)
