# Long-History Prefix Reuse

Long prompts can make an endpoint feel slow even when it decodes at tens of
tokens per second. Backend generation rate excludes the initial queue and
prefill. A request that generates 128 tokens after rebuilding tens of thousands
of input tokens can therefore have a much lower output/request-wall-time rate.

For these hybrid models, reusable history needs both complete attention-KV pages
and the matching recurrent/sliding-window state. Native MTP also needs its carry
hidden state at that exact position. Keeping the KV pages alone is insufficient.

## Checkpoint Retention

The runtime preserves complete, untouched lookahead pages during recurrent
replay, including pages shared with another history. It also keeps
checkpoint ancestry through unwritten, revertible output pages for retention;
those backup pages are **not** treated as currently allocatable cache hits.
Writing a borrowed page removes that protection. Genuinely destroyed ancestry
is still pruned, and the existing global checkpoint-memory budget still applies.

When a request demonstrates a substantial shared-prefix gap without a matching
checkpoint, prefill additionally stops at that exact page boundary and saves the
state there. The minimum gap is 2,048 tokens. This learns useful fork boundaries
without checkpointing every page or globally shortening the 32k prefill interval.
It does not relabel a later state as an earlier checkpoint.

Weights, precision, context limits, GPU KV pools, request slots, device selection,
speculative verification, and the mixed-prefill scheduling policy are unchanged.
Bulk RAM KV spilling remains off by default. Recurrent checkpoints remain enabled
under the budgets in each recipe. No per-thread memory reservation is added.

## Numerical Diagnostics

For anonymous numerical logging, set:

```bash
export MESHIFY_PREFIX_METRICS_PATH=/tmp/tabby-prefix-metrics.jsonl
```

This records input/output counts, timing and the initial prefix-allocation
positions. It contains no prompts, generated text, fingerprints, request IDs or
session labels. It also works when `MESHIFY_MODEL_IO_LOGGING=0` disables the
separate fingerprint diagnostics. The parent directory must exist. Logging is
optional and does not change cache eligibility, slots or memory budgets.

The `prefix_previous_completed_tokens`, `prefix_resident_tokens` and
`prefix_resume_tokens` fields distinguish a previously processed matching
prefix, currently resident KV pages and actual reuse. A positive
`prefix_missing_kv_tokens` identifies missing previously completed matching
pages; a positive `prefix_state_gap_tokens` identifies resident KV without a
matching state checkpoint. All lengths are tokens, times are seconds and
`gen_tokens_per_sec` is accepted output tokens per backend generation second.
`prefix_attribution_available=0` means attribution is unavailable. Without a
known session, an unrecognized branch is not classified as an input edit.

The portable launcher supports an optional log destination:

```bash
export MESHIFY_PREFIX_DIAGNOSTICS_PATH=/tmp/tabby-prefix-requests.jsonl
```

Then launch a Tabby recipe normally. The parent directory must exist. Logs contain
counts, timing, reason labels and process-keyed fingerprints, without prompt text,
token arrays, tool arguments or generated responses. Fingerprints are comparable
within a server process, not across restarts.

| Field | Unit / interpretation |
| --- | --- |
| `previous_observed_prefix_tokens` | Matching complete-page prefix seen in the bounded recent-history index; observation alone does not prove it completed |
| `previous_completed_prefix_tokens` | Matching complete-page prefix previously processed and released |
| `resident_prefix_tokens` | Contiguous matching complete KV pages before allocation, in tokens |
| `valid_checkpoint_tokens` | Latest matching checkpoint position within that resident prefix, in tokens |
| `restored_position_tokens` | Actual allocation resume position, in tokens |
| `resident_kv_without_state_tokens` | Resident prefix beyond the matching state checkpoint, in tokens |
| `previous_completed_kv_missing_tokens` | Previously completed matching prefix beyond the current resident prefix, in tokens |
| `checkpoint_loss_tokens` | Latest matching position recorded lost to budget or stranded ancestry; not a count of deleted tokens |
| `first_progress_s` | Server request entry to first nonempty content, reasoning or tool-call stream progress, in seconds; null for unobserved/nonstreaming progress |
| `max_progress_gap_s` | Largest observed gap between meaningful streamed events, in seconds |

An optional `X-Meshify-Prefix-Session` header correlates a thread's histories for
diagnostics; the server hashes it. `X-Meshify-Session` is also recognized. Neither
header is required for admission or cache reuse. Cache identity continues to use
the actual token prefix. Without a known prior session, a missing observation is
not classified as an incoming edit.

## What A Cache Cannot Reuse

A meaningful edit to earlier instructions, tool schemas, environment notes,
reasoning or message content changes the token prefix. State after that edit
must be rebuilt. Sticky routing cannot repair changed tokens, and a full retained
cache is not itself proof that active requests are being evicted.

Inspect the first changed normalized message, resident prefix and state position
before changing memory budgets or draft depth. Keep legitimate compaction and
instruction changes; do not remove meaningful input solely to increase a hit rate.

The existing [mixed-serving policy](MIXED-SERVING.md) allows ready decoders to
progress while new prompts are ingested. Its bounded chunks trade new-prompt
latency against interruptions to existing streams. They do not eliminate the
computation required by a genuinely new long suffix.

Recurrent checkpoints preserve hybrid state; the selected configurations keep
bulk KV page spilling disabled.

[The separate two-history check](TWO-HISTORY-PREFIX-REUSE.md) reports concurrent
and alternating 131k/176k histories, with exact per-request cache reuse and timing.

<!-- BEGIN GENERATED VERIFICATION -->

## Retained Long-History Checks

These are separate bounded serving checks, with one observation per selected service and ordinary traffic uncontrolled. They are not averages or an isolated speedup estimate. Native requests use temperature zero and 128/256 output budgets, with a 128-token minimum. Qwen3.8-27B Orca follows an appended history without a middle edit; Apex Flash 1 returns to the original branch after an intentional middle edit. The histories differ, so this is not a matched model comparison.

| Tool-result follow-up | Input tokens | Cached tokens | Output tokens | Backend prefill s | Client first progress s | Client total s |
| --- | --- | --- | --- | --- | --- | --- |
| Qwen3.8-27B Orca | 80,622 | 80,384 | 128 | 0.83 | 1.38 | 5.59 |
| Apex Flash 1 EXL3 | 131,502 | 131,328 | 128 | 0.40 | 0.87 | 5.17 |

A meaningful edit still needs replay: the selected Apex Flash 1 middle-edit check rebuilt the changed suffix in 101.88 seconds. Cold Qwen3.8-27B Orca observations in distinct runtime cohorts took 237.81 and 329.42 seconds under different background traffic. Every cohort remains in the downloadable data, including slower observations. Earlier runtime variants are separate from the selected service; warm reuse does not establish faster cold prefill.

## Final Runtime Concurrent Progress

| Wave | Request | Submitted requests | Input tokens/request | Cached tokens/request | Output tokens/request | Prefill s/request | Backend decode tok/s/request | Client first progress s/request |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Apex Flash 1 EXL3 / two long histories | a | 2 | 131,482 | 131,328 | 256 | 0.35 | 27.61 | 1.10 |
| Apex Flash 1 EXL3 / two long histories | b | 2 | 131,479 | 131,072 | 256 | 2.74 | 31.52 | 3.94 |
| Qwen3.8-27B Orca / warm long + short | a | 2 | 80,296 | 80,128 | 128 | 2.80 | 22.41 | 4.53 |
| Qwen3.8-27B Orca / warm long + short | short | 2 | 316 | 256 | 128 | 2.97 | 21.82 | 4.52 |

Generator traces confirm both streams advance in the same deliveries: 103 shared delivery timestamps for Apex Flash 1 and 43 for Qwen3.8-27B Orca. Per-request backend rates are not aggregate wave throughput. Cached/fresh greedy continuations match on both final runtimes; cancellation and page-table audits pass. No general model-quality comparison or near-limit endurance test is implied.

## Profile Coverage

| Recipe | ExLlama checkpoint retention | Launch/config validation | New live history checks |
| --- | --- | --- | --- |
| apex-abliterated-awq-dflash2-pp3-balanced | not applicable | passed | not rerun |
| apex-abliterated-exl3-mtp1-tp3 | shared runtime | passed | passed |
| deepseek-v41-flash-dspark5-tp3 | not applicable | passed | not rerun |
| glm-5.3-flash-mtp1-tp3 | shared runtime | passed | not rerun |
| mimo-flash-mtp1-tp3 | shared runtime | passed | not rerun |
| qwen-flash-next-mtp2-layer-split | shared runtime | passed | not rerun |
| qwen27-orca-mtp3-native | shared runtime | passed | passed |
| qwen3.8-27b-exl3 | shared runtime | passed | not rerun |

These retained prefix checks preserve their tested settings. Apex Flash 1's 1,083,136-token test pool predates the separately qualified [1,374,976-token recipe](../recipes/apex-abliterated-exl3-mtp1-tp3/README.md#resident-kv-qualification).

All six Tabby recipes use the same engine and diagnostic launcher. Apex Flash 1 AWQ and DeepSeek V4.1 Flash use separate vLLM cache implementations. Their launch/configuration checks pass. Only Apex Flash 1 EXL3 and Qwen3.8-27B Orca received new GPU history checks.

## Gateway Input Preservation

Prefix reuse requires the gateway to preserve the rendered history, tool schemas and template options. Replica affinity selects the same cache but does not make different token prefixes equivalent. Archived gateway observations with different backend input counts are excluded from long-history performance comparisons; all observations and their qualification flags remain available.

[Aggregate evidence and scope](../data/prefix-reuse-verification.json). [All 59 request observations, JSON](../data/prefix-reuse-requests.json). [Downloadable CSV](../data/prefix-reuse-requests.csv).

## Apex Flash 1 Gateway Validation

A separate Apex-only check preserves all 131,240 input tokens through both gateway APIs. The entire rendered prompt and template options match native serving, including the qualified tool name, on an 826,701-character neutral history. The native cold request primes the cache; the gateway observations are warm and are not cold-runtime comparisons. These are single observations under uncontrolled ordinary traffic.

| Gateway check | Wave requests | Input tokens/request | Cached tokens/request | Output tokens/request | Prefill s/request | Backend decode tok/s/request | Client first progress s/request |
| --- | --- | --- | --- | --- | --- | --- | --- |
| exact-repeat | 1 | 131,240 | 131,072 | 128 | 0.38 | 40.35 | 0.67 |
| tool-result | 1 | 131,271 | 131,072 | 128 | 0.43 | 42.79 | 0.75 |
| concurrent-short | 2 | 165 | 0 | 128 | 0.51 | 30.44 | 0.57 |
| concurrent-long | 2 | 131,271 | 131,072 | 128 | 0.43 | 33.47 | 1.10 |

The concurrent streams share 68 generator-delivery timestamps. Tool-result history reuse is verified with a supplied synthetic call/result; the forced 128-token generation probe ended at its output limit without a completed call. No new general tool-generation, model-quality or near-limit qualification is implied. Qwen3.8-27B Orca was not loaded for this follow-up, so its gateway route was not retested.

Small-budget behavior differs by API: gateway Responses generates 16 tokens for a one-token output maximum, while current native Responses and gateway Chat Completions generate one. The 128-token requests obey their budgets. The source of that minimum has not been established locally. Every running model stayed up; this follow-up changed no serving configuration or local runtime code.

[Scope and numerical results](../data/prefix-gateway-verification.json). [All nine observations, CSV](../data/prefix-gateway-requests.csv).
