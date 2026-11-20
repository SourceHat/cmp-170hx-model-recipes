# ad002-glm-dflash22-small_exl3-layer_split-matched-076

**Historical record. Decode interval measured.**

Model family: GLM 5.3 Flash.

Historical configurations are provided for comparison. The [recommended recipes](../../../README.md) include supported launch scripts.

Current recipes using the same recorded checkpoint repository: [glm-5.3-flash-mtp1-tp3](../../../recipes/glm-5.3-flash-mtp1-tp3/README.md). Context, cache and runtime versions can differ.

## Saved Configuration Versions

Each configuration ID identifies a distinct original settings record. Deployment fields are omitted; versions can have identical published settings after that omission. Upstream runtime commits remain unspecified where the source retained only an integration label.

| Configuration | Recorded artifact / source | Configured card counts | Context tokens | GPU pool tokens | Slots | Draft mode / tokens |
| --- | --- | --- | --- | --- | --- | --- |
| cfg-181ea3a4a534c533dcaf | [turboderp/GLM-5.3-Flash-exl3@2a30229e67](https://huggingface.co/turboderp/GLM-5.3-Flash-exl3/tree/2a30229e67012798ba9f0cd832bb78abf4c363d5) | 3 | 262,144 | 262,144 | 4 | dflash2 / 2 |

Card counts are saved configuration choices, not a claim that every allowed placement was measured. A derived view can differ from its pinned download source.

<details>
<summary>cfg-181ea3a4a534c533dcaf</summary>

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
  "served_model_label": "glm-5.3-flash",
  "main_reserve_mib_values_unordered": [
    3584
  ]
}
```

Pinned model revision recorded: yes. Source receipt labels, hashes and object locators are retained in [configurations.json](../configurations.json).

</details>

## Retained Measurements

| Profile / Wave | Layout; Draft / Tokens | Requests | Input tokens/request | Accepted output tokens/request | Cache / Reused input tokens | Context / GPU pool tokens | Shared decode tok/s total | Client after-first-token estimate tok/s | Whole-wave output tok/s | Median TTFT, s | Source report |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [ad002-glm-dflash22-small_exl3-layer_split-matched-076](ad002-glm-dflash22-small_exl3-layer_split-matched-076.md)<br>wave-07f4c1385107a0297047 | layer_split; dflash2 / 2 | 4 | 32,767 | 256 (budget 256) | cold; reused 0 | 262,144 / 262,144 | 47.30 | Not recorded | 5.76 | 155.90 | Pass |
| [ad002-glm-dflash22-small_exl3-layer_split-matched-076](ad002-glm-dflash22-small_exl3-layer_split-matched-076.md)<br>wave-0ec3b7413b53a42c5e40 | layer_split; dflash2 / 2 | 4 | 32,767 | 256 (budget 256) | cached_prefix; reused 32,512 | 262,144 / 262,144 | 47.44 | Not recorded | 41.93 | 2.93 | Pass |
| [ad002-glm-dflash22-small_exl3-layer_split-matched-076](ad002-glm-dflash22-small_exl3-layer_split-matched-076.md)<br>wave-38eac26f6fb9186755e7 | layer_split; dflash2 / 2 | 1 | 32,766 | 256 (budget 256) | cold; reused 0 | 262,144 / 262,144 | 39.36 | Not recorded | 5.67 | 38.94 | Pass |
| [ad002-glm-dflash22-small_exl3-layer_split-matched-076](ad002-glm-dflash22-small_exl3-layer_split-matched-076.md)<br>wave-5c50fa2f65411d50e0ec | layer_split; dflash2 / 2 | 1 | 32,766 | 256 (budget 256) | cached_prefix; reused 32,512 | 262,144 / 262,144 | 39.41 | Not recorded | 35.75 | 0.74 | Pass |

Rates are whole-wave totals over the stated request count. A wave may span multiple independent model instances; [measurements.json](../measurements.json) retains their contributions and the exact configuration IDs. Do not interpret a multi-instance total as one card's rate.

A dash in shared decode means no qualified synchronized interval is available. Whole-wave throughput includes prefill and queueing. A valid decode interval can survive inside an overall failed or partial check; the source-report outcome is preserved. No rows are averaged.

## Bounded Checks

| Check | Reported outcome | Retained counts / flags |
| --- | --- | --- |
| check-279fd78c1a763e6656f8 | Pass | {"passed":true,"elapsed_seconds":45.18853770400165,"ttft_seconds":[38.94256031700206],"end_to_end_accepted_tok_s":5.665153443930319} |
| check-4b7eaf14a15728f02102 | Pass | {"passed":true,"elapsed_seconds":177.72286427099607,"ttft_seconds":[155.10080690700124,155.1006720410005,156.69833478899818,156.69801423999888],"end_to_end_accepted_tok_s":5.761779747363177} |
| check-d7077c29a2076ab3d15f | Pass | {"passed":true,"elapsed_seconds":177.72286427099607,"ttft_seconds":[155.10080690700124,155.1006720410005,156.69833478899818,156.69801423999888],"end_to_end_accepted_tok_s":5.761779747363177} |
| check-f53ec57482536f06f793 | Pass | {"passed":true,"elapsed_seconds":45.18853770400165,"ttft_seconds":[38.94256031700206],"end_to_end_accepted_tok_s":5.665153443930319} |

These checks retain their reported scope. A context/allocation/retrieval check is not a general quality score or a speed qualification at that context. Exact flags and provenance are in [checks.json](../checks.json).

## Additional Test Results

| Result / Source | Profile | Evidence type | Reported outcome | Retained values | Configuration binding |
| --- | --- | --- | --- | --- | --- |
| [result-22f453085687592ee681](../observations.json)<br>source-da1323bac7dcf483c91eed0c.json<br>`/waves/1` | [ad002-glm-dflash22-small_exl3-layer_split-matched-076](ad002-glm-dflash22-small_exl3-layer_split-matched-076.md)<br>[record-26c850ec689cf58c6b67](record-26c850ec689cf58c6b67.md)<br>[glm-dflash22-small_exl3-layer_split](glm-dflash22-small_exl3-layer_split.md) | performance detail | Outcome unspecified | elapsed_seconds=7.16 s; end_to_end_accepted_tok_s=35.75 accepted tokens/s; output_tokens=256 tokens; ttft_seconds=0.74 s; p50_ms=21.97 ms; p95_ms=64.08 ms; prefill: per-request 461.82 tokens/s; Draft accepted / proposed: 150 / 212 tokens; fraction 0.7075 | Recorded configuration/job |
| [result-37bb46e7e4db75c61f97](../observations.json)<br>source-1191a560c84be12f7498ad8b.json<br>`/waves/1` | [ad002-glm-dflash22-small_exl3-layer_split-matched-076](ad002-glm-dflash22-small_exl3-layer_split-matched-076.md)<br>[record-26c850ec689cf58c6b67](record-26c850ec689cf58c6b67.md)<br>[glm-dflash22-small_exl3-layer_split](glm-dflash22-small_exl3-layer_split.md) | performance detail | Outcome unspecified | elapsed_seconds=24.42 s; end_to_end_accepted_tok_s=41.93 accepted tokens/s; output_tokens=256 tokens; ttft_seconds=1.51<br>2.93<br>2.93<br>2.93 s; p50_ms=74.25 ms; p95_ms=219.71 ms; prefill: per-request 286.52 to 566.67 tokens/s; Draft accepted / proposed: 590 / 868 tokens; fraction 0.6797 | Recorded configuration/job |
| [result-508a4cb5b76e2ec1dd7d](../observations.json)<br>source-da1323bac7dcf483c91eed0c.json<br>`/waves/0` | [ad002-glm-dflash22-small_exl3-layer_split-matched-076](ad002-glm-dflash22-small_exl3-layer_split-matched-076.md)<br>[record-26c850ec689cf58c6b67](record-26c850ec689cf58c6b67.md)<br>[glm-dflash22-small_exl3-layer_split](glm-dflash22-small_exl3-layer_split.md) | performance detail | Outcome unspecified | elapsed_seconds=45.19 s; end_to_end_accepted_tok_s=5.67 accepted tokens/s; output_tokens=256 tokens; ttft_seconds=38.94 s; p50_ms=21.97 ms; p95_ms=64.15 ms; prefill: per-request 847.76 tokens/s; Draft accepted / proposed: 151 / 210 tokens; fraction 0.7190 | Recorded configuration/job |
| [result-6cb5be186bc68330e16d](../observations.json)<br>source-1191a560c84be12f7498ad8b.json<br>`/waves/0` | [ad002-glm-dflash22-small_exl3-layer_split-matched-076](ad002-glm-dflash22-small_exl3-layer_split-matched-076.md)<br>[record-26c850ec689cf58c6b67](record-26c850ec689cf58c6b67.md)<br>[glm-dflash22-small_exl3-layer_split](glm-dflash22-small_exl3-layer_split.md) | performance detail | Outcome unspecified | elapsed_seconds=177.72 s; end_to_end_accepted_tok_s=5.76 accepted tokens/s; output_tokens=256 tokens; ttft_seconds=155.10<br>155.10<br>156.70<br>156.70 s; p50_ms=74.78 ms; p95_ms=219.74 ms; prefill: per-request 214.72 to 217.45 tokens/s; Draft accepted / proposed: 592 / 864 tokens; fraction 0.6852 | Recorded configuration/job |
| [result-6f8b747ebe95320dab7f](../observations.json)<br>source-1191a560c84be12f7498ad8b.json<br>`/` | [ad002-glm-dflash22-small_exl3-layer_split-matched-076](ad002-glm-dflash22-small_exl3-layer_split-matched-076.md)<br>[record-26c850ec689cf58c6b67](record-26c850ec689cf58c6b67.md)<br>[glm-dflash22-small_exl3-layer_split](glm-dflash22-small_exl3-layer_split.md) | performance detail | Pass | elapsed_seconds=177.72 s; end_to_end_accepted_tok_s=5.76 accepted tokens/s; ttft_seconds=155.10<br>155.10<br>156.70<br>156.70 s; p50_ms=74.25 ms; p95_ms=219.71 ms; cold_prefill: per-request 214.72 to 217.45 tokens/s; Draft accepted / proposed: 590 / 868 tokens; fraction 0.6797 | Recorded configuration/job |
| [result-8bd728d79379337667fa](../observations.json)<br>source-a9e622d351a86c8b776605d4.json<br>`/managed_phase_timings/76` | [ad002-glm-dflash22-small_exl3-layer_split-matched-076](ad002-glm-dflash22-small_exl3-layer_split-matched-076.md) | test outcome | Outcome unspecified | wall_seconds=569.52 s | Recorded configuration/job |
| [result-c98cc95418e7e10cda03](../observations.json)<br>source-da1323bac7dcf483c91eed0c.json<br>`/` | [ad002-glm-dflash22-small_exl3-layer_split-matched-076](ad002-glm-dflash22-small_exl3-layer_split-matched-076.md)<br>[record-26c850ec689cf58c6b67](record-26c850ec689cf58c6b67.md)<br>[glm-dflash22-small_exl3-layer_split](glm-dflash22-small_exl3-layer_split.md) | performance detail | Pass | elapsed_seconds=45.19 s; end_to_end_accepted_tok_s=5.67 accepted tokens/s; ttft_seconds=38.94 s; p50_ms=21.97 ms; p95_ms=64.08 ms; cold_prefill: per-request 847.76 tokens/s; Draft accepted / proposed: 150 / 212 tokens; fraction 0.7075 | Recorded configuration/job |

These are saved result records, including failures and bounded checks. Copies, individual requests, report summaries and regrading can overlap; their counts are not independent test repetitions. Open each result for exact values, units, configuration binding and source receipts.

There are 1 retained lifecycle records. Their states, exit codes and configuration IDs remain in [catalog.json](../catalog.json); they do not supply missing benchmark results.

[Full archive](../../README.md) | [All retained waves](../RESULTS.md) | [Data definitions](../DATA.md) | [Recommended recipes](../../../README.md)
