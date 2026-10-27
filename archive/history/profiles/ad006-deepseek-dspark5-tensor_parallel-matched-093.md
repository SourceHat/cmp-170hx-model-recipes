# ad006-deepseek-dspark5-tensor_parallel-matched-093

**Historical record. Decode interval measured.**

Model family: DeepSeek.

Historical configurations are provided for comparison. The [recommended recipes](../../../README.md) include supported launch scripts.

Current recipes using the same recorded checkpoint repository: [deepseek-v41-flash-dspark5-tp3](../../../recipes/deepseek-v41-flash-dspark5-tp3/README.md). Context, cache and runtime versions can differ.

## Saved Configuration Versions

Each configuration ID identifies a distinct original settings record. Deployment fields are omitted; versions can have identical published settings after that omission. Upstream runtime commits remain unspecified where the source retained only an integration label.

| Configuration | Recorded artifact / source | Configured card counts | Context tokens | GPU pool tokens | Slots | Draft mode / tokens |
| --- | --- | --- | --- | --- | --- | --- |
| cfg-76e4555b74d82bde1087 | [sfxnz/DeepSeek-V4.1-Flash-EXL3@982b70452f](https://huggingface.co/sfxnz/DeepSeek-V4.1-Flash-EXL3/tree/982b70452f399814f56b46272fd30394ae10d58c) | 3 | 262,144 | Not recorded | 4 | dspark / 5 |

Card counts are saved configuration choices, not a claim that every allowed placement was measured. A derived view can differ from its pinned download source.

<details>
<summary>cfg-76e4555b74d82bde1087</summary>

```json
{
  "kind": "vllm_native",
  "gpu_counts": [
    3
  ],
  "context": 262144,
  "kv_dtype": "fp8",
  "draft_mode": "dspark",
  "draft_tokens": 5,
  "max_sessions": 4,
  "chunk_size": 1280,
  "ram_kv_mib": 8192,
  "power_watts": 200,
  "host_memory_gib": 80,
  "host_swap_gib": 0,
  "min_vram_mib_per_gpu": 65530,
  "min_effective_vram_mib": 196000,
  "parallelism": "tensor_parallel",
  "engram_row_cache_mib": 64,
  "enforce_eager": true,
  "batch_invariant": true,
  "gpu_memory_utilization": 0.95,
  "prefix_match_unit": 8,
  "transport": "host",
  "model_repository": "sfxnz/DeepSeek-V4.1-Flash-EXL3",
  "model_revision": "982b70452f399814f56b46272fd30394ae10d58c",
  "draft_repository": null,
  "draft_revision": null,
  "recorded_runtime_label": "deepseek-v41-sm80-r2",
  "served_model_label": "deepseek-v4.1-flash"
}
```

Pinned model revision recorded: yes. Source receipt labels, hashes and object locators are retained in [configurations.json](../configurations.json).

</details>

## Retained Measurements

| Profile / Wave | Layout; Draft / Tokens | Requests | Input tokens/request | Accepted output tokens/request | Cache / Reused input tokens | Context / GPU pool tokens | Shared decode tok/s total | Client after-first-token estimate tok/s | Whole-wave output tok/s | Median TTFT, s | Source report |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [ad006-deepseek-dspark5-tensor_parallel-matched-093](ad006-deepseek-dspark5-tensor_parallel-matched-093.md)<br>wave-4670f34cbcd94c9150c2 | tensor_parallel; dspark / 5 | 1 | 32,764 | 256 (budget 256) | cold; reused - | 262,144 / - | 14.05 | Not recorded | 2.99 | 67.69 | Pass |
| [ad006-deepseek-dspark5-tensor_parallel-matched-093](ad006-deepseek-dspark5-tensor_parallel-matched-093.md)<br>wave-705b5f2e46743adf24f9 | tensor_parallel; dspark / 5 | 4 | 32,764 | 256 (budget 256) | repeated_input; reused - | 262,144 / - | 31.61 | Not recorded | 28.88 | 2.01 | Pass |
| [ad006-deepseek-dspark5-tensor_parallel-matched-093](ad006-deepseek-dspark5-tensor_parallel-matched-093.md)<br>wave-8b4601d92ac9a05260f8 | tensor_parallel; dspark / 5 | 4 | 32,764 | 256 (budget 256) | cold; reused - | 262,144 / - | 26.46 | Not recorded | 3.39 | 170.23 | Pass |
| [ad006-deepseek-dspark5-tensor_parallel-matched-093](ad006-deepseek-dspark5-tensor_parallel-matched-093.md)<br>wave-e48938c3dd0bc2553f17 | tensor_parallel; dspark / 5 | 1 | 32,764 | 256 (budget 256) | repeated_input; reused - | 262,144 / - | 14.76 | Not recorded | 14.53 | 0.68 | Pass |

Rates are whole-wave totals over the stated request count. A wave may span multiple independent model instances; [measurements.json](../measurements.json) retains their contributions and the exact configuration IDs. Do not interpret a multi-instance total as one card's rate.

A dash in shared decode means no qualified synchronized interval is available. Whole-wave throughput includes prefill and queueing. A valid decode interval can survive inside an overall failed or partial check; the source-report outcome is preserved. No rows are averaged.

## Bounded Checks

| Check | Reported outcome | Retained counts / flags |
| --- | --- | --- |
| check-3bb5842a0e630b01c64d | Pass | {"passed":true,"elapsed_seconds":85.48412803799874,"ttft_seconds":[67.69299974799651],"end_to_end_accepted_tok_s":2.9947079753355483} |
| check-74d50577913cf1d260b0 | Pass | {"passed":true,"elapsed_seconds":301.800024655,"ttft_seconds":[67.35519565100549,135.5543876590018,204.91120009600127,275.52854238500004],"end_to_end_accepted_tok_s":3.392975203267715} |
| check-84fc36b9c262169f0409 | Pass | {"passed":true,"elapsed_seconds":85.48412803799874,"ttft_seconds":[67.69299974799651],"end_to_end_accepted_tok_s":2.9947079753355483} |
| check-889249cbdde0f4267645 | Pass | {"passed":true,"elapsed_seconds":301.800024655,"ttft_seconds":[67.35519565100549,135.5543876590018,204.91120009600127,275.52854238500004],"end_to_end_accepted_tok_s":3.392975203267715} |

These checks retain their reported scope. A context/allocation/retrieval check is not a general quality score or a speed qualification at that context. Exact flags and provenance are in [checks.json](../checks.json).

## Additional Test Results

| Result / Source | Profile | Evidence type | Reported outcome | Retained values | Configuration binding |
| --- | --- | --- | --- | --- | --- |
| [result-53d935ea8f67d7499542](../observations.json)<br>source-06e65bbe238da422163343e9.json<br>`/speed/1` | [ad006-deepseek-dspark5-tensor_parallel-matched-093](ad006-deepseek-dspark5-tensor_parallel-matched-093.md)<br>[deepseek-dspark5-tensor_parallel](deepseek-dspark5-tensor_parallel.md) | performance detail | Pass | elapsed_seconds=301.80 s; end_to_end_accepted_tok_s=3.39 accepted tokens/s; ttft_seconds=67.36<br>135.55<br>204.91<br>275.53 s; p50_ms=153.23 ms; p95_ms=374.97 ms; Draft accepted / proposed: 663.00 / 1,820.00 tokens; fraction 0.3643 | Recorded configuration/job |
| [result-565e74cd93420a580bc5](../observations.json)<br>source-06e65bbe238da422163343e9.json<br>`/speed/0/waves/1` | [ad006-deepseek-dspark5-tensor_parallel-matched-093](ad006-deepseek-dspark5-tensor_parallel-matched-093.md)<br>[deepseek-dspark5-tensor_parallel](deepseek-dspark5-tensor_parallel.md) | performance detail | Outcome unspecified | elapsed_seconds=17.61 s; end_to_end_accepted_tok_s=14.53 accepted tokens/s; output_tokens=256 tokens; ttft_seconds=0.68 s; p50_ms=86.35 ms; p95_ms=192.05 ms; Draft accepted / proposed: 163.00 / 465.00 tokens; fraction 0.3505 | Recorded configuration/job |
| [result-7b63629869ec699fd056](../observations.json)<br>source-06e65bbe238da422163343e9.json<br>`/speed/1/waves/1` | [ad006-deepseek-dspark5-tensor_parallel-matched-093](ad006-deepseek-dspark5-tensor_parallel-matched-093.md)<br>[deepseek-dspark5-tensor_parallel](deepseek-dspark5-tensor_parallel.md) | performance detail | Outcome unspecified | elapsed_seconds=35.45 s; end_to_end_accepted_tok_s=28.88 accepted tokens/s; output_tokens=256 tokens; ttft_seconds=0.67<br>1.41<br>2.62<br>2.62 s; p50_ms=153.23 ms; p95_ms=374.97 ms; Draft accepted / proposed: 663.00 / 1,820.00 tokens; fraction 0.3643 | Recorded configuration/job |
| [result-86eac815caab6f8fa49b](../observations.json)<br>source-06e65bbe238da422163343e9.json<br>`/capacity/trials/0` | [ad006-deepseek-dspark5-tensor_parallel-matched-093](ad006-deepseek-dspark5-tensor_parallel-matched-093.md)<br>[deepseek-dspark5-tensor_parallel](deepseek-dspark5-tensor_parallel.md) | context allocation | Outcome unspecified | resident_pool_tokens=2,781,864 tokens | Recorded configuration/job |
| [result-988f8b20a8d9ccc5049a](../observations.json)<br>source-06e65bbe238da422163343e9.json<br>`/speed/0` | [ad006-deepseek-dspark5-tensor_parallel-matched-093](ad006-deepseek-dspark5-tensor_parallel-matched-093.md)<br>[deepseek-dspark5-tensor_parallel](deepseek-dspark5-tensor_parallel.md) | performance detail | Pass | elapsed_seconds=85.48 s; end_to_end_accepted_tok_s=2.99 accepted tokens/s; ttft_seconds=67.69 s; p50_ms=86.35 ms; p95_ms=192.05 ms; Draft accepted / proposed: 163.00 / 465.00 tokens; fraction 0.3505 | Recorded configuration/job |
| [result-c590672d5fb47d4d4489](../observations.json)<br>source-06e65bbe238da422163343e9.json<br>`/speed/0/waves/0` | [ad006-deepseek-dspark5-tensor_parallel-matched-093](ad006-deepseek-dspark5-tensor_parallel-matched-093.md)<br>[deepseek-dspark5-tensor_parallel](deepseek-dspark5-tensor_parallel.md) | performance detail | Outcome unspecified | elapsed_seconds=85.48 s; end_to_end_accepted_tok_s=2.99 accepted tokens/s; output_tokens=256 tokens; ttft_seconds=67.69 s; p50_ms=90.53 ms; p95_ms=193.81 ms; Draft accepted / proposed: 161.00 / 475.00 tokens; fraction 0.3389 | Recorded configuration/job |
| [result-cf5f8bd09916aaf4dec8](../observations.json)<br>source-a9e622d351a86c8b776605d4.json<br>`/managed_phase_timings/93` | [ad006-deepseek-dspark5-tensor_parallel-matched-093](ad006-deepseek-dspark5-tensor_parallel-matched-093.md) | test outcome | Outcome unspecified | wall_seconds=877.08 s | Recorded configuration/job |
| [result-d3a2a5a3f9e7b3d95c09](../observations.json)<br>source-06e65bbe238da422163343e9.json<br>`/speed/1/waves/0` | [ad006-deepseek-dspark5-tensor_parallel-matched-093](ad006-deepseek-dspark5-tensor_parallel-matched-093.md)<br>[deepseek-dspark5-tensor_parallel](deepseek-dspark5-tensor_parallel.md) | performance detail | Outcome unspecified | elapsed_seconds=301.80 s; end_to_end_accepted_tok_s=3.39 accepted tokens/s; output_tokens=256 tokens; ttft_seconds=67.36<br>135.55<br>204.91<br>275.53 s; p50_ms=118.32 ms; p95_ms=371.70 ms; Draft accepted / proposed: 647.00 / 1,905.00 tokens; fraction 0.3396 | Recorded configuration/job |

These are saved result records, including failures and bounded checks. Copies, individual requests, report summaries and regrading can overlap; their counts are not independent test repetitions. Open each result for exact values, units, configuration binding and source receipts.

There are 1 retained lifecycle records. Their states, exit codes and configuration IDs remain in [catalog.json](../catalog.json); they do not supply missing benchmark results.

[Full archive](../../README.md) | [All retained waves](../RESULTS.md) | [Data definitions](../DATA.md) | [Recommended recipes](../../../README.md)
