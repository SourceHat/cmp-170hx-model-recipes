# ad001-glm-mtp2-original-layer_split-matched-069

**Historical record. Decode interval measured.**

Model family: GLM 5.3 Flash.

Historical configurations are provided for comparison. The [recommended recipes](../../../README.md) include supported launch scripts.

Current recipes using the same recorded checkpoint repository: [glm-5.3-flash-mtp1-tp3](../../../recipes/glm-5.3-flash-mtp1-tp3/README.md). Context, cache and runtime versions can differ.

## Saved Configuration Versions

Each configuration ID identifies a distinct original settings record. Deployment fields are omitted; versions can have identical published settings after that omission. Upstream runtime commits remain unspecified where the source retained only an integration label.

| Configuration | Recorded artifact / source | Configured card counts | Context tokens | GPU pool tokens | Slots | Draft mode / tokens |
| --- | --- | --- | --- | --- | --- | --- |
| cfg-08beb7a92836ea1c765a | [turboderp/GLM-5.3-Flash-exl3@2a30229e67](https://huggingface.co/turboderp/GLM-5.3-Flash-exl3/tree/2a30229e67012798ba9f0cd832bb78abf4c363d5) | 3 | 262,144 | 262,144 | 4 | mtp / 2 |

Card counts are saved configuration choices, not a claim that every allowed placement was measured. A derived view can differ from its pinned download source.

<details>
<summary>cfg-08beb7a92836ea1c765a</summary>

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
  "draft_tokens": 2,
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
| [ad001-glm-mtp2-original-layer_split-matched-069](ad001-glm-mtp2-original-layer_split-matched-069.md)<br>wave-1543765460f5dc473d3a | layer_split; mtp / 2 | 1 | 32,766 | 256 (budget 256) | cached_prefix; reused 32,512 | 262,144 / 262,144 | 42.37 | Not recorded | 37.74 | 0.81 | Pass |
| [ad001-glm-mtp2-original-layer_split-matched-069](ad001-glm-mtp2-original-layer_split-matched-069.md)<br>wave-7ed583dfe61217a4892e | layer_split; mtp / 2 | 1 | 32,766 | 256 (budget 256) | cold; reused 0 | 262,144 / 262,144 | 41.30 | Not recorded | 5.57 | 39.81 | Pass |
| [ad001-glm-mtp2-original-layer_split-matched-069](ad001-glm-mtp2-original-layer_split-matched-069.md)<br>wave-abb42109512a16b04519 | layer_split; mtp / 2 | 4 | 32,767 | 256 (budget 256) | cold; reused 0 | 262,144 / 262,144 | 46.52 | Not recorded | 5.73 | 157.64 | Pass |
| [ad001-glm-mtp2-original-layer_split-matched-069](ad001-glm-mtp2-original-layer_split-matched-069.md)<br>wave-fc9696dd2229fe8b6331 | layer_split; mtp / 2 | 4 | 32,767 | 256 (budget 256) | cached_prefix; reused 32,512 | 262,144 / 262,144 | 47.28 | Not recorded | 41.97 | 2.95 | Pass |

Rates are whole-wave totals over the stated request count. A wave may span multiple independent model instances; [measurements.json](../measurements.json) retains their contributions and the exact configuration IDs. Do not interpret a multi-instance total as one card's rate.

A dash in shared decode means no qualified synchronized interval is available. Whole-wave throughput includes prefill and queueing. A valid decode interval can survive inside an overall failed or partial check; the source-report outcome is preserved. No rows are averaged.

## Bounded Checks

| Check | Reported outcome | Retained counts / flags |
| --- | --- | --- |
| check-098f56f0c139019e4014 | Pass | {"passed":true,"elapsed_seconds":178.86008862900053,"ttft_seconds":[150.94113877700147,157.36143263800477,157.90919254800247,157.90888563200133],"end_to_end_accepted_tok_s":5.725145323639115} |
| check-2aa22b2c679682a8ee18 | Pass | {"passed":true,"elapsed_seconds":178.86008862900053,"ttft_seconds":[150.94113877700147,157.36143263800477,157.90919254800247,157.90888563200133],"end_to_end_accepted_tok_s":5.725145323639115} |
| check-3d626e38887bddef3d4a | Pass | {"passed":true,"elapsed_seconds":45.938991435999924,"ttft_seconds":[39.81154948299809],"end_to_end_accepted_tok_s":5.572608191815603} |
| check-956f0f7f607c8312e266 | Pass | {"passed":true,"elapsed_seconds":45.938991435999924,"ttft_seconds":[39.81154948299809],"end_to_end_accepted_tok_s":5.572608191815603} |

These checks retain their reported scope. A context/allocation/retrieval check is not a general quality score or a speed qualification at that context. Exact flags and provenance are in [checks.json](../checks.json).

## Additional Test Results

| Result / Source | Profile | Evidence type | Reported outcome | Retained values | Configuration binding |
| --- | --- | --- | --- | --- | --- |
| [result-31a77e6937699e8ffe21](../observations.json)<br>source-87803c28fc1ff87bef832715.json<br>`/` | [ad001-glm-mtp2-original-layer_split-matched-069](ad001-glm-mtp2-original-layer_split-matched-069.md)<br>[record-26c850ec689cf58c6b67](record-26c850ec689cf58c6b67.md)<br>[glm-mtp2-original-layer_split](glm-mtp2-original-layer_split.md) | performance detail | Pass | elapsed_seconds=45.94 s; end_to_end_accepted_tok_s=5.57 accepted tokens/s; ttft_seconds=39.81 s; p50_ms=20.89 ms; p95_ms=60.39 ms; cold_prefill: per-request 826.38 tokens/s; Draft accepted / proposed: 152 / 208 tokens; fraction 0.7308 | Recorded configuration/job |
| [result-7ea294fe0ddbdfd2973a](../observations.json)<br>source-a9e622d351a86c8b776605d4.json<br>`/managed_phase_timings/69` | [ad001-glm-mtp2-original-layer_split-matched-069](ad001-glm-mtp2-original-layer_split-matched-069.md) | test outcome | Outcome unspecified | wall_seconds=584.74 s | Recorded configuration/job |
| [result-8d3b4e2eba8d64c6233a](../observations.json)<br>source-e64626d90a31fd410a677def.json<br>`/` | [ad001-glm-mtp2-original-layer_split-matched-069](ad001-glm-mtp2-original-layer_split-matched-069.md)<br>[record-26c850ec689cf58c6b67](record-26c850ec689cf58c6b67.md)<br>[glm-mtp2-original-layer_split](glm-mtp2-original-layer_split.md) | performance detail | Pass | elapsed_seconds=178.86 s; end_to_end_accepted_tok_s=5.73 accepted tokens/s; ttft_seconds=150.94<br>157.36<br>157.91<br>157.91 s; p50_ms=71.56 ms; p95_ms=208.12 ms; cold_prefill: per-request 214.43 to 217.26 tokens/s; Draft accepted / proposed: 594 / 860 tokens; fraction 0.6907 | Recorded configuration/job |
| [result-a6df6624b94a90d6fa06](../observations.json)<br>source-87803c28fc1ff87bef832715.json<br>`/waves/1` | [ad001-glm-mtp2-original-layer_split-matched-069](ad001-glm-mtp2-original-layer_split-matched-069.md)<br>[record-26c850ec689cf58c6b67](record-26c850ec689cf58c6b67.md)<br>[glm-mtp2-original-layer_split](glm-mtp2-original-layer_split.md) | performance detail | Outcome unspecified | elapsed_seconds=6.78 s; end_to_end_accepted_tok_s=37.74 accepted tokens/s; output_tokens=256 tokens; ttft_seconds=0.81 s; p50_ms=20.89 ms; p95_ms=60.39 ms; prefill: per-request 461.82 tokens/s; Draft accepted / proposed: 152 / 208 tokens; fraction 0.7308 | Recorded configuration/job |
| [result-ba57e975ad5f4edb191c](../observations.json)<br>source-e64626d90a31fd410a677def.json<br>`/waves/0` | [ad001-glm-mtp2-original-layer_split-matched-069](ad001-glm-mtp2-original-layer_split-matched-069.md)<br>[record-26c850ec689cf58c6b67](record-26c850ec689cf58c6b67.md)<br>[glm-mtp2-original-layer_split](glm-mtp2-original-layer_split.md) | performance detail | Outcome unspecified | elapsed_seconds=178.86 s; end_to_end_accepted_tok_s=5.73 accepted tokens/s; output_tokens=256 tokens; ttft_seconds=150.94<br>157.36<br>157.91<br>157.91 s; p50_ms=72.81 ms; p95_ms=207.95 ms; prefill: per-request 214.43 to 217.26 tokens/s; Draft accepted / proposed: 599 / 850 tokens; fraction 0.7047 | Recorded configuration/job |
| [result-d2ca8e81951ec3bcd1f2](../observations.json)<br>source-87803c28fc1ff87bef832715.json<br>`/waves/0` | [ad001-glm-mtp2-original-layer_split-matched-069](ad001-glm-mtp2-original-layer_split-matched-069.md)<br>[record-26c850ec689cf58c6b67](record-26c850ec689cf58c6b67.md)<br>[glm-mtp2-original-layer_split](glm-mtp2-original-layer_split.md) | performance detail | Outcome unspecified | elapsed_seconds=45.94 s; end_to_end_accepted_tok_s=5.57 accepted tokens/s; output_tokens=256 tokens; ttft_seconds=39.81 s; p50_ms=21.46 ms; p95_ms=61.23 ms; prefill: per-request 826.38 tokens/s; Draft accepted / proposed: 152 / 208 tokens; fraction 0.7308 | Recorded configuration/job |
| [result-f2d7fb34ffef0fdbb0cd](../observations.json)<br>source-e64626d90a31fd410a677def.json<br>`/waves/1` | [ad001-glm-mtp2-original-layer_split-matched-069](ad001-glm-mtp2-original-layer_split-matched-069.md)<br>[record-26c850ec689cf58c6b67](record-26c850ec689cf58c6b67.md)<br>[glm-mtp2-original-layer_split](glm-mtp2-original-layer_split.md) | performance detail | Outcome unspecified | elapsed_seconds=24.40 s; end_to_end_accepted_tok_s=41.97 accepted tokens/s; output_tokens=256 tokens; ttft_seconds=0.96<br>2.95<br>2.95<br>2.95 s; p50_ms=71.56 ms; p95_ms=208.12 ms; prefill: per-request 277.17 to 566.67 tokens/s; Draft accepted / proposed: 594 / 860 tokens; fraction 0.6907 | Recorded configuration/job |

These are saved result records, including failures and bounded checks. Copies, individual requests, report summaries and regrading can overlap; their counts are not independent test repetitions. Open each result for exact values, units, configuration binding and source receipts.

There are 1 retained lifecycle records. Their states, exit codes and configuration IDs remain in [catalog.json](../catalog.json); they do not supply missing benchmark results.

[Full archive](../../README.md) | [All retained waves](../RESULTS.md) | [Data definitions](../DATA.md) | [Recommended recipes](../../../README.md)
