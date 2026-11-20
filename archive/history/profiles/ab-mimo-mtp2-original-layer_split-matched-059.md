# ab-mimo-mtp2-original-layer_split-matched-059

**Historical record. Decode interval measured.**

Model family: MiMo V2.6 Flash.

Historical configurations are provided for comparison. The [recommended recipes](../../../README.md) include supported launch scripts.

Current recipes using the same recorded checkpoint repository: [mimo-flash-mtp1-tp3](../../../recipes/mimo-flash-mtp1-tp3/README.md). Context, cache and runtime versions can differ.

## Saved Configuration Versions

Each configuration ID identifies a distinct original settings record. Deployment fields are omitted; versions can have identical published settings after that omission. Upstream runtime commits remain unspecified where the source retained only an integration label.

| Configuration | Recorded artifact / source | Configured card counts | Context tokens | GPU pool tokens | Slots | Draft mode / tokens |
| --- | --- | --- | --- | --- | --- | --- |
| cfg-442222ebf12c381d6a19 | [MikeRoz/MiMo-V2.6-Flash-MOPD-4.03bpw-h8-exl3@29c8351a8b](https://huggingface.co/MikeRoz/MiMo-V2.6-Flash-MOPD-4.03bpw-h8-exl3/tree/29c8351a8b5854ec385adaeba7bbe62c790d40ea) | 3 | 262,144 | 262,144 | 4 | mtp / 2 |

Card counts are saved configuration choices, not a claim that every allowed placement was measured. A derived view can differ from its pinned download source.

<details>
<summary>cfg-442222ebf12c381d6a19</summary>

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
  "model_repository": "MikeRoz/MiMo-V2.6-Flash-MOPD-4.03bpw-h8-exl3",
  "model_revision": "29c8351a8b5854ec385adaeba7bbe62c790d40ea",
  "draft_repository": null,
  "draft_revision": null,
  "recorded_runtime_label": null,
  "served_model_label": "mimo-v2.6-flash"
}
```

Pinned model revision recorded: yes. Source receipt labels, hashes and object locators are retained in [configurations.json](../configurations.json).

</details>

## Retained Measurements

| Profile / Wave | Layout; Draft / Tokens | Requests | Input tokens/request | Accepted output tokens/request | Cache / Reused input tokens | Context / GPU pool tokens | Shared decode tok/s total | Client after-first-token estimate tok/s | Whole-wave output tok/s | Median TTFT, s | Source report |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [ab-mimo-mtp2-original-layer_split-matched-059](ab-mimo-mtp2-original-layer_split-matched-059.md)<br>wave-1394ad88788369a43a57 | layer_split; mtp / 2 | 1 | 2,038 | 512 (budget 512) | cached_prefix; reused 1,792 | 262,144 / 262,144 | 44.54 | Not recorded | 42.58 | 0.71 | Pass |
| [ab-mimo-mtp2-original-layer_split-matched-059](ab-mimo-mtp2-original-layer_split-matched-059.md)<br>wave-2a05fc132f8bc1e33648 | layer_split; mtp / 2 | 1 | 32,765 | 512 (budget 512) | cached_prefix; reused 32,512 | 262,144 / 262,144 | 32.43 | Not recorded | 30.87 | 0.92 | Pass |
| [ab-mimo-mtp2-original-layer_split-matched-059](ab-mimo-mtp2-original-layer_split-matched-059.md)<br>wave-79161b0cfe7ee9459440 | layer_split; mtp / 2 | 4 | 2,039 | 512 (budget 512) | cached_prefix; reused 1,792 | 262,144 / 262,144 | 69.40 | Not recorded | 65.49 | 2.26 | Pass |
| [ab-mimo-mtp2-original-layer_split-matched-059](ab-mimo-mtp2-original-layer_split-matched-059.md)<br>wave-83184ba36692f1825c7f | layer_split; mtp / 2 | 4 | 32,766 | 512 (budget 512) | cached_prefix; reused 32,512 | 262,144 / 262,144 | 39.44 | Not recorded | 37.11 | 3.73 | Pass |
| [ab-mimo-mtp2-original-layer_split-matched-059](ab-mimo-mtp2-original-layer_split-matched-059.md)<br>wave-b0ec166318e1ac66f939 | layer_split; mtp / 2 | 4 | 32,766 | 512 (budget 512) | cold; reused 0 | 262,144 / 262,144 | 39.16 | Not recorded | 9.36 | 166.88 | Pass |
| [ab-mimo-mtp2-original-layer_split-matched-059](ab-mimo-mtp2-original-layer_split-matched-059.md)<br>wave-b261d9d4580d0a4ef019 | layer_split; mtp / 2 | 1 | 32,765 | 512 (budget 512) | cold; reused 0 | 262,144 / 262,144 | 32.43 | Not recorded | 8.90 | 41.86 | Pass |
| [ab-mimo-mtp2-original-layer_split-matched-059](ab-mimo-mtp2-original-layer_split-matched-059.md)<br>wave-c55425877cd92716804a | layer_split; mtp / 2 | 1 | 2,038 | 512 (budget 512) | cold; reused 0 | 262,144 / 262,144 | 45.14 | Not recorded | 36.31 | 2.85 | Pass |
| [ab-mimo-mtp2-original-layer_split-matched-059](ab-mimo-mtp2-original-layer_split-matched-059.md)<br>wave-fb712204d0b037d32955 | layer_split; mtp / 2 | 4 | 2,039 | 512 (budget 512) | cold; reused 0 | 262,144 / 262,144 | 70.43 | Not recorded | 51.52 | 11.09 | Pass |

Rates are whole-wave totals over the stated request count. A wave may span multiple independent model instances; [measurements.json](../measurements.json) retains their contributions and the exact configuration IDs. Do not interpret a multi-instance total as one card's rate.

A dash in shared decode means no qualified synchronized interval is available. Whole-wave throughput includes prefill and queueing. A valid decode interval can survive inside an overall failed or partial check; the source-report outcome is preserved. No rows are averaged.

## Bounded Checks

| Check | Reported outcome | Retained counts / flags |
| --- | --- | --- |
| check-4ae16494507b49a9cf73 | Pass | {"passed":true,"elapsed_seconds":57.528409742000804,"ttft_seconds":[41.86308282099344],"end_to_end_accepted_tok_s":8.899950516556604} |
| check-4ecd4ef31c7873c0fd2a | Pass | {"passed":true,"elapsed_seconds":14.101537668000674,"ttft_seconds":[2.845165941005689],"end_to_end_accepted_tok_s":36.30809717736206} |
| check-61a4541eeb1b7e17a37a | Pass | {"passed":true,"elapsed_seconds":39.75302372599981,"ttft_seconds":[7.622439792001387,11.091210279002553,11.09051535600156,11.090514192001137],"end_to_end_accepted_tok_s":51.518093670458065} |
| check-724fdc700c12f627f06e | Pass | {"passed":true,"elapsed_seconds":218.76028132200008,"ttft_seconds":[163.56061673600198,166.87956958099676,166.87902175100317,167.7690764910003],"end_to_end_accepted_tok_s":9.361845704456217} |
| check-74a53a20218dd06d7741 | Pass | {"passed":true,"elapsed_seconds":39.75302372599981,"ttft_seconds":[7.622439792001387,11.091210279002553,11.09051535600156,11.090514192001137],"end_to_end_accepted_tok_s":51.518093670458065} |
| check-8edc36c2e51716e32c43 | Pass | {"passed":true,"elapsed_seconds":14.101537668000674,"ttft_seconds":[2.845165941005689],"end_to_end_accepted_tok_s":36.30809717736206} |
| check-b372c1804ff6ce7318ff | Pass | {"passed":true,"elapsed_seconds":218.76028132200008,"ttft_seconds":[163.56061673600198,166.87956958099676,166.87902175100317,167.7690764910003],"end_to_end_accepted_tok_s":9.361845704456217} |
| check-bf6b51245e9fb453dace | Pass | {"passed":true,"elapsed_seconds":57.528409742000804,"ttft_seconds":[41.86308282099344],"end_to_end_accepted_tok_s":8.899950516556604} |

These checks retain their reported scope. A context/allocation/retrieval check is not a general quality score or a speed qualification at that context. Exact flags and provenance are in [checks.json](../checks.json).

## Additional Test Results

| Result / Source | Profile | Evidence type | Reported outcome | Retained values | Configuration binding |
| --- | --- | --- | --- | --- | --- |
| [result-5e4e21f1f9497de8669a](../observations.json)<br>source-a9e622d351a86c8b776605d4.json<br>`/managed_phase_timings/59` | [ab-mimo-mtp2-original-layer_split-matched-059](ab-mimo-mtp2-original-layer_split-matched-059.md) | test outcome | Outcome unspecified | wall_seconds=770.50 s | Recorded configuration/job |
| [result-73041d2eda60572771c3](../observations.json)<br>source-5809b04a194d8806c2aaa9a3.json<br>`/waves/0` | [ab-mimo-mtp2-original-layer_split-matched-059](ab-mimo-mtp2-original-layer_split-matched-059.md)<br>[record-26c850ec689cf58c6b67](record-26c850ec689cf58c6b67.md)<br>[mimo-mtp2-original-layer_split](mimo-mtp2-original-layer_split.md) | performance detail | Outcome unspecified | elapsed_seconds=14.10 s; end_to_end_accepted_tok_s=36.31 accepted tokens/s; output_tokens=512 tokens; ttft_seconds=2.85 s; p50_ms=19.31 ms; p95_ms=51.71 ms; prefill: per-request 730.47 tokens/s; Draft accepted / proposed: 289 / 446 tokens; fraction 0.6480 | Recorded configuration/job |
| [result-754907de2ffb0ddc26ce](../observations.json)<br>source-5809b04a194d8806c2aaa9a3.json<br>`/waves/1` | [ab-mimo-mtp2-original-layer_split-matched-059](ab-mimo-mtp2-original-layer_split-matched-059.md)<br>[record-26c850ec689cf58c6b67](record-26c850ec689cf58c6b67.md)<br>[mimo-mtp2-original-layer_split](mimo-mtp2-original-layer_split.md) | performance detail | Outcome unspecified | elapsed_seconds=12.02 s; end_to_end_accepted_tok_s=42.58 accepted tokens/s; output_tokens=512 tokens; ttft_seconds=0.71 s; p50_ms=19.46 ms; p95_ms=51.52 ms; prefill: per-request 455.56 tokens/s; Draft accepted / proposed: 289 / 446 tokens; fraction 0.6480 | Recorded configuration/job |
| [result-77211997fdf6f86f0c83](../observations.json)<br>source-ba9f796abf51a2b048974408.json<br>`/waves/0` | [ab-mimo-mtp2-original-layer_split-matched-059](ab-mimo-mtp2-original-layer_split-matched-059.md)<br>[record-26c850ec689cf58c6b67](record-26c850ec689cf58c6b67.md)<br>[mimo-mtp2-original-layer_split](mimo-mtp2-original-layer_split.md) | performance detail | Outcome unspecified | elapsed_seconds=218.76 s; end_to_end_accepted_tok_s=9.36 accepted tokens/s; output_tokens=512 tokens; ttft_seconds=163.56<br>166.88<br>166.88<br>167.77 s; p50_ms=93.77 ms; p95_ms=232.68 ms; prefill: per-request 200.61 to 203.24 tokens/s; Draft accepted / proposed: 1,127 / 1,842 tokens; fraction 0.6118 | Recorded configuration/job |
| [result-8501da1c00602c0c3d61](../observations.json)<br>source-56af84c2cbee25ba36b4b93b.json<br>`/` | [ab-mimo-mtp2-original-layer_split-matched-059](ab-mimo-mtp2-original-layer_split-matched-059.md)<br>[record-26c850ec689cf58c6b67](record-26c850ec689cf58c6b67.md)<br>[mimo-mtp2-original-layer_split](mimo-mtp2-original-layer_split.md) | performance detail | Pass | elapsed_seconds=57.53 s; end_to_end_accepted_tok_s=8.90 accepted tokens/s; ttft_seconds=41.86 s; p50_ms=28.24 ms; p95_ms=69.01 ms; cold_prefill: per-request 785.35 tokens/s; Draft accepted / proposed: 283 / 458 tokens; fraction 0.6179 | Recorded configuration/job |
| [result-9760027ff546b82f706f](../observations.json)<br>source-56af84c2cbee25ba36b4b93b.json<br>`/waves/1` | [ab-mimo-mtp2-original-layer_split-matched-059](ab-mimo-mtp2-original-layer_split-matched-059.md)<br>[record-26c850ec689cf58c6b67](record-26c850ec689cf58c6b67.md)<br>[mimo-mtp2-original-layer_split](mimo-mtp2-original-layer_split.md) | performance detail | Outcome unspecified | elapsed_seconds=16.58 s; end_to_end_accepted_tok_s=30.87 accepted tokens/s; output_tokens=512 tokens; ttft_seconds=0.92 s; p50_ms=28.24 ms; p95_ms=69.01 ms; prefill: per-request 328.57 tokens/s; Draft accepted / proposed: 283 / 458 tokens; fraction 0.6179 | Recorded configuration/job |
| [result-9d8a8ee4d179cb295b01](../observations.json)<br>source-5809b04a194d8806c2aaa9a3.json<br>`/` | [ab-mimo-mtp2-original-layer_split-matched-059](ab-mimo-mtp2-original-layer_split-matched-059.md)<br>[record-26c850ec689cf58c6b67](record-26c850ec689cf58c6b67.md)<br>[mimo-mtp2-original-layer_split](mimo-mtp2-original-layer_split.md) | performance detail | Pass | elapsed_seconds=14.10 s; end_to_end_accepted_tok_s=36.31 accepted tokens/s; ttft_seconds=2.85 s; p50_ms=19.46 ms; p95_ms=51.52 ms; cold_prefill: per-request 730.47 tokens/s; Draft accepted / proposed: 289 / 446 tokens; fraction 0.6480 | Recorded configuration/job |
| [result-b54e62952f9909b2df65](../observations.json)<br>source-f26c7c8e72b2c7b5d6d5d4ce.json<br>`/waves/1` | [ab-mimo-mtp2-original-layer_split-matched-059](ab-mimo-mtp2-original-layer_split-matched-059.md)<br>[record-26c850ec689cf58c6b67](record-26c850ec689cf58c6b67.md)<br>[mimo-mtp2-original-layer_split](mimo-mtp2-original-layer_split.md) | performance detail | Outcome unspecified | elapsed_seconds=31.27 s; end_to_end_accepted_tok_s=65.49 accepted tokens/s; output_tokens=512 tokens; ttft_seconds=0.63<br>2.26<br>2.26<br>2.36 s; p50_ms=48.82 ms; p95_ms=135.87 ms; prefill: per-request 274.44 to 548.89 tokens/s; Draft accepted / proposed: 1,154 / 1,788 tokens; fraction 0.6454 | Recorded configuration/job |
| [result-bf1dd4e226e0742d62ef](../observations.json)<br>source-f26c7c8e72b2c7b5d6d5d4ce.json<br>`/waves/0` | [ab-mimo-mtp2-original-layer_split-matched-059](ab-mimo-mtp2-original-layer_split-matched-059.md)<br>[record-26c850ec689cf58c6b67](record-26c850ec689cf58c6b67.md)<br>[mimo-mtp2-original-layer_split](mimo-mtp2-original-layer_split.md) | performance detail | Outcome unspecified | elapsed_seconds=39.75 s; end_to_end_accepted_tok_s=51.52 accepted tokens/s; output_tokens=512 tokens; ttft_seconds=7.62<br>11.09<br>11.09<br>11.09 s; p50_ms=48.34 ms; p95_ms=133.86 ms; prefill: per-request 252.98 to 352.77 tokens/s; Draft accepted / proposed: 1,163 / 1,770 tokens; fraction 0.6571 | Recorded configuration/job |
| [result-e3eedcad2df52303b514](../observations.json)<br>source-f26c7c8e72b2c7b5d6d5d4ce.json<br>`/` | [ab-mimo-mtp2-original-layer_split-matched-059](ab-mimo-mtp2-original-layer_split-matched-059.md)<br>[record-26c850ec689cf58c6b67](record-26c850ec689cf58c6b67.md)<br>[mimo-mtp2-original-layer_split](mimo-mtp2-original-layer_split.md) | performance detail | Pass | elapsed_seconds=39.75 s; end_to_end_accepted_tok_s=51.52 accepted tokens/s; ttft_seconds=7.62<br>11.09<br>11.09<br>11.09 s; p50_ms=48.82 ms; p95_ms=135.87 ms; cold_prefill: per-request 252.98 to 352.77 tokens/s; Draft accepted / proposed: 1,154 / 1,788 tokens; fraction 0.6454 | Recorded configuration/job |
| [result-ea2862e2b3fb45fe2f4d](../observations.json)<br>source-ba9f796abf51a2b048974408.json<br>`/` | [ab-mimo-mtp2-original-layer_split-matched-059](ab-mimo-mtp2-original-layer_split-matched-059.md)<br>[record-26c850ec689cf58c6b67](record-26c850ec689cf58c6b67.md)<br>[mimo-mtp2-original-layer_split](mimo-mtp2-original-layer_split.md) | performance detail | Pass | elapsed_seconds=218.76 s; end_to_end_accepted_tok_s=9.36 accepted tokens/s; ttft_seconds=163.56<br>166.88<br>166.88<br>167.77 s; p50_ms=95.67 ms; p95_ms=228.97 ms; cold_prefill: per-request 200.61 to 203.24 tokens/s; Draft accepted / proposed: 1,121 / 1,854 tokens; fraction 0.6046 | Recorded configuration/job |
| [result-f299456542e1f35ba3a9](../observations.json)<br>source-56af84c2cbee25ba36b4b93b.json<br>`/waves/0` | [ab-mimo-mtp2-original-layer_split-matched-059](ab-mimo-mtp2-original-layer_split-matched-059.md)<br>[record-26c850ec689cf58c6b67](record-26c850ec689cf58c6b67.md)<br>[mimo-mtp2-original-layer_split](mimo-mtp2-original-layer_split.md) | performance detail | Outcome unspecified | elapsed_seconds=57.53 s; end_to_end_accepted_tok_s=8.90 accepted tokens/s; output_tokens=512 tokens; ttft_seconds=41.86 s; p50_ms=28.57 ms; p95_ms=68.35 ms; prefill: per-request 785.35 tokens/s; Draft accepted / proposed: 282 / 460 tokens; fraction 0.6130 | Recorded configuration/job |
| [result-f2ede708d51fade8a477](../observations.json)<br>source-ba9f796abf51a2b048974408.json<br>`/waves/1` | [ab-mimo-mtp2-original-layer_split-matched-059](ab-mimo-mtp2-original-layer_split-matched-059.md)<br>[record-26c850ec689cf58c6b67](record-26c850ec689cf58c6b67.md)<br>[mimo-mtp2-original-layer_split](mimo-mtp2-original-layer_split.md) | performance detail | Outcome unspecified | elapsed_seconds=55.18 s; end_to_end_accepted_tok_s=37.11 accepted tokens/s; output_tokens=512 tokens; ttft_seconds=1.12<br>3.73<br>3.73<br>3.73 s; p50_ms=95.67 ms; p95_ms=228.97 ms; prefill: per-request 190.98 to 384.85 tokens/s; Draft accepted / proposed: 1,121 / 1,854 tokens; fraction 0.6046 | Recorded configuration/job |

These are saved result records, including failures and bounded checks. Copies, individual requests, report summaries and regrading can overlap; their counts are not independent test repetitions. Open each result for exact values, units, configuration binding and source receipts.

There are 1 retained lifecycle records. Their states, exit codes and configuration IDs remain in [catalog.json](../catalog.json); they do not supply missing benchmark results.

[Full archive](../../README.md) | [All retained waves](../RESULTS.md) | [Data definitions](../DATA.md) | [Recommended recipes](../../../README.md)
