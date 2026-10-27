# glm53-capacity3-1250k

**Historical record. Decode interval measured.**

Model family: GLM 5.3 Flash.

Recorded archive reason: Historical capacity, fit or control configuration; later DFlash2 and MTP variants have separate records.

Historical configurations are provided for comparison. The [recommended recipes](../../../README.md) include supported launch scripts.

Current recipes using the same recorded checkpoint repository: [glm-5.3-flash-mtp1-tp3](../../../recipes/glm-5.3-flash-mtp1-tp3/README.md). Context, cache and runtime versions can differ.

## Saved Configuration Versions

Each configuration ID identifies a distinct original settings record. Deployment fields are omitted; versions can have identical published settings after that omission. Upstream runtime commits remain unspecified where the source retained only an integration label.

| Configuration | Recorded artifact / source | Configured card counts | Context tokens | GPU pool tokens | Slots | Draft mode / tokens |
| --- | --- | --- | --- | --- | --- | --- |
| cfg-2d5a12339db1cc4d6a6b | [turboderp/GLM-5.3-Flash-exl3@2a30229e67](https://huggingface.co/turboderp/GLM-5.3-Flash-exl3/tree/2a30229e67012798ba9f0cd832bb78abf4c363d5) | 3 | 500,000 | 1,310,720 | 8 | mtp / 1 |

Card counts are saved configuration choices, not a claim that every allowed placement was measured. A derived view can differ from its pinned download source.

<details>
<summary>cfg-2d5a12339db1cc4d6a6b</summary>

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
  "chunk_size": 512,
  "reserve_mib": 1664,
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

## Retained Measurements

| Profile / Wave | Layout; Draft / Tokens | Requests | Input tokens/request | Accepted output tokens/request | Cache / Reused input tokens | Context / GPU pool tokens | Shared decode tok/s total | Client after-first-token estimate tok/s | Whole-wave output tok/s | Median TTFT, s | Source report |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [glm53-capacity3-1250k](glm53-capacity3-1250k.md)<br>wave-05d80d757a5afdb22f3a | layout unspecified; mtp / 1 | 2 | 400,039 | 512 | cold; reused 399,872 | 500,000 / 1,310,720 | 42.44 | Not recorded | 36.07 | 3.36 | Pass |
| [glm53-capacity3-1250k](glm53-capacity3-1250k.md)<br>wave-2a057cc14e79d94dcdcd | layout unspecified; mtp / 1 | 4 | 400,039 | 39 to 68 | cold; reused 131,072 | 500,000 / 1,310,720 | Not recorded | Not recorded | 0.18 | 978.37 | Pass |
| [glm53-capacity3-1250k](glm53-capacity3-1250k.md)<br>wave-6104ee2f2b33b4d28c0a | layout unspecified; mtp / 1 | 4 | 32,803 | 70 to 98 | cold; reused 0 | 500,000 / 1,310,720 | Not recorded | Not recorded | 2.16 | 149.98 | Pass |
| [glm53-capacity3-1250k](glm53-capacity3-1250k.md)<br>wave-733a5ad5252726301e02 | layout unspecified; mtp / 1 | 4 | 400,087 to 400,116 | 19 | cached_prefix; reused 399,872 | 500,000 / 1,310,720 | Not recorded | Not recorded | 5.42 | 9.40 | Pass |
| [glm53-capacity3-1250k](glm53-capacity3-1250k.md)<br>wave-aa681765df93dfded5c6 | layout unspecified; mtp / 1 | 4 | 131,160 to 131,213 | 19 to 22 | cached_prefix; reused 131,072 | 500,000 / 1,310,720 | Not recorded | Not recorded | 18.85 | 3.47 | Pass |
| [glm53-capacity3-1250k](glm53-capacity3-1250k.md)<br>wave-abbcbfb7011a2a0b8b72 | layout unspecified; mtp / 1 | 4 | 131,101 | 128 | cold; reused 32,768 | 500,000 / 1,310,720 | Not recorded | Not recorded | 1.15 | 439.03 | Pass |
| [glm53-capacity3-1250k](glm53-capacity3-1250k.md)<br>wave-d837891d10cf16bcd1fd | layout unspecified; mtp / 1 | 4 | 32,882 to 32,910 | 19 | cached_prefix; reused 32,768 | 500,000 / 1,310,720 | Not recorded | Not recorded | 22.15 | 2.84 | Pass |
| [glm53-capacity3-1250k](glm53-capacity3-1250k.md)<br>wave-f94b541fb737bf7ed570 | layout unspecified; mtp / 1 | 2 | 400,562 to 400,564 | 512 | cached_prefix; reused 399,872 | 500,000 / 1,310,720 | 42.10 | Not recorded | 35.48 | 4.54 | Pass |

Rates are whole-wave totals over the stated request count. A wave may span multiple independent model instances; [measurements.json](../measurements.json) retains their contributions and the exact configuration IDs. Do not interpret a multi-instance total as one card's rate.

A dash in shared decode means no qualified synchronized interval is available. Whole-wave throughput includes prefill and queueing. A valid decode interval can survive inside an overall failed or partial check; the source-report outcome is preserved. No rows are averaged.

## Bounded Checks

| Check | Reported outcome | Retained counts / flags |
| --- | --- | --- |
| check-092910890bbffb9e06c0 | Pass | {"passed":true,"recurrent_restores":20,"restored_pages":5646} |
| check-1c639584d9bfe599ac9d | Pass | {"passed":true,"replayed_history_tokens":[29,29,29,29]} |
| check-200da827c8acacb620ae | Pass | {"passed":true,"input_tokens":[131099,131099,131099,131099],"replayed_history_tokens":[29,29,29,29],"extension_cached_tokens":[32768,32768,32768,32768]} |
| check-27cddbcc0ea06a7c0062 | Pass | {"passed":true,"replayed_history_tokens":[35,35,35,35]} |
| check-3b343eb2000077e736ef | Pass | {"passed":true,"replayed_history_tokens":[35,35,35,35],"input_tokens":[32801,32801,32801,32801]} |
| check-53912b381df9b5ba49d8 | Pass | {"passed":true,"replayed_history_tokens":[167,167,167,167]} |
| check-b07d07c050a5b50e0923 | Pass | {"passed":true,"input_tokens":[400037,400037,400037,400037],"replayed_history_tokens":[167,167,167,167],"extension_cached_tokens":[131072,131072,131072,131072]} |

These checks retain their reported scope. A context/allocation/retrieval check is not a general quality score or a speed qualification at that context. Exact flags and provenance are in [checks.json](../checks.json).

## Additional Test Results

| Result / Source | Profile | Evidence type | Reported outcome | Retained values | Configuration binding |
| --- | --- | --- | --- | --- | --- |
| [result-0fc4bc1f77feebeb1f9a](../observations.json)<br>source-a4296d565ac24c12ec01d02b.json<br>`/stages/1/cold` | [glm53-capacity3-1250k](glm53-capacity3-1250k.md) | test outcome | Outcome unspecified | end_to_end_output_tps=1.15 accepted tokens/s; generated_tokens=512 accepted tokens; wall_seconds=446.84 s | Recorded configuration/job |
| [result-1afeeb3d3f2f8fad384e](../observations.json)<br>source-18880a944b6f446efc6763c6.json<br>`/warm/replicas/0/rates` | [glm53-capacity3-1250k](glm53-capacity3-1250k.md) | test outcome | Outcome unspecified | end_to_end_output_tps=35.48 accepted tokens/s; generated_tokens=1,024 accepted tokens; wall_seconds=28.86 s | Recorded configuration/job |
| [result-2386c9aa346aa42f7d4d](../observations.json)<br>source-854fa218737b222d85d22c08.json<br>`/after_cold/totals` | [glm53-capacity3-1250k](glm53-capacity3-1250k.md) | context allocation | Outcome unspecified | cached_tokens=262,144 tokens; generated_tokens=1,306 accepted tokens; prompt_tokens=836,770 tokens; recurrent_restores=8 checkpoints | Recorded configuration/job |
| [result-2555a66c4fa2552b8c96](../observations.json)<br>source-4b47b5a3558d3a343a7db4c9.json<br>`/after_cold/totals` | [glm53-capacity3-1250k](glm53-capacity3-1250k.md) | context allocation | Outcome unspecified | cached_tokens=0 tokens; generated_tokens=334 accepted tokens; prompt_tokens=131,212 tokens; recurrent_restores=0 checkpoints | Recorded configuration/job |
| [result-2a64c5a565835f26cd90](../observations.json)<br>source-a4296d565ac24c12ec01d02b.json<br>`/stages/0` | [glm53-capacity3-1250k](glm53-capacity3-1250k.md) | test outcome | Pass | replayed_history_tokens=35 tokens | Recorded configuration/job |
| [result-2d9b8704a8fb5361007f](../observations.json)<br>source-a4296d565ac24c12ec01d02b.json<br>`/stages/0/cold` | [glm53-capacity3-1250k](glm53-capacity3-1250k.md) | test outcome | Outcome unspecified | end_to_end_output_tps=2.16 accepted tokens/s; generated_tokens=334 accepted tokens; wall_seconds=154.91 s | Recorded configuration/job |
| [result-3ddd9b7fc09a70470dae](../observations.json)<br>source-a4296d565ac24c12ec01d02b.json<br>`/stages/2/warm` | [glm53-capacity3-1250k](glm53-capacity3-1250k.md) | test outcome | Outcome unspecified | end_to_end_output_tps=5.42 accepted tokens/s; generated_tokens=76 accepted tokens; wall_seconds=14.03 s | Recorded configuration/job |
| [result-4224fe3b2b0fc64106b0](../observations.json)<br>source-a4296d565ac24c12ec01d02b.json<br>`/stages/0/warm` | [glm53-capacity3-1250k](glm53-capacity3-1250k.md) | test outcome | Outcome unspecified | end_to_end_output_tps=22.15 accepted tokens/s; generated_tokens=76 accepted tokens; wall_seconds=3.43 s | Recorded configuration/job |
| [result-4b82e11b7f3caaabcf33](../observations.json)<br>source-a4296d565ac24c12ec01d02b.json<br>`/stages/1` | [glm53-capacity3-1250k](glm53-capacity3-1250k.md) | test outcome | Pass | replayed_history_tokens=29 tokens | Recorded configuration/job |
| [result-50c2f887df70ef1728f1](../observations.json)<br>source-4b47b5a3558d3a343a7db4c9.json<br>`/after_burst/totals` | [glm53-capacity3-1250k](glm53-capacity3-1250k.md) | context allocation | Outcome unspecified | cached_tokens=0 tokens; generated_tokens=718 accepted tokens; prompt_tokens=180,784 tokens; recurrent_restores=0 checkpoints | Recorded configuration/job |
| [result-6202303f4d2a34303892](../observations.json)<br>source-854fa218737b222d85d22c08.json<br>`/after_burst` | [glm53-capacity3-1250k](glm53-capacity3-1250k.md) | test outcome | Outcome unspecified | context=500,000 tokens | Recorded configuration/job |
| [result-673fb760fba09c6200ec](../observations.json)<br>source-a4296d565ac24c12ec01d02b.json<br>`/stages/1/warm` | [glm53-capacity3-1250k](glm53-capacity3-1250k.md) | test outcome | Outcome unspecified | end_to_end_output_tps=18.85 accepted tokens/s; generated_tokens=79 accepted tokens; wall_seconds=4.19 s | Recorded configuration/job |
| [result-676673aae636ab0de47c](../observations.json)<br>source-a4296d565ac24c12ec01d02b.json<br>`/stages/2` | [glm53-capacity3-1250k](glm53-capacity3-1250k.md) | test outcome | Pass | replayed_history_tokens=167 tokens | Recorded configuration/job |
| [result-69b1357240735c4ad0b4](../observations.json)<br>source-854fa218737b222d85d22c08.json<br>`/after_burst/totals` | [glm53-capacity3-1250k](glm53-capacity3-1250k.md) | context allocation | Outcome unspecified | cached_tokens=311,296 tokens; generated_tokens=1,690 accepted tokens; prompt_tokens=886,342 tokens; recurrent_restores=20 checkpoints | Recorded configuration/job |
| [result-6ffbcb3fd95dca858ec4](../observations.json)<br>source-a165b509277a308464f66e68.json<br>`/after_cold` | [glm53-capacity3-1250k](glm53-capacity3-1250k.md) | test outcome | Outcome unspecified | context=500,000 tokens | Recorded configuration/job |
| [result-7586fa7f35019403ce82](../observations.json)<br>source-18880a944b6f446efc6763c6.json<br>`/cold/replicas/0/rates` | [glm53-capacity3-1250k](glm53-capacity3-1250k.md) | test outcome | Outcome unspecified | end_to_end_output_tps=36.07 accepted tokens/s; generated_tokens=1,024 accepted tokens; wall_seconds=28.39 s | Recorded configuration/job |
| [result-7807335fae2cc4b269d6](../observations.json)<br>source-854fa218737b222d85d22c08.json<br>`/after_cold/cache` | [glm53-capacity3-1250k](glm53-capacity3-1250k.md) | test outcome | Outcome unspecified | cached_tokens=573,440 tokens | Recorded configuration/job |
| [result-782c9932b041ef671be8](../observations.json)<br>source-a4296d565ac24c12ec01d02b.json<br>`/` | [glm53-capacity3-1250k](glm53-capacity3-1250k.md) | context allocation | Pass | recurrent_restores=20 checkpoints; restored_pages=5,646 pages | Recorded configuration/job |
| [result-79c899f02e546d20c1b9](../observations.json)<br>source-4b47b5a3558d3a343a7db4c9.json<br>`/after_burst` | [glm53-capacity3-1250k](glm53-capacity3-1250k.md) | test outcome | Outcome unspecified | context=500,000 tokens | Recorded configuration/job |
| [result-7ea7395aa596f65f8e7f](../observations.json)<br>source-4b47b5a3558d3a343a7db4c9.json<br>`/after_cold/cache` | [glm53-capacity3-1250k](glm53-capacity3-1250k.md) | test outcome | Outcome unspecified | cached_tokens=131,072 tokens | Recorded configuration/job |
| [result-a2ad8f0d2ebe922aa147](../observations.json)<br>source-a4296d565ac24c12ec01d02b.json<br>`/stages/2/cold` | [glm53-capacity3-1250k](glm53-capacity3-1250k.md) | test outcome | Outcome unspecified | end_to_end_output_tps=0.18 accepted tokens/s; generated_tokens=233 accepted tokens; wall_seconds=1,309.27 s | Recorded configuration/job |
| [result-afe69bd4678cd973d385](../observations.json)<br>source-4b47b5a3558d3a343a7db4c9.json<br>`/after_burst/cache` | [glm53-capacity3-1250k](glm53-capacity3-1250k.md) | test outcome | Outcome unspecified | cached_tokens=180,224 tokens | Recorded configuration/job |
| [result-bc400beb23f876928a99](../observations.json)<br>source-a165b509277a308464f66e68.json<br>`/after_cold/cache` | [glm53-capacity3-1250k](glm53-capacity3-1250k.md) | test outcome | Outcome unspecified | cached_tokens=1,307,392 tokens | Recorded configuration/job |
| [result-cc8b982f742d01d2bc59](../observations.json)<br>source-854fa218737b222d85d22c08.json<br>`/after_cold` | [glm53-capacity3-1250k](glm53-capacity3-1250k.md) | test outcome | Outcome unspecified | context=500,000 tokens | Recorded configuration/job |
| [result-d32a9464627e3d21595c](../observations.json)<br>source-a165b509277a308464f66e68.json<br>`/after_burst` | [glm53-capacity3-1250k](glm53-capacity3-1250k.md) | test outcome | Outcome unspecified | context=500,000 tokens | Recorded configuration/job |
| [result-e543d1527ad673ad86f2](../observations.json)<br>source-a165b509277a308464f66e68.json<br>`/after_burst/totals` | [glm53-capacity3-1250k](glm53-capacity3-1250k.md) | context allocation | Outcome unspecified | cached_tokens=1,409,024 tokens; generated_tokens=2,386 accepted tokens; prompt_tokens=3,060,869 tokens; recurrent_restores=40 checkpoints | Recorded configuration/job |
| [result-e9689c73bf94e7835d74](../observations.json)<br>source-a165b509277a308464f66e68.json<br>`/after_cold/totals` | [glm53-capacity3-1250k](glm53-capacity3-1250k.md) | context allocation | Outcome unspecified | cached_tokens=1,359,872 tokens; generated_tokens=2,002 accepted tokens; prompt_tokens=3,011,297 tokens; recurrent_restores=28 checkpoints | Recorded configuration/job |
| [result-fab9e7df2bda76ad6f97](../observations.json)<br>source-854fa218737b222d85d22c08.json<br>`/after_burst/cache` | [glm53-capacity3-1250k](glm53-capacity3-1250k.md) | test outcome | Outcome unspecified | cached_tokens=573,440 tokens | Recorded configuration/job |
| [result-fadd1ca86a33099336a3](../observations.json)<br>source-4b47b5a3558d3a343a7db4c9.json<br>`/after_cold` | [glm53-capacity3-1250k](glm53-capacity3-1250k.md) | test outcome | Outcome unspecified | context=500,000 tokens | Recorded configuration/job |
| [result-fee00174dd0a2545a6ab](../observations.json)<br>source-a165b509277a308464f66e68.json<br>`/after_burst/cache` | [glm53-capacity3-1250k](glm53-capacity3-1250k.md) | test outcome | Outcome unspecified | cached_tokens=1,304,832 tokens | Recorded configuration/job |

These are saved result records, including failures and bounded checks. Copies, individual requests, report summaries and regrading can overlap; their counts are not independent test repetitions. Open each result for exact values, units, configuration binding and source receipts.

There are 1 retained lifecycle records. Their states, exit codes and configuration IDs remain in [catalog.json](../catalog.json); they do not supply missing benchmark results.

[Full archive](../../README.md) | [All retained waves](../RESULTS.md) | [Data definitions](../DATA.md) | [Recommended recipes](../../../README.md)
