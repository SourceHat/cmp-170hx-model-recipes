# mimo-flash-dflash-validation

**Historical record. Decode interval measured.**

Model family: MiMo V2.6 Flash.

Historical configurations are provided for comparison. The [recommended recipes](../../../README.md) include supported launch scripts.

Current recipes using the same recorded checkpoint repository: [mimo-flash-mtp1-tp3](../../../recipes/mimo-flash-mtp1-tp3/README.md). Context, cache and runtime versions can differ.

## Saved Configuration Versions

Each configuration ID identifies a distinct original settings record. Deployment fields are omitted; versions can have identical published settings after that omission. Upstream runtime commits remain unspecified where the source retained only an integration label.

| Configuration | Recorded artifact / source | Configured card counts | Context tokens | GPU pool tokens | Slots | Draft mode / tokens |
| --- | --- | --- | --- | --- | --- | --- |
| cfg-3a775a77bffe73e24773 | [MikeRoz/MiMo-V2.6-Flash-MOPD-4.03bpw-h8-exl3@29c8351a8b](https://huggingface.co/MikeRoz/MiMo-V2.6-Flash-MOPD-4.03bpw-h8-exl3/tree/29c8351a8b5854ec385adaeba7bbe62c790d40ea) | 3 | 500,000 | 524,288 | 4 | dflash / 7 |
| cfg-464d3499fbe9eba27869 | [MikeRoz/MiMo-V2.6-Flash-MOPD-4.03bpw-h8-exl3@29c8351a8b](https://huggingface.co/MikeRoz/MiMo-V2.6-Flash-MOPD-4.03bpw-h8-exl3/tree/29c8351a8b5854ec385adaeba7bbe62c790d40ea) | 3 | 32,768 | 131,072 | 8 | dflash / 7 |
| cfg-b80d4abe82b9667baf9c | [MikeRoz/MiMo-V2.6-Flash-MOPD-4.03bpw-h8-exl3@29c8351a8b](https://huggingface.co/MikeRoz/MiMo-V2.6-Flash-MOPD-4.03bpw-h8-exl3/tree/29c8351a8b5854ec385adaeba7bbe62c790d40ea) | 3 | 32,768 | 131,072 | 8 | dflash / 7 |

Card counts are saved configuration choices, not a claim that every allowed placement was measured. A derived view can differ from its pinned download source.

<details>
<summary>cfg-3a775a77bffe73e24773</summary>

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
  "draft_mode": "dflash",
  "draft_tokens": 7,
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
<summary>cfg-464d3499fbe9eba27869</summary>

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
  "draft_mode": "dflash",
  "draft_tokens": 7,
  "max_sessions": 8,
  "chunk_size": 512,
  "reserve_mib": 4096,
  "ram_kv_mib": 16384,
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
  "served_model_label": "mimo-v2.6-flash"
}
```

Pinned model revision recorded: yes. Source receipt labels, hashes and object locators are retained in [configurations.json](../configurations.json).

</details>

<details>
<summary>cfg-b80d4abe82b9667baf9c</summary>

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
  "draft_mode": "dflash",
  "draft_tokens": 7,
  "max_sessions": 8,
  "chunk_size": 512,
  "reserve_mib": 4096,
  "ram_kv_mib": 16384,
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
  "main_reserve_mib_values_unordered": []
}
```

Pinned model revision recorded: yes. Source receipt labels, hashes and object locators are retained in [configurations.json](../configurations.json).

</details>

## Retained Measurements

| Profile / Wave | Layout; Draft / Tokens | Requests | Input tokens/request | Accepted output tokens/request | Cache / Reused input tokens | Context / GPU pool tokens | Shared decode tok/s total | Client after-first-token estimate tok/s | Whole-wave output tok/s | Median TTFT, s | Source report |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [mimo-flash-dflash-validation](mimo-flash-dflash-validation.md)<br>wave-3afcbe268d4e306b0bc8 | layout unspecified; dflash / 7 | 1 | Not recorded | Not recorded | unspecified; reused - | 500,000 / 524,288 | 47.74 | Not recorded | Not recorded | Not recorded | Unspecified |
| [mimo-flash-dflash-validation](mimo-flash-dflash-validation.md)<br>wave-4b068fe9165ef92ef690 | layout unspecified; dflash / 7 | 1 | Not recorded | Not recorded | unspecified; reused - | 500,000 / 524,288 | 50.99 | Not recorded | Not recorded | Not recorded | Unspecified |
| [mimo-flash-dflash-validation](mimo-flash-dflash-validation.md)<br>wave-adedd2fd8d62b4bcebcf | layout unspecified; dflash / 7 | 4 | Not recorded | Not recorded | unspecified; reused - | 500,000 / 524,288 | 67.04 | Not recorded | Not recorded | Not recorded | Unspecified |

Rates are whole-wave totals over the stated request count. A wave may span multiple independent model instances; [measurements.json](../measurements.json) retains their contributions and the exact configuration IDs. Do not interpret a multi-instance total as one card's rate.

A dash in shared decode means no qualified synchronized interval is available. Whole-wave throughput includes prefill and queueing. A valid decode interval can survive inside an overall failed or partial check; the source-report outcome is preserved. No rows are averaged.

## Bounded Checks

| Check | Reported outcome | Retained counts / flags |
| --- | --- | --- |
| check-b012945e0029587dd56a | Failed / partial | {"passed":false,"ram_restoration_qualified":false} |

These checks retain their reported scope. A context/allocation/retrieval check is not a general quality score or a speed qualification at that context. Exact flags and provenance are in [checks.json](../checks.json).

## Additional Test Results

| Result / Source | Profile | Evidence type | Reported outcome | Retained values | Configuration binding |
| --- | --- | --- | --- | --- | --- |
| [result-1861cfa6957129bea839](../observations.json)<br>source-2f9c258247019894adda2278.json<br>`/single_warm` | [mimo-flash-dflash-validation](mimo-flash-dflash-validation.md) | test outcome | Outcome unspecified | generated_tokens=502 accepted tokens | Recorded configuration/job |
| [result-49de05268de59f13eea5](../observations.json)<br>source-ab89fca7e0f49696d5258b56.json<br>`/profiles/11/current_config` | [mimo-flash-dflash-validation](mimo-flash-dflash-validation.md) | context allocation | Outcome unspecified | cache_tokens=524,288 tokens; context=500,000 tokens; reserve_mib=4,096 MiB | Recorded configuration/job |
| [result-4d6d4392f0b289fbc21d](../observations.json)<br>source-8e1aa927bd11aeb4ea17c6c3.json<br>`/jobs/0` | [mimo-flash-dflash-validation](mimo-flash-dflash-validation.md) | test outcome | Failed / partial | passed=false | Recorded configuration/job |
| [result-54d3d39fd6eb6c798aef](../observations.json)<br>source-e5281cd0d7c34c1145ba98e5.json<br>`/original_job/tabby` | [mimo-flash-dflash-validation](mimo-flash-dflash-validation.md) | test outcome | Outcome unspecified | cache_tokens=131,072 tokens | Recorded configuration/job |
| [result-5d19ec3488b994c98db0](../observations.json)<br>source-3c01551729539f53c8004a3c.json<br>`/` | [mimo-flash-dflash-validation](mimo-flash-dflash-validation.md) | test outcome | Failed / partial | ram_restoration_qualified=false | Recorded configuration/job |
| [result-70bd71987d75e5066399](../observations.json)<br>source-3c01551729539f53c8004a3c.json<br>`/phases/3` | [mimo-flash-dflash-validation](mimo-flash-dflash-validation.md) | test outcome | Failed / partial | passed=false | Recorded configuration/job |
| [result-a9c7fb884116d7f22e8c](../observations.json)<br>source-2f9c258247019894adda2278.json<br>`/single_cold` | [mimo-flash-dflash-validation](mimo-flash-dflash-validation.md) | test outcome | Outcome unspecified | generated_tokens=500 accepted tokens | Recorded configuration/job |
| [result-b3291b1a3e6df4b85f2c](../observations.json)<br>source-57659989a2a99d4099dd1ced.json<br>`/original_job/tabby` | [mimo-flash-dflash-validation](mimo-flash-dflash-validation.md) | test outcome | Outcome unspecified | cache_tokens=524,288 tokens | Recorded configuration/job |
| [result-dfc4d273f2bd18cbd7e4](../observations.json)<br>source-2f9c258247019894adda2278.json<br>`/shared_decode_window` | [mimo-flash-dflash-validation](mimo-flash-dflash-validation.md) | test outcome | Outcome unspecified | generated_tokens=1,758 accepted tokens | Recorded configuration/job |

These are saved result records, including failures and bounded checks. Copies, individual requests, report summaries and regrading can overlap; their counts are not independent test repetitions. Open each result for exact values, units, configuration binding and source receipts.

There are 2 retained lifecycle records. Their states, exit codes and configuration IDs remain in [catalog.json](../catalog.json); they do not supply missing benchmark results.

[Full archive](../../README.md) | [All retained waves](../RESULTS.md) | [Data definitions](../DATA.md) | [Recommended recipes](../../../README.md)
