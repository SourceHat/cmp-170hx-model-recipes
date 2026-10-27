# DeepSeek V4.1 Flash 1017: Four-Card Native Profile

The selected serial-Engram configuration for DeepSeek V4.1 Flash 1017 on four
CMP 170HX cards, with explicit model, Engram and
listener placeholders in [profile.json](profile.json). Runtime identities and
qualification limits are in [metadata.json](metadata.json).

| Setting | Recorded Value |
| --- | --- |
| Checkpoint | [LibertAIDAI/DeepSeek-V4.1-Flash-1017-EXL3-2.9bpw](https://huggingface.co/LibertAIDAI/DeepSeek-V4.1-Flash-1017-EXL3-2.9bpw/tree/afc7aa0aab98ee735c0f54e0a122019af1ac08f1) |
| Artifact revision | `afc7aa0aab98ee735c0f54e0a122019af1ac08f1` |
| Base revision | `1bae0e1088993b9b82de08f59de5be5a34e42170` |
| Cards | Four CMP 170HX cards, 64 GiB usable memory each |
| Layout | Tensor parallel across four cards, host-mediated transport |
| Request context | 524,288 tokens |
| Active slots | 4 |
| KV | FP8, maximum automatic sizing; no literal resident token count retained |
| GPU memory utilization | 0.98391 |
| Host KV budget | 8,192 MiB total across the service |
| Prefill chunk | 1,280 tokens |
| Speculation | DSpark, five draft tokens |
| Engram access | Serial; 64 MiB row-cache budget per table and TP rank |
| Engram backing | Immutable NVMe tables |
| Execution | Eager, prefix caching enabled, batch invariance disabled |
| Requested power cap | 200 W per card; not an average-power measurement |
| Compatibility selection | Baseline engine, profiling disabled |

## Runtime Scope

The measurements use the native compatibility entry point
`meshify_deepseek_perf/server.py`, the original baseline interpreter and native
plugin, and the sealed runtime identified in metadata. The startup repair fixes
the observer logging import in cold model-inspection subprocesses. This profile
records those dependencies; it does not bundle that separate native runtime or
claim that the older TP3 Docker launcher reproduces these checks.

Replace the three `@...@` placeholders for a deployment with that qualified
runtime. This configuration record is not accepted by `scripts/launch.py`;
that helper covers entries marked portable in the shared configuration catalog. No new
clean-container GPU qualification was performed for this export.

## Measured Result

Thirty primary observations completed across six input/output combinations,
with five observations per combination in one process. Median accepted
generation rates span **18.94-25.47 tokens/s**, excluding prefill. Two individual
long-input requests and eight requests in two concurrent batches bring the
baseline to **40 measured requests**; warmup and four API/code checks are additional.

The two four-request batches completed at **51.84** and **49.91 aggregate
tokens/s**, including prefill and scheduling over the whole batch. Prefix reuse
was permitted. The mixed batch followed an individual near-full request; four
simultaneous fresh maximum-length histories were not tested.

The batched candidate stalled twice. Three complete comparisons changed median
generation by -0.89%, +1.47% and -0.88%; a fourth cell has only four successful
observations. No qualifying speedup or candidate concurrency result was
established. Earlier baseline attempts also stalled, and the GPU fault remains
unexplained. The separate fresh startup check passed a 256-token request and
four API/code checks without adding primary or capacity observations.

See the [experiments and charts](../../docs/DEEPSEEK-1017.md),
[numeric data and definitions](../../data/deepseek-1017-20261026/README.md), and
[source-verification receipt](../../data/deepseek-1017-20261026/source-verification.json).
The [three-card configuration](../../recipes/deepseek-v41-flash-dspark5-tp3/README.md)
keeps its original artifact, software and short-output measurements. These
cohorts do not isolate the benefit of adding a GPU.

Original profile documentation and data are CC BY 4.0, attributed to
SourceHat/MCP Capital LLC. Model weights retain their publisher's license;
this configuration does not redistribute them.
