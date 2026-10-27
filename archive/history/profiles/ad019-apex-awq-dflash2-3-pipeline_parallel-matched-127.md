# ad019-apex-awq-dflash2-3-pipeline_parallel-matched-127

**Historical record. Decode interval measured.**

Model family: Apex Flash 1 (GLM 5.3 Flash post-train).

Historical configurations are provided for comparison. The [recommended recipes](../../../README.md) include supported launch scripts.

Current recipes using the same recorded checkpoint repository: [apex-abliterated-awq-dflash2-pp3-balanced](../../../recipes/apex-abliterated-awq-dflash2-pp3-balanced/README.md). Context, cache and runtime versions can differ.

## Saved Configuration Versions

Each configuration ID identifies a distinct original settings record. Deployment fields are omitted; versions can have identical published settings after that omission. Upstream runtime commits remain unspecified where the source retained only an integration label.

| Configuration | Recorded artifact / source | Configured card counts | Context tokens | GPU pool tokens | Slots | Draft mode / tokens |
| --- | --- | --- | --- | --- | --- | --- |
| cfg-39cf138a219fe05d6bde | [svbmrgd/apex-flash-1-abliterated-AWQ@7ea31e3d22](https://huggingface.co/svbmrgd/apex-flash-1-abliterated-AWQ/tree/7ea31e3d22c6622c999d3de74d1569efce815943) | 3 | 262,144 | Not recorded | 4 | dflash2 / 3 |

Card counts are saved configuration choices, not a claim that every allowed placement was measured. A derived view can differ from its pinned download source.

<details>
<summary>cfg-39cf138a219fe05d6bde</summary>

```json
{
  "kind": "vllm_apex_awq",
  "gpu_counts": [
    3
  ],
  "context": 262144,
  "kv_dtype": "fp8_e4m3",
  "draft_kv_dtype": "int8_per_token_head",
  "draft_mode": "dflash2",
  "draft_tokens": 3,
  "max_sessions": 4,
  "chunk_size": 512,
  "ram_kv_mib": 8192,
  "power_watts": 200,
  "host_memory_gib": 80,
  "host_swap_gib": 0,
  "min_vram_mib_per_gpu": 65530,
  "min_effective_vram_mib": 196000,
  "parallelism": "pipeline_parallel",
  "tensor_parallel_size": 1,
  "pipeline_parallel_size": 3,
  "pipeline_layer_partition": [
    17,
    14,
    14
  ],
  "enforce_eager": true,
  "gpu_memory_utilization": 0.985,
  "transport": "host",
  "model_repository": "svbmrgd/apex-flash-1-abliterated-AWQ",
  "model_revision": "7ea31e3d22c6622c999d3de74d1569efce815943",
  "draft_repository": "incoai/GLM-5.3-Flash-DFlash2",
  "draft_revision": "bf582e4eacc1810f76656d1811693ff6c6737d2a",
  "recorded_runtime_label": "apex-awq-nope8-campaign-f",
  "served_model_label": "apex-flash-1-abliterated-awq",
  "draft_directory_template": "@DRAFT_ROOT@"
}
```

Pinned model revision recorded: yes. Source receipt labels, hashes and object locators are retained in [configurations.json](../configurations.json).

</details>

## Retained Measurements

| Profile / Wave | Layout; Draft / Tokens | Requests | Input tokens/request | Accepted output tokens/request | Cache / Reused input tokens | Context / GPU pool tokens | Shared decode tok/s total | Client after-first-token estimate tok/s | Whole-wave output tok/s | Median TTFT, s | Source report |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [ad019-apex-awq-dflash2-3-pipeline_parallel-matched-127](ad019-apex-awq-dflash2-3-pipeline_parallel-matched-127.md)<br>wave-1fda118b599231958955 | pipeline_parallel; dflash2 / 3 | 1 | 32,765 | 256 (budget 256) | repeated_input; reused - | 262,144 / - | 51.16 | Not recorded | 21.01 | 7.85 | Pass |
| [ad019-apex-awq-dflash2-3-pipeline_parallel-matched-127](ad019-apex-awq-dflash2-3-pipeline_parallel-matched-127.md)<br>wave-711f0b333f848825faf1 | pipeline_parallel; dflash2 / 3 | 1 | 32,765 | 256 (budget 256) | cold; reused - | 262,144 / - | 49.66 | Not recorded | 6.35 | 36.04 | Pass |
| [ad019-apex-awq-dflash2-3-pipeline_parallel-matched-127](ad019-apex-awq-dflash2-3-pipeline_parallel-matched-127.md)<br>wave-a084b6592df3cdf9d424 | pipeline_parallel; dflash2 / 3 | 4 | 32,766 | 256 (budget 256) | cold; reused - | 262,144 / - | 135.79 | Not recorded | 8.89 | 82.55 | Pass |
| [ad019-apex-awq-dflash2-3-pipeline_parallel-matched-127](ad019-apex-awq-dflash2-3-pipeline_parallel-matched-127.md)<br>wave-b11914827de06d07b46d | pipeline_parallel; dflash2 / 3 | 4 | 32,766 | 256 (budget 256) | repeated_input; reused - | 262,144 / - | 114.52 | Not recorded | 17.43 | 46.40 | Pass |

Rates are whole-wave totals over the stated request count. A wave may span multiple independent model instances; [measurements.json](../measurements.json) retains their contributions and the exact configuration IDs. Do not interpret a multi-instance total as one card's rate.

A dash in shared decode means no qualified synchronized interval is available. Whole-wave throughput includes prefill and queueing. A valid decode interval can survive inside an overall failed or partial check; the source-report outcome is preserved. No rows are averaged.

## Bounded Checks

| Check | Reported outcome | Retained counts / flags |
| --- | --- | --- |
| check-4eee6b7c32758f651a57 | Pass | {"passed":true,"elapsed_seconds":115.1534337660014,"ttft_seconds":[42.75095849599893,64.3027744960018,100.79823219499667,110.0857452780001],"end_to_end_accepted_tok_s":8.89248341548224} |
| check-648167f834cc2770c001 | Pass | {"passed":true,"elapsed_seconds":40.29445799000314,"ttft_seconds":[36.039110316000006],"end_to_end_accepted_tok_s":6.353231009175316} |
| check-8997199fa4c39c175c6a | Pass | {"passed":true,"elapsed_seconds":115.1534337660014,"ttft_seconds":[42.75095849599893,64.3027744960018,100.79823219499667,110.0857452780001],"end_to_end_accepted_tok_s":8.89248341548224} |
| check-bfa5b9a4f1d6ee904047 | Pass | {"passed":true,"elapsed_seconds":40.29445799000314,"ttft_seconds":[36.039110316000006],"end_to_end_accepted_tok_s":6.353231009175316} |

These checks retain their reported scope. A context/allocation/retrieval check is not a general quality score or a speed qualification at that context. Exact flags and provenance are in [checks.json](../checks.json).

## Additional Test Results

| Result / Source | Profile | Evidence type | Reported outcome | Retained values | Configuration binding |
| --- | --- | --- | --- | --- | --- |
| [result-6fbbe7de2de74242f33d](../observations.json)<br>source-b15d8fb978f8ef80623bcbc1.json<br>`/speed/0/waves/1` | [ad019-apex-awq-dflash2-3-pipeline_parallel-matched-127](ad019-apex-awq-dflash2-3-pipeline_parallel-matched-127.md)<br>[apex-awq-dflash2-3-pipeline_parallel](apex-awq-dflash2-3-pipeline_parallel.md) | performance detail | Outcome unspecified | elapsed_seconds=12.19 s; end_to_end_accepted_tok_s=21.01 accepted tokens/s; output_tokens=256 tokens; ttft_seconds=7.85 s; p50_ms=17.78 ms; p95_ms=54.45 ms; Draft accepted / proposed: 167.00 / 267.00 tokens; fraction 0.6255 | Recorded configuration/job |
| [result-828e51a783fecdb39e10](../observations.json)<br>source-b15d8fb978f8ef80623bcbc1.json<br>`/speed/0` | [ad019-apex-awq-dflash2-3-pipeline_parallel-matched-127](ad019-apex-awq-dflash2-3-pipeline_parallel-matched-127.md)<br>[apex-awq-dflash2-3-pipeline_parallel](apex-awq-dflash2-3-pipeline_parallel.md) | performance detail | Pass | elapsed_seconds=40.29 s; end_to_end_accepted_tok_s=6.35 accepted tokens/s; ttft_seconds=36.04 s; p50_ms=17.78 ms; p95_ms=54.45 ms; Draft accepted / proposed: 167.00 / 267.00 tokens; fraction 0.6255 | Recorded configuration/job |
| [result-82bb7d1c8e78268ce0e0](../observations.json)<br>source-b15d8fb978f8ef80623bcbc1.json<br>`/speed/0/waves/0` | [ad019-apex-awq-dflash2-3-pipeline_parallel-matched-127](ad019-apex-awq-dflash2-3-pipeline_parallel-matched-127.md)<br>[apex-awq-dflash2-3-pipeline_parallel](apex-awq-dflash2-3-pipeline_parallel.md) | performance detail | Outcome unspecified | elapsed_seconds=40.29 s; end_to_end_accepted_tok_s=6.35 accepted tokens/s; output_tokens=256 tokens; ttft_seconds=36.04 s; p50_ms=17.80 ms; p95_ms=54.51 ms; Draft accepted / proposed: 168.00 / 264.00 tokens; fraction 0.6364 | Recorded configuration/job |
| [result-8d71b9cc1e15161af25d](../observations.json)<br>source-b15d8fb978f8ef80623bcbc1.json<br>`/speed/1/waves/0` | [ad019-apex-awq-dflash2-3-pipeline_parallel-matched-127](ad019-apex-awq-dflash2-3-pipeline_parallel-matched-127.md)<br>[apex-awq-dflash2-3-pipeline_parallel](apex-awq-dflash2-3-pipeline_parallel.md) | performance detail | Outcome unspecified | elapsed_seconds=115.15 s; end_to_end_accepted_tok_s=8.89 accepted tokens/s; output_tokens=256 tokens; ttft_seconds=42.75<br>64.30<br>100.80<br>110.09 s; p50_ms=9.70 ms; p95_ms=30.18 ms; Draft accepted / proposed: 666.00 / 1,080.00 tokens; fraction 0.6167 | Recorded configuration/job |
| [result-a80f38e3fb91442fa7d3](../observations.json)<br>source-b15d8fb978f8ef80623bcbc1.json<br>`/capacity/trials/0` | [ad019-apex-awq-dflash2-3-pipeline_parallel-matched-127](ad019-apex-awq-dflash2-3-pipeline_parallel-matched-127.md)<br>[apex-awq-dflash2-3-pipeline_parallel](apex-awq-dflash2-3-pipeline_parallel.md) | context allocation | Outcome unspecified | resident_pool_tokens=710,171 tokens | Recorded configuration/job |
| [result-ac7538d095a8f8086a1d](../observations.json)<br>source-b15d8fb978f8ef80623bcbc1.json<br>`/speed/1` | [ad019-apex-awq-dflash2-3-pipeline_parallel-matched-127](ad019-apex-awq-dflash2-3-pipeline_parallel-matched-127.md)<br>[apex-awq-dflash2-3-pipeline_parallel](apex-awq-dflash2-3-pipeline_parallel.md) | performance detail | Pass | elapsed_seconds=115.15 s; end_to_end_accepted_tok_s=8.89 accepted tokens/s; ttft_seconds=42.75<br>64.30<br>100.80<br>110.09 s; p50_ms=31.29 ms; p95_ms=92.11 ms; Draft accepted / proposed: 638.00 / 1,164.00 tokens; fraction 0.5481 | Recorded configuration/job |
| [result-bfecbf9860d13e1a92fe](../observations.json)<br>source-b15d8fb978f8ef80623bcbc1.json<br>`/speed/1/waves/1` | [ad019-apex-awq-dflash2-3-pipeline_parallel-matched-127](ad019-apex-awq-dflash2-3-pipeline_parallel-matched-127.md)<br>[apex-awq-dflash2-3-pipeline_parallel](apex-awq-dflash2-3-pipeline_parallel.md) | performance detail | Outcome unspecified | elapsed_seconds=58.76 s; end_to_end_accepted_tok_s=17.43 accepted tokens/s; output_tokens=256 tokens; ttft_seconds=22.35<br>42.01<br>50.79<br>51.56 s; p50_ms=31.29 ms; p95_ms=92.11 ms; Draft accepted / proposed: 638.00 / 1,164.00 tokens; fraction 0.5481 | Recorded configuration/job |

These are saved result records, including failures and bounded checks. Copies, individual requests, report summaries and regrading can overlap; their counts are not independent test repetitions. Open each result for exact values, units, configuration binding and source receipts.

There are 1 retained lifecycle records. Their states, exit codes and configuration IDs remain in [catalog.json](../catalog.json); they do not supply missing benchmark results.

[Full archive](../../README.md) | [All retained waves](../RESULTS.md) | [Data definitions](../DATA.md) | [Recommended recipes](../../../README.md)
