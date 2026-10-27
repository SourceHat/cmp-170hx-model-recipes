# ad005-apex_exl3-dflash23-small_exl3-layer_split-matched-088

**Historical record. Decode interval measured.**

Model family: Apex Flash 1 (GLM 5.3 Flash post-train).

Historical configurations are provided for comparison. The [recommended recipes](../../../README.md) include supported launch scripts.

Current recipes using the same recorded checkpoint repository: [apex-abliterated-exl3-mtp1-tp3](../../../recipes/apex-abliterated-exl3-mtp1-tp3/README.md). Context, cache and runtime versions can differ.

## Saved Configuration Versions

Each configuration ID identifies a distinct original settings record. Deployment fields are omitted; versions can have identical published settings after that omission. Upstream runtime commits remain unspecified where the source retained only an integration label.

| Configuration | Recorded artifact / source | Configured card counts | Context tokens | GPU pool tokens | Slots | Draft mode / tokens |
| --- | --- | --- | --- | --- | --- | --- |
| cfg-10924d1fa4359a11cbd6 | [SloptimistPrime/apex-flash-1-abliterated-EXL3-4bit-DGX-Spark@a4c922dc57](https://huggingface.co/SloptimistPrime/apex-flash-1-abliterated-EXL3-4bit-DGX-Spark/tree/a4c922dc57dae44a9569ec82a08a2f311636e2a6) | 3 | 262,144 | 262,144 | 4 | dflash2 / 3 |

Card counts are saved configuration choices, not a claim that every allowed placement was measured. A derived view can differ from its pinned download source.

<details>
<summary>cfg-10924d1fa4359a11cbd6</summary>

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
  "model_repository": "SloptimistPrime/apex-flash-1-abliterated-EXL3-4bit-DGX-Spark",
  "model_revision": "a4c922dc57dae44a9569ec82a08a2f311636e2a6",
  "draft_repository": null,
  "draft_revision": null,
  "recorded_runtime_label": null,
  "served_model_label": "apex-flash-1-abliterated-exl3-4bit-spark",
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
| [ad005-apex_exl3-dflash23-small_exl3-layer_split-matched-088](ad005-apex_exl3-dflash23-small_exl3-layer_split-matched-088.md)<br>wave-1e3fd31153e814e824df | layer_split; dflash2 / 3 | 1 | 32,766 | 256 (budget 256) | cold; reused 0 | 262,144 / 262,144 | 39.12 | Not recorded | 5.58 | 39.49 | Pass |
| [ad005-apex_exl3-dflash23-small_exl3-layer_split-matched-088](ad005-apex_exl3-dflash23-small_exl3-layer_split-matched-088.md)<br>wave-302fc39e957462c9c5ee | layer_split; dflash2 / 3 | 4 | 32,767 | 256 (budget 256) | cold; reused 0 | 262,144 / 262,144 | 44.52 | Not recorded | 5.68 | 158.09 | Pass |
| [ad005-apex_exl3-dflash23-small_exl3-layer_split-matched-088](ad005-apex_exl3-dflash23-small_exl3-layer_split-matched-088.md)<br>wave-3407bc14327aecb42428 | layer_split; dflash2 / 3 | 4 | 32,767 | 256 (budget 256) | cached_prefix; reused 32,512 | 262,144 / 262,144 | 43.38 | Not recorded | 39.19 | 2.71 | Pass |
| [ad005-apex_exl3-dflash23-small_exl3-layer_split-matched-088](ad005-apex_exl3-dflash23-small_exl3-layer_split-matched-088.md)<br>wave-645e2f594af36d4d9485 | layer_split; dflash2 / 3 | 1 | 32,766 | 256 (budget 256) | cached_prefix; reused 32,512 | 262,144 / 262,144 | 40.88 | Not recorded | 36.80 | 0.74 | Pass |

Rates are whole-wave totals over the stated request count. A wave may span multiple independent model instances; [measurements.json](../measurements.json) retains their contributions and the exact configuration IDs. Do not interpret a multi-instance total as one card's rate.

A dash in shared decode means no qualified synchronized interval is available. Whole-wave throughput includes prefill and queueing. A valid decode interval can survive inside an overall failed or partial check; the source-report outcome is preserved. No rows are averaged.

## Bounded Checks

| Check | Reported outcome | Retained counts / flags |
| --- | --- | --- |
| check-b052332abb4e787717f8 | Pass | {"passed":true,"elapsed_seconds":45.8954076250011,"ttft_seconds":[39.48740843500127],"end_to_end_accepted_tok_s":5.577900126559642} |
| check-b48692dc985e4a95e33e | Pass | {"passed":true,"elapsed_seconds":180.34813950100215,"ttft_seconds":[156.77827564199833,158.08906008500344,158.0888158969974,158.0884162420043],"end_to_end_accepted_tok_s":5.677907201223498} |
| check-c3a21376bc18e82e60e5 | Pass | {"passed":true,"elapsed_seconds":45.8954076250011,"ttft_seconds":[39.48740843500127],"end_to_end_accepted_tok_s":5.577900126559642} |
| check-c8c7b2c9054fdcd9b50d | Pass | {"passed":true,"elapsed_seconds":180.34813950100215,"ttft_seconds":[156.77827564199833,158.08906008500344,158.0888158969974,158.0884162420043],"end_to_end_accepted_tok_s":5.677907201223498} |

These checks retain their reported scope. A context/allocation/retrieval check is not a general quality score or a speed qualification at that context. Exact flags and provenance are in [checks.json](../checks.json).

## Additional Test Results

| Result / Source | Profile | Evidence type | Reported outcome | Retained values | Configuration binding |
| --- | --- | --- | --- | --- | --- |
| [result-5f76aaec3a1ddffbb74d](../observations.json)<br>source-123c4cb2d7eb2cba61b9dfea.json<br>`/` | [ad005-apex_exl3-dflash23-small_exl3-layer_split-matched-088](ad005-apex_exl3-dflash23-small_exl3-layer_split-matched-088.md)<br>[record-26c850ec689cf58c6b67](record-26c850ec689cf58c6b67.md)<br>[apex_exl3-dflash23-small_exl3-layer_split](apex_exl3-dflash23-small_exl3-layer_split.md) | performance detail | Pass | elapsed_seconds=180.35 s; end_to_end_accepted_tok_s=5.68 accepted tokens/s; ttft_seconds=156.78<br>158.09<br>158.09<br>158.09 s; p50_ms=82.59 ms; p95_ms=243.74 ms; cold_prefill: per-request 212.58 to 215.50 tokens/s; Draft accepted / proposed: 625 / 1,197 tokens; fraction 0.5221 | Recorded configuration/job |
| [result-794a1a9ad825dc9a857c](../observations.json)<br>source-123c4cb2d7eb2cba61b9dfea.json<br>`/waves/0` | [ad005-apex_exl3-dflash23-small_exl3-layer_split-matched-088](ad005-apex_exl3-dflash23-small_exl3-layer_split-matched-088.md)<br>[record-26c850ec689cf58c6b67](record-26c850ec689cf58c6b67.md)<br>[apex_exl3-dflash23-small_exl3-layer_split](apex_exl3-dflash23-small_exl3-layer_split.md) | performance detail | Outcome unspecified | elapsed_seconds=180.35 s; end_to_end_accepted_tok_s=5.68 accepted tokens/s; output_tokens=256 tokens; ttft_seconds=156.78<br>158.09<br>158.09<br>158.09 s; p50_ms=81.22 ms; p95_ms=242.49 ms; prefill: per-request 212.58 to 215.50 tokens/s; Draft accepted / proposed: 633 / 1,173 tokens; fraction 0.5396 | Recorded configuration/job |
| [result-7ab6214feb241c7c9c03](../observations.json)<br>source-a9e622d351a86c8b776605d4.json<br>`/managed_phase_timings/88` | [ad005-apex_exl3-dflash23-small_exl3-layer_split-matched-088](ad005-apex_exl3-dflash23-small_exl3-layer_split-matched-088.md) | test outcome | Outcome unspecified | wall_seconds=592.63 s | Recorded configuration/job |
| [result-7c14cbd0a7ca567f6183](../observations.json)<br>source-c6b570fd3a37bce6e185a72e.json<br>`/waves/1` | [ad005-apex_exl3-dflash23-small_exl3-layer_split-matched-088](ad005-apex_exl3-dflash23-small_exl3-layer_split-matched-088.md)<br>[record-26c850ec689cf58c6b67](record-26c850ec689cf58c6b67.md)<br>[apex_exl3-dflash23-small_exl3-layer_split](apex_exl3-dflash23-small_exl3-layer_split.md) | performance detail | Outcome unspecified | elapsed_seconds=6.96 s; end_to_end_accepted_tok_s=36.80 accepted tokens/s; output_tokens=256 tokens; ttft_seconds=0.74 s; p50_ms=20.76 ms; p95_ms=74.31 ms; prefill: per-request 470.37 tokens/s; Draft accepted / proposed: 167 / 267 tokens; fraction 0.6255 | Recorded configuration/job |
| [result-821147854df8d7f07550](../observations.json)<br>source-c6b570fd3a37bce6e185a72e.json<br>`/` | [ad005-apex_exl3-dflash23-small_exl3-layer_split-matched-088](ad005-apex_exl3-dflash23-small_exl3-layer_split-matched-088.md)<br>[record-26c850ec689cf58c6b67](record-26c850ec689cf58c6b67.md)<br>[apex_exl3-dflash23-small_exl3-layer_split](apex_exl3-dflash23-small_exl3-layer_split.md) | performance detail | Pass | elapsed_seconds=45.90 s; end_to_end_accepted_tok_s=5.58 accepted tokens/s; ttft_seconds=39.49 s; p50_ms=20.76 ms; p95_ms=74.31 ms; cold_prefill: per-request 833.95 tokens/s; Draft accepted / proposed: 167 / 267 tokens; fraction 0.6255 | Recorded configuration/job |
| [result-ac183bd92f6ccf1cceb6](../observations.json)<br>source-123c4cb2d7eb2cba61b9dfea.json<br>`/waves/1` | [ad005-apex_exl3-dflash23-small_exl3-layer_split-matched-088](ad005-apex_exl3-dflash23-small_exl3-layer_split-matched-088.md)<br>[record-26c850ec689cf58c6b67](record-26c850ec689cf58c6b67.md)<br>[apex_exl3-dflash23-small_exl3-layer_split](apex_exl3-dflash23-small_exl3-layer_split.md) | performance detail | Outcome unspecified | elapsed_seconds=26.13 s; end_to_end_accepted_tok_s=39.19 accepted tokens/s; output_tokens=256 tokens; ttft_seconds=0.96<br>2.71<br>2.71<br>2.71 s; p50_ms=82.59 ms; p95_ms=243.74 ms; prefill: per-request 193.18 to 593.02 tokens/s; Draft accepted / proposed: 625 / 1,197 tokens; fraction 0.5221 | Recorded configuration/job |
| [result-b2e7c3b5d80bd54f2b90](../observations.json)<br>source-c6b570fd3a37bce6e185a72e.json<br>`/waves/0` | [ad005-apex_exl3-dflash23-small_exl3-layer_split-matched-088](ad005-apex_exl3-dflash23-small_exl3-layer_split-matched-088.md)<br>[record-26c850ec689cf58c6b67](record-26c850ec689cf58c6b67.md)<br>[apex_exl3-dflash23-small_exl3-layer_split](apex_exl3-dflash23-small_exl3-layer_split.md) | performance detail | Outcome unspecified | elapsed_seconds=45.90 s; end_to_end_accepted_tok_s=5.58 accepted tokens/s; output_tokens=256 tokens; ttft_seconds=39.49 s; p50_ms=23.95 ms; p95_ms=66.51 ms; prefill: per-request 833.95 tokens/s; Draft accepted / proposed: 165 / 273 tokens; fraction 0.6044 | Recorded configuration/job |

These are saved result records, including failures and bounded checks. Copies, individual requests, report summaries and regrading can overlap; their counts are not independent test repetitions. Open each result for exact values, units, configuration binding and source receipts.

There are 1 retained lifecycle records. Their states, exit codes and configuration IDs remain in [catalog.json](../catalog.json); they do not supply missing benchmark results.

[Full archive](../../README.md) | [All retained waves](../RESULTS.md) | [Data definitions](../DATA.md) | [Recommended recipes](../../../README.md)
