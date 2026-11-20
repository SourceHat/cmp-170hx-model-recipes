# Qwen3.8-27B Orca - abliterated, adaptive native MTP up to 3

Recipe for NVIDIA CMP 170HX cards with 64 GiB usable VRAM.

| Parameter | Value |
| --- | --- |
| Checkpoint | [Lygodactylus/Qwen3.8-27B-Uncensored-exl3-8bpw](https://huggingface.co/Lygodactylus/Qwen3.8-27B-Uncensored-exl3-8bpw/tree/3487b152b302930e303dc4a2e99e7e976e3ad28f) |
| Checkpoint revision | `3487b152b302930e303dc4a2e99e7e976e3ad28f` |
| Quantization | EXL3 8 bpw |
| Runtime | TabbyAPI / ExLlamaV3 |
| Runtime version | ExLlamaV3 1.5.3 |
| Cards | 1 x 64 GiB SM80 |
| Layout | layer split |
| OpenAI model id | `qwen27-orca-exl3-8bpw` |
| Configured request slots | 8 |
| Per-request context, tokens | 262,144 |
| Shared GPU KV pool, tokens | 866,560 |
| Main KV | Q8 |
| Draft KV | Q8 |
| Speculation | mtp / up to 3 (adaptive) |
| Prefill chunk, tokens | 512 |
| Recurrent RAM checkpoint budget, MiB | 16,384 |
| Full unshared histories, pool arithmetic | 3 |
| KV left after one full history, tokens | 604,416 |
| Observed main GPU KV payload, GiB | 28.10 |
| Observed draft GPU KV payload, GiB | 1.76 |
| Observed peak VRAM/card, GiB | 60.92 |
| Memory observation phase | native-final-pool-sampled-peaks |

## Reproduce

Prepare the matching [tabby runtime](../../docs/REPRODUCING.md), then download the pinned checkpoint:

```bash
python3 scripts/download_model.py qwen27-orca-mtp3-native \
  --directory /path/to/models/qwen27-orca-exl3-8bpw
```

Run from the repository root. Replace the example device ordinals with your own selection in layer/pipeline order:

```bash
bash recipes/qwen27-orca-mtp3-native/launch.sh \
  --devices 0 \
  --runtime-root /path/to/prepared/runtimes \
  --model-path /path/to/models/qwen27-orca-exl3-8bpw \
  --dry-run
```

`--dry-run` prints the command, environment and rendered config without importing a GPU runtime. Remove it to serve. The launcher runs in the foreground; Ctrl-C stops it.

The engine-native template is in [config.yml](config.yml).

## Interface

Choose the listener with `--host` and `--port`; see [launch options](../../docs/REPRODUCING.md#launch-options).

Endpoints: `/v1/models`, `/v1/chat/completions` and `/v1/completions`. Chat serving supports the selected engine's tool-call parser and a tool-result continuation.

## Measurements

These retained throughput waves used fixed MTP3. The current recipe uses adaptive MTP up to three; [later live serving checks](../../docs/MIXED-SERVING.md) are a separate dataset.

Decode is accepted output tokens/s, including reasoning and excluding prefill. Concurrent rates are whole-wave aggregate. TTFT is the median first-token latency across the listed requests. Prefill is the backend's per-request timer, whose boundaries differ between engines. Output budgets are distinct from tokens counted inside the common decode interval.

| Actual input/request, tokens | Requests | Cache | Output budget/request, tokens | Decode total tok/s | Decode/request tok/s | TTFT median, s | Prefill/request tok/s | Draft acceptance % | End-to-end total tok/s | Test pool tokens / equivalents | Test context limit, tokens |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2,026 | 1 | cold | 256 | 60.57 | 60.57 | 1.58 | 1,324.18 | 62.55 | 44.96 | 866,560 | 262,144 |
| 2,026 | 1 | cached_prefix | 512 | 64.49 | 64.49 | 0.44 | 806.90 | 66.47 | 62.03 | 866,560 | 262,144 |
| 2,027 | 8 | cold | 256 | 189.79 | 24.26<br>24.47<br>24.47<br>23.19<br>23.19<br>23.19<br>23.51<br>23.51 | 12.14 | 260.54 | 57.69 | 87.67 | 866,560 | 262,144 |
| 2,027 | 8 | cached_prefix | 512 | 204.10 | 25.84<br>25.89<br>25.78<br>25.73<br>25.15<br>25.15<br>25.20<br>25.36 | 3.26 | 783.33 | 59.74 | 178.13 | 866,560 | 262,144 |
| 32,769 | 1 | cold | 256 | 47.49 | 47.49 | 24.57 | 1,339.70 | 59.42 | 8.58 | 866,560 | 262,144 |
| 32,769 | 1 | repeated-input | 512 | 46.69 | 46.69 | 24.70 | 1,333.16 | 57.93 | 14.42 | 866,560 | 262,144 |
| 32,770 | 8 | cold | 256 | 112.38 | 14.12<br>13.69<br>14.50<br>14.50<br>14.50<br>13.75<br>14.06<br>13.26 | 200.45 | 168.01 | 64.33 | 9.39 | 866,560 | 262,144 |
| 32,770 | 8 | cached_prefix | 512 | 111.33 | 13.09<br>13.86<br>13.86<br>14.20<br>14.40<br>13.94<br>13.94<br>14.03 | 1.94 | 50.00 | 62.61 | 107.95 | 866,560 | 262,144 |

<details>
<summary>Earlier measurements of these weights and decoding layout</summary>

These use the recorded earlier pool/context/runtime geometry. Full configurations and source references are included in the numerical export.

| Actual input/request, tokens | Requests | Cache | Output budget/request, tokens | Decode total tok/s | Decode/request tok/s | TTFT median, s | Prefill/request tok/s | Draft acceptance % | End-to-end total tok/s | Test pool tokens / equivalents | Test context limit, tokens |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2,026 | 1 | cold | 512 | 62.12 | 62.12 | 1.69 | 1,282.28 | 65.89 | 52.23 | 524,288 | 262,144 |
| 2,026 | 1 | cached_prefix | 512 | 63.22 | 63.22 | 0.41 | 806.90 | 66.47 | 60.73 | 524,288 | 262,144 |
| 2,027 | 8 | cold | 512 | 197.09 | 24.95<br>25.00<br>24.90<br>24.85<br>24.28<br>24.28<br>24.34<br>24.49 | 11.59 | 255.00 | 59.74 | 122.61 | 524,288 | 262,144 |
| 2,027 | 8 | cached_prefix | 512 | 200.96 | 25.42<br>25.42<br>25.42<br>25.32<br>24.74<br>24.84<br>24.79<br>25.00 | 3.35 | 783.33 | 59.80 | 175.36 | 524,288 | 262,144 |
| 32,769 | 1 | cold | 512 | 46.38 | 46.38 | 24.69 | 1,333.16 | 57.93 | 14.40 | 524,288 | 262,144 |
| 32,769 | 1 | repeated-input | 512 | 46.09 | 46.09 | 24.87 | 1,327.22 | 57.93 | 14.32 | 524,288 | 262,144 |
| 32,770 | 8 | cold | 512 | 111.81 | 13.87<br>14.65<br>13.63<br>13.75<br>14.11<br>14.08<br>13.96<br>13.75 | 200.43 | 169.15 | 63.98 | 17.32 | 524,288 | 262,144 |
| 32,770 | 8 | cached_prefix | 512 | 111.74 | 13.83<br>14.63<br>13.66<br>13.78<br>14.13<br>13.98<br>13.95<br>13.78 | 2.58 | 50.00 | 63.98 | 106.79 | 524,288 | 262,144 |

</details>

Recorded per-request timers, accepted/proposed counts, decode intervals, cache-hit counters and source SHA256 references: [benchmarks.json](benchmarks.json). Unavailable fields remain null. The configured serving pool and each measured test pool are labeled separately.

## Verification

The shared runtime includes [long-history checkpoint retention](../../docs/PREFIX-REUSE.md).

| Check | Result |
| --- | --- |
| Context check | passed |
| Context-check actual long input, tokens | 253,996 |
| Context-check pool, tokens | 866,560 |
| Concurrent requests in context check | 8 |
| Retrieval answer checked | yes |
| RAM history restoration | passed |

Allocation audits, per-card memory counters, task checks, quantization metadata and verification provenance: [evidence.json](evidence.json). [Data definitions](../../docs/DATA.md) explain measurement scope and missing fields.

## Tradeoffs

MTP3 on one 64 GiB card. The recorded context check includes retrieval and RAM history restoration.

## Qualification And Limits

- The context limit is per request; the KV pool is shared across requests and retained prefixes.
- Maximum-history counts are capacity arithmetic, not a long-context concurrent speed measurement.
- Current serving enables adaptive MTP up to three tokens. Retained recipe throughput waves used fixed MTP3; later serving checks are reported separately.
- measured on the reference host; portable export not GPU-requalified.

This original recipe documentation and data are [CC BY 4.0](../../LICENSES/CC-BY-4.0.txt); attribute SourceHat and link to this recipe when sharing or adapting them. The checkpoint's own model license applies to downloaded weights. Runtime code and patches retain the licenses described in [THIRD_PARTY.md](../../THIRD_PARTY.md).
