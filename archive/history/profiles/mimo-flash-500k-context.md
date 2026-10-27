# mimo-flash-500k-context

**Historical record. Bounded checks only.**

Model family: MiMo V2.6 Flash.

Historical configurations are provided for comparison. The [recommended recipes](../../../README.md) include supported launch scripts.

Current recipes using the same recorded checkpoint repository: [mimo-flash-mtp1-tp3](../../../recipes/mimo-flash-mtp1-tp3/README.md). Context, cache and runtime versions can differ.

## Saved Configuration Versions

Each configuration ID identifies a distinct original settings record. Deployment fields are omitted; versions can have identical published settings after that omission. Upstream runtime commits remain unspecified where the source retained only an integration label.

| Configuration | Recorded artifact / source | Configured card counts | Context tokens | GPU pool tokens | Slots | Draft mode / tokens |
| --- | --- | --- | --- | --- | --- | --- |
| cfg-689ebb25df47b531a2ae | [MikeRoz/MiMo-V2.6-Flash-MOPD-4.03bpw-h8-exl3@29c8351a8b](https://huggingface.co/MikeRoz/MiMo-V2.6-Flash-MOPD-4.03bpw-h8-exl3/tree/29c8351a8b5854ec385adaeba7bbe62c790d40ea) | 3 | 500,000 | 524,288 | 4 | mtp / 1 |
| cfg-dae27d8234cfa5a7d631 | [MikeRoz/MiMo-V2.6-Flash-MOPD-4.03bpw-h8-exl3@29c8351a8b](https://huggingface.co/MikeRoz/MiMo-V2.6-Flash-MOPD-4.03bpw-h8-exl3/tree/29c8351a8b5854ec385adaeba7bbe62c790d40ea) | 3 | 500,000 | 1,048,576 | 4 | mtp / 1 |

Card counts are saved configuration choices, not a claim that every allowed placement was measured. A derived view can differ from its pinned download source.

<details>
<summary>cfg-689ebb25df47b531a2ae</summary>

```json
{
  "kind": "tabby",
  "gpu_counts": [
    3
  ],
  "context": 500000,
  "cache_tokens": 524288,
  "cache_mode": "Q8",
  "draft_cache_mode": "Q8",
  "draft_mode": "mtp",
  "draft_tokens": 1,
  "max_sessions": 4,
  "chunk_size": 512,
  "reserve_mib": 4096,
  "ram_kv_mib": 32768,
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
  "main_reserve_mib_values_unordered": [
    5120
  ]
}
```

Pinned model revision recorded: yes. Source receipt labels, hashes and object locators are retained in [configurations.json](../configurations.json).

</details>

<details>
<summary>cfg-dae27d8234cfa5a7d631</summary>

```json
{
  "kind": "tabby",
  "gpu_counts": [
    3
  ],
  "context": 500000,
  "cache_tokens": 1048576,
  "cache_mode": "Q8",
  "draft_cache_mode": "Q8",
  "draft_mode": "mtp",
  "draft_tokens": 1,
  "max_sessions": 4,
  "chunk_size": 512,
  "reserve_mib": 4096,
  "ram_kv_mib": 32768,
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
  "main_reserve_mib_values_unordered": [
    5120
  ]
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
| check-edca7749b2cf698b28a8 | Failed / partial | {"passed":false,"ram_restoration_qualified":false} |

These checks retain their reported scope. A context/allocation/retrieval check is not a general quality score or a speed qualification at that context. Exact flags and provenance are in [checks.json](../checks.json).

## Additional Test Results

| Result / Source | Profile | Evidence type | Reported outcome | Retained values | Configuration binding |
| --- | --- | --- | --- | --- | --- |
| [result-25114cb65ec3c589b71d](../observations.json)<br>source-72d77091c9ef3150b060de2a.json<br>`/phases/2` | [mimo-flash-500k-context](mimo-flash-500k-context.md) | test outcome | Failed / partial | passed=false | Recorded configuration/job |
| [result-39cd5be9caad94fdd298](../observations.json)<br>source-52aef369a883986b2ec7c8e1.json<br>`/original_job/tabby` | [mimo-flash-500k-context](mimo-flash-500k-context.md) | test outcome | Outcome unspecified | cache_tokens=524,288 tokens | Recorded configuration/job |
| [result-43f5b82f0f4a7f166579](../observations.json)<br>source-72d77091c9ef3150b060de2a.json<br>`/` | [mimo-flash-500k-context](mimo-flash-500k-context.md) | test outcome | Failed / partial | ram_restoration_qualified=false | Recorded configuration/job |
| [result-467d63bfb647aee5b7f9](../observations.json)<br>source-dafa7cfd2ecedae77dbf0523.json<br>`/` | [mimo-flash-500k-context](mimo-flash-500k-context.md) | test outcome | Failed / partial | passed=false | Recorded configuration/job |
| [result-64bf10160a06c8ca7353](../observations.json)<br>source-a44ccffdec463062f2bc758f.json<br>`/original_job/tabby` | [mimo-flash-500k-context](mimo-flash-500k-context.md) | test outcome | Outcome unspecified | cache_tokens=524,288 tokens | Recorded configuration/job |
| [result-839d310d2c127d81ceae](../observations.json)<br>source-bda0459782d3e14070cfa987.json<br>`/` | [mimo-flash-500k-context](mimo-flash-500k-context.md) | test outcome | Failed / partial | passed=false | Recorded configuration/job |
| [result-9fae1f5e900b7990d21f](../observations.json)<br>source-2a5839d2f0cf78051a0abccc.json<br>`/profiles/1` | [mimo-flash-500k-context](mimo-flash-500k-context.md) | test outcome | Outcome unspecified | cache_tokens=1,048,576 tokens; context=500,000 tokens | Exact configuration unresolved |
| [result-bc40a8302d9e7e1134c0](../observations.json)<br>source-ab89fca7e0f49696d5258b56.json<br>`/profiles/10/current_config` | [mimo-flash-500k-context](mimo-flash-500k-context.md) | context allocation | Outcome unspecified | cache_tokens=524,288 tokens; context=500,000 tokens; reserve_mib=4,096 MiB | Recorded configuration/job |
| [result-dd8bff5bdc597b749e42](../observations.json)<br>source-cba4c8cf729b8993b7556568.json<br>`/original_job/tabby` | [mimo-flash-500k-context](mimo-flash-500k-context.md) | test outcome | Outcome unspecified | cache_tokens=1,048,576 tokens | Recorded configuration/job |

These are saved result records, including failures and bounded checks. Copies, individual requests, report summaries and regrading can overlap; their counts are not independent test repetitions. Open each result for exact values, units, configuration binding and source receipts.

There are 3 retained lifecycle records. Their states, exit codes and configuration IDs remain in [catalog.json](../catalog.json); they do not supply missing benchmark results.

[Full archive](../../README.md) | [All retained waves](../RESULTS.md) | [Data definitions](../DATA.md) | [Recommended recipes](../../../README.md)
