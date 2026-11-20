# ad027-flash-baseline-0

**Historical record. Decode interval measured.**

Model family: Other model workflows.

Historical configurations are provided for comparison. The [recommended recipes](../../../README.md) include supported launch scripts.

## Saved Configuration Versions

Each configuration ID identifies a distinct original settings record. Deployment fields are omitted; versions can have identical published settings after that omission. Upstream runtime commits remain unspecified where the source retained only an integration label.

| Configuration | Recorded artifact / source | Configured card counts | Context tokens | GPU pool tokens | Slots | Draft mode / tokens |
| --- | --- | --- | --- | --- | --- | --- |
| cfg-37ceb18520c117d0eeb6 | qwen3.8-flash-next | 2 | Not recorded | Not recorded | Not recorded | unspecified / - |
| cfg-f3fb7cb82b751a1ed2d0 | qwen3.8-flash-next | 2 | Not recorded | Not recorded | Not recorded | unspecified / - |

Card counts are saved configuration choices, not a claim that every allowed placement was measured. A derived view can differ from its pinned download source.

<details>
<summary>cfg-37ceb18520c117d0eeb6</summary>

```json
{
  "kind": "command",
  "gpu_counts": [
    2
  ],
  "power_watts": 200,
  "host_memory_gib": 0,
  "host_swap_gib": 0,
  "min_vram_mib_per_gpu": 65530,
  "min_effective_vram_mib": 131060,
  "model_repository": null,
  "model_revision": null,
  "draft_repository": null,
  "draft_revision": null,
  "recorded_runtime_label": null,
  "served_model_label": "qwen3.8-flash-next",
  "recorded_wrapper_settings": {
    "kind": "tabby",
    "context": 262144,
    "max_sessions": 6,
    "draft_tokens": 2
  }
}
```

Pinned model revision recorded: no. Source receipt labels, hashes and object locators are retained in [configurations.json](../configurations.json).

</details>

<details>
<summary>cfg-f3fb7cb82b751a1ed2d0</summary>

```json
{
  "kind": "command",
  "gpu_counts": [
    2
  ],
  "power_watts": 200,
  "host_memory_gib": 0,
  "host_swap_gib": 0,
  "min_vram_mib_per_gpu": 65530,
  "min_effective_vram_mib": 131060,
  "model_repository": null,
  "model_revision": null,
  "draft_repository": null,
  "draft_revision": null,
  "recorded_runtime_label": null,
  "served_model_label": "qwen3.8-flash-next",
  "recorded_wrapper_settings": {
    "kind": "tabby",
    "context": 262144,
    "max_sessions": 6,
    "draft_tokens": 2
  }
}
```

Pinned model revision recorded: no. Source receipt labels, hashes and object locators are retained in [configurations.json](../configurations.json).

</details>

## Retained Measurements

| Profile / Wave | Layout; Draft / Tokens | Requests | Input tokens/request | Accepted output tokens/request | Cache / Reused input tokens | Context / GPU pool tokens | Shared decode tok/s total | Client after-first-token estimate tok/s | Whole-wave output tok/s | Median TTFT, s | Source report |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [ad027-flash-baseline-0](ad027-flash-baseline-0.md)<br>wave-1c7469ac59cd73faf71a | layout unspecified; draft unspecified / - | 1 | 32,769 | 256 (budget 256) | cold; reused 0 | - / - | 74.79 | Not recorded | 9.16 | 24.60 | Pass |
| [ad027-flash-baseline-0](ad027-flash-baseline-0.md)<br>wave-aa854fd24336ebbc2f83 | layout unspecified; draft unspecified / - | 6 | 32,770 | 256 (budget 256) | cold; reused 0 | - / - | 136.71 | Not recorded | 9.67 | 147.66 | Pass |

Rates are whole-wave totals over the stated request count. A wave may span multiple independent model instances; [measurements.json](../measurements.json) retains their contributions and the exact configuration IDs. Do not interpret a multi-instance total as one card's rate.

A dash in shared decode means no qualified synchronized interval is available. Whole-wave throughput includes prefill and queueing. A valid decode interval can survive inside an overall failed or partial check; the source-report outcome is preserved. No rows are averaged.

## Bounded Checks

| Check | Reported outcome | Retained counts / flags |
| --- | --- | --- |
| check-24c45968a9e435eb1ccc | Pass | {"passed":true,"elapsed_seconds":27.960676650996902,"ttft_seconds":[24.603307130993926],"end_to_end_accepted_tok_s":9.155715478397504} |
| check-d2961bafc23b542bad35 | Pass | {"passed":true,"elapsed_seconds":158.82701132100192,"ttft_seconds":[142.69154487999913,146.574814024003,147.65679018599621,147.656049807003,147.80560369699378,147.80498512000486],"end_to_end_accepted_tok_s":9.670899094711434} |

These checks retain their reported scope. A context/allocation/retrieval check is not a general quality score or a speed qualification at that context. Exact flags and provenance are in [checks.json](../checks.json).

## Additional Test Results

| Result / Source | Profile | Evidence type | Reported outcome | Retained values | Configuration binding |
| --- | --- | --- | --- | --- | --- |
| [result-010b19b2d6101a1d926a](../observations.json)<br>source-ed21e72502f19e91fcf5b107.json<br>`/spec/serving_config` | [ad027-flash-baseline-0](ad027-flash-baseline-0.md) | context allocation | Outcome unspecified | cache_tokens=1,356,032 tokens; context=262,144 tokens; reserve_mib=2,048 MiB | Recorded configuration/job |
| [result-3edc48ccaec50d9961a8](../observations.json)<br>source-cf1d9416f4fb1e22d8f67a6d.json<br>`/waves/0` | [ad027-flash-baseline-0](ad027-flash-baseline-0.md) | performance detail | Outcome unspecified | elapsed_seconds=158.83 s; end_to_end_accepted_tok_s=9.67 accepted tokens/s; output_tokens=256 tokens; ttft_seconds=142.69<br>146.57<br>147.66<br>147.66<br>147.81<br>147.80 s; p50_ms=37.85 ms; p95_ms=112.13 ms; prefill: per-request 226.33 to 233.06 tokens/s; Draft accepted / proposed: 921 / 1,230 tokens; fraction 0.7488 | Recorded configuration/job |
| [result-59f8ee151eb6ee3a2b53](../observations.json)<br>source-cf1d9416f4fb1e22d8f67a6d.json<br>`/` | [ad027-flash-baseline-0](ad027-flash-baseline-0.md) | performance detail | Pass | elapsed_seconds=158.83 s; end_to_end_accepted_tok_s=9.67 accepted tokens/s; ttft_seconds=142.69<br>146.57<br>147.66<br>147.66<br>147.81<br>147.80 s; p50_ms=37.85 ms; p95_ms=112.13 ms; cold_prefill: per-request 226.33 to 233.06 tokens/s; Draft accepted / proposed: 921 / 1,230 tokens; fraction 0.7488 | Recorded configuration/job |
| [result-80c258a52c98c92ed6ea](../observations.json)<br>source-3f6203ee5fe06f6185c22639.json<br>`/waves/0` | [ad027-flash-baseline-0](ad027-flash-baseline-0.md) | performance detail | Outcome unspecified | elapsed_seconds=27.96 s; end_to_end_accepted_tok_s=9.16 accepted tokens/s; output_tokens=256 tokens; ttft_seconds=24.60 s; p50_ms=11.74 ms; p95_ms=33.53 ms; prefill: per-request 1,336.96 tokens/s; Draft accepted / proposed: 158 / 196 tokens; fraction 0.8061 | Recorded configuration/job |
| [result-e592f3205b989432d0a6](../observations.json)<br>source-3f6203ee5fe06f6185c22639.json<br>`/` | [ad027-flash-baseline-0](ad027-flash-baseline-0.md) | performance detail | Pass | elapsed_seconds=27.96 s; end_to_end_accepted_tok_s=9.16 accepted tokens/s; ttft_seconds=24.60 s; p50_ms=11.74 ms; p95_ms=33.53 ms; cold_prefill: per-request 1,336.96 tokens/s; Draft accepted / proposed: 158 / 196 tokens; fraction 0.8061 | Recorded configuration/job |

These are saved result records, including failures and bounded checks. Copies, individual requests, report summaries and regrading can overlap; their counts are not independent test repetitions. Open each result for exact values, units, configuration binding and source receipts.

There are 1 retained lifecycle records. Their states, exit codes and configuration IDs remain in [catalog.json](../catalog.json); they do not supply missing benchmark results.

[Full archive](../../README.md) | [All retained waves](../RESULTS.md) | [Data definitions](../DATA.md) | [Recommended recipes](../../../README.md)
