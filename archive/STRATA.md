# Strata Runtime Comparisons

Two previously tested Strata configurations, retained as historical alternatives.
Each has a native engine configuration template, checkpoint/runtime pins, exact
measurements and selection limits. These are historical records requiring your
own Strata integration. The [recommended catalog](../catalog.json) and launch
helpers cover the portable entries in the [selected configuration inventory](../README.md).

## Saved Configurations

| Configuration | Cards | Batch slots | Context tokens/request | Resident batch GPU KV tokens | Logical host-backed batch tokens |
| --- | --- | --- | --- | --- | --- |
| [Strata IQ4 / single card](strata-q4-single/README.md) | 1 | 8 | 262,144 | 262,144 | 2,097,152 |
| [Strata Q6 / layer split](strata-q6-split/README.md) | 2 | 6 | 262,144 | 196,608 | 1,572,864 |

Context is the configured per-request limit. Each batch slot has 32,768 resident
GPU tokens. Batch capacities span the allocated slots; the separate 32,768-token solo GPU workspace is listed only on each
profile's page. Neither configuration was qualified near its full context limit.

## Retained Performance

All four waves use approximately 32k input tokens and 256 accepted output tokens
per request. Each row is one cold wave; request count is explicit.

| Configuration | Wave requests | Actual input tokens/request | Shared decode tok/s total | Whole-wave output tok/s | Median TTFT, s | Slowest TTFT, s |
| --- | --- | --- | --- | --- | --- | --- |
| Strata IQ4 / single card | 1 | 32,769 | 67.63 | 6.54 | 35.34 | 35.34 |
| Strata IQ4 / single card | 8 | 32,770 | Not recorded | 6.32 | 177.69 | 319.53 |
| Strata Q6 / layer split | 1 | 32,769 | 85.43 | 12.02 | 18.31 | 18.31 |
| Strata Q6 / layer split | 6 | 32,770 | 178.89 | 12.76 | 65.29 | 111.82 |

Shared decode excludes prefill; whole-wave throughput includes prefill, queueing
and generation. IQ4 C8 had no common eight-request decode interval: **6.32 tok/s
is its whole-wave throughput**, and shared decode is unqualified.

Q6 reached 178.89 shared decode tok/s across six requests in the retained wave.
EXL3/MTP2 remained selected after review of the overall context, resident-memory
and host-backed-operation tradeoffs. These measurements do not establish
maximum-context serving speed, maximum-context concurrency or relative model
quality. A smaller quantization label alone does not quantify quality loss.

The failed two-card IQ4 startup and the vLLM variant that never reached a GPU
run remain identified in [related runtime comparisons](../data/runtime-trials.json).
They are not completed performance tests or additional archived launch profiles.

## Files And Scope

- [Archive catalog](catalog.json): separate machine-readable list of these two profiles.
- Each profile's `profile.json`: pins, settings, historical status and recommended alternative.
- Each profile's `engine-config.json`: native server template with explicit path/device/listener placeholders.
- Each profile's `benchmarks.json` and `evidence.json`: exact numeric results, validation scope and sanitized source receipts.
- [benchmarks.csv](benchmarks.csv): four archival waves, kept separate from the recommended-recipe waves.
- [runtime.json](runtime.json): pinned runtime/dependency and the metadata-only allocation patch, with its MIT notice.

Strata's host-backed active KV is distinct from Tabby's evicted-prefix
RAM tier. The selected Tabby configuration defaults do not
retroactively change these historical results. No fresh GPU run or full portable
Strata runtime installation is claimed. Source hashes identify retained evidence;
private originals, credentials, host paths and raw prompts/responses are omitted.

[Recommended Flash Next recipe](../recipes/qwen-flash-next-mtp2-layer-split/README.md) | [Measurement definitions](../docs/DATA.md) | [Attribution and licenses](../LICENSE)
