# glm53-capacity3

**Historical record. Decode interval measured.**

Model family: GLM 5.3 Flash.

Recorded archive reason: Historical capacity, fit or control configuration; later DFlash2 and MTP variants have separate records.

Historical configurations are provided for comparison. The [recommended recipes](../../../README.md) include supported launch scripts.

Current recipes using the same recorded checkpoint repository: [glm-5.3-flash-mtp1-tp3](../../../recipes/glm-5.3-flash-mtp1-tp3/README.md). Context, cache and runtime versions can differ.

## Saved Configuration Versions

Each configuration ID identifies a distinct original settings record. Deployment fields are omitted; versions can have identical published settings after that omission. Upstream runtime commits remain unspecified where the source retained only an integration label.

| Configuration | Recorded artifact / source | Configured card counts | Context tokens | GPU pool tokens | Slots | Draft mode / tokens |
| --- | --- | --- | --- | --- | --- | --- |
| cfg-1e6294be97b4e48f7f63 | [turboderp/GLM-5.3-Flash-exl3@2a30229e67](https://huggingface.co/turboderp/GLM-5.3-Flash-exl3/tree/2a30229e67012798ba9f0cd832bb78abf4c363d5) | 3 | 500,000 | 1,048,576 | 8 | mtp / 1 |
| cfg-aa31505049c6e22c000c | [turboderp/GLM-5.3-Flash-exl3@2a30229e67](https://huggingface.co/turboderp/GLM-5.3-Flash-exl3/tree/2a30229e67012798ba9f0cd832bb78abf4c363d5) | 3 | 500,000 | 786,432 | 8 | mtp / 1 |
| cfg-ad698e9fdcdee13be9b8 | [turboderp/GLM-5.3-Flash-exl3@2a30229e67](https://huggingface.co/turboderp/GLM-5.3-Flash-exl3/tree/2a30229e67012798ba9f0cd832bb78abf4c363d5) | 3 | 500,000 | 786,432 | 8 | mtp / 1 |
| cfg-d85a795353166594db04 | [turboderp/GLM-5.3-Flash-exl3@2a30229e67](https://huggingface.co/turboderp/GLM-5.3-Flash-exl3/tree/2a30229e67012798ba9f0cd832bb78abf4c363d5) | 3 | 500,000 | 1,572,864 | 8 | mtp / 1 |
| cfg-d9df57babf83573f3a44 | [turboderp/GLM-5.3-Flash-exl3@2a30229e67](https://huggingface.co/turboderp/GLM-5.3-Flash-exl3/tree/2a30229e67012798ba9f0cd832bb78abf4c363d5) | 3 | 500,000 | 1,048,576 | 8 | mtp / 1 |
| cfg-efecbd151dbf36e5304b | [turboderp/GLM-5.3-Flash-exl3@2a30229e67](https://huggingface.co/turboderp/GLM-5.3-Flash-exl3/tree/2a30229e67012798ba9f0cd832bb78abf4c363d5) | 3 | 500,000 | 1,310,720 | 8 | mtp / 1 |

Card counts are saved configuration choices, not a claim that every allowed placement was measured. A derived view can differ from its pinned download source.

<details>
<summary>cfg-1e6294be97b4e48f7f63</summary>

```json
{
  "kind": "tabby",
  "gpu_counts": [
    3
  ],
  "context": 500000,
  "cache_tokens": 1048576,
  "cache_mode": "Q8",
  "draft_cache_mode": "Q8",
  "draft_mode": "mtp",
  "draft_tokens": 1,
  "max_sessions": 8,
  "chunk_size": 512,
  "reserve_mib": 4096,
  "ram_kv_mib": 32768,
  "ram_recurrent_mib": 16384,
  "dynamic_draft": false,
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
  "served_model_label": "glm-5.3-flash"
}
```

Pinned model revision recorded: yes. Source receipt labels, hashes and object locators are retained in [configurations.json](../configurations.json).

</details>

<details>
<summary>cfg-aa31505049c6e22c000c</summary>

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
  "draft_mode": "mtp",
  "draft_tokens": 1,
  "max_sessions": 8,
  "chunk_size": 512,
  "reserve_mib": 3072,
  "ram_kv_mib": 32768,
  "ram_recurrent_mib": 16384,
  "dynamic_draft": false,
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
    4096,
    4096
  ]
}
```

Pinned model revision recorded: yes. Source receipt labels, hashes and object locators are retained in [configurations.json](../configurations.json).

</details>

<details>
<summary>cfg-ad698e9fdcdee13be9b8</summary>

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
  "draft_mode": "mtp",
  "draft_tokens": 1,
  "max_sessions": 8,
  "chunk_size": 512,
  "reserve_mib": 4096,
  "ram_kv_mib": 32768,
  "ram_recurrent_mib": 16384,
  "dynamic_draft": false,
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
  "served_model_label": "glm-5.3-flash"
}
```

Pinned model revision recorded: yes. Source receipt labels, hashes and object locators are retained in [configurations.json](../configurations.json).

</details>

<details>
<summary>cfg-d85a795353166594db04</summary>

```json
{
  "kind": "tabby",
  "gpu_counts": [
    3
  ],
  "context": 500000,
  "cache_tokens": 1572864,
  "cache_mode": "Q8",
  "draft_cache_mode": "Q8",
  "draft_mode": "mtp",
  "draft_tokens": 1,
  "max_sessions": 8,
  "chunk_size": 2048,
  "reserve_mib": 4096,
  "ram_kv_mib": 32768,
  "ram_recurrent_mib": 16384,
  "dynamic_draft": false,
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
  "served_model_label": "glm-5.3-flash"
}
```

Pinned model revision recorded: yes. Source receipt labels, hashes and object locators are retained in [configurations.json](../configurations.json).

</details>

<details>
<summary>cfg-d9df57babf83573f3a44</summary>

```json
{
  "kind": "tabby",
  "gpu_counts": [
    3
  ],
  "context": 500000,
  "cache_tokens": 1048576,
  "cache_mode": "Q8",
  "draft_cache_mode": "Q8",
  "draft_mode": "mtp",
  "draft_tokens": 1,
  "max_sessions": 8,
  "chunk_size": 1024,
  "reserve_mib": 4096,
  "ram_kv_mib": 32768,
  "ram_recurrent_mib": 16384,
  "dynamic_draft": false,
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
  "served_model_label": "glm-5.3-flash"
}
```

Pinned model revision recorded: yes. Source receipt labels, hashes and object locators are retained in [configurations.json](../configurations.json).

</details>

<details>
<summary>cfg-efecbd151dbf36e5304b</summary>

```json
{
  "kind": "tabby",
  "gpu_counts": [
    3
  ],
  "context": 500000,
  "cache_tokens": 1310720,
  "cache_mode": "Q8",
  "draft_cache_mode": "Q8",
  "draft_mode": "mtp",
  "draft_tokens": 1,
  "max_sessions": 8,
  "chunk_size": 1024,
  "reserve_mib": 4096,
  "ram_kv_mib": 32768,
  "ram_recurrent_mib": 16384,
  "dynamic_draft": false,
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
  "served_model_label": "glm-5.3-flash"
}
```

Pinned model revision recorded: yes. Source receipt labels, hashes and object locators are retained in [configurations.json](../configurations.json).

</details>

## Retained Measurements

| Profile / Wave | Layout; Draft / Tokens | Requests | Input tokens/request | Accepted output tokens/request | Cache / Reused input tokens | Context / GPU pool tokens | Shared decode tok/s total | Client after-first-token estimate tok/s | Whole-wave output tok/s | Median TTFT, s | Source report |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [glm53-capacity3](glm53-capacity3.md)<br>wave-280ddd1a632f96cd6e35 | layout unspecified; mtp / 1 | 4 | 499,523 | 39 to 65 | cold; reused 449,792 | 500,000 / 786,432 | Not recorded | Not recorded | 0.77 | 172.56 | Pass |
| [glm53-capacity3](glm53-capacity3.md)<br>wave-3bb31896fbfbb9e374a9 | layout unspecified; mtp / 1 | 4 | 32,878 to 32,920 | 19 | cached_prefix; reused 32,768 | 500,000 / 786,432 | Not recorded | Not recorded | 23.52 | 2.62 | Pass |
| [glm53-capacity3](glm53-capacity3.md)<br>wave-414e06ba4d4cd54c96a9 | layout unspecified; mtp / 1 | 4 | 131,099 | 122 to 240 | cold; reused 32,768 | 500,000 / 786,432 | Not recorded | Not recorded | 1.63 | 438.14 | Pass |
| [glm53-capacity3](glm53-capacity3.md)<br>wave-64e86ec0cdeefe3d5f6e | layout unspecified; mtp / 1 | 4 | 32,801 | 68 to 110 | cold; reused 0 | 500,000 / 786,432 | Not recorded | Not recorded | 2.28 | 149.54 | Pass |
| [glm53-capacity3](glm53-capacity3.md)<br>wave-91de911fc03cae0d1643 | layout unspecified; mtp / 1 | 4 | 131,191 to 131,241 | 19 | cached_prefix; reused 131,072 | 500,000 / 786,432 | Not recorded | Not recorded | 17.84 | 3.12 | Pass |
| [glm53-capacity3](glm53-capacity3.md)<br>wave-9a41c55f4e3a8766b05e | layout unspecified; mtp / 1 | 4 | 499,571 to 499,597 | 19 | cached_prefix; reused 499,456 | 500,000 / 786,432 | Not recorded | Not recorded | 5.20 | 10.42 | Pass |
| [glm53-capacity3](glm53-capacity3.md)<br>wave-a4b57b4cb914cea57957 | layout unspecified; mtp / 1 | 8 | 2,607 to 8,765 | 512 | cached_prefix; reused 2,048 to 8,192 | 500,000 / 786,432 | 62.87 | Not recorded | 54.19 | 10.48 | Pass |
| [glm53-capacity3](glm53-capacity3.md)<br>wave-c207134b07d43c40ac5f | layout unspecified; mtp / 1 | 4 | 450,041 | 39 to 64 | cold; reused 399,872 | 500,000 / 786,432 | Not recorded | Not recorded | 0.67 | 170.28 | Pass |
| [glm53-capacity3](glm53-capacity3.md)<br>wave-c934999055ed911efcc6 | layout unspecified; mtp / 1 | 8 | 2,098 to 8,254 | 512 | cold; reused 0 | 500,000 / 786,432 | 67.34 | Not recorded | 38.72 | 39.15 | Pass |
| [glm53-capacity3](glm53-capacity3.md)<br>wave-d25d5b469d4dd6d9b4cc | layout unspecified; mtp / 1 | 4 | 450,089 to 450,114 | 19 | cached_prefix; reused 449,792 | 500,000 / 786,432 | Not recorded | Not recorded | 5.10 | 10.35 | Pass |
| [glm53-capacity3](glm53-capacity3.md)<br>wave-e2f4bb8295ad040dadbb | layout unspecified; mtp / 1 | 4 | 400,037 | 39 to 65 | cold; reused 131,072 | 500,000 / 786,432 | Not recorded | Not recorded | 0.16 | 821.94 | Pass |
| [glm53-capacity3](glm53-capacity3.md)<br>wave-ef53e51017e4f8c18799 | layout unspecified; mtp / 1 | 4 | 400,085 to 400,111 | 19 | cached_prefix; reused 399,872 | 500,000 / 786,432 | Not recorded | Not recorded | 6.05 | 8.43 | Pass |

Rates are whole-wave totals over the stated request count. A wave may span multiple independent model instances; [measurements.json](../measurements.json) retains their contributions and the exact configuration IDs. Do not interpret a multi-instance total as one card's rate.

A dash in shared decode means no qualified synchronized interval is available. Whole-wave throughput includes prefill and queueing. A valid decode interval can survive inside an overall failed or partial check; the source-report outcome is preserved. No rows are averaged.

## Bounded Checks

| Check | Reported outcome | Retained counts / flags |
| --- | --- | --- |
| check-28f1ff3ec46e283a6401 | Pass | {"passed":true,"replayed_history_tokens":[33,33,33,33]} |
| check-49c8fbc4e9331bdf4f1e | Pass | {"passed":true,"input_tokens":[450039,450039,450039,450039],"replayed_history_tokens":[249,249,249,249],"extension_cached_tokens":[399872,399872,399872,399872]} |
| check-6adf3b987c5c260783a3 | Pass | {"passed":true} |
| check-9e404975877feeac9f4e | Pass | {"passed":true,"input_tokens":[499521,499521,499521,499521],"replayed_history_tokens":[67,67,67,67],"extension_cached_tokens":[449792,449792,449792,449792]} |
| check-9fa6f8a8b6b072bd0f6b | Pass | {"passed":true,"input_tokens":[400035,400035,400035,400035],"replayed_history_tokens":[165,165,165,165],"extension_cached_tokens":[131072,131072,131072,131072]} |
| check-bb6698b9c11c666e1fd8 | Pass | {"passed":true,"recurrent_restores":24,"restored_pages":15344} |
| check-c23ea1c1baf5476038b9 | Pass | {"passed":true,"replayed_history_tokens":[249,249,249,249]} |
| check-c8610d1e1762906ca7a9 | Pass | {"passed":true,"replayed_history_tokens":[33,33,33,33],"input_tokens":[32799,32799,32799,32799]} |
| check-d15b9162b70b66e757f6 | Pass | {"passed":true,"replayed_history_tokens":[67,67,67,67]} |
| check-dcad2db837fa9b240303 | Pass | {"passed":true,"input_tokens":[131097,131097,131097,131097],"replayed_history_tokens":[27,27,27,27],"extension_cached_tokens":[32768,32768,32768,32768]} |
| check-dcb3430213d238e5294e | Pass | {"passed":true,"replayed_history_tokens":[165,165,165,165]} |
| check-f57774c100afcd5baf4b | Pass | {"passed":true} |
| check-fe9d69d9379f59f6b85c | Pass | {"passed":true,"replayed_history_tokens":[27,27,27,27]} |

These checks retain their reported scope. A context/allocation/retrieval check is not a general quality score or a speed qualification at that context. Exact flags and provenance are in [checks.json](../checks.json).

## Additional Test Results

| Result / Source | Profile | Evidence type | Reported outcome | Retained values | Configuration binding |
| --- | --- | --- | --- | --- | --- |
| [result-02eeed6d1cb805fe88d3](../observations.json)<br>source-d387b69ade5dabb2cb6821e5.json<br>`/stages/2` | [glm53-capacity3](glm53-capacity3.md) | test outcome | Outcome unspecified | recurrent_restores_on_return=4 checkpoints; restored_page_images_on_return=5,267 pages; return_wave_seconds=12.56 s | Recorded configuration/job |
| [result-075c2a42840f28869837](../observations.json)<br>source-781f444772539bdc0224e270.json<br>`/stages/1/warm` | [glm53-capacity3](glm53-capacity3.md) | test outcome | Outcome unspecified | end_to_end_output_tps=17.84 accepted tokens/s; generated_tokens=76 accepted tokens; wall_seconds=4.26 s | Recorded configuration/job |
| [result-0c63b0ebbea9df347e3c](../observations.json)<br>source-781f444772539bdc0224e270.json<br>`/stages/3` | [glm53-capacity3](glm53-capacity3.md) | test outcome | Pass | replayed_history_tokens=249 tokens | Recorded configuration/job |
| [result-10273959ed2e53155653](../observations.json)<br>source-781f444772539bdc0224e270.json<br>`/stages/1` | [glm53-capacity3](glm53-capacity3.md) | test outcome | Pass | replayed_history_tokens=27 tokens | Recorded configuration/job |
| [result-162f6cc01c990d7554e7](../observations.json)<br>source-5a35c523994e864ed1e2e05a.json<br>`/after_burst/cache` | [glm53-capacity3](glm53-capacity3.md) | test outcome | Outcome unspecified | cached_tokens=655,616 tokens | Recorded configuration/job |
| [result-1b5de3dfb647996ba3df](../observations.json)<br>source-7ea9c5a7a51254b66dc04f78.json<br>`/after_burst` | [glm53-capacity3](glm53-capacity3.md) | test outcome | Outcome unspecified | context=500,000 tokens | Recorded configuration/job |
| [result-2abb2f905324baaafa62](../observations.json)<br>source-7ea9c5a7a51254b66dc04f78.json<br>`/after_cold/totals` | [glm53-capacity3](glm53-capacity3.md) | context allocation | Outcome unspecified | cached_tokens=0 tokens; generated_tokens=450 accepted tokens; prompt_tokens=131,838 tokens; recurrent_restores=0 checkpoints | Recorded configuration/job |
| [result-2b9fc506082fcadd0d85](../observations.json)<br>source-267ae14256a622a087b4bd24.json<br>`/after_cold` | [glm53-capacity3](glm53-capacity3.md) | test outcome | Outcome unspecified | context=500,000 tokens | Recorded configuration/job |
| [result-2ba8072940a847b4c2da](../observations.json)<br>source-781f444772539bdc0224e270.json<br>`/stages/3/warm` | [glm53-capacity3](glm53-capacity3.md) | test outcome | Outcome unspecified | end_to_end_output_tps=5.10 accepted tokens/s; generated_tokens=76 accepted tokens; wall_seconds=14.91 s | Recorded configuration/job |
| [result-2f02571936e8221d6a26](../observations.json)<br>source-781f444772539bdc0224e270.json<br>`/stages/0/warm` | [glm53-capacity3](glm53-capacity3.md) | test outcome | Outcome unspecified | end_to_end_output_tps=23.52 accepted tokens/s; generated_tokens=76 accepted tokens; wall_seconds=3.23 s | Recorded configuration/job |
| [result-36537cac8343aadfe6a3](../observations.json)<br>source-cde4ecf31dafce3484cc531c.json<br>`/returning` | [glm53-capacity3](glm53-capacity3.md) | test outcome | Outcome unspecified | generated_tps=62.87 accepted tokens/s | Recorded configuration/job |
| [result-3adfb2a67150c567147e](../observations.json)<br>source-765eaac5eb5d951009e19e74.json<br>`/after_cold/totals` | [glm53-capacity3](glm53-capacity3.md) | context allocation | Outcome unspecified | cached_tokens=8,501,248 tokens; generated_tokens=4,138 accepted tokens; prompt_tokens=10,638,806 tokens; recurrent_restores=80 checkpoints | Recorded configuration/job |
| [result-441dce3b47151b62e136](../observations.json)<br>source-3e12c1c06c62e444e0e37774.json<br>`/after_cold/totals` | [glm53-capacity3](glm53-capacity3.md) | context allocation | Outcome unspecified | cached_tokens=1,441,792 tokens; generated_tokens=2,568 accepted tokens; prompt_tokens=3,176,321 tokens; recurrent_restores=32 checkpoints | Recorded configuration/job |
| [result-4834e509dd6c27cf151d](../observations.json)<br>source-3e12c1c06c62e444e0e37774.json<br>`/after_burst/totals` | [glm53-capacity3](glm53-capacity3.md) | context allocation | Outcome unspecified | cached_tokens=1,572,864 tokens; generated_tokens=3,080 accepted tokens; prompt_tokens=3,308,049 tokens; recurrent_restores=48 checkpoints | Recorded configuration/job |
| [result-4a61e2d493db83187731](../observations.json)<br>source-3e12c1c06c62e444e0e37774.json<br>`/after_burst` | [glm53-capacity3](glm53-capacity3.md) | test outcome | Outcome unspecified | context=500,000 tokens | Recorded configuration/job |
| [result-51900ecb0e3b56e8b760](../observations.json)<br>source-cde4ecf31dafce3484cc531c.json<br>`/idle_stats` | [glm53-capacity3](glm53-capacity3.md) | test outcome | Outcome unspecified | context=500,000 tokens | Recorded configuration/job |
| [result-5aca9b097e5d6703ccc8](../observations.json)<br>source-d387b69ade5dabb2cb6821e5.json<br>`/stages/0` | [glm53-capacity3](glm53-capacity3.md) | test outcome | Outcome unspecified | recurrent_restores_on_return=4 checkpoints; restored_page_images_on_return=0 pages; return_wave_seconds=3.23 s | Recorded configuration/job |
| [result-5f4de08d1cf3ac5ba15d](../observations.json)<br>source-781f444772539bdc0224e270.json<br>`/stages/2/warm` | [glm53-capacity3](glm53-capacity3.md) | test outcome | Outcome unspecified | end_to_end_output_tps=6.05 accepted tokens/s; generated_tokens=76 accepted tokens; wall_seconds=12.56 s | Recorded configuration/job |
| [result-600cfbb37c4f1566eebf](../observations.json)<br>source-267ae14256a622a087b4bd24.json<br>`/after_cold/cache` | [glm53-capacity3](glm53-capacity3.md) | test outcome | Outcome unspecified | cached_tokens=786,176 tokens | Recorded configuration/job |
| [result-631b69f00d8ffc787e3c](../observations.json)<br>source-765eaac5eb5d951009e19e74.json<br>`/after_burst/cache` | [glm53-capacity3](glm53-capacity3.md) | test outcome | Outcome unspecified | cached_tokens=782,080 tokens | Recorded configuration/job |
| [result-6e012996e58f2e838ca9](../observations.json)<br>source-5a35c523994e864ed1e2e05a.json<br>`/after_burst/totals` | [glm53-capacity3](glm53-capacity3.md) | context allocation | Outcome unspecified | cached_tokens=393,216 tokens; generated_tokens=2,284 accepted tokens; prompt_tokens=1,051,283 tokens; recurrent_restores=24 checkpoints | Recorded configuration/job |
| [result-6fe14bda9438c87d5b3a](../observations.json)<br>source-267ae14256a622a087b4bd24.json<br>`/after_burst` | [glm53-capacity3](glm53-capacity3.md) | test outcome | Outcome unspecified | context=500,000 tokens | Recorded configuration/job |
| [result-73a533b027657697f2d8](../observations.json)<br>source-7ea9c5a7a51254b66dc04f78.json<br>`/after_burst/totals` | [glm53-capacity3](glm53-capacity3.md) | context allocation | Outcome unspecified | cached_tokens=0 tokens; generated_tokens=962 accepted tokens; prompt_tokens=263,566 tokens; recurrent_restores=0 checkpoints | Recorded configuration/job |
| [result-7dd1978740d55fd1d98d](../observations.json)<br>source-765eaac5eb5d951009e19e74.json<br>`/after_burst/totals` | [glm53-capacity3](glm53-capacity3.md) | context allocation | Outcome unspecified | cached_tokens=8,632,320 tokens; generated_tokens=4,650 accepted tokens; prompt_tokens=10,770,534 tokens; recurrent_restores=96 checkpoints | Recorded configuration/job |
| [result-7e793834808d4cfce306](../observations.json)<br>source-cde4ecf31dafce3484cc531c.json<br>`/cold` | [glm53-capacity3](glm53-capacity3.md) | test outcome | Outcome unspecified | generated_tps=67.34 accepted tokens/s | Recorded configuration/job |
| [result-92dd045cef53107b0c36](../observations.json)<br>source-d387b69ade5dabb2cb6821e5.json<br>`/retention` | [glm53-capacity3](glm53-capacity3.md) | test outcome | Outcome unspecified | draft_page_bytes=286,720 bytes; main_page_bytes=3,153,920 bytes; paired_page_image_bytes=3,440,640 bytes; ram_cache_tokens=2,556,416 tokens | Recorded configuration/job |
| [result-979e4cd898d0da07202c](../observations.json)<br>source-781f444772539bdc0224e270.json<br>`/stages/2/cold` | [glm53-capacity3](glm53-capacity3.md) | test outcome | Outcome unspecified | end_to_end_output_tps=0.16 accepted tokens/s; generated_tokens=208 accepted tokens; wall_seconds=1,316.90 s | Recorded configuration/job |
| [result-9e9a3d7dddf1af480943](../observations.json)<br>source-765eaac5eb5d951009e19e74.json<br>`/after_cold` | [glm53-capacity3](glm53-capacity3.md) | test outcome | Outcome unspecified | context=500,000 tokens | Recorded configuration/job |
| [result-a2d1bff4d2d8dd0c35ba](../observations.json)<br>source-5a35c523994e864ed1e2e05a.json<br>`/after_burst` | [glm53-capacity3](glm53-capacity3.md) | test outcome | Outcome unspecified | context=500,000 tokens | Recorded configuration/job |
| [result-a71eef8b862c3f066301](../observations.json)<br>source-d387b69ade5dabb2cb6821e5.json<br>`/stages/1` | [glm53-capacity3](glm53-capacity3.md) | test outcome | Outcome unspecified | recurrent_restores_on_return=4 checkpoints; restored_page_images_on_return=0 pages; return_wave_seconds=4.26 s | Recorded configuration/job |
| [result-abb28b90e14624d17140](../observations.json)<br>source-267ae14256a622a087b4bd24.json<br>`/after_cold/totals` | [glm53-capacity3](glm53-capacity3.md) | context allocation | Outcome unspecified | cached_tokens=4,771,840 tokens; generated_tokens=3,337 accepted tokens; prompt_tokens=6,708,605 tokens; recurrent_restores=56 checkpoints | Recorded configuration/job |
| [result-af5b5666c94db8a8384a](../observations.json)<br>source-cde4ecf31dafce3484cc531c.json<br>`/idle_stats/cache` | [glm53-capacity3](glm53-capacity3.md) | test outcome | Outcome unspecified | cached_tokens=782,080 tokens | Recorded configuration/job |
| [result-b2c4e5d76e2b38a457eb](../observations.json)<br>source-d387b69ade5dabb2cb6821e5.json<br>`/stages/4` | [glm53-capacity3](glm53-capacity3.md) | test outcome | Outcome unspecified | recurrent_restores_on_return=4 checkpoints; restored_page_images_on_return=7,804 pages; return_wave_seconds=14.61 s | Recorded configuration/job |
| [result-b44d2022e69aa5e85cbe](../observations.json)<br>source-7ea9c5a7a51254b66dc04f78.json<br>`/after_cold/cache` | [glm53-capacity3](glm53-capacity3.md) | test outcome | Outcome unspecified | cached_tokens=131,072 tokens | Recorded configuration/job |
| [result-bb12fa4ffe84164b7346](../observations.json)<br>source-781f444772539bdc0224e270.json<br>`/stages/4/warm` | [glm53-capacity3](glm53-capacity3.md) | test outcome | Outcome unspecified | end_to_end_output_tps=5.20 accepted tokens/s; generated_tokens=76 accepted tokens; wall_seconds=14.61 s | Recorded configuration/job |
| [result-bebe74b0a1056370b89d](../observations.json)<br>source-765eaac5eb5d951009e19e74.json<br>`/after_cold/cache` | [glm53-capacity3](glm53-capacity3.md) | test outcome | Outcome unspecified | cached_tokens=786,176 tokens | Recorded configuration/job |
| [result-c15f59a7550643e8de6a](../observations.json)<br>source-7ea9c5a7a51254b66dc04f78.json<br>`/after_cold` | [glm53-capacity3](glm53-capacity3.md) | test outcome | Outcome unspecified | context=500,000 tokens | Recorded configuration/job |
| [result-c61ba0ca3083a8ce9c03](../observations.json)<br>source-824d0132a1898fd7bb144625.json<br>`/cold/replicas/0/rates` | [glm53-capacity3](glm53-capacity3.md) | test outcome | Outcome unspecified | end_to_end_output_tps=38.72 accepted tokens/s; generated_tokens=4,096 accepted tokens; wall_seconds=105.78 s | Recorded configuration/job |
| [result-c6fe81999a61554b1fdf](../observations.json)<br>source-781f444772539bdc0224e270.json<br>`/stages/2` | [glm53-capacity3](glm53-capacity3.md) | test outcome | Pass | replayed_history_tokens=165 tokens | Recorded configuration/job |
| [result-c8b1b036c820f47c0851](../observations.json)<br>source-781f444772539bdc0224e270.json<br>`/stages/4/cold` | [glm53-capacity3](glm53-capacity3.md) | test outcome | Outcome unspecified | end_to_end_output_tps=0.77 accepted tokens/s; generated_tokens=213 accepted tokens; wall_seconds=275.98 s | Recorded configuration/job |
| [result-cb020528c31c88e16069](../observations.json)<br>source-cde4ecf31dafce3484cc531c.json<br>`/idle_stats/totals` | [glm53-capacity3](glm53-capacity3.md) | context allocation | Outcome unspecified | cached_tokens=10,662,912 tokens; generated_tokens=12,918 accepted tokens; prompt_tokens=12,839,358 tokens; recurrent_restores=108 checkpoints | Recorded configuration/job |
| [result-cb25f662492c57c883dd](../observations.json)<br>source-781f444772539bdc0224e270.json<br>`/stages/1/cold` | [glm53-capacity3](glm53-capacity3.md) | test outcome | Outcome unspecified | end_to_end_output_tps=1.63 accepted tokens/s; generated_tokens=734 accepted tokens; wall_seconds=451.10 s | Recorded configuration/job |
| [result-d2c4a69eca86e77594da](../observations.json)<br>source-781f444772539bdc0224e270.json<br>`/stages/0/cold` | [glm53-capacity3](glm53-capacity3.md) | test outcome | Outcome unspecified | end_to_end_output_tps=2.28 accepted tokens/s; generated_tokens=353 accepted tokens; wall_seconds=154.61 s | Recorded configuration/job |
| [result-d331d188fca791e0552e](../observations.json)<br>source-5a35c523994e864ed1e2e05a.json<br>`/after_cold` | [glm53-capacity3](glm53-capacity3.md) | test outcome | Outcome unspecified | context=500,000 tokens | Recorded configuration/job |
| [result-d91edd6fb7aebc4f4159](../observations.json)<br>source-5a35c523994e864ed1e2e05a.json<br>`/after_cold/totals` | [glm53-capacity3](glm53-capacity3.md) | context allocation | Outcome unspecified | cached_tokens=262,144 tokens; generated_tokens=1,772 accepted tokens; prompt_tokens=919,555 tokens; recurrent_restores=8 checkpoints | Recorded configuration/job |
| [result-de0d20186e03812441fc](../observations.json)<br>source-5a35c523994e864ed1e2e05a.json<br>`/after_cold/cache` | [glm53-capacity3](glm53-capacity3.md) | test outcome | Outcome unspecified | cached_tokens=655,616 tokens | Recorded configuration/job |
| [result-df5e49bd1353b290c393](../observations.json)<br>source-765eaac5eb5d951009e19e74.json<br>`/after_burst` | [glm53-capacity3](glm53-capacity3.md) | test outcome | Outcome unspecified | context=500,000 tokens | Recorded configuration/job |
| [result-e1c4c64eca94da9adbf4](../observations.json)<br>source-7ea9c5a7a51254b66dc04f78.json<br>`/after_burst/cache` | [glm53-capacity3](glm53-capacity3.md) | test outcome | Outcome unspecified | cached_tokens=262,144 tokens | Recorded configuration/job |
| [result-e443be22d9fef7fdb254](../observations.json)<br>source-3e12c1c06c62e444e0e37774.json<br>`/after_cold` | [glm53-capacity3](glm53-capacity3.md) | test outcome | Outcome unspecified | context=500,000 tokens | Recorded configuration/job |
| [result-e71371684cc865e721bd](../observations.json)<br>source-781f444772539bdc0224e270.json<br>`/stages/4` | [glm53-capacity3](glm53-capacity3.md) | test outcome | Pass | replayed_history_tokens=67 tokens | Recorded configuration/job |
| [result-e84eddf1acdde39bd4c4](../observations.json)<br>source-3e12c1c06c62e444e0e37774.json<br>`/after_cold/cache` | [glm53-capacity3](glm53-capacity3.md) | test outcome | Outcome unspecified | cached_tokens=786,176 tokens | Recorded configuration/job |
| [result-e9920eda87f2afb8347b](../observations.json)<br>source-781f444772539bdc0224e270.json<br>`/` | [glm53-capacity3](glm53-capacity3.md) | context allocation | Pass | recurrent_restores=24 checkpoints; restored_pages=15,344 pages | Recorded configuration/job |
| [result-eb0f7114c5926393dd05](../observations.json)<br>source-3e12c1c06c62e444e0e37774.json<br>`/after_burst/cache` | [glm53-capacity3](glm53-capacity3.md) | test outcome | Outcome unspecified | cached_tokens=782,080 tokens | Recorded configuration/job |
| [result-ebbd2638a1de29affe0a](../observations.json)<br>source-781f444772539bdc0224e270.json<br>`/stages/0` | [glm53-capacity3](glm53-capacity3.md) | test outcome | Pass | replayed_history_tokens=33 tokens | Recorded configuration/job |
| [result-f25fbd122e071713f1ff](../observations.json)<br>source-267ae14256a622a087b4bd24.json<br>`/after_burst/cache` | [glm53-capacity3](glm53-capacity3.md) | test outcome | Outcome unspecified | cached_tokens=782,080 tokens | Recorded configuration/job |
| [result-f3ed17e2ca783b44d77d](../observations.json)<br>source-267ae14256a622a087b4bd24.json<br>`/after_burst/totals` | [glm53-capacity3](glm53-capacity3.md) | context allocation | Outcome unspecified | cached_tokens=4,902,912 tokens; generated_tokens=3,849 accepted tokens; prompt_tokens=6,840,333 tokens; recurrent_restores=72 checkpoints | Recorded configuration/job |
| [result-fccb4fd67ac25aa756bb](../observations.json)<br>source-824d0132a1898fd7bb144625.json<br>`/warm/replicas/0/rates` | [glm53-capacity3](glm53-capacity3.md) | test outcome | Outcome unspecified | end_to_end_output_tps=54.19 accepted tokens/s; generated_tokens=4,096 accepted tokens; wall_seconds=75.58 s | Recorded configuration/job |
| [result-fe00c865a46ebecde6d0](../observations.json)<br>source-781f444772539bdc0224e270.json<br>`/stages/3/cold` | [glm53-capacity3](glm53-capacity3.md) | test outcome | Outcome unspecified | end_to_end_output_tps=0.67 accepted tokens/s; generated_tokens=181 accepted tokens; wall_seconds=272.07 s | Recorded configuration/job |
| [result-feda418b7cc0dc5593f5](../observations.json)<br>source-d387b69ade5dabb2cb6821e5.json<br>`/stages/3` | [glm53-capacity3](glm53-capacity3.md) | test outcome | Outcome unspecified | recurrent_restores_on_return=4 checkpoints; restored_page_images_on_return=7,028 pages; return_wave_seconds=14.91 s | Recorded configuration/job |
| [result-ff653f9923788fed72a4](../observations.json)<br>source-d387b69ade5dabb2cb6821e5.json<br>`/profile` | [glm53-capacity3](glm53-capacity3.md) | context allocation | Outcome unspecified | cache_tokens=786,432 tokens; context=500,000 tokens; reserve_mib=3,072 MiB | Recorded configuration/job |

These are saved result records, including failures and bounded checks. Copies, individual requests, report summaries and regrading can overlap; their counts are not independent test repetitions. Open each result for exact values, units, configuration binding and source receipts.

There are 6 retained lifecycle records. Their states, exit codes and configuration IDs remain in [catalog.json](../catalog.json); they do not supply missing benchmark results.

[Full archive](../../README.md) | [All retained waves](../RESULTS.md) | [Data definitions](../DATA.md) | [Recommended recipes](../../../README.md)
