# ad019-apex-awq-dflash2-3-pp3-balanced-171513-matched-129

**Historical record. Decode interval measured.**

Model family: Apex Flash 1 (GLM 5.3 Flash post-train).

Historical configurations are provided for comparison. The [recommended recipes](../../../README.md) include supported launch scripts.

Current recipes using the same recorded checkpoint repository: [apex-abliterated-awq-dflash2-pp3-balanced](../../../recipes/apex-abliterated-awq-dflash2-pp3-balanced/README.md). Context, cache and runtime versions can differ.

## Saved Configuration Versions

Each configuration ID identifies a distinct original settings record. Deployment fields are omitted; versions can have identical published settings after that omission. Upstream runtime commits remain unspecified where the source retained only an integration label.

| Configuration | Recorded artifact / source | Configured card counts | Context tokens | GPU pool tokens | Slots | Draft mode / tokens |
| --- | --- | --- | --- | --- | --- | --- |
| cfg-abf657fbbffee4514491 | [svbmrgd/apex-flash-1-abliterated-AWQ@7ea31e3d22](https://huggingface.co/svbmrgd/apex-flash-1-abliterated-AWQ/tree/7ea31e3d22c6622c999d3de74d1569efce815943) | 3 | 262,144 | Not recorded | 4 | dflash2 / 3 |

Card counts are saved configuration choices, not a claim that every allowed placement was measured. A derived view can differ from its pinned download source.

<details>
<summary>cfg-abf657fbbffee4514491</summary>

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
    15,
    13
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
| [ad019-apex-awq-dflash2-3-pp3-balanced-171513-matched-129](ad019-apex-awq-dflash2-3-pp3-balanced-171513-matched-129.md)<br>wave-2dd69737279c7db51d4e | pipeline_parallel; dflash2 / 3 | 1 | 32,765 | 256 (budget 256) | repeated_input; reused - | 262,144 / - | 43.96 | Not recorded | 19.19 | 8.85 | Pass |
| [ad019-apex-awq-dflash2-3-pp3-balanced-171513-matched-129](ad019-apex-awq-dflash2-3-pp3-balanced-171513-matched-129.md)<br>wave-46c7f2d221623d2553e1 | pipeline_parallel; dflash2 / 3 | 4 | 32,766 | 256 (budget 256) | cold; reused - | 262,144 / - | 128.47 | Not recorded | 10.00 | 65.92 | Pass |
| [ad019-apex-awq-dflash2-3-pp3-balanced-171513-matched-129](ad019-apex-awq-dflash2-3-pp3-balanced-171513-matched-129.md)<br>wave-a13ed5bed9df254c2c64 | pipeline_parallel; dflash2 / 3 | 1 | 32,765 | 256 (budget 256) | cold; reused - | 262,144 / - | 52.49 | Not recorded | 12.42 | 16.33 | Pass |
| [ad019-apex-awq-dflash2-3-pp3-balanced-171513-matched-129](ad019-apex-awq-dflash2-3-pp3-balanced-171513-matched-129.md)<br>wave-bf561867ecaedc697e0b | pipeline_parallel; dflash2 / 3 | 4 | 32,766 | 256 (budget 256) | repeated_input; reused - | 262,144 / - | 116.06 | Not recorded | 22.60 | 34.95 | Pass |

Rates are whole-wave totals over the stated request count. A wave may span multiple independent model instances; [measurements.json](../measurements.json) retains their contributions and the exact configuration IDs. Do not interpret a multi-instance total as one card's rate.

A dash in shared decode means no qualified synchronized interval is available. Whole-wave throughput includes prefill and queueing. A valid decode interval can survive inside an overall failed or partial check; the source-report outcome is preserved. No rows are averaged.

## Bounded Checks

| Check | Reported outcome | Retained counts / flags |
| --- | --- | --- |
| check-2669b59b79f556e62c17 | Pass | {"passed":true,"elapsed_seconds":102.42527137200159,"ttft_seconds":[27.028977899000893,53.11200597000061,78.72722816600071,97.12393882199831],"end_to_end_accepted_tok_s":9.9975327014844} |
| check-2e25059f6f91487f9a61 | Pass | {"passed":true,"elapsed_seconds":20.607794837000256,"ttft_seconds":[16.327881042998342],"end_to_end_accepted_tok_s":12.422483920519479} |
| check-89562ea3eb7699ad16bf | Pass | {"passed":true,"elapsed_seconds":102.42527137200159,"ttft_seconds":[27.028977899000893,53.11200597000061,78.72722816600071,97.12393882199831],"end_to_end_accepted_tok_s":9.9975327014844} |
| check-c2b60849b965114a74b1 | Pass | {"passed":true,"elapsed_seconds":20.607794837000256,"ttft_seconds":[16.327881042998342],"end_to_end_accepted_tok_s":12.422483920519479} |

These checks retain their reported scope. A context/allocation/retrieval check is not a general quality score or a speed qualification at that context. Exact flags and provenance are in [checks.json](../checks.json).

## Additional Test Results

| Result / Source | Profile | Evidence type | Reported outcome | Retained values | Configuration binding |
| --- | --- | --- | --- | --- | --- |
| [result-2308ca1bbf073dbc8932](../observations.json)<br>source-d483a94cc2fdbf31ec4c2f97.json<br>`/speed/1/waves/0` | [ad019-apex-awq-dflash2-3-pp3-balanced-171513-matched-129](ad019-apex-awq-dflash2-3-pp3-balanced-171513-matched-129.md)<br>[apex-awq-dflash2-3-pp3-balanced-171513](apex-awq-dflash2-3-pp3-balanced-171513.md) | performance detail | Outcome unspecified | elapsed_seconds=102.43 s; end_to_end_accepted_tok_s=10.00 accepted tokens/s; output_tokens=256 tokens; ttft_seconds=27.03<br>53.11<br>78.73<br>97.12 s; p50_ms=10.23 ms; p95_ms=33.64 ms; Draft accepted / proposed: 646.00 / 1,125.00 tokens; fraction 0.5742 | Recorded configuration/job |
| [result-26096ebb26a798c3491f](../observations.json)<br>source-d483a94cc2fdbf31ec4c2f97.json<br>`/speed/0/waves/1` | [ad019-apex-awq-dflash2-3-pp3-balanced-171513-matched-129](ad019-apex-awq-dflash2-3-pp3-balanced-171513-matched-129.md)<br>[apex-awq-dflash2-3-pp3-balanced-171513](apex-awq-dflash2-3-pp3-balanced-171513.md) | performance detail | Outcome unspecified | elapsed_seconds=13.34 s; end_to_end_accepted_tok_s=19.19 accepted tokens/s; output_tokens=256 tokens; ttft_seconds=8.85 s; p50_ms=25.98 ms; p95_ms=55.13 ms; Draft accepted / proposed: 152.00 / 312.00 tokens; fraction 0.4872 | Recorded configuration/job |
| [result-6a93b991cd482a39670e](../observations.json)<br>source-d483a94cc2fdbf31ec4c2f97.json<br>`/speed/0/waves/0` | [ad019-apex-awq-dflash2-3-pp3-balanced-171513-matched-129](ad019-apex-awq-dflash2-3-pp3-balanced-171513-matched-129.md)<br>[apex-awq-dflash2-3-pp3-balanced-171513](apex-awq-dflash2-3-pp3-balanced-171513.md) | performance detail | Outcome unspecified | elapsed_seconds=20.61 s; end_to_end_accepted_tok_s=12.42 accepted tokens/s; output_tokens=256 tokens; ttft_seconds=16.33 s; p50_ms=14.04 ms; p95_ms=54.33 ms; Draft accepted / proposed: 171.00 / 261.00 tokens; fraction 0.6552 | Recorded configuration/job |
| [result-6d555c9d116286973abf](../observations.json)<br>source-d483a94cc2fdbf31ec4c2f97.json<br>`/speed/1` | [ad019-apex-awq-dflash2-3-pp3-balanced-171513-matched-129](ad019-apex-awq-dflash2-3-pp3-balanced-171513-matched-129.md)<br>[apex-awq-dflash2-3-pp3-balanced-171513](apex-awq-dflash2-3-pp3-balanced-171513.md) | performance detail | Pass | elapsed_seconds=102.43 s; end_to_end_accepted_tok_s=10.00 accepted tokens/s; ttft_seconds=27.03<br>53.11<br>78.73<br>97.12 s; p50_ms=30.73 ms; p95_ms=93.03 ms; Draft accepted / proposed: 650.00 / 1,113.00 tokens; fraction 0.5840 | Recorded configuration/job |
| [result-b22940f4a587a2ed3b58](../observations.json)<br>source-d483a94cc2fdbf31ec4c2f97.json<br>`/speed/1/waves/1` | [ad019-apex-awq-dflash2-3-pp3-balanced-171513-matched-129](ad019-apex-awq-dflash2-3-pp3-balanced-171513-matched-129.md)<br>[apex-awq-dflash2-3-pp3-balanced-171513](apex-awq-dflash2-3-pp3-balanced-171513.md) | performance detail | Outcome unspecified | elapsed_seconds=45.32 s; end_to_end_accepted_tok_s=22.60 accepted tokens/s; output_tokens=256 tokens; ttft_seconds=17.27<br>31.91<br>37.98<br>38.64 s; p50_ms=30.73 ms; p95_ms=93.03 ms; Draft accepted / proposed: 650.00 / 1,113.00 tokens; fraction 0.5840 | Recorded configuration/job |
| [result-f71d269fcad2dbe039e4](../observations.json)<br>source-d483a94cc2fdbf31ec4c2f97.json<br>`/speed/0` | [ad019-apex-awq-dflash2-3-pp3-balanced-171513-matched-129](ad019-apex-awq-dflash2-3-pp3-balanced-171513-matched-129.md)<br>[apex-awq-dflash2-3-pp3-balanced-171513](apex-awq-dflash2-3-pp3-balanced-171513.md) | performance detail | Pass | elapsed_seconds=20.61 s; end_to_end_accepted_tok_s=12.42 accepted tokens/s; ttft_seconds=16.33 s; p50_ms=25.98 ms; p95_ms=55.13 ms; Draft accepted / proposed: 152.00 / 312.00 tokens; fraction 0.4872 | Recorded configuration/job |
| [result-fb9b65131fb46c124383](../observations.json)<br>source-d483a94cc2fdbf31ec4c2f97.json<br>`/capacity/trials/0` | [ad019-apex-awq-dflash2-3-pp3-balanced-171513-matched-129](ad019-apex-awq-dflash2-3-pp3-balanced-171513-matched-129.md)<br>[apex-awq-dflash2-3-pp3-balanced-171513](apex-awq-dflash2-3-pp3-balanced-171513.md) | context allocation | Outcome unspecified | resident_pool_tokens=1,167,732 tokens | Recorded configuration/job |

These are saved result records, including failures and bounded checks. Copies, individual requests, report summaries and regrading can overlap; their counts are not independent test repetitions. Open each result for exact values, units, configuration binding and source receipts.

There are 1 retained lifecycle records. Their states, exit codes and configuration IDs remain in [catalog.json](../catalog.json); they do not supply missing benchmark results.

[Full archive](../../README.md) | [All retained waves](../RESULTS.md) | [Data definitions](../DATA.md) | [Recommended recipes](../../../README.md)
