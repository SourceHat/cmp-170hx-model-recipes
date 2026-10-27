# qwen3.8-27b-exl3

**Historical record. Decode interval measured.**

Model family: Qwen 3.8 27B.

Recorded archive reason: Base Qwen serving pilot; compare separately with the abliterated Orca and mathematical-overlay experiments.

Historical configurations are provided for comparison. The [recommended recipes](../../../README.md) include supported launch scripts.

Current recipes using the same recorded checkpoint repository: [qwen3.8-27b-exl3](../../../recipes/qwen3.8-27b-exl3/README.md). Context, cache and runtime versions can differ.

## Saved Configuration Versions

Each configuration ID identifies a distinct original settings record. Deployment fields are omitted; versions can have identical published settings after that omission. Upstream runtime commits remain unspecified where the source retained only an integration label.

| Configuration | Recorded artifact / source | Configured card counts | Context tokens | GPU pool tokens | Slots | Draft mode / tokens |
| --- | --- | --- | --- | --- | --- | --- |
| cfg-c25df694ad69e822652f | [turboderp/Qwen3.8-27B-exl3@9e4c23cfb2](https://huggingface.co/turboderp/Qwen3.8-27B-exl3/tree/9e4c23cfb23697165b8e2f6da2a1df995f66353c) | 1 | 262,144 | 917,504 | 16 | mtp / 1 |
| cfg-dfdf847a6f55dd3a5792 | [turboderp/Qwen3.8-27B-exl3@9e4c23cfb2](https://huggingface.co/turboderp/Qwen3.8-27B-exl3/tree/9e4c23cfb23697165b8e2f6da2a1df995f66353c) | 1 | 262,144 | 917,504 | 16 | mtp / 1 |
| cfg-e72a710d7d5ea5eb28c4 | [turboderp/Qwen3.8-27B-exl3@9e4c23cfb2](https://huggingface.co/turboderp/Qwen3.8-27B-exl3/tree/9e4c23cfb23697165b8e2f6da2a1df995f66353c) | 1 | 262,144 | 917,504 | 16 | mtp / 1 |
| cfg-ea8751de9de625da18ce | [turboderp/Qwen3.8-27B-exl3@9e4c23cfb2](https://huggingface.co/turboderp/Qwen3.8-27B-exl3/tree/9e4c23cfb23697165b8e2f6da2a1df995f66353c) | 1 | 262,144 | 917,504 | 16 | mtp / 1 |

Card counts are saved configuration choices, not a claim that every allowed placement was measured. A derived view can differ from its pinned download source.

<details>
<summary>cfg-c25df694ad69e822652f</summary>

```json
{
  "kind": "tabby",
  "gpu_counts": [
    1
  ],
  "context": 262144,
  "cache_tokens": 917504,
  "cache_mode": "Q8",
  "draft_cache_mode": "Q8",
  "draft_mode": "mtp",
  "draft_tokens": 1,
  "max_sessions": 16,
  "chunk_size": 2048,
  "reserve_mib": 4096,
  "ram_kv_mib": 10240,
  "ram_recurrent_mib": 7168,
  "dynamic_draft": false,
  "power_watts": 200,
  "host_memory_gib": 25,
  "host_swap_gib": 0,
  "min_vram_mib_per_gpu": 60000,
  "min_effective_vram_mib": 60000,
  "model_repository": "turboderp/Qwen3.8-27B-exl3",
  "model_revision": "9e4c23cfb23697165b8e2f6da2a1df995f66353c",
  "draft_repository": null,
  "draft_revision": null,
  "recorded_runtime_label": null,
  "served_model_label": "qwen3.8-27b"
}
```

Pinned model revision recorded: yes. Source receipt labels, hashes and object locators are retained in [configurations.json](../configurations.json).

</details>

<details>
<summary>cfg-dfdf847a6f55dd3a5792</summary>

```json
{
  "kind": "tabby",
  "gpu_counts": [
    1
  ],
  "context": 262144,
  "cache_tokens": 917504,
  "cache_mode": "Q8",
  "draft_cache_mode": "Q8",
  "draft_mode": "mtp",
  "draft_tokens": 1,
  "max_sessions": 16,
  "chunk_size": 2048,
  "reserve_mib": 4096,
  "ram_kv_mib": 10240,
  "ram_recurrent_mib": 7168,
  "dynamic_draft": false,
  "power_watts": 200,
  "host_memory_gib": 25,
  "host_swap_gib": 0,
  "min_vram_mib_per_gpu": 60000,
  "min_effective_vram_mib": 60000,
  "model_repository": "turboderp/Qwen3.8-27B-exl3",
  "model_revision": "9e4c23cfb23697165b8e2f6da2a1df995f66353c",
  "draft_repository": null,
  "draft_revision": null,
  "recorded_runtime_label": null,
  "served_model_label": "qwen3.8-27b",
  "power_watts_values_unordered": []
}
```

Pinned model revision recorded: yes. Source receipt labels, hashes and object locators are retained in [configurations.json](../configurations.json).

</details>

<details>
<summary>cfg-e72a710d7d5ea5eb28c4</summary>

```json
{
  "kind": "tabby",
  "gpu_counts": [
    1
  ],
  "context": 262144,
  "cache_tokens": 917504,
  "cache_mode": "Q8",
  "draft_cache_mode": "Q8",
  "draft_mode": "mtp",
  "draft_tokens": 1,
  "max_sessions": 16,
  "chunk_size": 2048,
  "reserve_mib": 4096,
  "ram_kv_mib": 10240,
  "ram_recurrent_mib": 7168,
  "dynamic_draft": false,
  "power_watts": 200,
  "host_memory_gib": 25,
  "host_swap_gib": 0,
  "min_vram_mib_per_gpu": 60000,
  "min_effective_vram_mib": 60000,
  "model_repository": "turboderp/Qwen3.8-27B-exl3",
  "model_revision": "9e4c23cfb23697165b8e2f6da2a1df995f66353c",
  "draft_repository": null,
  "draft_revision": null,
  "recorded_runtime_label": null,
  "served_model_label": "qwen3.8-27b"
}
```

Pinned model revision recorded: yes. Source receipt labels, hashes and object locators are retained in [configurations.json](../configurations.json).

</details>

<details>
<summary>cfg-ea8751de9de625da18ce</summary>

```json
{
  "kind": "tabby",
  "gpu_counts": [
    1
  ],
  "context": 262144,
  "cache_tokens": 917504,
  "cache_mode": "Q8",
  "draft_cache_mode": "Q8",
  "draft_mode": "mtp",
  "draft_tokens": 1,
  "max_sessions": 16,
  "chunk_size": 2048,
  "reserve_mib": 4096,
  "ram_kv_mib": 10240,
  "ram_recurrent_mib": 7168,
  "dynamic_draft": false,
  "power_watts": 200,
  "host_memory_gib": 25,
  "host_swap_gib": 0,
  "min_vram_mib_per_gpu": 60000,
  "min_effective_vram_mib": 60000,
  "model_repository": "turboderp/Qwen3.8-27B-exl3",
  "model_revision": "9e4c23cfb23697165b8e2f6da2a1df995f66353c",
  "draft_repository": null,
  "draft_revision": null,
  "recorded_runtime_label": null,
  "served_model_label": "qwen3.8-27b"
}
```

Pinned model revision recorded: yes. Source receipt labels, hashes and object locators are retained in [configurations.json](../configurations.json).

</details>

## Retained Measurements

| Profile / Wave | Layout; Draft / Tokens | Requests | Input tokens/request | Accepted output tokens/request | Cache / Reused input tokens | Context / GPU pool tokens | Shared decode tok/s total | Client after-first-token estimate tok/s | Whole-wave output tok/s | Median TTFT, s | Source report |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [qwen3.8-27b-exl3](qwen3.8-27b-exl3.md)<br>wave-18fbb288466426280127 | layout unspecified; mtp / 1 | 3 | 2,064 | 1,024 | cold; reused 0 | 262,144 / 917,504 | 135.88 | Not recorded | 128.89 | 1.17 | Pass |
| [qwen3.8-27b-exl3](qwen3.8-27b-exl3.md)<br>wave-587be831fdb357086497 | layout unspecified; mtp / 1 | 3 | 3,110 | 1,024 | cached_prefix; reused 2,048 | 262,144 / 917,504 | 134.73 | Not recorded | 128.10 | 1.07 | Pass |
| [qwen3.8-27b-exl3](qwen3.8-27b-exl3.md)<br>wave-6317600dc9476c0577de | layout unspecified; mtp / 1 | 48 | 2,067 to 8,204 | 1,024 | cold; reused 0 | 262,144 / 917,504 | 721.38 | Not recorded | 498.62 | 26.61 | Pass |
| [qwen3.8-27b-exl3](qwen3.8-27b-exl3.md)<br>wave-fd5cecf0d99cb42fa164 | layout unspecified; mtp / 1 | 48 | 3,111 to 9,250 | 1,024 | cached_prefix; reused 2,048 to 8,192 | 262,144 / 917,504 | 718.76 | Not recorded | 559.61 | 16.13 | Pass |

Rates are whole-wave totals over the stated request count. A wave may span multiple independent model instances; [measurements.json](../measurements.json) retains their contributions and the exact configuration IDs. Do not interpret a multi-instance total as one card's rate.

A dash in shared decode means no qualified synchronized interval is available. Whole-wave throughput includes prefill and queueing. A valid decode interval can survive inside an overall failed or partial check; the source-report outcome is preserved. No rows are averaged.

## Additional Test Results

| Result / Source | Profile | Evidence type | Reported outcome | Retained values | Configuration binding |
| --- | --- | --- | --- | --- | --- |
| [result-0b3300ff6b31d2e84720](../observations.json)<br>source-ab89fca7e0f49696d5258b56.json<br>`/profiles/24/current_config/operational_validation` | [MODEL-PROFILE-BASELINE-26](MODEL-PROFILE-BASELINE-26.md)<br>[qwen3.8-27b-exl3](qwen3.8-27b-exl3.md) | context allocation | Outcome unspecified | context_tokens=262,144 tokens | Recorded configuration/job |
| [result-15a7cb2d4e3a20c42392](../observations.json)<br>source-e18d36de0771b15b1c6245a4.json<br>`/measurements/one_stream_per_card/waves/cold` | [qwen3.8-27b-exl3](qwen3.8-27b-exl3.md) | test outcome | Outcome unspecified | generated_tokens=3,037 accepted tokens | Exact configuration unresolved |
| [result-2528694c091ec66002ac](../observations.json)<br>source-e18d36de0771b15b1c6245a4.json<br>`/thermal/2` | [qwen3.8-27b-exl3](qwen3.8-27b-exl3.md) | test outcome | Outcome unspecified | managed_ram_peak_bytes=22,590,824,448 bytes | Exact configuration unresolved |
| [result-2da4021b055925c08ba6](../observations.json)<br>source-335ade44cfeb9741ec4adac7.json<br>`/cold/replicas/2/rates` | [qwen3.8-27b-exl3](qwen3.8-27b-exl3.md) | test outcome | Outcome unspecified | end_to_end_output_tps=166.21 accepted tokens/s; generated_tokens=16,384 accepted tokens; wall_seconds=98.58 s | Recorded configuration/job |
| [result-307ef4e82c87bcc8a7dd](../observations.json)<br>source-e18d36de0771b15b1c6245a4.json<br>`/measurements/sixteen_streams_per_card/waves/cold` | [qwen3.8-27b-exl3](qwen3.8-27b-exl3.md) | test outcome | Outcome unspecified | generated_tokens=44,726 accepted tokens | Exact configuration unresolved |
| [result-3bbc8f8c0a4ae6fc2e17](../observations.json)<br>source-e18d36de0771b15b1c6245a4.json<br>`/thermal/1` | [qwen3.8-27b-exl3](qwen3.8-27b-exl3.md) | test outcome | Outcome unspecified | managed_ram_peak_bytes=22,524,108,800 bytes | Exact configuration unresolved |
| [result-3f83d7f322790eafc2e1](../observations.json)<br>source-5dba3f0789c94fd2013c38a3.json<br>`/jobs/2/settings` | [qwen3.8-27b-exl3](qwen3.8-27b-exl3.md) | test outcome | Outcome unspecified | context=262,144 tokens | Recorded configuration/job |
| [result-4071b7d643b339eb5526](../observations.json)<br>source-e18d36de0771b15b1c6245a4.json<br>`/thermal/0` | [qwen3.8-27b-exl3](qwen3.8-27b-exl3.md) | test outcome | Outcome unspecified | managed_ram_peak_bytes=22,480,969,728 bytes | Exact configuration unresolved |
| [result-40959c288612c53f3e80](../observations.json)<br>source-c520a462129a4cabc1643162.json<br>`/warm/replicas/1/rates` | [qwen3.8-27b-exl3](qwen3.8-27b-exl3.md) | test outcome | Outcome unspecified | end_to_end_output_tps=42.98 accepted tokens/s; generated_tokens=1,024 accepted tokens; wall_seconds=23.83 s | Recorded configuration/job |
| [result-41c3eb8f869af03109d0](../observations.json)<br>source-5dba3f0789c94fd2013c38a3.json<br>`/jobs/2/settings/totals` | [qwen3.8-27b-exl3](qwen3.8-27b-exl3.md) | context allocation | Outcome unspecified | cached_tokens=0 tokens; generated_tokens=0 accepted tokens; prompt_tokens=0 tokens; recurrent_restores=0 checkpoints | Recorded configuration/job |
| [result-4f6486ad9ac6d217f7e6](../observations.json)<br>source-c520a462129a4cabc1643162.json<br>`/warm/replicas/2/rates` | [qwen3.8-27b-exl3](qwen3.8-27b-exl3.md) | test outcome | Outcome unspecified | end_to_end_output_tps=42.70 accepted tokens/s; generated_tokens=1,024 accepted tokens; wall_seconds=23.98 s | Recorded configuration/job |
| [result-531676ce8aa3ae5d0e2c](../observations.json)<br>source-335ade44cfeb9741ec4adac7.json<br>`/warm/replicas/0/rates` | [qwen3.8-27b-exl3](qwen3.8-27b-exl3.md) | test outcome | Outcome unspecified | end_to_end_output_tps=203.23 accepted tokens/s; generated_tokens=16,384 accepted tokens; wall_seconds=80.62 s | Recorded configuration/job |
| [result-571dd923567ddf1ddc67](../observations.json)<br>source-e18d36de0771b15b1c6245a4.json<br>`/measurements/sixteen_streams_per_card/waves/warm` | [qwen3.8-27b-exl3](qwen3.8-27b-exl3.md) | test outcome | Outcome unspecified | generated_tokens=45,495 accepted tokens | Exact configuration unresolved |
| [result-6811164bc91ae3fedb2d](../observations.json)<br>source-335ade44cfeb9741ec4adac7.json<br>`/warm/replicas/1/rates` | [qwen3.8-27b-exl3](qwen3.8-27b-exl3.md) | test outcome | Outcome unspecified | end_to_end_output_tps=188.93 accepted tokens/s; generated_tokens=16,384 accepted tokens; wall_seconds=86.72 s | Recorded configuration/job |
| [result-688fef038d474c548e41](../observations.json)<br>source-335ade44cfeb9741ec4adac7.json<br>`/warm/replicas/2/rates` | [qwen3.8-27b-exl3](qwen3.8-27b-exl3.md) | test outcome | Outcome unspecified | end_to_end_output_tps=186.54 accepted tokens/s; generated_tokens=16,384 accepted tokens; wall_seconds=87.83 s | Recorded configuration/job |
| [result-6b36a67909c59e3a6c9d](../observations.json)<br>source-5dba3f0789c94fd2013c38a3.json<br>`/jobs/1/settings/totals` | [qwen3.8-27b-exl3](qwen3.8-27b-exl3.md) | context allocation | Outcome unspecified | cached_tokens=0 tokens; generated_tokens=0 accepted tokens; prompt_tokens=0 tokens; recurrent_restores=0 checkpoints | Recorded configuration/job |
| [result-76e20e21d993a6aef0a1](../observations.json)<br>source-335ade44cfeb9741ec4adac7.json<br>`/cold/replicas/1/rates` | [qwen3.8-27b-exl3](qwen3.8-27b-exl3.md) | test outcome | Outcome unspecified | end_to_end_output_tps=168.85 accepted tokens/s; generated_tokens=16,384 accepted tokens; wall_seconds=97.03 s | Recorded configuration/job |
| [result-854db24b9097e0746ea8](../observations.json)<br>source-e18d36de0771b15b1c6245a4.json<br>`/measurements/one_stream_per_card/waves/warm` | [qwen3.8-27b-exl3](qwen3.8-27b-exl3.md) | test outcome | Outcome unspecified | generated_tokens=3,019 accepted tokens | Exact configuration unresolved |
| [result-920df0e6e6457338763a](../observations.json)<br>source-c520a462129a4cabc1643162.json<br>`/cold/replicas/2/rates` | [qwen3.8-27b-exl3](qwen3.8-27b-exl3.md) | test outcome | Outcome unspecified | end_to_end_output_tps=42.96 accepted tokens/s; generated_tokens=1,024 accepted tokens; wall_seconds=23.83 s | Recorded configuration/job |
| [result-923b3b71a55d253205d9](../observations.json)<br>source-5dba3f0789c94fd2013c38a3.json<br>`/jobs/1/settings` | [qwen3.8-27b-exl3](qwen3.8-27b-exl3.md) | test outcome | Outcome unspecified | context=262,144 tokens | Recorded configuration/job |
| [result-93208d83f362b1d32178](../observations.json)<br>source-5dba3f0789c94fd2013c38a3.json<br>`/jobs/1/settings/cache` | [qwen3.8-27b-exl3](qwen3.8-27b-exl3.md) | test outcome | Outcome unspecified | cached_tokens=0 tokens | Recorded configuration/job |
| [result-93b03b15b70b0ba5dae0](../observations.json)<br>source-c520a462129a4cabc1643162.json<br>`/warm/replicas/0/rates` | [qwen3.8-27b-exl3](qwen3.8-27b-exl3.md) | test outcome | Outcome unspecified | end_to_end_output_tps=43.66 accepted tokens/s; generated_tokens=1,024 accepted tokens; wall_seconds=23.45 s | Recorded configuration/job |
| [result-96747a15bf1866593ed5](../observations.json)<br>source-5dba3f0789c94fd2013c38a3.json<br>`/jobs/0/settings/cache` | [qwen3.8-27b-exl3](qwen3.8-27b-exl3.md) | test outcome | Outcome unspecified | cached_tokens=0 tokens | Recorded configuration/job |
| [result-9cea33c27adc403d51e3](../observations.json)<br>source-5dba3f0789c94fd2013c38a3.json<br>`/jobs/2/settings/cache` | [qwen3.8-27b-exl3](qwen3.8-27b-exl3.md) | test outcome | Outcome unspecified | cached_tokens=0 tokens | Recorded configuration/job |
| [result-a0079339db304c02b9b5](../observations.json)<br>source-5dba3f0789c94fd2013c38a3.json<br>`/jobs/0/settings/totals` | [qwen3.8-27b-exl3](qwen3.8-27b-exl3.md) | context allocation | Outcome unspecified | cached_tokens=0 tokens; generated_tokens=0 accepted tokens; prompt_tokens=0 tokens; recurrent_restores=0 checkpoints | Recorded configuration/job |
| [result-a2aa494f3673cf63e557](../observations.json)<br>source-335ade44cfeb9741ec4adac7.json<br>`/cold/replicas/0/rates` | [qwen3.8-27b-exl3](qwen3.8-27b-exl3.md) | test outcome | Outcome unspecified | end_to_end_output_tps=178.70 accepted tokens/s; generated_tokens=16,384 accepted tokens; wall_seconds=91.69 s | Recorded configuration/job |
| [result-c84371771889fc9ee415](../observations.json)<br>source-5dba3f0789c94fd2013c38a3.json<br>`/jobs/0/settings` | [qwen3.8-27b-exl3](qwen3.8-27b-exl3.md) | test outcome | Outcome unspecified | context=262,144 tokens | Recorded configuration/job |
| [result-cf93a6f8dabb56825f3f](../observations.json)<br>source-c520a462129a4cabc1643162.json<br>`/cold/replicas/0/rates` | [qwen3.8-27b-exl3](qwen3.8-27b-exl3.md) | test outcome | Outcome unspecified | end_to_end_output_tps=43.51 accepted tokens/s; generated_tokens=1,024 accepted tokens; wall_seconds=23.54 s | Recorded configuration/job |
| [result-f69ee37cddedf12ca2bb](../observations.json)<br>source-c520a462129a4cabc1643162.json<br>`/cold/replicas/1/rates` | [qwen3.8-27b-exl3](qwen3.8-27b-exl3.md) | test outcome | Outcome unspecified | end_to_end_output_tps=43.18 accepted tokens/s; generated_tokens=1,024 accepted tokens; wall_seconds=23.71 s | Recorded configuration/job |
| [result-ff200e880e0d8dbc80d4](../observations.json)<br>source-ab89fca7e0f49696d5258b56.json<br>`/profiles/24/current_config` | [MODEL-PROFILE-BASELINE-26](MODEL-PROFILE-BASELINE-26.md)<br>[qwen3.8-27b-exl3](qwen3.8-27b-exl3.md) | context allocation | Outcome unspecified | cache_tokens=917,504 tokens; context=262,144 tokens; reserve_mib=4,096 MiB | Recorded configuration/job |

These are saved result records, including failures and bounded checks. Copies, individual requests, report summaries and regrading can overlap; their counts are not independent test repetitions. Open each result for exact values, units, configuration binding and source receipts.

There are 9 retained lifecycle records. Their states, exit codes and configuration IDs remain in [catalog.json](../catalog.json); they do not supply missing benchmark results.

[Full archive](../../README.md) | [All retained waves](../RESULTS.md) | [Data definitions](../DATA.md) | [Recommended recipes](../../../README.md)
