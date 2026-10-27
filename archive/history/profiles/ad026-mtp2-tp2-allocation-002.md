# ad026-mtp2-tp2-allocation-002

**Historical record. Bounded checks only.**

Model family: Qwen 3.8 Flash Next.

Historical configurations are provided for comparison. The [recommended recipes](../../../README.md) include supported launch scripts.

Current recipes using the same recorded checkpoint repository: [qwen-flash-next-mtp2-layer-split](../../../recipes/qwen-flash-next-mtp2-layer-split/README.md). Context, cache and runtime versions can differ.

## Saved Configuration Versions

Each configuration ID identifies a distinct original settings record. Deployment fields are omitted; versions can have identical published settings after that omission. Upstream runtime commits remain unspecified where the source retained only an integration label.

| Configuration | Recorded artifact / source | Configured card counts | Context tokens | GPU pool tokens | Slots | Draft mode / tokens |
| --- | --- | --- | --- | --- | --- | --- |
| cfg-7d23c374785f52517d7d | [turboderp/Qwen3.8-Flash-Next-exl3@d2e238feca](https://huggingface.co/turboderp/Qwen3.8-Flash-Next-exl3/tree/d2e238feca4c1c4d966943117356d8a42c2f4dcb) | 2 | 262,144 | 1,143,296 | 6 | mtp / 2 |
| cfg-a0b45ee9ac9f42d0374a | [turboderp/Qwen3.8-Flash-Next-exl3@d2e238feca](https://huggingface.co/turboderp/Qwen3.8-Flash-Next-exl3/tree/d2e238feca4c1c4d966943117356d8a42c2f4dcb) | 2 | 262,144 | 1,143,296 | 6 | mtp / 2 |

Card counts are saved configuration choices, not a claim that every allowed placement was measured. A derived view can differ from its pinned download source.

<details>
<summary>cfg-7d23c374785f52517d7d</summary>

```json
{
  "kind": "tabby",
  "gpu_counts": [
    2
  ],
  "context": 262144,
  "cache_tokens": 1143296,
  "cache_mode": "Q8",
  "draft_cache_mode": "Q8",
  "draft_mode": "mtp",
  "draft_tokens": 2,
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
  "transport": "p2p",
  "host_backing": "ordinary",
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

<details>
<summary>cfg-a0b45ee9ac9f42d0374a</summary>

```json
{
  "kind": "tabby",
  "gpu_counts": [
    2
  ],
  "context": 262144,
  "cache_tokens": 1143296,
  "cache_mode": "Q8",
  "draft_cache_mode": "Q8",
  "draft_mode": "mtp",
  "draft_tokens": 2,
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
  "transport": "p2p",
  "host_backing": "ordinary",
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

## Retained Measurements

No detailed benchmark receipt is matched to this record. A saved definition or a successful job exit alone is not a performance measurement.

A dash in shared decode means no qualified synchronized interval is available. Whole-wave throughput includes prefill and queueing. A valid decode interval can survive inside an overall failed or partial check; the source-report outcome is preserved. No rows are averaged.

## Bounded Checks

| Check | Reported outcome | Retained counts / flags |
| --- | --- | --- |
| check-ef7738a8478f70a17de3 | Pass | {"actual_long_request_prompt_tokens":2055,"passed":true,"configured_slots":6,"context_tokens":4096} |

These checks retain their reported scope. A context/allocation/retrieval check is not a general quality score or a speed qualification at that context. Exact flags and provenance are in [checks.json](../checks.json).

## Additional Test Results

| Result / Source | Profile | Evidence type | Reported outcome | Retained values | Configuration binding |
| --- | --- | --- | --- | --- | --- |
| [result-1c3319e44d2e46287fa2](../observations.json)<br>source-e656b2f801b18836fcba6eee.json<br>`/flash_final_ad026/cases/2` | [ad026-mtp2-tp2-allocation-002](ad026-mtp2-tp2-allocation-002.md) | context allocation | Outcome unspecified | pool=1,143,296 tokens | Recorded configuration/job |
| [result-1cb3198278ebe616a0fc](../observations.json)<br>source-e656b2f801b18836fcba6eee.json<br>`/flash_final_ad026/cases/2/speed/single` | [ad026-mtp2-tp2-allocation-002](ad026-mtp2-tp2-allocation-002.md) | test outcome | Outcome unspecified | request_count=1 requests | Recorded configuration/job |
| [result-592afaa54ca6f6611954](../observations.json)<br>source-f91d0c80d201ca4b73acb713.json<br>`/` | [ad026-mtp2-tp2-allocation-002](ad026-mtp2-tp2-allocation-002.md) | context allocation | Pass | actual_long_request_prompt_tokens=2,055 tokens; configured_slots=6 requests; context_tokens=4,096 tokens; 6 mixed-length request records | Recorded configuration/job |
| [result-aee0dfb0f58df63c3823](../observations.json)<br>source-2d590dc5e4b1c71777f7ee21.json<br>`/tabby` | [ad026-mtp2-tp2-allocation-002](ad026-mtp2-tp2-allocation-002.md) | test outcome | Outcome unspecified | cache_tokens=1,143,296 tokens | Recorded configuration/job |
| [result-e86e4678610871d2e683](../observations.json)<br>source-e656b2f801b18836fcba6eee.json<br>`/flash_final_ad026/cases/2/speed/concurrent` | [ad026-mtp2-tp2-allocation-002](ad026-mtp2-tp2-allocation-002.md) | test outcome | Outcome unspecified | request_count=6 requests | Recorded configuration/job |

These are saved result records, including failures and bounded checks. Copies, individual requests, report summaries and regrading can overlap; their counts are not independent test repetitions. Open each result for exact values, units, configuration binding and source receipts.

There are 1 retained lifecycle records. Their states, exit codes and configuration IDs remain in [catalog.json](../catalog.json); they do not supply missing benchmark results.

[Full archive](../../README.md) | [All retained waves](../RESULTS.md) | [Data definitions](../DATA.md) | [Recommended recipes](../../../README.md)
