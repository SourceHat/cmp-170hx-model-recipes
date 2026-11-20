# flash_next-mtp3-original-tensor_parallel-ctx524288-qualification

**Historical record. Bounded checks only.**

Model family: Qwen 3.8 Flash Next.

Historical configurations are provided for comparison. The [recommended recipes](../../../README.md) include supported launch scripts.

Current recipes using the same recorded checkpoint repository: [qwen-flash-next-mtp2-layer-split](../../../recipes/qwen-flash-next-mtp2-layer-split/README.md). Context, cache and runtime versions can differ.

## Saved Configuration Versions

Each configuration ID identifies a distinct original settings record. Deployment fields are omitted; versions can have identical published settings after that omission. Upstream runtime commits remain unspecified where the source retained only an integration label.

| Configuration | Recorded artifact / source | Configured card counts | Context tokens | GPU pool tokens | Slots | Draft mode / tokens |
| --- | --- | --- | --- | --- | --- | --- |
| cfg-ec434e0cf28fc5e55777 | [turboderp/Qwen3.8-Flash-Next-exl3@d2e238feca](https://huggingface.co/turboderp/Qwen3.8-Flash-Next-exl3/tree/d2e238feca4c1c4d966943117356d8a42c2f4dcb) (derived view) | 2 | 524,288 | 1,143,296 | 6 | mtp / 3 |

Card counts are saved configuration choices, not a claim that every allowed placement was measured. A derived view can differ from its pinned download source.

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
| check-07ca7a5c3e7626e5a499 | Pass | {"history_restoration_tested":false,"context_tokens":524288,"resident_pool_tokens":1143296,"passed":true,"retention_pressure_tested":false,"actual_long_request_prompt_tokens":522294,"useful_long_context_retrieval":true,"configured_slots":6} |

These checks retain their reported scope. A context/allocation/retrieval check is not a general quality score or a speed qualification at that context. Exact flags and provenance are in [checks.json](../checks.json).

## Additional Test Results

| Result / Source | Profile | Evidence type | Reported outcome | Retained values | Configuration binding |
| --- | --- | --- | --- | --- | --- |
| [result-1b3610f3249f287914e8](../observations.json)<br>source-797606345fa45914fcd85b71.json<br>`/profiles/qwen-flash-next-mtp3-tp2-native/context` | [record-26c850ec689cf58c6b67](record-26c850ec689cf58c6b67.md)<br>[flash_next-mtp3-original-tensor_parallel-completed](flash_next-mtp3-original-tensor_parallel-completed.md)<br>[flash_next-mtp3-original-tensor_parallel-ctx524288-qualification](flash_next-mtp3-original-tensor_parallel-ctx524288-qualification.md)<br>[qwen-flash-next-mtp3-tp2-native](qwen-flash-next-mtp3-tp2-native.md)<br>[flash_next-mtp3-original-tensor_parallel](flash_next-mtp3-original-tensor_parallel.md) | context allocation | Pass | actual_long_request_prompt_tokens=522,294 tokens; configured_slots=6 requests; context_tokens=524,288 tokens; resident_pool_tokens=1,143,296 tokens; 6 mixed-length request records; history_restoration_tested=false; retention_pressure_tested=false | Recorded configuration/job |

These are saved result records, including failures and bounded checks. Copies, individual requests, report summaries and regrading can overlap; their counts are not independent test repetitions. Open each result for exact values, units, configuration binding and source receipts.

[Full archive](../../README.md) | [All retained waves](../RESULTS.md) | [Data definitions](../DATA.md) | [Recommended recipes](../../../README.md)
