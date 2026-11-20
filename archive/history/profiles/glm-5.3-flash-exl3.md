# glm-5.3-flash-exl3

**Historical record. Decode interval measured.**

Model family: GLM 5.3 Flash.

Historical configurations are provided for comparison. The [recommended recipes](../../../README.md) include supported launch scripts.

Current recipes using the same recorded checkpoint repository: [glm-5.3-flash-mtp1-tp3](../../../recipes/glm-5.3-flash-mtp1-tp3/README.md). Context, cache and runtime versions can differ.

## Saved Configuration Versions

Each configuration ID identifies a distinct original settings record. Deployment fields are omitted; versions can have identical published settings after that omission. Upstream runtime commits remain unspecified where the source retained only an integration label.

| Configuration | Recorded artifact / source | Configured card counts | Context tokens | GPU pool tokens | Slots | Draft mode / tokens |
| --- | --- | --- | --- | --- | --- | --- |
| cfg-6f8ee43f93d6bad9aa85 | [turboderp/GLM-5.3-Flash-exl3@2a30229e67](https://huggingface.co/turboderp/GLM-5.3-Flash-exl3/tree/2a30229e67012798ba9f0cd832bb78abf4c363d5) | 3 | 500,000 | 1,835,008 | 4 | mtp / 1 |
| cfg-e033484cc5fecc5be7a7 | [turboderp/GLM-5.3-Flash-exl3@2a30229e67](https://huggingface.co/turboderp/GLM-5.3-Flash-exl3/tree/2a30229e67012798ba9f0cd832bb78abf4c363d5) | 3 | 500,000 | 786,432 | 4 | dflash2 / 3 |

Card counts are saved configuration choices, not a claim that every allowed placement was measured. A derived view can differ from its pinned download source.

<details>
<summary>cfg-6f8ee43f93d6bad9aa85</summary>

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

<details>
<summary>cfg-e033484cc5fecc5be7a7</summary>

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
| [glm-5.3-flash-exl3](glm-5.3-flash-exl3.md)<br>wave-3b4d61fead7a5d2a3b25 | layout unspecified; dflash2 / 3 | 4 | 450,040 | 39 to 43 | cold; reused 399,872 | 500,000 / 786,432 | Not recorded | Not recorded | 0.46 | 215.61 | Pass |
| [glm-5.3-flash-exl3](glm-5.3-flash-exl3.md)<br>wave-4bdfab2b30bfa4977be9 | layout unspecified; dflash2 / 3 | 4 | 32,800 | 63 to 109 | cold; reused 0 | 500,000 / 786,432 | Not recorded | Not recorded | 1.63 | 189.18 | Pass |
| [glm-5.3-flash-exl3](glm-5.3-flash-exl3.md)<br>wave-5979437b1f1cb0dbc24d | layout unspecified; dflash2 / 3 | 1 | 498,028 | 512 | cold; reused 497,920 | 500,000 / 786,432 | 27.84 | Not recorded | 20.85 | 6.42 | Pass |
| [glm-5.3-flash-exl3](glm-5.3-flash-exl3.md)<br>wave-628aef072b9a6ae343da | layout unspecified; dflash2 / 3 | 1 | 498,524 | 512 | cached_prefix; reused 497,920 | 500,000 / 786,432 | 35.44 | Not recorded | 29.63 | 3.06 | Pass |
| [glm-5.3-flash-exl3](glm-5.3-flash-exl3.md)<br>wave-749800a57726a9111de0 | layout unspecified; dflash2 / 3 | 4 | 498,089 to 498,102 | 19 | cached_prefix; reused 497,920 | 500,000 / 786,432 | Not recorded | Not recorded | 2.76 | 18.61 | Pass |
| [glm-5.3-flash-exl3](glm-5.3-flash-exl3.md)<br>wave-7cc8fb04a608be71944b | layout unspecified; dflash2 / 3 | 4 | 400,084 to 400,114 | 19 | cached_prefix; reused 399,872 | 500,000 / 786,432 | Not recorded | Not recorded | 3.44 | 14.65 | Pass |
| [glm-5.3-flash-exl3](glm-5.3-flash-exl3.md)<br>wave-7dc8a7ba403088af819c | layout unspecified; dflash2 / 3 | 4 | 32,872 to 32,918 | 19 | cached_prefix; reused 32,768 | 500,000 / 786,432 | Not recorded | Not recorded | 22.16 | 3.09 | Pass |
| [glm-5.3-flash-exl3](glm-5.3-flash-exl3.md)<br>wave-83b48e0b29450c12eb17 | layout unspecified; dflash2 / 3 | 4 | 400,036 | 39 to 69 | cold; reused 131,072 | 500,000 / 786,432 | Not recorded | Not recorded | 0.12 | 1,025.03 | Pass |
| [glm-5.3-flash-exl3](glm-5.3-flash-exl3.md)<br>wave-9d9b7c07d2078d19de44 | layout unspecified; mtp / 1 | 2 | 8,759 to 8,760 | 512 | cached_prefix; reused 8,192 | 500,000 / 1,835,008 | 51.88 | Not recorded | 44.29 | 3.45 | Pass |
| [glm-5.3-flash-exl3](glm-5.3-flash-exl3.md)<br>wave-a5d50635fc5a1d13d98b | layout unspecified; dflash2 / 3 | 4 | 131,158 to 131,187 | 19 to 22 | cached_prefix; reused 131,072 | 500,000 / 786,432 | Not recorded | Not recorded | 16.97 | 4.06 | Pass |
| [glm-5.3-flash-exl3](glm-5.3-flash-exl3.md)<br>wave-b726ac59d7fcdb7af24a | layout unspecified; mtp / 1 | 2 | 8,252 | 512 | cold; reused 0 | 500,000 / 1,835,008 | 54.08 | Not recorded | 22.32 | 26.56 | Pass |
| [glm-5.3-flash-exl3](glm-5.3-flash-exl3.md)<br>wave-bfc44b06084202a0b27a | layout unspecified; dflash2 / 3 | 4 | 131,098 | 51 to 113 | cold; reused 32,768 | 500,000 / 786,432 | Not recorded | Not recorded | 0.51 | 555.30 | Pass |
| [glm-5.3-flash-exl3](glm-5.3-flash-exl3.md)<br>wave-c231b6d8da15dbeb131d | layout unspecified; dflash2 / 3 | 4 | 498,028 | 65 to 86 | cold; reused 449,792 | 500,000 / 786,432 | Not recorded | Not recorded | 0.91 | 215.28 | Pass |
| [glm-5.3-flash-exl3](glm-5.3-flash-exl3.md)<br>wave-ee0487274358027db72d | layout unspecified; dflash2 / 3 | 4 | 450,088 to 450,092 | 19 | cached_prefix; reused 449,792 | 500,000 / 786,432 | Not recorded | Not recorded | 3.46 | 14.61 | Pass |

Rates are whole-wave totals over the stated request count. A wave may span multiple independent model instances; [measurements.json](../measurements.json) retains their contributions and the exact configuration IDs. Do not interpret a multi-instance total as one card's rate.

A dash in shared decode means no qualified synchronized interval is available. Whole-wave throughput includes prefill and queueing. A valid decode interval can survive inside an overall failed or partial check; the source-report outcome is preserved. No rows are averaged.

## Bounded Checks

| Check | Reported outcome | Retained counts / flags |
| --- | --- | --- |
| check-062347b2ed756cc0bbf2 | Pass | {"passed":true,"replayed_history_tokens":[248,248,248,248]} |
| check-08936175236eef7d443d | Pass | {"passed":true} |
| check-12f13951932352ddc5df | Pass | {"passed":true,"replayed_history_tokens":[164,164,164,164]} |
| check-2127af5d5571594aa1a0 | Pass | {"passed":true,"replayed_history_tokens":[32,32,32,32]} |
| check-2aab4aef67c16aeff3fc | Pass | {"passed":true,"replayed_history_tokens":[248,248,248,248]} |
| check-2b1be2b9e541ef9de8a7 | Pass | {"passed":true,"replayed_history_tokens":[32,32,32,32],"input_tokens":[32798,32798,32798,32798]} |
| check-3d11bbde88c7eb128b31 | Pass | {"passed":true,"recurrent_restores":24,"restored_pages":15320} |
| check-4fc95eb7c85fb048d069 | Pass | {"passed":true} |
| check-5a895ecedfc03e0e0e6c | Pass | {"passed":true,"replayed_history_tokens":[26,26,26,26]} |
| check-5b68dddb00f096f2e764 | Pass | {"passed":true,"compact_tokens":400000,"context_tokens":500000} |
| check-5ef9a0712e6a2cd90034 | Pass | {"passed":true,"compact_tokens":400000,"context_tokens":500000} |
| check-600c0cec19d4bcd5f87a | Pass | {"ram_kv_page_image_tokens":1480960,"passed":true,"configured_slots":4} |
| check-6b95a0a673b56dba4a83 | Pass | {"passed":true,"compact_tokens":400000,"context_tokens":500000} |
| check-797e0cca879b34f0c445 | Pass | {"passed":true,"replayed_history_tokens":[108,108,108,108]} |
| check-7da17f627810dfd5f0da | Pass | {"passed":true,"replayed_history_tokens":[164,164,164,164]} |
| check-80d9eb58de90c737c6e5 | Pass | {"passed":true,"compact_tokens":400000,"context_tokens":500000} |
| check-84b6bebb440f825ea94f | Pass | {"passed":true,"replayed_history_tokens":[32,32,32,32]} |
| check-8d15cfb092242073d247 | Pass | {"passed":true,"replayed_history_tokens":[108,108,108,108]} |
| check-91c4fd4970e7cc30801c | Pass | {"passed":true,"input_tokens":[131096,131096,131096,131096],"replayed_history_tokens":[26,26,26,26],"extension_cached_tokens":[32768,32768,32768,32768]} |
| check-951be3857a416d88b568 | Pass | {"passed":true,"replayed_history_tokens":[164,164,164,164]} |
| check-97f03703597b4c6ae840 | Pass | {"passed":true,"replayed_history_tokens":[26,26,26,26]} |
| check-9df93b6fa23898c110c7 | Pass | {"passed":true,"replayed_history_tokens":[108,108,108,108]} |
| check-ad9725a7619807d5e6a5 | Pass | {"passed":true,"input_tokens":[498026,498026,498026,498026],"replayed_history_tokens":[108,108,108,108],"extension_cached_tokens":[449792,449792,449792,449792]} |
| check-b85dcc8eaef6abc9d648 | Pass | {"passed":true,"replayed_history_tokens":[248,248,248,248]} |
| check-bc6d91715f60744beae2 | Pass | {"passed":true} |
| check-cc0f0add2064ef20cb1e | Pass | {"passed":true,"input_tokens":[400034,400034,400034,400034],"replayed_history_tokens":[164,164,164,164],"extension_cached_tokens":[131072,131072,131072,131072]} |
| check-e1336700c6589f528c92 | Pass | {"passed":true,"replayed_history_tokens":[32,32,32,32]} |
| check-f0816a18e9c9a5c1f752 | Pass | {"passed":true,"replayed_history_tokens":[26,26,26,26]} |
| check-ffdf7392de1f74f50936 | Pass | {"passed":true,"input_tokens":[450038,450038,450038,450038],"replayed_history_tokens":[248,248,248,248],"extension_cached_tokens":[399872,399872,399872,399872]} |

These checks retain their reported scope. A context/allocation/retrieval check is not a general quality score or a speed qualification at that context. Exact flags and provenance are in [checks.json](../checks.json).

## Additional Test Results

| Result / Source | Profile | Evidence type | Reported outcome | Retained values | Configuration binding |
| --- | --- | --- | --- | --- | --- |
| [result-00cc48e0dd176cca1bb3](../observations.json)<br>source-53b47e140621dafd2d38e470.json<br>`/after_burst/cache` | [glm-5.3-flash-exl3](glm-5.3-flash-exl3.md) | test outcome | Outcome unspecified | cached_tokens=782,080 tokens | Recorded configuration/job |
| [result-02b7762139a1d96af49b](../observations.json)<br>source-2ab1817b31fc8a349fa7e4fb.json<br>`/stages/4/warm` | [glm-5.3-flash-exl3](glm-5.3-flash-exl3.md) | test outcome | Outcome unspecified | end_to_end_output_tps=2.76 accepted tokens/s; generated_tokens=76 accepted tokens; wall_seconds=27.51 s | Recorded configuration/job |
| [result-07af1eb4b7680259a88e](../observations.json)<br>source-53b47e140621dafd2d38e470.json<br>`/after_cold` | [glm-5.3-flash-exl3](glm-5.3-flash-exl3.md) | test outcome | Outcome unspecified | context=500,000 tokens | Recorded configuration/job |
| [result-0f657366b433594e86ab](../observations.json)<br>source-1a75b76ac6d334615e55e710.json<br>`/completed_stages/0` | [glm-5.3-flash-exl3](glm-5.3-flash-exl3.md) | test outcome | Pass | replayed_history_tokens=32 tokens | Recorded configuration/job |
| [result-16d18f253a15bc3c09c3](../observations.json)<br>source-2ab1817b31fc8a349fa7e4fb.json<br>`/stages/1/cold` | [glm-5.3-flash-exl3](glm-5.3-flash-exl3.md) | test outcome | Outcome unspecified | end_to_end_output_tps=0.51 accepted tokens/s; generated_tokens=285 accepted tokens; wall_seconds=560.76 s | Recorded configuration/job |
| [result-1989750104fa135c579a](../observations.json)<br>source-d707ed443de5b0f6a93263f9.json<br>`/last_runtime/totals` | [glm-5.3-flash-exl3](glm-5.3-flash-exl3.md) | context allocation | Outcome unspecified | cached_tokens=11,647,232 tokens; generated_tokens=6,273 accepted tokens; prompt_tokens=13,791,190 tokens; recurrent_restores=109 checkpoints | Recorded configuration/job |
| [result-1c41cc2e24efcd0abe33](../observations.json)<br>source-2ab1817b31fc8a349fa7e4fb.json<br>`/stages/0/cold` | [glm-5.3-flash-exl3](glm-5.3-flash-exl3.md) | test outcome | Outcome unspecified | end_to_end_output_tps=1.63 accepted tokens/s; generated_tokens=316 accepted tokens; wall_seconds=193.64 s | Recorded configuration/job |
| [result-1d9a5ab10339dc6b8fa1](../observations.json)<br>source-2ab1817b31fc8a349fa7e4fb.json<br>`/stages/0` | [glm-5.3-flash-exl3](glm-5.3-flash-exl3.md) | test outcome | Pass | replayed_history_tokens=32 tokens | Recorded configuration/job |
| [result-214e8b5318e66a4d6029](../observations.json)<br>source-1a75b76ac6d334615e55e710.json<br>`/completed_stages/3` | [glm-5.3-flash-exl3](glm-5.3-flash-exl3.md) | test outcome | Pass | replayed_history_tokens=248 tokens | Recorded configuration/job |
| [result-21ea2eb5e95d1ac864d1](../observations.json)<br>source-522af409c2158fc1893f37f6.json<br>`/after_burst/totals` | [glm-5.3-flash-exl3](glm-5.3-flash-exl3.md) | context allocation | Outcome unspecified | cached_tokens=420,608 tokens; generated_tokens=2,742 accepted tokens; prompt_tokens=1,089,297 tokens; recurrent_restores=31 checkpoints | Recorded configuration/job |
| [result-2472b30f9ec2ad6d86f0](../observations.json)<br>source-a4d3e020cc4183805ce3e9c7.json<br>`/tabby` | [glm-5.3-flash-exl3](glm-5.3-flash-exl3.md) | test outcome | Outcome unspecified | cache_tokens=786,432 tokens | Recorded configuration/job |
| [result-2607cdc706230f8991a6](../observations.json)<br>source-84a296f9a57b3e4e910a7a5f.json<br>`/verification` | [glm-5.3-flash-exl3](glm-5.3-flash-exl3.md) | test outcome | Outcome unspecified | elapsed_seconds=0.06 s | Recorded configuration/job |
| [result-27d5bf5a08a4b1ce9a87](../observations.json)<br>source-2ab1817b31fc8a349fa7e4fb.json<br>`/` | [glm-5.3-flash-exl3](glm-5.3-flash-exl3.md) | context allocation | Pass | recurrent_restores=24 checkpoints; restored_pages=15,320 pages | Recorded configuration/job |
| [result-28069f045c885b0b5484](../observations.json)<br>source-cf4b5241f6c03e5a7037442a.json<br>`/` | [glm-5.3-flash-exl3](glm-5.3-flash-exl3.md) | test outcome | Pass | configured_slots=4 requests; ram_kv_page_image_tokens=1,480,960 tokens | Recorded configuration/job |
| [result-299a329e0e1e578a94ab](../observations.json)<br>source-abea772809c501893816c341.json<br>`/tabby` | [glm-5.3-flash-exl3](glm-5.3-flash-exl3.md) | test outcome | Outcome unspecified | cache_tokens=1,835,008 tokens | Recorded configuration/job |
| [result-2a5635b5b5f8d93549ae](../observations.json)<br>source-84a296f9a57b3e4e910a7a5f.json<br>`/client_result` | [glm-5.3-flash-exl3](glm-5.3-flash-exl3.md) | test outcome | Outcome unspecified | elapsed_seconds=16.75 s | Recorded configuration/job |
| [result-2b30920833420e0a3336](../observations.json)<br>source-2ab1817b31fc8a349fa7e4fb.json<br>`/stages/3/cold` | [glm-5.3-flash-exl3](glm-5.3-flash-exl3.md) | test outcome | Outcome unspecified | end_to_end_output_tps=0.46 accepted tokens/s; generated_tokens=160 accepted tokens; wall_seconds=344.10 s | Recorded configuration/job |
| [result-2e14592c0e4fe7a8998f](../observations.json)<br>source-946ea71503877f436b7cbf7d.json<br>`/after_burst/cache` | [glm-5.3-flash-exl3](glm-5.3-flash-exl3.md) | test outcome | Outcome unspecified | cached_tokens=782,080 tokens | Recorded configuration/job |
| [result-30989577b7f8d7dacc8d](../observations.json)<br>source-522af409c2158fc1893f37f6.json<br>`/after_cold` | [glm-5.3-flash-exl3](glm-5.3-flash-exl3.md) | test outcome | Outcome unspecified | context=500,000 tokens | Recorded configuration/job |
| [result-32e996eb34de3a3d7e43](../observations.json)<br>source-946ea71503877f436b7cbf7d.json<br>`/after_burst/totals` | [glm-5.3-flash-exl3](glm-5.3-flash-exl3.md) | context allocation | Outcome unspecified | cached_tokens=4,930,304 tokens; generated_tokens=4,271 accepted tokens; prompt_tokens=6,878,075 tokens; recurrent_restores=79 checkpoints | Recorded configuration/job |
| [result-340fbcdfe6c3d90f7c07](../observations.json)<br>source-946ea71503877f436b7cbf7d.json<br>`/after_burst` | [glm-5.3-flash-exl3](glm-5.3-flash-exl3.md) | test outcome | Outcome unspecified | context=500,000 tokens | Recorded configuration/job |
| [result-3f19ef9f51322705906d](../observations.json)<br>source-84a296f9a57b3e4e910a7a5f.json<br>`/` | [glm-5.3-flash-exl3](glm-5.3-flash-exl3.md) | context allocation | Pass | compact_tokens=400,000 tokens; context_tokens=500,000 tokens | Recorded configuration/job |
| [result-4333bb925ad87071b227](../observations.json)<br>source-2ab1817b31fc8a349fa7e4fb.json<br>`/stages/3` | [glm-5.3-flash-exl3](glm-5.3-flash-exl3.md) | test outcome | Pass | replayed_history_tokens=248 tokens | Recorded configuration/job |
| [result-50397472ff4bc915c243](../observations.json)<br>source-1a75b76ac6d334615e55e710.json<br>`/current_cache` | [glm-5.3-flash-exl3](glm-5.3-flash-exl3.md) | test outcome | Outcome unspecified | cached_tokens=785,920 tokens | Recorded configuration/job |
| [result-53fc0229532624765ba3](../observations.json)<br>source-d3d536389bbf245ede9ae53b.json<br>`/after_burst/cache` | [glm-5.3-flash-exl3](glm-5.3-flash-exl3.md) | test outcome | Outcome unspecified | cached_tokens=782,080 tokens | Recorded configuration/job |
| [result-557fc41694fad42e36d1](../observations.json)<br>source-2ab1817b31fc8a349fa7e4fb.json<br>`/stages/1` | [glm-5.3-flash-exl3](glm-5.3-flash-exl3.md) | test outcome | Pass | replayed_history_tokens=26 tokens | Recorded configuration/job |
| [result-567e551d5849d3813802](../observations.json)<br>source-d3d536389bbf245ede9ae53b.json<br>`/after_burst/totals` | [glm-5.3-flash-exl3](glm-5.3-flash-exl3.md) | context allocation | Outcome unspecified | cached_tokens=8,659,712 tokens; generated_tokens=5,173 accepted tokens; prompt_tokens=10,802,255 tokens; recurrent_restores=103 checkpoints | Recorded configuration/job |
| [result-5a2028bcb2cb30b0bfee](../observations.json)<br>source-53b47e140621dafd2d38e470.json<br>`/after_cold/cache` | [glm-5.3-flash-exl3](glm-5.3-flash-exl3.md) | test outcome | Outcome unspecified | cached_tokens=786,176 tokens | Recorded configuration/job |
| [result-5b8931246a4505c0d7c6](../observations.json)<br>source-1a3f2a4cf5331236024200f3.json<br>`/after_burst/totals` | [glm-5.3-flash-exl3](glm-5.3-flash-exl3.md) | context allocation | Outcome unspecified | cached_tokens=27,392 tokens; generated_tokens=1,869 accepted tokens; prompt_tokens=301,641 tokens; recurrent_restores=7 checkpoints | Recorded configuration/job |
| [result-63e4ffd872d12507fad9](../observations.json)<br>source-2ab1817b31fc8a349fa7e4fb.json<br>`/stages/2` | [glm-5.3-flash-exl3](glm-5.3-flash-exl3.md) | test outcome | Pass | replayed_history_tokens=164 tokens | Recorded configuration/job |
| [result-6b2d3f76bca6e5cfb003](../observations.json)<br>source-6c4907b44525431e880003f2.json<br>`/` | [glm-5.3-flash-exl3](glm-5.3-flash-exl3.md) | test outcome | Outcome unspecified | context=500,000 tokens | Recorded configuration/job |
| [result-7124e2a8dbfcb5833c20](../observations.json)<br>source-522af409c2158fc1893f37f6.json<br>`/after_burst` | [glm-5.3-flash-exl3](glm-5.3-flash-exl3.md) | test outcome | Outcome unspecified | context=500,000 tokens | Recorded configuration/job |
| [result-77dcc6ec242265d619ea](../observations.json)<br>source-1a3f2a4cf5331236024200f3.json<br>`/after_cold/totals` | [glm-5.3-flash-exl3](glm-5.3-flash-exl3.md) | context allocation | Outcome unspecified | cached_tokens=27,392 tokens; generated_tokens=1,357 accepted tokens; prompt_tokens=169,929 tokens; recurrent_restores=7 checkpoints | Recorded configuration/job |
| [result-78a47124df199460634e](../observations.json)<br>source-6c4907b44525431e880003f2.json<br>`/totals` | [glm-5.3-flash-exl3](glm-5.3-flash-exl3.md) | context allocation | Outcome unspecified | cached_tokens=0 tokens; generated_tokens=0 accepted tokens; prompt_tokens=0 tokens; recurrent_restores=0 checkpoints | Recorded configuration/job |
| [result-79ed691a2fb0347314a4](../observations.json)<br>source-d3d536389bbf245ede9ae53b.json<br>`/after_cold/cache` | [glm-5.3-flash-exl3](glm-5.3-flash-exl3.md) | test outcome | Outcome unspecified | cached_tokens=786,176 tokens | Recorded configuration/job |
| [result-7b5fe7f7cd1b5079f6a5](../observations.json)<br>source-84a296f9a57b3e4e910a7a5f.json<br>`/client_result` | [glm-5.3-flash-exl3](glm-5.3-flash-exl3.md) | test outcome | Outcome unspecified | elapsed_seconds=28.08 s | Recorded configuration/job |
| [result-7d70c9b88bfe816a5049](../observations.json)<br>source-1a75b76ac6d334615e55e710.json<br>`/completed_stages/1` | [glm-5.3-flash-exl3](glm-5.3-flash-exl3.md) | test outcome | Pass | replayed_history_tokens=26 tokens | Recorded configuration/job |
| [result-7e7ca04aebd1e6155e4f](../observations.json)<br>source-1a3f2a4cf5331236024200f3.json<br>`/after_cold/cache` | [glm-5.3-flash-exl3](glm-5.3-flash-exl3.md) | test outcome | Outcome unspecified | cached_tokens=141,056 tokens | Recorded configuration/job |
| [result-814b0315ed53ce09c239](../observations.json)<br>source-522af409c2158fc1893f37f6.json<br>`/after_cold/totals` | [glm-5.3-flash-exl3](glm-5.3-flash-exl3.md) | context allocation | Outcome unspecified | cached_tokens=289,536 tokens; generated_tokens=2,230 accepted tokens; prompt_tokens=957,585 tokens; recurrent_restores=15 checkpoints | Recorded configuration/job |
| [result-818e6868872cc94162f7](../observations.json)<br>source-2ab1817b31fc8a349fa7e4fb.json<br>`/stages/1/warm` | [glm-5.3-flash-exl3](glm-5.3-flash-exl3.md) | test outcome | Outcome unspecified | end_to_end_output_tps=16.97 accepted tokens/s; generated_tokens=79 accepted tokens; wall_seconds=4.66 s | Recorded configuration/job |
| [result-82726ce6d12b94cd1567](../observations.json)<br>source-84a296f9a57b3e4e910a7a5f.json<br>`/` | [glm-5.3-flash-exl3](glm-5.3-flash-exl3.md) | context allocation | Pass | compact_tokens=400,000 tokens; context_tokens=500,000 tokens | Recorded configuration/job |
| [result-83b46c3daf961c17a16d](../observations.json)<br>source-7a36e656ab72c34343821b7e.json<br>`/cache` | [glm-5.3-flash-exl3](glm-5.3-flash-exl3.md) | test outcome | Outcome unspecified | cached_tokens=0 tokens | Recorded configuration/job |
| [result-84a0e620fe6c673287c9](../observations.json)<br>source-d707ed443de5b0f6a93263f9.json<br>`/last_runtime` | [glm-5.3-flash-exl3](glm-5.3-flash-exl3.md) | test outcome | Outcome unspecified | context=500,000 tokens | Recorded configuration/job |
| [result-85ab439de9f80ed686e3](../observations.json)<br>source-946ea71503877f436b7cbf7d.json<br>`/after_cold/totals` | [glm-5.3-flash-exl3](glm-5.3-flash-exl3.md) | context allocation | Outcome unspecified | cached_tokens=4,799,232 tokens; generated_tokens=3,759 accepted tokens; prompt_tokens=6,746,363 tokens; recurrent_restores=63 checkpoints | Recorded configuration/job |
| [result-863ebab8656219cc6719](../observations.json)<br>source-1a75b76ac6d334615e55e710.json<br>`/completed_stages/2` | [glm-5.3-flash-exl3](glm-5.3-flash-exl3.md) | test outcome | Pass | replayed_history_tokens=164 tokens | Recorded configuration/job |
| [result-8aa956c5b2c3bb32bdef](../observations.json)<br>source-2ab1817b31fc8a349fa7e4fb.json<br>`/stages/0/warm` | [glm-5.3-flash-exl3](glm-5.3-flash-exl3.md) | test outcome | Outcome unspecified | end_to_end_output_tps=22.16 accepted tokens/s; generated_tokens=76 accepted tokens; wall_seconds=3.43 s | Recorded configuration/job |
| [result-8b782df65a3b99dad63a](../observations.json)<br>source-2ab1817b31fc8a349fa7e4fb.json<br>`/stages/2/cold` | [glm-5.3-flash-exl3](glm-5.3-flash-exl3.md) | test outcome | Outcome unspecified | end_to_end_output_tps=0.12 accepted tokens/s; generated_tokens=190 accepted tokens; wall_seconds=1,641.00 s | Recorded configuration/job |
| [result-8e255978ea7a9d7ffd29](../observations.json)<br>source-84a296f9a57b3e4e910a7a5f.json<br>`/client_result` | [glm-5.3-flash-exl3](glm-5.3-flash-exl3.md) | test outcome | Outcome unspecified | elapsed_seconds=18.55 s | Recorded configuration/job |
| [result-9c879ffdfbe52eef02e8](../observations.json)<br>source-84a296f9a57b3e4e910a7a5f.json<br>`/` | [glm-5.3-flash-exl3](glm-5.3-flash-exl3.md) | context allocation | Pass | compact_tokens=400,000 tokens; context_tokens=500,000 tokens | Recorded configuration/job |
| [result-a1e7cb84b43fafbe32e3](../observations.json)<br>source-1a3f2a4cf5331236024200f3.json<br>`/after_cold` | [glm-5.3-flash-exl3](glm-5.3-flash-exl3.md) | test outcome | Outcome unspecified | context=500,000 tokens | Recorded configuration/job |
| [result-a413dac91ab280f79dda](../observations.json)<br>source-53b47e140621dafd2d38e470.json<br>`/after_burst/totals` | [glm-5.3-flash-exl3](glm-5.3-flash-exl3.md) | context allocation | Outcome unspecified | cached_tokens=1,600,256 tokens; generated_tokens=3,523 accepted tokens; prompt_tokens=3,345,833 tokens; recurrent_restores=55 checkpoints | Recorded configuration/job |
| [result-a5b5c3c6f501c15f278f](../observations.json)<br>source-84a296f9a57b3e4e910a7a5f.json<br>`/verification` | [glm-5.3-flash-exl3](glm-5.3-flash-exl3.md) | test outcome | Outcome unspecified | elapsed_seconds=0.06 s | Recorded configuration/job |
| [result-a6311f68058879a5374a](../observations.json)<br>source-84a296f9a57b3e4e910a7a5f.json<br>`/verification` | [glm-5.3-flash-exl3](glm-5.3-flash-exl3.md) | test outcome | Outcome unspecified | elapsed_seconds=0.03 s | Recorded configuration/job |
| [result-a9026b476ceed60a970f](../observations.json)<br>source-53b47e140621dafd2d38e470.json<br>`/after_cold/totals` | [glm-5.3-flash-exl3](glm-5.3-flash-exl3.md) | context allocation | Outcome unspecified | cached_tokens=1,469,184 tokens; generated_tokens=3,011 accepted tokens; prompt_tokens=3,214,121 tokens; recurrent_restores=39 checkpoints | Recorded configuration/job |
| [result-ab9a5463cd001a56dd21](../observations.json)<br>source-2ab1817b31fc8a349fa7e4fb.json<br>`/stages/2/warm` | [glm-5.3-flash-exl3](glm-5.3-flash-exl3.md) | test outcome | Outcome unspecified | end_to_end_output_tps=3.44 accepted tokens/s; generated_tokens=76 accepted tokens; wall_seconds=22.08 s | Recorded configuration/job |
| [result-b085a354419cf3650e60](../observations.json)<br>source-522af409c2158fc1893f37f6.json<br>`/after_burst/cache` | [glm-5.3-flash-exl3](glm-5.3-flash-exl3.md) | test outcome | Outcome unspecified | cached_tokens=665,344 tokens | Recorded configuration/job |
| [result-b1aad92ed9e85a81e8e9](../observations.json)<br>source-039b2859b5f130fe8cb15859.json<br>`/cold/replicas/0/rates` | [glm-5.3-flash-exl3](glm-5.3-flash-exl3.md) | test outcome | Outcome unspecified | end_to_end_output_tps=20.85 accepted tokens/s; generated_tokens=512 accepted tokens; wall_seconds=24.56 s | Recorded configuration/job |
| [result-b6e48f2b470c9285bbab](../observations.json)<br>source-7a36e656ab72c34343821b7e.json<br>`/totals` | [glm-5.3-flash-exl3](glm-5.3-flash-exl3.md) | context allocation | Outcome unspecified | cached_tokens=0 tokens; generated_tokens=0 accepted tokens; prompt_tokens=0 tokens; recurrent_restores=0 checkpoints | Recorded configuration/job |
| [result-b8e804aacd29cf61d458](../observations.json)<br>source-84a296f9a57b3e4e910a7a5f.json<br>`/verification` | [glm-5.3-flash-exl3](glm-5.3-flash-exl3.md) | test outcome | Outcome unspecified | elapsed_seconds=0.06 s | Recorded configuration/job |
| [result-b9a4d2282a8ae5380999](../observations.json)<br>source-2ab1817b31fc8a349fa7e4fb.json<br>`/stages/3/warm` | [glm-5.3-flash-exl3](glm-5.3-flash-exl3.md) | test outcome | Outcome unspecified | end_to_end_output_tps=3.46 accepted tokens/s; generated_tokens=76 accepted tokens; wall_seconds=21.95 s | Recorded configuration/job |
| [result-bfd5e6894a365a4455dc](../observations.json)<br>source-522af409c2158fc1893f37f6.json<br>`/after_cold/cache` | [glm-5.3-flash-exl3](glm-5.3-flash-exl3.md) | test outcome | Outcome unspecified | cached_tokens=665,344 tokens | Recorded configuration/job |
| [result-c05ee09d79423e99d470](../observations.json)<br>source-d05be068bf31d093a1bb408e.json<br>`/cold/replicas/0/rates` | [glm-5.3-flash-exl3](glm-5.3-flash-exl3.md) | test outcome | Outcome unspecified | end_to_end_output_tps=22.32 accepted tokens/s; generated_tokens=1,024 accepted tokens; wall_seconds=45.88 s | Recorded configuration/job |
| [result-c22e38a0a6eed087865d](../observations.json)<br>source-2ab1817b31fc8a349fa7e4fb.json<br>`/stages/4` | [glm-5.3-flash-exl3](glm-5.3-flash-exl3.md) | test outcome | Pass | replayed_history_tokens=108 tokens | Recorded configuration/job |
| [result-c266e7f67acffdb74764](../observations.json)<br>source-d3d536389bbf245ede9ae53b.json<br>`/after_cold` | [glm-5.3-flash-exl3](glm-5.3-flash-exl3.md) | test outcome | Outcome unspecified | context=500,000 tokens | Recorded configuration/job |
| [result-c7b86aee90909d1e722d](../observations.json)<br>source-7a36e656ab72c34343821b7e.json<br>`/` | [glm-5.3-flash-exl3](glm-5.3-flash-exl3.md) | test outcome | Outcome unspecified | context=500,000 tokens | Recorded configuration/job |
| [result-cc53b0a81c8a8921ce36](../observations.json)<br>source-84a296f9a57b3e4e910a7a5f.json<br>`/` | [glm-5.3-flash-exl3](glm-5.3-flash-exl3.md) | context allocation | Pass | compact_tokens=400,000 tokens; context_tokens=500,000 tokens | Recorded configuration/job |
| [result-cca468471eab85cbf521](../observations.json)<br>source-d3d536389bbf245ede9ae53b.json<br>`/after_cold/totals` | [glm-5.3-flash-exl3](glm-5.3-flash-exl3.md) | context allocation | Outcome unspecified | cached_tokens=8,528,640 tokens; generated_tokens=4,661 accepted tokens; prompt_tokens=10,670,543 tokens; recurrent_restores=87 checkpoints | Recorded configuration/job |
| [result-ccdd7496d82528a224fc](../observations.json)<br>source-039b2859b5f130fe8cb15859.json<br>`/warm/replicas/0/rates` | [glm-5.3-flash-exl3](glm-5.3-flash-exl3.md) | test outcome | Outcome unspecified | end_to_end_output_tps=29.63 accepted tokens/s; generated_tokens=512 accepted tokens; wall_seconds=17.28 s | Recorded configuration/job |
| [result-cd7d8aa71c311ab93652](../observations.json)<br>source-d707ed443de5b0f6a93263f9.json<br>`/last_runtime/cache` | [glm-5.3-flash-exl3](glm-5.3-flash-exl3.md) | test outcome | Outcome unspecified | cached_tokens=785,920 tokens | Recorded configuration/job |
| [result-d8e03291eef7bc8c17d5](../observations.json)<br>source-946ea71503877f436b7cbf7d.json<br>`/after_cold` | [glm-5.3-flash-exl3](glm-5.3-flash-exl3.md) | test outcome | Outcome unspecified | context=500,000 tokens | Recorded configuration/job |
| [result-dd09a212a02e3ae765c5](../observations.json)<br>source-03f2fc195cdb3ad24acbf4fd.json<br>`/capacity/GLM_current_profiles/0` | [glm-5.3-flash-exl3](glm-5.3-flash-exl3.md) | context allocation | Outcome unspecified | pool=786,432 tokens | Exact configuration unresolved |
| [result-dec90c91ef7b95662fb0](../observations.json)<br>source-1a3f2a4cf5331236024200f3.json<br>`/after_burst/cache` | [glm-5.3-flash-exl3](glm-5.3-flash-exl3.md) | test outcome | Outcome unspecified | cached_tokens=272,128 tokens | Recorded configuration/job |
| [result-e4deeca8a44b6298bcbf](../observations.json)<br>source-d3d536389bbf245ede9ae53b.json<br>`/after_burst` | [glm-5.3-flash-exl3](glm-5.3-flash-exl3.md) | test outcome | Outcome unspecified | context=500,000 tokens | Recorded configuration/job |
| [result-e7d55f1c5aba540a94e9](../observations.json)<br>source-6c4907b44525431e880003f2.json<br>`/cache` | [glm-5.3-flash-exl3](glm-5.3-flash-exl3.md) | test outcome | Outcome unspecified | cached_tokens=0 tokens | Recorded configuration/job |
| [result-eb0a06436570641b8f84](../observations.json)<br>source-2ab1817b31fc8a349fa7e4fb.json<br>`/stages/4/cold` | [glm-5.3-flash-exl3](glm-5.3-flash-exl3.md) | test outcome | Outcome unspecified | end_to_end_output_tps=0.91 accepted tokens/s; generated_tokens=314 accepted tokens; wall_seconds=345.31 s | Recorded configuration/job |
| [result-ee0adb5fd9fc572abfb8](../observations.json)<br>source-d05be068bf31d093a1bb408e.json<br>`/warm/replicas/0/rates` | [glm-5.3-flash-exl3](glm-5.3-flash-exl3.md) | test outcome | Outcome unspecified | end_to_end_output_tps=44.29 accepted tokens/s; generated_tokens=1,024 accepted tokens; wall_seconds=23.12 s | Recorded configuration/job |
| [result-eec4b2736ed433790342](../observations.json)<br>source-1a75b76ac6d334615e55e710.json<br>`/completed_stages/4` | [glm-5.3-flash-exl3](glm-5.3-flash-exl3.md) | test outcome | Pass | replayed_history_tokens=108 tokens | Recorded configuration/job |
| [result-efe68f3ca5d383df6e97](../observations.json)<br>source-84a296f9a57b3e4e910a7a5f.json<br>`/client_result` | [glm-5.3-flash-exl3](glm-5.3-flash-exl3.md) | test outcome | Outcome unspecified | elapsed_seconds=26.38 s | Recorded configuration/job |
| [result-f348fa549b1888ccaffb](../observations.json)<br>source-53b47e140621dafd2d38e470.json<br>`/after_burst` | [glm-5.3-flash-exl3](glm-5.3-flash-exl3.md) | test outcome | Outcome unspecified | context=500,000 tokens | Recorded configuration/job |
| [result-f650633571e8f559d1f1](../observations.json)<br>source-946ea71503877f436b7cbf7d.json<br>`/after_cold/cache` | [glm-5.3-flash-exl3](glm-5.3-flash-exl3.md) | test outcome | Outcome unspecified | cached_tokens=786,176 tokens | Recorded configuration/job |
| [result-f68ab5c63021372f41c9](../observations.json)<br>source-1a3f2a4cf5331236024200f3.json<br>`/after_burst` | [glm-5.3-flash-exl3](glm-5.3-flash-exl3.md) | test outcome | Outcome unspecified | context=500,000 tokens | Recorded configuration/job |
| [result-fff19232c1d5e2a9630c](../observations.json)<br>source-ab89fca7e0f49696d5258b56.json<br>`/profiles/8/current_config` | [glm-5.3-flash-exl3](glm-5.3-flash-exl3.md) | context allocation | Outcome unspecified | cache_tokens=786,432 tokens; context=500,000 tokens; reserve_mib=1,024 MiB | Recorded configuration/job |

These are saved result records, including failures and bounded checks. Copies, individual requests, report summaries and regrading can overlap; their counts are not independent test repetitions. Open each result for exact values, units, configuration binding and source receipts.

There are 2 retained lifecycle records. Their states, exit codes and configuration IDs remain in [catalog.json](../catalog.json); they do not supply missing benchmark results.

[Full archive](../../README.md) | [All retained waves](../RESULTS.md) | [Data definitions](../DATA.md) | [Recommended recipes](../../../README.md)
