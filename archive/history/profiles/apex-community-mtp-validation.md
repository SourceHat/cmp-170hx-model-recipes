# apex-community-mtp-validation

**Historical record. Bounded checks only.**

Model family: Apex Flash 1 (GLM 5.3 Flash post-train).

Historical configurations are provided for comparison. The [recommended recipes](../../../README.md) include supported launch scripts.

## Saved Configuration Versions

Each configuration ID identifies a distinct original settings record. Deployment fields are omitted; versions can have identical published settings after that omission. Upstream runtime commits remain unspecified where the source retained only an integration label.

| Configuration | Recorded artifact / source | Configured card counts | Context tokens | GPU pool tokens | Slots | Draft mode / tokens |
| --- | --- | --- | --- | --- | --- | --- |
| cfg-257350d023acc4f990c0 | [wambosec/apex-flash-1-EXL3-4bpw@289ff417ee](https://huggingface.co/wambosec/apex-flash-1-EXL3-4bpw/tree/289ff417eeb5046698360d5ea317b42a05bd1497) | 3 | 32,768 | 131,072 | 4 | mtp / 1 |
| cfg-9b67f9e9bd2cc3f565aa | [wambosec/apex-flash-1-EXL3-4bpw@289ff417ee](https://huggingface.co/wambosec/apex-flash-1-EXL3-4bpw/tree/289ff417eeb5046698360d5ea317b42a05bd1497) | 3 | 32,768 | 131,072 | 4 | mtp / 1 |

Card counts are saved configuration choices, not a claim that every allowed placement was measured. A derived view can differ from its pinned download source.

<details>
<summary>cfg-257350d023acc4f990c0</summary>

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
  "draft_mode": "mtp",
  "draft_tokens": 1,
  "max_sessions": 4,
  "chunk_size": 512,
  "reserve_mib": 4096,
  "ram_kv_mib": 4096,
  "ram_recurrent_mib": 16384,
  "ngram_ram": false,
  "dynamic_draft": false,
  "power_watts": 200,
  "host_memory_gib": 80,
  "host_swap_gib": 0,
  "min_vram_mib_per_gpu": 65530,
  "min_effective_vram_mib": 196000,
  "model_repository": "wambosec/apex-flash-1-EXL3-4bpw",
  "model_revision": "289ff417eeb5046698360d5ea317b42a05bd1497",
  "draft_repository": null,
  "draft_revision": null,
  "recorded_runtime_label": null,
  "served_model_label": "apex-flash-1-community-exl3-4bpw"
}
```

Pinned model revision recorded: yes. Source receipt labels, hashes and object locators are retained in [configurations.json](../configurations.json).

</details>

<details>
<summary>cfg-9b67f9e9bd2cc3f565aa</summary>

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
  "draft_mode": "mtp",
  "draft_tokens": 1,
  "max_sessions": 4,
  "chunk_size": 512,
  "reserve_mib": 4096,
  "ram_kv_mib": 4096,
  "ram_recurrent_mib": 16384,
  "ngram_ram": false,
  "dynamic_draft": false,
  "power_watts": 200,
  "host_memory_gib": 80,
  "host_swap_gib": 0,
  "min_vram_mib_per_gpu": 65530,
  "min_effective_vram_mib": 196000,
  "model_repository": "wambosec/apex-flash-1-EXL3-4bpw",
  "model_revision": "289ff417eeb5046698360d5ea317b42a05bd1497",
  "draft_repository": null,
  "draft_revision": null,
  "recorded_runtime_label": null,
  "served_model_label": "apex-flash-1-community-exl3-4bpw",
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
| check-91c76de28c78d9e471a8 | Pass | {"passed":true,"ram_restoration_qualified":true} |

These checks retain their reported scope. A context/allocation/retrieval check is not a general quality score or a speed qualification at that context. Exact flags and provenance are in [checks.json](../checks.json).

## Additional Test Results

| Result / Source | Profile | Evidence type | Reported outcome | Retained values | Configuration binding |
| --- | --- | --- | --- | --- | --- |
| [result-4eec45aa661700a7b5ef](../observations.json)<br>source-f596eb1b05561b910db70f10.json<br>`/` | [apex-community-mtp-validation](apex-community-mtp-validation.md) | test outcome | Pass | passed=true; ram_restoration_qualified=true | Recorded configuration/job |
| [result-74b877dafaea702ddf80](../observations.json)<br>source-e9f201a3050f650e4804318a.json<br>`/original_job/tabby` | [apex-community-mtp-validation](apex-community-mtp-validation.md) | test outcome | Outcome unspecified | cache_tokens=131,072 tokens | Recorded configuration/job |
| [result-ffdeb1b683893b9b76da](../observations.json)<br>source-ab89fca7e0f49696d5258b56.json<br>`/profiles/3/current_config` | [apex-community-mtp-validation](apex-community-mtp-validation.md) | context allocation | Outcome unspecified | cache_tokens=131,072 tokens; context=32,768 tokens; reserve_mib=4,096 MiB | Recorded configuration/job |

These are saved result records, including failures and bounded checks. Copies, individual requests, report summaries and regrading can overlap; their counts are not independent test repetitions. Open each result for exact values, units, configuration binding and source receipts.

There are 1 retained lifecycle records. Their states, exit codes and configuration IDs remain in [catalog.json](../catalog.json); they do not supply missing benchmark results.

[Full archive](../../README.md) | [All retained waves](../RESULTS.md) | [Data definitions](../DATA.md) | [Recommended recipes](../../../README.md)
