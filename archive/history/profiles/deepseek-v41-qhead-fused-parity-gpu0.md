# deepseek-v41-qhead-fused-parity-gpu0

**Historical record. Additional test results; no matched decode wave.**

Model family: DeepSeek.

Historical configurations are provided for comparison. The [recommended recipes](../../../README.md) include supported launch scripts.

## Saved Configuration Versions

Each configuration ID identifies a distinct original settings record. Deployment fields are omitted; versions can have identical published settings after that omission. Upstream runtime commits remain unspecified where the source retained only an integration label.

| Configuration | Recorded artifact / source | Configured card counts | Context tokens | GPU pool tokens | Slots | Draft mode / tokens |
| --- | --- | --- | --- | --- | --- | --- |
| cfg-ad5ddf94ef4ca9487b83 | Identity not retained | 1 | Not recorded | Not recorded | Not recorded | unspecified / - |

Card counts are saved configuration choices, not a claim that every allowed placement was measured. A derived view can differ from its pinned download source.

<details>
<summary>cfg-ad5ddf94ef4ca9487b83</summary>

```json
{
  "kind": "command",
  "gpu_counts": [
    1
  ],
  "power_watts": 200,
  "host_memory_gib": 4,
  "host_swap_gib": 0,
  "min_vram_mib_per_gpu": 1024,
  "min_effective_vram_mib": 1024,
  "model_repository": null,
  "model_revision": null,
  "draft_repository": null,
  "draft_revision": null,
  "recorded_runtime_label": null,
  "served_model_label": null
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
| [result-10b2af6fff9b07b2c910](../observations.json)<br>source-ab3789687e5c6630011605a2.json<br>`/job` | [deepseek-v41-qhead-fused-parity-gpu0](deepseek-v41-qhead-fused-parity-gpu0.md) | test outcome | completed | See exact JSON for retained flags and timers | Recorded configuration/job |

These are saved result records, including failures and bounded checks. Copies, individual requests, report summaries and regrading can overlap; their counts are not independent test repetitions. Open each result for exact values, units, configuration binding and source receipts.

[Full archive](../../README.md) | [All retained waves](../RESULTS.md) | [Data definitions](../DATA.md) | [Recommended recipes](../../../README.md)
