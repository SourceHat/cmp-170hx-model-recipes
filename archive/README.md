# Archived Profiles And Experiments

**81 archived model profiles**, with saved settings,
measurements and selection evidence. Additional experiments cover quantization,
speculative decoding, layouts, cache sizing and context limits.

## Browse

| Start with | Contents |
| --- | --- |
| [Archived profiles](PROFILES.md) | All 81 profiles, grouped by model family |
| [Additional experiments](EXPERIMENTS.md) | Experimental configurations and source result records |
| [Decode and latency](history/RESULTS.md) | Every retained wave, with request counts and timing scope |
| [Prefill](history/PREFILL.md) | Backend input-processing rates, processed/cached tokens and exact timers |
| [Quality and correctness](history/QUALITY.md) | Bounded scores, category denominators and original/revised grades |
| [Other test results](history/OBSERVATIONS.md) | Context, allocation, cache, correctness and failed outcomes |
| [Qwen 3.8 27B replicas](qwen3.8-27b-replicas/README.md) | Three one-card instances at one or sixteen requests each |
| [Strata comparisons](STRATA.md) | One-card IQ4 and two-card Q6, with native server templates |
| [Historical RAM page tier](ram-prefix-tier/README.md) | Earlier capacity arithmetic and reuse counters; disabled in selected recipes |

## By Model Family

| Family | Archived profiles | Other records | Linked waves |
| --- | --- | --- | --- |
| [Apex Flash 1 (GLM 5.3 Flash post-train)](models/apex-flash-1.md) | 7 | 108 | 41 |
| [DeepSeek](models/deepseek.md) | 8 | 17 | 5 |
| [GLM 4.5 Air](models/glm-4.5-air.md) | 2 | 0 | 0 |
| [GLM 4.7 Flash](models/glm-4.7-flash.md) | 1 | 0 | 0 |
| [GLM 5.3 Flash](models/glm-5.3-flash.md) | 22 | 49 | 143 |
| [Huihui Qwen 3.8 27B abliterated](models/huihui-qwen-3.8-27b-abliterated.md) | 8 | 0 | 0 |
| [MiMo V2.6 Flash](models/mimo-v2.6-flash.md) | 3 | 34 | 43 |
| [Orca (Qwen 3.8 27B abliterated)](models/orca.md) | 4 | 57 | 43 |
| [Other model workflows](models/other-model-workflows.md) | 0 | 46 | 10 |
| [Qwen](models/qwen.md) | 3 | 3 | 0 |
| [Qwen 3.8 27B](models/qwen-3.8-27b.md) | 14 | 11 | 68 |
| [Qwen 3.8 Flash Next](models/qwen-3.8-flash-next.md) | 9 | 40 | 41 |
| [Unresolved model identity](models/unresolved-model-identity.md) | 0 | 15 | 0 |

## Evidence And Downloads

The inventory retains **461 historical records**,
**426 configuration snapshots** and
**394 measurement waves**. Of those waves,
**243 have a valid synchronized decode interval**.
There are also 772 bounded checks,
58 quoted rate summaries and
2,157 additional numeric/functional observations.
These counts describe saved records; copies, summaries, checks and regrading
can overlap. Family links can reference the same wave.

| Data | JSON | CSV |
| --- | --- | --- |
| Full inventory | [Catalog](history/catalog.json) | [Profiles / experiments](history/profiles.csv) |
| Exact settings | [Configuration snapshots](history/configurations.json) | JSON only |
| Measurement waves | [Measurements](history/measurements.json) | [Benchmarks](history/benchmarks.csv) |
| Prefill timers | [Per-request entries](history/prefill.json) | [Prefill](history/prefill.csv) |
| Additional results | [Observations](history/observations.json) | [Observations](history/observations.csv) |
| Bounded checks | [Checks](history/checks.json) | JSON only |
| Quoted rates | [Rate summaries](history/rate-summaries.json) | [Rate summaries](history/rate-summaries.csv) |

Read the [data definitions](history/DATA.md), [source receipts](history/sources.json),
[coverage](history/coverage.json) and [export verification](history/verification.json)
before combining results. The historical data can overlap the recommended
recipe data; combining files does not create independent repetitions.

<details>
<summary>Evidence status and interpretation</summary>

| Status | Historical records |
| --- | --- |
| Decode interval measured | 61 |
| Additional test results; no matched decode wave | 203 |
| Job history; no matched benchmark | 46 |
| Bounded checks only | 57 |
| Legacy / incomplete measurements | 20 |
| Definition; no matched test receipt | 59 |
| Rate summary only | 15 |

`Definition` and `job history` entries preserve an evidence gap; they do not
claim that a model was never tested. Configured context and allocated cache
do not establish speed or concurrency at those limits. Different artifacts,
settings and timing methods remain separate, including failed and partial runs.

</details>

Historical records are comparison evidence. The [eight recommended recipes](../README.md)
provide the supported launch scripts; archival templates require their stated
runtime integration and have not been newly GPU-qualified from this export.

[Recommended recipes](../README.md) | [Attribution and licenses](../LICENSE)
