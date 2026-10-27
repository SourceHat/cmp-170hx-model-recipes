# Cold Prefill And Concurrent Decode

This dataset retains the completed selected-serving comparisons. Each completed recipe has **one cold C1 request and
one concurrent wave**, at approximately **32,768 input tokens (+/-64)** and
**256 accepted output tokens per request**, including reasoning.
These are individual observations, not repetition means or uncertainty intervals.

| Recipe | C1 actual input, tokens | C1 prefill, tok/s | C1 TTFT, s | C1 decode, tok/s | Wave requests | Wave decode total, tok/s | Wave end-to-end total, tok/s |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Apex Flash 1 AWQ | 32,768 | 1,875.77 | 17.53 | 36.92 | 4 | 110.14 | 9.90 |
| DeepSeek V4.1 Flash TP3 | 32,764 | 493.92 | 66.52 | 16.86 | 4 | 29.97 | 3.51 |
| Qwen3.8-27B | 32,769 | 1,752.35 | 18.88 | 35.28 | 8 | 105.36 | 11.60 |

Temperature is zero, seed is `20261008`, reasoning effort is low, and both the
minimum and maximum accepted-output budgets are 256 tokens. Distinct synthetic
histories differ near the beginning; native counters verify **zero cached
input tokens**. Requests use the direct serving API. No gateway is in the path.

## Configuration

Qwen uses EXL3 6 bpw, native MTP1, Q8 main/draft KV, a 917,504-token pool,
262,144 context, eight slots and 2,048-token prefill chunks. Apex Flash 1 AWQ uses the
17/15/13-layer pipeline, DFlash2 depth three, 524,288 context, four slots and
512-token prefill chunks. DeepSeek V4.1 Flash uses TP3, DSpark5, 524,288 context, four
slots and 1,280-token prefill chunks. Exact pins and settings are retained in
the JSON and recipe files.

All three disable bulk RAM KV spilling. Qwen's separate recurrent-checkpoint
budget remains 7,168 MiB. The vLLM recipes retain automatic GPU KV sizing;
these 32k speed requests do not requalify their maximum-context capacity reports.
The exported AWQ and DeepSeek V4.1 Flash launch templates still configure an 8 GiB native
offload budget; the timed jobs here use zero. Their host-offload setting is
therefore an explicit difference from those templates, not a measured
enabled-versus-disabled speed comparison. The six exported Tabby recipes
default bulk page spilling off and retain their separate recurrent budgets.

The cards are CMP 170HX with 64 GiB usable memory and a 200 W limit per card.
Qwen uses one Gen2 x4 card. The multi-card recipes use Gen2 x8/x4/x4 in rank
order and host-mediated transport, with a different third physical card from
the older comparisons. Driver version is `615.71.09`; the
loaded module-note SHA256 is
`58d0109f7b13c9e2618e98e0b3de9a8c377fc635ed18dff822a1beba9517fb5a`.
Kernel ABI is `7.0.14-cmpunlocker-rootmmio32-vf-auto-cpu`. Runtime versions and pinned artifacts are
listed per recipe in the dataset.

## Timing And Accounting

- **Prefill:** computed input tokens divided by the backend request-prefill timer.
  A vLLM C1 timer requires exactly one completed-request histogram delta,
  matching prompt/output counts, unchanged metric identity and independent
  computed/cached-token accounting. Qwen retains its native per-request timer.
- **TTFT:** client POST to the first nonempty content, reasoning or tool delta.
- **Decode:** accepted-token deltas inside the common server generation interval,
  from the last request's first generation to the first completion. The boundary
  policy excludes deliveries at the ending boundary. Prefill, cancellation and
  requeue contamination invalidate that interval.
- **Whole-wave throughput:** all accepted output tokens divided by client wave
  elapsed time, including prefill and queueing. It is distinct from decode.

Numerical traces use a shared relative monotonic origin within each wave.
Their accepted counts and intervals reproduce the exported decode values;
per-request native timers are never summed into a throughput claim. Concurrent
vLLM prefill histograms sum individual request timers; that sum is not a
wall-clock prefill-throughput measurement.

When a completed C1 is reused from an earlier matching instance, the dataset
labels that scope and retains its original receipt. Artifact, settings,
driver and ordered placement match. A reused C1 is counted once.

## Interpretation

These measurements replace a headline row only as a complete C1/concurrent
pair. The older 262,144-context AWQ/DeepSeek V4.1 Flash observations and Qwen's shorter-input
replica tests remain separate. Several settings, inputs and the third card
differ, so differences from older results do not isolate a cause. Lower rates
remain in the new comparison. The synthetic workload measures serving
performance; it supplies no new model-quality score or full-context qualification.

An additional Qwen C8 observation at 32,769 input tokens per request returned
all eight 256-token outputs, but one request completed before the other seven
began generation. Its full request timers and numerical traces remain in the
JSON; no all-eight shared decode rate is assigned to that wave. A completed
request wave does not by itself guarantee an interval with every request decoding.

Download the [comparison CSV](../data/selected-serving-prefill.csv),
[complete numerical evidence](../data/selected-serving-prefill.json) or
[all recipe waves](../benchmarks.csv). [Measurement definitions](DATA.md) |
[Main comparison](../README.md#measured-performance)
