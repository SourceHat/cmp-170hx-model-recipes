# DeepSeek V4.1 Flash TP3 - DSpark5

Recipe for NVIDIA CMP 170HX cards with 64 GiB usable VRAM.

| Parameter | Value |
| --- | --- |
| Checkpoint | [sfxnz/DeepSeek-V4.1-Flash-EXL3](https://huggingface.co/sfxnz/DeepSeek-V4.1-Flash-EXL3/tree/982b70452f399814f56b46272fd30394ae10d58c) |
| Checkpoint revision | `982b70452f399814f56b46272fd30394ae10d58c` |
| Quantization | EXL3 2.0 bpw MCG routed experts; native non-routed tensors |
| Runtime | vLLM backport + vllm-exl3 |
| Runtime version | 0.13.0 (image distribution label; patched backport) |
| Cards | 3 x 64 GiB SM80 |
| Layout | tensor parallel |
| OpenAI model id | `deepseek-v4.1-flash` |
| Configured request slots | 4 |
| Per-request context, tokens | 524,288 |
| Context-normalized KV capacity, token-equivalents | 3,480,837 |
| Main KV | fp8 |
| Draft KV | fp8 |
| Speculation | dspark / depth 5 |
| Prefill chunk, tokens | 1,280 |
| Recurrent RAM checkpoint budget, MiB | 0 |
| Full-context requests, sizing estimate | 6 |
| Capacity reporting context, tokens | 524,288 |
| Automatic memory utilization | 0.98391 |
| Engram backing | NVMe; 64 MiB row cache |
| Execution | eager; batch invariant |
| Observed peak VRAM/card, GiB | 62.83 |
| Memory observation phase | final-pool-context-check |

## Reproduce

Prepare the matching [deepseek runtime](../../docs/REPRODUCING.md), then download the pinned checkpoint:

```bash
python3 scripts/download_model.py deepseek-v41-flash-dspark5-tp3 \
  --directory /path/to/deepseek-source
```

Complete the [TP3 transformation and NVMe Engram preparation](../../docs/REPRODUCING.md) before launching. The launcher builds and runs the pinned Docker Compose service; it does not need a host Python inference environment.

Run from the repository root. Replace the example device ordinals with your own selection in layer/pipeline order:

```bash
bash recipes/deepseek-v41-flash-dspark5-tp3/launch.sh \
  --devices 0,1,2 \
  --model-path /path/to/deepseek-tp3 \
  --source-model-path /path/to/deepseek-source \
  --engram-path /path/on/nvme/engram-tables \
  --dry-run
```

`--dry-run` prints the command, environment and rendered config without importing a GPU runtime. Remove it to serve. The launcher runs in the foreground; Ctrl-C stops it.

The engine argument/settings template is in [engine-config.json](engine-config.json).

## Interface

Choose the listener with `--host` and `--port`; see [launch options](../../docs/REPRODUCING.md#launch-options).

Endpoints: `/v1/models`, `/v1/chat/completions` and `/v1/completions`. Chat serving supports the selected engine's tool-call parser and a tool-result continuation.

## Measurements

Decode is accepted output tokens/s, including reasoning and excluding prefill. Concurrent rates are whole-wave aggregate. TTFT is the median first-token latency across the listed requests. Prefill is the backend's per-request timer, whose boundaries differ between engines. Output budgets are distinct from tokens counted inside the common decode interval.

| Actual input/request, tokens | Requests | Cache | Output budget/request, tokens | Decode total tok/s | Decode/request tok/s | TTFT median, s | Prefill/request tok/s | Draft acceptance % | End-to-end total tok/s | Test pool tokens / equivalents | Test context limit, tokens |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 32,764 | 1 | cold | 256 | 16.86 | 16.86 | 66.52 | 493.92 | 41.43 | 3.14 | Not recorded | 524,288 |
| 32,764 | 4 | cold | 256 | 29.97 | 5.99<br>6.66<br>11.32<br>5.99 | 168.67 | Not recorded | 40.53 | 3.51 | Not recorded | 524,288 |

<details>
<summary>Earlier measurements of these weights and decoding layout</summary>

These use the recorded earlier pool/context/runtime geometry. Full configurations and source references are included in the numerical export.

| Actual input/request, tokens | Requests | Cache | Output budget/request, tokens | Decode total tok/s | Decode/request tok/s | TTFT median, s | Prefill/request tok/s | Draft acceptance % | End-to-end total tok/s | Test pool tokens / equivalents | Test context limit, tokens |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 32,764 | 1 | cold | 256 | 14.05 | 14.05 | 67.69 | Not recorded | 33.89 | 2.99 | Not recorded | 262,144 |
| 32,764 | 1 | repeated-input | 256 | 14.76 | 14.76 | 0.68 | Not recorded | 35.05 | 14.53 | Not recorded | 262,144 |
| 32,764 | 4 | cold | 256 | 26.46 | 7.26<br>4.69<br>6.35<br>8.17 | 170.23 | Not recorded | 33.96 | 3.39 | Not recorded | 262,144 |
| 32,764 | 4 | repeated-input | 256 | 31.61 | 8.01<br>8.42<br>7.67<br>7.50 | 2.01 | Not recorded | 36.43 | 28.88 | Not recorded | 262,144 |

</details>

Recorded per-request timers, accepted/proposed counts, decode intervals, cache-hit counters and source SHA256 references: [benchmarks.json](benchmarks.json). Unavailable fields remain null. The configured serving pool and each measured test pool are labeled separately.

The headline pair uses the [selected-serving prefill comparison](../../docs/PREFILL-COMPARISON.md), with zero verified cached input tokens and bulk RAM spilling disabled. The full numerical traces reproduce its synchronized decode values. Earlier results retain their original settings and remain separate.

The exported launch template retains an 8 GiB native offload budget; the timed headline jobs used zero. This setting differs explicitly, and the comparison does not establish an offload speedup or requalify the earlier capacity report.

## Verification

| Check | Result |
| --- | --- |
| Recorded target/reference checks | passed |
| Context check | passed |
| Context-check actual long input, tokens | 522,259 |
| Context-check normalized capacity, token-equivalents | 3,480,837 |
| Concurrent requests in context check | 4 |
| Retrieval answer checked | yes |
| RAM history restoration | not retested |

Allocation audits, per-card memory counters, task checks, quantization metadata and verification provenance: [evidence.json](evidence.json). [Data definitions](../../docs/DATA.md) explain measurement scope and missing fields.

## Tradeoffs

TP3/DSpark5 requires NVMe-backed Engram tables and has lower measured decode throughput than the other language-model recipes. The unsupported PP3 pairing is excluded.

## Qualification And Limits

The legacy `shared_gpu_pool_tokens` metadata field records vLLM's context-normalized capacity report: calculated full-context concurrency times the configured maximum context, rounded down. It uses cache-block requirements across groups, including sliding/compressed attention and state. It is not a literal count of resident token slots or free cache tokens, and the full-context sizing estimate is not a measured concurrency limit. See [data definitions](../../docs/DATA.md#memory-and-context).

- The context limit is per request; the KV pool is shared across requests and retained prefixes.
- Maximum-history counts are capacity arithmetic, not a long-context concurrent speed measurement.
- Requires the SM80 loader, TP3 padding preparation, vllm-exl3 plugin and NVMe Engram tables.
- Speed measurements precede final automatic pool sizing; they are not a measurement of the final-sized pool.
- measured on the reference host; portable export not GPU-requalified.

## DeepSeek V4.1 Flash 1017 TP4

The [four-card configuration](../../profiles/deepseek-v41-flash-1017-dspark5-tp4/README.md) uses the 1017 EXL3 2.9 bpw artifact and its qualified native runtime. Its [long-output and concurrency experiments](../../docs/DEEPSEEK-1017.md) have different weights, software and output budgets from this TP3 configuration; the measurements do not isolate a hardware speedup.

This original recipe documentation and data are [CC BY 4.0](../../LICENSES/CC-BY-4.0.txt); attribute SourceHat and link to this recipe when sharing or adapting them. The checkpoint's own model license applies to downloaded weights. Runtime code and patches retain the licenses described in [THIRD_PARTY.md](../../THIRD_PARTY.md).
