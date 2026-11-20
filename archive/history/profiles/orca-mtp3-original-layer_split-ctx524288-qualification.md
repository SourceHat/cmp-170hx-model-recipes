# orca-mtp3-original-layer_split-ctx524288-qualification

**Historical record. Bounded checks only.**

Model family: Orca (Qwen 3.8 27B abliterated).

Historical configurations are provided for comparison. The [recommended recipes](../../../README.md) include supported launch scripts.

Current recipes using the same recorded checkpoint repository: [qwen27-orca-mtp3-native](../../../recipes/qwen27-orca-mtp3-native/README.md). Context, cache and runtime versions can differ.

## Saved Configuration Versions

Each configuration ID identifies a distinct original settings record. Deployment fields are omitted; versions can have identical published settings after that omission. Upstream runtime commits remain unspecified where the source retained only an integration label.

| Configuration | Recorded artifact / source | Configured card counts | Context tokens | GPU pool tokens | Slots | Draft mode / tokens |
| --- | --- | --- | --- | --- | --- | --- |
| cfg-cdb610fdfe92e6e57738 | [Lygodactylus/Qwen3.8-27B-Uncensored-exl3-8bpw@3487b152b3](https://huggingface.co/Lygodactylus/Qwen3.8-27B-Uncensored-exl3-8bpw/tree/3487b152b302930e303dc4a2e99e7e976e3ad28f) (derived view) | 1 | 524,288 | 866,560 | 8 | mtp / 3 |

Card counts are saved configuration choices, not a claim that every allowed placement was measured. A derived view can differ from its pinned download source.

<details>
<summary>cfg-cdb610fdfe92e6e57738</summary>

```json
{
  "kind": "tabby",
  "gpu_counts": [
    1
  ],
  "context": 524288,
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
  "served_model_label": "qwen27-orca-exl3-8bpw-yarn524k",
  "derived_model_view_used": true,
  "model_view_metadata_included": false,
  "main_reserve_mib_values_unordered": []
}
```

Pinned model revision recorded: yes. Source receipt labels, hashes and object locators are retained in [configurations.json](../configurations.json).

</details>

## Retained Measurements

No detailed benchmark receipt is matched to this record. A saved definition or a successful job exit alone is not a performance measurement.

A dash in shared decode means no qualified synchronized interval is available. Whole-wave throughput includes prefill and queueing. A valid decode interval can survive inside an overall failed or partial check; the source-report outcome is preserved. No rows are averaged.

## Bounded Checks

| Check | Reported outcome | Retained counts / flags |
| --- | --- | --- |
| check-9b0e003c1a9387f6a59d | Pass | {"context_tokens":524288,"resident_pool_tokens":866560,"passed":true,"history_restoration_answer_matched":true,"actual_long_request_prompt_tokens":516139,"useful_long_context_retrieval":true,"configured_slots":8} |

These checks retain their reported scope. A context/allocation/retrieval check is not a general quality score or a speed qualification at that context. Exact flags and provenance are in [checks.json](../checks.json).

## Additional Test Results

| Result / Source | Profile | Evidence type | Reported outcome | Retained values | Configuration binding |
| --- | --- | --- | --- | --- | --- |
| [result-d28064a3abf006aadab4](../observations.json)<br>source-797606345fa45914fcd85b71.json<br>`/profiles/qwen27-orca-mtp3-yarn524k/context` | [record-26c850ec689cf58c6b67](record-26c850ec689cf58c6b67.md)<br>[orca-mtp3-original-layer_split-ctx524288-qualification](orca-mtp3-original-layer_split-ctx524288-qualification.md)<br>[qwen27-orca-mtp3-yarn524k](qwen27-orca-mtp3-yarn524k.md) | context allocation | Pass | actual_long_request_prompt_tokens=516,139 tokens; configured_slots=8 requests; context_tokens=524,288 tokens; resident_pool_tokens=866,560 tokens; 8 mixed-length request records | Recorded configuration/job |

These are saved result records, including failures and bounded checks. Copies, individual requests, report summaries and regrading can overlap; their counts are not independent test repetitions. Open each result for exact values, units, configuration binding and source receipts.

[Full archive](../../README.md) | [All retained waves](../RESULTS.md) | [Data definitions](../DATA.md) | [Recommended recipes](../../../README.md)
