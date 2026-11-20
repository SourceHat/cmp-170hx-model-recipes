# Live Serving Verification

These are bounded serving checks on the reference configuration, separate
from the historical controlled recipe benchmarks. Qwen3.8-27B Orca uses adaptive native
MTP up to three; Apex Flash 1 EXL3 retains MTP1. Models, physical device selections,
context limits, slots and GPU KV pools were preserved.

The Apex Flash 1 checks on this page retain the 1,083,136-token pool they tested.
The current recipe's separately qualified 1,374,976-token pool is documented
in its [capacity qualification](../recipes/apex-abliterated-exl3-mtp1-tp3/README.md#resident-kv-qualification).

The runtime rotates occupied slots when another request is waiting,
preserves native MTP carry with recurrent checkpoints, sums accepted output
across every continuation, prunes unrestorable recurrent checkpoints during
continued work and skips unnecessary memory-map scans for ordinary backing.
Target verification and sampling remain authoritative.

## Two-Request Streams

Each row is one two-request wave with a 256-token budget per request. Native
checks use temperature zero and a matching minimum token count. Responses
checks use temperature zero and can finish incomplete at the intentional
token limit while still producing reasoning. Both requests progressed during
overlapping intervals. Native traces also confirm shared generator deliveries.

Cells with two values list the two requests in submission order.

| Model | Route | Input/request, tokens | Requests | Output/request, tokens | Backend generation/request, tok/s | Output/client total/request, tok/s | First progress/request, s |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Qwen3.8-27B Orca | Native completions | 32 | 2 | 256 | 46.37<br>46.36 | 38.48 | 1.17 |
| Qwen3.8-27B Orca | LiteLLM Responses | 84 | 2 | 256 | Not recorded | 31.47 | 1.52 |
| Apex Flash 1 EXL3 | Native completions | 33 | 2 | 256 | 34.72<br>33.34 | 33.92<br>31.83 | 0.22<br>0.43 |
| Apex Flash 1 EXL3 | LiteLLM Responses | 45 | 2 | 256 | Not recorded | 39.97<br>39.98 | 0.44 |

Backend generation divides accepted output by the backend's unrounded sum of
generation intervals; additional queue and resume-prefill intervals are
separate. The client rate divides accepted output by request-send-to-stream-close
wall time. It includes queue, prefill, network and gateway overhead. Reasoning
tokens count as accepted output; delivery events are not token counts. Native
and gateway requests have different chat wrapping, so these rows do not isolate
gateway overhead.

## Occupied-Slot Rotation

Each wave submits one more long request than the physical slot count, then
submits a short request after the slots fill. Long requests use distinct
synthetic input prefixes and a 1,536-token minimum/output budget; the short
request uses 32-33 input tokens and a 128-token budget. Ordinary production traffic
was uncontrolled, including long-context traffic during the Qwen3.8-27B Orca check.

The ranges are the minimum/maximum observations across this wave's long
requests, not repetition averages or uncertainty intervals.

| Model | Physical slots | Long / short submissions | Long input/request, tokens | Long output/request, tokens | Long backend generation/request, tok/s | Long output/client total/request, tok/s | Short first progress, s | Long requests resumed |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Qwen3.8-27B Orca | 8 | 9 / 1 | 8,461 | 1,536 | 21.87-26.05 | 6.98-8.48 | 9.93 | 9 |
| Apex Flash 1 EXL3 | 4 | 5 / 1 | 7,852 | 1,536 | 23.92-27.00 | 8.94-9.79 | 12.31 | 5 |

Every long stream completed with exactly 1,536 accepted tokens, with monotonic
cumulative token counts across resumes. Both short requests started before any
of their wave's long requests began streaming. Both page-table audits passed.
Cancellation and a forced tool-call/result round trip passed for both engines.
All 64 CPU tests passed. The complete exported patch was applied to the
pinned upstream archive and byte-compared across all 17 modified/added files.

These checks establish working batching and slot rotation, not a fixed rate at
100k+ context or sustained cache-pressure endurance. Cold input still requires
prefill, and yielding can add queue/resume time; the client-total columns retain
that cost. No model-quality assessment or isolated adaptive-versus-fixed MTP
speed comparison was performed. Preliminary checks while Apex Flash 1 was loading
measured only 12.41-12.66 backend tok/s for Qwen3.8-27B Orca; those lower observations are
retained in the aggregate data. Cache resets, traffic and policy changes are
confounded, so the later short-request rates are not a causal speedup estimate.

[Exact numerical observations, formulas and limitations](../data/serving-fairness-verification.json).
[Scheduling policy](MIXED-SERVING.md).

These Qwen3.8-27B Orca/Apex Flash 1 checks used the earlier 8 GiB RAM page tier. All six selected
Tabby/EXL3 launches now default bulk RAM KV spilling off while keeping their
existing recurrent budgets. No enabled/disabled speed comparison was run for
any model; the broader default is a policy choice. See the
[historical page-tier evidence](../archive/ram-prefix-tier/README.md).

Original documentation/data: [CC BY 4.0](../LICENSES/CC-BY-4.0.txt), with SourceHat attribution.
