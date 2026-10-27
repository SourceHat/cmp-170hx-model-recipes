# ad001-glm-mtp3-original-layer_split-matched-070

**Historical record. Decode interval measured.**

Model family: GLM 5.3 Flash.

Historical configurations are provided for comparison. The [recommended recipes](../../../README.md) include supported launch scripts.

Current recipes using the same recorded checkpoint repository: [glm-5.3-flash-mtp1-tp3](../../../recipes/glm-5.3-flash-mtp1-tp3/README.md). Context, cache and runtime versions can differ.

## Saved Configuration Versions

Each configuration ID identifies a distinct original settings record. Deployment fields are omitted; versions can have identical published settings after that omission. Upstream runtime commits remain unspecified where the source retained only an integration label.

| Configuration | Recorded artifact / source | Configured card counts | Context tokens | GPU pool tokens | Slots | Draft mode / tokens |
| --- | --- | --- | --- | --- | --- | --- |
| cfg-9463d7bf59a3d2bba881 | [turboderp/GLM-5.3-Flash-exl3@2a30229e67](https://huggingface.co/turboderp/GLM-5.3-Flash-exl3/tree/2a30229e67012798ba9f0cd832bb78abf4c363d5) | 3 | 262,144 | 262,144 | 4 | mtp / 3 |

Card counts are saved configuration choices, not a claim that every allowed placement was measured. A derived view can differ from its pinned download source.

<details>
<summary>cfg-9463d7bf59a3d2bba881</summary>

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
  "model_repository": "turboderp/GLM-5.3-Flash-exl3",
  "model_revision": "2a30229e67012798ba9f0cd832bb78abf4c363d5",
  "draft_repository": null,
  "draft_revision": null,
  "recorded_runtime_label": null,
  "served_model_label": "glm-5.3-flash"
}
```

Pinned model revision recorded: yes. Source receipt labels, hashes and object locators are retained in [configurations.json](../configurations.json).

</details>

## Retained Measurements

| Profile / Wave | Layout; Draft / Tokens | Requests | Input tokens/request | Accepted output tokens/request | Cache / Reused input tokens | Context / GPU pool tokens | Shared decode tok/s total | Client after-first-token estimate tok/s | Whole-wave output tok/s | Median TTFT, s | Source report |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [ad001-glm-mtp3-original-layer_split-matched-070](ad001-glm-mtp3-original-layer_split-matched-070.md)<br>wave-52d3d67f9de414d43292 | layer_split; mtp / 3 | 1 | 32,766 | 256 (budget 256) | cached_prefix; reused 32,512 | 262,144 / 262,144 | 45.89 | Not recorded | 41.08 | 0.78 | Pass |
| [ad001-glm-mtp3-original-layer_split-matched-070](ad001-glm-mtp3-original-layer_split-matched-070.md)<br>wave-7a962c3145a533401fac | layer_split; mtp / 3 | 4 | 32,767 | 256 (budget 256) | cached_prefix; reused 32,512 | 262,144 / 262,144 | 52.78 | Not recorded | 47.31 | 2.86 | Pass |
| [ad001-glm-mtp3-original-layer_split-matched-070](ad001-glm-mtp3-original-layer_split-matched-070.md)<br>wave-8967c5b01d794e64006d | layer_split; mtp / 3 | 4 | 32,767 | 256 (budget 256) | cold; reused 0 | 262,144 / 262,144 | 52.30 | Not recorded | 5.86 | 155.43 | Pass |
| [ad001-glm-mtp3-original-layer_split-matched-070](ad001-glm-mtp3-original-layer_split-matched-070.md)<br>wave-e69bc931ec46fad8e59f | layer_split; mtp / 3 | 1 | 32,766 | 256 (budget 256) | cold; reused 0 | 262,144 / 262,144 | 44.70 | Not recorded | 5.77 | 38.74 | Pass |

Rates are whole-wave totals over the stated request count. A wave may span multiple independent model instances; [measurements.json](../measurements.json) retains their contributions and the exact configuration IDs. Do not interpret a multi-instance total as one card's rate.

A dash in shared decode means no qualified synchronized interval is available. Whole-wave throughput includes prefill and queueing. A valid decode interval can survive inside an overall failed or partial check; the source-report outcome is preserved. No rows are averaged.

## Bounded Checks

| Check | Reported outcome | Retained counts / flags |
| --- | --- | --- |
| check-1bbf51fcb2d339108f92 | Pass | {"passed":true,"elapsed_seconds":44.34744192999642,"ttft_seconds":[38.74068538899883],"end_to_end_accepted_tok_s":5.772599023955037} |
| check-81eb07a3899c6eeb98f6 | Pass | {"passed":true,"elapsed_seconds":44.34744192999642,"ttft_seconds":[38.74068538899883],"end_to_end_accepted_tok_s":5.772599023955037} |
| check-a8bf4bd6599726b86b69 | Pass | {"passed":true,"elapsed_seconds":174.64370238400443,"ttft_seconds":[151.13140316800127,155.43248449000384,155.43199203000404,155.431632161999],"end_to_end_accepted_tok_s":5.863366305350315} |
| check-ca83abe864fabdd2cdb9 | Pass | {"passed":true,"elapsed_seconds":174.64370238400443,"ttft_seconds":[151.13140316800127,155.43248449000384,155.43199203000404,155.431632161999],"end_to_end_accepted_tok_s":5.863366305350315} |

These checks retain their reported scope. A context/allocation/retrieval check is not a general quality score or a speed qualification at that context. Exact flags and provenance are in [checks.json](../checks.json).

## Additional Test Results

| Result / Source | Profile | Evidence type | Reported outcome | Retained values | Configuration binding |
| --- | --- | --- | --- | --- | --- |
| [result-32d4b627ab214d9a2097](../observations.json)<br>source-a9e622d351a86c8b776605d4.json<br>`/managed_phase_timings/70` | [ad001-glm-mtp3-original-layer_split-matched-070](ad001-glm-mtp3-original-layer_split-matched-070.md) | test outcome | Outcome unspecified | wall_seconds=615.64 s | Recorded configuration/job |
| [result-39a9b69592fa6f9ab148](../observations.json)<br>source-0f44c02427debeb164391191.json<br>`/` | [ad001-glm-mtp3-original-layer_split-matched-070](ad001-glm-mtp3-original-layer_split-matched-070.md)<br>[record-26c850ec689cf58c6b67](record-26c850ec689cf58c6b67.md)<br>[glm-mtp3-original-layer_split](glm-mtp3-original-layer_split.md) | performance detail | Pass | elapsed_seconds=174.64 s; end_to_end_accepted_tok_s=5.86 accepted tokens/s; ttft_seconds=151.13<br>155.43<br>155.43<br>155.43 s; p50_ms=73.94 ms; p95_ms=226.76 ms; cold_prefill: per-request 215.70 to 218.46 tokens/s; Draft accepted / proposed: 667 / 1,071 tokens; fraction 0.6228 | Recorded configuration/job |
| [result-696e7d745b34bcd8db04](../observations.json)<br>source-d5f3db1afa64245fae9b8070.json<br>`/waves/0` | [ad001-glm-mtp3-original-layer_split-matched-070](ad001-glm-mtp3-original-layer_split-matched-070.md)<br>[record-26c850ec689cf58c6b67](record-26c850ec689cf58c6b67.md)<br>[glm-mtp3-original-layer_split](glm-mtp3-original-layer_split.md) | performance detail | Outcome unspecified | elapsed_seconds=44.35 s; end_to_end_accepted_tok_s=5.77 accepted tokens/s; output_tokens=256 tokens; ttft_seconds=38.74 s; p50_ms=22.16 ms; p95_ms=66.01 ms; prefill: per-request 849.74 tokens/s; Draft accepted / proposed: 169 / 261 tokens; fraction 0.6475 | Recorded configuration/job |
| [result-7febe760589f688ff097](../observations.json)<br>source-d5f3db1afa64245fae9b8070.json<br>`/waves/1` | [ad001-glm-mtp3-original-layer_split-matched-070](ad001-glm-mtp3-original-layer_split-matched-070.md)<br>[record-26c850ec689cf58c6b67](record-26c850ec689cf58c6b67.md)<br>[glm-mtp3-original-layer_split](glm-mtp3-original-layer_split.md) | performance detail | Outcome unspecified | elapsed_seconds=6.23 s; end_to_end_accepted_tok_s=41.08 accepted tokens/s; output_tokens=256 tokens; ttft_seconds=0.78 s; p50_ms=21.79 ms; p95_ms=63.97 ms; prefill: per-request 488.46 tokens/s; Draft accepted / proposed: 170 / 258 tokens; fraction 0.6589 | Recorded configuration/job |
| [result-8833bba7ba7b1204d0b7](../observations.json)<br>source-0f44c02427debeb164391191.json<br>`/waves/1` | [ad001-glm-mtp3-original-layer_split-matched-070](ad001-glm-mtp3-original-layer_split-matched-070.md)<br>[record-26c850ec689cf58c6b67](record-26c850ec689cf58c6b67.md)<br>[glm-mtp3-original-layer_split](glm-mtp3-original-layer_split.md) | performance detail | Outcome unspecified | elapsed_seconds=21.64 s; end_to_end_accepted_tok_s=47.31 accepted tokens/s; output_tokens=256 tokens; ttft_seconds=0.90<br>2.86<br>2.86<br>2.86 s; p50_ms=73.94 ms; p95_ms=226.76 ms; prefill: per-request 283.33 to 566.67 tokens/s; Draft accepted / proposed: 667 / 1,071 tokens; fraction 0.6228 | Recorded configuration/job |
| [result-9a3a4146fb21231cfb89](../observations.json)<br>source-d5f3db1afa64245fae9b8070.json<br>`/` | [ad001-glm-mtp3-original-layer_split-matched-070](ad001-glm-mtp3-original-layer_split-matched-070.md)<br>[record-26c850ec689cf58c6b67](record-26c850ec689cf58c6b67.md)<br>[glm-mtp3-original-layer_split](glm-mtp3-original-layer_split.md) | performance detail | Pass | elapsed_seconds=44.35 s; end_to_end_accepted_tok_s=5.77 accepted tokens/s; ttft_seconds=38.74 s; p50_ms=21.79 ms; p95_ms=63.97 ms; cold_prefill: per-request 849.74 tokens/s; Draft accepted / proposed: 170 / 258 tokens; fraction 0.6589 | Recorded configuration/job |
| [result-a0c10f15d3a4c09fa97c](../observations.json)<br>source-0f44c02427debeb164391191.json<br>`/waves/0` | [ad001-glm-mtp3-original-layer_split-matched-070](ad001-glm-mtp3-original-layer_split-matched-070.md)<br>[record-26c850ec689cf58c6b67](record-26c850ec689cf58c6b67.md)<br>[glm-mtp3-original-layer_split](glm-mtp3-original-layer_split.md) | performance detail | Outcome unspecified | elapsed_seconds=174.64 s; end_to_end_accepted_tok_s=5.86 accepted tokens/s; output_tokens=256 tokens; ttft_seconds=151.13<br>155.43<br>155.43<br>155.43 s; p50_ms=68.54 ms; p95_ms=229.15 ms; prefill: per-request 215.70 to 218.46 tokens/s; Draft accepted / proposed: 668 / 1,068 tokens; fraction 0.6255 | Recorded configuration/job |

These are saved result records, including failures and bounded checks. Copies, individual requests, report summaries and regrading can overlap; their counts are not independent test repetitions. Open each result for exact values, units, configuration binding and source receipts.

There are 1 retained lifecycle records. Their states, exit codes and configuration IDs remain in [catalog.json](../catalog.json); they do not supply missing benchmark results.

[Full archive](../../README.md) | [All retained waves](../RESULTS.md) | [Data definitions](../DATA.md) | [Recommended recipes](../../../README.md)
