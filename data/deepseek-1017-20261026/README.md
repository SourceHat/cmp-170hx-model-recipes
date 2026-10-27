# Data dictionary: DeepSeek V4.1 Flash 1017 TP4

## Reading the result

The serial baseline was retained. No qualifying reliable speedup was achieved.
The successful baseline contains 30 primary observations and 40 measured
requests in total. The batched candidate's diagnostic retry completed 19 primary
observations and failed on the next request. Its long-context/concurrency suite
was not reached. A fresh retained-baseline deployment check passed separately.

`results.json` is the normalized source for every chart. The CSVs contain the
same numeric facts, split into convenient tables. Numbers retain source precision;
the article rounds values for reading. JSON null and empty CSV values represent
missing/unmeasured values. A zero observation count is not a zero throughput.

The originals are identified by relative report path and SHA256 in
`source-index.json`. Full worker telemetry is not included. Prompts, generated
answers, token sequences, inference images, profiler payloads, stacks and locals
are excluded. Numeric token counts and timing records are included.

## Files

| File | Rows | Scope |
| --- | ---: | --- |
| `baseline-primary.csv` | 30 | Six cells, five successful observations each |
| `baseline-summary.csv` | 6 | Primary generation and TTFT medians, ranges and noise |
| `baseline-long-context.csv` | 2 | One individual request each at 128k and near-full input |
| `baseline-concurrency.csv` | 2 | One complete batch per scenario |
| `baseline-concurrent-requests.csv` | 8 | Four individual requests in each batch |
| `candidate-primary.csv` | 20 | Diagnostic retry: 19 completed and one failed request |
| `candidate-comparison.csv` | 6 | Three complete, one incomplete and two unreached cells |
| `candidate-attempts.csv` | 2 | First candidate attempt and diagnostic retry failure facts |
| `results.json` | n/a | Configuration, protocol, all the numeric tables and decision |
| `source-index.json` | n/a | Original report identities and SHA256 digests |

## Units and definitions

- All rates use accepted output tokens, not speculative draft proposals.
- `input_target_tokens` is the requested input size. `prompt_tokens` is the
  server's reported actual input count. For example, the 516,032-token target
  produced an actual 516,031-token near-full input. Actual counts are preserved.
- In compact labels, 2k/8k/32k/128k mean 2,048/8,192/32,768/131,072 tokens.
- `output_ceiling` is the requested output maximum. Successful measured
  requests in this dataset reached that maximum, as shown by their accepted
  counts. Failed requests retain only the partial accepted count.
- `generation_tokens_per_second` is `(accepted tokens - tokens in the first
  delivered block) / (last token-bearing block time - first token-bearing block
  time)`. It excludes prefill and the first delivered block. Speculative blocks
  can contain several tokens; the rate is not computed from individual engine
  token timestamps.
- `ttft_seconds` measures request start to the first token-bearing streamed
  block. It includes scheduling and input processing as experienced by the client.
- `total_seconds` measures request start through stream close. For batches,
  it measures batch launch through all four request completions.
- `aggregate_completion_tokens_per_second` is total accepted output tokens
  divided by whole-batch wall time, including input processing and scheduling.
  It is not the generation-only metric and is not single-user speed.
- Primary summaries use medians of five observations in the same process.
  Min/max marks show the observed sample range, not confidence intervals.
- `relative_noise_2mad_over_median` is twice the median absolute deviation
  divided by the cell's median. Only successful primary coding observations
  enter this statistic; concurrency samples are a separate workload.
- `generation_change_percent` is `100 * (candidate cell median / baseline cell
  median - 1)`. The fourth candidate cell has four successful samples and a
  subsequent failure; its percentage is explicitly incomplete. No full-suite
  generation ratio, overall gain or candidate concurrency cost was established.
- Candidate TTFT changes use the corresponding cell's median. They inherit
  the same repeat/prefix-cache limitations and do not measure cold prefill.

## Cache and repetition limits

Prefix caching was enabled in the launch arguments. Primary input construction
used the same seed between repeats, and the suite did not flush caches between
cases or output budgets. A warmup preceded the primary cases. Cache-hit counts
were not retained, so exact reused-token counts are unknown. Sub-second median
primary TTFT must not be presented as fresh-input prefill latency.

The two individual long-input requests ran after all 30 primary observations.
The two concurrency scenarios followed them. The mixed batch's near-full request
used the same construction and seed as the preceding individual near-full case;
prefix reuse was permitted. That batch verifies this workload in this process,
not four independent fresh maximum-length histories. The shorter batch's inputs
also followed earlier measurements, with reuse permitted.

Only one successful baseline process was retained, with no repeat-baseline run.
Its five observations per cell quantify within-run spread. Drift between
separate baseline process runs is unknown. Earlier baseline attempts stalled;
the successful process and later deployment check do not prove the underlying
intermittent GPU fault has been eliminated.

The candidate has two focused attempts. The first failed before any primary
request completed. The diagnostic retry is the sole source of candidate speed
medians; samples from different attempts were not pooled. Both attempts passed
warmup and four limited API/code checks. Missing long-context and concurrency
measurements stay unmeasured. The checked failure diagnostics do not establish
sampling, disk I/O or batching as the source of the stall.

## Configuration

The normalized configuration records the model and full artifact/base revisions,
EXL3 format, TP4, context 524,288, four slots, five-token DSpark, FP8 KV and
automatic maximum KV sizing. `ram_kv_mib=8192` is the total host KV allowance
across the service. `engram_row_cache_mib=64` is a per-table, per-rank budget;
it is not a whole-service 64 MiB cache. The requested 200 W per-card cap is not
a measurement of average power or performance per watt.

The comparison used the compatibility serving path (`recipe_mode` in the JSON),
with eager execution and host transport recorded in configuration. This is
separate from the article's historical TP3 checkpoint/software/workload. The
data supports no isolated claim about card scaling, model quality or energy
efficiency.

The production restart check is under `deployment_verification` in
`results.json`. Its 256-token inference and four API/code checks passed. It
added zero primary/capacity observations. Its first-token latency is startup
verification data, not an extra primary speed sample.

## Figure mapping

| Figure | Frozen numeric inputs |
| --- | --- |
| `01-baseline-generation` | `baseline.primary_observations`, `baseline.primary_summary` |
| `02-service-costs` | `baseline.long_context_observations`, `baseline.concurrent_batches` |
| `03-candidate-comparison` | `candidate.comparison`, `protocol.minimum_generation_gain_percent` |

The adjacent `figures/captions.json` supplies full captions, alt text and asset
dimensions. Every chart has SVG, PNG and PDF variants for desktop and mobile.
