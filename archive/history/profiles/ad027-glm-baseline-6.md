# ad027-glm-baseline-6

**Historical record. Decode interval measured.**

Model family: GLM 5.3 Flash.

Historical configurations are provided for comparison. The [recommended recipes](../../../README.md) include supported launch scripts.

## Saved Configuration Versions

Each configuration ID identifies a distinct original settings record. Deployment fields are omitted; versions can have identical published settings after that omission. Upstream runtime commits remain unspecified where the source retained only an integration label.

| Configuration | Recorded artifact / source | Configured card counts | Context tokens | GPU pool tokens | Slots | Draft mode / tokens |
| --- | --- | --- | --- | --- | --- | --- |
| cfg-d6cd3d78dbeeb93fe96f | glm-5.3-flash | 3 | Not recorded | Not recorded | Not recorded | unspecified / - |
| cfg-dfed67ae16124df92383 | glm-5.3-flash | 3 | Not recorded | Not recorded | Not recorded | unspecified / - |

Card counts are saved configuration choices, not a claim that every allowed placement was measured. A derived view can differ from its pinned download source.

<details>
<summary>cfg-d6cd3d78dbeeb93fe96f</summary>

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
<summary>cfg-dfed67ae16124df92383</summary>

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
| [ad027-glm-baseline-6](ad027-glm-baseline-6.md)<br>wave-045d9d837b712af917c8 | layout unspecified; draft unspecified / - | 1 | 32,766 | 256 (budget 256) | cold; reused 0 | - / - | 48.36 | Not recorded | 4.59 | 50.58 | Pass |
| [ad027-glm-baseline-6](ad027-glm-baseline-6.md)<br>wave-d79402d7515699043dd3 | layout unspecified; draft unspecified / - | 4 | 32,767 | 256 (budget 256) | cold; reused 0 | - / - | 100.65 | Not recorded | 4.88 | 199.02 | Pass |

Rates are whole-wave totals over the stated request count. A wave may span multiple independent model instances; [measurements.json](../measurements.json) retains their contributions and the exact configuration IDs. Do not interpret a multi-instance total as one card's rate.

A dash in shared decode means no qualified synchronized interval is available. Whole-wave throughput includes prefill and queueing. A valid decode interval can survive inside an overall failed or partial check; the source-report outcome is preserved. No rows are averaged.

## Bounded Checks

| Check | Reported outcome | Retained counts / flags |
| --- | --- | --- |
| check-0b576f8724db6a68140a | Pass | {"passed":true,"elapsed_seconds":55.816938199001015,"ttft_seconds":[50.58394586099894],"end_to_end_accepted_tok_s":4.586421402895613} |
| check-29ff48157111c2d37b48 | Pass | {"passed":true,"elapsed_seconds":209.77896015900478,"ttft_seconds":[194.74106964601378,198.3837893680029,199.6572132250003,199.65686144999927],"end_to_end_accepted_tok_s":4.881328419322155} |

These checks retain their reported scope. A context/allocation/retrieval check is not a general quality score or a speed qualification at that context. Exact flags and provenance are in [checks.json](../checks.json).

## Additional Test Results

| Result / Source | Profile | Evidence type | Reported outcome | Retained values | Configuration binding |
| --- | --- | --- | --- | --- | --- |
| [result-1fdfcdc9e1158f751192](../observations.json)<br>source-3f6203ee5fe06f6185c22639.json<br>`/waves/0` | [ad027-glm-baseline-6](ad027-glm-baseline-6.md) | performance detail | Outcome unspecified | elapsed_seconds=55.82 s; end_to_end_accepted_tok_s=4.59 accepted tokens/s; output_tokens=256 tokens; ttft_seconds=50.58 s; p50_ms=19.67 ms; p95_ms=37.91 ms; prefill: per-request 648.96 tokens/s; Draft accepted / proposed: 122 / 134 tokens; fraction 0.9104 | Recorded configuration/job |
| [result-240b40a56fc49d533657](../observations.json)<br>source-cf1d9416f4fb1e22d8f67a6d.json<br>`/` | [ad027-glm-baseline-6](ad027-glm-baseline-6.md) | performance detail | Pass | elapsed_seconds=209.78 s; end_to_end_accepted_tok_s=4.88 accepted tokens/s; ttft_seconds=194.74<br>198.38<br>199.66<br>199.66 s; p50_ms=36.76 ms; p95_ms=72.50 ms; cold_prefill: per-request 168.15 to 170.41 tokens/s; Draft accepted / proposed: 471 / 553 tokens; fraction 0.8517 | Recorded configuration/job |
| [result-c060f356d4cbad42063d](../observations.json)<br>source-3f6203ee5fe06f6185c22639.json<br>`/` | [ad027-glm-baseline-6](ad027-glm-baseline-6.md) | performance detail | Pass | elapsed_seconds=55.82 s; end_to_end_accepted_tok_s=4.59 accepted tokens/s; ttft_seconds=50.58 s; p50_ms=19.67 ms; p95_ms=37.91 ms; cold_prefill: per-request 648.96 tokens/s; Draft accepted / proposed: 122 / 134 tokens; fraction 0.9104 | Recorded configuration/job |
| [result-f82defc4c51e5ed44050](../observations.json)<br>source-ed21e72502f19e91fcf5b107.json<br>`/spec/serving_config` | [ad027-glm-baseline-6](ad027-glm-baseline-6.md) | context allocation | Outcome unspecified | cache_tokens=1,829,376 tokens; context=524,288 tokens; reserve_mib=2,048 MiB | Recorded configuration/job |
| [result-fd8629d2aa85fbd3c91c](../observations.json)<br>source-cf1d9416f4fb1e22d8f67a6d.json<br>`/waves/0` | [ad027-glm-baseline-6](ad027-glm-baseline-6.md) | performance detail | Outcome unspecified | elapsed_seconds=209.78 s; end_to_end_accepted_tok_s=4.88 accepted tokens/s; output_tokens=256 tokens; ttft_seconds=194.74<br>198.38<br>199.66<br>199.66 s; p50_ms=36.76 ms; p95_ms=72.50 ms; prefill: per-request 168.15 to 170.41 tokens/s; Draft accepted / proposed: 471 / 553 tokens; fraction 0.8517 | Recorded configuration/job |

These are saved result records, including failures and bounded checks. Copies, individual requests, report summaries and regrading can overlap; their counts are not independent test repetitions. Open each result for exact values, units, configuration binding and source receipts.

There are 1 retained lifecycle records. Their states, exit codes and configuration IDs remain in [catalog.json](../catalog.json); they do not supply missing benchmark results.

[Full archive](../../README.md) | [All retained waves](../RESULTS.md) | [Data definitions](../DATA.md) | [Recommended recipes](../../../README.md)
