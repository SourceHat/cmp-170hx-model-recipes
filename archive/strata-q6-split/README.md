# Strata Q6 / layer split

**Archived historical configuration.** EXL3/MTP2 layer split remained selected after review of resident KV capacity, host-backed operation and the retained 32k workload results.

The recommended alternative is [Qwen3.8-Flash-Next EXL3 / MTP2 layer split](../../recipes/qwen-flash-next-mtp2-layer-split/README.md).
This archive preserves the tested settings and numeric evidence. Its native
Strata server template requires your own runtime setup; the repository's
recipe launcher does not support this archived runtime.

## Model And Runtime

| Setting | Recorded value |
| --- | --- |
| Model | Qwen 3.8 Qwen3.8-Flash-Next |
| Main artifact | [unsloth/Qwen3.8-Flash-Next-GGUF](https://huggingface.co/unsloth/Qwen3.8-Flash-Next-GGUF/tree/38bb39ee97821de2c9009abb7e93950eec396e66/UD-Q6_K_XL) |
| Main revision | `38bb39ee97821de2c9009abb7e93950eec396e66` |
| Main quantization | UD-Q6_K_XL (mixed tensor formats) |
| MTP source | [Qwen/Qwen3.8-Flash-Next](https://huggingface.co/Qwen/Qwen3.8-Flash-Next/tree/de4b8e4d43b917e7706784d8bb445c9af86a3540) |
| MTP revision | `de4b8e4d43b917e7706784d8bb445c9af86a3540` |
| MTP expert format | Q2_0, 2.25 stored bits/weight |
| Runtime | [Strata 0.1.42](https://github.com/Niko1221/Strata/tree/61b3fb5dd3f1e8ec09cf7e4e05208bc6d3c46406) |
| Runtime revision | `61b3fb5dd3f1e8ec09cf7e4e05208bc6d3c46406` |
| Required cards | 2 x CMP 170HX, 64 GiB usable VRAM each, SM80 |
| Measurement power limit | 200 W/card |
| Build | CMAKE_BUILD_TYPE=Release, CMAKE_CUDA_ARCHITECTURES=80, STRATA_ENABLE_CUDA=ON, STRATA_MMQ_KQUANTS=ON, STRATA_NATIVE_EXPERTS=ON, STRATA_Q6K_EXPERTS=ON, STRATA_PREFILL_MMQ=OFF |

Exact shard names, recorded binary hash and build settings are in [profile.json](profile.json). [runtime.json](../runtime.json) pins Strata and its llama.cpp dependency and identifies the included allocation-audit patch.

## Context And Memory

| Setting / observation | Value |
| --- | --- |
| Configured context limit per request, tokens | 262,144 |
| Allocated batch slots | 6 |
| Main / draft KV | INT8 / INT8, allocation-audited |
| Resident GPU KV per batch slot, tokens | 32,768 |
| Resident batch GPU KV, tokens | 196,608 |
| Logical host-backed batch capacity, tokens | 1,572,864 |
| Separate solo GPU workspace, tokens | 32,768 |
| Separate solo logical capacity, tokens | 262,144 |
| Observed host KV allocation, GiB | 21.91 |
| Sampled peak VRAM per measurement card, GiB | 59.89<br>61.25 |
| Resident expert cache, GiB | 101.75 |
| Requested speculation / observed maximum verification, tokens | 4 / 6 |
| Maximum native MTP window, tokens | 4 |
| Batch MTP | Off in the observed allocation; native MTP weights loaded |
| Prompt-lookup n-gram length | 3 |

Each batch slot has 32,768 resident GPU tokens within its configured
262,144-token logical capacity. The remaining history uses host-backed operation;
simultaneous full-context requests were not qualified.
The separate solo workspace is not added to the batch pool. The small resident
workspace can require host transfers as active histories grow; their effect
near the configured context limit was not measured.

This historical Strata mechanism backs active KV with host memory; its
recorded settings remain distinct from the selected Tabby recipes.

## Measured Results

One cold wave per mode: a synthetic coding prompt targeting 32,768 input
tokens and 256 accepted output tokens per request, temperature zero, seed
`20261008`, low reasoning effort. Actual input counts appear in the table.
Accepted reasoning tokens count toward output. These are individual waves,
not averages across repeated runs.

| Configuration | Wave requests | Actual input tokens/request | Shared decode tok/s total | Whole-wave output tok/s | Median TTFT, s | Slowest TTFT, s |
| --- | --- | --- | --- | --- | --- | --- |
| Strata Q6 / layer split | 1 | 32,769 | 85.43 | 12.02 | 18.31 | 18.31 |
| Strata Q6 / layer split | 6 | 32,770 | 178.89 | 12.76 | 65.29 | 111.82 |

Shared decode excludes prefill and counts accepted tokens only between the
last request's first generation event and the first completion. Whole-wave
throughput includes prefill, queueing and generation. First-token times
include queueing. A dash means no qualified common decode interval.

Exact intervals, accepted-token numerators, per-request arrays, draft counts and source receipts: [benchmarks.json](benchmarks.json). [evidence.json](evidence.json) preserves memory/precision audits, tensor formats, artifact hashes and verification. The combined [archive CSV](../benchmarks.csv) contains these four waves separately from the recommended recipes.

## Historical Configuration

[engine-config.json](engine-config.json) preserves the original native engine
arguments and server settings, with deployment values replaced by placeholders:

| Placeholder | Supply |
| --- | --- |
| `@STRATA_BINARY@` | Your SM80 Strata build matching the recorded variant |
| `@STRATA_SOURCE@` | Pinned Strata checkout, also used for its expert profile |
| `@MODEL_ROOT@` | Directory containing all pinned GGUF shards in their quantization subdirectory |
| `@PACK@` | Dense/tokenizer pack produced by the pinned iq_pack.py with --compat-bf16 |
| `@MTP_PACK@` | Native MTP runtime pack from the pinned source, Q2_0 experts |
| `@PLE_GGUF@` | Lossless PLE-only GGUF view; layout and hash retained in evidence.json |
| `@DEVICES@` | Your ordered device selection, using the recorded card count |
| `@MODEL_NAME@`, `@HOST@`, `@PORT@` | Your served name and listener |
| `@API_KEY@`, `@LOG_PATH@` | Your server credential and log destination |

The historical build included the metadata-only [allocation-audit patch](../runtime/kv-allocation.patch).
Its [MIT notice](../runtime/LICENSE.Strata.txt) is retained. The original serving
wrapper and a portable Strata installer/launcher are not included; the template
has not been GPU-reproduced from this checkout. No model weights or compiled
binaries are redistributed.

## Limits And Selection

- Only approximately 32k-input / 256-output performance workloads were measured.
- The configured context is not a near-limit context, retrieval or general quality qualification.
- Logical host-backed capacity is not fully resident GPU KV and does not prove maximum-context concurrency.
- The separate solo workspace must not be added to the batch pool.
- Strata host-backed active KV differs from the optional evicted-prefix RAM tier in the recommended Tabby recipes.

The recorded tool round trip passed. The legacy completions adapter was CPU-verified after the GPU trial; this archive does not export that adapter or claim complete API compatibility.
The Q6 expert, grouped-expert and MMQ K-quant parity checks also passed.

No paired general-quality comparison establishes the quality loss from IQ4 versus Q6 or EXL3. Hardware, runtime and quantization differ between alternatives, so their speed differences do not isolate a single cause.

[Archive index](../README.md) | [Recommended recipes](../../README.md) | [Data definitions](../../docs/DATA.md) | [Attribution](../../LICENSE)
