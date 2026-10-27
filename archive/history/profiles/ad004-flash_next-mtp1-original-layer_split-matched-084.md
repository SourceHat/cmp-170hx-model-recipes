# ad004-flash_next-mtp1-original-layer_split-matched-084

**Historical record. Decode interval measured.**

Model family: Qwen 3.8 Flash Next.

Historical configurations are provided for comparison. The [recommended recipes](../../../README.md) include supported launch scripts.

Current recipes using the same recorded checkpoint repository: [qwen-flash-next-mtp2-layer-split](../../../recipes/qwen-flash-next-mtp2-layer-split/README.md). Context, cache and runtime versions can differ.

## Saved Configuration Versions

Each configuration ID identifies a distinct original settings record. Deployment fields are omitted; versions can have identical published settings after that omission. Upstream runtime commits remain unspecified where the source retained only an integration label.

| Configuration | Recorded artifact / source | Configured card counts | Context tokens | GPU pool tokens | Slots | Draft mode / tokens |
| --- | --- | --- | --- | --- | --- | --- |
| cfg-fd10d2aefedd517a0022 | [turboderp/Qwen3.8-Flash-Next-exl3@d2e238feca](https://huggingface.co/turboderp/Qwen3.8-Flash-Next-exl3/tree/d2e238feca4c1c4d966943117356d8a42c2f4dcb) | 2 | 262,144 | 262,144 | 6 | mtp / 1 |

Card counts are saved configuration choices, not a claim that every allowed placement was measured. A derived view can differ from its pinned download source.

<details>
<summary>cfg-fd10d2aefedd517a0022</summary>

```json
{
  "kind": "tabby",
  "gpu_counts": [
    2
  ],
  "context": 262144,
  "cache_tokens": 262144,
  "cache_mode": "Q8",
  "draft_cache_mode": "Q8",
  "draft_mode": "mtp",
  "draft_tokens": 1,
  "max_sessions": 6,
  "chunk_size": 512,
  "reserve_mib": 2048,
  "ram_kv_mib": 8192,
  "ram_recurrent_mib": 16384,
  "ngram_ram": true,
  "dynamic_draft": false,
  "output_chunk_tokens": 4096,
  "power_watts": 200,
  "host_memory_gib": 80,
  "host_swap_gib": 0,
  "min_vram_mib_per_gpu": 65530,
  "min_effective_vram_mib": 131060,
  "parallelism": "layer_split",
  "transport": "host",
  "host_backing": "ordinary",
  "model_repository": "turboderp/Qwen3.8-Flash-Next-exl3",
  "model_revision": "d2e238feca4c1c4d966943117356d8a42c2f4dcb",
  "draft_repository": null,
  "draft_revision": null,
  "recorded_runtime_label": null,
  "served_model_label": "qwen3.8-flash-next"
}
```

Pinned model revision recorded: yes. Source receipt labels, hashes and object locators are retained in [configurations.json](../configurations.json).

</details>

## Retained Measurements

| Profile / Wave | Layout; Draft / Tokens | Requests | Input tokens/request | Accepted output tokens/request | Cache / Reused input tokens | Context / GPU pool tokens | Shared decode tok/s total | Client after-first-token estimate tok/s | Whole-wave output tok/s | Median TTFT, s | Source report |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [ad004-flash_next-mtp1-original-layer_split-matched-084](ad004-flash_next-mtp1-original-layer_split-matched-084.md)<br>wave-15946c998231039e926b | layer_split; mtp / 1 | 6 | 32,770 | 256 (budget 256) | cold; reused 0 | 262,144 / 262,144 | 123.53 | Not recorded | 9.61 | 147.58 | Pass |
| [ad004-flash_next-mtp1-original-layer_split-matched-084](ad004-flash_next-mtp1-original-layer_split-matched-084.md)<br>wave-2d611b85711dc69efff0 | layer_split; mtp / 1 | 1 | 32,769 | 256 (budget 256) | repeated_input; reused 0 | 262,144 / 262,144 | 64.33 | Not recorded | 8.98 | 24.60 | Pass |
| [ad004-flash_next-mtp1-original-layer_split-matched-084](ad004-flash_next-mtp1-original-layer_split-matched-084.md)<br>wave-4ed3a2e80e879b5c39a7 | layer_split; mtp / 1 | 6 | 32,770 | 256 (budget 256) | cached_prefix; reused 32,768 | 262,144 / 262,144 | 123.80 | Not recorded | 116.28 | 1.02 | Pass |
| [ad004-flash_next-mtp1-original-layer_split-matched-084](ad004-flash_next-mtp1-original-layer_split-matched-084.md)<br>wave-e6a6d1db1fa49ff00659 | layer_split; mtp / 1 | 1 | 32,769 | 256 (budget 256) | cold; reused 0 | 262,144 / 262,144 | 64.31 | Not recorded | 8.98 | 24.58 | Pass |

Rates are whole-wave totals over the stated request count. A wave may span multiple independent model instances; [measurements.json](../measurements.json) retains their contributions and the exact configuration IDs. Do not interpret a multi-instance total as one card's rate.

A dash in shared decode means no qualified synchronized interval is available. Whole-wave throughput includes prefill and queueing. A valid decode interval can survive inside an overall failed or partial check; the source-report outcome is preserved. No rows are averaged.

## Bounded Checks

| Check | Reported outcome | Retained counts / flags |
| --- | --- | --- |
| check-282f5e235ad69ce4b662 | Pass | {"passed":true,"elapsed_seconds":159.8766058389956,"ttft_seconds":[144.77049693900335,147.58428094300325,147.58442758900492,147.58412039199902,147.71050306899997,147.70977529599622],"end_to_end_accepted_tok_s":9.607409363861747} |
| check-814f27cfec9933399746 | Pass | {"passed":true,"elapsed_seconds":28.495768149005016,"ttft_seconds":[24.575984178998624],"end_to_end_accepted_tok_s":8.983790107407184} |
| check-89555b77c0f28bcdbdf5 | Pass | {"passed":true,"elapsed_seconds":159.8766058389956,"ttft_seconds":[144.77049693900335,147.58428094300325,147.58442758900492,147.58412039199902,147.71050306899997,147.70977529599622],"end_to_end_accepted_tok_s":9.607409363861747} |
| check-d8cbd88422e56fd57e30 | Pass | {"passed":true,"elapsed_seconds":28.495768149005016,"ttft_seconds":[24.575984178998624],"end_to_end_accepted_tok_s":8.983790107407184} |

These checks retain their reported scope. A context/allocation/retrieval check is not a general quality score or a speed qualification at that context. Exact flags and provenance are in [checks.json](../checks.json).

## Additional Test Results

| Result / Source | Profile | Evidence type | Reported outcome | Retained values | Configuration binding |
| --- | --- | --- | --- | --- | --- |
| [result-083d8c3ea07604d1d729](../observations.json)<br>source-92c723f58caef6cbb3e61cb8.json<br>`/` | [ad004-flash_next-mtp1-original-layer_split-matched-084](ad004-flash_next-mtp1-original-layer_split-matched-084.md)<br>[record-26c850ec689cf58c6b67](record-26c850ec689cf58c6b67.md)<br>[flash_next-mtp1-original-layer_split](flash_next-mtp1-original-layer_split.md) | performance detail | Pass | elapsed_seconds=159.88 s; end_to_end_accepted_tok_s=9.61 accepted tokens/s; ttft_seconds=144.77<br>147.58<br>147.58<br>147.58<br>147.71<br>147.71 s; p50_ms=45.18 ms; p95_ms=91.39 ms; cold_prefill: per-request 225.78 to 230.05 tokens/s; Draft accepted / proposed: 715 / 821 tokens; fraction 0.8709 | Recorded configuration/job |
| [result-2db82ef2351575bff42b](../observations.json)<br>source-ba2f2da562f6767d915ca9d7.json<br>`/waves/0` | [ad004-flash_next-mtp1-original-layer_split-matched-084](ad004-flash_next-mtp1-original-layer_split-matched-084.md)<br>[record-26c850ec689cf58c6b67](record-26c850ec689cf58c6b67.md)<br>[flash_next-mtp1-original-layer_split](flash_next-mtp1-original-layer_split.md) | performance detail | Outcome unspecified | elapsed_seconds=28.50 s; end_to_end_accepted_tok_s=8.98 accepted tokens/s; output_tokens=256 tokens; ttft_seconds=24.58 s; p50_ms=14.53 ms; p95_ms=28.40 ms; prefill: per-request 1,338.06 tokens/s; Draft accepted / proposed: 119 / 137 tokens; fraction 0.8686 | Recorded configuration/job |
| [result-366f0edfbbd5ee1251b6](../observations.json)<br>source-a9e622d351a86c8b776605d4.json<br>`/managed_phase_timings/84` | [ad004-flash_next-mtp1-original-layer_split-matched-084](ad004-flash_next-mtp1-original-layer_split-matched-084.md) | test outcome | Outcome unspecified | wall_seconds=511.64 s | Recorded configuration/job |
| [result-6e302c65ca7075a3d1cd](../observations.json)<br>source-ba2f2da562f6767d915ca9d7.json<br>`/` | [ad004-flash_next-mtp1-original-layer_split-matched-084](ad004-flash_next-mtp1-original-layer_split-matched-084.md)<br>[record-26c850ec689cf58c6b67](record-26c850ec689cf58c6b67.md)<br>[flash_next-mtp1-original-layer_split](flash_next-mtp1-original-layer_split.md) | performance detail | Pass | elapsed_seconds=28.50 s; end_to_end_accepted_tok_s=8.98 accepted tokens/s; ttft_seconds=24.58 s; p50_ms=14.54 ms; p95_ms=28.42 ms; cold_prefill: per-request 1,338.06 tokens/s; Draft accepted / proposed: 119 / 137 tokens; fraction 0.8686 | Recorded configuration/job |
| [result-c7b6fa733d025b184f31](../observations.json)<br>source-92c723f58caef6cbb3e61cb8.json<br>`/waves/1` | [ad004-flash_next-mtp1-original-layer_split-matched-084](ad004-flash_next-mtp1-original-layer_split-matched-084.md)<br>[record-26c850ec689cf58c6b67](record-26c850ec689cf58c6b67.md)<br>[flash_next-mtp1-original-layer_split](flash_next-mtp1-original-layer_split.md) | performance detail | Outcome unspecified | elapsed_seconds=13.21 s; end_to_end_accepted_tok_s=116.28 accepted tokens/s; output_tokens=256 tokens; ttft_seconds=0.30<br>1.02<br>1.02<br>1.02<br>1.10<br>1.10 s; p50_ms=45.18 ms; p95_ms=91.39 ms; prefill: per-request 50.00 to 100.00 tokens/s; Draft accepted / proposed: 715 / 821 tokens; fraction 0.8709 | Recorded configuration/job |
| [result-e1e11e64eb86f657da75](../observations.json)<br>source-ba2f2da562f6767d915ca9d7.json<br>`/waves/1` | [ad004-flash_next-mtp1-original-layer_split-matched-084](ad004-flash_next-mtp1-original-layer_split-matched-084.md)<br>[record-26c850ec689cf58c6b67](record-26c850ec689cf58c6b67.md)<br>[flash_next-mtp1-original-layer_split](flash_next-mtp1-original-layer_split.md) | performance detail | Outcome unspecified | elapsed_seconds=28.51 s; end_to_end_accepted_tok_s=8.98 accepted tokens/s; output_tokens=256 tokens; ttft_seconds=24.60 s; p50_ms=14.54 ms; p95_ms=28.42 ms; prefill: per-request 1,336.96 tokens/s; Draft accepted / proposed: 119 / 137 tokens; fraction 0.8686 | Recorded configuration/job |
| [result-e3bab27da5f34d43af2c](../observations.json)<br>source-92c723f58caef6cbb3e61cb8.json<br>`/waves/0` | [ad004-flash_next-mtp1-original-layer_split-matched-084](ad004-flash_next-mtp1-original-layer_split-matched-084.md)<br>[record-26c850ec689cf58c6b67](record-26c850ec689cf58c6b67.md)<br>[flash_next-mtp1-original-layer_split](flash_next-mtp1-original-layer_split.md) | performance detail | Outcome unspecified | elapsed_seconds=159.88 s; end_to_end_accepted_tok_s=9.61 accepted tokens/s; output_tokens=256 tokens; ttft_seconds=144.77<br>147.58<br>147.58<br>147.58<br>147.71<br>147.71 s; p50_ms=45.87 ms; p95_ms=93.58 ms; prefill: per-request 225.78 to 230.05 tokens/s; Draft accepted / proposed: 703 / 833 tokens; fraction 0.8439 | Recorded configuration/job |

These are saved result records, including failures and bounded checks. Copies, individual requests, report summaries and regrading can overlap; their counts are not independent test repetitions. Open each result for exact values, units, configuration binding and source receipts.

There are 1 retained lifecycle records. Their states, exit codes and configuration IDs remain in [catalog.json](../catalog.json); they do not supply missing benchmark results.

[Full archive](../../README.md) | [All retained waves](../RESULTS.md) | [Data definitions](../DATA.md) | [Recommended recipes](../../../README.md)
