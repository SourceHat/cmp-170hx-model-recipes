# ad019-flash_next-mtp3-original-tensor_parallel-sizing-final-smoke-115

**Historical record. Bounded checks only.**

Model family: Qwen 3.8 Flash Next.

Historical configurations are provided for comparison. The [recommended recipes](../../../README.md) include supported launch scripts.

Current recipes using the same recorded checkpoint repository: [qwen-flash-next-mtp2-layer-split](../../../recipes/qwen-flash-next-mtp2-layer-split/README.md). Context, cache and runtime versions can differ.

## Saved Configuration Versions

Each configuration ID identifies a distinct original settings record. Deployment fields are omitted; versions can have identical published settings after that omission. Upstream runtime commits remain unspecified where the source retained only an integration label.

| Configuration | Recorded artifact / source | Configured card counts | Context tokens | GPU pool tokens | Slots | Draft mode / tokens |
| --- | --- | --- | --- | --- | --- | --- |
| cfg-5403991c2e42bab16813 | [turboderp/Qwen3.8-Flash-Next-exl3@d2e238feca](https://huggingface.co/turboderp/Qwen3.8-Flash-Next-exl3/tree/d2e238feca4c1c4d966943117356d8a42c2f4dcb) (derived view) | 2 | 524,288 | 1,143,296 | 6 | mtp / 3 |
| cfg-ec434e0cf28fc5e55777 | [turboderp/Qwen3.8-Flash-Next-exl3@d2e238feca](https://huggingface.co/turboderp/Qwen3.8-Flash-Next-exl3/tree/d2e238feca4c1c4d966943117356d8a42c2f4dcb) (derived view) | 2 | 524,288 | 1,143,296 | 6 | mtp / 3 |

Card counts are saved configuration choices, not a claim that every allowed placement was measured. A derived view can differ from its pinned download source.

<details>
<summary>cfg-5403991c2e42bab16813</summary>

```json
{
  "kind": "tabby",
  "gpu_counts": [
    2
  ],
  "context": 524288,
  "cache_tokens": 1143296,
  "cache_mode": "Q8",
  "draft_cache_mode": "Q8",
  "draft_mode": "mtp",
  "draft_tokens": 3,
  "max_sessions": 6,
  "chunk_size": 512,
  "reserve_mib": 2048,
  "ram_kv_mib": 8192,
  "ram_recurrent_mib": 16384,
  "ngram_ram": true,
  "dynamic_draft": false,
  "output_chunk_tokens": 4096,
  "power_watts": 200,
  "host_memory_gib": 80,
  "host_swap_gib": 0,
  "min_vram_mib_per_gpu": 65530,
  "min_effective_vram_mib": 131060,
  "parallelism": "tensor_parallel",
  "transport": "host",
  "host_backing": "ordinary",
  "model_repository": "turboderp/Qwen3.8-Flash-Next-exl3",
  "model_revision": "d2e238feca4c1c4d966943117356d8a42c2f4dcb",
  "draft_repository": null,
  "draft_revision": null,
  "recorded_runtime_label": null,
  "served_model_label": "qwen3.8-flash-next-yarn524k",
  "derived_model_view_used": true,
  "model_view_metadata_included": false
}
```

Pinned model revision recorded: yes. Source receipt labels, hashes and object locators are retained in [configurations.json](../configurations.json).

</details>

<details>
<summary>cfg-ec434e0cf28fc5e55777</summary>

```json
{
  "kind": "tabby",
  "gpu_counts": [
    2
  ],
  "context": 524288,
  "cache_tokens": 1143296,
  "cache_mode": "Q8",
  "draft_cache_mode": "Q8",
  "draft_mode": "mtp",
  "draft_tokens": 3,
  "max_sessions": 6,
  "chunk_size": 512,
  "reserve_mib": 2048,
  "ram_kv_mib": 8192,
  "ram_recurrent_mib": 16384,
  "ngram_ram": true,
  "dynamic_draft": false,
  "output_chunk_tokens": 4096,
  "power_watts": 200,
  "host_memory_gib": 80,
  "host_swap_gib": 0,
  "min_vram_mib_per_gpu": 65530,
  "min_effective_vram_mib": 131060,
  "parallelism": "tensor_parallel",
  "transport": "host",
  "host_backing": "ordinary",
  "model_repository": "turboderp/Qwen3.8-Flash-Next-exl3",
  "model_revision": "d2e238feca4c1c4d966943117356d8a42c2f4dcb",
  "draft_repository": null,
  "draft_revision": null,
  "recorded_runtime_label": null,
  "served_model_label": "qwen3.8-flash-next-yarn524k",
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
| check-8f17f3df7866fe7b517d | Pass | {"passed":true,"configured_slots":6,"context_tokens":524288} |
| check-e4943bce894de22494b3 | Pass | {"passed":true,"configured_slots":6,"context_tokens":524288} |

These checks retain their reported scope. A context/allocation/retrieval check is not a general quality score or a speed qualification at that context. Exact flags and provenance are in [checks.json](../checks.json).

## Additional Test Results

| Result / Source | Profile | Evidence type | Reported outcome | Retained values | Configuration binding |
| --- | --- | --- | --- | --- | --- |
| [result-1e813f4d442e0afac7b8](../observations.json)<br>source-797606345fa45914fcd85b71.json<br>`/profiles/qwen-flash-next-mtp3-tp2-native/final` | [ad019-flash_next-mtp3-original-tensor_parallel-sizing-final-smoke-115](ad019-flash_next-mtp3-original-tensor_parallel-sizing-final-smoke-115.md)<br>[flash_next-mtp3-original-tensor_parallel](flash_next-mtp3-original-tensor_parallel.md)<br>[qwen-flash-next-mtp3-tp2-native](qwen-flash-next-mtp3-tp2-native.md) | context allocation | Outcome unspecified | actual_input_tokens=522,294 tokens; configured_slots=6 requests; context_limit=524,288 tokens; host_peak_bytes=66,969,407,488 bytes; resident_pool_tokens=1,143,296 tokens; per_card_peak_used_MiB_unordered=63,055.00<br>63,449.00; exact_boundary_measured=false | Recorded configuration/job |
| [result-ed381d62c0fe8cd34de3](../observations.json)<br>source-e9709fe18fa406dbba87624f.json<br>`/capacity/trials/1/peak_prefill` | [ad019-flash_next-mtp3-original-tensor_parallel-sizing-final-smoke-115](ad019-flash_next-mtp3-original-tensor_parallel-sizing-final-smoke-115.md)<br>[flash_next-mtp3-original-tensor_parallel](flash_next-mtp3-original-tensor_parallel.md) | context allocation | Pass | configured_slots=6 requests; context_tokens=524,288 tokens | Recorded configuration/job |

These are saved result records, including failures and bounded checks. Copies, individual requests, report summaries and regrading can overlap; their counts are not independent test repetitions. Open each result for exact values, units, configuration binding and source receipts.

There are 1 retained lifecycle records. Their states, exit codes and configuration IDs remain in [catalog.json](../catalog.json); they do not supply missing benchmark results.

[Full archive](../../README.md) | [All retained waves](../RESULTS.md) | [Data definitions](../DATA.md) | [Recommended recipes](../../../README.md)
