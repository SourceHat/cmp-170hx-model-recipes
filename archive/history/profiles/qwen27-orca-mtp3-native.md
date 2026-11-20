# qwen27-orca-mtp3-native

**Historical record. Bounded checks only.**

Model family: Orca (Qwen 3.8 27B abliterated).

Historical configurations are provided for comparison. The [recommended recipes](../../../README.md) include supported launch scripts.

Current recipes using the same recorded checkpoint repository: [qwen27-orca-mtp3-native](../../../recipes/qwen27-orca-mtp3-native/README.md). Context, cache and runtime versions can differ.

## Saved Configuration Versions

Each configuration ID identifies a distinct original settings record. Deployment fields are omitted; versions can have identical published settings after that omission. Upstream runtime commits remain unspecified where the source retained only an integration label.

| Configuration | Recorded artifact / source | Configured card counts | Context tokens | GPU pool tokens | Slots | Draft mode / tokens |
| --- | --- | --- | --- | --- | --- | --- |
| cfg-064a2b6a08a2de098e4f | [Lygodactylus/Qwen3.8-27B-Uncensored-exl3-8bpw@3487b152b3](https://huggingface.co/Lygodactylus/Qwen3.8-27B-Uncensored-exl3-8bpw/tree/3487b152b302930e303dc4a2e99e7e976e3ad28f) | 1 | 262,144 | 866,560 | 8 | mtp / 3 |
| cfg-131abfb6ba2fbf1711b9 | [Lygodactylus/Qwen3.8-27B-Uncensored-exl3-8bpw@3487b152b3](https://huggingface.co/Lygodactylus/Qwen3.8-27B-Uncensored-exl3-8bpw/tree/3487b152b302930e303dc4a2e99e7e976e3ad28f) | 1 | 262,144 | 866,560 | 8 | mtp / 3 |
| cfg-bb2e759e762dfce8829b | [Lygodactylus/Qwen3.8-27B-Uncensored-exl3-8bpw@3487b152b3](https://huggingface.co/Lygodactylus/Qwen3.8-27B-Uncensored-exl3-8bpw/tree/3487b152b302930e303dc4a2e99e7e976e3ad28f) | 1 | 262,144 | 866,560 | 8 | mtp / 3 |
| cfg-eb687ca6d55b6e20ed52 | [Lygodactylus/Qwen3.8-27B-Uncensored-exl3-8bpw@3487b152b3](https://huggingface.co/Lygodactylus/Qwen3.8-27B-Uncensored-exl3-8bpw/tree/3487b152b302930e303dc4a2e99e7e976e3ad28f) | 1 | 262,144 | 866,560 | 8 | mtp / 3 |
| cfg-f375baffa67980366693 | [Lygodactylus/Qwen3.8-27B-Uncensored-exl3-8bpw@3487b152b3](https://huggingface.co/Lygodactylus/Qwen3.8-27B-Uncensored-exl3-8bpw/tree/3487b152b302930e303dc4a2e99e7e976e3ad28f) | 1 | 262,144 | 866,560 | 8 | mtp / 3 |

Card counts are saved configuration choices, not a claim that every allowed placement was measured. A derived view can differ from its pinned download source.

<details>
<summary>cfg-064a2b6a08a2de098e4f</summary>

```json
{
  "kind": "tabby",
  "gpu_counts": [
    1
  ],
  "context": 262144,
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
  "host_memory_gib": 0,
  "host_swap_gib": 0,
  "min_vram_mib_per_gpu": 63800,
  "min_effective_vram_mib": 63800,
  "parallelism": "layer_split",
  "transport": "host",
  "host_backing": "ordinary",
  "model_repository": "Lygodactylus/Qwen3.8-27B-Uncensored-exl3-8bpw",
  "model_revision": "3487b152b302930e303dc4a2e99e7e976e3ad28f",
  "draft_repository": null,
  "draft_revision": null,
  "recorded_runtime_label": null,
  "served_model_label": "qwen27-orca-exl3-8bpw"
}
```

Pinned model revision recorded: yes. Source receipt labels, hashes and object locators are retained in [configurations.json](../configurations.json).

</details>

<details>
<summary>cfg-131abfb6ba2fbf1711b9</summary>

```json
{
  "kind": "tabby",
  "gpu_counts": [
    1
  ],
  "context": 262144,
  "cache_tokens": 866560,
  "cache_mode": "Q8",
  "draft_cache_mode": "Q8",
  "draft_mode": "mtp",
  "draft_tokens": 3,
  "max_sessions": 8,
  "chunk_size": 512,
  "reserve_mib": 128,
  "ram_kv_mib": 0,
  "ram_recurrent_mib": 16384,
  "dynamic_draft": true,
  "output_chunk_tokens": 4096,
  "power_watts": 200,
  "host_memory_gib": 0,
  "host_swap_gib": 0,
  "min_vram_mib_per_gpu": 63800,
  "min_effective_vram_mib": 63800,
  "parallelism": "layer_split",
  "transport": "host",
  "host_backing": "ordinary",
  "model_repository": "Lygodactylus/Qwen3.8-27B-Uncensored-exl3-8bpw",
  "model_revision": "3487b152b302930e303dc4a2e99e7e976e3ad28f",
  "draft_repository": null,
  "draft_revision": null,
  "recorded_runtime_label": null,
  "served_model_label": "qwen27-orca-exl3-8bpw"
}
```

Pinned model revision recorded: yes. Source receipt labels, hashes and object locators are retained in [configurations.json](../configurations.json).

</details>

<details>
<summary>cfg-bb2e759e762dfce8829b</summary>

```json
{
  "kind": "tabby",
  "gpu_counts": [
    1
  ],
  "context": 262144,
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
  "served_model_label": "qwen27-orca-exl3-8bpw",
  "main_reserve_mib_values_unordered": []
}
```

Pinned model revision recorded: yes. Source receipt labels, hashes and object locators are retained in [configurations.json](../configurations.json).

</details>

<details>
<summary>cfg-eb687ca6d55b6e20ed52</summary>

```json
{
  "kind": "tabby",
  "gpu_counts": [
    1
  ],
  "context": 262144,
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
  "host_memory_gib": 0,
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
  "served_model_label": "qwen27-orca-exl3-8bpw"
}
```

Pinned model revision recorded: yes. Source receipt labels, hashes and object locators are retained in [configurations.json](../configurations.json).

</details>

<details>
<summary>cfg-f375baffa67980366693</summary>

```json
{
  "kind": "tabby",
  "gpu_counts": [
    1
  ],
  "context": 262144,
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
  "served_model_label": "qwen27-orca-exl3-8bpw",
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
| check-c395ff0e3d3ff34d2491 | Pass | {"context_tokens":262144,"resident_pool_tokens":866560,"passed":true,"history_restoration_answer_matched":true,"actual_long_request_prompt_tokens":253996,"useful_long_context_retrieval":true,"configured_slots":8} |

These checks retain their reported scope. A context/allocation/retrieval check is not a general quality score or a speed qualification at that context. Exact flags and provenance are in [checks.json](../checks.json).

## Additional Test Results

| Result / Source | Profile | Evidence type | Reported outcome | Retained values | Configuration binding |
| --- | --- | --- | --- | --- | --- |
| [result-14b18ac09985156a8406](../observations.json)<br>source-797606345fa45914fcd85b71.json<br>`/profiles/qwen27-orca-mtp3-native/fresh_speed/concurrent-32768` | [qwen27-orca-mtp3-native](qwen27-orca-mtp3-native.md) | test outcome | Outcome unspecified | request_count=8 requests | Recorded configuration/job |
| [result-557793db4ba745f47f23](../observations.json)<br>source-797606345fa45914fcd85b71.json<br>`/profiles/qwen27-orca-mtp3-native/fresh_speed/concurrent-2048` | [qwen27-orca-mtp3-native](qwen27-orca-mtp3-native.md) | test outcome | Outcome unspecified | request_count=8 requests | Recorded configuration/job |
| [result-562738b523785a72842e](../observations.json)<br>source-797606345fa45914fcd85b71.json<br>`/profiles/qwen27-orca-mtp3-native/old_speed/single-32768` | [qwen27-orca-mtp3-native](qwen27-orca-mtp3-native.md) | test outcome | Outcome unspecified | request_count=1 requests | Recorded configuration/job |
| [result-661888c04a062e363999](../observations.json)<br>source-797606345fa45914fcd85b71.json<br>`/profiles/qwen27-orca-mtp3-native/final` | [qwen27-orca-mtp3-native](qwen27-orca-mtp3-native.md)<br>[orca-mtp3-original-layer_split](orca-mtp3-original-layer_split.md) | context allocation | Outcome unspecified | actual_input_tokens=516,139 tokens; configured_slots=8 requests; context_limit=524,288 tokens; resident_pool_tokens=866,560 tokens | Recorded configuration/job |
| [result-695353033d8c3235300c](../observations.json)<br>source-797606345fa45914fcd85b71.json<br>`/profiles/qwen27-orca-mtp3-native/quality` | [qwen27-orca-mtp3-native](qwen27-orca-mtp3-native.md) | quality evaluation | 7 / 8 tasks passed | coding: 2 / 2; tool: 2 / 2; agent: 2 / 2; reasoning: 1 / 2; Task latency median 4.27 s; n=8 | Recorded configuration/job |
| [result-8a8c1090481318950472](../observations.json)<br>source-797606345fa45914fcd85b71.json<br>`/profiles/qwen27-orca-mtp3-native/old_speed/concurrent-32768` | [qwen27-orca-mtp3-native](qwen27-orca-mtp3-native.md) | test outcome | Outcome unspecified | request_count=8 requests | Recorded configuration/job |
| [result-8ae5e6481bb3b0c9fae1](../observations.json)<br>source-797606345fa45914fcd85b71.json<br>`/profiles/qwen27-orca-mtp3-native/old_speed/concurrent-2048` | [qwen27-orca-mtp3-native](qwen27-orca-mtp3-native.md) | test outcome | Outcome unspecified | request_count=8 requests | Recorded configuration/job |
| [result-91d0740c6c8964edce7d](../observations.json)<br>source-797606345fa45914fcd85b71.json<br>`/profiles/qwen27-orca-mtp3-native/fresh_speed/single-32768` | [qwen27-orca-mtp3-native](qwen27-orca-mtp3-native.md) | test outcome | Outcome unspecified | request_count=1 requests | Recorded configuration/job |
| [result-ab32bd191e35d16ae7b0](../observations.json)<br>source-797606345fa45914fcd85b71.json<br>`/profiles/qwen27-orca-mtp3-native/final/allocator_GPUs/0` | [qwen27-orca-mtp3-native](qwen27-orca-mtp3-native.md) | test outcome | Outcome unspecified | allocated_bytes=63,913,977,856 bytes; free_bytes=522,125,312 bytes; peak_allocated_bytes=66,180,146,176 bytes; peak_reserved_bytes=66,202,894,336 bytes; reserved_bytes=66,202,894,336 bytes | Recorded configuration/job |
| [result-b38e241da31b74865ba2](../observations.json)<br>source-797606345fa45914fcd85b71.json<br>`/profiles/qwen27-orca-mtp3-native/old_speed/single-2048` | [qwen27-orca-mtp3-native](qwen27-orca-mtp3-native.md) | test outcome | Outcome unspecified | request_count=1 requests | Recorded configuration/job |
| [result-ed97cade739117fcb105](../observations.json)<br>source-797606345fa45914fcd85b71.json<br>`/profiles/qwen27-orca-mtp3-native/context` | [record-26c850ec689cf58c6b67](record-26c850ec689cf58c6b67.md)<br>[orca-mtp3-original-layer_split-ctx262144-qualification](orca-mtp3-original-layer_split-ctx262144-qualification.md)<br>[qwen27-orca-mtp3-native](qwen27-orca-mtp3-native.md) | context allocation | Pass | actual_long_request_prompt_tokens=253,996 tokens; configured_slots=8 requests; context_tokens=262,144 tokens; resident_pool_tokens=866,560 tokens; 8 mixed-length request records | Recorded configuration/job |
| [result-ee6d7cf7eb2ce28b319c](../observations.json)<br>source-797606345fa45914fcd85b71.json<br>`/profiles/qwen27-orca-mtp3-native/fresh_speed/single-2048` | [qwen27-orca-mtp3-native](qwen27-orca-mtp3-native.md) | test outcome | Outcome unspecified | request_count=1 requests | Recorded configuration/job |
| [result-f8302bd91605bf55cf59](../observations.json)<br>source-797606345fa45914fcd85b71.json<br>`/profiles/qwen27-orca-mtp3-native` | [qwen27-orca-mtp3-native](qwen27-orca-mtp3-native.md) | context allocation | Outcome unspecified | pool=866,560 tokens; draft KV=1,885,634,560 bytes; main KV=30,170,152,960 bytes; allocator_reserved_GiB=61.30; free_GiB=1.49 | Recorded configuration/job |

These are saved result records, including failures and bounded checks. Copies, individual requests, report summaries and regrading can overlap; their counts are not independent test repetitions. Open each result for exact values, units, configuration binding and source receipts.

There are 24 retained lifecycle records. Their states, exit codes and configuration IDs remain in [catalog.json](../catalog.json); they do not supply missing benchmark results.

[Full archive](../../README.md) | [All retained waves](../RESULTS.md) | [Data definitions](../DATA.md) | [Recommended recipes](../../../README.md)
