# glm53-capacity3-agent-mtp0-rebalanced-1750k

**Historical record. Decode interval measured.**

Model family: GLM 5.3 Flash.

Recorded archive reason: Historical capacity, fit or control configuration; later DFlash2 and MTP variants have separate records.

Historical configurations are provided for comparison. The [recommended recipes](../../../README.md) include supported launch scripts.

Current recipes using the same recorded checkpoint repository: [glm-5.3-flash-mtp1-tp3](../../../recipes/glm-5.3-flash-mtp1-tp3/README.md). Context, cache and runtime versions can differ.

## Saved Configuration Versions

Each configuration ID identifies a distinct original settings record. Deployment fields are omitted; versions can have identical published settings after that omission. Upstream runtime commits remain unspecified where the source retained only an integration label.

| Configuration | Recorded artifact / source | Configured card counts | Context tokens | GPU pool tokens | Slots | Draft mode / tokens |
| --- | --- | --- | --- | --- | --- | --- |
| cfg-7b294aea7e89bfd5d522 | [turboderp/GLM-5.3-Flash-exl3@2a30229e67](https://huggingface.co/turboderp/GLM-5.3-Flash-exl3/tree/2a30229e67012798ba9f0cd832bb78abf4c363d5) | 3 | 500,000 | 1,835,008 | 4 | mtp / 1 |

Card counts are saved configuration choices, not a claim that every allowed placement was measured. A derived view can differ from its pinned download source.

<details>
<summary>cfg-7b294aea7e89bfd5d522</summary>

```json
{
  "kind": "tabby",
  "gpu_counts": [
    3
  ],
  "context": 500000,
  "cache_tokens": 1835008,
  "cache_mode": "Q8",
  "draft_cache_mode": "Q8",
  "draft_mode": "mtp",
  "draft_tokens": 1,
  "max_sessions": 4,
  "chunk_size": 256,
  "reserve_mib": 1024,
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
    1536,
    2560
  ]
}
```

Pinned model revision recorded: yes. Source receipt labels, hashes and object locators are retained in [configurations.json](../configurations.json).

</details>

## Retained Measurements

| Profile / Wave | Layout; Draft / Tokens | Requests | Input tokens/request | Accepted output tokens/request | Cache / Reused input tokens | Context / GPU pool tokens | Shared decode tok/s total | Client after-first-token estimate tok/s | Whole-wave output tok/s | Median TTFT, s | Source report |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [glm53-capacity3-agent-mtp0-rebalanced-1750k](glm53-capacity3-agent-mtp0-rebalanced-1750k.md)<br>wave-2b79b12788ad4039bba0 | layout unspecified; mtp / 1 | 2 | 8,254 | 512 | cold; reused 0 | 500,000 / 1,835,008 | 53.16 | Not recorded | 21.77 | 27.60 | Pass |
| [glm53-capacity3-agent-mtp0-rebalanced-1750k](glm53-capacity3-agent-mtp0-rebalanced-1750k.md)<br>wave-3c6428bde5841bed8a1c | layout unspecified; mtp / 1 | 4 | 400,039 | 39 to 65 | cold; reused 131,072 | 500,000 / 1,835,008 | Not recorded | Not recorded | 0.12 | 1,722.32 | Pass |
| [glm53-capacity3-agent-mtp0-rebalanced-1750k](glm53-capacity3-agent-mtp0-rebalanced-1750k.md)<br>wave-4586473a1a7cc7fda0dc | layout unspecified; mtp / 1 | 2 | 498,553 to 498,555 | 512 | cached_prefix; reused 497,920 | 500,000 / 1,835,008 | 41.42 | Not recorded | 33.42 | 6.09 | Pass |
| [glm53-capacity3-agent-mtp0-rebalanced-1750k](glm53-capacity3-agent-mtp0-rebalanced-1750k.md)<br>wave-52b2e7755dc43485fbb6 | layout unspecified; mtp / 1 | 4 | 450,091 to 450,127 | 19 | cached_prefix; reused 449,792 | 500,000 / 1,835,008 | Not recorded | Not recorded | 6.96 | 9.74 | Pass |
| [glm53-capacity3-agent-mtp0-rebalanced-1750k](glm53-capacity3-agent-mtp0-rebalanced-1750k.md)<br>wave-68c9e4ecae3dad0a6512 | layout unspecified; mtp / 1 | 2 | 8,744 to 8,760 | 512 | cached_prefix; reused 8,192 | 500,000 / 1,835,008 | 51.74 | Not recorded | 44.40 | 3.37 | Pass |
| [glm53-capacity3-agent-mtp0-rebalanced-1750k](glm53-capacity3-agent-mtp0-rebalanced-1750k.md)<br>wave-78b5766501b6376214b1 | layout unspecified; mtp / 1 | 4 | 32,896 to 32,926 | 19 | cached_prefix; reused 32,768 | 500,000 / 1,835,008 | Not recorded | Not recorded | 21.77 | 2.82 | Pass |
| [glm53-capacity3-agent-mtp0-rebalanced-1750k](glm53-capacity3-agent-mtp0-rebalanced-1750k.md)<br>wave-79dbcb7c62f6c47f0777 | layout unspecified; mtp / 1 | 2 | 498,031 | 512 | cold; reused 497,920 | 500,000 / 1,835,008 | 41.23 | Not recorded | 35.73 | 3.29 | Pass |
| [glm53-capacity3-agent-mtp0-rebalanced-1750k](glm53-capacity3-agent-mtp0-rebalanced-1750k.md)<br>wave-90f752c3c4edb5bf3925 | layout unspecified; mtp / 1 | 4 | 498,067 to 498,110 | 19 | cached_prefix; reused 497,920 | 500,000 / 1,835,008 | Not recorded | Not recorded | 7.34 | 7.98 | Pass |
| [glm53-capacity3-agent-mtp0-rebalanced-1750k](glm53-capacity3-agent-mtp0-rebalanced-1750k.md)<br>wave-c0ac1e6015915d705ff3 | layout unspecified; mtp / 1 | 4 | 400,087 to 400,113 | 19 | cached_prefix; reused 399,872 | 500,000 / 1,835,008 | Not recorded | Not recorded | 10.51 | 6.38 | Pass |
| [glm53-capacity3-agent-mtp0-rebalanced-1750k](glm53-capacity3-agent-mtp0-rebalanced-1750k.md)<br>wave-c27b02f9e3d5417669cf | layout unspecified; mtp / 1 | 4 | 450,043 | 39 to 75 | cold; reused 399,872 | 500,000 / 1,835,008 | Not recorded | Not recorded | 0.71 | 338.86 | Pass |
| [glm53-capacity3-agent-mtp0-rebalanced-1750k](glm53-capacity3-agent-mtp0-rebalanced-1750k.md)<br>wave-cbd078f1848000694ef8 | layout unspecified; mtp / 1 | 4 | 498,031 | 27 to 70 | cold; reused 449,792 | 500,000 / 1,835,008 | Not recorded | Not recorded | 0.52 | 251.89 | Pass |
| [glm53-capacity3-agent-mtp0-rebalanced-1750k](glm53-capacity3-agent-mtp0-rebalanced-1750k.md)<br>wave-d36fc641d7311901fc99 | layout unspecified; mtp / 1 | 4 | 131,148 to 131,198 | 19 | cached_prefix; reused 131,072 | 500,000 / 1,835,008 | Not recorded | Not recorded | 18.83 | 3.25 | Pass |
| [glm53-capacity3-agent-mtp0-rebalanced-1750k](glm53-capacity3-agent-mtp0-rebalanced-1750k.md)<br>wave-e7ec68906c2d6a621972 | layout unspecified; mtp / 1 | 4 | 131,101 | 83 to 128 | cold; reused 32,768 | 500,000 / 1,835,008 | Not recorded | Not recorded | 0.72 | 581.99 | Pass |
| [glm53-capacity3-agent-mtp0-rebalanced-1750k](glm53-capacity3-agent-mtp0-rebalanced-1750k.md)<br>wave-f1e8ca2508a6e7d6b4eb | layout unspecified; mtp / 1 | 4 | 32,803 | 84 to 114 | cold; reused 0 | 500,000 / 1,835,008 | Not recorded | Not recorded | 1.92 | 197.49 | Pass |

Rates are whole-wave totals over the stated request count. A wave may span multiple independent model instances; [measurements.json](../measurements.json) retains their contributions and the exact configuration IDs. Do not interpret a multi-instance total as one card's rate.

A dash in shared decode means no qualified synchronized interval is available. Whole-wave throughput includes prefill and queueing. A valid decode interval can survive inside an overall failed or partial check; the source-report outcome is preserved. No rows are averaged.

## Reported Rate Summaries

| Summary | Original field | Reported tok/s | Requests | Configuration binding |
| --- | --- | --- | --- | --- |
| summary-8faf4c5d3f70d7011469 | long_first_retained_tps | 41.23 | 2 | referenced_run_only |
| summary-dc87930a67f1369f1771 | long_returning_tps | 41.42 | 2 | referenced_run_only |
| summary-de2a10798cd45eea81ab | short_returning_tps | 51.74 | 2 | referenced_run_only |
| summary-fe3a292f5d81d8381718 | short_first_tps | 53.16 | 2 | referenced_run_only |

These quoted values can overlap detailed waves. A referenced earlier run's rate is not transferred to the citing configuration. Missing input, request and timing-window evidence remains missing. See [rate-summaries.json](../rate-summaries.json).

## Bounded Checks

| Check | Reported outcome | Retained counts / flags |
| --- | --- | --- |
| check-0c2a660fd27f7343eee0 | Pass | {"passed":true,"replayed_history_tokens":[35,35,35,35],"input_tokens":[32801,32801,32801,32801]} |
| check-103328cf398b362e2f09 | Pass | {"passed":true,"replayed_history_tokens":[251,251,251,251]} |
| check-136c99e06b4d9bf6c61b | Pass | {"passed":true,"input_tokens":[400037,400037,400037,400037],"replayed_history_tokens":[167,167,167,167],"extension_cached_tokens":[131072,131072,131072,131072]} |
| check-2f438b2562078c460b0f | Pass | {"passed":true} |
| check-3749b5ec74b5d8b42625 | Pass | {"passed":true,"replayed_history_tokens":[111,111,111,111]} |
| check-3d06bbb3376db20fd33f | Pass | {"passed":true,"replayed_history_tokens":[167,167,167,167]} |
| check-48c1f0fd454e442aefad | Pass | {"passed":true,"input_tokens":[450041,450041,450041,450041],"replayed_history_tokens":[251,251,251,251],"extension_cached_tokens":[399872,399872,399872,399872]} |
| check-4a681d0e36b311ad1e2d | Pass | {"passed":true,"replayed_history_tokens":[35,35,35,35]} |
| check-7cb906ceef03f8d2adf6 | Pass | {"passed":true,"input_tokens":[498029,498029,498029,498029],"replayed_history_tokens":[111,111,111,111],"extension_cached_tokens":[449792,449792,449792,449792]} |
| check-8318c874b4741f3fa31a | Pass | {"passed":true,"replayed_history_tokens":[29,29,29,29]} |
| check-8afa156b39cbd12b436e | Pass | {"passed":true,"recurrent_restores":24,"restored_pages":3535} |
| check-c1817cabfef2f1ed7a65 | Pass | {"return_wave_seconds":10.35537713299891,"passed":true,"replayed_history_tokens":[111,111,111,111]} |
| check-f559275d1150856cc692 | Pass | {"passed":true} |
| check-ff2b1dac77d59de0c222 | Pass | {"passed":true,"input_tokens":[131099,131099,131099,131099],"replayed_history_tokens":[29,29,29,29],"extension_cached_tokens":[32768,32768,32768,32768]} |

These checks retain their reported scope. A context/allocation/retrieval check is not a general quality score or a speed qualification at that context. Exact flags and provenance are in [checks.json](../checks.json).

## Additional Test Results

| Result / Source | Profile | Evidence type | Reported outcome | Retained values | Configuration binding |
| --- | --- | --- | --- | --- | --- |
| [result-068667f074c41a370e03](../observations.json)<br>source-2dd4ca9a1f9e1eb5c926adbf.json<br>`/after_cold/totals` | [glm53-capacity3-agent-mtp0-rebalanced-1750k](glm53-capacity3-agent-mtp0-rebalanced-1750k.md) | context allocation | Outcome unspecified | cached_tokens=4,788,224 tokens; generated_tokens=5,227 accepted tokens; prompt_tokens=6,742,603 tokens; recurrent_restores=58 checkpoints | Recorded configuration/job |
| [result-06b8859b311208ce8ed2](../observations.json)<br>source-2be7f39eee6cc5f8f104544a.json<br>`/warm/replicas/0/rates` | [glm53-capacity3-agent-mtp0-rebalanced-1750k](glm53-capacity3-agent-mtp0-rebalanced-1750k.md) | test outcome | Outcome unspecified | end_to_end_output_tps=33.42 accepted tokens/s; generated_tokens=1,024 accepted tokens; wall_seconds=30.64 s | Recorded configuration/job |
| [result-0a04da63ad95ae3b1790](../observations.json)<br>source-b900cfa5e2268781cd86a434.json<br>`/` | [glm53-capacity3-agent-mtp0-rebalanced-1750k](glm53-capacity3-agent-mtp0-rebalanced-1750k.md) | context allocation | Pass | recurrent_restores=24 checkpoints; restored_pages=3,535 pages | Recorded configuration/job |
| [result-0be0f298b453d6e2b85b](../observations.json)<br>source-68a00d1585d3640bfbe87feb.json<br>`/warm/replicas/0/rates` | [glm53-capacity3-agent-mtp0-rebalanced-1750k](glm53-capacity3-agent-mtp0-rebalanced-1750k.md) | test outcome | Outcome unspecified | end_to_end_output_tps=44.40 accepted tokens/s; generated_tokens=1,024 accepted tokens; wall_seconds=23.06 s | Recorded configuration/job |
| [result-0c3374f4915e0f4c5a77](../observations.json)<br>source-b3baf05cf655198da65f5d48.json<br>`/after_cold/cache` | [glm53-capacity3-agent-mtp0-rebalanced-1750k](glm53-capacity3-agent-mtp0-rebalanced-1750k.md) | test outcome | Outcome unspecified | cached_tokens=150,528 tokens | Recorded configuration/job |
| [result-0cd92fc949ace683f636](../observations.json)<br>source-146b0ff0ae89489f384f82d6.json<br>`/after_burst` | [glm53-capacity3-agent-mtp0-rebalanced-1750k](glm53-capacity3-agent-mtp0-rebalanced-1750k.md) | test outcome | Outcome unspecified | context=500,000 tokens | Recorded configuration/job |
| [result-1aed41c299773ed8c587](../observations.json)<br>source-70d912c53740eeab57ca32e7.json<br>`/after_burst` | [glm53-capacity3-agent-mtp0-rebalanced-1750k](glm53-capacity3-agent-mtp0-rebalanced-1750k.md) | test outcome | Outcome unspecified | context=500,000 tokens | Recorded configuration/job |
| [result-1fda282e69a7e3c9ea9b](../observations.json)<br>source-b900cfa5e2268781cd86a434.json<br>`/stages/4/cold` | [glm53-capacity3-agent-mtp0-rebalanced-1750k](glm53-capacity3-agent-mtp0-rebalanced-1750k.md) | test outcome | Outcome unspecified | end_to_end_output_tps=0.52 accepted tokens/s; generated_tokens=175 accepted tokens; wall_seconds=337.75 s | Recorded configuration/job |
| [result-23fa003d56d0dedf9022](../observations.json)<br>source-39fda3a8123844d2fa2bc877.json<br>`/last_runtime/totals` | [glm53-capacity3-agent-mtp0-rebalanced-1750k](glm53-capacity3-agent-mtp0-rebalanced-1750k.md) | context allocation | Outcome unspecified | cached_tokens=12,632,064 tokens; generated_tokens=8,626 accepted tokens; prompt_tokens=14,784,203 tokens; recurrent_restores=106 checkpoints | Recorded configuration/job |
| [result-2431b26917861b45371e](../observations.json)<br>source-70d912c53740eeab57ca32e7.json<br>`/after_cold/cache` | [glm53-capacity3-agent-mtp0-rebalanced-1750k](glm53-capacity3-agent-mtp0-rebalanced-1750k.md) | test outcome | Outcome unspecified | cached_tokens=674,816 tokens | Recorded configuration/job |
| [result-25f061f078da7e682b1a](../observations.json)<br>source-70d912c53740eeab57ca32e7.json<br>`/after_cold/totals` | [glm53-capacity3-agent-mtp0-rebalanced-1750k](glm53-capacity3-agent-mtp0-rebalanced-1750k.md) | context allocation | Outcome unspecified | cached_tokens=278,528 tokens; generated_tokens=3,600 accepted tokens; prompt_tokens=953,659 tokens; recurrent_restores=10 checkpoints | Recorded configuration/job |
| [result-2ad4a3b631ed271b7697](../observations.json)<br>source-2dd4ca9a1f9e1eb5c926adbf.json<br>`/after_cold` | [glm53-capacity3-agent-mtp0-rebalanced-1750k](glm53-capacity3-agent-mtp0-rebalanced-1750k.md) | test outcome | Outcome unspecified | context=500,000 tokens | Recorded configuration/job |
| [result-2caef5478f33cc9b529e](../observations.json)<br>source-b900cfa5e2268781cd86a434.json<br>`/stages/1/cold` | [glm53-capacity3-agent-mtp0-rebalanced-1750k](glm53-capacity3-agent-mtp0-rebalanced-1750k.md) | test outcome | Outcome unspecified | end_to_end_output_tps=0.72 accepted tokens/s; generated_tokens=426 accepted tokens; wall_seconds=589.23 s | Recorded configuration/job |
| [result-2e7a283cf2d8b964a3f0](../observations.json)<br>source-57954ab36e430def362a5ccf.json<br>`/profile_config` | [glm53-capacity3-agent-mtp0-rebalanced-1750k](glm53-capacity3-agent-mtp0-rebalanced-1750k.md) | context allocation | Outcome unspecified | cache_tokens=1,835,008 tokens; context=500,000 tokens; reserve_mib=1,024 MiB | Exact configuration unresolved |
| [result-2ed65e5acf39b9d88e21](../observations.json)<br>source-f0d4ae0635f986b4d5b70cbb.json<br>`/` | [glm53-capacity3-agent-mtp0-rebalanced-1750k](glm53-capacity3-agent-mtp0-rebalanced-1750k.md) | test outcome | Failed / partial | Reported error type: RuntimeError | Recorded configuration/job |
| [result-343238a19dea8905a045](../observations.json)<br>source-b3baf05cf655198da65f5d48.json<br>`/after_cold` | [glm53-capacity3-agent-mtp0-rebalanced-1750k](glm53-capacity3-agent-mtp0-rebalanced-1750k.md) | test outcome | Outcome unspecified | context=500,000 tokens | Recorded configuration/job |
| [result-34d219174dbf3f0d505e](../observations.json)<br>source-56df870d86e1d5bc469f735e.json<br>`/after_burst` | [glm53-capacity3-agent-mtp0-rebalanced-1750k](glm53-capacity3-agent-mtp0-rebalanced-1750k.md) | test outcome | Outcome unspecified | context=500,000 tokens | Recorded configuration/job |
| [result-37a8c647299763afb985](../observations.json)<br>source-2dd4ca9a1f9e1eb5c926adbf.json<br>`/after_burst` | [glm53-capacity3-agent-mtp0-rebalanced-1750k](glm53-capacity3-agent-mtp0-rebalanced-1750k.md) | test outcome | Outcome unspecified | context=500,000 tokens | Recorded configuration/job |
| [result-37d190a1498363fe378b](../observations.json)<br>source-68a00d1585d3640bfbe87feb.json<br>`/cold/replicas/0/rates` | [glm53-capacity3-agent-mtp0-rebalanced-1750k](glm53-capacity3-agent-mtp0-rebalanced-1750k.md) | test outcome | Outcome unspecified | end_to_end_output_tps=21.77 accepted tokens/s; generated_tokens=1,024 accepted tokens; wall_seconds=47.03 s | Recorded configuration/job |
| [result-3a08b026ec8663adabc5](../observations.json)<br>source-70d912c53740eeab57ca32e7.json<br>`/after_cold` | [glm53-capacity3-agent-mtp0-rebalanced-1750k](glm53-capacity3-agent-mtp0-rebalanced-1750k.md) | test outcome | Outcome unspecified | context=500,000 tokens | Recorded configuration/job |
| [result-3db84b94cc3ed3f4dfe9](../observations.json)<br>source-56df870d86e1d5bc469f735e.json<br>`/after_cold/cache` | [glm53-capacity3-agent-mtp0-rebalanced-1750k](glm53-capacity3-agent-mtp0-rebalanced-1750k.md) | test outcome | Outcome unspecified | cached_tokens=1,834,240 tokens | Recorded configuration/job |
| [result-3e5a3e92448ea343b243](../observations.json)<br>source-b900cfa5e2268781cd86a434.json<br>`/stages/1` | [glm53-capacity3-agent-mtp0-rebalanced-1750k](glm53-capacity3-agent-mtp0-rebalanced-1750k.md) | test outcome | Pass | replayed_history_tokens=29 tokens | Recorded configuration/job |
| [result-43d4b2fb5a939a7e9b3c](../observations.json)<br>source-b900cfa5e2268781cd86a434.json<br>`/stages/2/cold` | [glm53-capacity3-agent-mtp0-rebalanced-1750k](glm53-capacity3-agent-mtp0-rebalanced-1750k.md) | test outcome | Outcome unspecified | end_to_end_output_tps=0.12 accepted tokens/s; generated_tokens=208 accepted tokens; wall_seconds=1,725.66 s | Recorded configuration/job |
| [result-46908a48a4e7f10ad977](../observations.json)<br>source-146b0ff0ae89489f384f82d6.json<br>`/after_cold` | [glm53-capacity3-agent-mtp0-rebalanced-1750k](glm53-capacity3-agent-mtp0-rebalanced-1750k.md) | test outcome | Outcome unspecified | context=500,000 tokens | Recorded configuration/job |
| [result-4b6800a4e14731f9e1f3](../observations.json)<br>source-b900cfa5e2268781cd86a434.json<br>`/stages/4` | [glm53-capacity3-agent-mtp0-rebalanced-1750k](glm53-capacity3-agent-mtp0-rebalanced-1750k.md) | test outcome | Pass | replayed_history_tokens=111 tokens | Recorded configuration/job |
| [result-4ba23d54d8829ce3a6e4](../observations.json)<br>source-57954ab36e430def362a5ccf.json<br>`/long_workload` | [glm53-capacity3-agent-mtp0-rebalanced-1750k](glm53-capacity3-agent-mtp0-rebalanced-1750k.md) | test outcome | Outcome unspecified | output_tokens=512 tokens | Exact configuration unresolved |
| [result-4dac949141a3a6b4ee93](../observations.json)<br>source-b900cfa5e2268781cd86a434.json<br>`/stages/0` | [glm53-capacity3-agent-mtp0-rebalanced-1750k](glm53-capacity3-agent-mtp0-rebalanced-1750k.md) | test outcome | Pass | replayed_history_tokens=35 tokens | Recorded configuration/job |
| [result-5b1d61f9ea9c33e6fb1b](../observations.json)<br>source-39fda3a8123844d2fa2bc877.json<br>`/last_runtime/cache` | [glm53-capacity3-agent-mtp0-rebalanced-1750k](glm53-capacity3-agent-mtp0-rebalanced-1750k.md) | test outcome | Outcome unspecified | cached_tokens=1,833,216 tokens | Recorded configuration/job |
| [result-6b8fc4389ce56e3b5457](../observations.json)<br>source-70d912c53740eeab57ca32e7.json<br>`/after_burst/totals` | [glm53-capacity3-agent-mtp0-rebalanced-1750k](glm53-capacity3-agent-mtp0-rebalanced-1750k.md) | context allocation | Outcome unspecified | cached_tokens=409,600 tokens; generated_tokens=4,112 accepted tokens; prompt_tokens=1,085,419 tokens; recurrent_restores=26 checkpoints | Recorded configuration/job |
| [result-70ee5575f9a70d0973bb](../observations.json)<br>source-b900cfa5e2268781cd86a434.json<br>`/stages/2` | [glm53-capacity3-agent-mtp0-rebalanced-1750k](glm53-capacity3-agent-mtp0-rebalanced-1750k.md) | test outcome | Pass | replayed_history_tokens=167 tokens | Recorded configuration/job |
| [result-7ad007aa32d5acd36e31](../observations.json)<br>source-b900cfa5e2268781cd86a434.json<br>`/stages/0/cold` | [glm53-capacity3-agent-mtp0-rebalanced-1750k](glm53-capacity3-agent-mtp0-rebalanced-1750k.md) | test outcome | Outcome unspecified | end_to_end_output_tps=1.92 accepted tokens/s; generated_tokens=389 accepted tokens; wall_seconds=202.74 s | Recorded configuration/job |
| [result-7c318ff6ab877b21f782](../observations.json)<br>source-2dd4ca9a1f9e1eb5c926adbf.json<br>`/after_burst/totals` | [glm53-capacity3-agent-mtp0-rebalanced-1750k](glm53-capacity3-agent-mtp0-rebalanced-1750k.md) | context allocation | Outcome unspecified | cached_tokens=4,919,296 tokens; generated_tokens=5,739 accepted tokens; prompt_tokens=6,874,363 tokens; recurrent_restores=74 checkpoints | Recorded configuration/job |
| [result-7ffacd107f0cb61800f5](../observations.json)<br>source-2dd4ca9a1f9e1eb5c926adbf.json<br>`/after_cold/cache` | [glm53-capacity3-agent-mtp0-rebalanced-1750k](glm53-capacity3-agent-mtp0-rebalanced-1750k.md) | test outcome | Outcome unspecified | cached_tokens=1,825,536 tokens | Recorded configuration/job |
| [result-8500a09387e2546dbafc](../observations.json)<br>source-70d912c53740eeab57ca32e7.json<br>`/after_burst/cache` | [glm53-capacity3-agent-mtp0-rebalanced-1750k](glm53-capacity3-agent-mtp0-rebalanced-1750k.md) | test outcome | Outcome unspecified | cached_tokens=674,816 tokens | Recorded configuration/job |
| [result-8b3ed46f517b18592233](../observations.json)<br>source-b900cfa5e2268781cd86a434.json<br>`/stages/3/cold` | [glm53-capacity3-agent-mtp0-rebalanced-1750k](glm53-capacity3-agent-mtp0-rebalanced-1750k.md) | test outcome | Outcome unspecified | end_to_end_output_tps=0.71 accepted tokens/s; generated_tokens=243 accepted tokens; wall_seconds=344.64 s | Recorded configuration/job |
| [result-8dafc04eff420529de91](../observations.json)<br>source-57954ab36e430def362a5ccf.json<br>`/short_workload` | [glm53-capacity3-agent-mtp0-rebalanced-1750k](glm53-capacity3-agent-mtp0-rebalanced-1750k.md) | test outcome | Outcome unspecified | output_tokens=512 tokens | Exact configuration unresolved |
| [result-8dccf72e6812b7daa488](../observations.json)<br>source-146b0ff0ae89489f384f82d6.json<br>`/after_burst/totals` | [glm53-capacity3-agent-mtp0-rebalanced-1750k](glm53-capacity3-agent-mtp0-rebalanced-1750k.md) | context allocation | Outcome unspecified | cached_tokens=1,589,248 tokens; generated_tokens=4,908 accepted tokens; prompt_tokens=3,342,031 tokens; recurrent_restores=50 checkpoints | Recorded configuration/job |
| [result-8fb9ff909bc376a74ca0](../observations.json)<br>source-b900cfa5e2268781cd86a434.json<br>`/stages/0/warm` | [glm53-capacity3-agent-mtp0-rebalanced-1750k](glm53-capacity3-agent-mtp0-rebalanced-1750k.md) | test outcome | Outcome unspecified | end_to_end_output_tps=21.77 accepted tokens/s; generated_tokens=76 accepted tokens; wall_seconds=3.49 s | Recorded configuration/job |
| [result-93eb1eeab1f81396e0d3](../observations.json)<br>source-b900cfa5e2268781cd86a434.json<br>`/stages/3/warm` | [glm53-capacity3-agent-mtp0-rebalanced-1750k](glm53-capacity3-agent-mtp0-rebalanced-1750k.md) | test outcome | Outcome unspecified | end_to_end_output_tps=6.96 accepted tokens/s; generated_tokens=76 accepted tokens; wall_seconds=10.92 s | Recorded configuration/job |
| [result-a0852c675b2d50e058f0](../observations.json)<br>source-146b0ff0ae89489f384f82d6.json<br>`/after_burst/cache` | [glm53-capacity3-agent-mtp0-rebalanced-1750k](glm53-capacity3-agent-mtp0-rebalanced-1750k.md) | test outcome | Outcome unspecified | cached_tokens=1,750,016 tokens | Recorded configuration/job |
| [result-a5a2f1f618262c336414](../observations.json)<br>source-4f1eff02c53c4c1b71570807.json<br>`/cumulative_decode_restore_counters` | [glm53-capacity3-agent-mtp0-rebalanced-1750k](glm53-capacity3-agent-mtp0-rebalanced-1750k.md) | context allocation | Outcome unspecified | recurrent_restores=106 checkpoints | Recorded configuration/job |
| [result-ab97c26d25932c0ae2ce](../observations.json)<br>source-b900cfa5e2268781cd86a434.json<br>`/stages/3` | [glm53-capacity3-agent-mtp0-rebalanced-1750k](glm53-capacity3-agent-mtp0-rebalanced-1750k.md) | test outcome | Pass | replayed_history_tokens=251 tokens | Recorded configuration/job |
| [result-aba951b9cc91b6419d2d](../observations.json)<br>source-146b0ff0ae89489f384f82d6.json<br>`/after_cold/totals` | [glm53-capacity3-agent-mtp0-rebalanced-1750k](glm53-capacity3-agent-mtp0-rebalanced-1750k.md) | context allocation | Outcome unspecified | cached_tokens=1,458,176 tokens; generated_tokens=4,396 accepted tokens; prompt_tokens=3,210,271 tokens; recurrent_restores=34 checkpoints | Recorded configuration/job |
| [result-ad8ba16c66447ebbff80](../observations.json)<br>source-b3baf05cf655198da65f5d48.json<br>`/after_burst` | [glm53-capacity3-agent-mtp0-rebalanced-1750k](glm53-capacity3-agent-mtp0-rebalanced-1750k.md) | test outcome | Outcome unspecified | context=500,000 tokens | Recorded configuration/job |
| [result-b73f9f33aeba1003f718](../observations.json)<br>source-56df870d86e1d5bc469f735e.json<br>`/after_burst/totals` | [glm53-capacity3-agent-mtp0-rebalanced-1750k](glm53-capacity3-agent-mtp0-rebalanced-1750k.md) | context allocation | Outcome unspecified | cached_tokens=8,648,704 tokens; generated_tokens=6,502 accepted tokens; prompt_tokens=10,798,698 tokens; recurrent_restores=98 checkpoints | Recorded configuration/job |
| [result-c1fbf5af1db5c26af717](../observations.json)<br>source-b900cfa5e2268781cd86a434.json<br>`/stages/4/warm` | [glm53-capacity3-agent-mtp0-rebalanced-1750k](glm53-capacity3-agent-mtp0-rebalanced-1750k.md) | test outcome | Outcome unspecified | end_to_end_output_tps=7.34 accepted tokens/s; generated_tokens=76 accepted tokens; wall_seconds=10.36 s | Recorded configuration/job |
| [result-c2484d1449b279610293](../observations.json)<br>source-b900cfa5e2268781cd86a434.json<br>`/stages/1/warm` | [glm53-capacity3-agent-mtp0-rebalanced-1750k](glm53-capacity3-agent-mtp0-rebalanced-1750k.md) | test outcome | Outcome unspecified | end_to_end_output_tps=18.83 accepted tokens/s; generated_tokens=76 accepted tokens; wall_seconds=4.04 s | Recorded configuration/job |
| [result-c2e48452b9f0f9b4eb1f](../observations.json)<br>source-39fda3a8123844d2fa2bc877.json<br>`/last_runtime` | [glm53-capacity3-agent-mtp0-rebalanced-1750k](glm53-capacity3-agent-mtp0-rebalanced-1750k.md) | test outcome | Outcome unspecified | context=500,000 tokens | Recorded configuration/job |
| [result-d0a86b788c0f2c12568e](../observations.json)<br>source-2be7f39eee6cc5f8f104544a.json<br>`/cold/replicas/0/rates` | [glm53-capacity3-agent-mtp0-rebalanced-1750k](glm53-capacity3-agent-mtp0-rebalanced-1750k.md) | test outcome | Outcome unspecified | end_to_end_output_tps=35.73 accepted tokens/s; generated_tokens=1,024 accepted tokens; wall_seconds=28.66 s | Recorded configuration/job |
| [result-d13ce0265f4eb6b15da7](../observations.json)<br>source-4f1eff02c53c4c1b71570807.json<br>`/` | [glm53-capacity3-agent-mtp0-rebalanced-1750k](glm53-capacity3-agent-mtp0-rebalanced-1750k.md) | test outcome | Pass | replayed_history_tokens=111 tokens; return_wave_seconds=10.36 s | Recorded configuration/job |
| [result-d8fbd4cebf268b714f49](../observations.json)<br>source-b900cfa5e2268781cd86a434.json<br>`/stages/2/warm` | [glm53-capacity3-agent-mtp0-rebalanced-1750k](glm53-capacity3-agent-mtp0-rebalanced-1750k.md) | test outcome | Outcome unspecified | end_to_end_output_tps=10.51 accepted tokens/s; generated_tokens=76 accepted tokens; wall_seconds=7.23 s | Recorded configuration/job |
| [result-dd8fb44d2d9eef36dc9b](../observations.json)<br>source-b3baf05cf655198da65f5d48.json<br>`/after_burst/totals` | [glm53-capacity3-agent-mtp0-rebalanced-1750k](glm53-capacity3-agent-mtp0-rebalanced-1750k.md) | context allocation | Outcome unspecified | cached_tokens=16,384 tokens; generated_tokens=3,098 accepted tokens; prompt_tokens=297,618 tokens; recurrent_restores=2 checkpoints | Recorded configuration/job |
| [result-e083a21a9bfe18b913a8](../observations.json)<br>source-56df870d86e1d5bc469f735e.json<br>`/after_cold` | [glm53-capacity3-agent-mtp0-rebalanced-1750k](glm53-capacity3-agent-mtp0-rebalanced-1750k.md) | test outcome | Outcome unspecified | context=500,000 tokens | Recorded configuration/job |
| [result-e58355b86db60f1e536a](../observations.json)<br>source-56df870d86e1d5bc469f735e.json<br>`/after_cold/totals` | [glm53-capacity3-agent-mtp0-rebalanced-1750k](glm53-capacity3-agent-mtp0-rebalanced-1750k.md) | context allocation | Outcome unspecified | cached_tokens=8,517,632 tokens; generated_tokens=5,990 accepted tokens; prompt_tokens=10,666,938 tokens; recurrent_restores=82 checkpoints | Recorded configuration/job |
| [result-f1786a099b0c2d908e80](../observations.json)<br>source-b3baf05cf655198da65f5d48.json<br>`/after_cold/totals` | [glm53-capacity3-agent-mtp0-rebalanced-1750k](glm53-capacity3-agent-mtp0-rebalanced-1750k.md) | context allocation | Outcome unspecified | cached_tokens=16,384 tokens; generated_tokens=2,586 accepted tokens; prompt_tokens=165,858 tokens; recurrent_restores=2 checkpoints | Recorded configuration/job |
| [result-f376f7447f84039fa480](../observations.json)<br>source-2dd4ca9a1f9e1eb5c926adbf.json<br>`/after_burst/cache` | [glm53-capacity3-agent-mtp0-rebalanced-1750k](glm53-capacity3-agent-mtp0-rebalanced-1750k.md) | test outcome | Outcome unspecified | cached_tokens=1,825,536 tokens | Recorded configuration/job |
| [result-f3e98563918d75568ff8](../observations.json)<br>source-146b0ff0ae89489f384f82d6.json<br>`/after_cold/cache` | [glm53-capacity3-agent-mtp0-rebalanced-1750k](glm53-capacity3-agent-mtp0-rebalanced-1750k.md) | test outcome | Outcome unspecified | cached_tokens=1,750,016 tokens | Recorded configuration/job |
| [result-f74f2dc84373795871da](../observations.json)<br>source-56df870d86e1d5bc469f735e.json<br>`/after_burst/cache` | [glm53-capacity3-agent-mtp0-rebalanced-1750k](glm53-capacity3-agent-mtp0-rebalanced-1750k.md) | test outcome | Outcome unspecified | cached_tokens=1,830,144 tokens | Recorded configuration/job |
| [result-ffa32856b4a3a19abbb1](../observations.json)<br>source-b3baf05cf655198da65f5d48.json<br>`/after_burst/cache` | [glm53-capacity3-agent-mtp0-rebalanced-1750k](glm53-capacity3-agent-mtp0-rebalanced-1750k.md) | test outcome | Outcome unspecified | cached_tokens=281,600 tokens | Recorded configuration/job |

These are saved result records, including failures and bounded checks. Copies, individual requests, report summaries and regrading can overlap; their counts are not independent test repetitions. Open each result for exact values, units, configuration binding and source receipts.

There are 1 retained lifecycle records. Their states, exit codes and configuration IDs remain in [catalog.json](../catalog.json); they do not supply missing benchmark results.

[Full archive](../../README.md) | [All retained waves](../RESULTS.md) | [Data definitions](../DATA.md) | [Recommended recipes](../../../README.md)
