# Serving Long Prompts Alongside Streaming Responses

The shared TabbyAPI/ExLlamaV3 runtime batches requests ready for decoding and
interleaves prompt ingestion with those decode steps. A long fresh prompt consumes
GPU time even when another request has a nearly complete prefix-cache hit;
scheduling policy determines how that shared work affects streaming latency.

## Scheduling Policy

- With no response decoding, prompt ingestion retains the configured chunk size
  and advances every admitted prompt each iteration.
- When a response is decoding, GPU prefill advances one waiting prompt by at most
  256 tokens per iteration. Waiting prompts rotate in serial order.
- A mixed prefill/decode step accrues a decode-time debt. Subsequent iterations
  run batched decode while repaying that debt, then admit the next prefill chunk.
- Cache-only prefix advancement remains available during the decode-only steps.
  It stops at the usable recurrent checkpoint and never executes a model forward.
- The target/draft kernels, sampling, cache capacities, request boundaries and
  recurrent checkpoint intervals retain their existing behavior. The configured
  global chunk size is not temporarily overwritten.

When requests are queued beyond the occupied slots, a text prefill can yield
after 2,048 token positions of progress beyond its restored prefix, at a complete
page boundary. A decoder can
yield after 512 outputs at a complete page boundary. The continuation joins the
queue tail, and its matching recurrent/MTP state is saved before releasing the
slot. With no waiting request, these extra yields are disabled. Token healing
and atomic multimodal prefill, plus requests with banned-string rewind buffers,
keep their existing handling.

The slot count remains the maximum simultaneous physical batch. Rotation lets
more logical requests make progress; it does not create extra GPU KV capacity.
Long requests can still wait or require replay when their saved history is no
longer available. Cumulative output counts include every continuation segment.
Qwen3.8-27B Orca enables the engine's confidence-calibrated MTP, up to three draft tokens;
weak later proposals can be cut before another draft forward. Target sampling
and verification remain authoritative. Historical fixed-depth benchmarks are
not measurements of this later adaptive policy.

Queue rotation can add another queue or resume-prefill interval to an existing
stream. The backend adds its generation intervals across continuations; it
reports queue and prefill time separately. For user-visible responsiveness,
also measure accepted tokens over the client stream interval. A backend
generation rate alone can hide the time a yielded request spends waiting.

The engine arguments are `prefill_time_fraction=0.25` and
`mixed_prefill_chunk_size=256`. These are Generator arguments, not additional
TabbyAPI YAML settings. The mixed chunk is bounded by the configured solo chunk.
Exact or atomic multimodal spans still follow the engine's existing span rules
and can exceed a page-sized text chunk.

Inference runs on one dedicated worker thread. The HTTP event loop can accept
requests, stream output and answer health checks while a GPU step is running.
Enqueue, cancellation, forced output and cache inspection use the same worker
queue as inference. Async result queues stay on the HTTP event loop; tensor
payloads and cumulative token counts are captured before the next step can
reuse staging buffers. Unloading waits for the worker and CUDA work to finish
before releasing the model or cache. The console reads the last completed cache
snapshot rather than walking a page table while the worker changes it.

For a mixed step lasting `t` seconds and fraction `f`, the scheduler adds
`t * (1 - f) / f` seconds of decode debt. Each decode-only iteration subtracts
its measured duration. The entire mixed step is charged, including the target's
decode/readback: host-side prefill enqueue time can undercount asynchronous GPU
work. This is a conservative wall-time policy, not a measurement of per-kernel
GPU utilization or a strict latency bound.

## Practical Tradeoff

Requests progress concurrently through interleaved work. Responses ready for
generation are batched. The runtime does not run independent target-model
forward passes simultaneously on separate CUDA streams, and it does not add a
replica. Prompt ingestion receives less GPU time while existing responses are
decoding; it returns to the full solo policy when those responses finish.

The original benchmark tables measure controlled waves and their defined decode
intervals. They do not promise the same wall-clock rate for a streaming response
at a much longer context while unrelated prompts are being ingested. Full prefix
cache occupancy is also not itself evidence that running requests are being
evicted; cumulative cache-page reuse and per-request latency measure different
things.

## Verification

CPU source tests apply the exported patch to the pinned upstream methods and
exercise prefill/decode interleaving, round-robin progress, cancellation-related
selection, cache-only advancement, partial final pages and checkpoint alignment.
CI prepares the pinned upstream checkout in `.local/scheduler-base`; scheduler
policy tests run without Torch or a GPU. Source-method tests explicitly skip if
that checkout is absent.

The retained recipe measurements and live-service scheduling checks are separate
datasets with different workloads and timing definitions.

[Long-history checkpoint retention](PREFIX-REUSE.md) keeps useful state
through recurrent replay and unused output allocations. It preserves this
scheduler's chunk sizes, time fraction, slots and queue policy.

The [bounded serving verification](SERVING-VERIFICATION.md) checks occupied-slot
rotation, resumed MTP, adaptive Qwen3.8-27B Orca drafting, native and LiteLLM progress,
cancellation and tool-result continuation. Its client-total rates include
queue and resume-prefill intervals that backend generation rates omit.

Two short streaming checks completed while ordinary long prompts were being
ingested on the reference services:

| Recipe | Verification input tokens | Accepted output tokens | Backend generation wall time (s) | Backend generation rate (tok/s) | Output deliveries also reporting prefill |
| --- | ---: | ---: | ---: | ---: | ---: |
| Qwen3.8-27B Orca | 22 | 256 | 9.17 | 27.91 | 4 |
| Apex Flash 1 EXL3 | 22 | 256 | 12.05 | 21.24 | 4 |

These are single live checks with uncontrolled background traffic and freshly
restarted caches, not an isolated before/after comparison. The verification
requests themselves had short contexts. Both page-table audits passed. Exact
numeric observations and timing definitions are in
[the separate verification data](../data/serving-scheduler-verification.json).
The rates use the backend's unrounded generation interval; the displayed
durations are rounded to two decimal places by the backend. Token traces confirm
prefill progress and streaming output were delivered during the same request.
Neither model quality nor sustained behavior at a full cache is established by
these checks.

Ordinary long-context requests also completed after deployment:

| Recipe | Input tokens | Cached input tokens | Accepted output tokens | Prefill wall time (s) | Generation wall time (s) | Generation rate (tok/s) |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Apex Flash 1 EXL3 | 110,746 | 65,536 | 109 | 135.91 | 4.22 | 25.81 |
| Qwen3.8-27B Orca | 163,687 | 0 | 1,035 | 206.80 | 48.95 | 21.14 |
| Qwen3.8-27B Orca | 163,767 | 32,768 | 1,141 | 357.31 | 66.86 | 17.07 |

These are distinct production observations with uncontrolled prompts, sampling,
concurrency and cache state. They are not repeated trials or an isolated
comparison between scheduler policies. Generation rates exclude each request's
initial prefill but include interference during generation. The substantial
prefill times remain relevant: scheduling fairness improves responsiveness for
an existing decoder; it does not remove the cost of ingesting fresh long input.

The [Responses API adapter](API-COMPATIBILITY.md) also streams reasoning and
function-call progress. Receiving no answer text yet is not sufficient evidence
that a request is waiting for another request to finish.

### HTTP Worker Checks

A later live check uses the dedicated inference worker. Each row is one
two-request wave with 384 accepted output tokens per request. Both requests
progressed concurrently. Background traffic and cache state were uncontrolled,
and the native/gateway prompts differ; these values do not isolate a speedup
or the gateway's overhead.

| Recipe | Endpoint | Generation rate per request (tok/s) | Client total time per request (s) | Output / client total time (tok/s) |
| --- | --- | ---: | ---: | ---: |
| Qwen3.8-27B Orca | Native completions | 41.93 / 41.92 | 10.96 / 10.96 | 35.05 / 35.05 |
| Qwen3.8-27B Orca | LiteLLM Responses | 34.87 / 34.86 | 13.30 / 13.30 | 28.86 / 28.87 |
| Apex Flash 1 EXL3 | Native completions | 26.45 / 26.45 | 17.48 / 17.48 | 21.97 / 21.97 |
| Apex Flash 1 EXL3 | LiteLLM Responses | 29.69 / 29.68 | 16.58 / 16.58 | 23.16 / 23.16 |

The native Qwen3.8-27B Orca pair shared 99 generator deliveries; the Apex Flash 1 pair shared 195.
Health probes during those waves all returned HTTP 200, with maximum observed
latency of 99.64 ms and 110.32 ms respectively. Both page-table audits passed.
Closing either model's verification stream after its first text cancelled
generation after two tokens against a 512-token budget. All 49 CPU tests passed.

The Responses checks streamed reasoning and ended as `incomplete` at the
deliberate token limit. They establish concurrent progress and correct output
accounting, not answer quality. The previously observed Apex Flash 1 availability error
did not recur in this pair; the gateway's administrative policy was not inspected.
Fresh long prompts still require prefill. These checks do not qualify full-cache
endurance or promise a fixed generation rate at long context.

[Exact values, timing definitions and limitations](../data/serving-worker-verification.json)
are retained separately from the historical recipe benchmarks.
