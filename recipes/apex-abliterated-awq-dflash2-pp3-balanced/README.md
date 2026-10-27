# Apex Flash 1 AWQ - abliterated, DFlash2 PP3 balanced

Recipe for NVIDIA CMP 170HX cards with 64 GiB usable VRAM.

**Model lineage:** Apex Flash 1 is Cantina Security and Yeta's reinforcement-learning post-train of **GLM-5.3-Flash** for security investigations. This recipe serves a quantization of the **abliterated Apex Flash 1 derivative**. The [publisher's model card](https://huggingface.co/cantina-security/apex-flash-1/tree/28c647a6bd0444973a7ef3d940c24c67e64f52fe) describes the standard Apex Flash 1 checkpoint; its benchmark results do not establish this derivative's quality.

| Parameter | Value |
| --- | --- |
| Checkpoint | [svbmrgd/apex-flash-1-abliterated-AWQ](https://huggingface.co/svbmrgd/apex-flash-1-abliterated-AWQ/tree/7ea31e3d22c6622c999d3de74d1569efce815943) |
| Checkpoint revision | `7ea31e3d22c6622c999d3de74d1569efce815943` |
| Quantization | AWQ INT4, group size 128; native non-routed tensors |
| Runtime | vLLM |
| Runtime version | 0.30.1rc1.dev640+g155488d85 |
| Cards | 3 x 64 GiB SM80 |
| Layout | pipeline parallel |
| OpenAI model id | `apex-flash-1-abliterated-awq` |
| Configured request slots | 4 |
| Per-request context, tokens | 524,288 |
| Context-normalized KV capacity, token-equivalents | 1,400,157 |
| Main KV | fp8_e4m3 |
| Draft KV | int8_per_token_head |
| Speculation | dflash2 / depth 3 |
| Prefill chunk, tokens | 512 |
| Recurrent RAM checkpoint budget, MiB | 0 |
| Full-context requests, sizing estimate | 2 |
| Capacity reporting context, tokens | 524,288 |
| PP layer partition | 17 / 15 / 13 |
| Automatic memory utilization | 0.985 |
| Draft checkpoint | [incoai/GLM-5.3-Flash-DFlash2](https://huggingface.co/incoai/GLM-5.3-Flash-DFlash2/tree/bf582e4eacc1810f76656d1811693ff6c6737d2a) |
| Draft weights | BF16; target-matched embedding |
| Observed main GPU KV payload, GiB | 11.19 |
| Observed draft GPU KV payload, GiB | 3.29 |
| Observed peak VRAM/card, GiB | 63.14<br>63.11<br>63.13 |
| Memory observation phase | balanced-final-pool-context-check |
| Routed-expert payload bits/parameter | 4.1250 |
| Main weight payload, bytes | 175,929,679,096 |
| Main logical parameters | 313,890,438,974 |
| Main payload bits/parameter | 4.4838 |
| Native MTP weights present | no |
| Base model | zai-org/GLM-5.3-Flash |
| Post-trained checkpoint | cantina-security/apex-flash-1 |
| Post-training method | reinforcement learning |
| Parent checkpoint | [cantina-security/apex-flash-1-abliterated](https://huggingface.co/cantina-security/apex-flash-1-abliterated/tree/cecb5eeb9c6b32404a0dd930df81de2c239bdd84) |

## Reproduce

Prepare the matching [apex-awq runtime](../../docs/REPRODUCING.md), then download the pinned checkpoint:

```bash
python3 scripts/download_model.py apex-abliterated-awq-dflash2-pp3-balanced \
  --directory /path/to/models/apex-flash-1-abliterated-awq
```

Run from the repository root. Replace the example device ordinals with your own selection in layer/pipeline order:

```bash
bash recipes/apex-abliterated-awq-dflash2-pp3-balanced/launch.sh \
  --devices 0,1,2 \
  --runtime-root /path/to/prepared/runtimes \
  --model-path /path/to/models/apex-flash-1-abliterated-awq \
  --draft-path /path/to/prepared-dflash2-head \
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
| 32,768 | 1 | cold | 256 | 36.92 | 36.92 | 17.53 | 1,875.77 | 47.04 | 10.49 | Not recorded | 524,288 |
| 32,768 | 4 | cold | 256 | 110.14 | 24.02<br>29.16<br>25.73<br>31.22 | 53.23 | Not recorded | 51.83 | 9.90 | Not recorded | 524,288 |

<details>
<summary>Earlier measurements of these weights and decoding layout</summary>

These use the recorded earlier pool/context/runtime geometry. Full configurations and source references are included in the numerical export.

| Actual input/request, tokens | Requests | Cache | Output budget/request, tokens | Decode total tok/s | Decode/request tok/s | TTFT median, s | Prefill/request tok/s | Draft acceptance % | End-to-end total tok/s | Test pool tokens / equivalents | Test context limit, tokens |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 32,765 | 1 | cold | 256 | 52.49 | 52.49 | 16.33 | Not recorded | 65.52 | 12.42 | 1,167,732 | 262,144 |
| 32,765 | 1 | repeated-input | 256 | 43.96 | 43.96 | 8.85 | Not recorded | 48.72 | 19.19 | 1,167,732 | 262,144 |
| 32,766 | 4 | cold | 256 | 128.47 | 34.06<br>27.49<br>37.05<br>29.88 | 65.92 | Not recorded | 57.42 | 10.00 | 1,167,732 | 262,144 |
| 32,766 | 4 | repeated-input | 256 | 116.06 | 30.11<br>29.27<br>28.25<br>28.42 | 34.95 | Not recorded | 58.40 | 22.60 | 1,167,732 | 262,144 |
| 32,771 | 1 | cold | 8,192 | 58.87 | Not recorded | 16.82 | 2,030.70 | 84.53 | Not recorded | 1,400,157 | 524,288 |
| 32,771 | 1 | cached_prefix | 8,192 | 62.32 | Not recorded | 8.15 | 1,996.58 | 93.45 | Not recorded | 1,400,157 | 524,288 |

</details>

Recorded per-request timers, accepted/proposed counts, decode intervals, cache-hit counters and source SHA256 references: [benchmarks.json](benchmarks.json). Unavailable fields remain null. The configured serving pool and each measured test pool are labeled separately.

The two 8,192-output observations retain [native prefill recovered from saved metric snapshots](../../docs/RECOVERED-PREFILL.md). Their prefill is kept with that exact workload; the older 256-output C1/C4 rows have no retained native timer.

The headline pair uses the [selected-serving prefill comparison](../../docs/PREFILL-COMPARISON.md), with zero verified cached input tokens and bulk RAM spilling disabled. The full numerical traces reproduce its synchronized decode values. Earlier results retain their original settings and remain separate.

The exported launch template retains an 8 GiB native offload budget; the timed headline jobs used zero. This setting differs explicitly, and the comparison does not establish an offload speedup or requalify the earlier capacity report.

## Verification

| Check | Result |
| --- | --- |
| Recorded target/reference checks | passed |
| Context check | passed |
| Context-check actual long input, tokens | 522,279 |
| Context-check normalized capacity, token-equivalents | 1,400,157 |
| Concurrent requests in context check | 4 |
| Retrieval answer checked | yes |
| RAM history restoration | not retested |

Allocation audits, per-card memory counters, task checks, quantization metadata and verification provenance: [evidence.json](evidence.json). [Data definitions](../../docs/DATA.md) explain measurement scope and missing fields.

## Tradeoffs

The 17/15/13 PP3 partition preserves much more KV than 17/14/14 with the same AWQ target weights. Historical 262,144-context short-output waves recorded higher decode throughput than the EXL3 comparison. The newer 524,288-context C1/C4 pair records 36.92/110.14 tok/s, with lower C1 decode than the retained EXL3 headline. These cohorts differ in inputs, settings, driver epoch and third physical card; they do not isolate a backend or quantization effect. AWQ uses a separate BF16 DFlash2 head.

## Qualification And Limits

The legacy `shared_gpu_pool_tokens` metadata field records vLLM's context-normalized capacity report: calculated full-context concurrency times the configured maximum context, rounded down. It uses cache-block requirements across groups, including sliding/compressed attention and state. It is not a literal count of resident token slots or free cache tokens, and the full-context sizing estimate is not a measured concurrency limit. See [data definitions](../../docs/DATA.md#memory-and-context).

- The context limit is per request; the KV pool is shared across requests and retained prefixes.
- Maximum-history counts are capacity arithmetic, not a long-context concurrent speed measurement.
- Balanced and fast use the same AWQ weights. Balanced PP3 17/15/13 was selected for its larger KV pool.
- The external BF16 DFlash2 head must be prepared with the matching target embedding; draft KV is INT8.
- The 8,192-output SSE measurement and 256-output server measurements use different timing methods.
- measured on the reference host; portable export not GPU-requalified.

This original recipe documentation and data are [CC BY 4.0](../../LICENSES/CC-BY-4.0.txt); attribute SourceHat and link to this recipe when sharing or adapting them. The checkpoint's own model license applies to downloaded weights. Runtime code and patches retain the licenses described in [THIRD_PARTY.md](../../THIRD_PARTY.md).
