# ad027-apex-mhc-12

**Historical record. Decode interval measured.**

Model family: Apex Flash 1 (GLM 5.3 Flash post-train).

Historical configurations are provided for comparison. The [recommended recipes](../../../README.md) include supported launch scripts.

## Saved Configuration Versions

Each configuration ID identifies a distinct original settings record. Deployment fields are omitted; versions can have identical published settings after that omission. Upstream runtime commits remain unspecified where the source retained only an integration label.

| Configuration | Recorded artifact / source | Configured card counts | Context tokens | GPU pool tokens | Slots | Draft mode / tokens |
| --- | --- | --- | --- | --- | --- | --- |
| cfg-15c5f2b96640b2ebae44 | apex-flash-1-abliterated-exl3-4bit-spark | 3 | Not recorded | Not recorded | Not recorded | unspecified / - |
| cfg-5fb45297343044dbc72d | apex-flash-1-abliterated-exl3-4bit-spark | 3 | Not recorded | Not recorded | Not recorded | unspecified / - |

Card counts are saved configuration choices, not a claim that every allowed placement was measured. A derived view can differ from its pinned download source.

<details>
<summary>cfg-15c5f2b96640b2ebae44</summary>

```json
{
  "kind": "command",
  "gpu_counts": [
    3
  ],
  "power_watts": 200,
  "host_memory_gib": 0,
  "host_swap_gib": 0,
  "min_vram_mib_per_gpu": 65530,
  "min_effective_vram_mib": 196590,
  "model_repository": null,
  "model_revision": null,
  "draft_repository": null,
  "draft_revision": null,
  "recorded_runtime_label": null,
  "served_model_label": "apex-flash-1-abliterated-exl3-4bit-spark",
  "recorded_wrapper_settings": {
    "kind": "tabby",
    "context": 524288,
    "max_sessions": 4,
    "draft_tokens": 1
  }
}
```

Pinned model revision recorded: no. Source receipt labels, hashes and object locators are retained in [configurations.json](../configurations.json).

</details>

<details>
<summary>cfg-5fb45297343044dbc72d</summary>

```json
{
  "kind": "command",
  "gpu_counts": [
    3
  ],
  "power_watts": 200,
  "host_memory_gib": 0,
  "host_swap_gib": 0,
  "min_vram_mib_per_gpu": 65530,
  "min_effective_vram_mib": 196590,
  "model_repository": null,
  "model_revision": null,
  "draft_repository": null,
  "draft_revision": null,
  "recorded_runtime_label": null,
  "served_model_label": "apex-flash-1-abliterated-exl3-4bit-spark",
  "recorded_wrapper_settings": {
    "kind": "tabby",
    "context": 524288,
    "max_sessions": 4,
    "draft_tokens": 1
  }
}
```

Pinned model revision recorded: no. Source receipt labels, hashes and object locators are retained in [configurations.json](../configurations.json).

</details>

## Retained Measurements

| Profile / Wave | Layout; Draft / Tokens | Requests | Input tokens/request | Accepted output tokens/request | Cache / Reused input tokens | Context / GPU pool tokens | Shared decode tok/s total | Client after-first-token estimate tok/s | Whole-wave output tok/s | Median TTFT, s | Source report |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [ad027-apex-mhc-12](ad027-apex-mhc-12.md)<br>wave-5015af8d8c4952f9c890 | layout unspecified; draft unspecified / - | 4 | 32,769 | 256 (budget 256) | cold; reused 0 | - / - | 96.20 | Not recorded | 4.83 | 200.60 | Pass |
| [ad027-apex-mhc-12](ad027-apex-mhc-12.md)<br>wave-6d6bdd9990d3e6398ef7 | layout unspecified; draft unspecified / - | 1 | 32,766 | 256 (budget 256) | cold; reused 0 | - / - | 41.25 | Not recorded | 4.53 | 50.36 | Pass |
| [ad027-apex-mhc-12](ad027-apex-mhc-12.md)<br>wave-705cd93fc02c4004b60f | layout unspecified; draft unspecified / - | 4 | 32,767 | 256 (budget 256) | cold; reused 0 | - / - | 96.25 | Not recorded | 4.82 | 202.15 | Pass |

Rates are whole-wave totals over the stated request count. A wave may span multiple independent model instances; [measurements.json](../measurements.json) retains their contributions and the exact configuration IDs. Do not interpret a multi-instance total as one card's rate.

A dash in shared decode means no qualified synchronized interval is available. Whole-wave throughput includes prefill and queueing. A valid decode interval can survive inside an overall failed or partial check; the source-report outcome is preserved. No rows are averaged.

## Bounded Checks

| Check | Reported outcome | Retained counts / flags |
| --- | --- | --- |
| check-0d48385ea29a18ec2ffd | Pass | {"passed":true,"elapsed_seconds":212.0942292749969,"ttft_seconds":[194.85435455400147,199.69846469900222,201.50639223000326,201.50587532899226],"end_to_end_accepted_tok_s":4.828042721861626} |
| check-54899a542b4f84c79c2e | Pass | {"passed":true,"elapsed_seconds":56.49064947699662,"ttft_seconds":[50.35584377399937],"end_to_end_accepted_tok_s":4.531723433348822} |
| check-a1d65a9b97910ec5a4ff | Pass | {"passed":true,"elapsed_seconds":212.5956163820083,"ttft_seconds":[195.70939020399237,202.15340230798756,202.15309402999992,202.1532131569984],"end_to_end_accepted_tok_s":4.816656229449235} |

These checks retain their reported scope. A context/allocation/retrieval check is not a general quality score or a speed qualification at that context. Exact flags and provenance are in [checks.json](../checks.json).

## Additional Test Results

| Result / Source | Profile | Evidence type | Reported outcome | Retained values | Configuration binding |
| --- | --- | --- | --- | --- | --- |
| [result-087d7d8d48626961e867](../observations.json)<br>source-ed21e72502f19e91fcf5b107.json<br>`/spec/serving_config` | [ad027-apex-mhc-12](ad027-apex-mhc-12.md) | context allocation | Outcome unspecified | cache_tokens=1,083,136 tokens; context=524,288 tokens; reserve_mib=2,048 MiB | Recorded configuration/job |
| [result-1ac78e153cb38ceb07f4](../observations.json)<br>source-cf1d9416f4fb1e22d8f67a6d.json<br>`/waves/0` | [ad027-apex-mhc-12](ad027-apex-mhc-12.md) | performance detail | Outcome unspecified | elapsed_seconds=212.60 s; end_to_end_accepted_tok_s=4.82 accepted tokens/s; output_tokens=256 tokens; ttft_seconds=195.71<br>202.15<br>202.15<br>202.15 s; p50_ms=37.70 ms; p95_ms=75.30 ms; prefill: per-request 165.54 to 168.57 tokens/s; Draft accepted / proposed: 463 / 561 tokens; fraction 0.8253 | Recorded configuration/job |
| [result-2a4912a03a69f90ac8f2](../observations.json)<br>source-43b4d9fd0306e68f09306093.json<br>`/` | [ad027-apex-mhc-12](ad027-apex-mhc-12.md) | performance detail | Pass | elapsed_seconds=212.09 s; end_to_end_accepted_tok_s=4.83 accepted tokens/s; ttft_seconds=194.85<br>199.70<br>201.51<br>201.51 s; p50_ms=38.84 ms; p95_ms=75.50 ms; cold_prefill: per-request 166.29 to 168.25 tokens/s; Draft accepted / proposed: 473 / 551 tokens; fraction 0.8584 | Recorded configuration/job |
| [result-428ed93d80df7b025707](../observations.json)<br>source-3f6203ee5fe06f6185c22639.json<br>`/` | [ad027-apex-mhc-12](ad027-apex-mhc-12.md) | performance detail | Pass | elapsed_seconds=56.49 s; end_to_end_accepted_tok_s=4.53 accepted tokens/s; ttft_seconds=50.36 s; p50_ms=22.56 ms; p95_ms=43.99 ms; cold_prefill: per-request 651.93 tokens/s; Draft accepted / proposed: 116 / 140 tokens; fraction 0.8286 | Recorded configuration/job |
| [result-ad82c0b644e5f437f1b4](../observations.json)<br>source-cf1d9416f4fb1e22d8f67a6d.json<br>`/` | [ad027-apex-mhc-12](ad027-apex-mhc-12.md) | performance detail | Pass | elapsed_seconds=212.60 s; end_to_end_accepted_tok_s=4.82 accepted tokens/s; ttft_seconds=195.71<br>202.15<br>202.15<br>202.15 s; p50_ms=37.70 ms; p95_ms=75.30 ms; cold_prefill: per-request 165.54 to 168.57 tokens/s; Draft accepted / proposed: 463 / 561 tokens; fraction 0.8253 | Recorded configuration/job |
| [result-c4e1c15ec84b2d5e7466](../observations.json)<br>source-43b4d9fd0306e68f09306093.json<br>`/waves/0` | [ad027-apex-mhc-12](ad027-apex-mhc-12.md) | performance detail | Outcome unspecified | elapsed_seconds=212.09 s; end_to_end_accepted_tok_s=4.83 accepted tokens/s; output_tokens=256 tokens; ttft_seconds=194.85<br>199.70<br>201.51<br>201.51 s; p50_ms=38.84 ms; p95_ms=75.50 ms; prefill: per-request 166.29 to 168.25 tokens/s; Draft accepted / proposed: 473 / 551 tokens; fraction 0.8584 | Recorded configuration/job |
| [result-f5d282fa0cd675b513a9](../observations.json)<br>source-3f6203ee5fe06f6185c22639.json<br>`/waves/0` | [ad027-apex-mhc-12](ad027-apex-mhc-12.md) | performance detail | Outcome unspecified | elapsed_seconds=56.49 s; end_to_end_accepted_tok_s=4.53 accepted tokens/s; output_tokens=256 tokens; ttft_seconds=50.36 s; p50_ms=22.56 ms; p95_ms=43.99 ms; prefill: per-request 651.93 tokens/s; Draft accepted / proposed: 116 / 140 tokens; fraction 0.8286 | Recorded configuration/job |

These are saved result records, including failures and bounded checks. Copies, individual requests, report summaries and regrading can overlap; their counts are not independent test repetitions. Open each result for exact values, units, configuration binding and source receipts.

There are 1 retained lifecycle records. Their states, exit codes and configuration IDs remain in [catalog.json](../catalog.json); they do not supply missing benchmark results.

[Full archive](../../README.md) | [All retained waves](../RESULTS.md) | [Data definitions](../DATA.md) | [Recommended recipes](../../../README.md)
