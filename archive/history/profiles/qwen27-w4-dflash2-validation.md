# qwen27-w4-dflash2-validation

**Historical record. Bounded checks only.**

Model family: Qwen 3.8 27B.

Historical configurations are provided for comparison. The [recommended recipes](../../../README.md) include supported launch scripts.

## Saved Configuration Versions

Each configuration ID identifies a distinct original settings record. Deployment fields are omitted; versions can have identical published settings after that omission. Upstream runtime commits remain unspecified where the source retained only an integration label.

| Configuration | Recorded artifact / source | Configured card counts | Context tokens | GPU pool tokens | Slots | Draft mode / tokens |
| --- | --- | --- | --- | --- | --- | --- |
| cfg-1dff26cc2d108ff54063 | [dbirks/Qwen3.8-27B-W4A16-AutoRound@1f05c441c4](https://huggingface.co/dbirks/Qwen3.8-27B-W4A16-AutoRound/tree/1f05c441c4e64ae0549de44fa9ea5a6d43610314) | 3 | 32,768 | Not recorded | 4 | dflash2 / 7 |
| cfg-a8ef24ac757a5b5ace48 | [dbirks/Qwen3.8-27B-W4A16-AutoRound@1f05c441c4](https://huggingface.co/dbirks/Qwen3.8-27B-W4A16-AutoRound/tree/1f05c441c4e64ae0549de44fa9ea5a6d43610314) | 3 | 32,768 | Not recorded | 4 | dflash2 / 7 |
| cfg-e07f082653972e37858d | [dbirks/Qwen3.8-27B-W4A16-AutoRound@1f05c441c4](https://huggingface.co/dbirks/Qwen3.8-27B-W4A16-AutoRound/tree/1f05c441c4e64ae0549de44fa9ea5a6d43610314) | 3 | 32,768 | Not recorded | 4 | dflash2 / 7 |

Card counts are saved configuration choices, not a claim that every allowed placement was measured. A derived view can differ from its pinned download source.

<details>
<summary>cfg-1dff26cc2d108ff54063</summary>

```json
{
  "kind": "vllm_qwen27",
  "gpu_counts": [
    3
  ],
  "context": 32768,
  "kv_dtype": "bfloat16",
  "draft_mode": "dflash2",
  "draft_tokens": 7,
  "max_sessions": 4,
  "chunk_size": 1024,
  "ram_kv_mib": 8192,
  "power_watts": 200,
  "host_memory_gib": 80,
  "host_swap_gib": 0,
  "min_vram_mib_per_gpu": 65530,
  "min_effective_vram_mib": 196000,
  "tensor_parallel_size": 1,
  "pipeline_parallel_size": 1,
  "kv_cache_mib_per_gpu": 4096,
  "enforce_eager": true,
  "mamba_cache_mode": "align",
  "model_repository": "dbirks/Qwen3.8-27B-W4A16-AutoRound",
  "model_revision": "1f05c441c4e64ae0549de44fa9ea5a6d43610314",
  "draft_repository": null,
  "draft_revision": "4d30ec736ffc6b8688dc2ae2b502d9b48bdec279",
  "recorded_runtime_label": "qwen27-vllm-r1",
  "served_model_label": "qwen3.8-27b"
}
```

Pinned model revision recorded: yes. Source receipt labels, hashes and object locators are retained in [configurations.json](../configurations.json).

</details>

<details>
<summary>cfg-a8ef24ac757a5b5ace48</summary>

```json
{
  "kind": "vllm_qwen27",
  "gpu_counts": [
    3
  ],
  "context": 32768,
  "kv_dtype": "bfloat16",
  "draft_mode": "dflash2",
  "draft_tokens": 7,
  "max_sessions": 4,
  "chunk_size": 512,
  "ram_kv_mib": 8192,
  "power_watts": 200,
  "host_memory_gib": 80,
  "host_swap_gib": 0,
  "min_vram_mib_per_gpu": 65530,
  "min_effective_vram_mib": 196000,
  "tensor_parallel_size": 1,
  "pipeline_parallel_size": 1,
  "kv_cache_mib_per_gpu": 4096,
  "enforce_eager": true,
  "mamba_cache_mode": "align",
  "model_repository": "dbirks/Qwen3.8-27B-W4A16-AutoRound",
  "model_revision": "1f05c441c4e64ae0549de44fa9ea5a6d43610314",
  "draft_repository": null,
  "draft_revision": "4d30ec736ffc6b8688dc2ae2b502d9b48bdec279",
  "recorded_runtime_label": "qwen27-vllm-r1",
  "served_model_label": "qwen3.8-27b"
}
```

Pinned model revision recorded: yes. Source receipt labels, hashes and object locators are retained in [configurations.json](../configurations.json).

</details>

<details>
<summary>cfg-e07f082653972e37858d</summary>

```json
{
  "kind": "vllm_qwen27",
  "gpu_counts": [
    3
  ],
  "context": 32768,
  "kv_dtype": "bfloat16",
  "draft_mode": "dflash2",
  "draft_tokens": 7,
  "max_sessions": 4,
  "chunk_size": 512,
  "ram_kv_mib": 8192,
  "power_watts": 200,
  "host_memory_gib": 80,
  "host_swap_gib": 0,
  "min_vram_mib_per_gpu": 65530,
  "min_effective_vram_mib": 196000,
  "tensor_parallel_size": 1,
  "pipeline_parallel_size": 1,
  "kv_cache_mib_per_gpu": 4096,
  "enforce_eager": true,
  "mamba_cache_mode": "align",
  "model_repository": "dbirks/Qwen3.8-27B-W4A16-AutoRound",
  "model_revision": "1f05c441c4e64ae0549de44fa9ea5a6d43610314",
  "draft_repository": null,
  "draft_revision": "4d30ec736ffc6b8688dc2ae2b502d9b48bdec279",
  "recorded_runtime_label": "qwen27-vllm-r1",
  "served_model_label": "qwen3.8-27b"
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
| check-00684a551ab0260b6f2c | Failed / partial | {"passed":false,"ram_restoration_qualified":false} |
| check-21ef2cc98ff81b5b7291 | Failed / partial | {"passed":false,"input_tokens":[8195,8195]} |
| check-365abe81d689528e826f | Failed / partial | {"passed":false,"ram_restoration_qualified":false} |
| check-3fcd22cc3fc9f1ae929d | Failed / partial | {"passed":false,"ram_restoration_qualified":false} |
| check-49c46ff72b0d872eda60 | Failed / partial | {"passed":false,"ram_restoration_qualified":false} |
| check-62f6de46352909ea8c11 | Failed / partial | {"passed":false,"ram_restoration_qualified":false} |
| check-7aa97aa2ab7cc1390d49 | Failed / partial | {"passed":false,"ram_restoration_qualified":false} |
| check-abb2beb05cf7c9e16f74 | Pass | {"passed":true,"ram_restoration_qualified":true} |
| check-b66f9d1c1656bd359474 | Failed / partial | {"passed":false,"ram_restoration_qualified":false} |
| check-d68f59b1f266a3953cc6 | Failed / partial | {"passed":false,"ram_restoration_qualified":false} |
| check-ed4fde62a63e0d4d5e2f | Failed / partial | {"passed":false,"ram_restoration_qualified":false} |
| check-f9c8efdbcc2ec6ad96b8 | Failed / partial | {"passed":false,"ram_restoration_qualified":false} |

These checks retain their reported scope. A context/allocation/retrieval check is not a general quality score or a speed qualification at that context. Exact flags and provenance are in [checks.json](../checks.json).

## Additional Test Results

| Result / Source | Profile | Evidence type | Reported outcome | Retained values | Configuration binding |
| --- | --- | --- | --- | --- | --- |
| [result-0732b3613659561ea5c2](../observations.json)<br>source-a444806d1e3702ecb24f8598.json<br>`/stages/0/initial_requests/0` | [qwen27-w4-dflash2-validation](qwen27-w4-dflash2-validation.md) | performance detail | Outcome unspecified | wall_seconds=4.60 s | Recorded configuration/job |
| [result-0cae6d71777559225cc2](../observations.json)<br>source-8e1cf7d0cfceaf592806034b.json<br>`/jobs/2` | [qwen27-w4-dflash2-validation](qwen27-w4-dflash2-validation.md) | test outcome | Failed / partial | passed=false | Recorded configuration/job |
| [result-0e091d7285858311a171](../observations.json)<br>source-92c561913d9584212dc4ba07.json<br>`/phases/1` | [qwen27-w4-dflash2-validation](qwen27-w4-dflash2-validation.md) | test outcome | Failed / partial | passed=false | Recorded configuration/job |
| [result-15fac1fc203d71c748a3](../observations.json)<br>source-ee68f18b6bbcc948547010e4.json<br>`/` | [qwen27-w4-dflash2-validation](qwen27-w4-dflash2-validation.md) | test outcome | Failed / partial | ram_restoration_qualified=false | Recorded configuration/job |
| [result-1c136c4a3240558dd607](../observations.json)<br>source-a444806d1e3702ecb24f8598.json<br>`/stages/0/returning_requests/1` | [qwen27-w4-dflash2-validation](qwen27-w4-dflash2-validation.md) | performance detail | Outcome unspecified | wall_seconds=4.65 s | Recorded configuration/job |
| [result-1c8b688ea78b1b5f5ed4](../observations.json)<br>source-750c687592065f3cd14d3521.json<br>`/jobs/0` | [qwen27-w4-dflash2-validation](qwen27-w4-dflash2-validation.md) | test outcome | Failed / partial | passed=false | Recorded configuration/job |
| [result-23970ea4eb50555b54c2](../observations.json)<br>source-e433d17e17c7d96a17cdc90b.json<br>`/phases/1` | [qwen27-w4-dflash2-validation](qwen27-w4-dflash2-validation.md) | test outcome | Failed / partial | passed=false | Recorded configuration/job |
| [result-2728e6034749da0f0c85](../observations.json)<br>source-46c744708c934ef7375d911c.json<br>`/events/35` | [qwen27-w4-dflash2-validation](qwen27-w4-dflash2-validation.md) | test outcome | Outcome unspecified | prompt_tokens=8,195 tokens | Recorded configuration/job |
| [result-281e74b1a7099f0d0409](../observations.json)<br>source-06717a78cf528078f4e40019.json<br>`/phases/1` | [qwen27-w4-dflash2-validation](qwen27-w4-dflash2-validation.md) | test outcome | Failed / partial | passed=false | Recorded configuration/job |
| [result-2bb8b4075bd8b1f8e574](../observations.json)<br>source-a444806d1e3702ecb24f8598.json<br>`/stages/0/serial_initial_cache_evidence/1` | [qwen27-w4-dflash2-validation](qwen27-w4-dflash2-validation.md) | test outcome | Outcome unspecified | cached_tokens=0 tokens | Recorded configuration/job |
| [result-342f403e05ab1e804123](../observations.json)<br>source-b19ca7ac4b1035623af43ee5.json<br>`/` | [qwen27-w4-dflash2-validation](qwen27-w4-dflash2-validation.md) | test outcome | Failed / partial | ram_restoration_qualified=false | Recorded configuration/job |
| [result-39165cb0c3ec311f8597](../observations.json)<br>source-46c744708c934ef7375d911c.json<br>`/events/64` | [qwen27-w4-dflash2-validation](qwen27-w4-dflash2-validation.md) | test outcome | Outcome unspecified | prompt_tokens=16,391 tokens | Recorded configuration/job |
| [result-39e8c1066a41a59fdfdd](../observations.json)<br>source-a444806d1e3702ecb24f8598.json<br>`/stages/0` | [qwen27-w4-dflash2-validation](qwen27-w4-dflash2-validation.md) | performance detail | Failed / partial | input_tokens=8,195 tokens; burst: 3 requests | Recorded configuration/job |
| [result-3bd92bac1b21bd051f52](../observations.json)<br>source-46c744708c934ef7375d911c.json<br>`/events/0` | [qwen27-w4-dflash2-validation](qwen27-w4-dflash2-validation.md) | test outcome | Outcome unspecified | prompt_tokens=79 tokens | Recorded configuration/job |
| [result-3ed5a1aa8e61b63ac574](../observations.json)<br>source-c0031b8cc3011894b9cbb285.json<br>`/jobs/1` | [qwen27-w4-dflash2-validation](qwen27-w4-dflash2-validation.md) | test outcome | Failed / partial | passed=false | Recorded configuration/job |
| [result-3fb72a58025c19cfde0a](../observations.json)<br>source-ee68f18b6bbcc948547010e4.json<br>`/phases/1` | [qwen27-w4-dflash2-validation](qwen27-w4-dflash2-validation.md) | test outcome | Failed / partial | passed=false | Recorded configuration/job |
| [result-430d710dca8766614d11](../observations.json)<br>source-4febb349da9061c564a28751.json<br>`/jobs/1` | [qwen27-w4-dflash2-validation](qwen27-w4-dflash2-validation.md) | test outcome | Failed / partial | passed=false | Recorded configuration/job |
| [result-458d9a77f44d20a77d2c](../observations.json)<br>source-7a4dfa740ccf61567eeb9507.json<br>`/` | [qwen27-w4-dflash2-validation](qwen27-w4-dflash2-validation.md) | test outcome | Outcome unspecified | stored_bytes_before_return=4,883,873,792 bytes | Recorded configuration/job |
| [result-468043a46406b861c008](../observations.json)<br>source-d377699ffb803509d619c845.json<br>`/` | [qwen27-w4-dflash2-validation](qwen27-w4-dflash2-validation.md) | test outcome | Failed / partial | ram_restoration_qualified=false | Recorded configuration/job |
| [result-482cada66584c5562d0b](../observations.json)<br>source-46c744708c934ef7375d911c.json<br>`/events/67` | [qwen27-w4-dflash2-validation](qwen27-w4-dflash2-validation.md) | test outcome | Outcome unspecified | prompt_tokens=16,391 tokens | Recorded configuration/job |
| [result-51dc2369e85f2bcf9e4f](../observations.json)<br>source-a444806d1e3702ecb24f8598.json<br>`/stages/0/returning_requests/0` | [qwen27-w4-dflash2-validation](qwen27-w4-dflash2-validation.md) | performance detail | Outcome unspecified | wall_seconds=4.65 s | Recorded configuration/job |
| [result-5392d2396ab781524176](../observations.json)<br>source-46c744708c934ef7375d911c.json<br>`/events/1` | [qwen27-w4-dflash2-validation](qwen27-w4-dflash2-validation.md) | test outcome | Outcome unspecified | prompt_tokens=72 tokens | Recorded configuration/job |
| [result-5f1906d51e9851a94de2](../observations.json)<br>source-3b022f98ca9d928a0638f615.json<br>`/jobs/0` | [qwen27-w4-dflash2-validation](qwen27-w4-dflash2-validation.md) | test outcome | Failed / partial | passed=false | Recorded configuration/job |
| [result-6b59547ff026c23aedc4](../observations.json)<br>source-a444806d1e3702ecb24f8598.json<br>`/pressure_budget` | [qwen27-w4-dflash2-validation](qwen27-w4-dflash2-validation.md) | test outcome | Outcome unspecified | reported_gpu_pool_tokens=38,922 tokens | Recorded configuration/job |
| [result-6b8f4b45a20317f6b1ca](../observations.json)<br>source-b19ca7ac4b1035623af43ee5.json<br>`/phases/1` | [qwen27-w4-dflash2-validation](qwen27-w4-dflash2-validation.md) | test outcome | Failed / partial | passed=false | Recorded configuration/job |
| [result-6ecce2f47c6699adbb64](../observations.json)<br>source-d7144ac254cdb912158f6e59.json<br>`/jobs/0` | [qwen27-w4-dflash2-validation](qwen27-w4-dflash2-validation.md) | test outcome | Failed / partial | passed=false | Recorded configuration/job |
| [result-74ac3ad4fc58bcc1f16c](../observations.json)<br>source-f5399affe86a12ad72a00b75.json<br>`/jobs/0` | [qwen27-w4-dflash2-validation](qwen27-w4-dflash2-validation.md) | test outcome | Failed / partial | passed=false | Recorded configuration/job |
| [result-7b04b2ce98f806c192f3](../observations.json)<br>source-a444806d1e3702ecb24f8598.json<br>`/stages/0/initial_requests/1` | [qwen27-w4-dflash2-validation](qwen27-w4-dflash2-validation.md) | performance detail | Outcome unspecified | wall_seconds=4.57 s | Recorded configuration/job |
| [result-95365b7e7e545dbc7a1b](../observations.json)<br>source-a444806d1e3702ecb24f8598.json<br>`/` | [qwen27-w4-dflash2-validation](qwen27-w4-dflash2-validation.md) | test outcome | Failed / partial | ram_restoration_qualified=false | Recorded configuration/job |
| [result-a0af77c1cd7f019a1815](../observations.json)<br>source-e67f5fbc62c34d1a0cc2044d.json<br>`/` | [qwen27-w4-dflash2-validation](qwen27-w4-dflash2-validation.md) | test outcome | Failed / partial | ram_restoration_qualified=false | Recorded configuration/job |
| [result-a187b5179d692a03e6a1](../observations.json)<br>source-06717a78cf528078f4e40019.json<br>`/` | [qwen27-w4-dflash2-validation](qwen27-w4-dflash2-validation.md) | test outcome | Failed / partial | ram_restoration_qualified=false | Recorded configuration/job |
| [result-a8e088a68a0f9ca0e0c6](../observations.json)<br>source-de20770270f31598d5708c73.json<br>`/` | [qwen27-w4-dflash2-validation](qwen27-w4-dflash2-validation.md) | test outcome | Failed / partial | ram_restoration_qualified=false | Recorded configuration/job |
| [result-ae599dc429e0524609e2](../observations.json)<br>source-a444806d1e3702ecb24f8598.json<br>`/stages/0/initial_requests/0/accepted_token_evidence` | [qwen27-w4-dflash2-validation](qwen27-w4-dflash2-validation.md) | test outcome | complete | See exact JSON for retained flags and timers | Recorded configuration/job |
| [result-b28c53878f49a7861ce2](../observations.json)<br>source-e67f5fbc62c34d1a0cc2044d.json<br>`/phases/1` | [qwen27-w4-dflash2-validation](qwen27-w4-dflash2-validation.md) | test outcome | Failed / partial | passed=false | Recorded configuration/job |
| [result-b43a5a41a8583faee471](../observations.json)<br>source-7a4dfa740ccf61567eeb9507.json<br>`/return_lookups/1` | [qwen27-w4-dflash2-validation](qwen27-w4-dflash2-validation.md) | test outcome | Outcome unspecified | prompt_tokens=8,217 tokens | Recorded configuration/job |
| [result-be057d07c2ac9c903f21](../observations.json)<br>source-590e959afe87fd30b87aece9.json<br>`/` | [qwen27-w4-dflash2-validation](qwen27-w4-dflash2-validation.md) | test outcome | Pass | passed=true; ram_restoration_qualified=true | Recorded configuration/job |
| [result-bf0d047e26c799be8c37](../observations.json)<br>source-46c744708c934ef7375d911c.json<br>`/events/4` | [qwen27-w4-dflash2-validation](qwen27-w4-dflash2-validation.md) | test outcome | Outcome unspecified | prompt_tokens=404 tokens | Recorded configuration/job |
| [result-c7c1b97fb0a03a9d07c5](../observations.json)<br>source-de20770270f31598d5708c73.json<br>`/phases/1` | [qwen27-w4-dflash2-validation](qwen27-w4-dflash2-validation.md) | test outcome | Failed / partial | passed=false | Recorded configuration/job |
| [result-c81e196b077b0d6110ec](../observations.json)<br>source-46c744708c934ef7375d911c.json<br>`/events/2` | [qwen27-w4-dflash2-validation](qwen27-w4-dflash2-validation.md) | test outcome | Outcome unspecified | prompt_tokens=88 tokens | Recorded configuration/job |
| [result-cbb3684bca5bbaeb12df](../observations.json)<br>source-92c561913d9584212dc4ba07.json<br>`/` | [qwen27-w4-dflash2-validation](qwen27-w4-dflash2-validation.md) | test outcome | Failed / partial | ram_restoration_qualified=false | Recorded configuration/job |
| [result-d2bdd0626b9e1b848450](../observations.json)<br>source-7a4dfa740ccf61567eeb9507.json<br>`/return_lookups/0` | [qwen27-w4-dflash2-validation](qwen27-w4-dflash2-validation.md) | test outcome | Outcome unspecified | prompt_tokens=8,217 tokens | Recorded configuration/job |
| [result-d4062ce73a82ac8f92c0](../observations.json)<br>source-e433d17e17c7d96a17cdc90b.json<br>`/` | [qwen27-w4-dflash2-validation](qwen27-w4-dflash2-validation.md) | test outcome | Failed / partial | ram_restoration_qualified=false | Recorded configuration/job |
| [result-d5bbb28a472fafa2be0d](../observations.json)<br>source-b61a20fde780f4bf7bdb6fe6.json<br>`/phases/0` | [qwen27-w4-dflash2-validation](qwen27-w4-dflash2-validation.md) | test outcome | Failed / partial | passed=false | Recorded configuration/job |
| [result-d8cf50f35b50dc3c4087](../observations.json)<br>source-04c515f1e5e901072b7e9f76.json<br>`/jobs/0` | [qwen27-w4-dflash2-validation](qwen27-w4-dflash2-validation.md) | test outcome | Failed / partial | passed=false | Recorded configuration/job |
| [result-dbc9b69973b48847aa18](../observations.json)<br>source-153b916e74eb61dfe8262b94.json<br>`/` | [qwen27-w4-dflash2-validation](qwen27-w4-dflash2-validation.md) | performance detail | Pass | cases: 3 requests | Recorded configuration/job |
| [result-ddaeb54d1e28a5b4b9c2](../observations.json)<br>source-a444806d1e3702ecb24f8598.json<br>`/stages/0/serial_return_cache_evidence/1` | [qwen27-w4-dflash2-validation](qwen27-w4-dflash2-validation.md) | test outcome | Outcome unspecified | cached_tokens=0 tokens | Recorded configuration/job |
| [result-e023bed6d1ecdda707ff](../observations.json)<br>source-46c744708c934ef7375d911c.json<br>`/events/3` | [qwen27-w4-dflash2-validation](qwen27-w4-dflash2-validation.md) | test outcome | Outcome unspecified | prompt_tokens=347 tokens | Recorded configuration/job |
| [result-e1f56cf968644e3ef15f](../observations.json)<br>source-a444806d1e3702ecb24f8598.json<br>`/stages/0/serial_return_cache_evidence/0` | [qwen27-w4-dflash2-validation](qwen27-w4-dflash2-validation.md) | test outcome | Outcome unspecified | cached_tokens=0 tokens | Recorded configuration/job |
| [result-e9ed84a670b4ba08973d](../observations.json)<br>source-b61a20fde780f4bf7bdb6fe6.json<br>`/` | [qwen27-w4-dflash2-validation](qwen27-w4-dflash2-validation.md) | test outcome | Failed / partial | ram_restoration_qualified=false | Recorded configuration/job |
| [result-eb06af7cb545b5564684](../observations.json)<br>source-46c744708c934ef7375d911c.json<br>`/events/5` | [qwen27-w4-dflash2-validation](qwen27-w4-dflash2-validation.md) | test outcome | Outcome unspecified | prompt_tokens=79 tokens | Recorded configuration/job |
| [result-ecbb56739e06f3d0ea23](../observations.json)<br>source-a444806d1e3702ecb24f8598.json<br>`/stages/0/serial_initial_cache_evidence/0` | [qwen27-w4-dflash2-validation](qwen27-w4-dflash2-validation.md) | test outcome | Outcome unspecified | cached_tokens=0 tokens | Recorded configuration/job |
| [result-ed4d735f72b02a6dd319](../observations.json)<br>source-d377699ffb803509d619c845.json<br>`/phases/1` | [qwen27-w4-dflash2-validation](qwen27-w4-dflash2-validation.md) | test outcome | Failed / partial | passed=false | Recorded configuration/job |
| [result-f0f26cc28d6eb9cfa499](../observations.json)<br>source-2d9fdb8ef80b14bf9efc47a3.json<br>`/jobs/0` | [qwen27-w4-dflash2-validation](qwen27-w4-dflash2-validation.md) | test outcome | Failed / partial | passed=false | Recorded configuration/job |
| [result-f12184c57e1327116e54](../observations.json)<br>source-46c744708c934ef7375d911c.json<br>`/events/155` | [qwen27-w4-dflash2-validation](qwen27-w4-dflash2-validation.md) | test outcome | Outcome unspecified | prompt_tokens=16,391 tokens | Recorded configuration/job |
| [result-f9b04d519708d0448ee4](../observations.json)<br>source-46c744708c934ef7375d911c.json<br>`/events/6` | [qwen27-w4-dflash2-validation](qwen27-w4-dflash2-validation.md) | test outcome | Outcome unspecified | prompt_tokens=8,195 tokens | Recorded configuration/job |
| [result-fc0095dedbdcc738cb44](../observations.json)<br>source-153b916e74eb61dfe8262b94.json<br>`/features/stop_string` | [qwen27-w4-dflash2-validation](qwen27-w4-dflash2-validation.md) | performance detail | Outcome unspecified | wall_seconds=0.24 s | Recorded configuration/job |

These are saved result records, including failures and bounded checks. Copies, individual requests, report summaries and regrading can overlap; their counts are not independent test repetitions. Open each result for exact values, units, configuration binding and source receipts.

There are 10 retained lifecycle records. Their states, exit codes and configuration IDs remain in [catalog.json](../catalog.json); they do not supply missing benchmark results.

[Full archive](../../README.md) | [All retained waves](../RESULTS.md) | [Data definitions](../DATA.md) | [Recommended recipes](../../../README.md)
