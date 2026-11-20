# ab-mimo-dflash7-original-layer_split-matched-056

**Historical record. Decode interval measured.**

Model family: MiMo V2.6 Flash.

Historical configurations are provided for comparison. The [recommended recipes](../../../README.md) include supported launch scripts.

Current recipes using the same recorded checkpoint repository: [mimo-flash-mtp1-tp3](../../../recipes/mimo-flash-mtp1-tp3/README.md). Context, cache and runtime versions can differ.

## Saved Configuration Versions

Each configuration ID identifies a distinct original settings record. Deployment fields are omitted; versions can have identical published settings after that omission. Upstream runtime commits remain unspecified where the source retained only an integration label.

| Configuration | Recorded artifact / source | Configured card counts | Context tokens | GPU pool tokens | Slots | Draft mode / tokens |
| --- | --- | --- | --- | --- | --- | --- |
| cfg-217ff9c9b50e9f972525 | [MikeRoz/MiMo-V2.6-Flash-MOPD-4.03bpw-h8-exl3@29c8351a8b](https://huggingface.co/MikeRoz/MiMo-V2.6-Flash-MOPD-4.03bpw-h8-exl3/tree/29c8351a8b5854ec385adaeba7bbe62c790d40ea) | 3 | 262,144 | 262,144 | 4 | dflash / 7 |

Card counts are saved configuration choices, not a claim that every allowed placement was measured. A derived view can differ from its pinned download source.

<details>
<summary>cfg-217ff9c9b50e9f972525</summary>

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
  "draft_mode": "dflash",
  "draft_tokens": 7,
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
  "model_repository": "MikeRoz/MiMo-V2.6-Flash-MOPD-4.03bpw-h8-exl3",
  "model_revision": "29c8351a8b5854ec385adaeba7bbe62c790d40ea",
  "draft_repository": null,
  "draft_revision": null,
  "recorded_runtime_label": null,
  "served_model_label": "mimo-v2.6-flash",
  "main_reserve_mib_values_unordered": [
    6144
  ]
}
```

Pinned model revision recorded: yes. Source receipt labels, hashes and object locators are retained in [configurations.json](../configurations.json).

</details>

## Retained Measurements

| Profile / Wave | Layout; Draft / Tokens | Requests | Input tokens/request | Accepted output tokens/request | Cache / Reused input tokens | Context / GPU pool tokens | Shared decode tok/s total | Client after-first-token estimate tok/s | Whole-wave output tok/s | Median TTFT, s | Source report |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [ab-mimo-dflash7-original-layer_split-matched-056](ab-mimo-dflash7-original-layer_split-matched-056.md)<br>wave-15b442575659db2b974b | layer_split; dflash / 7 | 1 | 32,765 | 512 (budget 512) | cold; reused 0 | 262,144 / 262,144 | 24.45 | Not recorded | 8.17 | 41.98 | Pass |
| [ab-mimo-dflash7-original-layer_split-matched-056](ab-mimo-dflash7-original-layer_split-matched-056.md)<br>wave-1a80c0e2fee7b135327e | layer_split; dflash / 7 | 1 | 32,765 | 512 (budget 512) | cached_prefix; reused 32,512 | 262,144 / 262,144 | 24.06 | Not recorded | 23.36 | 1.06 | Pass |
| [ab-mimo-dflash7-original-layer_split-matched-056](ab-mimo-dflash7-original-layer_split-matched-056.md)<br>wave-8502b9b401dbcf4df5eb | layer_split; dflash / 7 | 4 | 2,039 | 512 (budget 512) | cached_prefix; reused 1,792 | 262,144 / 262,144 | 57.04 | Not recorded | 53.49 | 2.58 | Pass |
| [ab-mimo-dflash7-original-layer_split-matched-056](ab-mimo-dflash7-original-layer_split-matched-056.md)<br>wave-8a1aac553436e193f9ab | layer_split; dflash / 7 | 1 | 2,038 | 512 (budget 512) | cold; reused 0 | 262,144 / 262,144 | 42.55 | Not recorded | 35.06 | 2.78 | Pass |
| [ab-mimo-dflash7-original-layer_split-matched-056](ab-mimo-dflash7-original-layer_split-matched-056.md)<br>wave-9bb232c69a0d5018bac5 | layer_split; dflash / 7 | 1 | 2,038 | 512 (budget 512) | cached_prefix; reused 1,792 | 262,144 / 262,144 | 42.28 | Not recorded | 40.90 | 0.69 | Pass |
| [ab-mimo-dflash7-original-layer_split-matched-056](ab-mimo-dflash7-original-layer_split-matched-056.md)<br>wave-b0168c23f94bf0e9d06d | layer_split; dflash / 7 | 4 | 32,766 | 512 (budget 512) | cached_prefix; reused 32,512 | 262,144 / 262,144 | 40.85 | Not recorded | 38.30 | 4.20 | Pass |
| [ab-mimo-dflash7-original-layer_split-matched-056](ab-mimo-dflash7-original-layer_split-matched-056.md)<br>wave-ba4500789ea52d1a1166 | layer_split; dflash / 7 | 4 | 2,039 | 512 (budget 512) | cold; reused 0 | 262,144 / 262,144 | 55.40 | Not recorded | 42.62 | 11.35 | Pass |
| [ab-mimo-dflash7-original-layer_split-matched-056](ab-mimo-dflash7-original-layer_split-matched-056.md)<br>wave-c23913bf5c3fdd3e5c87 | layer_split; dflash / 7 | 4 | 32,766 | 512 (budget 512) | cold; reused 0 | 262,144 / 262,144 | 40.07 | Not recorded | 9.32 | 168.11 | Pass |

Rates are whole-wave totals over the stated request count. A wave may span multiple independent model instances; [measurements.json](../measurements.json) retains their contributions and the exact configuration IDs. Do not interpret a multi-instance total as one card's rate.

A dash in shared decode means no qualified synchronized interval is available. Whole-wave throughput includes prefill and queueing. A valid decode interval can survive inside an overall failed or partial check; the source-report outcome is preserved. No rows are averaged.

## Bounded Checks

| Check | Reported outcome | Retained counts / flags |
| --- | --- | --- |
| check-0a4364f0e5de1894b135 | Pass | {"passed":true,"elapsed_seconds":14.602885433007032,"ttft_seconds":[2.7789625149962376],"end_to_end_accepted_tok_s":35.06156384975272} |
| check-219873cf54f380eb187d | Pass | {"passed":true,"elapsed_seconds":14.602885433007032,"ttft_seconds":[2.7789625149962376],"end_to_end_accepted_tok_s":35.06156384975272} |
| check-3245cdd5b46800040ae3 | Pass | {"passed":true,"elapsed_seconds":48.04807932699623,"ttft_seconds":[6.99400350900396,11.144523205999576,11.565536098998564,11.56537631500396],"end_to_end_accepted_tok_s":42.62397225208778} |
| check-558547a4ed832a487338 | Pass | {"passed":true,"elapsed_seconds":62.67634049800108,"ttft_seconds":[41.9780139870054],"end_to_end_accepted_tok_s":8.168951727746917} |
| check-7921e7982bd289fdff64 | Pass | {"passed":true,"elapsed_seconds":48.04807932699623,"ttft_seconds":[6.99400350900396,11.144523205999576,11.565536098998564,11.56537631500396],"end_to_end_accepted_tok_s":42.62397225208778} |
| check-93c0895ee569d61994ed | Pass | {"passed":true,"elapsed_seconds":219.6608768379956,"ttft_seconds":[160.99443946599786,168.10722267700476,168.10681456999737,168.1067190850008],"end_to_end_accepted_tok_s":9.323462737110177} |
| check-e869064553e80f19c588 | Pass | {"passed":true,"elapsed_seconds":219.6608768379956,"ttft_seconds":[160.99443946599786,168.10722267700476,168.10681456999737,168.1067190850008],"end_to_end_accepted_tok_s":9.323462737110177} |
| check-eca37bcbead454ef9767 | Pass | {"passed":true,"elapsed_seconds":62.67634049800108,"ttft_seconds":[41.9780139870054],"end_to_end_accepted_tok_s":8.168951727746917} |

These checks retain their reported scope. A context/allocation/retrieval check is not a general quality score or a speed qualification at that context. Exact flags and provenance are in [checks.json](../checks.json).

## Additional Test Results

| Result / Source | Profile | Evidence type | Reported outcome | Retained values | Configuration binding |
| --- | --- | --- | --- | --- | --- |
| [result-35406d0c2cece3999b52](../observations.json)<br>source-dd9f7b0df7adaffb2c1c4beb.json<br>`/waves/1` | [ab-mimo-dflash7-original-layer_split-matched-056](ab-mimo-dflash7-original-layer_split-matched-056.md)<br>[record-26c850ec689cf58c6b67](record-26c850ec689cf58c6b67.md)<br>[mimo-dflash7-original-layer_split](mimo-dflash7-original-layer_split.md) | performance detail | Outcome unspecified | elapsed_seconds=12.52 s; end_to_end_accepted_tok_s=40.90 accepted tokens/s; output_tokens=512 tokens; ttft_seconds=0.69 s; p50_ms=26.69 ms; p95_ms=78.48 ms; prefill: per-request 473.08 tokens/s; Draft accepted / proposed: 349 / 1,141 tokens; fraction 0.3059 | Recorded configuration/job |
| [result-35949625429861227628](../observations.json)<br>source-8d6cb023fa860256e0f09a70.json<br>`/waves/1` | [ab-mimo-dflash7-original-layer_split-matched-056](ab-mimo-dflash7-original-layer_split-matched-056.md)<br>[record-26c850ec689cf58c6b67](record-26c850ec689cf58c6b67.md)<br>[mimo-dflash7-original-layer_split](mimo-dflash7-original-layer_split.md) | performance detail | Outcome unspecified | elapsed_seconds=53.48 s; end_to_end_accepted_tok_s=38.30 accepted tokens/s; output_tokens=512 tokens; ttft_seconds=1.25<br>4.20<br>4.20<br>4.19 s; p50_ms=106.03 ms; p95_ms=318.69 ms; prefill: per-request 192.42 to 384.85 tokens/s; Draft accepted / proposed: 1,421 / 4,389 tokens; fraction 0.3238 | Recorded configuration/job |
| [result-3efaa4decb8422b8aad5](../observations.json)<br>source-496b8dcd02dcc5f16ef947c1.json<br>`/waves/1` | [ab-mimo-dflash7-original-layer_split-matched-056](ab-mimo-dflash7-original-layer_split-matched-056.md)<br>[record-26c850ec689cf58c6b67](record-26c850ec689cf58c6b67.md)<br>[mimo-dflash7-original-layer_split](mimo-dflash7-original-layer_split.md) | performance detail | Outcome unspecified | elapsed_seconds=38.29 s; end_to_end_accepted_tok_s=53.49 accepted tokens/s; output_tokens=512 tokens; ttft_seconds=0.76<br>2.48<br>2.67<br>2.67 s; p50_ms=78.53 ms; p95_ms=229.74 ms; prefill: per-request 274.44 to 561.36 tokens/s; Draft accepted / proposed: 1,400 / 4,536 tokens; fraction 0.3086 | Recorded configuration/job |
| [result-43032168d3f28fc7af8d](../observations.json)<br>source-69c80a9f5a924936bdc84ee1.json<br>`/` | [ab-mimo-dflash7-original-layer_split-matched-056](ab-mimo-dflash7-original-layer_split-matched-056.md)<br>[record-26c850ec689cf58c6b67](record-26c850ec689cf58c6b67.md)<br>[mimo-dflash7-original-layer_split](mimo-dflash7-original-layer_split.md) | performance detail | Pass | elapsed_seconds=62.68 s; end_to_end_accepted_tok_s=8.17 accepted tokens/s; ttft_seconds=41.98 s; p50_ms=51.41 ms; p95_ms=120.07 ms; cold_prefill: per-request 784.98 tokens/s; Draft accepted / proposed: 330 / 1,274 tokens; fraction 0.2590 | Recorded configuration/job |
| [result-64685318582e62664cf0](../observations.json)<br>source-496b8dcd02dcc5f16ef947c1.json<br>`/` | [ab-mimo-dflash7-original-layer_split-matched-056](ab-mimo-dflash7-original-layer_split-matched-056.md)<br>[record-26c850ec689cf58c6b67](record-26c850ec689cf58c6b67.md)<br>[mimo-dflash7-original-layer_split](mimo-dflash7-original-layer_split.md) | performance detail | Pass | elapsed_seconds=48.05 s; end_to_end_accepted_tok_s=42.62 accepted tokens/s; ttft_seconds=6.99<br>11.14<br>11.57<br>11.57 s; p50_ms=78.53 ms; p95_ms=229.74 ms; cold_prefill: per-request 253.29 to 299.41 tokens/s; Draft accepted / proposed: 1,400 / 4,536 tokens; fraction 0.3086 | Recorded configuration/job |
| [result-7de8504e44958d15a8b3](../observations.json)<br>source-69c80a9f5a924936bdc84ee1.json<br>`/waves/0` | [ab-mimo-dflash7-original-layer_split-matched-056](ab-mimo-dflash7-original-layer_split-matched-056.md)<br>[record-26c850ec689cf58c6b67](record-26c850ec689cf58c6b67.md)<br>[mimo-dflash7-original-layer_split](mimo-dflash7-original-layer_split.md) | performance detail | Outcome unspecified | elapsed_seconds=62.68 s; end_to_end_accepted_tok_s=8.17 accepted tokens/s; output_tokens=512 tokens; ttft_seconds=41.98 s; p50_ms=51.61 ms; p95_ms=119.34 ms; prefill: per-request 784.98 tokens/s; Draft accepted / proposed: 330 / 1,274 tokens; fraction 0.2590 | Recorded configuration/job |
| [result-8cf3920cad701b45ea15](../observations.json)<br>source-dd9f7b0df7adaffb2c1c4beb.json<br>`/` | [ab-mimo-dflash7-original-layer_split-matched-056](ab-mimo-dflash7-original-layer_split-matched-056.md)<br>[record-26c850ec689cf58c6b67](record-26c850ec689cf58c6b67.md)<br>[mimo-dflash7-original-layer_split](mimo-dflash7-original-layer_split.md) | performance detail | Pass | elapsed_seconds=14.60 s; end_to_end_accepted_tok_s=35.06 accepted tokens/s; ttft_seconds=2.78 s; p50_ms=26.69 ms; p95_ms=78.48 ms; cold_prefill: per-request 752.03 tokens/s; Draft accepted / proposed: 349 / 1,141 tokens; fraction 0.3059 | Recorded configuration/job |
| [result-a7c9dadc28bebd734ce4](../observations.json)<br>source-8d6cb023fa860256e0f09a70.json<br>`/` | [ab-mimo-dflash7-original-layer_split-matched-056](ab-mimo-dflash7-original-layer_split-matched-056.md)<br>[record-26c850ec689cf58c6b67](record-26c850ec689cf58c6b67.md)<br>[mimo-dflash7-original-layer_split](mimo-dflash7-original-layer_split.md) | performance detail | Pass | elapsed_seconds=219.66 s; end_to_end_accepted_tok_s=9.32 accepted tokens/s; ttft_seconds=160.99<br>168.11<br>168.11<br>168.11 s; p50_ms=106.03 ms; p95_ms=318.69 ms; cold_prefill: per-request 199.68 to 203.76 tokens/s; Draft accepted / proposed: 1,421 / 4,389 tokens; fraction 0.3238 | Recorded configuration/job |
| [result-af941fca150742abb7e5](../observations.json)<br>source-8d6cb023fa860256e0f09a70.json<br>`/waves/0` | [ab-mimo-dflash7-original-layer_split-matched-056](ab-mimo-dflash7-original-layer_split-matched-056.md)<br>[record-26c850ec689cf58c6b67](record-26c850ec689cf58c6b67.md)<br>[mimo-dflash7-original-layer_split](mimo-dflash7-original-layer_split.md) | performance detail | Outcome unspecified | elapsed_seconds=219.66 s; end_to_end_accepted_tok_s=9.32 accepted tokens/s; output_tokens=512 tokens; ttft_seconds=160.99<br>168.11<br>168.11<br>168.11 s; p50_ms=121.02 ms; p95_ms=316.89 ms; prefill: per-request 199.68 to 203.76 tokens/s; Draft accepted / proposed: 1,386 / 4,634 tokens; fraction 0.2991 | Recorded configuration/job |
| [result-bb37611e92e04255c2e4](../observations.json)<br>source-69c80a9f5a924936bdc84ee1.json<br>`/waves/1` | [ab-mimo-dflash7-original-layer_split-matched-056](ab-mimo-dflash7-original-layer_split-matched-056.md)<br>[record-26c850ec689cf58c6b67](record-26c850ec689cf58c6b67.md)<br>[mimo-dflash7-original-layer_split](mimo-dflash7-original-layer_split.md) | performance detail | Outcome unspecified | elapsed_seconds=21.92 s; end_to_end_accepted_tok_s=23.36 accepted tokens/s; output_tokens=512 tokens; ttft_seconds=1.06 s; p50_ms=51.41 ms; p95_ms=120.07 ms; prefill: per-request 320.25 tokens/s; Draft accepted / proposed: 330 / 1,274 tokens; fraction 0.2590 | Recorded configuration/job |
| [result-cf2859fee128c3c5645a](../observations.json)<br>source-496b8dcd02dcc5f16ef947c1.json<br>`/waves/0` | [ab-mimo-dflash7-original-layer_split-matched-056](ab-mimo-dflash7-original-layer_split-matched-056.md)<br>[record-26c850ec689cf58c6b67](record-26c850ec689cf58c6b67.md)<br>[mimo-dflash7-original-layer_split](mimo-dflash7-original-layer_split.md) | performance detail | Outcome unspecified | elapsed_seconds=48.05 s; end_to_end_accepted_tok_s=42.62 accepted tokens/s; output_tokens=512 tokens; ttft_seconds=6.99<br>11.14<br>11.57<br>11.57 s; p50_ms=79.95 ms; p95_ms=227.50 ms; prefill: per-request 253.29 to 299.41 tokens/s; Draft accepted / proposed: 1,370 / 4,746 tokens; fraction 0.2887 | Recorded configuration/job |
| [result-d5446f82e006ca67b62f](../observations.json)<br>source-a9e622d351a86c8b776605d4.json<br>`/managed_phase_timings/56` | [ab-mimo-dflash7-original-layer_split-matched-056](ab-mimo-dflash7-original-layer_split-matched-056.md) | test outcome | Outcome unspecified | wall_seconds=797.62 s | Recorded configuration/job |
| [result-fc95adda5fef70158897](../observations.json)<br>source-dd9f7b0df7adaffb2c1c4beb.json<br>`/waves/0` | [ab-mimo-dflash7-original-layer_split-matched-056](ab-mimo-dflash7-original-layer_split-matched-056.md)<br>[record-26c850ec689cf58c6b67](record-26c850ec689cf58c6b67.md)<br>[mimo-dflash7-original-layer_split](mimo-dflash7-original-layer_split.md) | performance detail | Outcome unspecified | elapsed_seconds=14.60 s; end_to_end_accepted_tok_s=35.06 accepted tokens/s; output_tokens=512 tokens; ttft_seconds=2.78 s; p50_ms=26.55 ms; p95_ms=77.97 ms; prefill: per-request 752.03 tokens/s; Draft accepted / proposed: 349 / 1,141 tokens; fraction 0.3059 | Recorded configuration/job |

These are saved result records, including failures and bounded checks. Copies, individual requests, report summaries and regrading can overlap; their counts are not independent test repetitions. Open each result for exact values, units, configuration binding and source receipts.

There are 1 retained lifecycle records. Their states, exit codes and configuration IDs remain in [catalog.json](../catalog.json); they do not supply missing benchmark results.

[Full archive](../../README.md) | [All retained waves](../RESULTS.md) | [Data definitions](../DATA.md) | [Recommended recipes](../../../README.md)
