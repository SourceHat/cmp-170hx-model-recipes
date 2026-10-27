# glm53-final-dflash3-output4096-786432

**Historical record. Decode interval measured.**

Model family: GLM 5.3 Flash.

Recorded archive reason: Historical capacity, fit or control configuration; later DFlash2 and MTP variants have separate records.

Historical configurations are provided for comparison. The [recommended recipes](../../../README.md) include supported launch scripts.

Current recipes using the same recorded checkpoint repository: [glm-5.3-flash-mtp1-tp3](../../../recipes/glm-5.3-flash-mtp1-tp3/README.md). Context, cache and runtime versions can differ.

## Saved Configuration Versions

Each configuration ID identifies a distinct original settings record. Deployment fields are omitted; versions can have identical published settings after that omission. Upstream runtime commits remain unspecified where the source retained only an integration label.

| Configuration | Recorded artifact / source | Configured card counts | Context tokens | GPU pool tokens | Slots | Draft mode / tokens |
| --- | --- | --- | --- | --- | --- | --- |
| cfg-18f9aeb953369dbdba00 | [turboderp/GLM-5.3-Flash-exl3@2a30229e67](https://huggingface.co/turboderp/GLM-5.3-Flash-exl3/tree/2a30229e67012798ba9f0cd832bb78abf4c363d5) | 3 | 500,000 | 786,432 | 4 | dflash2 / 3 |

Card counts are saved configuration choices, not a claim that every allowed placement was measured. A derived view can differ from its pinned download source.

<details>
<summary>cfg-18f9aeb953369dbdba00</summary>

```json
{
  "kind": "tabby",
  "gpu_counts": [
    3
  ],
  "context": 500000,
  "cache_tokens": 786432,
  "cache_mode": "Q8",
  "draft_cache_mode": "Q8",
  "draft_mode": "dflash2",
  "draft_tokens": 3,
  "max_sessions": 4,
  "chunk_size": 256,
  "reserve_mib": 1024,
  "ram_kv_mib": 32768,
  "ram_recurrent_mib": 16384,
  "dynamic_draft": false,
  "output_chunk_tokens": 4096,
  "power_watts": 200,
  "host_memory_gib": 80,
  "host_swap_gib": 0,
  "min_vram_mib_per_gpu": 65530,
  "min_effective_vram_mib": 196000,
  "model_repository": "turboderp/GLM-5.3-Flash-exl3",
  "model_revision": "2a30229e67012798ba9f0cd832bb78abf4c363d5",
  "draft_repository": null,
  "draft_revision": null,
  "recorded_runtime_label": null,
  "served_model_label": "glm-5.3-flash",
  "main_reserve_mib_values_unordered": [
    1024,
    1536,
    2560
  ],
  "draft_split_mib_values_unordered": [
    3328,
    4864,
    5120
  ]
}
```

Pinned model revision recorded: yes. Source receipt labels, hashes and object locators are retained in [configurations.json](../configurations.json).

</details>

## Retained Measurements

| Profile / Wave | Layout; Draft / Tokens | Requests | Input tokens/request | Accepted output tokens/request | Cache / Reused input tokens | Context / GPU pool tokens | Shared decode tok/s total | Client after-first-token estimate tok/s | Whole-wave output tok/s | Median TTFT, s | Source report |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [glm53-final-dflash3-output4096-786432](glm53-final-dflash3-output4096-786432.md)<br>wave-08a5e17c97bdb617423c | layout unspecified; dflash2 / 3 | 2 | 8,207 | 1,024 | cold; reused 0 | 500,000 / 786,432 | 63.34 | Not recorded | 34.19 | 27.48 | Pass |
| [glm53-final-dflash3-output4096-786432](glm53-final-dflash3-output4096-786432.md)<br>wave-86b4d926f65c30cced40 | layout unspecified; dflash2 / 3 | 2 | 9,212 to 9,224 | 1,024 | cached_prefix; reused 8,192 | 500,000 / 786,432 | 60.08 | Not recorded | 50.76 | 5.27 | Pass |
| [glm53-final-dflash3-output4096-786432](glm53-final-dflash3-output4096-786432.md)<br>wave-898f775b846b99bf7961 | layout unspecified; dflash2 / 3 | 2 | 8,760 | 512 | cached_prefix; reused 8,192 | 500,000 / 786,432 | 61.31 | Not recorded | 51.40 | 3.45 | Pass |
| [glm53-final-dflash3-output4096-786432](glm53-final-dflash3-output4096-786432.md)<br>wave-9434a0f559d09834dd2f | layout unspecified; dflash2 / 3 | 2 | 8,252 | 512 | cold; reused 0 | 500,000 / 786,432 | 71.78 | Not recorded | 25.05 | 26.19 | Pass |

Rates are whole-wave totals over the stated request count. A wave may span multiple independent model instances; [measurements.json](../measurements.json) retains their contributions and the exact configuration IDs. Do not interpret a multi-instance total as one card's rate.

A dash in shared decode means no qualified synchronized interval is available. Whole-wave throughput includes prefill and queueing. A valid decode interval can survive inside an overall failed or partial check; the source-report outcome is preserved. No rows are averaged.

## Bounded Checks

| Check | Reported outcome | Retained counts / flags |
| --- | --- | --- |
| check-24f6fd2949a1e0f3b9e8 | Pass | {"passed":true} |

These checks retain their reported scope. A context/allocation/retrieval check is not a general quality score or a speed qualification at that context. Exact flags and provenance are in [checks.json](../checks.json).

## Additional Test Results

| Result / Source | Profile | Evidence type | Reported outcome | Retained values | Configuration binding |
| --- | --- | --- | --- | --- | --- |
| [result-39eda81e3f8eea74cb1d](../observations.json)<br>source-e2862bf3adb6b7570f68a730.json<br>`/cold/replicas/0/rates` | [glm53-final-dflash3-output4096-786432](glm53-final-dflash3-output4096-786432.md) | test outcome | Outcome unspecified | end_to_end_output_tps=34.19 accepted tokens/s; generated_tokens=2,048 accepted tokens; wall_seconds=59.90 s | Recorded configuration/job |
| [result-3f7e3958971f51689a2f](../observations.json)<br>source-80ab20c3256723e3e160b0c0.json<br>`/generated_decode1024/cold` | [glm53-final-dflash3-output4096-786432](glm53-final-dflash3-output4096-786432.md) | test outcome | Outcome unspecified | generated_tokens=1,959 accepted tokens | Recorded configuration/job |
| [result-7db3e53968ce755baaac](../observations.json)<br>source-80ab20c3256723e3e160b0c0.json<br>`/matched_short512/warm` | [glm53-final-dflash3-output4096-786432](glm53-final-dflash3-output4096-786432.md) | test outcome | Outcome unspecified | generated_tokens=988 accepted tokens | Recorded configuration/job |
| [result-925e55fd6be3be86b104](../observations.json)<br>source-80ab20c3256723e3e160b0c0.json<br>`/matched_short512/cold` | [glm53-final-dflash3-output4096-786432](glm53-final-dflash3-output4096-786432.md) | test outcome | Outcome unspecified | generated_tokens=1,003 accepted tokens | Recorded configuration/job |
| [result-ad4763d698e980906089](../observations.json)<br>source-d39977b8dd38ce6e6a651867.json<br>`/warm/replicas/0/rates` | [glm53-final-dflash3-output4096-786432](glm53-final-dflash3-output4096-786432.md) | test outcome | Outcome unspecified | end_to_end_output_tps=51.40 accepted tokens/s; generated_tokens=1,024 accepted tokens; wall_seconds=19.92 s | Recorded configuration/job |
| [result-c099be1551de76b49035](../observations.json)<br>source-fecf336c3e4024a12f78902d.json<br>`/totals` | [glm53-final-dflash3-output4096-786432](glm53-final-dflash3-output4096-786432.md) | context allocation | Outcome unspecified | cached_tokens=0 tokens; generated_tokens=0 accepted tokens; prompt_tokens=0 tokens; recurrent_restores=0 checkpoints | Recorded configuration/job |
| [result-c1e0162c9b04f29261d6](../observations.json)<br>source-fecf336c3e4024a12f78902d.json<br>`/` | [glm53-final-dflash3-output4096-786432](glm53-final-dflash3-output4096-786432.md) | test outcome | Outcome unspecified | context=500,000 tokens | Recorded configuration/job |
| [result-d056e714cbc9130ad1ff](../observations.json)<br>source-d39977b8dd38ce6e6a651867.json<br>`/cold/replicas/0/rates` | [glm53-final-dflash3-output4096-786432](glm53-final-dflash3-output4096-786432.md) | test outcome | Outcome unspecified | end_to_end_output_tps=25.05 accepted tokens/s; generated_tokens=1,024 accepted tokens; wall_seconds=40.88 s | Recorded configuration/job |
| [result-d1c7c62e979c17877a59](../observations.json)<br>source-7f5d4e42eff9abb95cd262fb.json<br>`/tabby` | [glm53-final-dflash3-output4096-786432](glm53-final-dflash3-output4096-786432.md) | test outcome | Outcome unspecified | cache_tokens=786,432 tokens | Recorded configuration/job |
| [result-d26fc4370e5c525ea302](../observations.json)<br>source-80ab20c3256723e3e160b0c0.json<br>`/generated_decode1024/warm` | [glm53-final-dflash3-output4096-786432](glm53-final-dflash3-output4096-786432.md) | test outcome | Outcome unspecified | generated_tokens=2,008 accepted tokens | Recorded configuration/job |
| [result-e1ce5a5a244dd4e10bc0](../observations.json)<br>source-fecf336c3e4024a12f78902d.json<br>`/cache` | [glm53-final-dflash3-output4096-786432](glm53-final-dflash3-output4096-786432.md) | test outcome | Outcome unspecified | cached_tokens=0 tokens | Recorded configuration/job |
| [result-f9e0cd7b86c0ba315b90](../observations.json)<br>source-e2862bf3adb6b7570f68a730.json<br>`/warm/replicas/0/rates` | [glm53-final-dflash3-output4096-786432](glm53-final-dflash3-output4096-786432.md) | test outcome | Outcome unspecified | end_to_end_output_tps=50.76 accepted tokens/s; generated_tokens=2,048 accepted tokens; wall_seconds=40.35 s | Recorded configuration/job |

These are saved result records, including failures and bounded checks. Copies, individual requests, report summaries and regrading can overlap; their counts are not independent test repetitions. Open each result for exact values, units, configuration binding and source receipts.

There are 1 retained lifecycle records. Their states, exit codes and configuration IDs remain in [catalog.json](../catalog.json); they do not supply missing benchmark results.

[Full archive](../../README.md) | [All retained waves](../RESULTS.md) | [Data definitions](../DATA.md) | [Recommended recipes](../../../README.md)
