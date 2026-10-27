# ab-mimo-mtp1-original-layer_split-matched-058

**Historical record. Decode interval measured.**

Model family: MiMo V2.6 Flash.

Historical configurations are provided for comparison. The [recommended recipes](../../../README.md) include supported launch scripts.

Current recipes using the same recorded checkpoint repository: [mimo-flash-mtp1-tp3](../../../recipes/mimo-flash-mtp1-tp3/README.md). Context, cache and runtime versions can differ.

## Saved Configuration Versions

Each configuration ID identifies a distinct original settings record. Deployment fields are omitted; versions can have identical published settings after that omission. Upstream runtime commits remain unspecified where the source retained only an integration label.

| Configuration | Recorded artifact / source | Configured card counts | Context tokens | GPU pool tokens | Slots | Draft mode / tokens |
| --- | --- | --- | --- | --- | --- | --- |
| cfg-5c7d162a53b4f9641b0e | [MikeRoz/MiMo-V2.6-Flash-MOPD-4.03bpw-h8-exl3@29c8351a8b](https://huggingface.co/MikeRoz/MiMo-V2.6-Flash-MOPD-4.03bpw-h8-exl3/tree/29c8351a8b5854ec385adaeba7bbe62c790d40ea) | 3 | 262,144 | 262,144 | 4 | mtp / 1 |

Card counts are saved configuration choices, not a claim that every allowed placement was measured. A derived view can differ from its pinned download source.

<details>
<summary>cfg-5c7d162a53b4f9641b0e</summary>

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
  "draft_tokens": 1,
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
| [ab-mimo-mtp1-original-layer_split-matched-058](ab-mimo-mtp1-original-layer_split-matched-058.md)<br>wave-0abd1735bf9377b76916 | layer_split; mtp / 1 | 1 | 2,038 | 512 (budget 512) | cold; reused 0 | 262,144 / 262,144 | 41.93 | Not recorded | 34.31 | 2.80 | Pass |
| [ab-mimo-mtp1-original-layer_split-matched-058](ab-mimo-mtp1-original-layer_split-matched-058.md)<br>wave-591072b2d4de9494d79b | layer_split; mtp / 1 | 4 | 2,039 | 512 (budget 512) | cold; reused 0 | 262,144 / 262,144 | 82.34 | Not recorded | 57.43 | 10.93 | Pass |
| [ab-mimo-mtp1-original-layer_split-matched-058](ab-mimo-mtp1-original-layer_split-matched-058.md)<br>wave-62b3b105dd263cc74188 | layer_split; mtp / 1 | 1 | 32,765 | 512 (budget 512) | cached_prefix; reused 32,512 | 262,144 / 262,144 | 33.23 | Not recorded | 31.44 | 0.96 | Pass |
| [ab-mimo-mtp1-original-layer_split-matched-058](ab-mimo-mtp1-original-layer_split-matched-058.md)<br>wave-73cbbac770b818433882 | layer_split; mtp / 1 | 1 | 2,038 | 512 (budget 512) | cached_prefix; reused 1,792 | 262,144 / 262,144 | 41.82 | Not recorded | 40.07 | 0.62 | Pass |
| [ab-mimo-mtp1-original-layer_split-matched-058](ab-mimo-mtp1-original-layer_split-matched-058.md)<br>wave-c4e8689a9e36b33fe21e | layer_split; mtp / 1 | 1 | 32,765 | 512 (budget 512) | cold; reused 0 | 262,144 / 262,144 | 33.23 | Not recorded | 8.96 | 41.80 | Pass |
| [ab-mimo-mtp1-original-layer_split-matched-058](ab-mimo-mtp1-original-layer_split-matched-058.md)<br>wave-cba7973e513ff6ea8805 | layer_split; mtp / 1 | 4 | 2,039 | 512 (budget 512) | cached_prefix; reused 1,792 | 262,144 / 262,144 | 83.52 | Not recorded | 76.99 | 2.27 | Pass |
| [ab-mimo-mtp1-original-layer_split-matched-058](ab-mimo-mtp1-original-layer_split-matched-058.md)<br>wave-d48a837fbeffa0328fea | layer_split; mtp / 1 | 4 | 32,766 | 512 (budget 512) | cached_prefix; reused 32,512 | 262,144 / 262,144 | 56.05 | Not recorded | 51.65 | 3.46 | Pass |
| [ab-mimo-mtp1-original-layer_split-matched-058](ab-mimo-mtp1-original-layer_split-matched-058.md)<br>wave-ea7311c4c0691abdc642 | layer_split; mtp / 1 | 4 | 32,766 | 512 (budget 512) | cold; reused 0 | 262,144 / 262,144 | 57.29 | Not recorded | 10.10 | 167.30 | Pass |

Rates are whole-wave totals over the stated request count. A wave may span multiple independent model instances; [measurements.json](../measurements.json) retains their contributions and the exact configuration IDs. Do not interpret a multi-instance total as one card's rate.

A dash in shared decode means no qualified synchronized interval is available. Whole-wave throughput includes prefill and queueing. A valid decode interval can survive inside an overall failed or partial check; the source-report outcome is preserved. No rows are averaged.

## Bounded Checks

| Check | Reported outcome | Retained counts / flags |
| --- | --- | --- |
| check-4cef539eeb8a1fd1ea8f | Pass | {"passed":true,"elapsed_seconds":202.7132909560023,"ttft_seconds":[158.57482437699946,167.30134527400514,167.30099527200218,167.45662629199796],"end_to_end_accepted_tok_s":10.10293893578249} |
| check-561415fe7b76e997588c | Pass | {"passed":true,"elapsed_seconds":14.922405666999111,"ttft_seconds":[2.804604349999863],"end_to_end_accepted_tok_s":34.310821688240765} |
| check-6ff48deeddc74c75fa43 | Pass | {"passed":true,"elapsed_seconds":57.12074183099321,"ttft_seconds":[41.80034529799741],"end_to_end_accepted_tok_s":8.963469023474644} |
| check-ad044d29ffb5ee3ef110 | Pass | {"passed":true,"elapsed_seconds":14.922405666999111,"ttft_seconds":[2.804604349999863],"end_to_end_accepted_tok_s":34.310821688240765} |
| check-c7c66edb08dcce242457 | Pass | {"passed":true,"elapsed_seconds":202.7132909560023,"ttft_seconds":[158.57482437699946,167.30134527400514,167.30099527200218,167.45662629199796],"end_to_end_accepted_tok_s":10.10293893578249} |
| check-ca5950d0496c31e4cc16 | Pass | {"passed":true,"elapsed_seconds":35.65946436700324,"ttft_seconds":[8.6172579280028,10.92623761199502,10.926738408001256,10.926313896998181],"end_to_end_accepted_tok_s":57.43215823216558} |
| check-d97d15aee9bacb938be0 | Pass | {"passed":true,"elapsed_seconds":35.65946436700324,"ttft_seconds":[8.6172579280028,10.92623761199502,10.926738408001256,10.926313896998181],"end_to_end_accepted_tok_s":57.43215823216558} |
| check-e8835840b7f3484be73c | Pass | {"passed":true,"elapsed_seconds":57.12074183099321,"ttft_seconds":[41.80034529799741],"end_to_end_accepted_tok_s":8.963469023474644} |

These checks retain their reported scope. A context/allocation/retrieval check is not a general quality score or a speed qualification at that context. Exact flags and provenance are in [checks.json](../checks.json).

## Additional Test Results

| Result / Source | Profile | Evidence type | Reported outcome | Retained values | Configuration binding |
| --- | --- | --- | --- | --- | --- |
| [result-0798a14561b580061269](../observations.json)<br>source-4ed034502968f784389461fc.json<br>`/waves/1` | [ab-mimo-mtp1-original-layer_split-matched-058](ab-mimo-mtp1-original-layer_split-matched-058.md)<br>[record-26c850ec689cf58c6b67](record-26c850ec689cf58c6b67.md)<br>[mimo-mtp1-original-layer_split](mimo-mtp1-original-layer_split.md) | performance detail | Outcome unspecified | elapsed_seconds=26.60 s; end_to_end_accepted_tok_s=76.99 accepted tokens/s; output_tokens=512 tokens; ttft_seconds=0.68<br>2.27<br>2.27<br>2.27 s; p50_ms=45.46 ms; p95_ms=89.34 ms; prefill: per-request 277.53 to 561.36 tokens/s; Draft accepted / proposed: 902 / 1,146 tokens; fraction 0.7871 | Recorded configuration/job |
| [result-2a7ddae484d2a6a0a489](../observations.json)<br>source-e843197328a56ffa7d94b72c.json<br>`/waves/1` | [ab-mimo-mtp1-original-layer_split-matched-058](ab-mimo-mtp1-original-layer_split-matched-058.md)<br>[record-26c850ec689cf58c6b67](record-26c850ec689cf58c6b67.md)<br>[mimo-mtp1-original-layer_split](mimo-mtp1-original-layer_split.md) | performance detail | Outcome unspecified | elapsed_seconds=12.78 s; end_to_end_accepted_tok_s=40.07 accepted tokens/s; output_tokens=512 tokens; ttft_seconds=0.62 s; p50_ms=21.95 ms; p95_ms=42.42 ms; prefill: per-request 439.29 tokens/s; Draft accepted / proposed: 219 / 293 tokens; fraction 0.7474 | Recorded configuration/job |
| [result-3e3305bfdfa8b50385f2](../observations.json)<br>source-4ed034502968f784389461fc.json<br>`/waves/0` | [ab-mimo-mtp1-original-layer_split-matched-058](ab-mimo-mtp1-original-layer_split-matched-058.md)<br>[record-26c850ec689cf58c6b67](record-26c850ec689cf58c6b67.md)<br>[mimo-mtp1-original-layer_split](mimo-mtp1-original-layer_split.md) | performance detail | Outcome unspecified | elapsed_seconds=35.66 s; end_to_end_accepted_tok_s=57.43 accepted tokens/s; output_tokens=512 tokens; ttft_seconds=8.62<br>10.93<br>10.93<br>10.93 s; p50_ms=45.97 ms; p95_ms=89.90 ms; prefill: per-request 269.00 to 392.12 tokens/s; Draft accepted / proposed: 898 / 1,150 tokens; fraction 0.7809 | Recorded configuration/job |
| [result-47c0e023cec8d957a9a4](../observations.json)<br>source-60fae1dfd4e991f95596acb2.json<br>`/waves/0` | [ab-mimo-mtp1-original-layer_split-matched-058](ab-mimo-mtp1-original-layer_split-matched-058.md)<br>[record-26c850ec689cf58c6b67](record-26c850ec689cf58c6b67.md)<br>[mimo-mtp1-original-layer_split](mimo-mtp1-original-layer_split.md) | performance detail | Outcome unspecified | elapsed_seconds=202.71 s; end_to_end_accepted_tok_s=10.10 accepted tokens/s; output_tokens=512 tokens; ttft_seconds=158.57<br>167.30<br>167.30<br>167.46 s; p50_ms=64.00 ms; p95_ms=124.73 ms; prefill: per-request 200.91 to 206.79 tokens/s; Draft accepted / proposed: 900 / 1,148 tokens; fraction 0.7840 | Recorded configuration/job |
| [result-6c031b2017bc2074356e](../observations.json)<br>source-e843197328a56ffa7d94b72c.json<br>`/` | [ab-mimo-mtp1-original-layer_split-matched-058](ab-mimo-mtp1-original-layer_split-matched-058.md)<br>[record-26c850ec689cf58c6b67](record-26c850ec689cf58c6b67.md)<br>[mimo-mtp1-original-layer_split](mimo-mtp1-original-layer_split.md) | performance detail | Pass | elapsed_seconds=14.92 s; end_to_end_accepted_tok_s=34.31 accepted tokens/s; ttft_seconds=2.80 s; p50_ms=21.95 ms; p95_ms=42.42 ms; cold_prefill: per-request 738.41 tokens/s; Draft accepted / proposed: 219 / 293 tokens; fraction 0.7474 | Recorded configuration/job |
| [result-6cea0f4d0878453e8557](../observations.json)<br>source-a9e622d351a86c8b776605d4.json<br>`/managed_phase_timings/58` | [ab-mimo-mtp1-original-layer_split-matched-058](ab-mimo-mtp1-original-layer_split-matched-058.md) | test outcome | Outcome unspecified | wall_seconds=743.22 s | Recorded configuration/job |
| [result-7266a6621ae2cfd58a1a](../observations.json)<br>source-5d0c9ea22147c80126472c42.json<br>`/` | [ab-mimo-mtp1-original-layer_split-matched-058](ab-mimo-mtp1-original-layer_split-matched-058.md)<br>[record-26c850ec689cf58c6b67](record-26c850ec689cf58c6b67.md)<br>[mimo-mtp1-original-layer_split](mimo-mtp1-original-layer_split.md) | performance detail | Pass | elapsed_seconds=57.12 s; end_to_end_accepted_tok_s=8.96 accepted tokens/s; ttft_seconds=41.80 s; p50_ms=27.55 ms; p95_ms=51.74 ms; cold_prefill: per-request 786.11 tokens/s; Draft accepted / proposed: 218 / 294 tokens; fraction 0.7415 | Recorded configuration/job |
| [result-73f428c31bcaccaf089e](../observations.json)<br>source-e843197328a56ffa7d94b72c.json<br>`/waves/0` | [ab-mimo-mtp1-original-layer_split-matched-058](ab-mimo-mtp1-original-layer_split-matched-058.md)<br>[record-26c850ec689cf58c6b67](record-26c850ec689cf58c6b67.md)<br>[mimo-mtp1-original-layer_split](mimo-mtp1-original-layer_split.md) | performance detail | Outcome unspecified | elapsed_seconds=14.92 s; end_to_end_accepted_tok_s=34.31 accepted tokens/s; output_tokens=512 tokens; ttft_seconds=2.80 s; p50_ms=21.80 ms; p95_ms=42.17 ms; prefill: per-request 738.41 tokens/s; Draft accepted / proposed: 219 / 293 tokens; fraction 0.7474 | Recorded configuration/job |
| [result-78434a1097a35c7e8fdc](../observations.json)<br>source-4ed034502968f784389461fc.json<br>`/` | [ab-mimo-mtp1-original-layer_split-matched-058](ab-mimo-mtp1-original-layer_split-matched-058.md)<br>[record-26c850ec689cf58c6b67](record-26c850ec689cf58c6b67.md)<br>[mimo-mtp1-original-layer_split](mimo-mtp1-original-layer_split.md) | performance detail | Pass | elapsed_seconds=35.66 s; end_to_end_accepted_tok_s=57.43 accepted tokens/s; ttft_seconds=8.62<br>10.93<br>10.93<br>10.93 s; p50_ms=45.46 ms; p95_ms=89.34 ms; cold_prefill: per-request 269.00 to 392.12 tokens/s; Draft accepted / proposed: 902 / 1,146 tokens; fraction 0.7871 | Recorded configuration/job |
| [result-a96ac28b4f5637d2051b](../observations.json)<br>source-5d0c9ea22147c80126472c42.json<br>`/waves/1` | [ab-mimo-mtp1-original-layer_split-matched-058](ab-mimo-mtp1-original-layer_split-matched-058.md)<br>[record-26c850ec689cf58c6b67](record-26c850ec689cf58c6b67.md)<br>[mimo-mtp1-original-layer_split](mimo-mtp1-original-layer_split.md) | performance detail | Outcome unspecified | elapsed_seconds=16.28 s; end_to_end_accepted_tok_s=31.44 accepted tokens/s; output_tokens=512 tokens; ttft_seconds=0.96 s; p50_ms=27.55 ms; p95_ms=51.74 ms; prefill: per-request 332.89 tokens/s; Draft accepted / proposed: 218 / 294 tokens; fraction 0.7415 | Recorded configuration/job |
| [result-bc3b20061f529218ce37](../observations.json)<br>source-60fae1dfd4e991f95596acb2.json<br>`/waves/1` | [ab-mimo-mtp1-original-layer_split-matched-058](ab-mimo-mtp1-original-layer_split-matched-058.md)<br>[record-26c850ec689cf58c6b67](record-26c850ec689cf58c6b67.md)<br>[mimo-mtp1-original-layer_split](mimo-mtp1-original-layer_split.md) | performance detail | Outcome unspecified | elapsed_seconds=39.65 s; end_to_end_accepted_tok_s=51.65 accepted tokens/s; output_tokens=512 tokens; ttft_seconds=1.03<br>3.46<br>3.46<br>3.46 s; p50_ms=64.08 ms; p95_ms=126.12 ms; prefill: per-request 192.42 to 384.85 tokens/s; Draft accepted / proposed: 874 / 1,174 tokens; fraction 0.7445 | Recorded configuration/job |
| [result-bf6b2baa5acf3b66973d](../observations.json)<br>source-60fae1dfd4e991f95596acb2.json<br>`/` | [ab-mimo-mtp1-original-layer_split-matched-058](ab-mimo-mtp1-original-layer_split-matched-058.md)<br>[record-26c850ec689cf58c6b67](record-26c850ec689cf58c6b67.md)<br>[mimo-mtp1-original-layer_split](mimo-mtp1-original-layer_split.md) | performance detail | Pass | elapsed_seconds=202.71 s; end_to_end_accepted_tok_s=10.10 accepted tokens/s; ttft_seconds=158.57<br>167.30<br>167.30<br>167.46 s; p50_ms=64.08 ms; p95_ms=126.12 ms; cold_prefill: per-request 200.91 to 206.79 tokens/s; Draft accepted / proposed: 874 / 1,174 tokens; fraction 0.7445 | Recorded configuration/job |
| [result-ff1be2f4404ab09cc9d9](../observations.json)<br>source-5d0c9ea22147c80126472c42.json<br>`/waves/0` | [ab-mimo-mtp1-original-layer_split-matched-058](ab-mimo-mtp1-original-layer_split-matched-058.md)<br>[record-26c850ec689cf58c6b67](record-26c850ec689cf58c6b67.md)<br>[mimo-mtp1-original-layer_split](mimo-mtp1-original-layer_split.md) | performance detail | Outcome unspecified | elapsed_seconds=57.12 s; end_to_end_accepted_tok_s=8.96 accepted tokens/s; output_tokens=512 tokens; ttft_seconds=41.80 s; p50_ms=27.50 ms; p95_ms=51.93 ms; prefill: per-request 786.11 tokens/s; Draft accepted / proposed: 218 / 294 tokens; fraction 0.7415 | Recorded configuration/job |

These are saved result records, including failures and bounded checks. Copies, individual requests, report summaries and regrading can overlap; their counts are not independent test repetitions. Open each result for exact values, units, configuration binding and source receipts.

There are 1 retained lifecycle records. Their states, exit codes and configuration IDs remain in [catalog.json](../catalog.json); they do not supply missing benchmark results.

[Full archive](../../README.md) | [All retained waves](../RESULTS.md) | [Data definitions](../DATA.md) | [Recommended recipes](../../../README.md)
