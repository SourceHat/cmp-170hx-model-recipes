# ad027-strata-q4-single-13

**Historical record. Decode interval measured.**

Model family: Other model workflows.

Historical configurations are provided for comparison. The [recommended recipes](../../../README.md) include supported launch scripts.

## Saved Configuration Versions

Each configuration ID identifies a distinct original settings record. Deployment fields are omitted; versions can have identical published settings after that omission. Upstream runtime commits remain unspecified where the source retained only an integration label.

| Configuration | Recorded artifact / source | Configured card counts | Context tokens | GPU pool tokens | Slots | Draft mode / tokens |
| --- | --- | --- | --- | --- | --- | --- |
| cfg-e69c8c0bd7bd17e89d6d | trial-strata-q4-single | 1 | Not recorded | Not recorded | Not recorded | unspecified / - |

Card counts are saved configuration choices, not a claim that every allowed placement was measured. A derived view can differ from its pinned download source.

<details>
<summary>cfg-e69c8c0bd7bd17e89d6d</summary>

```json
{
  "kind": "command",
  "gpu_counts": [
    1
  ],
  "power_watts": 200,
  "host_memory_gib": 0,
  "host_swap_gib": 0,
  "min_vram_mib_per_gpu": 65530,
  "min_effective_vram_mib": 65530,
  "model_repository": null,
  "model_revision": null,
  "draft_repository": null,
  "draft_revision": null,
  "recorded_runtime_label": null,
  "served_model_label": "trial-strata-q4-single",
  "recorded_wrapper_settings": {
    "kind": "strata",
    "context": 262144,
    "max_sessions": 8,
    "kv_dtype": "int8",
    "draft_tokens": 3
  }
}
```

Pinned model revision recorded: no. Source receipt labels, hashes and object locators are retained in [configurations.json](../configurations.json).

</details>

## Retained Measurements

| Profile / Wave | Layout; Draft / Tokens | Requests | Input tokens/request | Accepted output tokens/request | Cache / Reused input tokens | Context / GPU pool tokens | Shared decode tok/s total | Client after-first-token estimate tok/s | Whole-wave output tok/s | Median TTFT, s | Source report |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [ad027-strata-q4-single-13](ad027-strata-q4-single-13.md)<br>wave-4e9f1953b74656183113 | layout unspecified; draft unspecified / - | 8 | 32,770 | 256 (budget 256) | cold; reused 0 | - / - | Not recorded | Not recorded | 6.32 | 177.69 | Pass |
| [ad027-strata-q4-single-13](ad027-strata-q4-single-13.md)<br>wave-7da544fa27ae10c0f29c | layout unspecified; draft unspecified / - | 1 | 32,769 | 256 (budget 256) | cold; reused 0 | - / - | 67.63 | Not recorded | 6.54 | 35.34 | Pass |

Rates are whole-wave totals over the stated request count. A wave may span multiple independent model instances; [measurements.json](../measurements.json) retains their contributions and the exact configuration IDs. Do not interpret a multi-instance total as one card's rate.

A dash in shared decode means no qualified synchronized interval is available. Whole-wave throughput includes prefill and queueing. A valid decode interval can survive inside an overall failed or partial check; the source-report outcome is preserved. No rows are averaged.

## Bounded Checks

| Check | Reported outcome | Retained counts / flags |
| --- | --- | --- |
| check-657756e0cc01ff51ef9f | Pass | {"passed":true,"elapsed_seconds":323.9966261840018,"ttft_seconds":[36.12453158100834,238.71170867199544,76.56409317799262,116.97093970100104,198.03593590100354,157.3538816710061,319.52860251799575,279.12148164000246],"end_to_end_accepted_tok_s":6.321053475528831} |
| check-abe4b201db48349b8754 | Pass | {"passed":true,"elapsed_seconds":39.115961050993064,"ttft_seconds":[35.34489375600242],"end_to_end_accepted_tok_s":6.544642982599062} |

These checks retain their reported scope. A context/allocation/retrieval check is not a general quality score or a speed qualification at that context. Exact flags and provenance are in [checks.json](../checks.json).

## Additional Test Results

| Result / Source | Profile | Evidence type | Reported outcome | Retained values | Configuration binding |
| --- | --- | --- | --- | --- | --- |
| [result-17b626deb367c4101f93](../observations.json)<br>source-3dbc53fe958c3cf088aab4d7.json<br>`/` | [ad027-strata-q4-single-13](ad027-strata-q4-single-13.md) | test outcome | complete | generated_tokens=256 accepted tokens | Recorded configuration/job |
| [result-2aecaad2f20d407125f2](../observations.json)<br>source-6cbc5bd0f5a5e22328ac184f.json<br>`/` | [ad027-strata-q4-single-13](ad027-strata-q4-single-13.md) | test outcome | complete | generated_tokens=256 accepted tokens | Recorded configuration/job |
| [result-2d72260c6f4069172d2a](../observations.json)<br>source-ed21e72502f19e91fcf5b107.json<br>`/spec/serving_config` | [ad027-strata-q4-single-1](ad027-strata-q4-single-1.md)<br>[ad027-strata-q4-single-13](ad027-strata-q4-single-13.md) | test outcome | Outcome unspecified | context=262,144 tokens | Recorded configuration/job |
| [result-3bda79915731fb4b1fb1](../observations.json)<br>source-a0219c290ebd38ae53983154.json<br>`/` | [ad027-strata-q4-single-13](ad027-strata-q4-single-13.md) | test outcome | complete | generated_tokens=256 accepted tokens | Recorded configuration/job |
| [result-579488c4edd3f93a34b8](../observations.json)<br>source-b01687f17b201e6c4b73bd05.json<br>`/` | [ad027-strata-q4-single-13](ad027-strata-q4-single-13.md) | test outcome | complete | generated_tokens=256 accepted tokens | Recorded configuration/job |
| [result-5e1150f8aa2196454804](../observations.json)<br>source-3f6203ee5fe06f6185c22639.json<br>`/` | [ad027-strata-q4-single-13](ad027-strata-q4-single-13.md) | performance detail | Pass | elapsed_seconds=39.12 s; end_to_end_accepted_tok_s=6.54 accepted tokens/s; ttft_seconds=35.34 s; p50_ms=0.07 ms; p95_ms=56.72 ms; cold_prefill: per-request 928.03 tokens/s; Draft accepted / proposed: 160 / 233 tokens; fraction 0.6867 | Recorded configuration/job |
| [result-6cf947be930c7a9eaf01](../observations.json)<br>source-3f6203ee5fe06f6185c22639.json<br>`/waves/0` | [ad027-strata-q4-single-13](ad027-strata-q4-single-13.md) | performance detail | Outcome unspecified | elapsed_seconds=39.12 s; end_to_end_accepted_tok_s=6.54 accepted tokens/s; output_tokens=256 tokens; ttft_seconds=35.34 s; p50_ms=0.07 ms; p95_ms=56.72 ms; prefill: per-request 928.03 tokens/s; Draft accepted / proposed: 160 / 233 tokens; fraction 0.6867 | Recorded configuration/job |
| [result-728d3e9d126224ec3755](../observations.json)<br>source-a430dda9cd101ebe6523f5c9.json<br>`/` | [ad027-strata-q4-single-13](ad027-strata-q4-single-13.md) | test outcome | complete | generated_tokens=256 accepted tokens | Recorded configuration/job |
| [result-7f44d1d01042631e32df](../observations.json)<br>source-cf1d9416f4fb1e22d8f67a6d.json<br>`/` | [ad027-strata-q4-single-13](ad027-strata-q4-single-13.md) | performance detail | Pass | elapsed_seconds=324.00 s; end_to_end_accepted_tok_s=6.32 accepted tokens/s; ttft_seconds=36.12<br>238.71<br>76.56<br>116.97<br>198.04<br>157.35<br>319.53<br>279.12 s; p50_ms=17.65 ms; p95_ms=29.84 ms; cold_prefill: per-request 820.84 to 1,590,776.70 tokens/s; Draft accepted / proposed: 146 / 241 tokens; fraction 0.6058 | Recorded configuration/job |
| [result-a929b67da9eeb88aec37](../observations.json)<br>source-b363969942ee39b61a66dc3c.json<br>`/` | [ad027-strata-q4-single-13](ad027-strata-q4-single-13.md) | test outcome | complete | generated_tokens=256 accepted tokens | Recorded configuration/job |
| [result-ad0e2219fc99526ab9ad](../observations.json)<br>source-cc002b4c5dbf14b5935b34e4.json<br>`/` | [ad027-strata-q4-single-13](ad027-strata-q4-single-13.md) | test outcome | complete | generated_tokens=256 accepted tokens | Recorded configuration/job |
| [result-b271fbae9370dce34b59](../observations.json)<br>source-0c91b6b81fa0055b4a662e24.json<br>`/` | [ad027-strata-q4-single-13](ad027-strata-q4-single-13.md) | test outcome | complete | generated_tokens=256 accepted tokens | Recorded configuration/job |
| [result-c0bfc9c31676f678dcec](../observations.json)<br>source-cf1d9416f4fb1e22d8f67a6d.json<br>`/waves/0` | [ad027-strata-q4-single-13](ad027-strata-q4-single-13.md) | performance detail | Outcome unspecified | elapsed_seconds=324.00 s; end_to_end_accepted_tok_s=6.32 accepted tokens/s; output_tokens=256 tokens; ttft_seconds=36.12<br>238.71<br>76.56<br>116.97<br>198.04<br>157.35<br>319.53<br>279.12 s; p50_ms=17.65 ms; p95_ms=29.84 ms; prefill: per-request 820.84 to 1,590,776.70 tokens/s; Draft accepted / proposed: 146 / 241 tokens; fraction 0.6058 | Recorded configuration/job |
| [result-f684dfc54a1aa033289c](../observations.json)<br>source-db25c3b281a04216b34607cf.json<br>`/` | [ad027-strata-q4-single-13](ad027-strata-q4-single-13.md) | test outcome | complete | generated_tokens=256 accepted tokens | Recorded configuration/job |

These are saved result records, including failures and bounded checks. Copies, individual requests, report summaries and regrading can overlap; their counts are not independent test repetitions. Open each result for exact values, units, configuration binding and source receipts.

There are 1 retained lifecycle records. Their states, exit codes and configuration IDs remain in [catalog.json](../catalog.json); they do not supply missing benchmark results.

[Full archive](../../README.md) | [All retained waves](../RESULTS.md) | [Data definitions](../DATA.md) | [Recommended recipes](../../../README.md)
