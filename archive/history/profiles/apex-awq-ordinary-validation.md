# apex-awq-ordinary-validation

**Historical record. Bounded checks only.**

Model family: Apex Flash 1 (GLM 5.3 Flash post-train).

Recorded archive reason: Ordinary or four-card capacity comparison; speculative and other card-count configurations have separate records.

Historical configurations are provided for comparison. The [recommended recipes](../../../README.md) include supported launch scripts.

Current recipes using the same recorded checkpoint repository: [apex-abliterated-awq-dflash2-pp3-balanced](../../../recipes/apex-abliterated-awq-dflash2-pp3-balanced/README.md). Context, cache and runtime versions can differ.

## Saved Configuration Versions

Each configuration ID identifies a distinct original settings record. Deployment fields are omitted; versions can have identical published settings after that omission. Upstream runtime commits remain unspecified where the source retained only an integration label.

| Configuration | Recorded artifact / source | Configured card counts | Context tokens | GPU pool tokens | Slots | Draft mode / tokens |
| --- | --- | --- | --- | --- | --- | --- |
| cfg-15c78dae47cee5c35c8c | [svbmrgd/apex-flash-1-abliterated-AWQ@7ea31e3d22](https://huggingface.co/svbmrgd/apex-flash-1-abliterated-AWQ/tree/7ea31e3d22c6622c999d3de74d1569efce815943) | 3 | 32,768 | Not recorded | 4 | disabled / 0 |

Card counts are saved configuration choices, not a claim that every allowed placement was measured. A derived view can differ from its pinned download source.

<details>
<summary>cfg-15c78dae47cee5c35c8c</summary>

```json
{
  "kind": "vllm_apex_awq",
  "gpu_counts": [
    3
  ],
  "context": 32768,
  "kv_dtype": "bfloat16",
  "draft_mode": "disabled",
  "draft_tokens": 0,
  "max_sessions": 4,
  "chunk_size": 1280,
  "ram_kv_mib": 8192,
  "power_watts": 200,
  "host_memory_gib": 80,
  "host_swap_gib": 0,
  "min_vram_mib_per_gpu": 65530,
  "min_effective_vram_mib": 196000,
  "tensor_parallel_size": 1,
  "pipeline_parallel_size": 3,
  "pipeline_layer_partition": [
    17,
    14,
    14
  ],
  "kv_cache_mib_per_gpu": 1024,
  "enforce_eager": true,
  "mamba_cache_mode": "align",
  "model_repository": "svbmrgd/apex-flash-1-abliterated-AWQ",
  "model_revision": "7ea31e3d22c6622c999d3de74d1569efce815943",
  "draft_repository": null,
  "draft_revision": null,
  "recorded_runtime_label": "apex-awq-pp3-r1",
  "served_model_label": "apex-flash-1-abliterated-awq"
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
| check-05ee3db3f4f97f737eff | Failed / partial | {"passed":false,"ram_restoration_qualified":false} |
| check-69169059358ae10265a1 | Pass | {"passed":true,"ram_restoration_qualified":true} |
| check-8fd172b979f7ccd59f60 | Failed / partial | {"passed":false,"ram_restoration_qualified":false} |
| check-ede164b9d798cb3ee3c7 | Failed / partial | {"passed":false,"ram_restoration_qualified":false} |
| check-efb84ba564617da7beb9 | Failed / partial | {"passed":false,"ram_restoration_qualified":false} |

These checks retain their reported scope. A context/allocation/retrieval check is not a general quality score or a speed qualification at that context. Exact flags and provenance are in [checks.json](../checks.json).

## Additional Test Results

| Result / Source | Profile | Evidence type | Reported outcome | Retained values | Configuration binding |
| --- | --- | --- | --- | --- | --- |
| [result-3795d4ce7a8d6dfdc399](../observations.json)<br>source-35dad41c7b0a1e79f2849305.json<br>`/` | [apex-awq-ordinary-validation](apex-awq-ordinary-validation.md) | test outcome | Failed / partial | passed=false | Recorded configuration/job |
| [result-3b2b8bf44e832646636c](../observations.json)<br>source-95477c1cf203349fbae49a3f.json<br>`/` | [apex-awq-ordinary-validation](apex-awq-ordinary-validation.md) | test outcome | Failed / partial | passed=false | Recorded configuration/job |
| [result-8a4f6cf5c6cca23463e5](../observations.json)<br>source-8a05ba9a2720165bebeef920.json<br>`/stages/1` | [apex-awq-ordinary-validation](apex-awq-ordinary-validation.md) | test outcome | Outcome unspecified | load_seconds=330.50 s | Recorded configuration/job |
| [result-a670ed6e64cd19d41327](../observations.json)<br>source-8a05ba9a2720165bebeef920.json<br>`/stages/2` | [apex-awq-ordinary-validation](apex-awq-ordinary-validation.md) | test outcome | Outcome unspecified | load_seconds=360.04 s | Recorded configuration/job |
| [result-ad08e07f5b4167f89d48](../observations.json)<br>source-efc9ceb0869bcb4cd67156f9.json<br>`/` | [apex-awq-ordinary-validation](apex-awq-ordinary-validation.md) | test outcome | Failed / partial | passed=false | Recorded configuration/job |
| [result-b14e5227dd631f30024d](../observations.json)<br>source-5e964c9bfc12a4cca6cc4e9c.json<br>`/` | [apex-awq-ordinary-validation](apex-awq-ordinary-validation.md) | test outcome | Failed / partial | ram_restoration_qualified=false | Recorded configuration/job |
| [result-bcd223b0c1de587c6535](../observations.json)<br>source-8aad592a1b81cd77b20b5cf9.json<br>`/` | [apex-awq-ordinary-validation](apex-awq-ordinary-validation.md) | test outcome | Pass | passed=true; ram_restoration_qualified=true | Recorded configuration/job |
| [result-d97020409f5dee25df44](../observations.json)<br>source-ab89fca7e0f49696d5258b56.json<br>`/profiles/1/current_config` | [apex-awq-ordinary-validation](apex-awq-ordinary-validation.md) | test outcome | Outcome unspecified | context=32,768 tokens | Recorded configuration/job |
| [result-e03952cedc9c11753645](../observations.json)<br>source-8a05ba9a2720165bebeef920.json<br>`/stages/0` | [apex-awq-ordinary-validation](apex-awq-ordinary-validation.md) | test outcome | Outcome unspecified | load_seconds=329.97 s | Recorded configuration/job |
| [result-e4a665c297e4d26f7b20](../observations.json)<br>source-4af7fa71a07e7d0567ce337e.json<br>`/` | [apex-awq-ordinary-validation](apex-awq-ordinary-validation.md) | test outcome | Failed / partial | ram_restoration_qualified=false | Recorded configuration/job |
| [result-e85b53d25de9e322ff95](../observations.json)<br>source-3797667f6fd1f8645a4214f6.json<br>`/` | [apex-awq-ordinary-validation](apex-awq-ordinary-validation.md) | test outcome | Failed / partial | ram_restoration_qualified=false | Recorded configuration/job |
| [result-eddd83b610def8d490b0](../observations.json)<br>source-fc7371954a16f0aeb6d777ff.json<br>`/` | [apex-awq-ordinary-validation](apex-awq-ordinary-validation.md) | test outcome | Failed / partial | ram_restoration_qualified=false | Recorded configuration/job |
| [result-f1d616cfdac1c3daa686](../observations.json)<br>source-0ed61d52b9a809ee90b7d5b3.json<br>`/` | [apex-awq-ordinary-validation](apex-awq-ordinary-validation.md) | test outcome | Failed / partial | passed=false | Recorded configuration/job |

These are saved result records, including failures and bounded checks. Copies, individual requests, report summaries and regrading can overlap; their counts are not independent test repetitions. Open each result for exact values, units, configuration binding and source receipts.

There are 6 retained lifecycle records. Their states, exit codes and configuration IDs remain in [catalog.json](../catalog.json); they do not supply missing benchmark results.

[Full archive](../../README.md) | [All retained waves](../RESULTS.md) | [Data definitions](../DATA.md) | [Recommended recipes](../../../README.md)
