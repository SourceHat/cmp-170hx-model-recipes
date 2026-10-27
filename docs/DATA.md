# Published Data

The current Apex Flash 1 EXL3 recipe uses a 1,374,976-token resident Q8/Q8 pool.
Its [capacity evidence](../data/apex-kv-capacity/evidence.json) is derived from
two independent loads and checked by `python3 scripts/apex_capacity.py`.
The accompanying numerical qualification/lifecycle receipts preserve the
measured values; host paths, device identities and listener metadata are
redacted. Their original source hashes and exported-file hashes are recorded
separately in [source verification](../data/apex-kv-capacity/source-verification.json).
The earlier 32k speed and prefix-reuse records keep their tested 1,083,136-token
pool. Their rates are not reassigned to the larger pool. Capacity-probe completion
rates use per-request backend timers and remain separate from shared decode.

The root [README](../README.md) covers the nine selected configurations. Each
profile's README combines its settings, memory measurements, speed table,
verification and selection rationale. The numerical files retain more
precision and detail than the rendered tables.

| File | Contents |
| --- | --- |
| `recipes/<profile>/recipe.json` | Checkpoint/runtime pins, API identity, required card count, slots, native context, shared KV and launch settings |
| `recipes/<profile>/config.yml` or `engine-config.json` | Engine-native template; listener and model paths are supplied at launch |
| `recipes/<profile>/benchmarks.json` | All retained speed waves of the winning configuration, with per-request counts, timers, cache counters and test geometry |
| `recipes/<profile>/evidence.json` | Memory observations, actual cache-precision audits, context/retrieval checks, restoration/reload evidence, task checks and quantization metadata |
| [benchmarks.csv](../benchmarks.csv) | Flattened numerical export of the 62 language-model benchmark waves |
| [Qwen historical replica results](../recipes/qwen3.8-27b-exl3/historical-replica-result.json) | Four cold/warm measurements at three replicas and 1/16 requests per replica |
| [Qwen replica archive](../archive/qwen3.8-27b-replicas/README.md) | Historical replica comparison and exact CSV, separate from the current eight-slot recipe |
| [Qwen replica request timings](../recipes/qwen3.8-27b-exl3/historical-replica-requests.json) | All 102 original requests from the same four decode waves, with backend prefill, cached tokens and client TTFT |
| [Qwen 32k retention evidence](QWEN-32K-EVIDENCE.md) | Historical MTP1 C2 check with native timers, separate from the selected C1/C8 performance pair |
| [Recovered native prefill](RECOVERED-PREFILL.md) | Four saved AWQ long-output observations with exact [JSON snapshots](../data/native-prefill-recovery.json) and [CSV](../data/native-prefill-recovery.csv) |
| [Selected-serving prefill comparison](PREFILL-COMPARISON.md) | Six complete C1/concurrent waves for Qwen, AWQ and DeepSeek V4.1 Flash; exact [CSV](../data/selected-serving-prefill.csv), [numerical traces and native counters](../data/selected-serving-prefill.json), plus the additional Qwen C8 outcome |
| [Quantization sources](../data/quantization-sources.json) | Pinned publisher declarations and Apex Flash 1's effective-bpw calculation from stored weight bytes and logical parameters |
| [Benchmark protocol](../data/benchmark-protocol.json) | Source-defined sampling, synthetic coding prompt, output budgets and decode accounting |
| [Related runtime trials](../data/runtime-trials.json) | Retained Flash/Strata and GLM-5.3-Flash/Apex Flash 1 fusion comparisons, including blocked and skipped cases |
| [Selection comparisons](../data/selection-comparisons.json) | Flash MTP/layout alternatives and reported Apex Flash 1 quantization-fidelity/memory evidence |
| [Archived profiles and experiments](../archive/README.md) | Full historical model-profile and campaign inventory, configuration versions, results and evidence gaps |
| [Historical wave CSV](../archive/history/benchmarks.csv) | Detailed and legacy measurement waves; timing methods and overlapping recipe evidence are explicit |
| [All additional historical results](../archive/history/OBSERVATIONS.md) | Quality, correctness, prefill/latency, allocation, cache and failed outcomes, with exact JSON/CSV |
| [Historical quality comparisons](../archive/history/QUALITY.md) | Bounded task scores, category denominators and original/revised grading kept separate |
| [Historical prefill](../archive/history/PREFILL.md) | Processed/cached input tokens, backend timers and per-request rates, with exact JSON/CSV |
| [Archive coverage](../archive/history/coverage.json) | Inventory of the 81 archived profiles, configuration versions and retained result records |
| [Strata CSV](../archive/benchmarks.csv) | Four Strata waves, including IQ4 C8 with no qualified shared decode rate |

The [archive catalog](../archive/catalog.json) links the complete
[historical inventory](../archive/history/catalog.json) and the detailed Strata
records. Its settings preserve historical versions; shared launch/runtime
helpers cover the recommended recipes. Missing evidence remains explicit.
The historical export can overlap the selected recipes and the Strata CSV;
combining them does not add independent repetitions. The six new selected-serving
waves are stored separately from that historical inventory. Their mirrored
entries in recipe JSON and the comparison dataset are the same observations,
not additional repetitions. See the [historical definitions](../archive/history/DATA.md).

## Performance Fields

The campaign performance collector uses temperature zero, seed `20261008`,
and equal requested minimum/maximum output budgets. Its synthetic input repeats
a small Python function and requests a scheduling-library implementation.
The prompt is adjusted through each model's tokenizer to within 64 tokens of
the target. The recorded source definition and hash are in
[benchmark-protocol.json](../data/benchmark-protocol.json); older per-run
parameters absent from their receipts remain unspecified. The separate
standard-Qwen replica collection retains its own recorded workload geometry.
The new selected-serving comparison instead uses distinct synthetic neutral
engineering text and the exact tokenizer counts in its numerical export.
Its sampling, output limits and timing definitions are documented separately;
the older campaign prompt definition is not attributed to those new inputs.

`input_target_tokens` is the intended prompt size. The actual tokenizer counts
are in `input_tokens_per_request`; output budgets and actual accepted outputs
are recorded separately from tokens counted inside the decode interval.

`decode_tok_s_aggregate` uses the common observed decode window. That window
starts after the last request begins generation and ends before the first
completion. `shared_decode_accepted_tokens / shared_decode_interval_seconds`
reconstructs the reported rate. Tokens outside that shared interval still
count toward each request's completion total and end-to-end rate.

`decode_tok_s_per_request` and `shared_decode_requests` use that same shared
window. They sum to the aggregate rate. `request_generation` retains the
individual backend timers where available; those can use different boundaries.
`end_to_end_accepted_tok_s` includes input processing, queueing and generation.
All token rates include accepted reasoning tokens.

First-token timings include queueing. The numerical export contains both the
median and slowest request, individual first-token times, backend prefill
records, draft tokens proposed/accepted and inter-token latency statistics.
Speculative token batches affect the interpretation of inter-token timing;
their recorded timing-source labels are retained.

Backend prefill rates divide the number of processed prompt tokens by the
backend prefill interval in seconds. Cached tokens are recorded separately.
These are per-request rates, including in concurrent waves; they are not
summed into an aggregate prefill throughput. TTFT includes other work and is
not substituted for a missing backend timer. The historical prefill index is
a derived view of the existing observations, not additional measurements.

`cached_prefix` means a cache hit was verified by recorded counters or the
source receipt. `repeated-input` means the prompt was repeated without that
confirmation, or the reported cached-token count was zero. A repeated prompt
can still incur full prefill. `cache_hit_verified: null` means unavailable.

Arrays keep request order. Identical values are displayed once in tables;
varying values appear on separate lines. JSON and CSV preserve the complete
arrays. CSV array/object cells are JSON-encoded.

## Test Geometry And History

Each wave has a `cohort`, `test_configuration`, `tested_kv_pool_tokens` and
source reference. The configured serving pool is separate from the measured
test pool. Earlier MiMo-V2.6-Flash/GLM-5.3-Flash/Apex Flash 1 waves used smaller pools and a 262,144-token
configured limit; these recipes now configure 524,288. Earlier driver/runtime
epochs are labeled where the receipts identify them.
The larger-context Qwen3.8-Flash-Next configuration used a 524,288-token configured limit, exceeding
the selected native 262,144-token limit. Its records are labeled as an earlier
extended-context run, with explicit test limits; they are not relabeled as
native-context qualification. Scaling parameters absent from those receipts
remain unspecified.

`headline_eligible` identifies waves eligible for a matching comparison;
`preferred_headline_cohort`, when present, selects the complete newer pair. Earlier
additional measurements appear in each profile's expandable historical table.
This preserves the recorded data without treating every run as a matched
comparison. The short 256/512-output waves and long 8,192-output AWQ waves
retain their distinct timing methods and workload sizes.

The current eight-slot standard Qwen recipe has a measured 32k C1/C8 pair in
the [selected-serving comparison](PREFILL-COMPARISON.md). Its four historical
replica results used three independent instances with one or sixteen requests
per replica: three or forty-eight requests across the rig. Their whole-rig
rates and each replica's contribution remain in the separate historical file;
they are not substituted for the selected eight-request wave.

## Memory And Context

The native context limit is per request. Tabby uses an explicitly allocated
GPU token pool shared across active requests and retained prefixes. Dividing
that pool by the context limit assumes unshared histories; it is arithmetic,
not a measured throughput limit. Shared prefixes can reduce physical page use.
Configured slots also limit the number of active requests.

For Apex Flash 1 AWQ and DeepSeek V4.1 Flash, the legacy `shared_gpu_pool_tokens` field stores
vLLM's **context-normalized block-capacity report**. `capacity_basis` identifies
this meaning, and `capacity_context_tokens` records the reporting context.
The runtime calculates full-context concurrency from the available block count
and each cache group's maximum-context block requirement, then reports
`floor(calculated_concurrency * max_model_len)` token-equivalents. These mixed
groups include full/sliding/compressed attention, recurrent state or other
architecture-specific buffers. A host-group limit applies if that feature is used.

That number is neither a literal count of resident token slots nor a free-token
budget. Its normalization can change with the configured context even at the
same byte allocation. The displayed full-context sizing count is a calculation,
not a measured maximum concurrency or a qualification of simultaneous large
histories. Recorded large-history-plus-small-request checks retain their narrower
scope. No cache-boundary maximum is inferred from successful startup or a smoke.

Each memory observation records its own context, pool and phase. Peak used
VRAM, allocator allocated/reserved memory and CUDA free memory are different
counters, sometimes sampled at different times. They are preserved with their
original units and source references. The profile page reports sampled peak
VRAM in GiB; allocator snapshots remain in `evidence.json`.

Main/draft payload bytes count the observed serving-cache tensors, including
packing/scales where recorded. They are distinct from total VRAM, model weights
and allocator workspace. Full layer audits retain device, tensor shapes,
storage dtypes and quantization bits. DeepSeek V4.1 Flash's shared-storage views are
preserved as audits; no separate main/draft payload total is invented by
adding overlapping storage views.

Host KV/recurrent cache budgets are configuration values. Observed host
allocation is a separate measurement and can be zero before eviction. Host
RAM is uncapped. Eight-bit serving KV does not imply eight-bit recurrent
state, positional keys, activations or model weights.

Qwen3.8-27B Orca's native context check used 253,996 input tokens and verified retrieval
and RAM restoration. MiMo-V2.6-Flash, GLM-5.3-Flash, Apex Flash 1 and DeepSeek V4.1 Flash have recorded near-limit
context checks, including exact long-input counts, request timings and
retrieval results. Their later checks did not repeat full retention/restoration
stress. Qwen3.8-Flash-Next's native pool was allocation-checked; a fresh native
near-limit context test was not run. The standard Qwen restoration results
belong to its historical sixteen-slot configuration; its 131k/261k native
context-stage counts and timings are preserved in `evidence.json`.

## Quantization And Task Checks

Apex Flash 1 evidence includes actual safetensors-header audits: tensor groups,
logical parameter counts, payload bits per parameter, native tensors,
calibration metadata, source provenance and MTP presence. Both targets cite
the same source revision. Their advertised four-bit routed experts do not
make the complete checkpoints exactly four bits per parameter. AWQ uses an
external BF16 DFlash2 head; EXL3 retains native MTP weights.

The eight-task campaign checks are retained with task/category, grading result,
failure reason and token/timing counts. They were small and formatting-sensitive;
they do not establish general quality or rank the quantization formats. No new
quality benchmark or quality superiority claim is added by this export.
The earlier decision evidence also preserves the EXL3 publisher's reported
92.52% next-token agreement and 0.0444 nats mean KL across eight held-out
128-token input windows. The `total_tokens: 1024` field records the product of
that input geometry, not an established number of scored prediction positions.
The exact scoring denominator and BF16 reference revision are unspecified.
This external model-card report has no equivalent AWQ reference result and
does not establish a local head-to-head quality ranking.

## Provenance And Missing Values

Each measurement identifies the original receipt by a public label, SHA256 and
object locator. Dated internal labels and absolute run timestamps are omitted.
Elapsed durations and the settings needed to interpret a result are preserved.
Each evidence file lists its source receipts. Values remain at their
recorded precision in JSON. `null` means unavailable or inapplicable; the tables
display `Not recorded`. A false verification flag remains false, rather than being changed
into an unspecified result.

Private host paths, GPU UUIDs, credentials and raw conversation content are
omitted. Reference GPU ordinals and local worker devices preserve placement
information; the topology is documented in [HARDWARE.md](HARDWARE.md). The
recorded Qwen3.8-27B Orca measurements used reference GPU0. Measurement device labels
do not assign a card to a recipe on another system. Private serving ports,
listener addresses and startup choices are omitted.

The original host was GPU-tested. The portable repository has CPU validation
and source/config checks; it has not been GPU-qualified from a fresh install.
