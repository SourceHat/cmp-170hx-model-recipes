# Additional Retained Test Results

These records complement the [measurement waves](RESULTS.md). They preserve
quality scores, correctness gates, request/prefill timing, memory and context
observations, and failed or partial outcomes. They are not additional
independent repetitions: report copies, individual requests, quoted scores
and regrading can overlap. No scores or rates are pooled across records.

Open a profile to compare its exact configuration versions. A filename or
profile association without a recorded config/job remains explicitly unbound.
An error flag records the presence of a source error without publishing its
private text or asserting its cause. Configured limits and memory snapshots
are observations, not evidence that the associated workload passed.

| Result category | Retained records |
| --- | --- |
| [Context Allocation](observations/context_allocation.md) | 350 |
| [Correctness Check](observations/correctness_check.md) | 117 |
| [Numerical Evaluation](observations/numerical_evaluation.md) | 2 |
| [Performance Detail](observations/performance_detail.md) | 427 |
| [Quality Evaluation](observations/quality_evaluation.md) | 15 |
| [Quoted Quality Score](observations/quoted_quality_score.md) | 2 |
| [Test Outcome](observations/test_outcome.md) | 1244 |

[Exact JSON](observations.json) | [CSV](observations.csv) | [Quality comparison](QUALITY.md) | [Definitions](DATA.md) | [Archive](../README.md)
