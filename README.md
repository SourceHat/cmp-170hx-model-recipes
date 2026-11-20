# CMP 170HX Model Recipes

7 current serving configurations for NVIDIA CMP 170HX GPUs,
with pinned checkpoints, engine-native settings and measured results.

Each configuration links its settings, setup requirements and numerical
evidence. TabbyAPI recipes include portable launchers. The four-card DeepSeek V4.1 Flash
configuration records its qualified native-runtime dependencies.

## Companion Article

Serving long-context models on CMP 170HX explains the configuration choices,
speculative-decoding comparisons, cache-capacity tradeoffs and runtime trials
behind these recipes. The measurements and supporting files are available here.

## Standard EXL3 Runtimes

[HY4 Flash, Sage S2.1 Flash and SenseNova Loop 9B](runtimes/standard-exl3/README.md)
have six pinned EXL3 reference profiles and five matching source trees.
Their serving guides describe measurements separate from the current
recipes' benchmark tables.

## Serving Configurations

Reference hardware: NVIDIA CMP 170HX with **64 GiB usable VRAM per card**,
SM80, 200 W per card, with cmpunlocker exposing the cards' full memory.

**PCIe limitation:** GPU1, GPU2 and GPU3 use **x4 links**; GPU0 uses x8.
The original multi-card comparisons use Gen2 links and host-mediated copies.
This restricted bandwidth likely limits multi-card performance; a wider-link
comparison was not measured. See the [test topology](docs/HARDWARE.md).

**Model identities:** standard Qwen is **Qwen3.8-27B**. **Qwen3.8-27B Orca is Qwen3.8-27B abliterated**, using the separately pinned uncensored EXL3 checkpoint.
**Apex Flash 1 is Cantina Security and Yeta's reinforcement-learning post-train
of GLM-5.3-Flash** for security investigations. The Apex Flash 1 EXL3 recipe uses a
quantized version of its abliterated derivative.

| Configuration | Weight quantization | Cards | Context, tokens | GPU KV, tokens / equiv. | Slots |
| --- | --- | --- | --- | --- | --- |
| [Qwen3.8-27B Orca](recipes/qwen27-orca-mtp3-native/README.md) | EXL3 8 bpw | 1 | 262,144 | 866,560 | 8 |
| [Qwen3.8-Flash-Next](recipes/qwen-flash-next-mtp2-layer-split/README.md) | EXL3 6.05 bpw | 2 | 262,144 | 1,356,032 | 6 |
| [MiMo-V2.6-Flash](recipes/mimo-flash-mtp1-tp3/README.md) | EXL3 4.03 bpw | 3 | 524,288 | 1,070,848 | 4 |
| [GLM-5.3-Flash](recipes/glm-5.3-flash-mtp1-tp3/README.md) | EXL3 4.05 bpw | 3 | 524,288 | 1,829,376 | 4 |
| [Apex Flash 1 EXL3](recipes/apex-abliterated-exl3-mtp1-tp3/README.md) | EXL3 4.37 bpw | 3 | 524,288 | 1,374,976 | 4 |
| [DeepSeek V4.1 Flash 1017 TP4](profiles/deepseek-v41-flash-1017-dspark5-tp4/README.md) | EXL3 2.9 bpw artifact | 4 | 524,288 | Automatic; count not recorded | 4 |
| [Qwen3.8-27B](recipes/qwen3.8-27b-exl3/README.md) | EXL3 6 bpw | 1 | 262,144 | 917,504 | 8 |

Quantization describes the main weights. Apex Flash 1 EXL3's **4.37 effective bpw** is
calculated from its complete checkpoint, including MTP:
`175,642,473,288 bytes * 8 / 321,323,031,390 parameters = 4.37298 bpw`.
This includes quantization overhead, native tensors and file headers.
The main tensor payload excluding MTP also rounds to 4.37 bpw.
See the [quantization source](data/quantization-sources.json) and each recipe's
tensor-format details. KV precision is configured separately.

## Measured Performance

### Short-Output Comparisons

Cold-input measurements for 6 portable configurations. C1 means one request per
model instance; a multi-card model is one instance. Prefill uses the backend's input-processing timer;
TTFT is client time to first token and includes queueing and other overhead.
Decode counts accepted output tokens inside the common generation interval,
excluding prefill. Each row uses matched C1/concurrent runs, not repetition means.
Wave request counts and rates are per model instance.

| Recipe | Input target / output budget, tokens/request | C1 prefill, tok/s | C1 TTFT, s | C1 decode, tok/s | Wave requests | Wave decode, tok/s total |
| --- | --- | --- | --- | --- | --- | --- |
| [Qwen3.8-27B Orca](recipes/qwen27-orca-mtp3-native/README.md) | 32,768 / 256 | 1,339.70 | 24.57 | 47.49 | 8 | 112.38 |
| [Qwen3.8-Flash-Next](recipes/qwen-flash-next-mtp2-layer-split/README.md) | 32,768 / 256 | 1,336.96 | 24.60 | 74.79 | 6 | 136.71 |
| [MiMo-V2.6-Flash](recipes/mimo-flash-mtp1-tp3/README.md) | 32,768 / 512 | 621.61 | 52.83 | 48.17 | 4 | 86.52 |
| [GLM-5.3-Flash](recipes/glm-5.3-flash-mtp1-tp3/README.md) | 32,768 / 256 | 648.96 | 50.58 | 48.36 | 4 | 100.65 |
| [Apex Flash 1 EXL3](recipes/apex-abliterated-exl3-mtp1-tp3/README.md) | 32,768 / 256 | 648.57 | 50.61 | 40.09 | 4 | 98.49 |
| [Qwen3.8-27B](recipes/qwen3.8-27b-exl3/README.md) | 32,768 / 256 | 1,752.35 | 18.88 | 35.28 | 8 | 105.36 |

The [prefill comparison](docs/PREFILL-COMPARISON.md) retains matched C1 and concurrent waves for standard Qwen and the two archived recipes, with their actual settings. Download its [comparison CSV](data/selected-serving-prefill.csv).

Standard Qwen's row measures C1/C8 at 32k input. Its [historical replica results](archive/qwen3.8-27b-replicas/README.md) and [32k C2 retention check](docs/QWEN-32K-EVIDENCE.md) remain separate.

**Apex Flash 1 EXL3 capacity:** the current recipe has a separately qualified **1,374,976-token** resident pool with rebalanced rank reserves. Its retained 32k speed pair used **1,083,136 tokens** and the earlier placement. See the [two-load capacity qualification](recipes/apex-abliterated-exl3-mtp1-tp3/README.md#resident-kv-qualification); the larger capacity is not a new throughput measurement.


### DeepSeek V4.1 Flash 1017 TP4: Long Outputs

[DeepSeek V4.1 Flash 1017 TP4](profiles/deepseek-v41-flash-1017-dspark5-tp4/README.md) uses five observations per input/output combination in one process,
with prefix reuse permitted. Generation excludes prefill and the first delivered
token block. These longer-output observations use different weights and a
different native runtime from the [archived TP3 recipe](archive/recipes/deepseek-v41-flash-dspark5-tp3/README.md).
The output budgets and timing methods also differ from the cold, short-output
measurements.

| Input target, tokens | Output tokens | Median generation, tok/s | Observations |
| --- | --- | --- | --- |
| 2,048 | 2,048 | 19.23 | 5 |
| 2,048 | 8,192 | 25.47 | 5 |
| 8,192 | 2,048 | 20.09 | 5 |
| 8,192 | 8,192 | 24.09 | 5 |
| 32,768 | 2,048 | 18.94 | 5 |
| 32,768 | 8,192 | 24.29 | 5 |

Both four-request batches completed, at **51.84** and **49.91 aggregate output
tokens/s including prefill and scheduling**. Prefix reuse was permitted; the
mixed batch followed an individual near-full-context request. Thirty primary
observations, two individual long-input requests and eight concurrent requests
give 40 measured requests. The batched Engram candidate stalled twice and was
rejected; no qualifying speedup or candidate concurrency result was established.
The startup compatibility repair passed a fresh launch and four API/code checks;
the intermittent GPU fault remains unresolved. See the
[experiments and charts](docs/DEEPSEEK-1017.md) and
[data definitions](data/deepseek-1017-20261026/README.md).


<details>
<summary>Measurement geometry and serving limits</summary>

Context, KV and configured slots describe the selected recipe. Qwen3.8-27B Orca's listed
speed waves used fixed MTP3; current serving uses adaptive MTP up to three.
MiMo-V2.6-Flash's listed speed waves used a 262,144-token pool/context.
Each recipe labels its test geometry.

The context limit is per request. Tabby capacity is an explicitly allocated
shared token pool. The slot count does not guarantee simultaneous maximum
histories. See the [data definitions](docs/DATA.md#memory-and-context).
The selected text recipes use the checkpoints' native context limits; YaRN and
custom positional scaling are not configured.

</details>

## Start Here

1. Read [Hardware Requirements And Test Setup](docs/HARDWARE.md).
2. Prepare the matching [runtime and model assets](docs/REPRODUCING.md).
3. Open the configuration's README for its setup. Portable entries support `launch.sh --dry-run`; the native DeepSeek V4.1 Flash entry lists its runtime dependencies and configuration placeholders.
4. Select devices and listener settings, then follow that configuration's launch instructions. Portable [launch options](docs/REPRODUCING.md#launch-options) apply to the bundled launchers.

## Archived Alternatives

[Apex Flash 1 AWQ and DeepSeek V4.1 Flash TP3](archive/recipes/README.md) are
retired from the serving catalog. Their pinned launch settings and measurements
are in the archive.

The [archive](archive/README.md) contains 81 archived model profiles,
additional experimental configurations and retained results. It includes
quantization, speculative-decoding, layout, cache-sizing and context alternatives,
with exact measurements, partial/failed outcomes and explicit evidence gaps.
Its catalog and CSVs document the broader search behind the selected configurations.
Browse the [timing waves](archive/history/RESULTS.md),
[bounded quality comparisons](archive/history/QUALITY.md), and
[all additional test results](archive/history/OBSERVATIONS.md) for the retained
measurements, original/revised grades, allocation checks and negative outcomes.

## Reproducibility

- [Benchmark methodology and limits](docs/BENCHMARKS.md)
- [Completion, chat and Responses interfaces](docs/API-COMPATIBILITY.md)
- [Current recipe benchmark points](benchmarks.csv)
- [Detailed evidence and data definitions](docs/DATA.md)
- [Machine-readable catalog](catalog.json)
- [Model/runtime attribution and licenses](THIRD_PARTY.md)
- [Reuse and required attribution](LICENSE)
- [Contributing a recipe](CONTRIBUTING.md)

The original configurations were GPU-tested on the reference host. This
portable export is validated on CPU; it has not been GPU-qualified from a
fresh installation. Model weights, compiled binaries, credentials and raw
conversation logs are referenced or omitted rather than committed.

## License And Attribution

Original recipe documentation, metadata and benchmark data are **CC BY 4.0**.
When sharing or adapting them, credit **SourceHat**, link to this repository or
the relevant recipe, link to the license and identify your changes. For example:

> Based on SourceHat's [CMP 170HX Model Recipes](https://github.com/SourceHat/cmp-170hx-model-recipes), [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Modified by YOUR NAME.

Original standalone code is **Apache-2.0**; retain applicable notices, including
[NOTICE](NOTICE), when redistributing it. Upstream runtime code, patches and
model weights keep their own licenses. See [LICENSE](LICENSE) for the scope and
[THIRD_PARTY.md](THIRD_PARTY.md) for upstream attribution.

---

This work was performed and is released by **MCP Capital LLC**, owner of the **SourceHat** brand.
