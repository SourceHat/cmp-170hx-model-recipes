# orca-mtp3-original-layer_split-completed

**Historical record. Bounded checks only.**

Model family: Orca (Qwen 3.8 27B abliterated).

Historical configurations are provided for comparison. The [recommended recipes](../../../README.md) include supported launch scripts.

Current recipes using the same recorded checkpoint repository: [qwen27-orca-mtp3-native](../../../recipes/qwen27-orca-mtp3-native/README.md). Context, cache and runtime versions can differ.

## Saved Configuration Versions

Each configuration ID identifies a distinct original settings record. Deployment fields are omitted; versions can have identical published settings after that omission. Upstream runtime commits remain unspecified where the source retained only an integration label.

| Configuration | Recorded artifact / source | Configured card counts | Context tokens | GPU pool tokens | Slots | Draft mode / tokens |
| --- | --- | --- | --- | --- | --- | --- |
| cfg-bb2e759e762dfce8829b | [Lygodactylus/Qwen3.8-27B-Uncensored-exl3-8bpw@3487b152b3](https://huggingface.co/Lygodactylus/Qwen3.8-27B-Uncensored-exl3-8bpw/tree/3487b152b302930e303dc4a2e99e7e976e3ad28f) | 1 | 262,144 | 866,560 | 8 | mtp / 3 |

Card counts are saved configuration choices, not a claim that every allowed placement was measured. A derived view can differ from its pinned download source.

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

## Retained Measurements

No detailed benchmark receipt is matched to this record. A saved definition or a successful job exit alone is not a performance measurement.

A dash in shared decode means no qualified synchronized interval is available. Whole-wave throughput includes prefill and queueing. A valid decode interval can survive inside an overall failed or partial check; the source-report outcome is preserved. No rows are averaged.

## Bounded Checks

| Check | Reported outcome | Retained counts / flags |
| --- | --- | --- |
| check-ed2883eeddd877b20b2e | Pass | {"reserve_mib":128,"passed":true} |

These checks retain their reported scope. A context/allocation/retrieval check is not a general quality score or a speed qualification at that context. Exact flags and provenance are in [checks.json](../checks.json).

## Additional Test Results

| Result / Source | Profile | Evidence type | Reported outcome | Retained values | Configuration binding |
| --- | --- | --- | --- | --- | --- |
| [result-04815054c28ff6ff88fb](../observations.json)<br>source-b792a6ab248fc2780330c3d7.json<br>`/capacity/failures/1` | [record-26c850ec689cf58c6b67](record-26c850ec689cf58c6b67.md)<br>[orca-mtp3-original-layer_split-completed](orca-mtp3-original-layer_split-completed.md)<br>[orca-mtp3-original-layer_split](orca-mtp3-original-layer_split.md) | context allocation | Error recorded | pool=883,968 tokens | Recorded configuration/job |
| [result-33e86345b5044949ca1e](../observations.json)<br>source-b792a6ab248fc2780330c3d7.json<br>`/capacity/failures/4` | [record-26c850ec689cf58c6b67](record-26c850ec689cf58c6b67.md)<br>[orca-mtp3-original-layer_split-completed](orca-mtp3-original-layer_split-completed.md)<br>[orca-mtp3-original-layer_split](orca-mtp3-original-layer_split.md) | context allocation | Error recorded | pool=866,816 tokens | Recorded configuration/job |
| [result-78fb734ff5c1b5516630](../observations.json)<br>source-b792a6ab248fc2780330c3d7.json<br>`/capacity/trials/9` | [record-26c850ec689cf58c6b67](record-26c850ec689cf58c6b67.md)<br>[orca-mtp3-original-layer_split-completed](orca-mtp3-original-layer_split-completed.md)<br>[orca-mtp3-original-layer_split](orca-mtp3-original-layer_split.md) | context allocation | Outcome unspecified | context_tokens=262,144 tokens; resident_pool_tokens=866,560 tokens | Recorded configuration/job |
| [result-90e935d9cb6b193514c1](../observations.json)<br>source-b792a6ab248fc2780330c3d7.json<br>`/capacity` | [record-26c850ec689cf58c6b67](record-26c850ec689cf58c6b67.md)<br>[orca-mtp3-original-layer_split-completed](orca-mtp3-original-layer_split-completed.md)<br>[orca-mtp3-original-layer_split](orca-mtp3-original-layer_split.md) | context allocation | Outcome unspecified | maximum_resident_pool_tokens=866,560 tokens; planning_reserve_mib=128 MiB | Recorded configuration/job |
| [result-9fec2762c681d35e65b4](../observations.json)<br>source-b792a6ab248fc2780330c3d7.json<br>`/capacity/failures/2` | [record-26c850ec689cf58c6b67](record-26c850ec689cf58c6b67.md)<br>[orca-mtp3-original-layer_split-completed](orca-mtp3-original-layer_split-completed.md)<br>[orca-mtp3-original-layer_split](orca-mtp3-original-layer_split.md) | context allocation | Error recorded | pool=870,912 tokens | Recorded configuration/job |
| [result-c2d8ab3b6d8af595138a](../observations.json)<br>source-b792a6ab248fc2780330c3d7.json<br>`/capacity/failures/0` | [record-26c850ec689cf58c6b67](record-26c850ec689cf58c6b67.md)<br>[orca-mtp3-original-layer_split-completed](orca-mtp3-original-layer_split-completed.md)<br>[orca-mtp3-original-layer_split](orca-mtp3-original-layer_split.md) | context allocation | Error recorded | pool=935,424 tokens | Recorded configuration/job |
| [result-c42ea96da5d843de60f0](../observations.json)<br>source-b792a6ab248fc2780330c3d7.json<br>`/capacity/failures/3` | [record-26c850ec689cf58c6b67](record-26c850ec689cf58c6b67.md)<br>[orca-mtp3-original-layer_split-completed](orca-mtp3-original-layer_split-completed.md)<br>[orca-mtp3-original-layer_split](orca-mtp3-original-layer_split.md) | context allocation | Error recorded | pool=867,584 tokens | Recorded configuration/job |
| [result-e19b024365027463b36e](../observations.json)<br>source-b792a6ab248fc2780330c3d7.json<br>`/capacity/headroom_trials/0` | [record-26c850ec689cf58c6b67](record-26c850ec689cf58c6b67.md)<br>[orca-mtp3-original-layer_split-completed](orca-mtp3-original-layer_split-completed.md)<br>[orca-mtp3-original-layer_split](orca-mtp3-original-layer_split.md) | context allocation | Pass | reserve_mib=128 MiB | Recorded configuration/job |
| [result-f51f0655170f769755d8](../observations.json)<br>source-b792a6ab248fc2780330c3d7.json<br>`/capacity/trials/8` | [record-26c850ec689cf58c6b67](record-26c850ec689cf58c6b67.md)<br>[orca-mtp3-original-layer_split-completed](orca-mtp3-original-layer_split-completed.md)<br>[orca-mtp3-original-layer_split](orca-mtp3-original-layer_split.md) | context allocation | Outcome unspecified | context_tokens=262,144 tokens; resident_pool_tokens=866,560 tokens | Recorded configuration/job |

These are saved result records, including failures and bounded checks. Copies, individual requests, report summaries and regrading can overlap; their counts are not independent test repetitions. Open each result for exact values, units, configuration binding and source receipts.

[Full archive](../../README.md) | [All retained waves](../RESULTS.md) | [Data definitions](../DATA.md) | [Recommended recipes](../../../README.md)
