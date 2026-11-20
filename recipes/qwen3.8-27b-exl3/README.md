# Qwen3.8-27B - EXL3 6 bpw, MTP1

Recipe for NVIDIA CMP 170HX cards with 64 GiB usable VRAM.

| Parameter | Value |
| --- | --- |
| Checkpoint | [turboderp/Qwen3.8-27B-exl3](https://huggingface.co/turboderp/Qwen3.8-27B-exl3/tree/9e4c23cfb23697165b8e2f6da2a1df995f66353c) |
| Checkpoint revision | `9e4c23cfb23697165b8e2f6da2a1df995f66353c` |
| Quantization | EXL3 6 bpw |
| Runtime | TabbyAPI / ExLlamaV3 |
| Runtime version | ExLlamaV3 1.5.3 |
| Cards | 1 x 64 GiB SM80 |
| Layout | single card |
| OpenAI model id | `qwen3.8-27b` |
| Configured request slots | 8 |
| Per-request context, tokens | 262,144 |
| Shared GPU KV pool, tokens | 917,504 |
| Main KV | Q8 |
| Draft KV | Q8 |
| Speculation | mtp / depth 1 |
| Prefill chunk, tokens | 2,048 |
| Recurrent RAM checkpoint budget, MiB | 7,168 |
| Full unshared histories, pool arithmetic | 3 |
| KV left after one full history, tokens | 655,360 |

## Reproduce

Prepare the matching [tabby runtime](../../docs/REPRODUCING.md), then download the pinned checkpoint:

```bash
python3 scripts/download_model.py qwen3.8-27b-exl3 \
  --directory /path/to/models/qwen3.8-27b
```

Run from the repository root. Replace the example device ordinals with your own selection in layer/pipeline order:

```bash
bash recipes/qwen3.8-27b-exl3/launch.sh \
  --devices 0 \
  --runtime-root /path/to/prepared/runtimes \
  --model-path /path/to/models/qwen3.8-27b \
  --dry-run
```

`--dry-run` prints the command, environment and rendered config without importing a GPU runtime. Remove it to serve. The launcher runs in the foreground; Ctrl-C stops it.

The engine-native template is in [config.yml](config.yml).

## Interface

Choose the listener with `--host` and `--port`; see [launch options](../../docs/REPRODUCING.md#launch-options).

Endpoints: `/v1/models`, `/v1/chat/completions` and `/v1/completions`. Chat serving supports the selected engine's tool-call parser and a tool-result continuation.

## Measurements

Decode is accepted output tokens/s, including reasoning and excluding prefill. Concurrent rates are whole-wave aggregate. TTFT is the median first-token latency across the listed requests. Prefill is the backend's per-request timer, whose boundaries differ between engines. Output budgets are distinct from tokens counted inside the common decode interval.

| Actual input/request, tokens | Requests | Cache | Output budget/request, tokens | Decode total tok/s | Decode/request tok/s | TTFT median, s | Prefill/request tok/s | Draft acceptance % | End-to-end total tok/s | Test pool tokens / equivalents | Test context limit, tokens |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 32,769 | 1 | cold | 256 | 35.28 | 35.28 | 18.88 | 1,752.35 | 75.34 | 9.84 | 917,504 | 262,144 |
| 32,717 | 8 | cold | 256 | 105.36 | 13.67<br>12.67<br>13.17<br>13.42<br>13.92<br>12.43<br>12.92<br>13.17 | 156.95 | 215.64 | 75.49 | 11.60 | 917,504 | 262,144 |

Recorded per-request timers, accepted/proposed counts, decode intervals, cache-hit counters and source SHA256 references: [benchmarks.json](benchmarks.json). Unavailable fields remain null. The configured serving pool and each measured test pool are labeled separately.

The headline pair uses the [selected-serving prefill comparison](../../docs/PREFILL-COMPARISON.md), with zero verified cached input tokens and bulk RAM spilling disabled. The full numerical traces reproduce its synchronized decode values. Earlier results retain their original settings and remain separate.

## Verification

The shared runtime includes [long-history checkpoint retention](../../docs/PREFIX-REUSE.md).

| Check | Result |
| --- | --- |
| Historical validation checks | passed |
| Historical tested slots/replica | 16 |
| Native-context input stages, tokens | 131,072<br>261,632 |
| Native-context checks | passed |
| RAM history restoration | passed, main/MTP pages and recurrent checkpoints |

Allocation audits, per-card memory counters, task checks, quantization metadata and verification provenance: [evidence.json](evidence.json). [Data definitions](../../docs/DATA.md) explain measurement scope and missing fields.

## Tradeoffs

Standard Qwen3.8-27B with native MTP1. Current eight-slot performance has a separate approximately 32k-input / 256-output C1/C8 comparison. Historical three-replica results and the C2 retention check retain their original geometry.

## Qualification And Limits

- The context limit is per request; the KV pool is shared across requests and retained prefixes.
- Maximum-history counts are capacity arithmetic, not a long-context concurrent speed measurement.
- Current eight-slot C1/C8 performance is measured at approximately 32k input and 256 accepted output tokens; historical 16-slot/three-replica measurements remain separate.
- measured on the reference host; portable export not GPU-requalified.

This original recipe documentation and data are [CC BY 4.0](../../LICENSES/CC-BY-4.0.txt); attribute SourceHat and link to this recipe when sharing or adapting them. The checkpoint's own model license applies to downloaded weights. Runtime code and patches retain the licenses described in [THIRD_PARTY.md](../../THIRD_PARTY.md).
