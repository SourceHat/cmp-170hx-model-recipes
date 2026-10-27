# Recovered Native Prefill Measurements

Saved vLLM metric snapshots retain four Apex Flash 1 AWQ prefill observations:
one cold and one partially cached C1 request for each PP3 layout.
Each request uses **32,771 input tokens and 8,192 accepted output tokens**.
These are existing runs, not new experiments or independent repetitions of
the short-output comparison.

| PP3 layout | Source wave | Requests | Input tokens | Computed tokens | Cached tokens | Output tokens | Native prefill, s | Prefill, tok/s | Client TTFT, s |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| balanced | cold | 1 | 32,771 | 32,771 | 0 | 8,192 | 16.13779 | 2,030.70 | 16.82 |
| balanced | cached_prefix | 1 | 32,771 | 15,107 | 17,664 | 8,192 | 7.56644 | 1,996.58 | 8.15 |
| fast | cold | 1 | 32,771 | 32,771 | 0 | 8,192 | 15.82284 | 2,071.12 | 16.76 |
| fast | cached_prefix | 1 | 32,771 | 15,107 | 17,664 | 8,192 | 7.22904 | 2,089.77 | 7.89 |

The balanced layout is **17 / 15 / 13 layers**; fast is **17 / 14 / 14**.
Both use the pinned Apex Flash 1 AWQ artifact, DFlash2 with three draft tokens,
524,288 context and four configured slots. These observations used an 8 GiB
native host-offload budget. The selected-serving short-output timing jobs use
zero; the exported AWQ launch template retains 8 GiB. These are distinct settings,
not an enabled-versus-disabled speed comparison.
One request is measured in each row despite four configured slots.

## Calculation And Attribution

```text
computed tokens = after.request_prefill_kv_computed_tokens_sum - before.sum
native seconds  = after.request_prefill_time_seconds_sum - before.sum
prefill tok/s   = computed tokens / native seconds
```

The prefill-time, computed-token, prompt-token and output-token histograms each
advance by exactly **one** completed request. Their labels and creation-epoch
fingerprints remain unchanged. Prompt/output deltas match the saved response;
prefix-query/hit deltas independently verify computed/cached token accounting.
Absolute creation timestamps are omitted from the export.

For the balanced cold request, `32,771 / 16.13779351800622 = 2,030.6989281672732 tok/s`.
The cached continuation computes only **15,107** tokens and reuses **17,664**;
dividing the full input by its shorter timer would overstate prefill performance.
The native timer runs from first scheduling to first new token, excludes queue
time and includes any preemptions. It is not an exclusive kernel timer.

## Scope

The older 32k-input / 256-output Apex Flash 1 AWQ C1/C4 test used 262,144 context
and has no retained native prefill timer. These long-output results are not
combined with that test's decode measurements. Any subsequent complete
comparison remains a separate cohort with its own timers and configuration.

Exact [JSON snapshots and formulas](../data/native-prefill-recovery.json),
[CSV values](../data/native-prefill-recovery.csv) and
[CPU validation](../scripts/native_prefill.py) make the calculation reproducible.
The balanced observations also enrich their matching long-output points in
[benchmarks.json](../recipes/apex-abliterated-awq-dflash2-pp3-balanced/benchmarks.json).

[Prefill archive](../archive/history/PREFILL.md) | [Data definitions](DATA.md)
