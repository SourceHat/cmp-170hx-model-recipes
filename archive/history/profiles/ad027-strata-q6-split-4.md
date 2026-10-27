# ad027-strata-q6-split-4

**Historical record. Decode interval measured.**

Model family: Other model workflows.

Historical configurations are provided for comparison. The [recommended recipes](../../../README.md) include supported launch scripts.

## Saved Configuration Versions

Each configuration ID identifies a distinct original settings record. Deployment fields are omitted; versions can have identical published settings after that omission. Upstream runtime commits remain unspecified where the source retained only an integration label.

| Configuration | Recorded artifact / source | Configured card counts | Context tokens | GPU pool tokens | Slots | Draft mode / tokens |
| --- | --- | --- | --- | --- | --- | --- |
| cfg-67c1e9e48b12abb84b21 | trial-strata-q6-split | 2 | Not recorded | Not recorded | Not recorded | unspecified / - |

Card counts are saved configuration choices, not a claim that every allowed placement was measured. A derived view can differ from its pinned download source.

<details>
<summary>cfg-67c1e9e48b12abb84b21</summary>

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
  "served_model_label": "trial-strata-q6-split",
  "recorded_wrapper_settings": {
    "kind": "strata",
    "context": 262144,
    "max_sessions": 6,
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
| [ad027-strata-q6-split-4](ad027-strata-q6-split-4.md)<br>wave-3355f5ebba396ea0b356 | layout unspecified; draft unspecified / - | 6 | 32,770 | 256 (budget 256) | cold; reused 0 | - / - | 178.89 | Not recorded | 12.76 | 65.29 | Pass |
| [ad027-strata-q6-split-4](ad027-strata-q6-split-4.md)<br>wave-708eebd767c0cd27bc23 | layout unspecified; draft unspecified / - | 1 | 32,769 | 256 (budget 256) | cold; reused 0 | - / - | 85.43 | Not recorded | 12.02 | 18.31 | Pass |

Rates are whole-wave totals over the stated request count. A wave may span multiple independent model instances; [measurements.json](../measurements.json) retains their contributions and the exact configuration IDs. Do not interpret a multi-instance total as one card's rate.

A dash in shared decode means no qualified synchronized interval is available. Whole-wave throughput includes prefill and queueing. A valid decode interval can survive inside an overall failed or partial check; the source-report outcome is preserved. No rows are averaged.

## Bounded Checks

| Check | Reported outcome | Retained counts / flags |
| --- | --- | --- |
| check-082433ab2baeec00a2d4 | Pass | {"passed":true,"elapsed_seconds":21.298710470990045,"ttft_seconds":[18.30595663600252],"end_to_end_accepted_tok_s":12.019507018919542} |
| check-1fb2f3202461c481a5c6 | Pass | {"passed":true,"elapsed_seconds":120.33921011000348,"ttft_seconds":[37.400342905006255,18.757922756005428,74.58656735499972,93.191959615011,111.81588743599423,55.986597909010015],"end_to_end_accepted_tok_s":12.763919578630476} |

These checks retain their reported scope. A context/allocation/retrieval check is not a general quality score or a speed qualification at that context. Exact flags and provenance are in [checks.json](../checks.json).

## Additional Test Results

| Result / Source | Profile | Evidence type | Reported outcome | Retained values | Configuration binding |
| --- | --- | --- | --- | --- | --- |
| [result-32452c2375fb7f1c2692](../observations.json)<br>source-cf1d9416f4fb1e22d8f67a6d.json<br>`/` | [ad027-strata-q6-split-4](ad027-strata-q6-split-4.md) | performance detail | Pass | elapsed_seconds=120.34 s; end_to_end_accepted_tok_s=12.76 accepted tokens/s; ttft_seconds=37.40<br>18.76<br>74.59<br>93.19<br>111.82<br>55.99 s; p50_ms=31.94 ms; p95_ms=35.95 ms; cold_prefill: per-request 1,792.41 to 1,567,942.58 tokens/s; Draft accepted / proposed: 0 / 0 tokens; fraction - | Recorded configuration/job |
| [result-4298f864015e6fc76b3d](../observations.json)<br>source-2a77dcf0b9d27beb5122535c.json<br>`/` | [ad027-strata-q6-split-4](ad027-strata-q6-split-4.md) | test outcome | complete | generated_tokens=256 accepted tokens | Recorded configuration/job |
| [result-630bba23dc96d498b068](../observations.json)<br>source-8ad35fb376f3e6f2288ded8f.json<br>`/` | [ad027-strata-q6-split-4](ad027-strata-q6-split-4.md) | test outcome | complete | generated_tokens=256 accepted tokens | Recorded configuration/job |
| [result-640bec9dbcb1b9bf8292](../observations.json)<br>source-cf1d9416f4fb1e22d8f67a6d.json<br>`/waves/0` | [ad027-strata-q6-split-4](ad027-strata-q6-split-4.md) | performance detail | Outcome unspecified | elapsed_seconds=120.34 s; end_to_end_accepted_tok_s=12.76 accepted tokens/s; output_tokens=256 tokens; ttft_seconds=37.40<br>18.76<br>74.59<br>93.19<br>111.82<br>55.99 s; p50_ms=31.94 ms; p95_ms=35.95 ms; prefill: per-request 1,792.41 to 1,567,942.58 tokens/s; Draft accepted / proposed: 0 / 0 tokens; fraction - | Recorded configuration/job |
| [result-8026bdc05d6985d0d4fb](../observations.json)<br>source-e057d97adea5cf0d4cd8a9a5.json<br>`/` | [ad027-strata-q6-split-4](ad027-strata-q6-split-4.md) | test outcome | complete | generated_tokens=256 accepted tokens | Recorded configuration/job |
| [result-987035cb21c800ee8752](../observations.json)<br>source-3f6203ee5fe06f6185c22639.json<br>`/` | [ad027-strata-q6-split-4](ad027-strata-q6-split-4.md) | performance detail | Pass | elapsed_seconds=21.30 s; end_to_end_accepted_tok_s=12.02 accepted tokens/s; ttft_seconds=18.31 s; p50_ms=0.05 ms; p95_ms=35.97 ms; cold_prefill: per-request 1,793.62 tokens/s; Draft accepted / proposed: 161 / 218 tokens; fraction 0.7385 | Recorded configuration/job |
| [result-aaab8d900ca2ab35d80d](../observations.json)<br>source-28771ecda10b4e04f83daaed.json<br>`/` | [ad027-strata-q6-split-4](ad027-strata-q6-split-4.md) | test outcome | complete | generated_tokens=256 accepted tokens | Recorded configuration/job |
| [result-ae407002ccccdd519a31](../observations.json)<br>source-e623d410adbed029954c00e5.json<br>`/` | [ad027-strata-q6-split-4](ad027-strata-q6-split-4.md) | test outcome | complete | generated_tokens=256 accepted tokens | Recorded configuration/job |
| [result-b64d355f37ed9d6ca6c4](../observations.json)<br>source-3f6203ee5fe06f6185c22639.json<br>`/waves/0` | [ad027-strata-q6-split-4](ad027-strata-q6-split-4.md) | performance detail | Outcome unspecified | elapsed_seconds=21.30 s; end_to_end_accepted_tok_s=12.02 accepted tokens/s; output_tokens=256 tokens; ttft_seconds=18.31 s; p50_ms=0.05 ms; p95_ms=35.97 ms; prefill: per-request 1,793.62 tokens/s; Draft accepted / proposed: 161 / 218 tokens; fraction 0.7385 | Recorded configuration/job |
| [result-b6e4ff50bc1b7970d884](../observations.json)<br>source-7d27072524a4aa6504393937.json<br>`/` | [ad027-strata-q6-split-4](ad027-strata-q6-split-4.md) | test outcome | complete | generated_tokens=256 accepted tokens | Recorded configuration/job |
| [result-e1950d74845793709667](../observations.json)<br>source-ed21e72502f19e91fcf5b107.json<br>`/spec/serving_config` | [ad027-strata-q6-split-4](ad027-strata-q6-split-4.md) | test outcome | Outcome unspecified | context=262,144 tokens | Recorded configuration/job |
| [result-e744d029ec797431b639](../observations.json)<br>source-d3cebd41781f8b7696b0d598.json<br>`/` | [ad027-strata-q6-split-4](ad027-strata-q6-split-4.md) | test outcome | complete | generated_tokens=256 accepted tokens | Recorded configuration/job |

These are saved result records, including failures and bounded checks. Copies, individual requests, report summaries and regrading can overlap; their counts are not independent test repetitions. Open each result for exact values, units, configuration binding and source receipts.

There are 1 retained lifecycle records. Their states, exit codes and configuration IDs remain in [catalog.json](../catalog.json); they do not supply missing benchmark results.

[Full archive](../../README.md) | [All retained waves](../RESULTS.md) | [Data definitions](../DATA.md) | [Recommended recipes](../../../README.md)
