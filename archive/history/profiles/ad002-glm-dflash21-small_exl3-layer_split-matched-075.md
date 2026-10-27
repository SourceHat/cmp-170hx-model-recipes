# ad002-glm-dflash21-small_exl3-layer_split-matched-075

**Historical record. Decode interval measured.**

Model family: GLM 5.3 Flash.

Historical configurations are provided for comparison. The [recommended recipes](../../../README.md) include supported launch scripts.

Current recipes using the same recorded checkpoint repository: [glm-5.3-flash-mtp1-tp3](../../../recipes/glm-5.3-flash-mtp1-tp3/README.md). Context, cache and runtime versions can differ.

## Saved Configuration Versions

Each configuration ID identifies a distinct original settings record. Deployment fields are omitted; versions can have identical published settings after that omission. Upstream runtime commits remain unspecified where the source retained only an integration label.

| Configuration | Recorded artifact / source | Configured card counts | Context tokens | GPU pool tokens | Slots | Draft mode / tokens |
| --- | --- | --- | --- | --- | --- | --- |
| cfg-66267a562cb260b8d0ad | [turboderp/GLM-5.3-Flash-exl3@2a30229e67](https://huggingface.co/turboderp/GLM-5.3-Flash-exl3/tree/2a30229e67012798ba9f0cd832bb78abf4c363d5) | 3 | 262,144 | 262,144 | 4 | dflash2 / 1 |

Card counts are saved configuration choices, not a claim that every allowed placement was measured. A derived view can differ from its pinned download source.

<details>
<summary>cfg-66267a562cb260b8d0ad</summary>

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
    3584
  ]
}
```

Pinned model revision recorded: yes. Source receipt labels, hashes and object locators are retained in [configurations.json](../configurations.json).

</details>

## Retained Measurements

| Profile / Wave | Layout; Draft / Tokens | Requests | Input tokens/request | Accepted output tokens/request | Cache / Reused input tokens | Context / GPU pool tokens | Shared decode tok/s total | Client after-first-token estimate tok/s | Whole-wave output tok/s | Median TTFT, s | Source report |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [ad002-glm-dflash21-small_exl3-layer_split-matched-075](ad002-glm-dflash21-small_exl3-layer_split-matched-075.md)<br>wave-33b3338b13d2debdb016 | layer_split; dflash2 / 1 | 4 | 32,767 | 256 (budget 256) | cached_prefix; reused 32,512 | 262,144 / 262,144 | 61.14 | Not recorded | 53.05 | 2.83 | Pass |
| [ad002-glm-dflash21-small_exl3-layer_split-matched-075](ad002-glm-dflash21-small_exl3-layer_split-matched-075.md)<br>wave-7d9cc59dbf5bafcfd890 | layer_split; dflash2 / 1 | 1 | 32,766 | 256 (budget 256) | cached_prefix; reused 32,512 | 262,144 / 262,144 | 33.55 | Not recorded | 30.80 | 0.74 | Pass |
| [ad002-glm-dflash21-small_exl3-layer_split-matched-075](ad002-glm-dflash21-small_exl3-layer_split-matched-075.md)<br>wave-ed843d4460b3dc00b597 | layer_split; dflash2 / 1 | 1 | 32,766 | 256 (budget 256) | cold; reused 0 | 262,144 / 262,144 | 33.03 | Not recorded | 5.52 | 38.74 | Pass |
| [ad002-glm-dflash21-small_exl3-layer_split-matched-075](ad002-glm-dflash21-small_exl3-layer_split-matched-075.md)<br>wave-f3d3264c195617ebb73f | layer_split; dflash2 / 1 | 4 | 32,767 | 256 (budget 256) | cold; reused 0 | 262,144 / 262,144 | 60.33 | Not recorded | 5.93 | 155.45 | Pass |

Rates are whole-wave totals over the stated request count. A wave may span multiple independent model instances; [measurements.json](../measurements.json) retains their contributions and the exact configuration IDs. Do not interpret a multi-instance total as one card's rate.

A dash in shared decode means no qualified synchronized interval is available. Whole-wave throughput includes prefill and queueing. A valid decode interval can survive inside an overall failed or partial check; the source-report outcome is preserved. No rows are averaged.

## Bounded Checks

| Check | Reported outcome | Retained counts / flags |
| --- | --- | --- |
| check-3318a4c9f41b48a6858f | Pass | {"passed":true,"elapsed_seconds":46.38940439099679,"ttft_seconds":[38.74352070799796],"end_to_end_accepted_tok_s":5.51850154923921} |
| check-98991195709282b49dd4 | Pass | {"passed":true,"elapsed_seconds":46.38940439099679,"ttft_seconds":[38.74352070799796],"end_to_end_accepted_tok_s":5.51850154923921} |
| check-c9d23fedad9f9adc4595 | Pass | {"passed":true,"elapsed_seconds":172.80829716200242,"ttft_seconds":[152.30317034799373,155.45504852999875,155.45448418600427,156.0027912469959],"end_to_end_accepted_tok_s":5.925641400424378} |
| check-f71ebc9c4f548fc6f0e8 | Pass | {"passed":true,"elapsed_seconds":172.80829716200242,"ttft_seconds":[152.30317034799373,155.45504852999875,155.45448418600427,156.0027912469959],"end_to_end_accepted_tok_s":5.925641400424378} |

These checks retain their reported scope. A context/allocation/retrieval check is not a general quality score or a speed qualification at that context. Exact flags and provenance are in [checks.json](../checks.json).

## Additional Test Results

| Result / Source | Profile | Evidence type | Reported outcome | Retained values | Configuration binding |
| --- | --- | --- | --- | --- | --- |
| [result-12ff76f7be1c1cd3fd16](../observations.json)<br>source-54e03862fdcf41516c17bb9d.json<br>`/` | [ad002-glm-dflash21-small_exl3-layer_split-matched-075](ad002-glm-dflash21-small_exl3-layer_split-matched-075.md)<br>[record-26c850ec689cf58c6b67](record-26c850ec689cf58c6b67.md)<br>[glm-dflash21-small_exl3-layer_split](glm-dflash21-small_exl3-layer_split.md) | performance detail | Pass | elapsed_seconds=172.81 s; end_to_end_accepted_tok_s=5.93 accepted tokens/s; ttft_seconds=152.30<br>155.46<br>155.45<br>156.00 s; p50_ms=61.23 ms; p95_ms=122.31 ms; cold_prefill: per-request 215.29 to 219.59 tokens/s; Draft accepted / proposed: 460 / 564 tokens; fraction 0.8156 | Recorded configuration/job |
| [result-3fc17f695f7971f0b378](../observations.json)<br>source-50f2510b9539ea8e4ceb1eca.json<br>`/waves/1` | [ad002-glm-dflash21-small_exl3-layer_split-matched-075](ad002-glm-dflash21-small_exl3-layer_split-matched-075.md)<br>[record-26c850ec689cf58c6b67](record-26c850ec689cf58c6b67.md)<br>[glm-dflash21-small_exl3-layer_split](glm-dflash21-small_exl3-layer_split.md) | performance detail | Outcome unspecified | elapsed_seconds=8.31 s; end_to_end_accepted_tok_s=30.80 accepted tokens/s; output_tokens=256 tokens; ttft_seconds=0.74 s; p50_ms=28.17 ms; p95_ms=56.31 ms; prefill: per-request 461.82 tokens/s; Draft accepted / proposed: 113 / 143 tokens; fraction 0.7902 | Recorded configuration/job |
| [result-51fa527c48e3dbb16518](../observations.json)<br>source-a9e622d351a86c8b776605d4.json<br>`/managed_phase_timings/75` | [ad002-glm-dflash21-small_exl3-layer_split-matched-075](ad002-glm-dflash21-small_exl3-layer_split-matched-075.md) | test outcome | Outcome unspecified | wall_seconds=565.41 s | Recorded configuration/job |
| [result-8bf73cd0a25a21707394](../observations.json)<br>source-54e03862fdcf41516c17bb9d.json<br>`/waves/1` | [ad002-glm-dflash21-small_exl3-layer_split-matched-075](ad002-glm-dflash21-small_exl3-layer_split-matched-075.md)<br>[record-26c850ec689cf58c6b67](record-26c850ec689cf58c6b67.md)<br>[glm-dflash21-small_exl3-layer_split](glm-dflash21-small_exl3-layer_split.md) | performance detail | Outcome unspecified | elapsed_seconds=19.30 s; end_to_end_accepted_tok_s=53.05 accepted tokens/s; output_tokens=256 tokens; ttft_seconds=0.88<br>2.83<br>2.83<br>2.83 s; p50_ms=61.23 ms; p95_ms=122.31 ms; prefill: per-request 280.22 to 566.67 tokens/s; Draft accepted / proposed: 460 / 564 tokens; fraction 0.8156 | Recorded configuration/job |
| [result-93d1a1690eb727575c56](../observations.json)<br>source-50f2510b9539ea8e4ceb1eca.json<br>`/waves/0` | [ad002-glm-dflash21-small_exl3-layer_split-matched-075](ad002-glm-dflash21-small_exl3-layer_split-matched-075.md)<br>[record-26c850ec689cf58c6b67](record-26c850ec689cf58c6b67.md)<br>[glm-dflash21-small_exl3-layer_split](glm-dflash21-small_exl3-layer_split.md) | performance detail | Outcome unspecified | elapsed_seconds=46.39 s; end_to_end_accepted_tok_s=5.52 accepted tokens/s; output_tokens=256 tokens; ttft_seconds=38.74 s; p50_ms=28.22 ms; p95_ms=56.37 ms; prefill: per-request 849.30 tokens/s; Draft accepted / proposed: 113 / 143 tokens; fraction 0.7902 | Recorded configuration/job |
| [result-cba81d8842fb5869a3dd](../observations.json)<br>source-50f2510b9539ea8e4ceb1eca.json<br>`/` | [ad002-glm-dflash21-small_exl3-layer_split-matched-075](ad002-glm-dflash21-small_exl3-layer_split-matched-075.md)<br>[record-26c850ec689cf58c6b67](record-26c850ec689cf58c6b67.md)<br>[glm-dflash21-small_exl3-layer_split](glm-dflash21-small_exl3-layer_split.md) | performance detail | Pass | elapsed_seconds=46.39 s; end_to_end_accepted_tok_s=5.52 accepted tokens/s; ttft_seconds=38.74 s; p50_ms=28.17 ms; p95_ms=56.31 ms; cold_prefill: per-request 849.30 tokens/s; Draft accepted / proposed: 113 / 143 tokens; fraction 0.7902 | Recorded configuration/job |
| [result-f4b6b8a08f56a2106121](../observations.json)<br>source-54e03862fdcf41516c17bb9d.json<br>`/waves/0` | [ad002-glm-dflash21-small_exl3-layer_split-matched-075](ad002-glm-dflash21-small_exl3-layer_split-matched-075.md)<br>[record-26c850ec689cf58c6b67](record-26c850ec689cf58c6b67.md)<br>[glm-dflash21-small_exl3-layer_split](glm-dflash21-small_exl3-layer_split.md) | performance detail | Outcome unspecified | elapsed_seconds=172.81 s; end_to_end_accepted_tok_s=5.93 accepted tokens/s; output_tokens=256 tokens; ttft_seconds=152.30<br>155.46<br>155.45<br>156.00 s; p50_ms=61.49 ms; p95_ms=122.98 ms; prefill: per-request 215.29 to 219.59 tokens/s; Draft accepted / proposed: 464 / 560 tokens; fraction 0.8286 | Recorded configuration/job |

These are saved result records, including failures and bounded checks. Copies, individual requests, report summaries and regrading can overlap; their counts are not independent test repetitions. Open each result for exact values, units, configuration binding and source receipts.

There are 1 retained lifecycle records. Their states, exit codes and configuration IDs remain in [catalog.json](../catalog.json); they do not supply missing benchmark results.

[Full archive](../../README.md) | [All retained waves](../RESULTS.md) | [Data definitions](../DATA.md) | [Recommended recipes](../../../README.md)
