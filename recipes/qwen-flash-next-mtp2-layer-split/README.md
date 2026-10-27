# Qwen3.8-Flash-Next - MTP2 layer split

Recipe for NVIDIA CMP 170HX cards with 64 GiB usable VRAM.

| Parameter | Value |
| --- | --- |
| Checkpoint | [turboderp/Qwen3.8-Flash-Next-exl3](https://huggingface.co/turboderp/Qwen3.8-Flash-Next-exl3/tree/d2e238feca4c1c4d966943117356d8a42c2f4dcb) |
| Checkpoint revision | `d2e238feca4c1c4d966943117356d8a42c2f4dcb` |
| Quantization | EXL3 6.05 bpw |
| Runtime | TabbyAPI / ExLlamaV3 |
| Runtime version | ExLlamaV3 1.5.3 |
| Cards | 2 x 64 GiB SM80 |
| Layout | layer split |
| OpenAI model id | `qwen3.8-flash-next` |
| Configured request slots | 6 |
| Per-request context, tokens | 262,144 |
| Shared GPU KV pool, tokens | 1,356,032 |
| Main KV | Q8 |
| Draft KV | Q8 |
| Speculation | mtp / depth 2 |
| Prefill chunk, tokens | 512 |
| Recurrent RAM checkpoint budget, MiB | 16,384 |
| Full unshared histories, pool arithmetic | 5 |
| KV left after one full history, tokens | 1,093,888 |
| Observed main GPU KV payload, GiB | 21.34 |
| Observed draft GPU KV payload, GiB | 1.78 |
| Observed host KV allocation, GiB | 0.00 |
| Observed peak VRAM/card, GiB | 60.35<br>60.50 |
| Memory observation phase | focused-stock-runtime |
| Output head format | EXL3 6 bpw |
| MTP expert format | EXL3 6 bpw |

## Reproduce

Prepare the matching [tabby runtime](../../docs/REPRODUCING.md), then download the pinned checkpoint:

```bash
python3 scripts/download_model.py qwen-flash-next-mtp2-layer-split \
  --directory /path/to/models/qwen3.8-flash-next
```

Run from the repository root. Replace the example device ordinals with your own selection in layer/pipeline order:

```bash
bash recipes/qwen-flash-next-mtp2-layer-split/launch.sh \
  --devices 0,1 \
  --runtime-root /path/to/prepared/runtimes \
  --model-path /path/to/models/qwen3.8-flash-next \
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
| 32,769 | 1 | cold | 256 | 74.79 | 74.79 | 24.60 | 1,336.96 | 80.61 | 9.16 | 1,356,032 | 262,144 |
| 32,770 | 6 | cold | 256 | 136.71 | 21.51<br>23.12<br>22.46<br>23.49<br>23.02<br>23.12 | 147.66 | 228.59 | 74.88 | 9.67 | 1,356,032 | 262,144 |

<details>
<summary>Earlier measurements of these weights and decoding layout</summary>

These use the recorded earlier pool/context/runtime geometry. Full configurations and source references are included in the numerical export.

| Actual input/request, tokens | Requests | Cache | Output budget/request, tokens | Decode total tok/s | Decode/request tok/s | TTFT median, s | Prefill/request tok/s | Draft acceptance % | End-to-end total tok/s | Test pool tokens / equivalents | Test context limit, tokens |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 32,769 | 1 | cold | 256 | 73.10 | 73.10 | 24.90 | 1,321.33 | 78.00 | 9.04 | 1,356,032 | 524,288 |
| 32,769 | 1 | repeated-input | 512 | 76.87 | 76.87 | 24.84 | 1,324.54 | 83.33 | 16.29 | 1,356,032 | 524,288 |
| 32,770 | 6 | cold | 256 | 136.23 | 21.43<br>21.90<br>22.56<br>23.13<br>23.60<br>23.60 | 148.91 | 226.86 | 78.64 | 9.61 | 1,356,032 | 524,288 |
| 32,770 | 6 | cached_prefix | 512 | 135.31 | 22.30<br>21.60<br>22.57<br>23.22<br>22.94<br>22.67 | 1.26 | 100.00 | 82.19 | 130.46 | 1,356,032 | 524,288 |
| 32,769 | 1 | cold | 256 | 76.31 | 76.31 | 24.59 | 1,337.51 | 80.61 | 9.18 | 262,144 | 262,144 |
| 32,769 | 1 | repeated-input | 256 | 76.33 | 76.33 | 24.63 | 1,336.96 | 80.61 | 9.18 | 262,144 | 262,144 |
| 32,770 | 6 | cold | 256 | 132.77 | 20.96<br>22.62<br>22.44<br>22.16<br>22.07<br>22.53 | 147.64 | 228.07 | 75.49 | 9.66 | 262,144 | 262,144 |
| 32,770 | 6 | cached_prefix | 256 | 130.23 | 22.52<br>21.37<br>22.04<br>21.85<br>21.28<br>21.18 | 1.21 | 100.00 | 74.68 | 121.15 | 262,144 | 262,144 |

</details>

Recorded per-request timers, accepted/proposed counts, decode intervals, cache-hit counters and source SHA256 references: [benchmarks.json](benchmarks.json). Unavailable fields remain null. The configured serving pool and each measured test pool are labeled separately.

## Verification

The shared runtime includes [long-history checkpoint retention](../../docs/PREFIX-REUSE.md).

| Check | Result |
| --- | --- |
| Tool-call/result round trip | passed |

Allocation audits, per-card memory counters, task checks, quantization metadata and verification provenance: [evidence.json](evidence.json). [Data definitions](../../docs/DATA.md) explain measurement scope and missing fields.

## Tradeoffs

MTP2 layer split provides a larger shared KV pool and lower cold first-token latency than the measured TP2 alternatives. Depth/layout comparisons are included in the numerical evidence.

## Qualification And Limits

- The context limit is per request; the KV pool is shared across requests and retained prefixes.
- Maximum-history counts are capacity arithmetic, not a long-context concurrent speed measurement.
- PLE/n-gram weights are resident in host RAM; host memory is uncapped.
- The native 262,144-token limit was retained without a new near-limit native-context test.
- measured on the reference host; portable export not GPU-requalified.

This original recipe documentation and data are [CC BY 4.0](../../LICENSES/CC-BY-4.0.txt); attribute SourceHat and link to this recipe when sharing or adapting them. The checkpoint's own model license applies to downloaded weights. Runtime code and patches retain the licenses described in [THIRD_PARTY.md](../../THIRD_PARTY.md).
