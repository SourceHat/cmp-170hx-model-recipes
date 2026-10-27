# Historical Data Definitions

The archive contains 81 archived model profiles, additional experimental
configurations and retained measurements. The coverage file lists every
archived profile and accounts for the configuration and result records.
An archival definition with no matched receipt remains a documented evidence
gap; it is not relabeled as a completed test or an untested model.

## Configuration Versions

`catalog.json` lists named records and their evidence links.
`configurations.json` stores distinct original configuration versions, with
sanitized settings and source receipt labels/hashes/object locators.
Calendar timestamps and dated internal identifiers are omitted; elapsed
durations, source digests and configuration distinctions are preserved.
Configuration IDs preserve differences in original records, even when removing
deployment details leaves identical public fields. `settings_sha256` hashes
the public settings using sorted keys and compact JSON separators.

`model_repository` and `model_revision` identify the artifact only when retained.
An integration runtime label is not an upstream commit. No current runtime pin
is retroactively assigned to an older run. Runtime observations without exact
artifact identity are explicitly marked. The supported launch helpers cover
the recommended recipes; historical settings require their own integration.
Local derived model views and directory overrides are marked when present;
a pinned download source does not imply those local transformations were
absent. Missing view metadata is not reconstructed. Native argument lists,
where retained, use explicit placeholders for paths, listeners and credentials.

Context is the configured per-request limit. `cache_tokens`, where present,
records the configured pool for that version; it is not a measured stable
maximum. The architecture-specific interpretation in the main
[data definitions](../../docs/DATA.md) still applies. Configured slots do not
prove simultaneous maximum-context requests. Host KV/recurrent budgets are
configuration values, not measured transfer rates or additional resident KV.

Hardware-specific UUID maps retain only unordered numeric reserve/power values.
Names containing reference GPU labels describe historical records and assign
no device. Fixed ports, listener addresses, credentials, local artifact paths,
raw prompts and generated answers are omitted.

## Measurement Waves

`measurements.json` records each retained wave with its configuration IDs,
actual request arrays and source receipts. Individual waves are not averaged.
Repeated receipts for the same synchronized monotonic timing window are
deduplicated; additional provenance stays attached to that wave. Different
contexts, artifacts, drafts, layouts and epochs remain separate observations.
The main recipe benchmark export can overlap this archive. Combining those
files does not create more repetitions or justify pooled averages.

`shared_decode_valid` requires the retained interval to be declared valid and
its accepted-token numerator to reproduce its reported aggregate rate:

```text
decode_tok_s_aggregate = shared_decode_accepted_tokens / shared_decode_interval_seconds
```

The shared interval starts after the last request starts generation and ends
before the first completion. Prefill is excluded; accepted reasoning tokens
are included where specified by the source protocol. Invalid or absent
intervals remain unavailable, with the original diagnostic retained.

`request_count` is the whole wave's request count. A wave can span independent
model instances; `per_replica_decode` retains contributions from each serving
job in the original common interval. Those are model instances, not individual
physical cards inside a tensor/pipeline-parallel instance. The instance total
must not be treated as a one-card rate.

The retained Qwen 3.8 27B C48 comparison uses three independent MTP1 instances,
with 16 requests per instance. Each cold/warm wave preserves all 48 request
records. Its client wall-time throughput and after-first-token estimate remain
separate from synchronized decode. `observed_instances` retains the reported
context/cache/slot geometry without inventing an artifact pin or runtime
commit where the source does not provide one.

Whole-wave accepted throughput includes input processing, queueing and generation:

```text
end_to_end_accepted_tok_s = accepted_output_tokens_total / elapsed_seconds
```

The accounting check is recorded separately and remains unspecified when the
source does not retain every denominator. TTFT is a client-observed first-token
time in seconds and includes queueing. Complete per-request values, median and
slowest TTFT remain separate; no confidence interval is invented.

The older `reported_after_first_token_tok_s_estimate` is a retained client
latency-based estimate. It is not a synchronized aggregate decode rate. It
never fills the shared decode field. Missing output counts, sampling settings
and input targets remain missing. The campaign's known synthetic protocol is
documented [separately](../../data/benchmark-protocol.json); it is not applied
to older runs with unspecified sampling.

The four `client_estimated_decode_wave` records retain long-output client
stream intervals with an estimated first token batch. The source calls its
interval valid, but does not provide a synchronized backend trace. Its rate
therefore stays in `reported_after_first_token_tok_s_estimate`, with shared
decode left unavailable. Repeated embedded copies of the same client record
are retained as additional provenance rather than new waves. Failed sizing
attempts with no timing interval remain distinct attempts.

The results tables identify the historical profile, layout, draft depth,
actual input and accepted output counts, and known requested output budget.
Input/output ranges summarize the per-request values within one row; they
are not averages across experiments. Exact arrays remain in JSON and CSV.

`report_passed` preserves the enclosing report's overall outcome. A valid
timing window inside a failed or partial functional/context report is still
shown with that outcome; it does not turn the full experiment into a pass.

## Summaries And Checks

`rate-summaries.json` preserves quoted rates when detailed request/window
evidence is missing or separately referenced. The original field name and
known request count are retained. These summaries can overlap detailed waves
and must not be pooled with them. A result credited from an earlier run is not
transferred to the configuration that cites it: `citing_configuration_ids`
records citation context, while measured configuration IDs remain unresolved
unless the referenced source itself provides them.

`checks.json` retains bounded context, allocation, restoration and functional
counts/flags. It excludes answer text and private workloads. A context or
retrieval pass does not establish general quality, sustained throughput at
that context or a measured cache-boundary maximum. Lifecycle records preserve
states and numeric exit codes, without treating successful process exit as
benchmark qualification.

## Additional Model-Test Results

`observations.json` and `observations.csv` retain additional numeric results
that do not fit the synchronized-wave schema: bounded quality grades,
correctness gates, prefill/inter-token timing, context/cache/allocation
observations, request batches and failed outcomes. The
[category index](OBSERVATIONS.md) links all of them; the
[quality comparison](QUALITY.md) explains the scored task sets.
`result-sources.json` maps original receipt identities to these records.

The [prefill index](PREFILL.md), [prefill.json](prefill.json) and
[prefill.csv](prefill.csv) expose all retained `cold_prefill` and `prefill`
array entries from `observations.json`. Each entry keeps its source field,
zero-based array index, processed/cached tokens, backend timer, source-reported
rate and original configuration binding. The rate is processed tokens divided
by backend seconds; it is not inferred from client TTFT. Per-request rates
are not summed into aggregate prefill throughput. This view duplicates
existing evidence for navigation and does not add independent experiments.

An observation is not an additional independent repetition. The same model
request can occur in a detailed wave, a correctness receipt, an enclosing
report and a later summary. Identical original result objects are deduplicated
within their configuration binding, with all retained source references.
Quoted scores without task records are separate from evaluated task records.
No overall average or ranking is calculated from these overlapping exports.

`configuration_ids` is populated from an explicitly recorded config/job or
the checkpoint comparison's per-arm recipe map. Otherwise it stays empty.
`associated_profile_ids` records a named source association without assigning
its result to another version of that profile. Local mathematical overlays
with incomplete artifact identity remain unresolved.

The quality schema keeps tasks passed / total tasks, category denominators,
indexed grades, truncation flags, numeric usage/timing and original grades
where the source also retains a revised grade. It excludes task text,
generated answers, code and calibration material. A category denominator is
either explicitly reported or counted from retained task-category metadata;
it is never inferred by evenly dividing the total. Per-task latency summaries
use the saved client total times, with count, minimum, median and maximum.
The eight-task summary's reported latency is the median of those same total
times, as specified by the retained report generator. Revised grading of the
same responses does not establish a new inference result.

`numeric_units` maps every field in an observation's `values` object to its
unit. Prefill objects use processed/cached prompt tokens, backend prefill
seconds and tokens per second. Inter-token latency fields `p50_ms` and
`p95_ms` are source-reported percentiles in milliseconds; the export does not
invent missing sample counts or reconstruct a latency distribution.
Draft acceptance is accepted draft tokens / proposed draft tokens; `ratio`
is a fraction. These are per-source observations, not rates averaged across
models. Main/draft KV sizes are bytes; sampled per-card peaks use MiB, with
physical identities removed and values marked unordered. Other retained
allocation arrays explicitly name GiB. A snapshot does not prove capacity
or successful serving.

`request_metrics`, `response_metrics`, `request_batches` and the measurement
requests' `recorded_backend_usage` / `recorded_backend_timings` retain backend
counters and timers without response text. Usage token fields are counts;
`prompt_time`, `completion_time` and `total_time` are backend seconds, and
`*_tokens_per_sec` are backend tokens/s. Timing `*_n` fields are token counts;
`*_ms` fields are milliseconds, `*_per_token_ms` are milliseconds/token and
`*_per_second` fields are tokens/s. Backend completion rates and client total
time remain distinct. They do not provide a synchronized aggregate interval.

Numerical-overlay summaries report RMS logit differences in logit units,
relative L2 differences as fractions and changed/identical output counts over
the stated task set. They are not quality improvements. Source errors retain
their presence and reported outcome without private exception text or an
inferred diagnosis. False qualification flags remain false.
Standalone incomplete runs can retain a reported exception class without its
exception text; that class does not establish a model-quality failure.

`sources.json` lists receipt labels and the SHA256 hashes of their original
bytes. Source receipts identify individual objects with JSON pointers or
opaque `source_location_id` values. Neutral labels and opaque locations retain
source identity without publishing deployment details. Original files are not
redistributed. The numerical export uses retained measurements.

[Archive](../README.md) | [All wave results](RESULTS.md) | [Coverage](coverage.json)
