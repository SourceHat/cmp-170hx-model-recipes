# ab-mimo-mtp3-original-layer_split-matched-060

**Historical record. Decode interval measured.**

Model family: MiMo V2.6 Flash.

Historical configurations are provided for comparison. The [recommended recipes](../../../README.md) include supported launch scripts.

Current recipes using the same recorded checkpoint repository: [mimo-flash-mtp1-tp3](../../../recipes/mimo-flash-mtp1-tp3/README.md). Context, cache and runtime versions can differ.

## Saved Configuration Versions

Each configuration ID identifies a distinct original settings record. Deployment fields are omitted; versions can have identical published settings after that omission. Upstream runtime commits remain unspecified where the source retained only an integration label.

| Configuration | Recorded artifact / source | Configured card counts | Context tokens | GPU pool tokens | Slots | Draft mode / tokens |
| --- | --- | --- | --- | --- | --- | --- |
| cfg-dbb2632a6db1ccc83d6c | [MikeRoz/MiMo-V2.6-Flash-MOPD-4.03bpw-h8-exl3@29c8351a8b](https://huggingface.co/MikeRoz/MiMo-V2.6-Flash-MOPD-4.03bpw-h8-exl3/tree/29c8351a8b5854ec385adaeba7bbe62c790d40ea) | 3 | 262,144 | 262,144 | 4 | mtp / 3 |

Card counts are saved configuration choices, not a claim that every allowed placement was measured. A derived view can differ from its pinned download source.

<details>
<summary>cfg-dbb2632a6db1ccc83d6c</summary>

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
| [ab-mimo-mtp3-original-layer_split-matched-060](ab-mimo-mtp3-original-layer_split-matched-060.md)<br>wave-291582985650aaddebab | layer_split; mtp / 3 | 1 | 32,765 | 512 (budget 512) | cold; reused 0 | 262,144 / 262,144 | 33.26 | Not recorded | 8.96 | 41.95 | Pass |
| [ab-mimo-mtp3-original-layer_split-matched-060](ab-mimo-mtp3-original-layer_split-matched-060.md)<br>wave-31a9ed0f5ac1c482ea02 | layer_split; mtp / 3 | 1 | 2,038 | 512 (budget 512) | cached_prefix; reused 1,792 | 262,144 / 262,144 | 42.77 | Not recorded | 41.02 | 0.67 | Pass |
| [ab-mimo-mtp3-original-layer_split-matched-060](ab-mimo-mtp3-original-layer_split-matched-060.md)<br>wave-5768f9600e78bb0a0d4b | layer_split; mtp / 3 | 1 | 2,038 | 512 (budget 512) | cold; reused 0 | 262,144 / 262,144 | 42.93 | Not recorded | 35.17 | 2.79 | Pass |
| [ab-mimo-mtp3-original-layer_split-matched-060](ab-mimo-mtp3-original-layer_split-matched-060.md)<br>wave-61cba6e83b811dfa2561 | layer_split; mtp / 3 | 4 | 2,039 | 512 (budget 512) | cached_prefix; reused 1,792 | 262,144 / 262,144 | 71.90 | Not recorded | 67.67 | 2.38 | Pass |
| [ab-mimo-mtp3-original-layer_split-matched-060](ab-mimo-mtp3-original-layer_split-matched-060.md)<br>wave-71ef20b9a1a55a69edf7 | layer_split; mtp / 3 | 1 | 32,765 | 512 (budget 512) | cached_prefix; reused 32,512 | 262,144 / 262,144 | 33.59 | Not recorded | 32.12 | 0.90 | Pass |
| [ab-mimo-mtp3-original-layer_split-matched-060](ab-mimo-mtp3-original-layer_split-matched-060.md)<br>wave-acf4b2b51fb7d19532c7 | layer_split; mtp / 3 | 4 | 2,039 | 512 (budget 512) | cold; reused 0 | 262,144 / 262,144 | 68.75 | Not recorded | 50.78 | 10.71 | Pass |
| [ab-mimo-mtp3-original-layer_split-matched-060](ab-mimo-mtp3-original-layer_split-matched-060.md)<br>wave-c55c4f6ffa25516185c2 | layer_split; mtp / 3 | 4 | 32,766 | 512 (budget 512) | cold; reused 0 | 262,144 / 262,144 | 42.81 | Not recorded | 9.53 | 167.54 | Pass |
| [ab-mimo-mtp3-original-layer_split-matched-060](ab-mimo-mtp3-original-layer_split-matched-060.md)<br>wave-f492c16415680b0da865 | layer_split; mtp / 3 | 4 | 32,766 | 512 (budget 512) | cached_prefix; reused 32,512 | 262,144 / 262,144 | 41.44 | Not recorded | 39.34 | 3.61 | Pass |

Rates are whole-wave totals over the stated request count. A wave may span multiple independent model instances; [measurements.json](../measurements.json) retains their contributions and the exact configuration IDs. Do not interpret a multi-instance total as one card's rate.

A dash in shared decode means no qualified synchronized interval is available. Whole-wave throughput includes prefill and queueing. A valid decode interval can survive inside an overall failed or partial check; the source-report outcome is preserved. No rows are averaged.

## Bounded Checks

| Check | Reported outcome | Retained counts / flags |
| --- | --- | --- |
| check-4f5c7800d90195f42fcc | Pass | {"passed":true,"elapsed_seconds":40.33452864699939,"ttft_seconds":[7.070831982004165,10.111317529997905,11.307260415997007,11.306597132002935],"end_to_end_accepted_tok_s":50.77535473201463} |
| check-5696e0d4949624e5f35f | Pass | {"passed":true,"elapsed_seconds":14.55791934300214,"ttft_seconds":[2.7935415579995606],"end_to_end_accepted_tok_s":35.169861017681335} |
| check-7ed1c340d3c475deb29e | Pass | {"passed":true,"elapsed_seconds":214.86815218399715,"ttft_seconds":[164.1142133100002,167.4234748040035,167.66663749999861,167.66632985600154],"end_to_end_accepted_tok_s":9.531426501244562} |
| check-a8f4e511b942871da2f8 | Pass | {"passed":true,"elapsed_seconds":40.33452864699939,"ttft_seconds":[7.070831982004165,10.111317529997905,11.307260415997007,11.306597132002935],"end_to_end_accepted_tok_s":50.77535473201463} |
| check-ae1b466f2c67a7180417 | Pass | {"passed":true,"elapsed_seconds":214.86815218399715,"ttft_seconds":[164.1142133100002,167.4234748040035,167.66663749999861,167.66632985600154],"end_to_end_accepted_tok_s":9.531426501244562} |
| check-af576c8ffc78448db522 | Pass | {"passed":true,"elapsed_seconds":57.1369037849945,"ttft_seconds":[41.95339798499481],"end_to_end_accepted_tok_s":8.960933583777132} |
| check-b24dc05ebaa499454ab9 | Pass | {"passed":true,"elapsed_seconds":14.55791934300214,"ttft_seconds":[2.7935415579995606],"end_to_end_accepted_tok_s":35.169861017681335} |
| check-eee344fd7996f8d8cbca | Pass | {"passed":true,"elapsed_seconds":57.1369037849945,"ttft_seconds":[41.95339798499481],"end_to_end_accepted_tok_s":8.960933583777132} |

These checks retain their reported scope. A context/allocation/retrieval check is not a general quality score or a speed qualification at that context. Exact flags and provenance are in [checks.json](../checks.json).

## Additional Test Results

| Result / Source | Profile | Evidence type | Reported outcome | Retained values | Configuration binding |
| --- | --- | --- | --- | --- | --- |
| [result-013c6cf6b7e74046bfda](../observations.json)<br>source-ce77a594e6cc1eebe7fc82a5.json<br>`/waves/1` | [ab-mimo-mtp3-original-layer_split-matched-060](ab-mimo-mtp3-original-layer_split-matched-060.md)<br>[record-26c850ec689cf58c6b67](record-26c850ec689cf58c6b67.md)<br>[mimo-mtp3-original-layer_split](mimo-mtp3-original-layer_split.md) | performance detail | Outcome unspecified | elapsed_seconds=15.94 s; end_to_end_accepted_tok_s=32.12 accepted tokens/s; output_tokens=512 tokens; ttft_seconds=0.90 s; p50_ms=27.42 ms; p95_ms=76.03 ms; prefill: per-request 341.89 tokens/s; Draft accepted / proposed: 314 / 594 tokens; fraction 0.5286 | Recorded configuration/job |
| [result-37658830bff97a1aa99e](../observations.json)<br>source-29ac72475ee13b76a0e91f7d.json<br>`/` | [ab-mimo-mtp3-original-layer_split-matched-060](ab-mimo-mtp3-original-layer_split-matched-060.md)<br>[record-26c850ec689cf58c6b67](record-26c850ec689cf58c6b67.md)<br>[mimo-mtp3-original-layer_split](mimo-mtp3-original-layer_split.md) | performance detail | Pass | elapsed_seconds=214.87 s; end_to_end_accepted_tok_s=9.53 accepted tokens/s; ttft_seconds=164.11<br>167.42<br>167.67<br>167.67 s; p50_ms=106.86 ms; p95_ms=245.34 ms; cold_prefill: per-request 200.21 to 202.27 tokens/s; Draft accepted / proposed: 1,229 / 2,457 tokens; fraction 0.5002 | Recorded configuration/job |
| [result-3e1bfcfd0a081e849415](../observations.json)<br>source-ce77a594e6cc1eebe7fc82a5.json<br>`/waves/0` | [ab-mimo-mtp3-original-layer_split-matched-060](ab-mimo-mtp3-original-layer_split-matched-060.md)<br>[record-26c850ec689cf58c6b67](record-26c850ec689cf58c6b67.md)<br>[mimo-mtp3-original-layer_split](mimo-mtp3-original-layer_split.md) | performance detail | Outcome unspecified | elapsed_seconds=57.14 s; end_to_end_accepted_tok_s=8.96 accepted tokens/s; output_tokens=512 tokens; ttft_seconds=41.95 s; p50_ms=27.19 ms; p95_ms=75.98 ms; prefill: per-request 784.23 tokens/s; Draft accepted / proposed: 314 / 594 tokens; fraction 0.5286 | Recorded configuration/job |
| [result-40bede833b524b4a5251](../observations.json)<br>source-91bf6bd7136f7cca26507424.json<br>`/waves/1` | [ab-mimo-mtp3-original-layer_split-matched-060](ab-mimo-mtp3-original-layer_split-matched-060.md)<br>[record-26c850ec689cf58c6b67](record-26c850ec689cf58c6b67.md)<br>[mimo-mtp3-original-layer_split](mimo-mtp3-original-layer_split.md) | performance detail | Outcome unspecified | elapsed_seconds=30.26 s; end_to_end_accepted_tok_s=67.67 accepted tokens/s; output_tokens=512 tokens; ttft_seconds=0.72<br>2.38<br>2.38<br>2.38 s; p50_ms=52.73 ms; p95_ms=148.76 ms; prefill: per-request 271.43 to 548.89 tokens/s; Draft accepted / proposed: 1,265 / 2,349 tokens; fraction 0.5385 | Recorded configuration/job |
| [result-49904be725746a0f7b38](../observations.json)<br>source-91bf6bd7136f7cca26507424.json<br>`/` | [ab-mimo-mtp3-original-layer_split-matched-060](ab-mimo-mtp3-original-layer_split-matched-060.md)<br>[record-26c850ec689cf58c6b67](record-26c850ec689cf58c6b67.md)<br>[mimo-mtp3-original-layer_split](mimo-mtp3-original-layer_split.md) | performance detail | Pass | elapsed_seconds=40.33 s; end_to_end_accepted_tok_s=50.78 accepted tokens/s; ttft_seconds=7.07<br>10.11<br>11.31<br>11.31 s; p50_ms=52.73 ms; p95_ms=148.76 ms; cold_prefill: per-request 266.19 to 389.12 tokens/s; Draft accepted / proposed: 1,265 / 2,349 tokens; fraction 0.5385 | Recorded configuration/job |
| [result-4a9cf351f73bfe235358](../observations.json)<br>source-91bf6bd7136f7cca26507424.json<br>`/waves/0` | [ab-mimo-mtp3-original-layer_split-matched-060](ab-mimo-mtp3-original-layer_split-matched-060.md)<br>[record-26c850ec689cf58c6b67](record-26c850ec689cf58c6b67.md)<br>[mimo-mtp3-original-layer_split](mimo-mtp3-original-layer_split.md) | performance detail | Outcome unspecified | elapsed_seconds=40.33 s; end_to_end_accepted_tok_s=50.78 accepted tokens/s; output_tokens=512 tokens; ttft_seconds=7.07<br>10.11<br>11.31<br>11.31 s; p50_ms=59.04 ms; p95_ms=151.10 ms; prefill: per-request 266.19 to 389.12 tokens/s; Draft accepted / proposed: 1,235 / 2,439 tokens; fraction 0.5064 | Recorded configuration/job |
| [result-5d53b75e5ae905c241f5](../observations.json)<br>source-29ac72475ee13b76a0e91f7d.json<br>`/waves/1` | [ab-mimo-mtp3-original-layer_split-matched-060](ab-mimo-mtp3-original-layer_split-matched-060.md)<br>[record-26c850ec689cf58c6b67](record-26c850ec689cf58c6b67.md)<br>[mimo-mtp3-original-layer_split](mimo-mtp3-original-layer_split.md) | performance detail | Outcome unspecified | elapsed_seconds=52.05 s; end_to_end_accepted_tok_s=39.34 accepted tokens/s; output_tokens=512 tokens; ttft_seconds=1.13<br>3.61<br>3.61<br>3.61 s; p50_ms=106.86 ms; p95_ms=245.34 ms; prefill: per-request 190.98 to 384.85 tokens/s; Draft accepted / proposed: 1,229 / 2,457 tokens; fraction 0.5002 | Recorded configuration/job |
| [result-66e85603b4fe83064414](../observations.json)<br>source-a9e622d351a86c8b776605d4.json<br>`/managed_phase_timings/60` | [ab-mimo-mtp3-original-layer_split-matched-060](ab-mimo-mtp3-original-layer_split-matched-060.md) | test outcome | Outcome unspecified | wall_seconds=766.63 s | Recorded configuration/job |
| [result-9d598b4811887b822d57](../observations.json)<br>source-ce77a594e6cc1eebe7fc82a5.json<br>`/` | [ab-mimo-mtp3-original-layer_split-matched-060](ab-mimo-mtp3-original-layer_split-matched-060.md)<br>[record-26c850ec689cf58c6b67](record-26c850ec689cf58c6b67.md)<br>[mimo-mtp3-original-layer_split](mimo-mtp3-original-layer_split.md) | performance detail | Pass | elapsed_seconds=57.14 s; end_to_end_accepted_tok_s=8.96 accepted tokens/s; ttft_seconds=41.95 s; p50_ms=27.42 ms; p95_ms=76.03 ms; cold_prefill: per-request 784.23 tokens/s; Draft accepted / proposed: 314 / 594 tokens; fraction 0.5286 | Recorded configuration/job |
| [result-9da9d5d3586494b90ef1](../observations.json)<br>source-99feb0abdf2ac0d4c511ad2a.json<br>`/waves/0` | [ab-mimo-mtp3-original-layer_split-matched-060](ab-mimo-mtp3-original-layer_split-matched-060.md)<br>[record-26c850ec689cf58c6b67](record-26c850ec689cf58c6b67.md)<br>[mimo-mtp3-original-layer_split](mimo-mtp3-original-layer_split.md) | performance detail | Outcome unspecified | elapsed_seconds=14.56 s; end_to_end_accepted_tok_s=35.17 accepted tokens/s; output_tokens=512 tokens; ttft_seconds=2.79 s; p50_ms=23.23 ms; p95_ms=59.42 ms; prefill: per-request 757.62 tokens/s; Draft accepted / proposed: 306 / 618 tokens; fraction 0.4951 | Recorded configuration/job |
| [result-b070107c7f3806dcdbc8](../observations.json)<br>source-29ac72475ee13b76a0e91f7d.json<br>`/waves/0` | [ab-mimo-mtp3-original-layer_split-matched-060](ab-mimo-mtp3-original-layer_split-matched-060.md)<br>[record-26c850ec689cf58c6b67](record-26c850ec689cf58c6b67.md)<br>[mimo-mtp3-original-layer_split](mimo-mtp3-original-layer_split.md) | performance detail | Outcome unspecified | elapsed_seconds=214.87 s; end_to_end_accepted_tok_s=9.53 accepted tokens/s; output_tokens=512 tokens; ttft_seconds=164.11<br>167.42<br>167.67<br>167.67 s; p50_ms=86.14 ms; p95_ms=239.80 ms; prefill: per-request 200.21 to 202.27 tokens/s; Draft accepted / proposed: 1,243 / 2,415 tokens; fraction 0.5147 | Recorded configuration/job |
| [result-b50430053f6ccbdc2863](../observations.json)<br>source-99feb0abdf2ac0d4c511ad2a.json<br>`/waves/1` | [ab-mimo-mtp3-original-layer_split-matched-060](ab-mimo-mtp3-original-layer_split-matched-060.md)<br>[record-26c850ec689cf58c6b67](record-26c850ec689cf58c6b67.md)<br>[mimo-mtp3-original-layer_split](mimo-mtp3-original-layer_split.md) | performance detail | Outcome unspecified | elapsed_seconds=12.48 s; end_to_end_accepted_tok_s=41.02 accepted tokens/s; output_tokens=512 tokens; ttft_seconds=0.67 s; p50_ms=23.50 ms; p95_ms=58.84 ms; prefill: per-request 447.27 tokens/s; Draft accepted / proposed: 306 / 618 tokens; fraction 0.4951 | Recorded configuration/job |
| [result-b61bd51a3ead23f3b053](../observations.json)<br>source-99feb0abdf2ac0d4c511ad2a.json<br>`/` | [ab-mimo-mtp3-original-layer_split-matched-060](ab-mimo-mtp3-original-layer_split-matched-060.md)<br>[record-26c850ec689cf58c6b67](record-26c850ec689cf58c6b67.md)<br>[mimo-mtp3-original-layer_split](mimo-mtp3-original-layer_split.md) | performance detail | Pass | elapsed_seconds=14.56 s; end_to_end_accepted_tok_s=35.17 accepted tokens/s; ttft_seconds=2.79 s; p50_ms=23.50 ms; p95_ms=58.84 ms; cold_prefill: per-request 757.62 tokens/s; Draft accepted / proposed: 306 / 618 tokens; fraction 0.4951 | Recorded configuration/job |

These are saved result records, including failures and bounded checks. Copies, individual requests, report summaries and regrading can overlap; their counts are not independent test repetitions. Open each result for exact values, units, configuration binding and source receipts.

There are 1 retained lifecycle records. Their states, exit codes and configuration IDs remain in [catalog.json](../catalog.json); they do not supply missing benchmark results.

[Full archive](../../README.md) | [All retained waves](../RESULTS.md) | [Data definitions](../DATA.md) | [Recommended recipes](../../../README.md)
