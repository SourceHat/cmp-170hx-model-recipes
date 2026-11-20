# ad003-apex_exl3-mtp1-original-layer_split-matched-079

**Historical record. Decode interval measured.**

Model family: Apex Flash 1 (GLM 5.3 Flash post-train).

Historical configurations are provided for comparison. The [recommended recipes](../../../README.md) include supported launch scripts.

Current recipes using the same recorded checkpoint repository: [apex-abliterated-exl3-mtp1-tp3](../../../recipes/apex-abliterated-exl3-mtp1-tp3/README.md). Context, cache and runtime versions can differ.

## Saved Configuration Versions

Each configuration ID identifies a distinct original settings record. Deployment fields are omitted; versions can have identical published settings after that omission. Upstream runtime commits remain unspecified where the source retained only an integration label.

| Configuration | Recorded artifact / source | Configured card counts | Context tokens | GPU pool tokens | Slots | Draft mode / tokens |
| --- | --- | --- | --- | --- | --- | --- |
| cfg-576716c2e319ddba6cb4 | [SloptimistPrime/apex-flash-1-abliterated-EXL3-4bit-DGX-Spark@a4c922dc57](https://huggingface.co/SloptimistPrime/apex-flash-1-abliterated-EXL3-4bit-DGX-Spark/tree/a4c922dc57dae44a9569ec82a08a2f311636e2a6) | 3 | 262,144 | 262,144 | 4 | mtp / 1 |

Card counts are saved configuration choices, not a claim that every allowed placement was measured. A derived view can differ from its pinned download source.

<details>
<summary>cfg-576716c2e319ddba6cb4</summary>

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
  "model_repository": "SloptimistPrime/apex-flash-1-abliterated-EXL3-4bit-DGX-Spark",
  "model_revision": "a4c922dc57dae44a9569ec82a08a2f311636e2a6",
  "draft_repository": null,
  "draft_revision": null,
  "recorded_runtime_label": null,
  "served_model_label": "apex-flash-1-abliterated-exl3-4bit-spark"
}
```

Pinned model revision recorded: yes. Source receipt labels, hashes and object locators are retained in [configurations.json](../configurations.json).

</details>

## Retained Measurements

| Profile / Wave | Layout; Draft / Tokens | Requests | Input tokens/request | Accepted output tokens/request | Cache / Reused input tokens | Context / GPU pool tokens | Shared decode tok/s total | Client after-first-token estimate tok/s | Whole-wave output tok/s | Median TTFT, s | Source report |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [ad003-apex_exl3-mtp1-original-layer_split-matched-079](ad003-apex_exl3-mtp1-original-layer_split-matched-079.md)<br>wave-440cccac193cfec30755 | layer_split; mtp / 1 | 4 | 32,767 | 256 (budget 256) | cached_prefix; reused 32,512 | 262,144 / 262,144 | 68.94 | Not recorded | 59.16 | 2.66 | Pass |
| [ad003-apex_exl3-mtp1-original-layer_split-matched-079](ad003-apex_exl3-mtp1-original-layer_split-matched-079.md)<br>wave-4b54f49a6139286b0306 | layer_split; mtp / 1 | 1 | 32,766 | 256 (budget 256) | cached_prefix; reused 32,512 | 262,144 / 262,144 | 35.90 | Not recorded | 32.86 | 0.74 | Pass |
| [ad003-apex_exl3-mtp1-original-layer_split-matched-079](ad003-apex_exl3-mtp1-original-layer_split-matched-079.md)<br>wave-525093fdf02ce6185ae6 | layer_split; mtp / 1 | 4 | 32,767 | 256 (budget 256) | cold; reused 0 | 262,144 / 262,144 | 65.57 | Not recorded | 5.87 | 158.87 | Pass |
| [ad003-apex_exl3-mtp1-original-layer_split-matched-079](ad003-apex_exl3-mtp1-original-layer_split-matched-079.md)<br>wave-c3da4b841e86dd0dcf2d | layer_split; mtp / 1 | 1 | 32,766 | 256 (budget 256) | cold; reused 0 | 262,144 / 262,144 | 34.32 | Not recorded | 5.45 | 39.65 | Pass |

Rates are whole-wave totals over the stated request count. A wave may span multiple independent model instances; [measurements.json](../measurements.json) retains their contributions and the exact configuration IDs. Do not interpret a multi-instance total as one card's rate.

A dash in shared decode means no qualified synchronized interval is available. Whole-wave throughput includes prefill and queueing. A valid decode interval can survive inside an overall failed or partial check; the source-report outcome is preserved. No rows are averaged.

## Bounded Checks

| Check | Reported outcome | Retained counts / flags |
| --- | --- | --- |
| check-07056eb7ad7c845ebf31 | Pass | {"passed":true,"elapsed_seconds":46.99082195200026,"ttft_seconds":[39.64696770699811],"end_to_end_accepted_tok_s":5.4478723581702075} |
| check-1ae411c338ffbaa66dc8 | Pass | {"passed":true,"elapsed_seconds":174.34234568199463,"ttft_seconds":[157.2183255639975,158.87830880900583,158.87772848599707,158.8710017179983],"end_to_end_accepted_tok_s":5.873501334367756} |
| check-4645d731b86ffa2a5c2a | Pass | {"passed":true,"elapsed_seconds":174.34234568199463,"ttft_seconds":[157.2183255639975,158.87830880900583,158.87772848599707,158.8710017179983],"end_to_end_accepted_tok_s":5.873501334367756} |
| check-d498a28871573cd0b744 | Pass | {"passed":true,"elapsed_seconds":46.99082195200026,"ttft_seconds":[39.64696770699811],"end_to_end_accepted_tok_s":5.4478723581702075} |

These checks retain their reported scope. A context/allocation/retrieval check is not a general quality score or a speed qualification at that context. Exact flags and provenance are in [checks.json](../checks.json).

## Additional Test Results

| Result / Source | Profile | Evidence type | Reported outcome | Retained values | Configuration binding |
| --- | --- | --- | --- | --- | --- |
| [result-0724d5d67f5e6c198be4](../observations.json)<br>source-0cd54d2302a9e3c01ee96b52.json<br>`/waves/1` | [ad003-apex_exl3-mtp1-original-layer_split-matched-079](ad003-apex_exl3-mtp1-original-layer_split-matched-079.md)<br>[record-26c850ec689cf58c6b67](record-26c850ec689cf58c6b67.md)<br>[apex_exl3-mtp1-original-layer_split](apex_exl3-mtp1-original-layer_split.md) | performance detail | Outcome unspecified | elapsed_seconds=17.31 s; end_to_end_accepted_tok_s=59.16 accepted tokens/s; output_tokens=256 tokens; ttft_seconds=1.47<br>2.66<br>2.66<br>2.66 s; p50_ms=56.43 ms; p95_ms=112.41 ms; prefill: per-request 289.77 to 579.55 tokens/s; Draft accepted / proposed: 470 / 554 tokens; fraction 0.8484 | Recorded configuration/job |
| [result-2354d9470cdd39fd8eca](../observations.json)<br>source-0cd54d2302a9e3c01ee96b52.json<br>`/` | [ad003-apex_exl3-mtp1-original-layer_split-matched-079](ad003-apex_exl3-mtp1-original-layer_split-matched-079.md)<br>[record-26c850ec689cf58c6b67](record-26c850ec689cf58c6b67.md)<br>[apex_exl3-mtp1-original-layer_split](apex_exl3-mtp1-original-layer_split.md) | performance detail | Pass | elapsed_seconds=174.34 s; end_to_end_accepted_tok_s=5.87 accepted tokens/s; ttft_seconds=157.22<br>158.88<br>158.88<br>158.87 s; p50_ms=56.43 ms; p95_ms=112.41 ms; cold_prefill: per-request 210.03 to 212.22 tokens/s; Draft accepted / proposed: 470 / 554 tokens; fraction 0.8484 | Recorded configuration/job |
| [result-25a0c0cbd57667a5b1db](../observations.json)<br>source-0cd54d2302a9e3c01ee96b52.json<br>`/waves/0` | [ad003-apex_exl3-mtp1-original-layer_split-matched-079](ad003-apex_exl3-mtp1-original-layer_split-matched-079.md)<br>[record-26c850ec689cf58c6b67](record-26c850ec689cf58c6b67.md)<br>[apex_exl3-mtp1-original-layer_split](apex_exl3-mtp1-original-layer_split.md) | performance detail | Outcome unspecified | elapsed_seconds=174.34 s; end_to_end_accepted_tok_s=5.87 accepted tokens/s; output_tokens=256 tokens; ttft_seconds=157.22<br>158.88<br>158.88<br>158.87 s; p50_ms=56.14 ms; p95_ms=111.79 ms; prefill: per-request 210.03 to 212.22 tokens/s; Draft accepted / proposed: 458 / 566 tokens; fraction 0.8092 | Recorded configuration/job |
| [result-5600ff2e9ca64b86131b](../observations.json)<br>source-204490ae2f04feeb020ea675.json<br>`/waves/1` | [ad003-apex_exl3-mtp1-original-layer_split-matched-079](ad003-apex_exl3-mtp1-original-layer_split-matched-079.md)<br>[record-26c850ec689cf58c6b67](record-26c850ec689cf58c6b67.md)<br>[apex_exl3-mtp1-original-layer_split](apex_exl3-mtp1-original-layer_split.md) | performance detail | Outcome unspecified | elapsed_seconds=7.79 s; end_to_end_accepted_tok_s=32.86 accepted tokens/s; output_tokens=256 tokens; ttft_seconds=0.74 s; p50_ms=26.62 ms; p95_ms=51.87 ms; prefill: per-request 461.82 tokens/s; Draft accepted / proposed: 117 / 139 tokens; fraction 0.8417 | Recorded configuration/job |
| [result-735c892513a7eead27b6](../observations.json)<br>source-204490ae2f04feeb020ea675.json<br>`/waves/0` | [ad003-apex_exl3-mtp1-original-layer_split-matched-079](ad003-apex_exl3-mtp1-original-layer_split-matched-079.md)<br>[record-26c850ec689cf58c6b67](record-26c850ec689cf58c6b67.md)<br>[apex_exl3-mtp1-original-layer_split](apex_exl3-mtp1-original-layer_split.md) | performance detail | Outcome unspecified | elapsed_seconds=46.99 s; end_to_end_accepted_tok_s=5.45 accepted tokens/s; output_tokens=256 tokens; ttft_seconds=39.65 s; p50_ms=26.52 ms; p95_ms=52.61 ms; prefill: per-request 828.89 tokens/s; Draft accepted / proposed: 112 / 144 tokens; fraction 0.7778 | Recorded configuration/job |
| [result-dee1434d5eaffbd80d4a](../observations.json)<br>source-204490ae2f04feeb020ea675.json<br>`/` | [ad003-apex_exl3-mtp1-original-layer_split-matched-079](ad003-apex_exl3-mtp1-original-layer_split-matched-079.md)<br>[record-26c850ec689cf58c6b67](record-26c850ec689cf58c6b67.md)<br>[apex_exl3-mtp1-original-layer_split](apex_exl3-mtp1-original-layer_split.md) | performance detail | Pass | elapsed_seconds=46.99 s; end_to_end_accepted_tok_s=5.45 accepted tokens/s; ttft_seconds=39.65 s; p50_ms=26.62 ms; p95_ms=51.87 ms; cold_prefill: per-request 828.89 tokens/s; Draft accepted / proposed: 117 / 139 tokens; fraction 0.8417 | Recorded configuration/job |
| [result-dfc686252613a610ddab](../observations.json)<br>source-a9e622d351a86c8b776605d4.json<br>`/managed_phase_timings/79` | [ad003-apex_exl3-mtp1-original-layer_split-matched-079](ad003-apex_exl3-mtp1-original-layer_split-matched-079.md) | test outcome | Outcome unspecified | wall_seconds=586.54 s | Recorded configuration/job |

These are saved result records, including failures and bounded checks. Copies, individual requests, report summaries and regrading can overlap; their counts are not independent test repetitions. Open each result for exact values, units, configuration binding and source receipts.

There are 1 retained lifecycle records. Their states, exit codes and configuration IDs remain in [catalog.json](../catalog.json); they do not supply missing benchmark results.

[Full archive](../../README.md) | [All retained waves](../RESULTS.md) | [Data definitions](../DATA.md) | [Recommended recipes](../../../README.md)
