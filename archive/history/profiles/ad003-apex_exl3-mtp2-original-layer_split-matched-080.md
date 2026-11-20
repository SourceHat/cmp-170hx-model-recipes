# ad003-apex_exl3-mtp2-original-layer_split-matched-080

**Historical record. Decode interval measured.**

Model family: Apex Flash 1 (GLM 5.3 Flash post-train).

Historical configurations are provided for comparison. The [recommended recipes](../../../README.md) include supported launch scripts.

Current recipes using the same recorded checkpoint repository: [apex-abliterated-exl3-mtp1-tp3](../../../recipes/apex-abliterated-exl3-mtp1-tp3/README.md). Context, cache and runtime versions can differ.

## Saved Configuration Versions

Each configuration ID identifies a distinct original settings record. Deployment fields are omitted; versions can have identical published settings after that omission. Upstream runtime commits remain unspecified where the source retained only an integration label.

| Configuration | Recorded artifact / source | Configured card counts | Context tokens | GPU pool tokens | Slots | Draft mode / tokens |
| --- | --- | --- | --- | --- | --- | --- |
| cfg-9b86da9a5d24364425b5 | [SloptimistPrime/apex-flash-1-abliterated-EXL3-4bit-DGX-Spark@a4c922dc57](https://huggingface.co/SloptimistPrime/apex-flash-1-abliterated-EXL3-4bit-DGX-Spark/tree/a4c922dc57dae44a9569ec82a08a2f311636e2a6) | 3 | 262,144 | 262,144 | 4 | mtp / 2 |

Card counts are saved configuration choices, not a claim that every allowed placement was measured. A derived view can differ from its pinned download source.

<details>
<summary>cfg-9b86da9a5d24364425b5</summary>

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
| [ad003-apex_exl3-mtp2-original-layer_split-matched-080](ad003-apex_exl3-mtp2-original-layer_split-matched-080.md)<br>wave-30b8bc592d3d303acc64 | layer_split; mtp / 2 | 4 | 32,767 | 256 (budget 256) | cold; reused 0 | 262,144 / 262,144 | 49.74 | Not recorded | 5.71 | 159.39 | Pass |
| [ad003-apex_exl3-mtp2-original-layer_split-matched-080](ad003-apex_exl3-mtp2-original-layer_split-matched-080.md)<br>wave-5ebe67f00edd6b45eba2 | layer_split; mtp / 2 | 4 | 32,767 | 256 (budget 256) | cached_prefix; reused 32,512 | 262,144 / 262,144 | 46.33 | Not recorded | 42.00 | 2.91 | Pass |
| [ad003-apex_exl3-mtp2-original-layer_split-matched-080](ad003-apex_exl3-mtp2-original-layer_split-matched-080.md)<br>wave-6cf9422487ba29f9e19e | layer_split; mtp / 2 | 1 | 32,766 | 256 (budget 256) | cached_prefix; reused 32,512 | 262,144 / 262,144 | 37.90 | Not recorded | 34.64 | 0.74 | Pass |
| [ad003-apex_exl3-mtp2-original-layer_split-matched-080](ad003-apex_exl3-mtp2-original-layer_split-matched-080.md)<br>wave-af72af09e731dae0acba | layer_split; mtp / 2 | 1 | 32,766 | 256 (budget 256) | cold; reused 0 | 262,144 / 262,144 | 37.37 | Not recorded | 5.51 | 39.68 | Pass |

Rates are whole-wave totals over the stated request count. A wave may span multiple independent model instances; [measurements.json](../measurements.json) retains their contributions and the exact configuration IDs. Do not interpret a multi-instance total as one card's rate.

A dash in shared decode means no qualified synchronized interval is available. Whole-wave throughput includes prefill and queueing. A valid decode interval can survive inside an overall failed or partial check; the source-report outcome is preserved. No rows are averaged.

## Bounded Checks

| Check | Reported outcome | Retained counts / flags |
| --- | --- | --- |
| check-72404a2981cbcd2938c3 | Pass | {"passed":true,"elapsed_seconds":179.37791153599392,"ttft_seconds":[154.8519917589947,159.39114067000628,159.39108778800437,159.39071222700295],"end_to_end_accepted_tok_s":5.708618141618426} |
| check-74f37dd754b91b251538 | Pass | {"passed":true,"elapsed_seconds":179.37791153599392,"ttft_seconds":[154.8519917589947,159.39114067000628,159.39108778800437,159.39071222700295],"end_to_end_accepted_tok_s":5.708618141618426} |
| check-f50cd29683e4f008575d | Pass | {"passed":true,"elapsed_seconds":46.41952242199477,"ttft_seconds":[39.67511041100079],"end_to_end_accepted_tok_s":5.5149210212188775} |
| check-fed3dcfa5dbbf823f702 | Pass | {"passed":true,"elapsed_seconds":46.41952242199477,"ttft_seconds":[39.67511041100079],"end_to_end_accepted_tok_s":5.5149210212188775} |

These checks retain their reported scope. A context/allocation/retrieval check is not a general quality score or a speed qualification at that context. Exact flags and provenance are in [checks.json](../checks.json).

## Additional Test Results

| Result / Source | Profile | Evidence type | Reported outcome | Retained values | Configuration binding |
| --- | --- | --- | --- | --- | --- |
| [result-021834efbf2f52ad2772](../observations.json)<br>source-ef5a82ae57e8ddbda9ff8de0.json<br>`/` | [ad003-apex_exl3-mtp2-original-layer_split-matched-080](ad003-apex_exl3-mtp2-original-layer_split-matched-080.md)<br>[record-26c850ec689cf58c6b67](record-26c850ec689cf58c6b67.md)<br>[apex_exl3-mtp2-original-layer_split](apex_exl3-mtp2-original-layer_split.md) | performance detail | Pass | elapsed_seconds=179.38 s; end_to_end_accepted_tok_s=5.71 accepted tokens/s; ttft_seconds=154.85<br>159.39<br>159.39<br>159.39 s; p50_ms=72.36 ms; p95_ms=211.55 ms; cold_prefill: per-request 210.90 to 213.93 tokens/s; Draft accepted / proposed: 579 / 890 tokens; fraction 0.6506 | Recorded configuration/job |
| [result-077823b8eee6b38c6f7a](../observations.json)<br>source-55bd385004456a77d4fdebf6.json<br>`/` | [ad003-apex_exl3-mtp2-original-layer_split-matched-080](ad003-apex_exl3-mtp2-original-layer_split-matched-080.md)<br>[record-26c850ec689cf58c6b67](record-26c850ec689cf58c6b67.md)<br>[apex_exl3-mtp2-original-layer_split](apex_exl3-mtp2-original-layer_split.md) | performance detail | Pass | elapsed_seconds=46.42 s; end_to_end_accepted_tok_s=5.51 accepted tokens/s; ttft_seconds=39.68 s; p50_ms=22.51 ms; p95_ms=63.75 ms; cold_prefill: per-request 828.47 tokens/s; Draft accepted / proposed: 147 / 218 tokens; fraction 0.6743 | Recorded configuration/job |
| [result-1ebf273c90f12e38353c](../observations.json)<br>source-ef5a82ae57e8ddbda9ff8de0.json<br>`/waves/1` | [ad003-apex_exl3-mtp2-original-layer_split-matched-080](ad003-apex_exl3-mtp2-original-layer_split-matched-080.md)<br>[record-26c850ec689cf58c6b67](record-26c850ec689cf58c6b67.md)<br>[apex_exl3-mtp2-original-layer_split](apex_exl3-mtp2-original-layer_split.md) | performance detail | Outcome unspecified | elapsed_seconds=24.38 s; end_to_end_accepted_tok_s=42.00 accepted tokens/s; output_tokens=256 tokens; ttft_seconds=0.95<br>2.84<br>2.99<br>2.99 s; p50_ms=72.36 ms; p95_ms=211.55 ms; prefill: per-request 286.52 to 579.55 tokens/s; Draft accepted / proposed: 579 / 890 tokens; fraction 0.6506 | Recorded configuration/job |
| [result-5c68afda768e721eda53](../observations.json)<br>source-ef5a82ae57e8ddbda9ff8de0.json<br>`/waves/0` | [ad003-apex_exl3-mtp2-original-layer_split-matched-080](ad003-apex_exl3-mtp2-original-layer_split-matched-080.md)<br>[record-26c850ec689cf58c6b67](record-26c850ec689cf58c6b67.md)<br>[apex_exl3-mtp2-original-layer_split](apex_exl3-mtp2-original-layer_split.md) | performance detail | Outcome unspecified | elapsed_seconds=179.38 s; end_to_end_accepted_tok_s=5.71 accepted tokens/s; output_tokens=256 tokens; ttft_seconds=154.85<br>159.39<br>159.39<br>159.39 s; p50_ms=71.72 ms; p95_ms=209.38 ms; prefill: per-request 210.90 to 213.93 tokens/s; Draft accepted / proposed: 599 / 850 tokens; fraction 0.7047 | Recorded configuration/job |
| [result-7a7d8fd75f9fa8caeb72](../observations.json)<br>source-a9e622d351a86c8b776605d4.json<br>`/managed_phase_timings/80` | [ad003-apex_exl3-mtp2-original-layer_split-matched-080](ad003-apex_exl3-mtp2-original-layer_split-matched-080.md) | test outcome | Outcome unspecified | wall_seconds=598.09 s | Recorded configuration/job |
| [result-7c07eae8e17befd955c8](../observations.json)<br>source-55bd385004456a77d4fdebf6.json<br>`/waves/0` | [ad003-apex_exl3-mtp2-original-layer_split-matched-080](ad003-apex_exl3-mtp2-original-layer_split-matched-080.md)<br>[record-26c850ec689cf58c6b67](record-26c850ec689cf58c6b67.md)<br>[apex_exl3-mtp2-original-layer_split](apex_exl3-mtp2-original-layer_split.md) | performance detail | Outcome unspecified | elapsed_seconds=46.42 s; end_to_end_accepted_tok_s=5.51 accepted tokens/s; output_tokens=256 tokens; ttft_seconds=39.68 s; p50_ms=22.50 ms; p95_ms=62.76 ms; prefill: per-request 828.47 tokens/s; Draft accepted / proposed: 147 / 218 tokens; fraction 0.6743 | Recorded configuration/job |
| [result-de991ad3668b9fb1f489](../observations.json)<br>source-55bd385004456a77d4fdebf6.json<br>`/waves/1` | [ad003-apex_exl3-mtp2-original-layer_split-matched-080](ad003-apex_exl3-mtp2-original-layer_split-matched-080.md)<br>[record-26c850ec689cf58c6b67](record-26c850ec689cf58c6b67.md)<br>[apex_exl3-mtp2-original-layer_split](apex_exl3-mtp2-original-layer_split.md) | performance detail | Outcome unspecified | elapsed_seconds=7.39 s; end_to_end_accepted_tok_s=34.64 accepted tokens/s; output_tokens=256 tokens; ttft_seconds=0.74 s; p50_ms=22.51 ms; p95_ms=63.75 ms; prefill: per-request 470.37 tokens/s; Draft accepted / proposed: 147 / 218 tokens; fraction 0.6743 | Recorded configuration/job |

These are saved result records, including failures and bounded checks. Copies, individual requests, report summaries and regrading can overlap; their counts are not independent test repetitions. Open each result for exact values, units, configuration binding and source receipts.

There are 1 retained lifecycle records. Their states, exit codes and configuration IDs remain in [catalog.json](../catalog.json); they do not supply missing benchmark results.

[Full archive](../../README.md) | [All retained waves](../RESULTS.md) | [Data definitions](../DATA.md) | [Recommended recipes](../../../README.md)
