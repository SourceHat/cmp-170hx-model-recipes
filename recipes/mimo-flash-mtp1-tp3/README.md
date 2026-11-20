# MiMo-V2.6-Flash - MTP1 TP3

Recipe for NVIDIA CMP 170HX cards with 64 GiB usable VRAM.

| Parameter | Value |
| --- | --- |
| Checkpoint | [MikeRoz/MiMo-V2.6-Flash-MOPD-4.03bpw-h8-exl3](https://huggingface.co/MikeRoz/MiMo-V2.6-Flash-MOPD-4.03bpw-h8-exl3/tree/29c8351a8b5854ec385adaeba7bbe62c790d40ea) |
| Checkpoint revision | `29c8351a8b5854ec385adaeba7bbe62c790d40ea` |
| Quantization | EXL3 4.03 bpw |
| Runtime | TabbyAPI / ExLlamaV3 |
| Runtime version | ExLlamaV3 1.5.3 |
| Cards | 3 x 64 GiB SM80 |
| Layout | tensor parallel |
| OpenAI model id | `mimo-v2.6-flash` |
| Configured request slots | 4 |
| Per-request context, tokens | 524,288 |
| Shared GPU KV pool, tokens | 1,070,848 |
| Main KV | Q8 |
| Draft KV | Q8 |
| Speculation | mtp / depth 1 |
| Prefill chunk, tokens | 512 |
| Recurrent RAM checkpoint budget, MiB | 16,384 |
| Full unshared histories, pool arithmetic | 2 |
| KV left after one full history, tokens | 546,560 |
| Observed main GPU KV payload, GiB | 14.65 |
| Observed draft GPU KV payload, GiB | 9.77 |
| Observed peak VRAM/card, GiB | 59.00<br>59.08<br>62.58 |
| Memory observation phase | final-pool-context-check |

## Reproduce

Prepare the matching [tabby runtime](../../docs/REPRODUCING.md), then download the pinned checkpoint:

```bash
python3 scripts/download_model.py mimo-flash-mtp1-tp3 \
  --directory /path/to/models/mimo-v2.6-flash
```

Run from the repository root. Replace the example device ordinals with your own selection in layer/pipeline order:

```bash
bash recipes/mimo-flash-mtp1-tp3/launch.sh \
  --devices 0,1,2 \
  --runtime-root /path/to/prepared/runtimes \
  --model-path /path/to/models/mimo-v2.6-flash \
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
| 2,038 | 1 | cold | 512 | 52.66 | 52.66 | 5.50 | 373.94 | 78.40 | 33.78 | 262,144 | 262,144 |
| 2,038 | 1 | cached_prefix | 512 | 55.16 | 55.16 | 0.49 | 572.09 | 86.86 | 52.70 | 262,144 | 262,144 |
| 2,039 | 4 | cold | 512 | 126.28 | 31.94<br>31.30<br>30.59<br>32.45 | 13.59 | 261.94 | 83.35 | 67.18 | 262,144 | 262,144 |
| 2,039 | 4 | cached_prefix | 512 | 126.80 | 32.43<br>30.48<br>30.94<br>32.95 | 2.06 | 561.36 | 81.08 | 112.01 | 262,144 | 262,144 |
| 32,765 | 1 | cold | 512 | 48.17 | 48.17 | 52.83 | 621.61 | 85.51 | 8.08 | 262,144 | 262,144 |
| 32,765 | 1 | cached_prefix | 512 | 48.45 | 48.45 | 0.65 | 468.52 | 85.51 | 45.87 | 262,144 | 262,144 |
| 32,766 | 4 | cold | 512 | 86.52 | 21.67<br>21.02<br>21.59<br>22.24 | 197.79 | 170.29 | 77.01 | 9.23 | 262,144 | 262,144 |
| 32,766 | 4 | cached_prefix | 512 | 86.64 | 21.50<br>21.67<br>21.58<br>21.89 | 2.70 | 470.37 | 76.86 | 78.37 | 262,144 | 262,144 |

Recorded per-request timers, accepted/proposed counts, decode intervals, cache-hit counters and source SHA256 references: [benchmarks.json](benchmarks.json). Unavailable fields remain null. The configured serving pool and each measured test pool are labeled separately.

## Verification

The shared runtime includes [long-history checkpoint retention](../../docs/PREFIX-REUSE.md).

| Check | Result |
| --- | --- |
| Recorded target/reference checks | passed |
| Context check | passed |
| Context-check actual long input, tokens | 522,285 |
| Context-check pool, tokens | 1,070,848 |
| Concurrent requests in context check | 4 |
| Retrieval answer checked | yes |
| RAM history restoration | not retested |

Allocation audits, per-card memory counters, task checks, quantization metadata and verification provenance: [evidence.json](evidence.json). [Data definitions](../../docs/DATA.md) explain measurement scope and missing fields.

## Tradeoffs

Native MTP1 with tensor parallelism across three cards. Throughput, cache precision and context checks are reported separately.

## Qualification And Limits

- The context limit is per request; the KV pool is shared across requests and retained prefixes.
- Maximum-history counts are capacity arithmetic, not a long-context concurrent speed measurement.
- measured on the reference host; portable export not GPU-requalified.

This original recipe documentation and data are [CC BY 4.0](../../LICENSES/CC-BY-4.0.txt); attribute SourceHat and link to this recipe when sharing or adapting them. The checkpoint's own model license applies to downloaded weights. Runtime code and patches retain the licenses described in [THIRD_PARTY.md](../../THIRD_PARTY.md).
