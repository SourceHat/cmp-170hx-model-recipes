# ab-orca-mtp3-original-layer_split-max-final-pressure-043

**Historical record. Decode interval measured.**

Model family: Orca (Qwen 3.8 27B abliterated).

Historical configurations are provided for comparison. The [recommended recipes](../../../README.md) include supported launch scripts.

Current recipes using the same recorded checkpoint repository: [qwen27-orca-mtp3-native](../../../recipes/qwen27-orca-mtp3-native/README.md). Context, cache and runtime versions can differ.

## Saved Configuration Versions

Each configuration ID identifies a distinct original settings record. Deployment fields are omitted; versions can have identical published settings after that omission. Upstream runtime commits remain unspecified where the source retained only an integration label.

| Configuration | Recorded artifact / source | Configured card counts | Context tokens | GPU pool tokens | Slots | Draft mode / tokens |
| --- | --- | --- | --- | --- | --- | --- |
| cfg-bb2e759e762dfce8829b | [Lygodactylus/Qwen3.8-27B-Uncensored-exl3-8bpw@3487b152b3](https://huggingface.co/Lygodactylus/Qwen3.8-27B-Uncensored-exl3-8bpw/tree/3487b152b302930e303dc4a2e99e7e976e3ad28f) | 1 | 262,144 | 866,560 | 8 | mtp / 3 |
| cfg-cf5e6ace357eef8628c4 | [Lygodactylus/Qwen3.8-27B-Uncensored-exl3-8bpw@3487b152b3](https://huggingface.co/Lygodactylus/Qwen3.8-27B-Uncensored-exl3-8bpw/tree/3487b152b302930e303dc4a2e99e7e976e3ad28f) | 1 | 262,144 | 866,560 | 8 | mtp / 3 |

Card counts are saved configuration choices, not a claim that every allowed placement was measured. A derived view can differ from its pinned download source.

<details>
<summary>cfg-bb2e759e762dfce8829b</summary>

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
<summary>cfg-cf5e6ace357eef8628c4</summary>

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
| [ab-orca-mtp3-original-layer_split-max-final-pressure-043](ab-orca-mtp3-original-layer_split-max-final-pressure-043.md)<br>wave-a3fa7bf86fce606df16e | layer_split; mtp / 3 | 8 | 104,230 | 128 (budget 128) | cold; reused 0 | 262,144 / 866,560 | 52.54 | Not recorded | 1.22 | 823.52 | Pass |

Rates are whole-wave totals over the stated request count. A wave may span multiple independent model instances; [measurements.json](../measurements.json) retains their contributions and the exact configuration IDs. Do not interpret a multi-instance total as one card's rate.

A dash in shared decode means no qualified synchronized interval is available. Whole-wave throughput includes prefill and queueing. A valid decode interval can survive inside an overall failed or partial check; the source-report outcome is preserved. No rows are averaged.

## Bounded Checks

| Check | Reported outcome | Retained counts / flags |
| --- | --- | --- |
| check-a6c4d953da5ab1ce72e0 | Pass | {"passed":true,"elapsed_seconds":840.9002972599992,"ttft_seconds":[815.3445179150003,822.7939666909988,822.7927624699987,823.5166788940005,823.515428783001,823.935843321,823.9346482520014,824.3572187039972],"end_to_end_accepted_tok_s":1.2177424640431396} |
| check-ed6a52cf04e718cf6332 | Pass | {"passed":true,"elapsed_seconds":840.9002972599992,"ttft_seconds":[815.3445179150003,822.7939666909988,822.7927624699987,823.5166788940005,823.515428783001,823.935843321,823.9346482520014,824.3572187039972],"end_to_end_accepted_tok_s":1.2177424640431396} |

These checks retain their reported scope. A context/allocation/retrieval check is not a general quality score or a speed qualification at that context. Exact flags and provenance are in [checks.json](../checks.json).

## Additional Test Results

| Result / Source | Profile | Evidence type | Reported outcome | Retained values | Configuration binding |
| --- | --- | --- | --- | --- | --- |
| [result-2e4ed5f53785d12dc5ad](../observations.json)<br>source-a9e622d351a86c8b776605d4.json<br>`/managed_phase_timings/43` | [ab-orca-mtp3-original-layer_split-max-final-pressure-043](ab-orca-mtp3-original-layer_split-max-final-pressure-043.md) | test outcome | Outcome unspecified | wall_seconds=873.28 s | Recorded configuration/job |
| [result-2f161995c802d21180cb](../observations.json)<br>source-b792a6ab248fc2780330c3d7.json<br>`/capacity/trials/9/peak_prefill/waves/0` | [ab-orca-mtp3-original-layer_split-max-final-pressure-043](ab-orca-mtp3-original-layer_split-max-final-pressure-043.md)<br>[orca-mtp3-original-layer_split](orca-mtp3-original-layer_split.md) | performance detail | Outcome unspecified | elapsed_seconds=840.90 s; end_to_end_accepted_tok_s=1.22 accepted tokens/s; output_tokens=128 tokens; ttft_seconds=815.34<br>822.79<br>822.79<br>823.52<br>823.52<br>823.94<br>823.93<br>824.36 s; p50_ms=138.85 ms; p95_ms=420.55 ms; prefill: per-request 127.79 to 128.60 tokens/s; Draft accepted / proposed: 671 / 1,059 tokens; fraction 0.6336 | Recorded configuration/job |
| [result-a2b0f91df082d7c721fd](../observations.json)<br>source-b792a6ab248fc2780330c3d7.json<br>`/capacity/trials/9/peak_prefill` | [ab-orca-mtp3-original-layer_split-max-final-pressure-043](ab-orca-mtp3-original-layer_split-max-final-pressure-043.md)<br>[orca-mtp3-original-layer_split](orca-mtp3-original-layer_split.md) | performance detail | Pass | elapsed_seconds=840.90 s; end_to_end_accepted_tok_s=1.22 accepted tokens/s; ttft_seconds=815.34<br>822.79<br>822.79<br>823.52<br>823.52<br>823.94<br>823.93<br>824.36 s; p50_ms=138.85 ms; p95_ms=420.55 ms; cold_prefill: per-request 127.79 to 128.60 tokens/s; Draft accepted / proposed: 671 / 1,059 tokens; fraction 0.6336 | Recorded configuration/job |

These are saved result records, including failures and bounded checks. Copies, individual requests, report summaries and regrading can overlap; their counts are not independent test repetitions. Open each result for exact values, units, configuration binding and source receipts.

There are 1 retained lifecycle records. Their states, exit codes and configuration IDs remain in [catalog.json](../catalog.json); they do not supply missing benchmark results.

[Full archive](../../README.md) | [All retained waves](../RESULTS.md) | [Data definitions](../DATA.md) | [Recommended recipes](../../../README.md)
