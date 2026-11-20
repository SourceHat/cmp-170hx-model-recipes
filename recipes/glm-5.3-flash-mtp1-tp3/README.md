# GLM-5.3-Flash - MTP1 TP3

Recipe for NVIDIA CMP 170HX cards with 64 GiB usable VRAM.

| Parameter | Value |
| --- | --- |
| Checkpoint | [turboderp/GLM-5.3-Flash-exl3](https://huggingface.co/turboderp/GLM-5.3-Flash-exl3/tree/2a30229e67012798ba9f0cd832bb78abf4c363d5) |
| Checkpoint revision | `2a30229e67012798ba9f0cd832bb78abf4c363d5` |
| Quantization | EXL3 4.05 bpw |
| Runtime | TabbyAPI / ExLlamaV3 |
| Runtime version | ExLlamaV3 1.5.3 |
| Cards | 3 x 64 GiB SM80 |
| Layout | tensor parallel |
| OpenAI model id | `glm-5.3-flash` |
| Configured request slots | 4 |
| Per-request context, tokens | 524,288 |
| Shared GPU KV pool, tokens | 1,829,376 |
| Main KV | Q8 |
| Draft KV | Q8 |
| Speculation | mtp / depth 1 |
| Prefill chunk, tokens | 512 |
| Recurrent RAM checkpoint budget, MiB | 16,384 |
| Full unshared histories, pool arithmetic | 3 |
| KV left after one full history, tokens | 1,305,088 |
| Observed main GPU KV payload, GiB | 20.99 |
| Observed draft GPU KV payload, GiB | 1.91 |
| Observed host KV allocation, GiB | 0.00 |
| Observed peak VRAM/card, GiB | 61.59<br>61.00<br>61.80 |
| Memory observation phase | focused-stock-runtime |
| Output head format | EXL3 6 bpw |

## Reproduce

Prepare the matching [tabby runtime](../../docs/REPRODUCING.md), then download the pinned checkpoint:

```bash
python3 scripts/download_model.py glm-5.3-flash-mtp1-tp3 \
  --directory /path/to/models/glm-5.3-flash
```

Run from the repository root. Replace the example device ordinals with your own selection in layer/pipeline order:

```bash
bash recipes/glm-5.3-flash-mtp1-tp3/launch.sh \
  --devices 0,1,2 \
  --runtime-root /path/to/prepared/runtimes \
  --model-path /path/to/models/glm-5.3-flash \
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
| 32,766 | 1 | cold | 256 | 48.36 | 48.36 | 50.58 | 648.96 | 91.04 | 4.59 | 1,829,376 | 524,288 |
| 32,767 | 4 | cold | 256 | 100.65 | 25.50<br>24.98<br>24.78<br>25.39 | 199.02 | 169.76 | 85.17 | 4.88 | 1,829,376 | 524,288 |

<details>
<summary>Earlier measurements of these weights and decoding layout</summary>

These use the recorded earlier pool/context/runtime geometry. Full configurations and source references are included in the numerical export.

| Actual input/request, tokens | Requests | Cache | Output budget/request, tokens | Decode total tok/s | Decode/request tok/s | TTFT median, s | Prefill/request tok/s | Draft acceptance % | End-to-end total tok/s | Test pool tokens / equivalents | Test context limit, tokens |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 32,766 | 1 | cold | 256 | 48.85 | 48.85 | 49.44 | 663.95 | 84.17 | 4.69 | 262,144 | 262,144 |
| 32,766 | 1 | cached_prefix | 256 | 49.08 | 49.08 | 0.58 | 552.17 | 84.17 | 44.63 | 262,144 | 262,144 |
| 32,767 | 4 | cold | 256 | 98.59 | 24.30<br>24.00<br>25.29<br>25.00 | 199.40 | 168.87 | 82.21 | 4.88 | 262,144 | 262,144 |
| 32,767 | 4 | cached_prefix | 256 | 100.91 | 25.38<br>25.59<br>24.87<br>25.07 | 2.45 | 554.35 | 86.18 | 82.33 | 262,144 | 262,144 |

</details>

Recorded per-request timers, accepted/proposed counts, decode intervals, cache-hit counters and source SHA256 references: [benchmarks.json](benchmarks.json). Unavailable fields remain null. The configured serving pool and each measured test pool are labeled separately.

## Verification

The shared runtime includes [long-history checkpoint retention](../../docs/PREFIX-REUSE.md).

| Check | Result |
| --- | --- |
| Tool-call/result round trip | passed |
| Recorded target/reference checks | passed |
| Context check | passed |
| Context-check actual long input, tokens | 522,281 |
| Context-check pool, tokens | 1,829,376 |
| Concurrent requests in context check | 4 |
| Retrieval answer checked | yes |
| RAM history restoration | not retested |

Allocation audits, per-card memory counters, task checks, quantization metadata and verification provenance: [evidence.json](evidence.json). [Data definitions](../../docs/DATA.md) explain measurement scope and missing fields.

## Tradeoffs

Native MTP1/TP3. Additional mHC fusion did not establish a useful concurrent-serving gain in the recorded comparisons.

## Qualification And Limits

- The context limit is per request; the KV pool is shared across requests and retained prefixes.
- Maximum-history counts are capacity arithmetic, not a long-context concurrent speed measurement.
- measured on the reference host; portable export not GPU-requalified.

This original recipe documentation and data are [CC BY 4.0](../../LICENSES/CC-BY-4.0.txt); attribute SourceHat and link to this recipe when sharing or adapting them. The checkpoint's own model license applies to downloaded weights. Runtime code and patches retain the licenses described in [THIRD_PARTY.md](../../THIRD_PARTY.md).
