# ad003-apex_exl3-mtp3-original-layer_split-matched-081

**Historical record. Decode interval measured.**

Model family: Apex Flash 1 (GLM 5.3 Flash post-train).

Historical configurations are provided for comparison. The [recommended recipes](../../../README.md) include supported launch scripts.

Current recipes using the same recorded checkpoint repository: [apex-abliterated-exl3-mtp1-tp3](../../../recipes/apex-abliterated-exl3-mtp1-tp3/README.md). Context, cache and runtime versions can differ.

## Saved Configuration Versions

Each configuration ID identifies a distinct original settings record. Deployment fields are omitted; versions can have identical published settings after that omission. Upstream runtime commits remain unspecified where the source retained only an integration label.

| Configuration | Recorded artifact / source | Configured card counts | Context tokens | GPU pool tokens | Slots | Draft mode / tokens |
| --- | --- | --- | --- | --- | --- | --- |
| cfg-24cbe54dc740cdeb3ec8 | [SloptimistPrime/apex-flash-1-abliterated-EXL3-4bit-DGX-Spark@a4c922dc57](https://huggingface.co/SloptimistPrime/apex-flash-1-abliterated-EXL3-4bit-DGX-Spark/tree/a4c922dc57dae44a9569ec82a08a2f311636e2a6) | 3 | 262,144 | 262,144 | 4 | mtp / 3 |

Card counts are saved configuration choices, not a claim that every allowed placement was measured. A derived view can differ from its pinned download source.

<details>
<summary>cfg-24cbe54dc740cdeb3ec8</summary>

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
  "served_model_label": "apex-flash-1-abliterated-exl3-4bit-spark"
}
```

Pinned model revision recorded: yes. Source receipt labels, hashes and object locators are retained in [configurations.json](../configurations.json).

</details>

## Retained Measurements

| Profile / Wave | Layout; Draft / Tokens | Requests | Input tokens/request | Accepted output tokens/request | Cache / Reused input tokens | Context / GPU pool tokens | Shared decode tok/s total | Client after-first-token estimate tok/s | Whole-wave output tok/s | Median TTFT, s | Source report |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [ad003-apex_exl3-mtp3-original-layer_split-matched-081](ad003-apex_exl3-mtp3-original-layer_split-matched-081.md)<br>wave-16a19e0719f449debbe2 | layer_split; mtp / 3 | 4 | 32,767 | 256 (budget 256) | cached_prefix; reused 32,512 | 262,144 / 262,144 | 45.89 | Not recorded | 41.67 | 3.07 | Pass |
| [ad003-apex_exl3-mtp3-original-layer_split-matched-081](ad003-apex_exl3-mtp3-original-layer_split-matched-081.md)<br>wave-30f1b561dc67a96e6d48 | layer_split; mtp / 3 | 1 | 32,766 | 256 (budget 256) | cold; reused 0 | 262,144 / 262,144 | 38.44 | Not recorded | 5.53 | 39.75 | Pass |
| [ad003-apex_exl3-mtp3-original-layer_split-matched-081](ad003-apex_exl3-mtp3-original-layer_split-matched-081.md)<br>wave-c04da91cc8544d64f748 | layer_split; mtp / 3 | 1 | 32,766 | 256 (budget 256) | cached_prefix; reused 32,512 | 262,144 / 262,144 | 41.75 | Not recorded | 37.89 | 0.80 | Pass |
| [ad003-apex_exl3-mtp3-original-layer_split-matched-081](ad003-apex_exl3-mtp3-original-layer_split-matched-081.md)<br>wave-f829168ef3a65210a314 | layer_split; mtp / 3 | 4 | 32,767 | 256 (budget 256) | cold; reused 0 | 262,144 / 262,144 | 46.93 | Not recorded | 5.67 | 158.72 | Pass |

Rates are whole-wave totals over the stated request count. A wave may span multiple independent model instances; [measurements.json](../measurements.json) retains their contributions and the exact configuration IDs. Do not interpret a multi-instance total as one card's rate.

A dash in shared decode means no qualified synchronized interval is available. Whole-wave throughput includes prefill and queueing. A valid decode interval can survive inside an overall failed or partial check; the source-report outcome is preserved. No rows are averaged.

## Bounded Checks

| Check | Reported outcome | Retained counts / flags |
| --- | --- | --- |
| check-308c4809ead0baf0717a | Pass | {"passed":true,"elapsed_seconds":46.27537265400315,"ttft_seconds":[39.745100225001806],"end_to_end_accepted_tok_s":5.5321002364279} |
| check-5497abc894e770c53e05 | Pass | {"passed":true,"elapsed_seconds":180.58520231099828,"ttft_seconds":[154.82148168099957,158.02526066399878,159.4131580530011,159.41281319299742],"end_to_end_accepted_tok_s":5.670453541572574} |
| check-96f721692f09f5109c4c | Pass | {"passed":true,"elapsed_seconds":180.58520231099828,"ttft_seconds":[154.82148168099957,158.02526066399878,159.4131580530011,159.41281319299742],"end_to_end_accepted_tok_s":5.670453541572574} |
| check-e0f2105ac0b23f4aad37 | Pass | {"passed":true,"elapsed_seconds":46.27537265400315,"ttft_seconds":[39.745100225001806],"end_to_end_accepted_tok_s":5.5321002364279} |

These checks retain their reported scope. A context/allocation/retrieval check is not a general quality score or a speed qualification at that context. Exact flags and provenance are in [checks.json](../checks.json).

## Additional Test Results

| Result / Source | Profile | Evidence type | Reported outcome | Retained values | Configuration binding |
| --- | --- | --- | --- | --- | --- |
| [result-3fea01c1ef300be56963](../observations.json)<br>source-a9e622d351a86c8b776605d4.json<br>`/managed_phase_timings/81` | [ad003-apex_exl3-mtp3-original-layer_split-matched-081](ad003-apex_exl3-mtp3-original-layer_split-matched-081.md) | test outcome | Outcome unspecified | wall_seconds=596.58 s | Recorded configuration/job |
| [result-50295cd174c59690c6eb](../observations.json)<br>source-21e5a33f93dfbe306c115b34.json<br>`/waves/1` | [ad003-apex_exl3-mtp3-original-layer_split-matched-081](ad003-apex_exl3-mtp3-original-layer_split-matched-081.md)<br>[record-26c850ec689cf58c6b67](record-26c850ec689cf58c6b67.md)<br>[apex_exl3-mtp3-original-layer_split](apex_exl3-mtp3-original-layer_split.md) | performance detail | Outcome unspecified | elapsed_seconds=24.57 s; end_to_end_accepted_tok_s=41.67 accepted tokens/s; output_tokens=256 tokens; ttft_seconds=0.93<br>3.07<br>3.07<br>3.24 s; p50_ms=80.91 ms; p95_ms=235.33 ms; prefill: per-request 286.52 to 579.55 tokens/s; Draft accepted / proposed: 636 / 1,164 tokens; fraction 0.5464 | Recorded configuration/job |
| [result-5332c09790850ef9ce4a](../observations.json)<br>source-21e5a33f93dfbe306c115b34.json<br>`/` | [ad003-apex_exl3-mtp3-original-layer_split-matched-081](ad003-apex_exl3-mtp3-original-layer_split-matched-081.md)<br>[record-26c850ec689cf58c6b67](record-26c850ec689cf58c6b67.md)<br>[apex_exl3-mtp3-original-layer_split](apex_exl3-mtp3-original-layer_split.md) | performance detail | Pass | elapsed_seconds=180.59 s; end_to_end_accepted_tok_s=5.67 accepted tokens/s; ttft_seconds=154.82<br>158.03<br>159.41<br>159.41 s; p50_ms=80.91 ms; p95_ms=235.33 ms; cold_prefill: per-request 211.89 to 214.91 tokens/s; Draft accepted / proposed: 636 / 1,164 tokens; fraction 0.5464 | Recorded configuration/job |
| [result-5e2453a8aa087f678189](../observations.json)<br>source-ac20941d1a39a76be7d859a8.json<br>`/` | [ad003-apex_exl3-mtp3-original-layer_split-matched-081](ad003-apex_exl3-mtp3-original-layer_split-matched-081.md)<br>[record-26c850ec689cf58c6b67](record-26c850ec689cf58c6b67.md)<br>[apex_exl3-mtp3-original-layer_split](apex_exl3-mtp3-original-layer_split.md) | performance detail | Pass | elapsed_seconds=46.28 s; end_to_end_accepted_tok_s=5.53 accepted tokens/s; ttft_seconds=39.75 s; p50_ms=23.37 ms; p95_ms=67.41 ms; cold_prefill: per-request 827.22 tokens/s; Draft accepted / proposed: 170 / 258 tokens; fraction 0.6589 | Recorded configuration/job |
| [result-6ba68a062e1d511817b2](../observations.json)<br>source-ac20941d1a39a76be7d859a8.json<br>`/waves/1` | [ad003-apex_exl3-mtp3-original-layer_split-matched-081](ad003-apex_exl3-mtp3-original-layer_split-matched-081.md)<br>[record-26c850ec689cf58c6b67](record-26c850ec689cf58c6b67.md)<br>[apex_exl3-mtp3-original-layer_split](apex_exl3-mtp3-original-layer_split.md) | performance detail | Outcome unspecified | elapsed_seconds=6.76 s; end_to_end_accepted_tok_s=37.89 accepted tokens/s; output_tokens=256 tokens; ttft_seconds=0.80 s; p50_ms=23.37 ms; p95_ms=67.41 ms; prefill: per-request 479.25 tokens/s; Draft accepted / proposed: 170 / 258 tokens; fraction 0.6589 | Recorded configuration/job |
| [result-8c9402ebb3f6ee422220](../observations.json)<br>source-ac20941d1a39a76be7d859a8.json<br>`/waves/0` | [ad003-apex_exl3-mtp3-original-layer_split-matched-081](ad003-apex_exl3-mtp3-original-layer_split-matched-081.md)<br>[record-26c850ec689cf58c6b67](record-26c850ec689cf58c6b67.md)<br>[apex_exl3-mtp3-original-layer_split](apex_exl3-mtp3-original-layer_split.md) | performance detail | Outcome unspecified | elapsed_seconds=46.28 s; end_to_end_accepted_tok_s=5.53 accepted tokens/s; output_tokens=256 tokens; ttft_seconds=39.75 s; p50_ms=24.52 ms; p95_ms=69.63 ms; prefill: per-request 827.22 tokens/s; Draft accepted / proposed: 164 / 276 tokens; fraction 0.5942 | Recorded configuration/job |
| [result-bec80e75a76d58e195b0](../observations.json)<br>source-21e5a33f93dfbe306c115b34.json<br>`/waves/0` | [ad003-apex_exl3-mtp3-original-layer_split-matched-081](ad003-apex_exl3-mtp3-original-layer_split-matched-081.md)<br>[record-26c850ec689cf58c6b67](record-26c850ec689cf58c6b67.md)<br>[apex_exl3-mtp3-original-layer_split](apex_exl3-mtp3-original-layer_split.md) | performance detail | Outcome unspecified | elapsed_seconds=180.59 s; end_to_end_accepted_tok_s=5.67 accepted tokens/s; output_tokens=256 tokens; ttft_seconds=154.82<br>158.03<br>159.41<br>159.41 s; p50_ms=79.76 ms; p95_ms=233.78 ms; prefill: per-request 211.89 to 214.91 tokens/s; Draft accepted / proposed: 640 / 1,152 tokens; fraction 0.5556 | Recorded configuration/job |

These are saved result records, including failures and bounded checks. Copies, individual requests, report summaries and regrading can overlap; their counts are not independent test repetitions. Open each result for exact values, units, configuration binding and source receipts.

There are 1 retained lifecycle records. Their states, exit codes and configuration IDs remain in [catalog.json](../catalog.json); they do not supply missing benchmark results.

[Full archive](../../README.md) | [All retained waves](../RESULTS.md) | [Data definitions](../DATA.md) | [Recommended recipes](../../../README.md)
