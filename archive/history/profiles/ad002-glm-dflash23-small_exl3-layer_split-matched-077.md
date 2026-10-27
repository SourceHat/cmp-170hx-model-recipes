# ad002-glm-dflash23-small_exl3-layer_split-matched-077

**Historical record. Decode interval measured.**

Model family: GLM 5.3 Flash.

Historical configurations are provided for comparison. The [recommended recipes](../../../README.md) include supported launch scripts.

Current recipes using the same recorded checkpoint repository: [glm-5.3-flash-mtp1-tp3](../../../recipes/glm-5.3-flash-mtp1-tp3/README.md). Context, cache and runtime versions can differ.

## Saved Configuration Versions

Each configuration ID identifies a distinct original settings record. Deployment fields are omitted; versions can have identical published settings after that omission. Upstream runtime commits remain unspecified where the source retained only an integration label.

| Configuration | Recorded artifact / source | Configured card counts | Context tokens | GPU pool tokens | Slots | Draft mode / tokens |
| --- | --- | --- | --- | --- | --- | --- |
| cfg-edb976bdd38e5b5f78c9 | [turboderp/GLM-5.3-Flash-exl3@2a30229e67](https://huggingface.co/turboderp/GLM-5.3-Flash-exl3/tree/2a30229e67012798ba9f0cd832bb78abf4c363d5) | 3 | 262,144 | 262,144 | 4 | dflash2 / 3 |

Card counts are saved configuration choices, not a claim that every allowed placement was measured. A derived view can differ from its pinned download source.

<details>
<summary>cfg-edb976bdd38e5b5f78c9</summary>

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
  "draft_tokens": 3,
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
    3584
  ]
}
```

Pinned model revision recorded: yes. Source receipt labels, hashes and object locators are retained in [configurations.json](../configurations.json).

</details>

## Retained Measurements

| Profile / Wave | Layout; Draft / Tokens | Requests | Input tokens/request | Accepted output tokens/request | Cache / Reused input tokens | Context / GPU pool tokens | Shared decode tok/s total | Client after-first-token estimate tok/s | Whole-wave output tok/s | Median TTFT, s | Source report |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [ad002-glm-dflash23-small_exl3-layer_split-matched-077](ad002-glm-dflash23-small_exl3-layer_split-matched-077.md)<br>wave-000f08f5a76db8a0caf9 | layer_split; dflash2 / 3 | 1 | 32,766 | 256 (budget 256) | cached_prefix; reused 32,512 | 262,144 / 262,144 | 43.46 | Not recorded | 39.00 | 0.74 | Pass |
| [ad002-glm-dflash23-small_exl3-layer_split-matched-077](ad002-glm-dflash23-small_exl3-layer_split-matched-077.md)<br>wave-30f7712c83e27ad7b383 | layer_split; dflash2 / 3 | 4 | 32,767 | 256 (budget 256) | cold; reused 0 | 262,144 / 262,144 | 48.88 | Not recorded | 5.79 | 155.63 | Pass |
| [ad002-glm-dflash23-small_exl3-layer_split-matched-077](ad002-glm-dflash23-small_exl3-layer_split-matched-077.md)<br>wave-8a48fe7f7025d9c16d26 | layer_split; dflash2 / 3 | 4 | 32,767 | 256 (budget 256) | cached_prefix; reused 32,512 | 262,144 / 262,144 | 49.80 | Not recorded | 43.73 | 2.80 | Pass |
| [ad002-glm-dflash23-small_exl3-layer_split-matched-077](ad002-glm-dflash23-small_exl3-layer_split-matched-077.md)<br>wave-e6a079b0540b8a4e999b | layer_split; dflash2 / 3 | 1 | 32,766 | 256 (budget 256) | cold; reused 0 | 262,144 / 262,144 | 42.82 | Not recorded | 5.73 | 38.74 | Pass |

Rates are whole-wave totals over the stated request count. A wave may span multiple independent model instances; [measurements.json](../measurements.json) retains their contributions and the exact configuration IDs. Do not interpret a multi-instance total as one card's rate.

A dash in shared decode means no qualified synchronized interval is available. Whole-wave throughput includes prefill and queueing. A valid decode interval can survive inside an overall failed or partial check; the source-report outcome is preserved. No rows are averaged.

## Bounded Checks

| Check | Reported outcome | Retained counts / flags |
| --- | --- | --- |
| check-31da1d1957571e955d98 | Pass | {"passed":true,"elapsed_seconds":176.74240852300136,"ttft_seconds":[152.45225720699818,155.62919465500454,155.62883413900272,156.57606427800056],"end_to_end_accepted_tok_s":5.793742478431463} |
| check-4997ba1e3b31aa7dcb6d | Pass | {"passed":true,"elapsed_seconds":176.74240852300136,"ttft_seconds":[152.45225720699818,155.62919465500454,155.62883413900272,156.57606427800056],"end_to_end_accepted_tok_s":5.793742478431463} |
| check-828482f97926421db60a | Pass | {"passed":true,"elapsed_seconds":44.64516924000054,"ttft_seconds":[38.736184433000744],"end_to_end_accepted_tok_s":5.73410302520777} |
| check-db7f62a969b84e4cb0fe | Pass | {"passed":true,"elapsed_seconds":44.64516924000054,"ttft_seconds":[38.736184433000744],"end_to_end_accepted_tok_s":5.73410302520777} |

These checks retain their reported scope. A context/allocation/retrieval check is not a general quality score or a speed qualification at that context. Exact flags and provenance are in [checks.json](../checks.json).

## Additional Test Results

| Result / Source | Profile | Evidence type | Reported outcome | Retained values | Configuration binding |
| --- | --- | --- | --- | --- | --- |
| [result-10a76e1ebc08ab2e8fae](../observations.json)<br>source-a09770d0f970110b9fab7baa.json<br>`/` | [ad002-glm-dflash23-small_exl3-layer_split-matched-077](ad002-glm-dflash23-small_exl3-layer_split-matched-077.md)<br>[record-26c850ec689cf58c6b67](record-26c850ec689cf58c6b67.md)<br>[glm-dflash23-small_exl3-layer_split](glm-dflash23-small_exl3-layer_split.md) | performance detail | Pass | elapsed_seconds=176.74 s; end_to_end_accepted_tok_s=5.79 accepted tokens/s; ttft_seconds=152.45<br>155.63<br>155.63<br>156.58 s; p50_ms=70.85 ms; p95_ms=240.61 ms; cold_prefill: per-request 214.11 to 218.34 tokens/s; Draft accepted / proposed: 660 / 1,092 tokens; fraction 0.6044 | Recorded configuration/job |
| [result-6d61daaa6635382dbcaa](../observations.json)<br>source-d98ca2f735aafa9e16da86bb.json<br>`/waves/0` | [ad002-glm-dflash23-small_exl3-layer_split-matched-077](ad002-glm-dflash23-small_exl3-layer_split-matched-077.md)<br>[record-26c850ec689cf58c6b67](record-26c850ec689cf58c6b67.md)<br>[glm-dflash23-small_exl3-layer_split](glm-dflash23-small_exl3-layer_split.md) | performance detail | Outcome unspecified | elapsed_seconds=44.65 s; end_to_end_accepted_tok_s=5.73 accepted tokens/s; output_tokens=256 tokens; ttft_seconds=38.74 s; p50_ms=19.03 ms; p95_ms=71.13 ms; prefill: per-request 848.42 tokens/s; Draft accepted / proposed: 168 / 264 tokens; fraction 0.6364 | Recorded configuration/job |
| [result-a8b866450c0f1db48dbf](../observations.json)<br>source-a09770d0f970110b9fab7baa.json<br>`/waves/0` | [ad002-glm-dflash23-small_exl3-layer_split-matched-077](ad002-glm-dflash23-small_exl3-layer_split-matched-077.md)<br>[record-26c850ec689cf58c6b67](record-26c850ec689cf58c6b67.md)<br>[glm-dflash23-small_exl3-layer_split](glm-dflash23-small_exl3-layer_split.md) | performance detail | Outcome unspecified | elapsed_seconds=176.74 s; end_to_end_accepted_tok_s=5.79 accepted tokens/s; output_tokens=256 tokens; ttft_seconds=152.45<br>155.63<br>155.63<br>156.58 s; p50_ms=62.67 ms; p95_ms=241.12 ms; prefill: per-request 214.11 to 218.34 tokens/s; Draft accepted / proposed: 665 / 1,077 tokens; fraction 0.6175 | Recorded configuration/job |
| [result-aa33f1754a83b4e70376](../observations.json)<br>source-d98ca2f735aafa9e16da86bb.json<br>`/waves/1` | [ad002-glm-dflash23-small_exl3-layer_split-matched-077](ad002-glm-dflash23-small_exl3-layer_split-matched-077.md)<br>[record-26c850ec689cf58c6b67](record-26c850ec689cf58c6b67.md)<br>[glm-dflash23-small_exl3-layer_split](glm-dflash23-small_exl3-layer_split.md) | performance detail | Outcome unspecified | elapsed_seconds=6.56 s; end_to_end_accepted_tok_s=39.00 accepted tokens/s; output_tokens=256 tokens; ttft_seconds=0.74 s; p50_ms=19.08 ms; p95_ms=70.88 ms; prefill: per-request 470.37 tokens/s; Draft accepted / proposed: 168 / 264 tokens; fraction 0.6364 | Recorded configuration/job |
| [result-b5d174b2b40f8851dbd6](../observations.json)<br>source-a09770d0f970110b9fab7baa.json<br>`/waves/1` | [ad002-glm-dflash23-small_exl3-layer_split-matched-077](ad002-glm-dflash23-small_exl3-layer_split-matched-077.md)<br>[record-26c850ec689cf58c6b67](record-26c850ec689cf58c6b67.md)<br>[glm-dflash23-small_exl3-layer_split](glm-dflash23-small_exl3-layer_split.md) | performance detail | Outcome unspecified | elapsed_seconds=23.42 s; end_to_end_accepted_tok_s=43.73 accepted tokens/s; output_tokens=256 tokens; ttft_seconds=0.88<br>2.80<br>2.80<br>2.80 s; p50_ms=70.85 ms; p95_ms=240.61 ms; prefill: per-request 286.52 to 566.67 tokens/s; Draft accepted / proposed: 660 / 1,092 tokens; fraction 0.6044 | Recorded configuration/job |
| [result-b5f26c724cb9dae95aab](../observations.json)<br>source-a9e622d351a86c8b776605d4.json<br>`/managed_phase_timings/77` | [ad002-glm-dflash23-small_exl3-layer_split-matched-077](ad002-glm-dflash23-small_exl3-layer_split-matched-077.md) | test outcome | Outcome unspecified | wall_seconds=564.52 s | Recorded configuration/job |
| [result-e697a45da562ca94ef11](../observations.json)<br>source-d98ca2f735aafa9e16da86bb.json<br>`/` | [ad002-glm-dflash23-small_exl3-layer_split-matched-077](ad002-glm-dflash23-small_exl3-layer_split-matched-077.md)<br>[record-26c850ec689cf58c6b67](record-26c850ec689cf58c6b67.md)<br>[glm-dflash23-small_exl3-layer_split](glm-dflash23-small_exl3-layer_split.md) | performance detail | Pass | elapsed_seconds=44.65 s; end_to_end_accepted_tok_s=5.73 accepted tokens/s; ttft_seconds=38.74 s; p50_ms=19.08 ms; p95_ms=70.88 ms; cold_prefill: per-request 848.42 tokens/s; Draft accepted / proposed: 168 / 264 tokens; fraction 0.6364 | Recorded configuration/job |

These are saved result records, including failures and bounded checks. Copies, individual requests, report summaries and regrading can overlap; their counts are not independent test repetitions. Open each result for exact values, units, configuration binding and source receipts.

There are 1 retained lifecycle records. Their states, exit codes and configuration IDs remain in [catalog.json](../catalog.json); they do not supply missing benchmark results.

[Full archive](../../README.md) | [All retained waves](../RESULTS.md) | [Data definitions](../DATA.md) | [Recommended recipes](../../../README.md)
