# ad002-glm-dflash23-original-layer_split-matched-074

**Historical record. Decode interval measured.**

Model family: GLM 5.3 Flash.

Historical configurations are provided for comparison. The [recommended recipes](../../../README.md) include supported launch scripts.

Current recipes using the same recorded checkpoint repository: [glm-5.3-flash-mtp1-tp3](../../../recipes/glm-5.3-flash-mtp1-tp3/README.md). Context, cache and runtime versions can differ.

## Saved Configuration Versions

Each configuration ID identifies a distinct original settings record. Deployment fields are omitted; versions can have identical published settings after that omission. Upstream runtime commits remain unspecified where the source retained only an integration label.

| Configuration | Recorded artifact / source | Configured card counts | Context tokens | GPU pool tokens | Slots | Draft mode / tokens |
| --- | --- | --- | --- | --- | --- | --- |
| cfg-49fef599d99a9167d885 | [turboderp/GLM-5.3-Flash-exl3@2a30229e67](https://huggingface.co/turboderp/GLM-5.3-Flash-exl3/tree/2a30229e67012798ba9f0cd832bb78abf4c363d5) | 3 | 262,144 | 262,144 | 4 | dflash2 / 3 |

Card counts are saved configuration choices, not a claim that every allowed placement was measured. A derived view can differ from its pinned download source.

<details>
<summary>cfg-49fef599d99a9167d885</summary>

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
| [ad002-glm-dflash23-original-layer_split-matched-074](ad002-glm-dflash23-original-layer_split-matched-074.md)<br>wave-17364ddd37d53c7ecfce | layer_split; dflash2 / 3 | 4 | 32,767 | 256 (budget 256) | cold; reused 0 | 262,144 / 262,144 | 52.49 | Not recorded | 5.87 | 155.25 | Pass |
| [ad002-glm-dflash23-original-layer_split-matched-074](ad002-glm-dflash23-original-layer_split-matched-074.md)<br>wave-4c672be09b8f9bef2893 | layer_split; dflash2 / 3 | 1 | 32,766 | 256 (budget 256) | cached_prefix; reused 32,512 | 262,144 / 262,144 | 44.64 | Not recorded | 40.38 | 0.78 | Pass |
| [ad002-glm-dflash23-original-layer_split-matched-074](ad002-glm-dflash23-original-layer_split-matched-074.md)<br>wave-b80857bc8f9cd8405ca7 | layer_split; dflash2 / 3 | 4 | 32,767 | 256 (budget 256) | cached_prefix; reused 32,512 | 262,144 / 262,144 | 52.52 | Not recorded | 46.83 | 2.88 | Pass |
| [ad002-glm-dflash23-original-layer_split-matched-074](ad002-glm-dflash23-original-layer_split-matched-074.md)<br>wave-db8c73dbcc90c184bd41 | layer_split; dflash2 / 3 | 1 | 32,766 | 256 (budget 256) | cold; reused 0 | 262,144 / 262,144 | 43.74 | Not recorded | 5.79 | 38.53 | Pass |

Rates are whole-wave totals over the stated request count. A wave may span multiple independent model instances; [measurements.json](../measurements.json) retains their contributions and the exact configuration IDs. Do not interpret a multi-instance total as one card's rate.

A dash in shared decode means no qualified synchronized interval is available. Whole-wave throughput includes prefill and queueing. A valid decode interval can survive inside an overall failed or partial check; the source-report outcome is preserved. No rows are averaged.

## Bounded Checks

| Check | Reported outcome | Retained counts / flags |
| --- | --- | --- |
| check-204593b908d98af8772c | Pass | {"passed":true,"elapsed_seconds":44.21604611300427,"ttft_seconds":[38.53429492899886],"end_to_end_accepted_tok_s":5.789753324974675} |
| check-358aaa943fa582cd268e | Pass | {"passed":true,"elapsed_seconds":174.36189108899998,"ttft_seconds":[150.79202502800035,155.12867432900384,155.37105367200274,155.37065519899625],"end_to_end_accepted_tok_s":5.872842933765367} |
| check-aaca8a6596333fd5afb3 | Pass | {"passed":true,"elapsed_seconds":44.21604611300427,"ttft_seconds":[38.53429492899886],"end_to_end_accepted_tok_s":5.789753324974675} |
| check-d3092a60c9f7e92099b1 | Pass | {"passed":true,"elapsed_seconds":174.36189108899998,"ttft_seconds":[150.79202502800035,155.12867432900384,155.37105367200274,155.37065519899625],"end_to_end_accepted_tok_s":5.872842933765367} |

These checks retain their reported scope. A context/allocation/retrieval check is not a general quality score or a speed qualification at that context. Exact flags and provenance are in [checks.json](../checks.json).

## Additional Test Results

| Result / Source | Profile | Evidence type | Reported outcome | Retained values | Configuration binding |
| --- | --- | --- | --- | --- | --- |
| [result-15eca53805e8f18fb1e2](../observations.json)<br>source-6d7fdf2040e6503ec9bf20b6.json<br>`/waves/1` | [ad002-glm-dflash23-original-layer_split-matched-074](ad002-glm-dflash23-original-layer_split-matched-074.md)<br>[record-26c850ec689cf58c6b67](record-26c850ec689cf58c6b67.md)<br>[glm-dflash23-original-layer_split](glm-dflash23-original-layer_split.md) | performance detail | Outcome unspecified | elapsed_seconds=6.34 s; end_to_end_accepted_tok_s=40.38 accepted tokens/s; output_tokens=256 tokens; ttft_seconds=0.78 s; p50_ms=18.71 ms; p95_ms=60.63 ms; prefill: per-request 488.46 tokens/s; Draft accepted / proposed: 172 / 252 tokens; fraction 0.6825 | Recorded configuration/job |
| [result-3a18c18b50ba57e1c9e3](../observations.json)<br>source-6d7fdf2040e6503ec9bf20b6.json<br>`/` | [ad002-glm-dflash23-original-layer_split-matched-074](ad002-glm-dflash23-original-layer_split-matched-074.md)<br>[record-26c850ec689cf58c6b67](record-26c850ec689cf58c6b67.md)<br>[glm-dflash23-original-layer_split](glm-dflash23-original-layer_split.md) | performance detail | Pass | elapsed_seconds=44.22 s; end_to_end_accepted_tok_s=5.79 accepted tokens/s; ttft_seconds=38.53 s; p50_ms=18.71 ms; p95_ms=60.63 ms; cold_prefill: per-request 854.39 tokens/s; Draft accepted / proposed: 172 / 252 tokens; fraction 0.6825 | Recorded configuration/job |
| [result-5d56d5009b44d752054a](../observations.json)<br>source-a9e622d351a86c8b776605d4.json<br>`/managed_phase_timings/74` | [ad002-glm-dflash23-original-layer_split-matched-074](ad002-glm-dflash23-original-layer_split-matched-074.md) | test outcome | Outcome unspecified | wall_seconds=568.01 s | Recorded configuration/job |
| [result-bb38b1810327b4c972cf](../observations.json)<br>source-eeac617896b9470753745609.json<br>`/` | [ad002-glm-dflash23-original-layer_split-matched-074](ad002-glm-dflash23-original-layer_split-matched-074.md)<br>[record-26c850ec689cf58c6b67](record-26c850ec689cf58c6b67.md)<br>[glm-dflash23-original-layer_split](glm-dflash23-original-layer_split.md) | performance detail | Pass | elapsed_seconds=174.36 s; end_to_end_accepted_tok_s=5.87 accepted tokens/s; ttft_seconds=150.79<br>155.13<br>155.37<br>155.37 s; p50_ms=61.78 ms; p95_ms=237.55 ms; cold_prefill: per-request 216.21 to 218.94 tokens/s; Draft accepted / proposed: 678 / 1,038 tokens; fraction 0.6532 | Recorded configuration/job |
| [result-c20684ed30fd8249ea1c](../observations.json)<br>source-eeac617896b9470753745609.json<br>`/waves/1` | [ad002-glm-dflash23-original-layer_split-matched-074](ad002-glm-dflash23-original-layer_split-matched-074.md)<br>[record-26c850ec689cf58c6b67](record-26c850ec689cf58c6b67.md)<br>[glm-dflash23-original-layer_split](glm-dflash23-original-layer_split.md) | performance detail | Outcome unspecified | elapsed_seconds=21.87 s; end_to_end_accepted_tok_s=46.83 accepted tokens/s; output_tokens=256 tokens; ttft_seconds=0.87<br>2.80<br>2.97<br>2.97 s; p50_ms=61.78 ms; p95_ms=237.55 ms; prefill: per-request 286.52 to 579.55 tokens/s; Draft accepted / proposed: 678 / 1,038 tokens; fraction 0.6532 | Recorded configuration/job |
| [result-c3f9280a2605cbb9aa2e](../observations.json)<br>source-eeac617896b9470753745609.json<br>`/waves/0` | [ad002-glm-dflash23-original-layer_split-matched-074](ad002-glm-dflash23-original-layer_split-matched-074.md)<br>[record-26c850ec689cf58c6b67](record-26c850ec689cf58c6b67.md)<br>[glm-dflash23-original-layer_split](glm-dflash23-original-layer_split.md) | performance detail | Outcome unspecified | elapsed_seconds=174.36 s; end_to_end_accepted_tok_s=5.87 accepted tokens/s; output_tokens=256 tokens; ttft_seconds=150.79<br>155.13<br>155.37<br>155.37 s; p50_ms=62.84 ms; p95_ms=234.00 ms; prefill: per-request 216.21 to 218.94 tokens/s; Draft accepted / proposed: 678 / 1,038 tokens; fraction 0.6532 | Recorded configuration/job |
| [result-e52fe2806f7e66b9588d](../observations.json)<br>source-6d7fdf2040e6503ec9bf20b6.json<br>`/waves/0` | [ad002-glm-dflash23-original-layer_split-matched-074](ad002-glm-dflash23-original-layer_split-matched-074.md)<br>[record-26c850ec689cf58c6b67](record-26c850ec689cf58c6b67.md)<br>[glm-dflash23-original-layer_split](glm-dflash23-original-layer_split.md) | performance detail | Outcome unspecified | elapsed_seconds=44.22 s; end_to_end_accepted_tok_s=5.79 accepted tokens/s; output_tokens=256 tokens; ttft_seconds=38.53 s; p50_ms=19.06 ms; p95_ms=65.30 ms; prefill: per-request 854.39 tokens/s; Draft accepted / proposed: 172 / 252 tokens; fraction 0.6825 | Recorded configuration/job |

These are saved result records, including failures and bounded checks. Copies, individual requests, report summaries and regrading can overlap; their counts are not independent test repetitions. Open each result for exact values, units, configuration binding and source receipts.

There are 1 retained lifecycle records. Their states, exit codes and configuration IDs remain in [catalog.json](../catalog.json); they do not supply missing benchmark results.

[Full archive](../../README.md) | [All retained waves](../RESULTS.md) | [Data definitions](../DATA.md) | [Recommended recipes](../../../README.md)
