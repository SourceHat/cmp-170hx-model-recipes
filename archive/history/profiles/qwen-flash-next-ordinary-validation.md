# qwen-flash-next-ordinary-validation

**Historical record. Additional test results; no matched decode wave.**

Model family: Qwen 3.8 Flash Next.

Recorded archive reason: Fit, pilot or control configuration; measured serving variants have separate records.

Historical configurations are provided for comparison. The [recommended recipes](../../../README.md) include supported launch scripts.

Current recipes using the same recorded checkpoint repository: [qwen-flash-next-mtp2-layer-split](../../../recipes/qwen-flash-next-mtp2-layer-split/README.md). Context, cache and runtime versions can differ.

## Saved Configuration Versions

Each configuration ID identifies a distinct original settings record. Deployment fields are omitted; versions can have identical published settings after that omission. Upstream runtime commits remain unspecified where the source retained only an integration label.

| Configuration | Recorded artifact / source | Configured card counts | Context tokens | GPU pool tokens | Slots | Draft mode / tokens |
| --- | --- | --- | --- | --- | --- | --- |
| cfg-6ca27db91c3fe1e40de3 | [turboderp/Qwen3.8-Flash-Next-exl3@d2e238feca](https://huggingface.co/turboderp/Qwen3.8-Flash-Next-exl3/tree/d2e238feca4c1c4d966943117356d8a42c2f4dcb) | 3 | 32,768 | 131,072 | 8 | disabled / 1 |
| cfg-7cdf59e83ad104df7d97 | [turboderp/Qwen3.8-Flash-Next-exl3@d2e238feca](https://huggingface.co/turboderp/Qwen3.8-Flash-Next-exl3/tree/d2e238feca4c1c4d966943117356d8a42c2f4dcb) | 3 | 32,768 | 131,072 | 8 | disabled / 1 |

Card counts are saved configuration choices, not a claim that every allowed placement was measured. A derived view can differ from its pinned download source.

<details>
<summary>cfg-6ca27db91c3fe1e40de3</summary>

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
  "ram_kv_mib": 8192,
  "ram_recurrent_mib": 16384,
  "ngram_ram": true,
  "dynamic_draft": false,
  "power_watts": 200,
  "host_memory_gib": 80,
  "host_swap_gib": 0,
  "min_vram_mib_per_gpu": 65530,
  "min_effective_vram_mib": 196000,
  "model_repository": "turboderp/Qwen3.8-Flash-Next-exl3",
  "model_revision": "d2e238feca4c1c4d966943117356d8a42c2f4dcb",
  "draft_repository": null,
  "draft_revision": null,
  "recorded_runtime_label": null,
  "served_model_label": "qwen3.8-flash-next"
}
```

Pinned model revision recorded: yes. Source receipt labels, hashes and object locators are retained in [configurations.json](../configurations.json).

</details>

<details>
<summary>cfg-7cdf59e83ad104df7d97</summary>

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
  "ram_kv_mib": 8192,
  "ram_recurrent_mib": 16384,
  "ngram_ram": true,
  "dynamic_draft": false,
  "power_watts": 200,
  "host_memory_gib": 80,
  "host_swap_gib": 0,
  "min_vram_mib_per_gpu": 65530,
  "min_effective_vram_mib": 196000,
  "model_repository": "turboderp/Qwen3.8-Flash-Next-exl3",
  "model_revision": "d2e238feca4c1c4d966943117356d8a42c2f4dcb",
  "draft_repository": null,
  "draft_revision": null,
  "recorded_runtime_label": null,
  "served_model_label": "qwen3.8-flash-next",
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
| [result-107abac77af996a7c0a6](../observations.json)<br>source-d5dfb757ff75124c6fa7b0ae.json<br>`/backend_stats` | [qwen-flash-next-ordinary-validation](qwen-flash-next-ordinary-validation.md) | test outcome | Outcome unspecified | context=32,768 tokens | Recorded configuration/job |
| [result-352713a72584d456a744](../observations.json)<br>source-09edcb07cd5752375fcdfd34.json<br>`/status/totals` | [qwen-flash-next-ordinary-validation](qwen-flash-next-ordinary-validation.md) | context allocation | Outcome unspecified | cached_tokens=0 tokens; generated_tokens=0 accepted tokens; prompt_tokens=0 tokens; recurrent_restores=0 checkpoints | Recorded configuration/job |
| [result-378dcdd3a893af7f35ea](../observations.json)<br>source-d5dfb757ff75124c6fa7b0ae.json<br>`/backend_stats/totals` | [qwen-flash-next-ordinary-validation](qwen-flash-next-ordinary-validation.md) | context allocation | Outcome unspecified | cached_tokens=0 tokens; generated_tokens=70 accepted tokens; prompt_tokens=136 tokens; recurrent_restores=0 checkpoints | Recorded configuration/job |
| [result-4ed4828e39e0fc4a6b08](../observations.json)<br>source-073d98e3717a50bc4d06e6c5.json<br>`/tabby` | [qwen-flash-next-ordinary-validation](qwen-flash-next-ordinary-validation.md) | test outcome | Outcome unspecified | cache_tokens=131,072 tokens | Recorded configuration/job |
| [result-902e0d1788cf98cc3d1d](../observations.json)<br>source-4bb6a7c6dae4b08def283fa5.json<br>`/original_job/tabby` | [qwen-flash-next-ordinary-validation](qwen-flash-next-ordinary-validation.md) | test outcome | Outcome unspecified | cache_tokens=131,072 tokens | Recorded configuration/job |
| [result-b4efff9b192f4e64a91c](../observations.json)<br>source-09edcb07cd5752375fcdfd34.json<br>`/status` | [qwen-flash-next-ordinary-validation](qwen-flash-next-ordinary-validation.md) | test outcome | Outcome unspecified | context=32,768 tokens | Recorded configuration/job |
| [result-de1262ed1675de64dc6d](../observations.json)<br>source-d5dfb757ff75124c6fa7b0ae.json<br>`/backend_stats/cache` | [qwen-flash-next-ordinary-validation](qwen-flash-next-ordinary-validation.md) | test outcome | Outcome unspecified | cached_tokens=0 tokens | Recorded configuration/job |
| [result-e8702e737ce58157254a](../observations.json)<br>source-09edcb07cd5752375fcdfd34.json<br>`/status/cache` | [qwen-flash-next-ordinary-validation](qwen-flash-next-ordinary-validation.md) | test outcome | Outcome unspecified | cached_tokens=0 tokens | Recorded configuration/job |

These are saved result records, including failures and bounded checks. Copies, individual requests, report summaries and regrading can overlap; their counts are not independent test repetitions. Open each result for exact values, units, configuration binding and source receipts.

There are 2 retained lifecycle records. Their states, exit codes and configuration IDs remain in [catalog.json](../catalog.json); they do not supply missing benchmark results.

[Full archive](../../README.md) | [All retained waves](../RESULTS.md) | [Data definitions](../DATA.md) | [Recommended recipes](../../../README.md)
