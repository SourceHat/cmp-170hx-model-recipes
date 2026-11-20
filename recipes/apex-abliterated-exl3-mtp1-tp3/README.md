# Apex Flash 1 EXL3 - abliterated, MTP1 TP3

Recipe for NVIDIA CMP 170HX cards with 64 GiB usable VRAM.

**Model lineage:** Apex Flash 1 is Cantina Security and Yeta's reinforcement-learning post-train of **GLM-5.3-Flash** for security investigations. This recipe serves a quantization of the **abliterated Apex Flash 1 derivative**. The [publisher's model card](https://huggingface.co/cantina-security/apex-flash-1/tree/28c647a6bd0444973a7ef3d940c24c67e64f52fe) describes the standard Apex Flash 1 checkpoint; its benchmark results do not establish this derivative's quality.

| Parameter | Value |
| --- | --- |
| Checkpoint | [SloptimistPrime/apex-flash-1-abliterated-EXL3-4bit-DGX-Spark](https://huggingface.co/SloptimistPrime/apex-flash-1-abliterated-EXL3-4bit-DGX-Spark/tree/a4c922dc57dae44a9569ec82a08a2f311636e2a6) |
| Checkpoint revision | `a4c922dc57dae44a9569ec82a08a2f311636e2a6` |
| Quantization | EXL3 4.37 effective bpw; mixed tensor precision |
| Runtime | TabbyAPI / ExLlamaV3 |
| Runtime version | ExLlamaV3 1.5.3 |
| Cards | 3 x 64 GiB SM80 |
| Layout | tensor parallel |
| OpenAI model id | `apex-flash-1-abliterated-exl3-4bit-spark` |
| Configured request slots | 4 |
| Per-request context, tokens | 524,288 |
| Shared GPU KV pool, tokens | 1,374,976 |
| Main KV | Q8 |
| Draft KV | Q8 |
| Speculation | mtp / depth 1 |
| Prefill chunk, tokens | 512 |
| Recurrent RAM checkpoint budget, MiB | 16,384 |
| Full unshared histories, pool arithmetic | 2 |
| KV left after one full history, tokens | 850,688 |
| Observed main GPU KV payload, GiB | 15.78 |
| Observed draft GPU KV payload, GiB | 1.43 |
| Observed peak VRAM/card, GiB | 63.37<br>63.42<br>63.74 |
| Memory observation phase | two-load-q8-capacity-qualification |
| Peak VRAM accounting | NVML total minus physical free bytes, all processes and driver reservations included; maximum across the two recorded load intervals. |
| Autosplit reserve by selected GPU rank, MiB | 2,560<br>2,336<br>2,848 |
| Output head format | Native 16-bit |
| MTP expert format | EXL3 4 bpw |
| Routed-expert payload bits/parameter | 4.0117 |
| Main weight payload, bytes | 171,618,809,848 |
| Main logical parameters | 313,890,438,974 |
| Main payload bits/parameter | 4.3740 |
| Native MTP weights present | yes |
| Complete checkpoint files including MTP, bytes | 175,642,473,288 |
| Complete checkpoint logical parameters | 321,323,031,390 |
| Complete checkpoint effective bpw | 4.37298 |
| Effective bpw calculation | `8 * stored weight bytes / logical parameters` (matching tensor scope) |
| Base model | zai-org/GLM-5.3-Flash |
| Post-trained checkpoint | cantina-security/apex-flash-1 |
| Post-training method | reinforcement learning |
| Parent checkpoint | [cantina-security/apex-flash-1-abliterated](https://huggingface.co/cantina-security/apex-flash-1-abliterated/tree/cecb5eeb9c6b32404a0dd930df81de2c239bdd84) |

## Reproduce

Prepare the matching [tabby runtime](../../docs/REPRODUCING.md), then download the pinned checkpoint:

```bash
python3 scripts/download_model.py apex-abliterated-exl3-mtp1-tp3 \
  --directory /path/to/models/apex-flash-1-abliterated-exl3-4bit-spark
```

Run from the repository root. Replace the example device ordinals with your own selection in layer/pipeline order:

```bash
bash recipes/apex-abliterated-exl3-mtp1-tp3/launch.sh \
  --devices 0,1,2 \
  --runtime-root /path/to/prepared/runtimes \
  --model-path /path/to/models/apex-flash-1-abliterated-exl3-4bit-spark \
  --dry-run
```

`--dry-run` prints the command, environment and rendered config without importing a GPU runtime. Remove it to serve. The launcher runs in the foreground; Ctrl-C stops it.

The engine-native template is in [config.yml](config.yml).

## Interface

Choose the listener with `--host` and `--port`; see [launch options](../../docs/REPRODUCING.md#launch-options).

Endpoints: `/v1/models`, `/v1/chat/completions` and `/v1/completions`. Chat serving supports the selected engine's tool-call parser and a tool-result continuation.

## Resident KV Qualification

The selected **1,374,976-token Q8/Q8 pool** is **26.9% larger** than the earlier allocation. It retains four slots, a 524,288-token per-request context and fixed MTP1 with adaptation disabled. Two independent reference-host loads passed mixed prefill/decode, output growth on all slots, near-context retrieval, tool-call/result continuation, cancellation and recurrent prefix reuse.

| Independent load | Distinct history input, tokens | Fraction of pool | Peak active slots | Lowest physical free memory/card, MiB |
| --- | --- | --- | --- | --- |
| 1 | 1,312,746 | 95.47% | 4 | 291.06 |
| 2 | 1,312,405 | 95.45% | 4 | 271.06 |

Each load exercised distinct histories above 95% of the pool. The memory guard requires at least 256 MiB physically free on every selected GPU throughout the recorded sampling interval. This is a bounded qualification on those devices, not an exhaustive capacity search or four simultaneous maximum-length histories. Bulk host KV spilling stays off; the 16 GiB recurrent-checkpoint budget is separate.

The main-model autosplit reserves are **2,560 / 2,336 / 2,848 MiB** in selected GPU-rank order. The last selected GPU also carries the draft. The reference order is CPU Gen2 x8, CPU Gen2 x4, PCH Gen2 x4; preserve the rank order or retune for different devices.

The performance table below retains its earlier **1,083,136-token** test pool and placement. Later completion-rate probes varied by workload and load and use a different backend timer; they are retained in the qualification data and are not substituted for synchronized aggregate decode.

[Numerical capacity evidence](../../data/apex-kv-capacity/evidence.json) | [Two-load source report](../../data/apex-kv-capacity/qualification-report.json) | [Saved profile](../../data/apex-kv-capacity/saved-profile.json). Run `python3 scripts/apex_capacity.py` from the repository root to verify the included source identities, capacity arithmetic and recipe settings.

## Measurements

Decode is accepted output tokens/s, including reasoning and excluding prefill. Concurrent rates are whole-wave aggregate. TTFT is the median first-token latency across the listed requests. Prefill is the backend's per-request timer, whose boundaries differ between engines. Output budgets are distinct from tokens counted inside the common decode interval.

| Actual input/request, tokens | Requests | Cache | Output budget/request, tokens | Decode total tok/s | Decode/request tok/s | TTFT median, s | Prefill/request tok/s | Draft acceptance % | End-to-end total tok/s | Test pool tokens / equivalents | Test context limit, tokens |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 32,766 | 1 | cold | 256 | 40.09 | 40.09 | 50.61 | 648.57 | 82.86 | 4.50 | 1,083,136 | 524,288 |
| 32,767 | 4 | cold | 256 | 98.49 | 25.00<br>25.50<br>23.49<br>24.50 | 202.01 | 165.02 | 82.53 | 4.82 | 1,083,136 | 524,288 |

<details>
<summary>Earlier measurements of these weights and decoding layout</summary>

These use the recorded earlier pool/context/runtime geometry. Full configurations and source references are included in the numerical export.

| Actual input/request, tokens | Requests | Cache | Output budget/request, tokens | Decode total tok/s | Decode/request tok/s | TTFT median, s | Prefill/request tok/s | Draft acceptance % | End-to-end total tok/s | Test pool tokens / equivalents | Test context limit, tokens |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 32,766 | 1 | cold | 256 | 41.86 | 41.86 | 51.17 | 641.46 | 77.78 | 4.47 | 262,144 | 262,144 |
| 32,766 | 1 | cached_prefix | 256 | 44.22 | 44.22 | 0.64 | 540.43 | 85.51 | 40.36 | 262,144 | 262,144 |
| 32,767 | 4 | cold | 256 | 95.28 | 24.02<br>24.40<br>23.43<br>23.43 | 200.95 | 167.95 | 82.86 | 4.83 | 262,144 | 262,144 |
| 32,767 | 4 | cached_prefix | 256 | 99.38 | 24.77<br>25.27<br>25.17<br>24.17 | 2.44 | 542.55 | 84.84 | 80.56 | 262,144 | 262,144 |

</details>

Recorded per-request timers, accepted/proposed counts, decode intervals, cache-hit counters and source SHA256 references: [benchmarks.json](benchmarks.json). Unavailable fields remain null. The configured serving pool and each measured test pool are labeled separately.

## Earlier Verification

The shared runtime includes [long-history checkpoint retention](../../docs/PREFIX-REUSE.md).

| Check | Result |
| --- | --- |
| Tool-call/result round trip | passed |
| Recorded target/reference checks | passed |
| Context check | passed |
| Context-check actual long input, tokens | 522,281 |
| Context-check pool, tokens | 1,083,136 |
| Concurrent requests in context check | 4 |
| Retrieval answer checked | yes |
| RAM history restoration | not retested |

Allocation audits, per-card memory counters, task checks, quantization metadata and verification provenance: [evidence.json](evidence.json). [Data definitions](../../docs/DATA.md) explain measurement scope and missing fields.

## Tradeoffs

EXL3 with native MTP. Routed experts are quantized while non-routed tensors retain their source precision. The small task checks do not establish general quality superiority over AWQ.

## Qualification And Limits

- The context limit is per request; the KV pool is shared across requests and retained prefixes.
- Maximum-history counts are capacity arithmetic, not a long-context concurrent speed measurement.
- Routed experts are four-bit; attention/shared/head tensors retain source precision.
- The 1,374,976-token resident pool is qualified on the reference host; the 32k headline speed observations retain their earlier 1,083,136-token test pool.
- Autosplit reserves are 2,560 / 2,336 / 2,848 MiB in selected GPU-rank order. Preserve that device order or retune the allocation for a different placement.
- measured on the reference host; portable export not GPU-requalified.

This original recipe documentation and data are [CC BY 4.0](../../LICENSES/CC-BY-4.0.txt); attribute SourceHat and link to this recipe when sharing or adapting them. The checkpoint's own model license applies to downloaded weights. Runtime code and patches retain the licenses described in [THIRD_PARTY.md](../../THIRD_PARTY.md).
