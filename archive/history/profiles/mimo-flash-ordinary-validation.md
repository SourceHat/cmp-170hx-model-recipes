# mimo-flash-ordinary-validation

**Historical record. Additional test results; no matched decode wave.**

Model family: MiMo V2.6 Flash.

Recorded archive reason: Fit, pilot or control configuration; measured serving variants have separate records.

Historical configurations are provided for comparison. The [recommended recipes](../../../README.md) include supported launch scripts.

Current recipes using the same recorded checkpoint repository: [mimo-flash-mtp1-tp3](../../../recipes/mimo-flash-mtp1-tp3/README.md). Context, cache and runtime versions can differ.

## Saved Configuration Versions

Each configuration ID identifies a distinct original settings record. Deployment fields are omitted; versions can have identical published settings after that omission. Upstream runtime commits remain unspecified where the source retained only an integration label.

| Configuration | Recorded artifact / source | Configured card counts | Context tokens | GPU pool tokens | Slots | Draft mode / tokens |
| --- | --- | --- | --- | --- | --- | --- |
| cfg-af92914cbb49142d019d | [MikeRoz/MiMo-V2.6-Flash-MOPD-4.03bpw-h8-exl3@29c8351a8b](https://huggingface.co/MikeRoz/MiMo-V2.6-Flash-MOPD-4.03bpw-h8-exl3/tree/29c8351a8b5854ec385adaeba7bbe62c790d40ea) | 3 | 32,768 | 131,072 | 8 | disabled / 1 |
| cfg-f7be88f7858d06957abe | [MikeRoz/MiMo-V2.6-Flash-MOPD-4.03bpw-h8-exl3@29c8351a8b](https://huggingface.co/MikeRoz/MiMo-V2.6-Flash-MOPD-4.03bpw-h8-exl3/tree/29c8351a8b5854ec385adaeba7bbe62c790d40ea) | 3 | 32,768 | 131,072 | 8 | disabled / 1 |

Card counts are saved configuration choices, not a claim that every allowed placement was measured. A derived view can differ from its pinned download source.

<details>
<summary>cfg-af92914cbb49142d019d</summary>

```json
{
  "kind": "tabby",
  "gpu_counts": [
    3
  ],
  "context": 32768,
  "cache_tokens": 131072,
  "cache_mode": "Q8",
  "draft_cache_mode": "Q8",
  "draft_mode": "disabled",
  "draft_tokens": 1,
  "max_sessions": 8,
  "chunk_size": 512,
  "reserve_mib": 4096,
  "ram_kv_mib": 16384,
  "ram_recurrent_mib": 4096,
  "ngram_ram": false,
  "dynamic_draft": false,
  "power_watts": 200,
  "host_memory_gib": 80,
  "host_swap_gib": 0,
  "min_vram_mib_per_gpu": 65530,
  "min_effective_vram_mib": 196000,
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

<details>
<summary>cfg-f7be88f7858d06957abe</summary>

```json
{
  "kind": "tabby",
  "gpu_counts": [
    3
  ],
  "context": 32768,
  "cache_tokens": 131072,
  "cache_mode": "Q8",
  "draft_cache_mode": "Q8",
  "draft_mode": "disabled",
  "draft_tokens": 1,
  "max_sessions": 8,
  "chunk_size": 512,
  "reserve_mib": 4096,
  "ram_kv_mib": 16384,
  "ram_recurrent_mib": 4096,
  "ngram_ram": false,
  "dynamic_draft": false,
  "power_watts": 200,
  "host_memory_gib": 80,
  "host_swap_gib": 0,
  "min_vram_mib_per_gpu": 65530,
  "min_effective_vram_mib": 196000,
  "model_repository": "MikeRoz/MiMo-V2.6-Flash-MOPD-4.03bpw-h8-exl3",
  "model_revision": "29c8351a8b5854ec385adaeba7bbe62c790d40ea",
  "draft_repository": null,
  "draft_revision": null,
  "recorded_runtime_label": null,
  "served_model_label": "mimo-v2.6-flash",
  "main_reserve_mib_values_unordered": []
}
```

Pinned model revision recorded: yes. Source receipt labels, hashes and object locators are retained in [configurations.json](../configurations.json).

</details>

## Retained Measurements

No detailed benchmark receipt is matched to this record. A saved definition or a successful job exit alone is not a performance measurement.

A dash in shared decode means no qualified synchronized interval is available. Whole-wave throughput includes prefill and queueing. A valid decode interval can survive inside an overall failed or partial check; the source-report outcome is preserved. No rows are averaged.

## Additional Test Results

| Result / Source | Profile | Evidence type | Reported outcome | Retained values | Configuration binding |
| --- | --- | --- | --- | --- | --- |
| [result-37c51259064491dd2fcc](../observations.json)<br>source-f260a437dc4ee7a138478018.json<br>`/original_job/tabby` | [mimo-flash-ordinary-validation](mimo-flash-ordinary-validation.md) | test outcome | Outcome unspecified | cache_tokens=131,072 tokens | Recorded configuration/job |

These are saved result records, including failures and bounded checks. Copies, individual requests, report summaries and regrading can overlap; their counts are not independent test repetitions. Open each result for exact values, units, configuration binding and source receipts.

There are 1 retained lifecycle records. Their states, exit codes and configuration IDs remain in [catalog.json](../catalog.json); they do not supply missing benchmark results.

[Full archive](../../README.md) | [All retained waves](../RESULTS.md) | [Data definitions](../DATA.md) | [Recommended recipes](../../../README.md)
