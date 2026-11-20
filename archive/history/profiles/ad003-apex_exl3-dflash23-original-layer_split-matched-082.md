# ad003-apex_exl3-dflash23-original-layer_split-matched-082

**Historical record. Decode interval measured.**

Model family: Apex Flash 1 (GLM 5.3 Flash post-train).

Historical configurations are provided for comparison. The [recommended recipes](../../../README.md) include supported launch scripts.

Current recipes using the same recorded checkpoint repository: [apex-abliterated-exl3-mtp1-tp3](../../../recipes/apex-abliterated-exl3-mtp1-tp3/README.md). Context, cache and runtime versions can differ.

## Saved Configuration Versions

Each configuration ID identifies a distinct original settings record. Deployment fields are omitted; versions can have identical published settings after that omission. Upstream runtime commits remain unspecified where the source retained only an integration label.

| Configuration | Recorded artifact / source | Configured card counts | Context tokens | GPU pool tokens | Slots | Draft mode / tokens |
| --- | --- | --- | --- | --- | --- | --- |
| cfg-a9bc043422b06709c469 | [SloptimistPrime/apex-flash-1-abliterated-EXL3-4bit-DGX-Spark@a4c922dc57](https://huggingface.co/SloptimistPrime/apex-flash-1-abliterated-EXL3-4bit-DGX-Spark/tree/a4c922dc57dae44a9569ec82a08a2f311636e2a6) | 3 | 262,144 | 262,144 | 4 | dflash2 / 3 |

Card counts are saved configuration choices, not a claim that every allowed placement was measured. A derived view can differ from its pinned download source.

<details>
<summary>cfg-a9bc043422b06709c469</summary>

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
| [ad003-apex_exl3-dflash23-original-layer_split-matched-082](ad003-apex_exl3-dflash23-original-layer_split-matched-082.md)<br>wave-4fe0eba795ae89709ac3 | layer_split; dflash2 / 3 | 1 | 32,766 | 256 (budget 256) | cached_prefix; reused 32,512 | 262,144 / 262,144 | 38.16 | Not recorded | 35.04 | 0.85 | Pass |
| [ad003-apex_exl3-dflash23-original-layer_split-matched-082](ad003-apex_exl3-dflash23-original-layer_split-matched-082.md)<br>wave-9c9543f0b57cb771d4ca | layer_split; dflash2 / 3 | 1 | 32,766 | 256 (budget 256) | cold; reused 0 | 262,144 / 262,144 | 39.30 | Not recorded | 5.59 | 39.39 | Pass |
| [ad003-apex_exl3-dflash23-original-layer_split-matched-082](ad003-apex_exl3-dflash23-original-layer_split-matched-082.md)<br>wave-adf29f6ad00ffe24bfb7 | layer_split; dflash2 / 3 | 4 | 32,767 | 256 (budget 256) | cold; reused 0 | 262,144 / 262,144 | 42.56 | Not recorded | 5.65 | 157.34 | Pass |
| [ad003-apex_exl3-dflash23-original-layer_split-matched-082](ad003-apex_exl3-dflash23-original-layer_split-matched-082.md)<br>wave-d1ddae28c26330f2903b | layer_split; dflash2 / 3 | 4 | 32,767 | 256 (budget 256) | cached_prefix; reused 32,512 | 262,144 / 262,144 | 44.09 | Not recorded | 39.97 | 3.08 | Pass |

Rates are whole-wave totals over the stated request count. A wave may span multiple independent model instances; [measurements.json](../measurements.json) retains their contributions and the exact configuration IDs. Do not interpret a multi-instance total as one card's rate.

A dash in shared decode means no qualified synchronized interval is available. Whole-wave throughput includes prefill and queueing. A valid decode interval can survive inside an overall failed or partial check; the source-report outcome is preserved. No rows are averaged.

## Bounded Checks

| Check | Reported outcome | Retained counts / flags |
| --- | --- | --- |
| check-14284ba6221cb3806bce | Pass | {"passed":true,"elapsed_seconds":45.80659992400615,"ttft_seconds":[39.392523984002764],"end_to_end_accepted_tok_s":5.588714299352231} |
| check-254430aaa944a42932ee | Pass | {"passed":true,"elapsed_seconds":181.23041259599995,"ttft_seconds":[152.39842848699482,157.33938572899933,157.33906315900094,158.30287992100057],"end_to_end_accepted_tok_s":5.650265787799687} |
| check-5b98a5155a63dbba11a4 | Pass | {"passed":true,"elapsed_seconds":181.23041259599995,"ttft_seconds":[152.39842848699482,157.33938572899933,157.33906315900094,158.30287992100057],"end_to_end_accepted_tok_s":5.650265787799687} |
| check-fa1184da4698e46ad139 | Pass | {"passed":true,"elapsed_seconds":45.80659992400615,"ttft_seconds":[39.392523984002764],"end_to_end_accepted_tok_s":5.588714299352231} |

These checks retain their reported scope. A context/allocation/retrieval check is not a general quality score or a speed qualification at that context. Exact flags and provenance are in [checks.json](../checks.json).

## Additional Test Results

| Result / Source | Profile | Evidence type | Reported outcome | Retained values | Configuration binding |
| --- | --- | --- | --- | --- | --- |
| [result-174e97dcf3276ce50891](../observations.json)<br>source-448fe337a66d19226687fde8.json<br>`/waves/1` | [ad003-apex_exl3-dflash23-original-layer_split-matched-082](ad003-apex_exl3-dflash23-original-layer_split-matched-082.md)<br>[record-26c850ec689cf58c6b67](record-26c850ec689cf58c6b67.md)<br>[apex_exl3-dflash23-original-layer_split](apex_exl3-dflash23-original-layer_split.md) | performance detail | Outcome unspecified | elapsed_seconds=25.62 s; end_to_end_accepted_tok_s=39.97 accepted tokens/s; output_tokens=256 tokens; ttft_seconds=0.88<br>2.98<br>3.17<br>3.37 s; p50_ms=81.54 ms; p95_ms=246.98 ms; prefill: per-request 510.00 to 593.02 tokens/s; Draft accepted / proposed: 632 / 1,176 tokens; fraction 0.5374 | Recorded configuration/job |
| [result-7746b28f9df90e121159](../observations.json)<br>source-448fe337a66d19226687fde8.json<br>`/` | [ad003-apex_exl3-dflash23-original-layer_split-matched-082](ad003-apex_exl3-dflash23-original-layer_split-matched-082.md)<br>[record-26c850ec689cf58c6b67](record-26c850ec689cf58c6b67.md)<br>[apex_exl3-dflash23-original-layer_split](apex_exl3-dflash23-original-layer_split.md) | performance detail | Pass | elapsed_seconds=181.23 s; end_to_end_accepted_tok_s=5.65 accepted tokens/s; ttft_seconds=152.40<br>157.34<br>157.34<br>158.30 s; p50_ms=81.54 ms; p95_ms=246.98 ms; cold_prefill: per-request 212.95 to 217.55 tokens/s; Draft accepted / proposed: 632 / 1,176 tokens; fraction 0.5374 | Recorded configuration/job |
| [result-86e5a7c100ff85971b9e](../observations.json)<br>source-a9e622d351a86c8b776605d4.json<br>`/managed_phase_timings/82` | [ad003-apex_exl3-dflash23-original-layer_split-matched-082](ad003-apex_exl3-dflash23-original-layer_split-matched-082.md) | test outcome | Outcome unspecified | wall_seconds=595.54 s | Recorded configuration/job |
| [result-8a057dba437c9fc8d3e6](../observations.json)<br>source-448fe337a66d19226687fde8.json<br>`/waves/0` | [ad003-apex_exl3-dflash23-original-layer_split-matched-082](ad003-apex_exl3-dflash23-original-layer_split-matched-082.md)<br>[record-26c850ec689cf58c6b67](record-26c850ec689cf58c6b67.md)<br>[apex_exl3-dflash23-original-layer_split](apex_exl3-dflash23-original-layer_split.md) | performance detail | Outcome unspecified | elapsed_seconds=181.23 s; end_to_end_accepted_tok_s=5.65 accepted tokens/s; output_tokens=256 tokens; ttft_seconds=152.40<br>157.34<br>157.34<br>158.30 s; p50_ms=83.82 ms; p95_ms=243.28 ms; prefill: per-request 212.95 to 217.55 tokens/s; Draft accepted / proposed: 624 / 1,200 tokens; fraction 0.5200 | Recorded configuration/job |
| [result-a8767038d83d490e4297](../observations.json)<br>source-dfaa296d6d9292dd97266c26.json<br>`/waves/1` | [ad003-apex_exl3-dflash23-original-layer_split-matched-082](ad003-apex_exl3-dflash23-original-layer_split-matched-082.md)<br>[record-26c850ec689cf58c6b67](record-26c850ec689cf58c6b67.md)<br>[apex_exl3-dflash23-original-layer_split](apex_exl3-dflash23-original-layer_split.md) | performance detail | Outcome unspecified | elapsed_seconds=7.30 s; end_to_end_accepted_tok_s=35.04 accepted tokens/s; output_tokens=256 tokens; ttft_seconds=0.85 s; p50_ms=25.11 ms; p95_ms=74.80 ms; prefill: per-request 488.46 tokens/s; Draft accepted / proposed: 165 / 273 tokens; fraction 0.6044 | Recorded configuration/job |
| [result-c94e0dc58d3330c0c7f7](../observations.json)<br>source-dfaa296d6d9292dd97266c26.json<br>`/waves/0` | [ad003-apex_exl3-dflash23-original-layer_split-matched-082](ad003-apex_exl3-dflash23-original-layer_split-matched-082.md)<br>[record-26c850ec689cf58c6b67](record-26c850ec689cf58c6b67.md)<br>[apex_exl3-dflash23-original-layer_split](apex_exl3-dflash23-original-layer_split.md) | performance detail | Outcome unspecified | elapsed_seconds=45.81 s; end_to_end_accepted_tok_s=5.59 accepted tokens/s; output_tokens=256 tokens; ttft_seconds=39.39 s; p50_ms=21.08 ms; p95_ms=73.87 ms; prefill: per-request 834.59 tokens/s; Draft accepted / proposed: 168 / 264 tokens; fraction 0.6364 | Recorded configuration/job |
| [result-e2deb50e7786e95a20d4](../observations.json)<br>source-dfaa296d6d9292dd97266c26.json<br>`/` | [ad003-apex_exl3-dflash23-original-layer_split-matched-082](ad003-apex_exl3-dflash23-original-layer_split-matched-082.md)<br>[record-26c850ec689cf58c6b67](record-26c850ec689cf58c6b67.md)<br>[apex_exl3-dflash23-original-layer_split](apex_exl3-dflash23-original-layer_split.md) | performance detail | Pass | elapsed_seconds=45.81 s; end_to_end_accepted_tok_s=5.59 accepted tokens/s; ttft_seconds=39.39 s; p50_ms=25.11 ms; p95_ms=74.80 ms; cold_prefill: per-request 834.59 tokens/s; Draft accepted / proposed: 165 / 273 tokens; fraction 0.6044 | Recorded configuration/job |

These are saved result records, including failures and bounded checks. Copies, individual requests, report summaries and regrading can overlap; their counts are not independent test repetitions. Open each result for exact values, units, configuration binding and source receipts.

There are 1 retained lifecycle records. Their states, exit codes and configuration IDs remain in [catalog.json](../catalog.json); they do not supply missing benchmark results.

[Full archive](../../README.md) | [All retained waves](../RESULTS.md) | [Data definitions](../DATA.md) | [Recommended recipes](../../../README.md)
