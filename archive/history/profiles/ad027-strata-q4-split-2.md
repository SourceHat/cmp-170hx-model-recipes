# ad027-strata-q4-split-2

**Historical record. Additional test results; no matched decode wave.**

Model family: Other model workflows.

Historical configurations are provided for comparison. The [recommended recipes](../../../README.md) include supported launch scripts.

## Saved Configuration Versions

Each configuration ID identifies a distinct original settings record. Deployment fields are omitted; versions can have identical published settings after that omission. Upstream runtime commits remain unspecified where the source retained only an integration label.

| Configuration | Recorded artifact / source | Configured card counts | Context tokens | GPU pool tokens | Slots | Draft mode / tokens |
| --- | --- | --- | --- | --- | --- | --- |
| cfg-6a2eb67e09382c570b20 | trial-strata-q4-split | 2 | Not recorded | Not recorded | Not recorded | unspecified / - |

Card counts are saved configuration choices, not a claim that every allowed placement was measured. A derived view can differ from its pinned download source.

<details>
<summary>cfg-6a2eb67e09382c570b20</summary>

```json
{
  "kind": "command",
  "gpu_counts": [
    2
  ],
  "power_watts": 200,
  "host_memory_gib": 0,
  "host_swap_gib": 0,
  "min_vram_mib_per_gpu": 65530,
  "min_effective_vram_mib": 131060,
  "model_repository": null,
  "model_revision": null,
  "draft_repository": null,
  "draft_revision": null,
  "recorded_runtime_label": null,
  "served_model_label": "trial-strata-q4-split",
  "recorded_wrapper_settings": {
    "kind": "strata",
    "context": 262144,
    "max_sessions": 6,
    "kv_dtype": "int8",
    "draft_tokens": 3
  }
}
```

Pinned model revision recorded: no. Source receipt labels, hashes and object locators are retained in [configurations.json](../configurations.json).

</details>

## Retained Measurements

No detailed benchmark receipt is matched to this record. A saved definition or a successful job exit alone is not a performance measurement.

A dash in shared decode means no qualified synchronized interval is available. Whole-wave throughput includes prefill and queueing. A valid decode interval can survive inside an overall failed or partial check; the source-report outcome is preserved. No rows are averaged.

## Additional Test Results

| Result / Source | Profile | Evidence type | Reported outcome | Retained values | Configuration binding |
| --- | --- | --- | --- | --- | --- |
| [result-19f01d72bd4a5d35cc55](../observations.json)<br>source-ed21e72502f19e91fcf5b107.json<br>`/spec/serving_config` | [ad027-strata-q4-split-2](ad027-strata-q4-split-2.md) | test outcome | Outcome unspecified | context=262,144 tokens | Recorded configuration/job |
| [result-224c2d262cc5a2494d8e](../observations.json)<br>source-bdf6a4d92647098766e1c0b2.json<br>`/` | [ad027-strata-q4-split-2](ad027-strata-q4-split-2.md) | test outcome | failed | See exact JSON for retained flags and timers | Recorded configuration/job |

These are saved result records, including failures and bounded checks. Copies, individual requests, report summaries and regrading can overlap; their counts are not independent test repetitions. Open each result for exact values, units, configuration binding and source receipts.

There are 1 retained lifecycle records. Their states, exit codes and configuration IDs remain in [catalog.json](../catalog.json); they do not supply missing benchmark results.

[Full archive](../../README.md) | [All retained waves](../RESULTS.md) | [Data definitions](../DATA.md) | [Recommended recipes](../../../README.md)
