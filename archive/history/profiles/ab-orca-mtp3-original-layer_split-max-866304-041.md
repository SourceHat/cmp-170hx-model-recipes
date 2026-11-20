# ab-orca-mtp3-original-layer_split-max-866304-041

**Historical record. Legacy / incomplete measurements.**

Model family: Orca (Qwen 3.8 27B abliterated).

Historical configurations are provided for comparison. The [recommended recipes](../../../README.md) include supported launch scripts.

Current recipes using the same recorded checkpoint repository: [qwen27-orca-mtp3-native](../../../recipes/qwen27-orca-mtp3-native/README.md). Context, cache and runtime versions can differ.

## Saved Configuration Versions

Each configuration ID identifies a distinct original settings record. Deployment fields are omitted; versions can have identical published settings after that omission. Upstream runtime commits remain unspecified where the source retained only an integration label.

| Configuration | Recorded artifact / source | Configured card counts | Context tokens | GPU pool tokens | Slots | Draft mode / tokens |
| --- | --- | --- | --- | --- | --- | --- |
| cfg-cf1dfaebbbdb0bb74737 | [Lygodactylus/Qwen3.8-27B-Uncensored-exl3-8bpw@3487b152b3](https://huggingface.co/Lygodactylus/Qwen3.8-27B-Uncensored-exl3-8bpw/tree/3487b152b302930e303dc4a2e99e7e976e3ad28f) | 1 | 262,144 | 866,304 | 8 | mtp / 3 |
| cfg-d8814723cd73cfe0b2e9 | [Lygodactylus/Qwen3.8-27B-Uncensored-exl3-8bpw@3487b152b3](https://huggingface.co/Lygodactylus/Qwen3.8-27B-Uncensored-exl3-8bpw/tree/3487b152b302930e303dc4a2e99e7e976e3ad28f) | 1 | 262,144 | 866,304 | 8 | mtp / 3 |

Card counts are saved configuration choices, not a claim that every allowed placement was measured. A derived view can differ from its pinned download source.

<details>
<summary>cfg-cf1dfaebbbdb0bb74737</summary>

```json
{
  "kind": "tabby",
  "gpu_counts": [
    1
  ],
  "context": 262144,
  "cache_tokens": 866304,
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

<details>
<summary>cfg-d8814723cd73cfe0b2e9</summary>

```json
{
  "kind": "tabby",
  "gpu_counts": [
    1
  ],
  "context": 262144,
  "cache_tokens": 866304,
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

## Retained Measurements

| Profile / Wave | Layout; Draft / Tokens | Requests | Input tokens/request | Accepted output tokens/request | Cache / Reused input tokens | Context / GPU pool tokens | Shared decode tok/s total | Client after-first-token estimate tok/s | Whole-wave output tok/s | Median TTFT, s | Source report |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [ab-orca-mtp3-original-layer_split-max-866304-041](ab-orca-mtp3-original-layer_split-max-866304-041.md)<br>wave-64b91c946aa8d96e756e | layer_split; mtp / 3 | 8 | 2,027 | 16 (budget 16) | cold; reused 0 | 262,144 / 866,304 | Not recorded | Not recorded | 9.14 | 13.42 | Pass |
| [ab-orca-mtp3-original-layer_split-max-866304-041](ab-orca-mtp3-original-layer_split-max-866304-041.md)<br>wave-eb5dfed86132a2e5a37d | layer_split; mtp / 3 | 8 | 2,027 | 16 (budget 16) | cold; reused 0 | 262,144 / 866,304 | Not recorded | Not recorded | 9.14 | 13.42 | Pass |

Rates are whole-wave totals over the stated request count. A wave may span multiple independent model instances; [measurements.json](../measurements.json) retains their contributions and the exact configuration IDs. Do not interpret a multi-instance total as one card's rate.

A dash in shared decode means no qualified synchronized interval is available. Whole-wave throughput includes prefill and queueing. A valid decode interval can survive inside an overall failed or partial check; the source-report outcome is preserved. No rows are averaged.

## Bounded Checks

| Check | Reported outcome | Retained counts / flags |
| --- | --- | --- |
| check-bf07a15be213526db522 | Pass | {"passed":true,"elapsed_seconds":13.99827685299897,"ttft_seconds":[9.72816110200074,13.074628451002354,13.074426737002796,13.07421494799928,13.764827060000243,13.764648522999778,13.936925521000376,13.936736937001115],"end_to_end_accepted_tok_s":9.143982601871278} |
| check-c5177e35d54afbb33513 | Pass | {"passed":true,"elapsed_seconds":13.99827685299897,"ttft_seconds":[9.72816110200074,13.074628451002354,13.074426737002796,13.07421494799928,13.764827060000243,13.764648522999778,13.936925521000376,13.936736937001115],"end_to_end_accepted_tok_s":9.143982601871278} |

These checks retain their reported scope. A context/allocation/retrieval check is not a general quality score or a speed qualification at that context. Exact flags and provenance are in [checks.json](../checks.json).

## Additional Test Results

| Result / Source | Profile | Evidence type | Reported outcome | Retained values | Configuration binding |
| --- | --- | --- | --- | --- | --- |
| [result-45e23d6935aa2f2115e8](../observations.json)<br>source-b792a6ab248fc2780330c3d7.json<br>`/capacity/trials/7/peak_prefill/waves/0` | [ab-orca-mtp3-original-layer_split-max-866304-041](ab-orca-mtp3-original-layer_split-max-866304-041.md)<br>[orca-mtp3-original-layer_split](orca-mtp3-original-layer_split.md) | performance detail | Outcome unspecified | elapsed_seconds=14.00 s; end_to_end_accepted_tok_s=9.14 accepted tokens/s; output_tokens=16 tokens; ttft_seconds=9.73<br>13.07<br>13.07<br>13.07<br>13.76<br>13.76<br>13.94<br>13.94 s; p50_ms=27.24 ms; p95_ms=27.24 ms; prefill: per-request 207.47 to 398.23 tokens/s; Draft accepted / proposed: 96 / 96 tokens; fraction 1.0000 | Recorded configuration/job |
| [result-871f32ff7d50a72bdf6e](../observations.json)<br>source-b792a6ab248fc2780330c3d7.json<br>`/capacity/trials/7` | [ab-orca-mtp3-original-layer_split-max-866304-041](ab-orca-mtp3-original-layer_split-max-866304-041.md)<br>[orca-mtp3-original-layer_split](orca-mtp3-original-layer_split.md) | context allocation | Outcome unspecified | context_tokens=262,144 tokens; resident_pool_tokens=866,304 tokens | Recorded configuration/job |
| [result-96b4ef7384f573617ed4](../observations.json)<br>source-b792a6ab248fc2780330c3d7.json<br>`/capacity/trials/7/peak_prefill` | [ab-orca-mtp3-original-layer_split-max-866304-041](ab-orca-mtp3-original-layer_split-max-866304-041.md)<br>[orca-mtp3-original-layer_split](orca-mtp3-original-layer_split.md) | performance detail | Pass | elapsed_seconds=14.00 s; end_to_end_accepted_tok_s=9.14 accepted tokens/s; ttft_seconds=9.73<br>13.07<br>13.07<br>13.07<br>13.76<br>13.76<br>13.94<br>13.94 s; p50_ms=27.24 ms; p95_ms=27.24 ms; cold_prefill: per-request 207.47 to 398.23 tokens/s; Draft accepted / proposed: 96 / 96 tokens; fraction 1.0000 | Recorded configuration/job |
| [result-ddf59f98e56d976d761c](../observations.json)<br>source-a9e622d351a86c8b776605d4.json<br>`/managed_phase_timings/41` | [ab-orca-mtp3-original-layer_split-max-866304-041](ab-orca-mtp3-original-layer_split-max-866304-041.md) | test outcome | Outcome unspecified | wall_seconds=32.22 s | Recorded configuration/job |

These are saved result records, including failures and bounded checks. Copies, individual requests, report summaries and regrading can overlap; their counts are not independent test repetitions. Open each result for exact values, units, configuration binding and source receipts.

There are 1 retained lifecycle records. Their states, exit codes and configuration IDs remain in [catalog.json](../catalog.json); they do not supply missing benchmark results.

[Full archive](../../README.md) | [All retained waves](../RESULTS.md) | [Data definitions](../DATA.md) | [Recommended recipes](../../../README.md)
