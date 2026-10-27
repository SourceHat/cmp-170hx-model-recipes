# ad002-glm-dflash22-original-layer_split-matched-073

**Historical record. Decode interval measured.**

Model family: GLM 5.3 Flash.

Historical configurations are provided for comparison. The [recommended recipes](../../../README.md) include supported launch scripts.

Current recipes using the same recorded checkpoint repository: [glm-5.3-flash-mtp1-tp3](../../../recipes/glm-5.3-flash-mtp1-tp3/README.md). Context, cache and runtime versions can differ.

## Saved Configuration Versions

Each configuration ID identifies a distinct original settings record. Deployment fields are omitted; versions can have identical published settings after that omission. Upstream runtime commits remain unspecified where the source retained only an integration label.

| Configuration | Recorded artifact / source | Configured card counts | Context tokens | GPU pool tokens | Slots | Draft mode / tokens |
| --- | --- | --- | --- | --- | --- | --- |
| cfg-626571b747f2654a29e1 | [turboderp/GLM-5.3-Flash-exl3@2a30229e67](https://huggingface.co/turboderp/GLM-5.3-Flash-exl3/tree/2a30229e67012798ba9f0cd832bb78abf4c363d5) | 3 | 262,144 | 262,144 | 4 | dflash2 / 2 |

Card counts are saved configuration choices, not a claim that every allowed placement was measured. A derived view can differ from its pinned download source.

<details>
<summary>cfg-626571b747f2654a29e1</summary>

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
  "draft_tokens": 2,
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
| [ad002-glm-dflash22-original-layer_split-matched-073](ad002-glm-dflash22-original-layer_split-matched-073.md)<br>wave-184e606ef70e99a0fd5a | layer_split; dflash2 / 2 | 4 | 32,767 | 256 (budget 256) | cached_prefix; reused 32,512 | 262,144 / 262,144 | 48.22 | Not recorded | 43.10 | 2.98 | Pass |
| [ad002-glm-dflash22-original-layer_split-matched-073](ad002-glm-dflash22-original-layer_split-matched-073.md)<br>wave-76ddc8d33651f86aa6e2 | layer_split; dflash2 / 2 | 1 | 32,766 | 256 (budget 256) | cold; reused 0 | 262,144 / 262,144 | 41.33 | Not recorded | 5.77 | 38.27 | Pass |
| [ad002-glm-dflash22-original-layer_split-matched-073](ad002-glm-dflash22-original-layer_split-matched-073.md)<br>wave-c3f8bd928cdafc8349cf | layer_split; dflash2 / 2 | 4 | 32,767 | 256 (budget 256) | cold; reused 0 | 262,144 / 262,144 | 46.08 | Not recorded | 5.82 | 153.69 | Pass |
| [ad002-glm-dflash22-original-layer_split-matched-073](ad002-glm-dflash22-original-layer_split-matched-073.md)<br>wave-fbf4e13244578596edcd | layer_split; dflash2 / 2 | 1 | 32,766 | 256 (budget 256) | cached_prefix; reused 32,512 | 262,144 / 262,144 | 41.01 | Not recorded | 36.93 | 0.80 | Pass |

Rates are whole-wave totals over the stated request count. A wave may span multiple independent model instances; [measurements.json](../measurements.json) retains their contributions and the exact configuration IDs. Do not interpret a multi-instance total as one card's rate.

A dash in shared decode means no qualified synchronized interval is available. Whole-wave throughput includes prefill and queueing. A valid decode interval can survive inside an overall failed or partial check; the source-report outcome is preserved. No rows are averaged.

## Bounded Checks

| Check | Reported outcome | Retained counts / flags |
| --- | --- | --- |
| check-1348df9b0d733b0a545e | Pass | {"passed":true,"elapsed_seconds":175.93077093800093,"ttft_seconds":[149.8159662420003,153.0531794280032,154.32865965599922,154.3281096540013],"end_to_end_accepted_tok_s":5.820471282768742} |
| check-34f3a88e0aa35aad57ad | Pass | {"passed":true,"elapsed_seconds":175.93077093800093,"ttft_seconds":[149.8159662420003,153.0531794280032,154.32865965599922,154.3281096540013],"end_to_end_accepted_tok_s":5.820471282768742} |
| check-89fb44d6c401aa842dfc | Pass | {"passed":true,"elapsed_seconds":44.36184433499875,"ttft_seconds":[38.266712099997676],"end_to_end_accepted_tok_s":5.7707249064492085} |
| check-e505f225691281f71438 | Pass | {"passed":true,"elapsed_seconds":44.36184433499875,"ttft_seconds":[38.266712099997676],"end_to_end_accepted_tok_s":5.7707249064492085} |

These checks retain their reported scope. A context/allocation/retrieval check is not a general quality score or a speed qualification at that context. Exact flags and provenance are in [checks.json](../checks.json).

## Additional Test Results

| Result / Source | Profile | Evidence type | Reported outcome | Retained values | Configuration binding |
| --- | --- | --- | --- | --- | --- |
| [result-0670a7dfb13c4d22009a](../observations.json)<br>source-51c3554007fbf46e729ed1b6.json<br>`/waves/1` | [ad002-glm-dflash22-original-layer_split-matched-073](ad002-glm-dflash22-original-layer_split-matched-073.md)<br>[record-26c850ec689cf58c6b67](record-26c850ec689cf58c6b67.md)<br>[glm-dflash22-original-layer_split](glm-dflash22-original-layer_split.md) | performance detail | Outcome unspecified | elapsed_seconds=6.93 s; end_to_end_accepted_tok_s=36.93 accepted tokens/s; output_tokens=256 tokens; ttft_seconds=0.80 s; p50_ms=21.91 ms; p95_ms=60.69 ms; prefill: per-request 470.37 tokens/s; Draft accepted / proposed: 154 / 204 tokens; fraction 0.7549 | Recorded configuration/job |
| [result-4990c07260fed3beadac](../observations.json)<br>source-f5afcb1beaffa9568e6e993e.json<br>`/waves/1` | [ad002-glm-dflash22-original-layer_split-matched-073](ad002-glm-dflash22-original-layer_split-matched-073.md)<br>[record-26c850ec689cf58c6b67](record-26c850ec689cf58c6b67.md)<br>[glm-dflash22-original-layer_split](glm-dflash22-original-layer_split.md) | performance detail | Outcome unspecified | elapsed_seconds=23.76 s; end_to_end_accepted_tok_s=43.10 accepted tokens/s; output_tokens=256 tokens; ttft_seconds=0.86<br>2.90<br>3.06<br>3.06 s; p50_ms=73.40 ms; p95_ms=215.70 ms; prefill: per-request 289.77 to 579.55 tokens/s; Draft accepted / proposed: 605 / 838 tokens; fraction 0.7220 | Recorded configuration/job |
| [result-5f04a88422e8afd3d1c8](../observations.json)<br>source-f5afcb1beaffa9568e6e993e.json<br>`/waves/0` | [ad002-glm-dflash22-original-layer_split-matched-073](ad002-glm-dflash22-original-layer_split-matched-073.md)<br>[record-26c850ec689cf58c6b67](record-26c850ec689cf58c6b67.md)<br>[glm-dflash22-original-layer_split](glm-dflash22-original-layer_split.md) | performance detail | Outcome unspecified | elapsed_seconds=175.93 s; end_to_end_accepted_tok_s=5.82 accepted tokens/s; output_tokens=256 tokens; ttft_seconds=149.82<br>153.05<br>154.33<br>154.33 s; p50_ms=74.59 ms; p95_ms=219.91 ms; prefill: per-request 218.58 to 221.53 tokens/s; Draft accepted / proposed: 593 / 862 tokens; fraction 0.6879 | Recorded configuration/job |
| [result-714d0ec195ad15d9c17d](../observations.json)<br>source-f5afcb1beaffa9568e6e993e.json<br>`/` | [ad002-glm-dflash22-original-layer_split-matched-073](ad002-glm-dflash22-original-layer_split-matched-073.md)<br>[record-26c850ec689cf58c6b67](record-26c850ec689cf58c6b67.md)<br>[glm-dflash22-original-layer_split](glm-dflash22-original-layer_split.md) | performance detail | Pass | elapsed_seconds=175.93 s; end_to_end_accepted_tok_s=5.82 accepted tokens/s; ttft_seconds=149.82<br>153.05<br>154.33<br>154.33 s; p50_ms=73.40 ms; p95_ms=215.70 ms; cold_prefill: per-request 218.58 to 221.53 tokens/s; Draft accepted / proposed: 605 / 838 tokens; fraction 0.7220 | Recorded configuration/job |
| [result-aa476f548771ed682393](../observations.json)<br>source-51c3554007fbf46e729ed1b6.json<br>`/` | [ad002-glm-dflash22-original-layer_split-matched-073](ad002-glm-dflash22-original-layer_split-matched-073.md)<br>[record-26c850ec689cf58c6b67](record-26c850ec689cf58c6b67.md)<br>[glm-dflash22-original-layer_split](glm-dflash22-original-layer_split.md) | performance detail | Pass | elapsed_seconds=44.36 s; end_to_end_accepted_tok_s=5.77 accepted tokens/s; ttft_seconds=38.27 s; p50_ms=21.91 ms; p95_ms=60.69 ms; cold_prefill: per-request 860.00 tokens/s; Draft accepted / proposed: 154 / 204 tokens; fraction 0.7549 | Recorded configuration/job |
| [result-d83539c3cadd1841df0d](../observations.json)<br>source-a9e622d351a86c8b776605d4.json<br>`/managed_phase_timings/73` | [ad002-glm-dflash22-original-layer_split-matched-073](ad002-glm-dflash22-original-layer_split-matched-073.md) | test outcome | Outcome unspecified | wall_seconds=579.52 s | Recorded configuration/job |
| [result-edb42b9cf2126d72df31](../observations.json)<br>source-51c3554007fbf46e729ed1b6.json<br>`/waves/0` | [ad002-glm-dflash22-original-layer_split-matched-073](ad002-glm-dflash22-original-layer_split-matched-073.md)<br>[record-26c850ec689cf58c6b67](record-26c850ec689cf58c6b67.md)<br>[glm-dflash22-original-layer_split](glm-dflash22-original-layer_split.md) | performance detail | Outcome unspecified | elapsed_seconds=44.36 s; end_to_end_accepted_tok_s=5.77 accepted tokens/s; output_tokens=256 tokens; ttft_seconds=38.27 s; p50_ms=21.40 ms; p95_ms=59.72 ms; prefill: per-request 860.00 tokens/s; Draft accepted / proposed: 155 / 202 tokens; fraction 0.7673 | Recorded configuration/job |

These are saved result records, including failures and bounded checks. Copies, individual requests, report summaries and regrading can overlap; their counts are not independent test repetitions. Open each result for exact values, units, configuration binding and source receipts.

There are 1 retained lifecycle records. Their states, exit codes and configuration IDs remain in [catalog.json](../catalog.json); they do not supply missing benchmark results.

[Full archive](../../README.md) | [All retained waves](../RESULTS.md) | [Data definitions](../DATA.md) | [Recommended recipes](../../../README.md)
