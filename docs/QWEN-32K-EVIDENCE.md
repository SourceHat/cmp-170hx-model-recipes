# Qwen3.8-27B: Saved 32k Retention Check

Standard **Qwen3.8-27B, EXL3 6 bpw, MTP1** has an existing approximately
32k retention check. It sends **two requests per phase (C2)**; it is not a
matched C1/C8 performance benchmark for the current eight-slot recipe.

The pinned artifact is `turboderp/Qwen3.8-27B-exl3` at
`9e4c23cfb23697165b8e2f6da2a1df995f66353c`. The tested service uses
262,144 context, a 917,504-token Q8 main/draft KV pool, 2,048-token prefill
chunks and **sixteen** configured slots. Its historical bulk-RAM budget is
10 GiB; the current recipe disables bulk spilling and uses eight slots.

| Phase | Request | Input tokens | Computed tokens | Cached tokens | Output tokens | Backend prefill, tok/s | Backend decode/request, tok/s | Client TTFT, s |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cold | 1 | 32,824 | 32,824 | 0 | 128 | 879.06 | 31.76 | 37.81226 |
| cold | 2 | 32,824 | 32,824 | 0 | 128 | 925.14 | 33.16 | 37.81222 |
| cached continuation | 1 | 32,971 | 203 | 32,768 | 35 | 548.65 | 22.73 | 1.21950 |
| cached continuation | 2 | 32,971 | 203 | 32,768 | 35 | 548.65 | 34.65 | 1.21970 |

Each cold request emits 128 accepted tokens. Each continuation emits 35 and
reuses 32,768 input tokens. The retained report passes its bounded retention
and cache audit; this does not establish general model quality at 32k.

Cold whole-wave accepted throughput is **6.15961 tok/s**:
256 accepted output tokens divided by 41.56105 seconds,
including input processing. Backend decode values in the table use each
request's own native generation timer. A synchronized generation-only aggregate
was not retained; the per-request rates are not summed into such a claim.

A separate [matched C1/C8 comparison](PREFILL-COMPARISON.md) now measures the current
eight-slot recipe at approximately 32,768 input and 256 accepted output tokens.
Its measurements remain distinct from this historical C2 retention check.

The [measurement JSON](../archive/history/measurements.json) retains cold
`wave-cf7c3974ad0593d5aea1` and warm `wave-d703b17b6f4e68088151`, including
every native timer and client latency. Their [configuration](../archive/history/configurations.json)
is `cfg-20fa4ad1dbac96e7ddae`; the [source receipt](../archive/history/sources.json)
has SHA256 `a1994fb0d37bb1b9a8265d8bca7d98f63a920c5f55022ca827f94302dd56b614`.

[Qwen recipe](../recipes/qwen3.8-27b-exl3/README.md) |
[Other Qwen results](../archive/models/qwen-3.8-27b.md) | [Definitions](DATA.md)
