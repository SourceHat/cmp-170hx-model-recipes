# ad027-glm-mhc-10

**Historical record. Decode interval measured.**

Model family: GLM 5.3 Flash.

Historical configurations are provided for comparison. The [recommended recipes](../../../README.md) include supported launch scripts.

## Saved Configuration Versions

Each configuration ID identifies a distinct original settings record. Deployment fields are omitted; versions can have identical published settings after that omission. Upstream runtime commits remain unspecified where the source retained only an integration label.

| Configuration | Recorded artifact / source | Configured card counts | Context tokens | GPU pool tokens | Slots | Draft mode / tokens |
| --- | --- | --- | --- | --- | --- | --- |
| cfg-58c2d7c17f9f02fa76c3 | glm-5.3-flash | 3 | Not recorded | Not recorded | Not recorded | unspecified / - |
| cfg-9a1e49ca895ec6fbc46f | glm-5.3-flash | 3 | Not recorded | Not recorded | Not recorded | unspecified / - |

Card counts are saved configuration choices, not a claim that every allowed placement was measured. A derived view can differ from its pinned download source.

<details>
<summary>cfg-58c2d7c17f9f02fa76c3</summary>

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
  "served_model_label": "glm-5.3-flash",
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
<summary>cfg-9a1e49ca895ec6fbc46f</summary>

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
  "served_model_label": "glm-5.3-flash",
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
| [ad027-glm-mhc-10](ad027-glm-mhc-10.md)<br>wave-874a57da853c0d28ede3 | layout unspecified; draft unspecified / - | 4 | 32,767 | 256 (budget 256) | cold; reused 0 | - / - | 100.26 | Not recorded | 4.87 | 199.45 | Pass |
| [ad027-glm-mhc-10](ad027-glm-mhc-10.md)<br>wave-be76fe37100f09d6e1d7 | layout unspecified; draft unspecified / - | 1 | 32,766 | 256 (budget 256) | cold; reused 0 | - / - | 50.02 | Not recorded | 4.67 | 49.79 | Pass |
| [ad027-glm-mhc-10](ad027-glm-mhc-10.md)<br>wave-dd6d496a8cd94b5a7196 | layout unspecified; draft unspecified / - | 4 | 32,769 | 256 (budget 256) | cold; reused 0 | - / - | 99.32 | Not recorded | 4.89 | 198.30 | Pass |

Rates are whole-wave totals over the stated request count. A wave may span multiple independent model instances; [measurements.json](../measurements.json) retains their contributions and the exact configuration IDs. Do not interpret a multi-instance total as one card's rate.

A dash in shared decode means no qualified synchronized interval is available. Whole-wave throughput includes prefill and queueing. A valid decode interval can survive inside an overall failed or partial check; the source-report outcome is preserved. No rows are averaged.

## Bounded Checks

| Check | Reported outcome | Retained counts / flags |
| --- | --- | --- |
| check-4fcfc661405d0f7f00f0 | Pass | {"passed":true,"elapsed_seconds":209.47913880899432,"ttft_seconds":[192.60387909600104,197.395060949013,199.20064529999217,199.20029719200102],"end_to_end_accepted_tok_s":4.888314921581265} |
| check-74a9c46a8ddf2557b03a | Pass | {"passed":true,"elapsed_seconds":54.81491587799974,"ttft_seconds":[49.79114627999661],"end_to_end_accepted_tok_s":4.670261659614203} |
| check-bc9eae356786b318c543 | Pass | {"passed":true,"elapsed_seconds":210.05617196399544,"ttft_seconds":[195.26115143000789,198.8867614070041,200.01168642799894,200.0113404649892],"end_to_end_accepted_tok_s":4.874886514524877} |

These checks retain their reported scope. A context/allocation/retrieval check is not a general quality score or a speed qualification at that context. Exact flags and provenance are in [checks.json](../checks.json).

## Additional Test Results

| Result / Source | Profile | Evidence type | Reported outcome | Retained values | Configuration binding |
| --- | --- | --- | --- | --- | --- |
| [result-2733b226c154d5a6f6f0](../observations.json)<br>source-cf1d9416f4fb1e22d8f67a6d.json<br>`/` | [ad027-glm-mhc-10](ad027-glm-mhc-10.md) | performance detail | Pass | elapsed_seconds=210.06 s; end_to_end_accepted_tok_s=4.87 accepted tokens/s; ttft_seconds=195.26<br>198.89<br>200.01<br>200.01 s; p50_ms=36.77 ms; p95_ms=73.48 ms; cold_prefill: per-request 166.98 to 168.93 tokens/s; Draft accepted / proposed: 471 / 553 tokens; fraction 0.8517 | Recorded configuration/job |
| [result-58a0060a48a7169179c8](../observations.json)<br>source-cf1d9416f4fb1e22d8f67a6d.json<br>`/waves/0` | [ad027-glm-mhc-10](ad027-glm-mhc-10.md) | performance detail | Outcome unspecified | elapsed_seconds=210.06 s; end_to_end_accepted_tok_s=4.87 accepted tokens/s; output_tokens=256 tokens; ttft_seconds=195.26<br>198.89<br>200.01<br>200.01 s; p50_ms=36.77 ms; p95_ms=73.48 ms; prefill: per-request 166.98 to 168.93 tokens/s; Draft accepted / proposed: 471 / 553 tokens; fraction 0.8517 | Recorded configuration/job |
| [result-621db8d25c091839fea2](../observations.json)<br>source-43b4d9fd0306e68f09306093.json<br>`/` | [ad027-glm-mhc-10](ad027-glm-mhc-10.md) | performance detail | Pass | elapsed_seconds=209.48 s; end_to_end_accepted_tok_s=4.89 accepted tokens/s; ttft_seconds=192.60<br>197.40<br>199.20<br>199.20 s; p50_ms=37.34 ms; p95_ms=74.65 ms; cold_prefill: per-request 168.24 to 170.22 tokens/s; Draft accepted / proposed: 468 / 556 tokens; fraction 0.8417 | Recorded configuration/job |
| [result-af72af2f7c3b367652af](../observations.json)<br>source-ed21e72502f19e91fcf5b107.json<br>`/spec/serving_config` | [ad027-glm-mhc-10](ad027-glm-mhc-10.md) | context allocation | Outcome unspecified | cache_tokens=1,829,376 tokens; context=524,288 tokens; reserve_mib=2,048 MiB | Recorded configuration/job |
| [result-b3aae6d3503e3ad17332](../observations.json)<br>source-3f6203ee5fe06f6185c22639.json<br>`/` | [ad027-glm-mhc-10](ad027-glm-mhc-10.md) | performance detail | Pass | elapsed_seconds=54.81 s; end_to_end_accepted_tok_s=4.67 accepted tokens/s; ttft_seconds=49.79 s; p50_ms=18.95 ms; p95_ms=36.79 ms; cold_prefill: per-request 659.81 tokens/s; Draft accepted / proposed: 122 / 134 tokens; fraction 0.9104 | Recorded configuration/job |
| [result-b6e7762c0be506981559](../observations.json)<br>source-43b4d9fd0306e68f09306093.json<br>`/waves/0` | [ad027-glm-mhc-10](ad027-glm-mhc-10.md) | performance detail | Outcome unspecified | elapsed_seconds=209.48 s; end_to_end_accepted_tok_s=4.89 accepted tokens/s; output_tokens=256 tokens; ttft_seconds=192.60<br>197.40<br>199.20<br>199.20 s; p50_ms=37.34 ms; p95_ms=74.65 ms; prefill: per-request 168.24 to 170.22 tokens/s; Draft accepted / proposed: 468 / 556 tokens; fraction 0.8417 | Recorded configuration/job |
| [result-ee3cd0cd2140d6ee2d1a](../observations.json)<br>source-3f6203ee5fe06f6185c22639.json<br>`/waves/0` | [ad027-glm-mhc-10](ad027-glm-mhc-10.md) | performance detail | Outcome unspecified | elapsed_seconds=54.81 s; end_to_end_accepted_tok_s=4.67 accepted tokens/s; output_tokens=256 tokens; ttft_seconds=49.79 s; p50_ms=18.95 ms; p95_ms=36.79 ms; prefill: per-request 659.81 tokens/s; Draft accepted / proposed: 122 / 134 tokens; fraction 0.9104 | Recorded configuration/job |

These are saved result records, including failures and bounded checks. Copies, individual requests, report summaries and regrading can overlap; their counts are not independent test repetitions. Open each result for exact values, units, configuration binding and source receipts.

There are 1 retained lifecycle records. Their states, exit codes and configuration IDs remain in [catalog.json](../catalog.json); they do not supply missing benchmark results.

[Full archive](../../README.md) | [All retained waves](../RESULTS.md) | [Data definitions](../DATA.md) | [Recommended recipes](../../../README.md)
