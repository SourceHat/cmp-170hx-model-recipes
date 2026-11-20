# ad027-apex-baseline-11

**Historical record. Decode interval measured.**

Model family: Apex Flash 1 (GLM 5.3 Flash post-train).

Historical configurations are provided for comparison. The [recommended recipes](../../../README.md) include supported launch scripts.

## Saved Configuration Versions

Each configuration ID identifies a distinct original settings record. Deployment fields are omitted; versions can have identical published settings after that omission. Upstream runtime commits remain unspecified where the source retained only an integration label.

| Configuration | Recorded artifact / source | Configured card counts | Context tokens | GPU pool tokens | Slots | Draft mode / tokens |
| --- | --- | --- | --- | --- | --- | --- |
| cfg-140c508716da6730e616 | apex-flash-1-abliterated-exl3-4bit-spark | 3 | Not recorded | Not recorded | Not recorded | unspecified / - |
| cfg-dbf720d2b1d05d4b4629 | apex-flash-1-abliterated-exl3-4bit-spark | 3 | Not recorded | Not recorded | Not recorded | unspecified / - |

Card counts are saved configuration choices, not a claim that every allowed placement was measured. A derived view can differ from its pinned download source.

<details>
<summary>cfg-140c508716da6730e616</summary>

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
<summary>cfg-dbf720d2b1d05d4b4629</summary>

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
| [ad027-apex-baseline-11](ad027-apex-baseline-11.md)<br>wave-01cd9bdd22ad277c4b7c | layout unspecified; draft unspecified / - | 1 | 32,766 | 256 (budget 256) | cold; reused 0 | - / - | 40.09 | Not recorded | 4.50 | 50.61 | Pass |
| [ad027-apex-baseline-11](ad027-apex-baseline-11.md)<br>wave-233f17641e1d5b47b3bf | layout unspecified; draft unspecified / - | 4 | 32,767 | 256 (budget 256) | cold; reused 0 | - / - | 98.49 | Not recorded | 4.82 | 202.01 | Pass |

Rates are whole-wave totals over the stated request count. A wave may span multiple independent model instances; [measurements.json](../measurements.json) retains their contributions and the exact configuration IDs. Do not interpret a multi-instance total as one card's rate.

A dash in shared decode means no qualified synchronized interval is available. Whole-wave throughput includes prefill and queueing. A valid decode interval can survive inside an overall failed or partial check; the source-report outcome is preserved. No rows are averaged.

## Bounded Checks

| Check | Reported outcome | Retained counts / flags |
| --- | --- | --- |
| check-325c4c9aaa506b188173 | Pass | {"passed":true,"elapsed_seconds":212.42050826399645,"ttft_seconds":[198.88281159300823,202.01556846300082,202.01481138399686,202.01447941199876],"end_to_end_accepted_tok_s":4.820626823505062} |
| check-b486cad81af0db7e5956 | Pass | {"passed":true,"elapsed_seconds":56.926106443002936,"ttft_seconds":[50.61319486699358],"end_to_end_accepted_tok_s":4.497057958044594} |

These checks retain their reported scope. A context/allocation/retrieval check is not a general quality score or a speed qualification at that context. Exact flags and provenance are in [checks.json](../checks.json).

## Additional Test Results

| Result / Source | Profile | Evidence type | Reported outcome | Retained values | Configuration binding |
| --- | --- | --- | --- | --- | --- |
| [result-3fc9ad5dca184725bd49](../observations.json)<br>source-ed21e72502f19e91fcf5b107.json<br>`/spec/serving_config` | [ad027-apex-baseline-11](ad027-apex-baseline-11.md) | context allocation | Outcome unspecified | cache_tokens=1,083,136 tokens; context=524,288 tokens; reserve_mib=2,048 MiB | Recorded configuration/job |
| [result-7526669f1bd48161a506](../observations.json)<br>source-cf1d9416f4fb1e22d8f67a6d.json<br>`/` | [ad027-apex-baseline-11](ad027-apex-baseline-11.md) | performance detail | Pass | elapsed_seconds=212.42 s; end_to_end_accepted_tok_s=4.82 accepted tokens/s; ttft_seconds=198.88<br>202.02<br>202.01<br>202.01 s; p50_ms=36.80 ms; p95_ms=74.16 ms; cold_prefill: per-request 164.51 to 165.87 tokens/s; Draft accepted / proposed: 463 / 561 tokens; fraction 0.8253 | Recorded configuration/job |
| [result-93c7c0713bc2e61e5798](../observations.json)<br>source-3f6203ee5fe06f6185c22639.json<br>`/waves/0` | [ad027-apex-baseline-11](ad027-apex-baseline-11.md) | performance detail | Outcome unspecified | elapsed_seconds=56.93 s; end_to_end_accepted_tok_s=4.50 accepted tokens/s; output_tokens=256 tokens; ttft_seconds=50.61 s; p50_ms=22.82 ms; p95_ms=45.44 ms; prefill: per-request 648.57 tokens/s; Draft accepted / proposed: 116 / 140 tokens; fraction 0.8286 | Recorded configuration/job |
| [result-eb7ce78206491dce5cf4](../observations.json)<br>source-cf1d9416f4fb1e22d8f67a6d.json<br>`/waves/0` | [ad027-apex-baseline-11](ad027-apex-baseline-11.md) | performance detail | Outcome unspecified | elapsed_seconds=212.42 s; end_to_end_accepted_tok_s=4.82 accepted tokens/s; output_tokens=256 tokens; ttft_seconds=198.88<br>202.02<br>202.01<br>202.01 s; p50_ms=36.80 ms; p95_ms=74.16 ms; prefill: per-request 164.51 to 165.87 tokens/s; Draft accepted / proposed: 463 / 561 tokens; fraction 0.8253 | Recorded configuration/job |
| [result-f7ba5afef7d8cbd613e9](../observations.json)<br>source-3f6203ee5fe06f6185c22639.json<br>`/` | [ad027-apex-baseline-11](ad027-apex-baseline-11.md) | performance detail | Pass | elapsed_seconds=56.93 s; end_to_end_accepted_tok_s=4.50 accepted tokens/s; ttft_seconds=50.61 s; p50_ms=22.82 ms; p95_ms=45.44 ms; cold_prefill: per-request 648.57 tokens/s; Draft accepted / proposed: 116 / 140 tokens; fraction 0.8286 | Recorded configuration/job |

These are saved result records, including failures and bounded checks. Copies, individual requests, report summaries and regrading can overlap; their counts are not independent test repetitions. Open each result for exact values, units, configuration binding and source receipts.

There are 1 retained lifecycle records. Their states, exit codes and configuration IDs remain in [catalog.json](../catalog.json); they do not supply missing benchmark results.

[Full archive](../../README.md) | [All retained waves](../RESULTS.md) | [Data definitions](../DATA.md) | [Recommended recipes](../../../README.md)
