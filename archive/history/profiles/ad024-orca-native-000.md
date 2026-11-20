# ad024-orca-native-000

**Historical record. Decode interval measured.**

Model family: Orca (Qwen 3.8 27B abliterated).

Historical configurations are provided for comparison. The [recommended recipes](../../../README.md) include supported launch scripts.

Current recipes using the same recorded checkpoint repository: [qwen27-orca-mtp3-native](../../../recipes/qwen27-orca-mtp3-native/README.md). Context, cache and runtime versions can differ.

## Saved Configuration Versions

Each configuration ID identifies a distinct original settings record. Deployment fields are omitted; versions can have identical published settings after that omission. Upstream runtime commits remain unspecified where the source retained only an integration label.

| Configuration | Recorded artifact / source | Configured card counts | Context tokens | GPU pool tokens | Slots | Draft mode / tokens |
| --- | --- | --- | --- | --- | --- | --- |
| cfg-b53031acebd92a7f3ad5 | [Lygodactylus/Qwen3.8-27B-Uncensored-exl3-8bpw@3487b152b3](https://huggingface.co/Lygodactylus/Qwen3.8-27B-Uncensored-exl3-8bpw/tree/3487b152b302930e303dc4a2e99e7e976e3ad28f) | 1 | 262,144 | 866,560 | 8 | mtp / 3 |
| cfg-db175da157819da2b96c | [Lygodactylus/Qwen3.8-27B-Uncensored-exl3-8bpw@3487b152b3](https://huggingface.co/Lygodactylus/Qwen3.8-27B-Uncensored-exl3-8bpw/tree/3487b152b302930e303dc4a2e99e7e976e3ad28f) | 1 | 262,144 | 866,560 | 8 | mtp / 3 |

Card counts are saved configuration choices, not a claim that every allowed placement was measured. A derived view can differ from its pinned download source.

<details>
<summary>cfg-b53031acebd92a7f3ad5</summary>

```json
{
  "kind": "tabby",
  "gpu_counts": [
    1
  ],
  "context": 262144,
  "cache_tokens": 866560,
  "cache_mode": "Q8",
  "draft_cache_mode": "Q8",
  "draft_mode": "mtp",
  "draft_tokens": 3,
  "max_sessions": 8,
  "chunk_size": 512,
  "reserve_mib": 128,
  "ram_kv_mib": 8192,
  "ram_recurrent_mib": 16384,
  "dynamic_draft": false,
  "output_chunk_tokens": 4096,
  "power_watts": 200,
  "host_memory_gib": 80,
  "host_swap_gib": 0,
  "min_vram_mib_per_gpu": 65530,
  "min_effective_vram_mib": 65530,
  "parallelism": "layer_split",
  "transport": "host",
  "host_backing": "ordinary",
  "model_repository": "Lygodactylus/Qwen3.8-27B-Uncensored-exl3-8bpw",
  "model_revision": "3487b152b302930e303dc4a2e99e7e976e3ad28f",
  "draft_repository": null,
  "draft_revision": null,
  "recorded_runtime_label": null,
  "served_model_label": "qwen27-orca-exl3-8bpw",
  "main_reserve_mib_values_unordered": []
}
```

Pinned model revision recorded: yes. Source receipt labels, hashes and object locators are retained in [configurations.json](../configurations.json).

</details>

<details>
<summary>cfg-db175da157819da2b96c</summary>

```json
{
  "kind": "tabby",
  "gpu_counts": [
    1
  ],
  "context": 262144,
  "cache_tokens": 866560,
  "cache_mode": "Q8",
  "draft_cache_mode": "Q8",
  "draft_mode": "mtp",
  "draft_tokens": 3,
  "max_sessions": 8,
  "chunk_size": 512,
  "reserve_mib": 128,
  "ram_kv_mib": 8192,
  "ram_recurrent_mib": 16384,
  "dynamic_draft": false,
  "output_chunk_tokens": 4096,
  "power_watts": 200,
  "host_memory_gib": 80,
  "host_swap_gib": 0,
  "min_vram_mib_per_gpu": 65530,
  "min_effective_vram_mib": 65530,
  "parallelism": "layer_split",
  "transport": "host",
  "host_backing": "ordinary",
  "model_repository": "Lygodactylus/Qwen3.8-27B-Uncensored-exl3-8bpw",
  "model_revision": "3487b152b302930e303dc4a2e99e7e976e3ad28f",
  "draft_repository": null,
  "draft_revision": null,
  "recorded_runtime_label": null,
  "served_model_label": "qwen27-orca-exl3-8bpw"
}
```

Pinned model revision recorded: yes. Source receipt labels, hashes and object locators are retained in [configurations.json](../configurations.json).

</details>

## Retained Measurements

| Profile / Wave | Layout; Draft / Tokens | Requests | Input tokens/request | Accepted output tokens/request | Cache / Reused input tokens | Context / GPU pool tokens | Shared decode tok/s total | Client after-first-token estimate tok/s | Whole-wave output tok/s | Median TTFT, s | Source report |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [ad024-orca-native-000](ad024-orca-native-000.md)<br>wave-21a308f05b7c717cbb04 | layer_split; mtp / 3 | 1 | 32,769 | 512 (budget 512) | repeated_input; reused 0 | 262,144 / 866,560 | 46.69 | Not recorded | 14.42 | 24.70 | Pass |
| [ad024-orca-native-000](ad024-orca-native-000.md)<br>wave-235d8e9b9fec74040e30 | layer_split; mtp / 3 | 8 | 2,027 | 512 (budget 512) | cached_prefix; reused 1,792 | 262,144 / 866,560 | 204.10 | Not recorded | 178.13 | 3.26 | Pass |
| [ad024-orca-native-000](ad024-orca-native-000.md)<br>wave-431d30e791ed9d0aae04 | layer_split; mtp / 3 | 8 | 2,027 | 256 (budget 256) | cold; reused 0 | 262,144 / 866,560 | 189.79 | Not recorded | 87.67 | 12.14 | Pass |
| [ad024-orca-native-000](ad024-orca-native-000.md)<br>wave-5f85cdc5df601d82e6c5 | layer_split; mtp / 3 | 1 | 2,026 | 256 (budget 256) | cold; reused 0 | 262,144 / 866,560 | 60.57 | Not recorded | 44.96 | 1.58 | Pass |
| [ad024-orca-native-000](ad024-orca-native-000.md)<br>wave-979de37c2d8b129e22a5 | layer_split; mtp / 3 | 8 | 32,770 | 256 (budget 256) | cold; reused 0 | 262,144 / 866,560 | 112.38 | Not recorded | 9.39 | 200.45 | Pass |
| [ad024-orca-native-000](ad024-orca-native-000.md)<br>wave-bab83c2e9cb13189eeaa | layer_split; mtp / 3 | 8 | 32,770 | 512 (budget 512) | cached_prefix; reused 32,768 | 262,144 / 866,560 | 111.33 | Not recorded | 107.95 | 1.94 | Pass |
| [ad024-orca-native-000](ad024-orca-native-000.md)<br>wave-cc4248f864123669dc2f | layer_split; mtp / 3 | 1 | 32,769 | 256 (budget 256) | cold; reused 0 | 262,144 / 866,560 | 47.49 | Not recorded | 8.58 | 24.57 | Pass |
| [ad024-orca-native-000](ad024-orca-native-000.md)<br>wave-e4f96fb824f881aa9ceb | layer_split; mtp / 3 | 1 | 2,026 | 512 (budget 512) | cached_prefix; reused 1,792 | 262,144 / 866,560 | 64.49 | Not recorded | 62.03 | 0.44 | Pass |

Rates are whole-wave totals over the stated request count. A wave may span multiple independent model instances; [measurements.json](../measurements.json) retains their contributions and the exact configuration IDs. Do not interpret a multi-instance total as one card's rate.

A dash in shared decode means no qualified synchronized interval is available. Whole-wave throughput includes prefill and queueing. A valid decode interval can survive inside an overall failed or partial check; the source-report outcome is preserved. No rows are averaged.

## Bounded Checks

| Check | Reported outcome | Retained counts / flags |
| --- | --- | --- |
| check-2cbe1a6dbadd2ebbf679 | Pass | {"passed":true,"elapsed_seconds":29.834651015000418,"ttft_seconds":[24.56953995200456],"end_to_end_accepted_tok_s":8.580626596613683} |
| check-c06b7c29dd03be7ac7f7 | Pass | {"passed":true,"elapsed_seconds":218.1156652349964,"ttft_seconds":[196.83740430799662,198.9048122460008,200.44814996100467,200.44780763200106,200.4477864299988,200.4474188650056,200.44733135700517,200.4469859220044],"end_to_end_accepted_tok_s":9.389513576631455} |
| check-d958788b3454d9b301d9 | Pass | {"passed":true,"elapsed_seconds":5.693861265994201,"ttft_seconds":[1.5815578039982938],"end_to_end_accepted_tok_s":44.960702068546105} |
| check-fcf3b0d66a1417eb9273 | Pass | {"passed":true,"elapsed_seconds":23.359507008004584,"ttft_seconds":[6.9097004089999245,10.927236520001316,12.136581712999032,12.136374635003449,12.136209626005439,12.136036190000596,12.882854964002036,12.882663322998269],"end_to_end_accepted_tok_s":87.6730831390497} |

These checks retain their reported scope. A context/allocation/retrieval check is not a general quality score or a speed qualification at that context. Exact flags and provenance are in [checks.json](../checks.json).

## Additional Test Results

| Result / Source | Profile | Evidence type | Reported outcome | Retained values | Configuration binding |
| --- | --- | --- | --- | --- | --- |
| [result-09353a33b2739ab5a453](../observations.json)<br>source-13058405d9e027a2fa3bc898.json<br>`/waves/1` | [ad024-orca-native-000](ad024-orca-native-000.md) | performance detail | Outcome unspecified | elapsed_seconds=8.25 s; end_to_end_accepted_tok_s=62.03 accepted tokens/s; output_tokens=512 tokens; ttft_seconds=0.44 s; p50_ms=11.81 ms; p95_ms=45.73 ms; prefill: per-request 806.90 tokens/s; Draft accepted / proposed: 341 / 513 tokens; fraction 0.6647 | Recorded configuration/job |
| [result-093c4559959908287344](../observations.json)<br>source-797606345fa45914fcd85b71.json<br>`/profiles/qwen27-orca-mtp3-native/raw_followup/quality` | [ad024-orca-native-000](ad024-orca-native-000.md)<br>[qwen27-orca-mtp3-native](qwen27-orca-mtp3-native.md) | quality evaluation | 6 / 8 tasks passed | Task latency median 4.27 s; n=8 | Recorded configuration/job |
| [result-39e8303f5c7d6572fc64](../observations.json)<br>source-974b2b61a28146618d6f0ab7.json<br>`/waves/1` | [ad024-orca-native-000](ad024-orca-native-000.md) | performance detail | Outcome unspecified | elapsed_seconds=22.99 s; end_to_end_accepted_tok_s=178.13 accepted tokens/s; output_tokens=512 tokens; ttft_seconds=0.45<br>2.40<br>3.20<br>3.20<br>3.31<br>3.31<br>3.42<br>3.42 s; p50_ms=36.29 ms; p95_ms=108.39 ms; prefill: per-request 405.17 to 810.34 tokens/s; Draft accepted / proposed: 2,629 / 4,401 tokens; fraction 0.5974 | Recorded configuration/job |
| [result-4c848a07587546d17641](../observations.json)<br>source-974b2b61a28146618d6f0ab7.json<br>`/` | [ad024-orca-native-000](ad024-orca-native-000.md) | performance detail | Pass | elapsed_seconds=23.36 s; end_to_end_accepted_tok_s=87.67 accepted tokens/s; ttft_seconds=6.91<br>10.93<br>12.14<br>12.14<br>12.14<br>12.14<br>12.88<br>12.88 s; p50_ms=36.29 ms; p95_ms=108.39 ms; cold_prefill: per-request 234.61 to 708.74 tokens/s; Draft accepted / proposed: 2,629 / 4,401 tokens; fraction 0.5974 | Recorded configuration/job |
| [result-533ac51e22a3ab1fd09e](../observations.json)<br>source-13058405d9e027a2fa3bc898.json<br>`/` | [ad024-orca-native-000](ad024-orca-native-000.md) | performance detail | Pass | elapsed_seconds=5.69 s; end_to_end_accepted_tok_s=44.96 accepted tokens/s; ttft_seconds=1.58 s; p50_ms=11.81 ms; p95_ms=45.73 ms; cold_prefill: per-request 1,324.18 tokens/s; Draft accepted / proposed: 341 / 513 tokens; fraction 0.6647 | Recorded configuration/job |
| [result-78853df602c41a0f5096](../observations.json)<br>source-d862bedb7b84a6a851e42db6.json<br>`/waves/0` | [ad024-orca-native-000](ad024-orca-native-000.md) | performance detail | Outcome unspecified | elapsed_seconds=218.12 s; end_to_end_accepted_tok_s=9.39 accepted tokens/s; output_tokens=256 tokens; ttft_seconds=196.84<br>198.90<br>200.45<br>200.45<br>200.45<br>200.45<br>200.45<br>200.45 s; p50_ms=62.32 ms; p95_ms=203.81 ms; prefill: per-request 167.08 to 174.70 tokens/s; Draft accepted / proposed: 1,349 / 2,097 tokens; fraction 0.6433 | Recorded configuration/job |
| [result-8580b6f06dac6ab2b282](../observations.json)<br>source-16cb134d0afa61017c0a17b2.json<br>`/` | [ad024-orca-native-000](ad024-orca-native-000.md) | performance detail | Pass | elapsed_seconds=29.83 s; end_to_end_accepted_tok_s=8.58 accepted tokens/s; ttft_seconds=24.57 s; p50_ms=19.46 ms; p95_ms=57.49 ms; cold_prefill: per-request 1,339.70 tokens/s; Draft accepted / proposed: 325 / 561 tokens; fraction 0.5793 | Recorded configuration/job |
| [result-8a02207c4a6200581984](../observations.json)<br>source-974b2b61a28146618d6f0ab7.json<br>`/waves/0` | [ad024-orca-native-000](ad024-orca-native-000.md) | performance detail | Outcome unspecified | elapsed_seconds=23.36 s; end_to_end_accepted_tok_s=87.67 accepted tokens/s; output_tokens=256 tokens; ttft_seconds=6.91<br>10.93<br>12.14<br>12.14<br>12.14<br>12.14<br>12.88<br>12.88 s; p50_ms=42.11 ms; p95_ms=107.75 ms; prefill: per-request 234.61 to 708.74 tokens/s; Draft accepted / proposed: 1,298 / 2,250 tokens; fraction 0.5769 | Recorded configuration/job |
| [result-8ae187cdfd4ff89e1753](../observations.json)<br>source-797606345fa45914fcd85b71.json<br>`/profiles/qwen27-orca-mtp3-native/raw_followup/final_geometry/stats/cache` | [ad024-orca-native-000](ad024-orca-native-000.md)<br>[qwen27-orca-mtp3-native](qwen27-orca-mtp3-native.md) | test outcome | Outcome unspecified | cached_tokens=320,000 tokens | Recorded configuration/job |
| [result-91601bbd94e6fda2f84b](../observations.json)<br>source-d862bedb7b84a6a851e42db6.json<br>`/` | [ad024-orca-native-000](ad024-orca-native-000.md) | performance detail | Pass | elapsed_seconds=218.12 s; end_to_end_accepted_tok_s=9.39 accepted tokens/s; ttft_seconds=196.84<br>198.90<br>200.45<br>200.45<br>200.45<br>200.45<br>200.45<br>200.45 s; p50_ms=67.87 ms; p95_ms=204.29 ms; cold_prefill: per-request 167.08 to 174.70 tokens/s; Draft accepted / proposed: 2,673 / 4,269 tokens; fraction 0.6261 | Recorded configuration/job |
| [result-92572c1c765f0c4d17a0](../observations.json)<br>source-16cb134d0afa61017c0a17b2.json<br>`/waves/1` | [ad024-orca-native-000](ad024-orca-native-000.md) | performance detail | Outcome unspecified | elapsed_seconds=35.50 s; end_to_end_accepted_tok_s=14.42 accepted tokens/s; output_tokens=512 tokens; ttft_seconds=24.70 s; p50_ms=19.46 ms; p95_ms=57.49 ms; prefill: per-request 1,333.16 tokens/s; Draft accepted / proposed: 325 / 561 tokens; fraction 0.5793 | Recorded configuration/job |
| [result-ae25567b7233823b5a39](../observations.json)<br>source-797606345fa45914fcd85b71.json<br>`/profiles/qwen27-orca-mtp3-native/raw_followup/final_geometry/stats/totals` | [ad024-orca-native-000](ad024-orca-native-000.md)<br>[qwen27-orca-mtp3-native](qwen27-orca-mtp3-native.md) | context allocation | Outcome unspecified | cached_tokens=278,272 tokens; generated_tokens=14,260 accepted tokens; prompt_tokens=627,685 tokens; recurrent_restores=17 checkpoints | Recorded configuration/job |
| [result-ca3950ec8c190711c90e](../observations.json)<br>source-16cb134d0afa61017c0a17b2.json<br>`/waves/0` | [ad024-orca-native-000](ad024-orca-native-000.md) | performance detail | Outcome unspecified | elapsed_seconds=29.83 s; end_to_end_accepted_tok_s=8.58 accepted tokens/s; output_tokens=256 tokens; ttft_seconds=24.57 s; p50_ms=19.39 ms; p95_ms=57.14 ms; prefill: per-request 1,339.70 tokens/s; Draft accepted / proposed: 164 / 276 tokens; fraction 0.5942 | Recorded configuration/job |
| [result-d808cf1f1a47ea19bd07](../observations.json)<br>source-797606345fa45914fcd85b71.json<br>`/profiles/qwen27-orca-mtp3-native/raw_followup/final_geometry/stats` | [ad024-orca-native-000](ad024-orca-native-000.md)<br>[qwen27-orca-mtp3-native](qwen27-orca-mtp3-native.md) | test outcome | Outcome unspecified | context=262,144 tokens | Recorded configuration/job |
| [result-e2a65e498ff37b304bab](../observations.json)<br>source-d862bedb7b84a6a851e42db6.json<br>`/waves/1` | [ad024-orca-native-000](ad024-orca-native-000.md) | performance detail | Outcome unspecified | elapsed_seconds=37.94 s; end_to_end_accepted_tok_s=107.95 accepted tokens/s; output_tokens=512 tokens; ttft_seconds=0.41<br>1.52<br>1.94<br>1.94<br>1.94<br>1.94<br>2.15<br>2.15 s; p50_ms=67.87 ms; p95_ms=204.29 ms; prefill: per-request 25.00 to 50.00 tokens/s; Draft accepted / proposed: 2,673 / 4,269 tokens; fraction 0.6261 | Recorded configuration/job |
| [result-f471326c65d9159d32d5](../observations.json)<br>source-67e0f6b34492767ee1fceeb9.json<br>`/tabby` | [ad024-orca-native-000](ad024-orca-native-000.md) | test outcome | Outcome unspecified | cache_tokens=866,560 tokens | Recorded configuration/job |
| [result-f95a0ef6ade1bbbd8137](../observations.json)<br>source-13058405d9e027a2fa3bc898.json<br>`/waves/0` | [ad024-orca-native-000](ad024-orca-native-000.md) | performance detail | Outcome unspecified | elapsed_seconds=5.69 s; end_to_end_accepted_tok_s=44.96 accepted tokens/s; output_tokens=256 tokens; ttft_seconds=1.58 s; p50_ms=15.46 ms; p95_ms=45.58 ms; prefill: per-request 1,324.18 tokens/s; Draft accepted / proposed: 167 / 267 tokens; fraction 0.6255 | Recorded configuration/job |

These are saved result records, including failures and bounded checks. Copies, individual requests, report summaries and regrading can overlap; their counts are not independent test repetitions. Open each result for exact values, units, configuration binding and source receipts.

There are 1 retained lifecycle records. Their states, exit codes and configuration IDs remain in [catalog.json](../catalog.json); they do not supply missing benchmark results.

[Full archive](../../README.md) | [All retained waves](../RESULTS.md) | [Data definitions](../DATA.md) | [Recommended recipes](../../../README.md)
