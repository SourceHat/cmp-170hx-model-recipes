# ab-orca-mtp3-original-layer_split-matched-015

**Historical record. Decode interval measured.**

Model family: Orca (Qwen 3.8 27B abliterated).

Historical configurations are provided for comparison. The [recommended recipes](../../../README.md) include supported launch scripts.

Current recipes using the same recorded checkpoint repository: [qwen27-orca-mtp3-native](../../../recipes/qwen27-orca-mtp3-native/README.md). Context, cache and runtime versions can differ.

## Saved Configuration Versions

Each configuration ID identifies a distinct original settings record. Deployment fields are omitted; versions can have identical published settings after that omission. Upstream runtime commits remain unspecified where the source retained only an integration label.

| Configuration | Recorded artifact / source | Configured card counts | Context tokens | GPU pool tokens | Slots | Draft mode / tokens |
| --- | --- | --- | --- | --- | --- | --- |
| cfg-91c0343bc6e7c4a49148 | [Lygodactylus/Qwen3.8-27B-Uncensored-exl3-8bpw@3487b152b3](https://huggingface.co/Lygodactylus/Qwen3.8-27B-Uncensored-exl3-8bpw/tree/3487b152b302930e303dc4a2e99e7e976e3ad28f) | 1 | 262,144 | 524,288 | 8 | mtp / 3 |
| cfg-cfacc4d48f8d520ba24b | [Lygodactylus/Qwen3.8-27B-Uncensored-exl3-8bpw@3487b152b3](https://huggingface.co/Lygodactylus/Qwen3.8-27B-Uncensored-exl3-8bpw/tree/3487b152b302930e303dc4a2e99e7e976e3ad28f) | 1 | 262,144 | 524,288 | 8 | mtp / 3 |

Card counts are saved configuration choices, not a claim that every allowed placement was measured. A derived view can differ from its pinned download source.

<details>
<summary>cfg-91c0343bc6e7c4a49148</summary>

```json
{
  "kind": "tabby",
  "gpu_counts": [
    1
  ],
  "context": 262144,
  "cache_tokens": 524288,
  "cache_mode": "Q8",
  "draft_cache_mode": "Q8",
  "draft_mode": "mtp",
  "draft_tokens": 3,
  "max_sessions": 8,
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

<details>
<summary>cfg-cfacc4d48f8d520ba24b</summary>

```json
{
  "kind": "tabby",
  "gpu_counts": [
    1
  ],
  "context": 262144,
  "cache_tokens": 524288,
  "cache_mode": "Q8",
  "draft_cache_mode": "Q8",
  "draft_mode": "mtp",
  "draft_tokens": 3,
  "max_sessions": 8,
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

## Retained Measurements

| Profile / Wave | Layout; Draft / Tokens | Requests | Input tokens/request | Accepted output tokens/request | Cache / Reused input tokens | Context / GPU pool tokens | Shared decode tok/s total | Client after-first-token estimate tok/s | Whole-wave output tok/s | Median TTFT, s | Source report |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [ab-orca-mtp3-original-layer_split-matched-015](ab-orca-mtp3-original-layer_split-matched-015.md)<br>wave-01134bbc3210a453b95f | layer_split; mtp / 3 | 8 | 2,027 | 512 (budget 512) | cached_prefix; reused 1,792 | 262,144 / 524,288 | 200.96 | Not recorded | 175.36 | 3.35 | Pass |
| [ab-orca-mtp3-original-layer_split-matched-015](ab-orca-mtp3-original-layer_split-matched-015.md)<br>wave-3481d5d828a2726e032b | layer_split; mtp / 3 | 1 | 32,769 | 512 (budget 512) | repeated_input; reused 0 | 262,144 / 524,288 | 46.09 | Not recorded | 14.32 | 24.87 | Pass |
| [ab-orca-mtp3-original-layer_split-matched-015](ab-orca-mtp3-original-layer_split-matched-015.md)<br>wave-3c63b019e3355d7cfdcd | layer_split; mtp / 3 | 8 | 61,441 | 512 (budget 512) | cached_prefix; reused 32,768 | 262,144 / 524,288 | 76.74 | Not recorded | 15.05 | 219.73 | Pass |
| [ab-orca-mtp3-original-layer_split-matched-015](ab-orca-mtp3-original-layer_split-matched-015.md)<br>wave-46cf6d134a7b0f7283cc | layer_split; mtp / 3 | 1 | 2,026 | 512 (budget 512) | cold; reused 0 | 262,144 / 524,288 | 62.12 | Not recorded | 52.23 | 1.69 | Pass |
| [ab-orca-mtp3-original-layer_split-matched-015](ab-orca-mtp3-original-layer_split-matched-015.md)<br>wave-4a8a3a9111e99e1c1ad7 | layer_split; mtp / 3 | 1 | 2,026 | 512 (budget 512) | cached_prefix; reused 1,792 | 262,144 / 524,288 | 63.22 | Not recorded | 60.73 | 0.41 | Pass |
| [ab-orca-mtp3-original-layer_split-matched-015](ab-orca-mtp3-original-layer_split-matched-015.md)<br>wave-ab3d6a5f8a99e5fafa33 | layer_split; mtp / 3 | 8 | 2,027 | 512 (budget 512) | cold; reused 0 | 262,144 / 524,288 | 197.09 | Not recorded | 122.61 | 11.59 | Pass |
| [ab-orca-mtp3-original-layer_split-matched-015](ab-orca-mtp3-original-layer_split-matched-015.md)<br>wave-aed34ce8d7245eaa7d77 | layer_split; mtp / 3 | 8 | 32,770 | 512 (budget 512) | cold; reused 0 | 262,144 / 524,288 | 111.81 | Not recorded | 17.32 | 200.43 | Pass |
| [ab-orca-mtp3-original-layer_split-matched-015](ab-orca-mtp3-original-layer_split-matched-015.md)<br>wave-ca893d7d0bc2c00b3cce | layer_split; mtp / 3 | 8 | 61,441 | 128 (budget 128) | cold; reused 0 | 262,144 / 524,288 | 76.57 | Not recorded | 2.35 | 422.90 | Pass |
| [ab-orca-mtp3-original-layer_split-matched-015](ab-orca-mtp3-original-layer_split-matched-015.md)<br>wave-cecc8e2f00f0d94e2686 | layer_split; mtp / 3 | 8 | 32,770 | 512 (budget 512) | cached_prefix; reused 32,768 | 262,144 / 524,288 | 111.74 | Not recorded | 106.79 | 2.58 | Pass |
| [ab-orca-mtp3-original-layer_split-matched-015](ab-orca-mtp3-original-layer_split-matched-015.md)<br>wave-efaaf46f2ac388dab71b | layer_split; mtp / 3 | 1 | 32,769 | 512 (budget 512) | cold; reused 0 | 262,144 / 524,288 | 46.38 | Not recorded | 14.40 | 24.69 | Pass |

Rates are whole-wave totals over the stated request count. A wave may span multiple independent model instances; [measurements.json](../measurements.json) retains their contributions and the exact configuration IDs. Do not interpret a multi-instance total as one card's rate.

A dash in shared decode means no qualified synchronized interval is available. Whole-wave throughput includes prefill and queueing. A valid decode interval can survive inside an overall failed or partial check; the source-report outcome is preserved. No rows are averaged.

## Bounded Checks

| Check | Reported outcome | Retained counts / flags |
| --- | --- | --- |
| check-3b33dec2987e9e23a439 | Pass | {"passed":true,"elapsed_seconds":35.562102530999255,"ttft_seconds":[24.69359900500058],"end_to_end_accepted_tok_s":14.397348963090495} |
| check-6ab0923dad2660776dd1 | Pass | {"passed":true,"elapsed_seconds":35.562102530999255,"ttft_seconds":[24.69359900500058],"end_to_end_accepted_tok_s":14.397348963090495} |
| check-731f340b29354a1bbea8 | Pass | {"passed":true,"elapsed_seconds":9.803518847000305,"ttft_seconds":[1.686119783000322],"end_to_end_accepted_tok_s":52.22614532501893} |
| check-79d10403f8891d5a068f | Pass | {"passed":true,"elapsed_seconds":434.91428234199884,"ttft_seconds":[400.2929761790001,421.27071099299974,422.75038062600106,422.74992740200105,423.05476159499995,423.0542651579999,423.0547507459996,423.05397255000025],"end_to_end_accepted_tok_s":2.3544869450729333} |
| check-7e4b338106e15d48946c | Pass | {"passed":true,"elapsed_seconds":33.407608286999675,"ttft_seconds":[9.114215077999688,9.114292260999719,10.964971221001178,10.964098689999446,12.216063701000166,12.215511881000566,13.080795863001185,13.080012128000817],"end_to_end_accepted_tok_s":122.6068015648378} |
| check-921866fcd38f1f25a048 | Pass | {"passed":true,"elapsed_seconds":33.407608286999675,"ttft_seconds":[9.114215077999688,9.114292260999719,10.964971221001178,10.964098689999446,12.216063701000166,12.215511881000566,13.080795863001185,13.080012128000817],"end_to_end_accepted_tok_s":122.6068015648378} |
| check-95422eb524ae50d31625 | Pass | {"passed":true,"elapsed_seconds":236.43461665499854,"ttft_seconds":[189.55275894700026,195.52028502900066,199.6486647670008,200.43505583200022,200.4343519390004,200.89396018499974,200.8932668890011,200.89285263199963],"end_to_end_accepted_tok_s":17.324028342164528} |
| check-9a8f6d6f1b1a61e66a63 | Pass | {"passed":true,"elapsed_seconds":236.43461665499854,"ttft_seconds":[189.55275894700026,195.52028502900066,199.6486647670008,200.43505583200022,200.4343519390004,200.89396018499974,200.8932668890011,200.89285263199963],"end_to_end_accepted_tok_s":17.324028342164528} |
| check-abe879318b76bcbc43a2 | Pass | {"passed":true,"elapsed_seconds":9.803518847000305,"ttft_seconds":[1.686119783000322],"end_to_end_accepted_tok_s":52.22614532501893} |
| check-fbc6aaf808ecc3dd889e | Pass | {"passed":true,"elapsed_seconds":434.91428234199884,"ttft_seconds":[400.2929761790001,421.27071099299974,422.75038062600106,422.74992740200105,423.05476159499995,423.0542651579999,423.0547507459996,423.05397255000025],"end_to_end_accepted_tok_s":2.3544869450729333} |

These checks retain their reported scope. A context/allocation/retrieval check is not a general quality score or a speed qualification at that context. Exact flags and provenance are in [checks.json](../checks.json).

## Additional Test Results

| Result / Source | Profile | Evidence type | Reported outcome | Retained values | Configuration binding |
| --- | --- | --- | --- | --- | --- |
| [result-022e25962cc35ec5272d](../observations.json)<br>source-b792a6ab248fc2780330c3d7.json<br>`/speed/0` | [ab-orca-mtp3-original-layer_split-matched-015](ab-orca-mtp3-original-layer_split-matched-015.md)<br>[orca-mtp3-original-layer_split](orca-mtp3-original-layer_split.md) | performance detail | Pass | elapsed_seconds=9.80 s; end_to_end_accepted_tok_s=52.23 accepted tokens/s; ttft_seconds=1.69 s; p50_ms=12.26 ms; p95_ms=46.75 ms; cold_prefill: per-request 1,282.28 tokens/s; Draft accepted / proposed: 341 / 513 tokens; fraction 0.6647 | Recorded configuration/job |
| [result-1195a1272ec02831eec1](../observations.json)<br>source-b792a6ab248fc2780330c3d7.json<br>`/speed/1` | [ab-orca-mtp3-original-layer_split-matched-015](ab-orca-mtp3-original-layer_split-matched-015.md)<br>[orca-mtp3-original-layer_split](orca-mtp3-original-layer_split.md) | performance detail | Pass | elapsed_seconds=33.41 s; end_to_end_accepted_tok_s=122.61 accepted tokens/s; ttft_seconds=9.11<br>9.11<br>10.96<br>10.96<br>12.22<br>12.22<br>13.08<br>13.08 s; p50_ms=36.76 ms; p95_ms=109.83 ms; cold_prefill: per-request 226.73 to 446.48 tokens/s; Draft accepted / proposed: 2,630 / 4,398 tokens; fraction 0.5980 | Recorded configuration/job |
| [result-1d39d5d7584093edd47e](../observations.json)<br>source-a9e622d351a86c8b776605d4.json<br>`/managed_phase_timings/15` | [ab-orca-mtp3-original-layer_split-matched-015](ab-orca-mtp3-original-layer_split-matched-015.md) | test outcome | Outcome unspecified | wall_seconds=1,202.56 s | Recorded configuration/job |
| [result-280594f5ee7531e2e373](../observations.json)<br>source-b792a6ab248fc2780330c3d7.json<br>`/capacity/trials/0/peak_prefill` | [ab-orca-mtp3-original-layer_split-matched-015](ab-orca-mtp3-original-layer_split-matched-015.md)<br>[orca-mtp3-original-layer_split](orca-mtp3-original-layer_split.md) | performance detail | Pass | elapsed_seconds=434.91 s; end_to_end_accepted_tok_s=2.35 accepted tokens/s; ttft_seconds=400.29<br>421.27<br>422.75<br>422.75<br>423.05<br>423.05<br>423.05<br>423.05 s; p50_ms=97.24 ms; p95_ms=292.39 ms; cold_prefill: per-request 148.18 to 153.60 tokens/s; Draft accepted / proposed: 2,668 / 4,284 tokens; fraction 0.6228 | Recorded configuration/job |
| [result-4d3d0289f826c0434161](../observations.json)<br>source-b792a6ab248fc2780330c3d7.json<br>`/speed/3/waves/1` | [ab-orca-mtp3-original-layer_split-matched-015](ab-orca-mtp3-original-layer_split-matched-015.md)<br>[orca-mtp3-original-layer_split](orca-mtp3-original-layer_split.md) | performance detail | Outcome unspecified | elapsed_seconds=38.36 s; end_to_end_accepted_tok_s=106.79 accepted tokens/s; output_tokens=512 tokens; ttft_seconds=0.61<br>2.26<br>2.26<br>2.58<br>2.58<br>2.79<br>2.79<br>2.99 s; p50_ms=67.79 ms; p95_ms=206.10 ms; prefill: per-request 25.00 to 50.00 tokens/s; Draft accepted / proposed: 2,693 / 4,209 tokens; fraction 0.6398 | Recorded configuration/job |
| [result-50f42ab04a2248166b96](../observations.json)<br>source-b792a6ab248fc2780330c3d7.json<br>`/speed/3/waves/0` | [ab-orca-mtp3-original-layer_split-matched-015](ab-orca-mtp3-original-layer_split-matched-015.md)<br>[orca-mtp3-original-layer_split](orca-mtp3-original-layer_split.md) | performance detail | Outcome unspecified | elapsed_seconds=236.43 s; end_to_end_accepted_tok_s=17.32 accepted tokens/s; output_tokens=512 tokens; ttft_seconds=189.55<br>195.52<br>199.65<br>200.44<br>200.43<br>200.89<br>200.89<br>200.89 s; p50_ms=67.95 ms; p95_ms=205.31 ms; prefill: per-request 167.78 to 175.89 tokens/s; Draft accepted / proposed: 2,693 / 4,209 tokens; fraction 0.6398 | Recorded configuration/job |
| [result-724e24738033ae4456a8](../observations.json)<br>source-b792a6ab248fc2780330c3d7.json<br>`/speed/0/waves/0` | [ab-orca-mtp3-original-layer_split-matched-015](ab-orca-mtp3-original-layer_split-matched-015.md)<br>[orca-mtp3-original-layer_split](orca-mtp3-original-layer_split.md) | performance detail | Outcome unspecified | elapsed_seconds=9.80 s; end_to_end_accepted_tok_s=52.23 accepted tokens/s; output_tokens=512 tokens; ttft_seconds=1.69 s; p50_ms=12.20 ms; p95_ms=46.68 ms; prefill: per-request 1,282.28 tokens/s; Draft accepted / proposed: 340 / 516 tokens; fraction 0.6589 | Recorded configuration/job |
| [result-82df7fdbbb57243c21d5](../observations.json)<br>source-b792a6ab248fc2780330c3d7.json<br>`/capacity/trials/0/peak_prefill/waves/0` | [ab-orca-mtp3-original-layer_split-matched-015](ab-orca-mtp3-original-layer_split-matched-015.md)<br>[orca-mtp3-original-layer_split](orca-mtp3-original-layer_split.md) | performance detail | Outcome unspecified | elapsed_seconds=434.91 s; end_to_end_accepted_tok_s=2.35 accepted tokens/s; output_tokens=128 tokens; ttft_seconds=400.29<br>421.27<br>422.75<br>422.75<br>423.05<br>423.05<br>423.05<br>423.05 s; p50_ms=96.54 ms; p95_ms=292.11 ms; prefill: per-request 148.18 to 153.60 tokens/s; Draft accepted / proposed: 676 / 1,044 tokens; fraction 0.6475 | Recorded configuration/job |
| [result-87af1ce0e4e1f622480c](../observations.json)<br>source-b792a6ab248fc2780330c3d7.json<br>`/speed/3` | [ab-orca-mtp3-original-layer_split-matched-015](ab-orca-mtp3-original-layer_split-matched-015.md)<br>[orca-mtp3-original-layer_split](orca-mtp3-original-layer_split.md) | performance detail | Pass | elapsed_seconds=236.43 s; end_to_end_accepted_tok_s=17.32 accepted tokens/s; ttft_seconds=189.55<br>195.52<br>199.65<br>200.44<br>200.43<br>200.89<br>200.89<br>200.89 s; p50_ms=67.79 ms; p95_ms=206.10 ms; cold_prefill: per-request 167.78 to 175.89 tokens/s; Draft accepted / proposed: 2,693 / 4,209 tokens; fraction 0.6398 | Recorded configuration/job |
| [result-95551123950406c8d89a](../observations.json)<br>source-b792a6ab248fc2780330c3d7.json<br>`/speed/1/waves/0` | [ab-orca-mtp3-original-layer_split-matched-015](ab-orca-mtp3-original-layer_split-matched-015.md)<br>[orca-mtp3-original-layer_split](orca-mtp3-original-layer_split.md) | performance detail | Outcome unspecified | elapsed_seconds=33.41 s; end_to_end_accepted_tok_s=122.61 accepted tokens/s; output_tokens=512 tokens; ttft_seconds=9.11<br>9.11<br>10.96<br>10.96<br>12.22<br>12.22<br>13.08<br>13.08 s; p50_ms=36.86 ms; p95_ms=109.37 ms; prefill: per-request 226.73 to 446.48 tokens/s; Draft accepted / proposed: 2,629 / 4,401 tokens; fraction 0.5974 | Recorded configuration/job |
| [result-dba0ecb9be99be978d88](../observations.json)<br>source-b792a6ab248fc2780330c3d7.json<br>`/speed/2/waves/0` | [ab-orca-mtp3-original-layer_split-matched-015](ab-orca-mtp3-original-layer_split-matched-015.md)<br>[orca-mtp3-original-layer_split](orca-mtp3-original-layer_split.md) | performance detail | Outcome unspecified | elapsed_seconds=35.56 s; end_to_end_accepted_tok_s=14.40 accepted tokens/s; output_tokens=512 tokens; ttft_seconds=24.69 s; p50_ms=19.60 ms; p95_ms=57.85 ms; prefill: per-request 1,333.16 tokens/s; Draft accepted / proposed: 325 / 561 tokens; fraction 0.5793 | Recorded configuration/job |
| [result-e0d816db52748742e260](../observations.json)<br>source-b792a6ab248fc2780330c3d7.json<br>`/speed/0/waves/1` | [ab-orca-mtp3-original-layer_split-matched-015](ab-orca-mtp3-original-layer_split-matched-015.md)<br>[orca-mtp3-original-layer_split](orca-mtp3-original-layer_split.md) | performance detail | Outcome unspecified | elapsed_seconds=8.43 s; end_to_end_accepted_tok_s=60.73 accepted tokens/s; output_tokens=512 tokens; ttft_seconds=0.41 s; p50_ms=12.26 ms; p95_ms=46.75 ms; prefill: per-request 806.90 tokens/s; Draft accepted / proposed: 341 / 513 tokens; fraction 0.6647 | Recorded configuration/job |
| [result-ec38fa5c95b5dcd62e7c](../observations.json)<br>source-b792a6ab248fc2780330c3d7.json<br>`/speed/1/waves/1` | [ab-orca-mtp3-original-layer_split-matched-015](ab-orca-mtp3-original-layer_split-matched-015.md)<br>[orca-mtp3-original-layer_split](orca-mtp3-original-layer_split.md) | performance detail | Outcome unspecified | elapsed_seconds=23.36 s; end_to_end_accepted_tok_s=175.36 accepted tokens/s; output_tokens=512 tokens; ttft_seconds=0.51<br>2.89<br>2.89<br>3.35<br>3.35<br>3.35<br>3.35<br>3.46 s; p50_ms=36.76 ms; p95_ms=109.83 ms; prefill: per-request 405.17 to 810.34 tokens/s; Draft accepted / proposed: 2,630 / 4,398 tokens; fraction 0.5980 | Recorded configuration/job |
| [result-ee5c4edadd1e0a9cd607](../observations.json)<br>source-b792a6ab248fc2780330c3d7.json<br>`/speed/2/waves/1` | [ab-orca-mtp3-original-layer_split-matched-015](ab-orca-mtp3-original-layer_split-matched-015.md)<br>[orca-mtp3-original-layer_split](orca-mtp3-original-layer_split.md) | performance detail | Outcome unspecified | elapsed_seconds=35.75 s; end_to_end_accepted_tok_s=14.32 accepted tokens/s; output_tokens=512 tokens; ttft_seconds=24.87 s; p50_ms=19.70 ms; p95_ms=58.17 ms; prefill: per-request 1,327.22 tokens/s; Draft accepted / proposed: 325 / 561 tokens; fraction 0.5793 | Recorded configuration/job |
| [result-f026472c9e1ee5e30f66](../observations.json)<br>source-b792a6ab248fc2780330c3d7.json<br>`/capacity/trials/0/peak_prefill/waves/1` | [ab-orca-mtp3-original-layer_split-matched-015](ab-orca-mtp3-original-layer_split-matched-015.md)<br>[orca-mtp3-original-layer_split](orca-mtp3-original-layer_split.md) | performance detail | Outcome unspecified | elapsed_seconds=272.18 s; end_to_end_accepted_tok_s=15.05 accepted tokens/s; output_tokens=512 tokens; ttft_seconds=207.06<br>219.73<br>219.73<br>219.73<br>219.73<br>219.73<br>219.72<br>221.20 s; p50_ms=97.24 ms; p95_ms=292.39 ms; prefill: per-request 135.11 to 141.30 tokens/s; Draft accepted / proposed: 2,668 / 4,284 tokens; fraction 0.6228 | Recorded configuration/job |
| [result-f31dff1a516d4680b053](../observations.json)<br>source-b792a6ab248fc2780330c3d7.json<br>`/speed/2` | [ab-orca-mtp3-original-layer_split-matched-015](ab-orca-mtp3-original-layer_split-matched-015.md)<br>[orca-mtp3-original-layer_split](orca-mtp3-original-layer_split.md) | performance detail | Pass | elapsed_seconds=35.56 s; end_to_end_accepted_tok_s=14.40 accepted tokens/s; ttft_seconds=24.69 s; p50_ms=19.70 ms; p95_ms=58.17 ms; cold_prefill: per-request 1,333.16 tokens/s; Draft accepted / proposed: 325 / 561 tokens; fraction 0.5793 | Recorded configuration/job |

These are saved result records, including failures and bounded checks. Copies, individual requests, report summaries and regrading can overlap; their counts are not independent test repetitions. Open each result for exact values, units, configuration binding and source receipts.

There are 1 retained lifecycle records. Their states, exit codes and configuration IDs remain in [catalog.json](../catalog.json); they do not supply missing benchmark results.

[Full archive](../../README.md) | [All retained waves](../RESULTS.md) | [Data definitions](../DATA.md) | [Recommended recipes](../../../README.md)
