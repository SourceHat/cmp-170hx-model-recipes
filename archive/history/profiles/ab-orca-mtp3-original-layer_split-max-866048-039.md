# ab-orca-mtp3-original-layer_split-max-866048-039

**Historical record. Legacy / incomplete measurements.**

Model family: Orca (Qwen 3.8 27B abliterated).

Historical configurations are provided for comparison. The [recommended recipes](../../../README.md) include supported launch scripts.

Current recipes using the same recorded checkpoint repository: [qwen27-orca-mtp3-native](../../../recipes/qwen27-orca-mtp3-native/README.md). Context, cache and runtime versions can differ.

## Saved Configuration Versions

Each configuration ID identifies a distinct original settings record. Deployment fields are omitted; versions can have identical published settings after that omission. Upstream runtime commits remain unspecified where the source retained only an integration label.

| Configuration | Recorded artifact / source | Configured card counts | Context tokens | GPU pool tokens | Slots | Draft mode / tokens |
| --- | --- | --- | --- | --- | --- | --- |
| cfg-18158081ace8f3e94980 | [Lygodactylus/Qwen3.8-27B-Uncensored-exl3-8bpw@3487b152b3](https://huggingface.co/Lygodactylus/Qwen3.8-27B-Uncensored-exl3-8bpw/tree/3487b152b302930e303dc4a2e99e7e976e3ad28f) | 1 | 262,144 | 866,048 | 8 | mtp / 3 |
| cfg-776e7f959b71be3610dc | [Lygodactylus/Qwen3.8-27B-Uncensored-exl3-8bpw@3487b152b3](https://huggingface.co/Lygodactylus/Qwen3.8-27B-Uncensored-exl3-8bpw/tree/3487b152b302930e303dc4a2e99e7e976e3ad28f) | 1 | 262,144 | 866,048 | 8 | mtp / 3 |

Card counts are saved configuration choices, not a claim that every allowed placement was measured. A derived view can differ from its pinned download source.

<details>
<summary>cfg-18158081ace8f3e94980</summary>

```json
{
  "kind": "tabby",
  "gpu_counts": [
    1
  ],
  "context": 262144,
  "cache_tokens": 866048,
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
<summary>cfg-776e7f959b71be3610dc</summary>

```json
{
  "kind": "tabby",
  "gpu_counts": [
    1
  ],
  "context": 262144,
  "cache_tokens": 866048,
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
| [ab-orca-mtp3-original-layer_split-max-866048-039](ab-orca-mtp3-original-layer_split-max-866048-039.md)<br>wave-364012b67079835c6f29 | layer_split; mtp / 3 | 8 | 2,027 | 16 (budget 16) | cold; reused 0 | 262,144 / 866,048 | Not recorded | Not recorded | 9.26 | 12.68 | Pass |
| [ab-orca-mtp3-original-layer_split-max-866048-039](ab-orca-mtp3-original-layer_split-max-866048-039.md)<br>wave-d7a60120b33b2e62fe32 | layer_split; mtp / 3 | 8 | 2,027 | 16 (budget 16) | cold; reused 0 | 262,144 / 866,048 | Not recorded | Not recorded | 9.26 | 12.68 | Pass |

Rates are whole-wave totals over the stated request count. A wave may span multiple independent model instances; [measurements.json](../measurements.json) retains their contributions and the exact configuration IDs. Do not interpret a multi-instance total as one card's rate.

A dash in shared decode means no qualified synchronized interval is available. Whole-wave throughput includes prefill and queueing. A valid decode interval can survive inside an overall failed or partial check; the source-report outcome is preserved. No rows are averaged.

## Bounded Checks

| Check | Reported outcome | Retained counts / flags |
| --- | --- | --- |
| check-0bcdcd1e8c0cf254a8e0 | Pass | {"passed":true,"elapsed_seconds":13.817701750002016,"ttft_seconds":[9.542782139000337,11.676515220999136,11.675567803999002,11.675186438002129,13.691140282997367,13.69080871800179,13.691024348998326,13.690629832002742],"end_to_end_accepted_tok_s":9.263479724475985} |
| check-a0dc104d6039ba3be027 | Pass | {"passed":true,"elapsed_seconds":13.817701750002016,"ttft_seconds":[9.542782139000337,11.676515220999136,11.675567803999002,11.675186438002129,13.691140282997367,13.69080871800179,13.691024348998326,13.690629832002742],"end_to_end_accepted_tok_s":9.263479724475985} |

These checks retain their reported scope. A context/allocation/retrieval check is not a general quality score or a speed qualification at that context. Exact flags and provenance are in [checks.json](../checks.json).

## Additional Test Results

| Result / Source | Profile | Evidence type | Reported outcome | Retained values | Configuration binding |
| --- | --- | --- | --- | --- | --- |
| [result-0e0a40a361a40fe8c8b2](../observations.json)<br>source-b792a6ab248fc2780330c3d7.json<br>`/capacity/trials/6/peak_prefill` | [ab-orca-mtp3-original-layer_split-max-866048-039](ab-orca-mtp3-original-layer_split-max-866048-039.md)<br>[orca-mtp3-original-layer_split](orca-mtp3-original-layer_split.md) | performance detail | Pass | elapsed_seconds=13.82 s; end_to_end_accepted_tok_s=9.26 accepted tokens/s; ttft_seconds=9.54<br>11.68<br>11.68<br>11.68<br>13.69<br>13.69<br>13.69<br>13.69 s; p50_ms=27.37 ms; p95_ms=27.37 ms; cold_prefill: per-request 208.11 to 413.67 tokens/s; Draft accepted / proposed: 96 / 96 tokens; fraction 1.0000 | Recorded configuration/job |
| [result-a95b904417c5749cf33e](../observations.json)<br>source-a9e622d351a86c8b776605d4.json<br>`/managed_phase_timings/39` | [ab-orca-mtp3-original-layer_split-max-866048-039](ab-orca-mtp3-original-layer_split-max-866048-039.md) | test outcome | Outcome unspecified | wall_seconds=31.09 s | Recorded configuration/job |
| [result-d6ef2620914c585ad0bc](../observations.json)<br>source-b792a6ab248fc2780330c3d7.json<br>`/capacity/trials/6/peak_prefill/waves/0` | [ab-orca-mtp3-original-layer_split-max-866048-039](ab-orca-mtp3-original-layer_split-max-866048-039.md)<br>[orca-mtp3-original-layer_split](orca-mtp3-original-layer_split.md) | performance detail | Outcome unspecified | elapsed_seconds=13.82 s; end_to_end_accepted_tok_s=9.26 accepted tokens/s; output_tokens=16 tokens; ttft_seconds=9.54<br>11.68<br>11.68<br>11.68<br>13.69<br>13.69<br>13.69<br>13.69 s; p50_ms=27.37 ms; p95_ms=27.37 ms; prefill: per-request 208.11 to 413.67 tokens/s; Draft accepted / proposed: 96 / 96 tokens; fraction 1.0000 | Recorded configuration/job |
| [result-f453f3b2c9ee4831d7c3](../observations.json)<br>source-b792a6ab248fc2780330c3d7.json<br>`/capacity/trials/6` | [ab-orca-mtp3-original-layer_split-max-866048-039](ab-orca-mtp3-original-layer_split-max-866048-039.md)<br>[orca-mtp3-original-layer_split](orca-mtp3-original-layer_split.md) | context allocation | Outcome unspecified | context_tokens=262,144 tokens; resident_pool_tokens=866,048 tokens | Recorded configuration/job |

These are saved result records, including failures and bounded checks. Copies, individual requests, report summaries and regrading can overlap; their counts are not independent test repetitions. Open each result for exact values, units, configuration binding and source receipts.

There are 1 retained lifecycle records. Their states, exit codes and configuration IDs remain in [catalog.json](../catalog.json); they do not supply missing benchmark results.

[Full archive](../../README.md) | [All retained waves](../RESULTS.md) | [Data definitions](../DATA.md) | [Recommended recipes](../../../README.md)
