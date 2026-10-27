#!/usr/bin/env python3
"""Build the public recipe cards and numerical CSV from the checked-in records."""
import csv
import json
from pathlib import Path
from native_prefill import recover_prefill
from model_names import display_names, MODEL_NAMES

REPO = Path(__file__).resolve().parents[1]


def number(value, decimals=2):
    if value is None:
        return "-"
    if isinstance(value, list):
        rendered = [number(item, decimals) for item in value]
        return rendered[0] if rendered and len(set(rendered)) == 1 else "<br>".join(rendered) or "-"
    if isinstance(value, int):
        return f"{value:,}"
    return f"{value:,.{decimals}f}"


def table(headers, rows):
    def cell(value):
        rendered = str(value).replace("|", "\\|").replace("\n", "<br>")
        return "<br>".join("Not recorded" if part in {"", "-", "None"} else part
                           for part in rendered.split("<br>"))
    return "| " + " | ".join(headers) + " |\n| " + " | ".join(["---"] * len(headers)) + " |\n" + "".join(
        "| " + " | ".join(map(cell, row)) + " |\n" for row in rows)


def recovered_prefill_document():
    data = json.loads((REPO / "data/native-prefill-recovery.json").read_text())
    rows = []
    for record in data["records"]:
        m = recover_prefill(record)
        rows.append([record["profile"].rsplit("-", 1)[-1], record["wave"], 1,
                     number(m["input_tokens"]), number(m["processed_prompt_tokens"]),
                     number(m["cached_prompt_tokens"]), number(m["accepted_output_tokens"]),
                     number(m["backend_prefill_seconds"], 5), number(m["prefill_tok_s"]),
                     number(record["request"]["client_ttft_seconds"])])
    raw = """# Recovered Native Prefill Measurements

Saved vLLM metric snapshots retain four Apex AWQ prefill observations:
one cold and one partially cached C1 request for each PP3 layout.
Each request uses **32,771 input tokens and 8,192 accepted output tokens**.
These are existing runs, not new experiments or independent repetitions of
the short-output comparison.

"""
    raw += table(["PP3 layout", "Source wave", "Requests", "Input tokens", "Computed tokens",
                  "Cached tokens", "Output tokens", "Native prefill, s", "Prefill, tok/s",
                  "Client TTFT, s"], rows)
    raw += """
The balanced layout is **17 / 15 / 13 layers**; fast is **17 / 14 / 14**.
Both use the pinned Apex AWQ artifact, DFlash2 with three draft tokens,
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

The older 32k-input / 256-output Apex AWQ C1/C4 test used 262,144 context
and has no retained native prefill timer. These long-output results are not
combined with that test's decode measurements. Any subsequent complete
comparison remains a separate cohort with its own timers and configuration.

Exact [JSON snapshots and formulas](../data/native-prefill-recovery.json),
[CSV values](../data/native-prefill-recovery.csv) and
[CPU validation](../scripts/native_prefill.py) make the calculation reproducible.
The balanced observations also enrich their matching long-output points in
[benchmarks.json](../recipes/apex-abliterated-awq-dflash2-pp3-balanced/benchmarks.json).

[Prefill archive](../archive/history/PREFILL.md) | [Data definitions](DATA.md)
"""
    return display_names(raw)


def qwen_32k_document():
    points = json.loads((REPO / "archive/history/measurements.json").read_text())["points"]
    cold = next(row for row in points if row["measurement_id"] == "wave-cf7c3974ad0593d5aea1")
    warm = next(row for row in points if row["measurement_id"] == "wave-d703b17b6f4e68088151")
    rows = []
    for label, wave in (("cold", cold), ("cached continuation", warm)):
        for index, request in enumerate(wave["requests"]):
            timing = request["recorded_backend_timings"]
            rows.append([label, index + 1, number(request["input_tokens"]),
                         number(timing["prompt_n"]), number(timing["cache_n"]),
                         number(request["accepted_output_tokens"]), number(timing["prompt_per_second"]),
                         number(timing["predicted_per_second"]), number(request["ttft_seconds"], 5)])
    raw = """# Qwen 3.8 27B: Saved 32k Retention Check

Standard **Qwen 3.8 27B, EXL3 6 bpw, MTP1** has an existing approximately
32k retention check. It sends **two requests per phase (C2)**; it is not a
matched C1/C8 performance benchmark for the current eight-slot recipe.

The pinned artifact is `turboderp/Qwen3.8-27B-exl3` at
`9e4c23cfb23697165b8e2f6da2a1df995f66353c`. The tested service uses
262,144 context, a 917,504-token Q8 main/draft KV pool, 2,048-token prefill
chunks and **sixteen** configured slots. Its historical bulk-RAM budget is
10 GiB; the current recipe disables bulk spilling and uses eight slots.

"""
    raw += table(["Phase", "Request", "Input tokens", "Computed tokens", "Cached tokens", "Output tokens",
                  "Backend prefill, tok/s", "Backend decode/request, tok/s", "Client TTFT, s"], rows)
    raw += f"""
Each cold request emits 128 accepted tokens. Each continuation emits 35 and
reuses 32,768 input tokens. The retained report passes its bounded retention
and cache audit; this does not establish general model quality at 32k.

Cold whole-wave accepted throughput is **{number(cold['end_to_end_accepted_tok_s'], 5)} tok/s**:
256 accepted output tokens divided by {number(cold['elapsed_seconds'], 5)} seconds,
including input processing. Backend decode values in the table use each
request's own native generation timer. A synchronized generation-only aggregate
was not retained; the per-request rates are not summed into such a claim.

The missing comparison remains **C1 and C8 at approximately 32,768 input and
256 accepted output tokens per request**, using the current serving recipe.
Historical 32k evidence must not be described as an absence of all 32k testing.

The [measurement JSON](../archive/history/measurements.json) retains cold
`wave-cf7c3974ad0593d5aea1` and warm `wave-d703b17b6f4e68088151`, including
every native timer and client latency. Their [configuration](../archive/history/configurations.json)
is `cfg-20fa4ad1dbac96e7ddae`; the [source receipt](../archive/history/sources.json)
has SHA256 `a1994fb0d37bb1b9a8265d8bca7d98f63a920c5f55022ca827f94302dd56b614`.

[Qwen recipe](../recipes/qwen3.8-27b-exl3/README.md) |
[Other Qwen results](../archive/models/qwen-3.8-27b.md) | [Definitions](DATA.md)
"""
    if any(p.get("cohort") == "selected-serving-native-prefill"
           for p in json.loads((REPO / "recipes/qwen3.8-27b-exl3/benchmarks.json").read_text())["points"]):
        raw = raw.replace("The missing comparison remains **C1 and C8 at approximately 32,768 input and\n"
            "256 accepted output tokens per request**, using the current serving recipe.\n"
            "Historical 32k evidence must not be described as an absence of all 32k testing.",
            "A separate [matched C1/C8 comparison](PREFILL-COMPARISON.md) now measures the current\n"
            "eight-slot recipe at approximately 32,768 input and 256 accepted output tokens.\n"
            "Its measurements remain distinct from this historical C2 retention check.")
    return display_names(raw)


def selected_prefill_document():
    data = json.loads((REPO / "data/selected-serving-prefill.json").read_text())
    rows = []
    for cohort in data["cohorts"]:
        recipe = json.loads((REPO / "recipes" / cohort["recipe"] / "recipe.json").read_text())
        single = next(p for p in cohort["points"] if p["concurrency"] == 1)
        wave = next(p for p in cohort["points"] if p["concurrency"] > 1)
        rows.append([recipe["short_name"], number(single["input_tokens_per_request"]),
                     number(single["backend_prefill_tok_s_per_request_median"]),
                     number(single["ttft_median_seconds"]), number(single["decode_tok_s_aggregate"]),
                     wave["concurrency"], number(wave["decode_tok_s_aggregate"]),
                     number(wave["end_to_end_accepted_tok_s"])])
    raw = """# Cold Prefill And Concurrent Decode

This dataset retains the completed selected-serving comparisons. Each completed recipe has **one cold C1 request and
one concurrent wave**, at approximately **32,768 input tokens (+/-64)** and
**256 accepted output tokens per request**, including reasoning.
These are individual observations, not repetition means or uncertainty intervals.

"""
    raw += table(["Recipe", "C1 actual input, tokens", "C1 prefill, tok/s", "C1 TTFT, s",
                  "C1 decode, tok/s", "Wave requests", "Wave decode total, tok/s",
                  "Wave end-to-end total, tok/s"], rows)
    raw += f"""
Temperature is zero, seed is `20261008`, reasoning effort is low, and both the
minimum and maximum accepted-output budgets are 256 tokens. Distinct synthetic
histories differ near the beginning; native counters verify **zero cached
input tokens**. Requests use the direct serving API. No gateway is in the path.

## Configuration

Qwen uses EXL3 6 bpw, native MTP1, Q8 main/draft KV, a 917,504-token pool,
262,144 context, eight slots and 2,048-token prefill chunks. Apex AWQ uses the
17/15/13-layer pipeline, DFlash2 depth three, 524,288 context, four slots and
512-token prefill chunks. DeepSeek uses TP3, DSpark5, 524,288 context, four
slots and 1,280-token prefill chunks. Exact pins and settings are retained in
the JSON and recipe files.

All three disable bulk RAM KV spilling. Qwen's separate recurrent-checkpoint
budget remains 7,168 MiB. The vLLM recipes retain automatic GPU KV sizing;
these 32k speed requests do not requalify their maximum-context capacity reports.
The exported AWQ and DeepSeek launch templates still configure an 8 GiB native
offload budget; the timed jobs here use zero. Their host-offload setting is
therefore an explicit difference from those templates, not a measured
enabled-versus-disabled speed comparison. The six exported Tabby recipes
default bulk page spilling off and retain their separate recurrent budgets.

The cards are CMP 170HX with 64 GiB usable memory and a 200 W limit per card.
Qwen uses one Gen2 x4 card. The multi-card recipes use Gen2 x8/x4/x4 in rank
order and host-mediated transport, with a different third physical card from
the older comparisons. Driver version is `{data['driver_version']}`; the
loaded module-note SHA256 is
`{data['loaded_driver_note_sha256']}`.
Kernel ABI is `{data['kernel']}`. Runtime versions and pinned artifacts are
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
pair. The older 262,144-context AWQ/DeepSeek observations and Qwen's shorter-input
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
"""
    return display_names(raw)


def comparison_notes():
    path = REPO / "data/selected-serving-prefill.json"
    measured = {c["recipe"] for c in json.loads(path.read_text())["cohorts"]} if path.exists() else set()
    raw = "\n"
    if measured:
        raw += ("The completed [selected-serving comparisons](docs/PREFILL-COMPARISON.md) retain artifact-specific measurements with their actual settings. "
                "Each completed C1/concurrent pair supplies its whole headline row; older measurements remain separate. "
                "Download its [comparison CSV](data/selected-serving-prefill.csv).\n\n")
    missing = [name for ident, name in (("apex-abliterated-awq-dflash2-pp3-balanced", "Apex AWQ"),
               ("deepseek-v41-flash-dspark5-tp3", "DeepSeek")) if ident not in measured]
    if missing:
        raw += (" and ".join(missing) + "'s displayed short-output measurements have no retained native "
                "prefill timer; those cells remain `Not recorded`.\n\n")
    raw += ("The separate AWQ 32k-input / 8,192-output run records "
            "[2,030.70 prefill tok/s](docs/RECOVERED-PREFILL.md); it is not substituted into the "
            "256-output comparison. Each recipe and the [prefill index](archive/history/PREFILL.md) retain the other waves.\n\n")
    if "qwen3.8-27b-exl3" in measured:
        raw += ("Standard Qwen's row measures C1/C8 at 32k input. Its "
                "[historical replica results](archive/qwen3.8-27b-replicas/README.md) and "
                "[32k C2 retention check](docs/QWEN-32K-EVIDENCE.md) remain separate.\n\n")
    else:
        raw += ("**Standard Qwen:** the row reports median observed per-replica values from three "
                "independent one-card instances running simultaneously, at one or sixteen requests per replica. "
                "Its shorter inputs and larger output budget differ from the 32k comparison. These are neither "
                "isolated-card tests nor uncertainty intervals; no current eight-request rate is implied. "
                "The complete [historical replica benchmarks](archive/qwen3.8-27b-replicas/README.md) are archived. "
                "A separate [32k MTP1 retention check](docs/QWEN-32K-EVIDENCE.md) used C2; "
                "the current recipe still lacks the matching C1/C8 benchmark.\n\n")
    if (REPO / "data/apex-kv-capacity/evidence.json").exists():
        raw += ("**Apex EXL3 capacity:** the current recipe has a separately qualified "
                "**1,374,976-token** resident pool with rebalanced rank reserves. "
                "Its retained 32k speed pair used **1,083,136 tokens** and the earlier placement. "
                "See the [two-load capacity qualification](recipes/apex-abliterated-exl3-mtp1-tp3/README.md#resident-kv-qualification); "
                "the larger capacity is not a new throughput measurement.\n\n")
    return display_names(raw)


def serving_verification():
    path = REPO / "data/serving-fairness-verification.json"
    if not path.exists():
        return
    data = json.loads(path.read_text())
    names = {"qwen27-orca-mtp3-native": "Orca", "apex-abliterated-exl3-mtp1-tp3": "Apex EXL3"}
    pairs, pressure = [], []
    for model in data["models"]:
        for check in model["checks"]:
            rows = check["requests"]
            if check["workload"] == "oversubscribed_native_wave":
                long_rows, short = rows[:-1], rows[-1]
                def span(field):
                    values = [r[field] for r in long_rows]
                    return number(min(values)) + "-" + number(max(values))
                pressure.append([names[model["recipe"]], model["physical_request_slots"],
                                 f"{len(long_rows)} / 1", number(long_rows[0]["input_tokens"]),
                                 number(long_rows[0]["accepted_output_tokens"]),
                                 span("backend_generation_tokens_per_second"),
                                 span("client_output_tokens_per_total_second"),
                                 number(short["client_first_progress_seconds"]),
                                 check["results"]["resumed_requests"]])
            else:
                route = "Native completions" if check["workload"] == "native_completions_pair" else "LiteLLM Responses"
                pairs.append([names[model["recipe"]], route,
                              number([r["input_tokens"] for r in rows]), check["submitted_requests"],
                              number([r["accepted_output_tokens"] for r in rows]),
                              number([r.get("backend_generation_tokens_per_second") for r in rows]),
                              number([r["client_output_tokens_per_total_second"] for r in rows]),
                              number([r["client_first_progress_seconds"] for r in rows])])
    raw = """# Live Serving Verification

These are bounded serving checks on the reference configuration, separate
from the historical controlled recipe benchmarks. Orca uses adaptive native
MTP up to three; Apex EXL3 retains MTP1. Models, physical device selections,
context limits, slots and GPU KV pools were preserved.

The Apex checks on this page retain the 1,083,136-token pool they tested.
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

"""
    raw += table(["Model", "Route", "Input/request, tokens", "Requests", "Output/request, tokens",
                  "Backend generation/request, tok/s", "Output/client total/request, tok/s", "First progress/request, s"], pairs)
    raw += """
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
was uncontrolled, including long-context traffic during the Orca check.

The ranges are the minimum/maximum observations across this wave's long
requests, not repetition averages or uncertainty intervals.

"""
    raw += table(["Model", "Physical slots", "Long / short submissions", "Long input/request, tokens",
                  "Long output/request, tokens", "Long backend generation/request, tok/s",
                  "Long output/client total/request, tok/s", "Short first progress, s", "Long requests resumed"], pressure)
    raw += f"""
Every long stream completed with exactly 1,536 accepted tokens, with monotonic
cumulative token counts across resumes. Both short requests started before any
of their wave's long requests began streaming. Both page-table audits passed.
Cancellation and a forced tool-call/result round trip passed for both engines.
All {data['cpu_tests_passed']} CPU tests passed. The complete exported patch was applied to the
pinned upstream archive and byte-compared across all 17 modified/added files.

These checks establish working batching and slot rotation, not a fixed rate at
100k+ context or sustained cache-pressure endurance. Cold input still requires
prefill, and yielding can add queue/resume time; the client-total columns retain
that cost. No model-quality assessment or isolated adaptive-versus-fixed MTP
speed comparison was performed. Preliminary checks while Apex was loading
measured only 12.41-12.66 backend tok/s for Orca; those lower observations are
retained in the aggregate data. Cache resets, traffic and policy changes are
confounded, so the later short-request rates are not a causal speedup estimate.

[Exact numerical observations, formulas and limitations](../data/serving-fairness-verification.json).
[Scheduling policy](MIXED-SERVING.md).

These Orca/Apex checks used the earlier 8 GiB RAM page tier. All six selected
Tabby/EXL3 launches now default bulk RAM KV spilling off while keeping their
existing recurrent budgets. No enabled/disabled speed comparison was run for
any model; the broader default is a policy choice. See the
[historical page-tier evidence](../archive/ram-prefix-tier/README.md).

Original documentation/data: [CC BY 4.0](../LICENSES/CC-BY-4.0.txt), with SourceHat attribution.
"""
    (REPO / "docs/SERVING-VERIFICATION.md").write_text(display_names(raw))


def memory_observation(evidence):
    observations = [row for row in evidence["memory_observations"] if row.get("preferred")]
    return next((row for row in observations if any(card.get("peak_used_mib") is not None for card in row.get("cards", []))),
                observations[0] if observations else {})


def prefix_verification():
    data = json.loads((REPO / "data/prefix-reuse-verification.json").read_text())
    cohorts = {row["id"]: row for row in data["cohorts"]}
    marker = "<!-- BEGIN GENERATED VERIFICATION -->"
    doc = REPO / "docs/PREFIX-REUSE.md"
    base = doc.read_text().split(marker)[0].rstrip()
    rows = []
    for identity in ("orca-final", "apex-final"):
        cohort = cohorts[identity]
        r = next(r for r in cohort["requests"] if r["check"] == "tool-result")
        label = {"orca-final":"Orca", "apex-final":"Apex EXL3"}[identity]
        rows.append([label, number(r["input_tokens"]), number(r["cached_input_tokens"]),
                     r["accepted_output_tokens"], number(r["backend_prefill_seconds"]),
                     number(r["client_first_progress_seconds"]), number(r["client_total_seconds"])])
    raw = "\n\n" + marker + "\n\n## Retained Long-History Checks\n\n"
    raw += ("These are separate bounded serving checks, with one observation per "
            "selected service and ordinary traffic uncontrolled. They are not averages or an isolated "
            "speedup estimate. Native requests use temperature zero and 128/256 output budgets, "
            "with a 128-token minimum. Orca follows an appended history without a middle edit; "
            "Apex returns to the original branch after an intentional middle edit. The histories "
            "differ, so this is not a matched model comparison.\n\n")
    raw += table(["Tool-result follow-up", "Input tokens", "Cached tokens", "Output tokens",
                  "Backend prefill s", "Client first progress s", "Client total s"], rows)
    raw += ("\nA meaningful edit still needs replay: the selected Apex middle-edit check rebuilt "
            "the changed suffix in 101.88 seconds. Cold Orca observations in distinct runtime "
            "cohorts took 237.81 and 329.42 seconds under different background traffic. "
            "Every cohort remains in the downloadable data, including slower observations. "
            "Earlier runtime variants are separate from the selected service; warm reuse "
            "does not establish faster cold prefill.\n\n")
    rows = []
    for identity, check in (("apex-final", "interleaved"),
                            ("orca-final-c2", "final-warm-plus-short")):
        for r in cohorts[identity]["requests"]:
            if r["check"] != check:
                continue
            rows.append(["Apex EXL3 / two long histories" if identity == "apex-final"
                         else "Orca / warm long + short", r["lane"], 2,
                         number(r["input_tokens"]), number(r["cached_input_tokens"]),
                         r["accepted_output_tokens"], number(r["backend_prefill_seconds"]),
                         number(r["backend_decode_tok_s_per_request"]),
                         number(r["client_first_progress_seconds"])])
    raw += "## Final Runtime Concurrent Progress\n\n"
    raw += table(["Wave", "Request", "Submitted requests", "Input tokens/request",
                  "Cached tokens/request", "Output tokens/request", "Prefill s/request",
                  "Backend decode tok/s/request", "Client first progress s/request"], rows)
    raw += ("\nGenerator traces confirm both streams advance in the same deliveries: "
            "103 shared delivery timestamps for Apex and 43 for Orca. Per-request backend "
            "rates are not aggregate wave throughput. Cached/fresh greedy continuations "
            "match on both final runtimes; cancellation and page-table audits pass. "
            "No general model-quality comparison or near-limit endurance test is implied.\n\n")
    coverage = [[r["recipe"], "shared runtime" if r["shared_prefix_runtime"] else "not applicable",
                 "passed", "passed" if r["new_live_history_check"] else "not rerun"]
                for r in data["profile_coverage"]]
    raw += "## Profile Coverage\n\n"
    raw += table(["Recipe", "ExLlama checkpoint retention", "Launch/config validation", "New live history checks"], coverage)
    raw += ("\nThese retained prefix checks preserve their tested settings. Apex's "
            "1,083,136-token test pool predates the separately qualified "
            "[1,374,976-token recipe](../recipes/apex-abliterated-exl3-mtp1-tp3/README.md#resident-kv-qualification).\n")
    raw += ("\nAll six Tabby recipes use the same engine and diagnostic launcher. "
            "Apex AWQ and DeepSeek use separate vLLM cache implementations. "
            "Their launch/configuration checks pass. Only Apex EXL3 and Orca "
            "received new GPU history checks.\n\n"
            "## Gateway Input Preservation\n\n"
            "Prefix reuse requires the gateway to preserve the rendered history, tool schemas "
            "and template options. Replica affinity selects the same cache but does not make "
            "different token prefixes equivalent. Archived gateway observations with different "
            "backend input counts are excluded from long-history performance comparisons; "
            "all observations and their qualification flags remain available.\n\n"
            "[Aggregate evidence and scope](../data/prefix-reuse-verification.json). "
            "[All 59 request observations, JSON](../data/prefix-reuse-requests.json). "
            "[Downloadable CSV](../data/prefix-reuse-requests.csv).\n")
    gateway = json.loads((REPO / "data/prefix-gateway-verification.json").read_text())
    raw += ("\n## Apex Gateway Validation\n\n"
            "A separate Apex-only check preserves all 131,240 input tokens through both "
            "gateway APIs. The entire rendered prompt and template options match native serving, "
            "including the qualified tool name, on an 826,701-character neutral history. "
            "The native cold request primes the cache; the gateway observations are warm and "
            "are not cold-runtime comparisons. These are single observations under uncontrolled "
            "ordinary traffic.\n\n")
    selected = [r for r in gateway["requests"] if r["check"] in (
        "exact-repeat", "tool-result", "concurrent-long", "concurrent-short")]
    rows = [[r["check"], r["submitted_concurrency"], number(r["input_tokens"]),
             number(r["cached_input_tokens"]), r["output_tokens"], number(r["backend_prefill_seconds"]),
             number(r["backend_decode_tok_s_per_request"]), number(r["client_first_progress_seconds"])]
            for r in selected]
    raw += table(["Gateway check", "Wave requests", "Input tokens/request", "Cached tokens/request",
                  "Output tokens/request", "Prefill s/request", "Backend decode tok/s/request",
                  "Client first progress s/request"], rows)
    raw += ("\nThe concurrent streams share 68 generator-delivery timestamps. Tool-result "
            "history reuse is verified with a supplied synthetic call/result; the forced "
            "128-token generation probe ended at its output limit without a completed call. "
            "No new general tool-generation, model-quality or near-limit qualification is implied. "
            "Orca was not loaded for this follow-up, so its gateway route was not retested.\n\n"
            "Small-budget behavior differs by API: gateway Responses generates 16 tokens for "
            "a one-token output maximum, while current native Responses and gateway Chat "
            "Completions generate one. The 128-token requests obey their budgets. The source "
            "of that minimum has not been established locally. Every running model stayed up; "
            "this follow-up changed no serving configuration or local runtime code.\n\n"
            "[Scope and numerical results](../data/prefix-gateway-verification.json). "
            "[All nine observations, CSV](../data/prefix-gateway-requests.csv).\n")
    doc.write_text(display_names(base + raw))


def capacity_section(recipe):
    filename = recipe.get("qualification", {}).get("capacity_file")
    if not filename:
        return ""
    data = json.loads((REPO / filename).read_text())
    raw = ("\n## Resident KV Qualification\n\n"
           f"The selected **{number(data['resident_pool_tokens'])}-token Q8/Q8 pool** is "
           f"**{data['increase_percent']:.1f}% larger** than the earlier allocation. "
           "It retains four slots, a 524,288-token per-request context and fixed MTP1 "
           "with adaptation disabled. Two independent reference-host loads passed "
           "mixed prefill/decode, output growth on all slots, near-context retrieval, "
           "tool-call/result continuation, cancellation and recurrent prefix reuse.\n\n")
    rows = [[index + 1, number(load["distinct_history_input_tokens"]),
             f"{100 * load['pool_fraction']:.2f}%", load["active_slots"],
             number(min(load["physical_min_free_bytes_by_rank"]) / 2**20)]
            for index, load in enumerate(data["independent_loads"])]
    raw += table(["Independent load", "Distinct history input, tokens", "Fraction of pool",
                  "Peak active slots", "Lowest physical free memory/card, MiB"], rows)
    raw += ("\nEach load exercised distinct histories above 95% of the pool. "
            "The memory guard requires at least 256 MiB physically free on every "
            "selected GPU throughout the recorded sampling interval. This is a "
            "bounded qualification on those devices, not an exhaustive capacity search "
            "or four simultaneous maximum-length histories. Bulk host KV spilling stays off; "
            "the 16 GiB recurrent-checkpoint budget is separate.\n\n"
            "The main-model autosplit reserves are **2,560 / 2,336 / 2,848 MiB** "
            "in selected GPU-rank order. The last selected GPU also carries the draft. "
            "The reference order is CPU Gen2 x8, CPU Gen2 x4, PCH Gen2 x4; "
            "preserve the rank order or retune for different devices.\n\n"
            "The performance table below retains its earlier **1,083,136-token** "
            "test pool and placement. Later completion-rate probes varied by workload "
            "and load and use a different backend timer; they are retained in the "
            "qualification data and are not substituted for synchronized aggregate decode.\n\n"
            "[Numerical capacity evidence](../../data/apex-kv-capacity/evidence.json) | "
            "[Two-load source report](../../data/apex-kv-capacity/qualification-report.json) | "
            "[Saved profile](../../data/apex-kv-capacity/saved-profile.json). "
            "Run `python3 scripts/apex_capacity.py` from the repository root to "
            "verify the included source identities, capacity arithmetic and recipe settings.\n")
    return display_names(raw)


def card(recipe):
    r, s, m = recipe, recipe["serving"], recipe["model"]
    mode = s["speculation"]["method"]
    speculation = f"{mode} / depth {s['speculation']['depth']}" if mode else "N/A"
    if s["speculation"].get("adaptive"):
        speculation = f"{mode} / up to {s['speculation']['depth']} (adaptive)"
    pool = s["kv"]["shared_gpu_pool_tokens"]
    normalized = s["kv"].get("capacity_basis") == "vllm_context_normalized_block_capacity"
    folder = REPO / "recipes" / r["id"]
    evidence = json.loads((folder / "evidence.json").read_text())
    memory = memory_observation(evidence)
    def gib(value):
        return number(value / 2**30) if value is not None else "-"
    parameters = [
        ["Checkpoint", f"[{m['hf_repo']}](https://huggingface.co/{m['hf_repo']}/tree/{m['revision']})"],
        ["Checkpoint revision", f"`{m['revision']}`"], ["Quantization", m["quantization"]],
        ["Runtime", r["runtime"]["engine"]], ["Runtime version", r["runtime"]["version"]],
        ["Cards", f"{r['hardware']['card_count']} x 64 GiB SM80"],
        ["Layout", s["parallelism"].replace("_", " ") if s["parallelism"] else "single card"],
        ["OpenAI model id", f"`{m['served_name']}`"], ["Configured request slots", s["max_requests"]],
    ]
    parameters += [
        ["Per-request context, tokens", number(s["context_tokens"])],
        ["Context-normalized KV capacity, token-equivalents" if normalized else "Shared GPU KV pool, tokens", number(pool)],
        ["Main KV", s["kv"]["main_dtype"] or "N/A"], ["Draft KV", s["kv"]["draft_dtype"] or "N/A"],
        ["Speculation", speculation], ["Prefill chunk, tokens", number(s["prefill_chunk_tokens"])],
        ["Recurrent RAM checkpoint budget, MiB", number(s["kv"]["host_recurrent_budget_mib"])],
    ]
    if pool and s["context_tokens"]:
        parameters += [["Full-context requests, sizing estimate" if normalized else "Full unshared histories, pool arithmetic",
                        pool // s["context_tokens"]]]
        if normalized:
            parameters += [["Capacity reporting context, tokens", number(s["kv"]["capacity_context_tokens"])]]
        else:
            parameters += [["KV left after one full history, tokens", number(pool - s["context_tokens"])]]
    if r["runtime"]["id"] == "apex-awq":
        parameters += [["PP layer partition", "17 / 15 / 13"], ["Automatic memory utilization", "0.985"],
                       ["Draft checkpoint", f"[{r['draft_model']['hf_repo']}](https://huggingface.co/{r['draft_model']['hf_repo']}/tree/{r['draft_model']['revision']})"],
                       ["Draft weights", "BF16; target-matched embedding"]]
    if r["runtime"]["id"] == "deepseek":
        parameters += [["Automatic memory utilization", "0.98391"], ["Engram backing", "NVMe; 64 MiB row cache"],
                       ["Execution", "eager; batch invariant"]]
    if memory:
        cards = memory.get("cards", [])
        parameters += [["Observed main GPU KV payload, GiB", gib(memory.get("main_gpu_kv_payload_bytes"))],
                       ["Observed draft GPU KV payload, GiB", gib(memory.get("draft_gpu_kv_payload_bytes"))],
                       ["Observed host KV allocation, GiB", gib(memory.get("host_kv_allocated_bytes"))],
                       ["Observed peak VRAM/card, GiB", number([card["peak_used_mib"] / 1024 for card in cards if card.get("peak_used_mib") is not None])],
                       ["Memory observation phase", memory.get("label", "-")]]
        if memory.get("peak_memory_definition"):
            parameters += [["Peak VRAM accounting", memory["peak_memory_definition"]]]
    if r.get("qualification", {}).get("capacity_file"):
        parameters += [["Autosplit reserve by selected GPU rank, MiB",
                        number(r["engine_config"]["model"]["autosplit_reserve"])]]
    quant = evidence["quantization"]
    if quant.get("observed_formats"):
        parameters += [["Output head format", quant["observed_formats"]["output_head"]],
                       ["MTP expert format", quant["observed_formats"]["mtp_experts"]]]
    if quant.get("groups"):
        main_groups = [row for name, row in quant["groups"].items() if name != "native_MTP"]
        parameters += [["Routed-expert payload bits/parameter", number(quant["groups"]["routed_experts"]["payload_bits_per_logical_parameter"], 4)],
                       ["Main weight payload, bytes", number(sum(row["payload_bytes"] for row in main_groups))],
                       ["Main logical parameters", number(sum(row["logical_parameters"] for row in main_groups))],
                       ["Main payload bits/parameter", number(quant["main_payload_bits_per_logical_parameter"], 4)],
                       ["Native MTP weights present", "yes" if quant["native_MTP_present"] else "no"]]
        source = next((row for row in json.loads((REPO / "data/quantization-sources.json").read_text())["records"]
                       if row["recipe"] == r["id"]), None)
        if source and "complete_checkpoint" in source:
            checkpoint = source["complete_checkpoint"]
            parameters += [["Complete checkpoint files including MTP, bytes", number(checkpoint["file_bytes_including_headers"])],
                           ["Complete checkpoint logical parameters", number(checkpoint["logical_parameters"])],
                           ["Complete checkpoint effective bpw", number(checkpoint["effective_file_bits_per_weight"], 5)],
                           ["Effective bpw calculation", "`8 * stored weight bytes / logical parameters` (matching tensor scope)"]]
    benchmark = json.loads((REPO / "recipes" / r["id"] / "benchmarks.json").read_text())
    points = benchmark["points"]
    rows, historical_rows = [], []
    for p in points:
        row = [number(p["input_tokens_per_request"]), p["concurrency"], p["cache_state"], number(p["output_tokens_per_request"]),
                     number(p["decode_tok_s_aggregate"]), number(p["decode_tok_s_per_request"]), number(p["ttft_median_seconds"]),
                     number(p.get("backend_prefill_tok_s_per_request_median")),
                     number(p.get("draft_acceptance_ratio") * 100 if p.get("draft_acceptance_ratio") is not None else None),
                     number(p.get("end_to_end_accepted_tok_s")), number(p.get("tested_kv_pool_tokens")),
                     number(p["test_configuration"].get("context"))]
        current = p["headline_eligible"] and (not benchmark.get("preferred_headline_cohort")
                  or p["cohort"] == benchmark["preferred_headline_cohort"])
        (rows if current else historical_rows).append(row)
    slots = r["hardware"]["card_count"]
    devices = ",".join(map(str, range(slots)))
    download_directory = model_directory = f"/path/to/models/{m['served_name']}"
    runtime_option = " \\\n  --runtime-root /path/to/prepared/runtimes"
    extra = ""
    if r["runtime"]["id"] == "apex-awq":
        extra = " \\\n  --draft-path /path/to/prepared-dflash2-head"
    if r["runtime"]["id"] == "deepseek":
        download_directory = "/path/to/deepseek-source"
        model_directory = "/path/to/deepseek-tp3"
        runtime_option = ""
        extra = " \\\n  --source-model-path /path/to/deepseek-source \\\n  --engram-path /path/on/nvme/engram-tables"
    raw = f"# {r['title']}\n\nRecipe for NVIDIA CMP 170HX cards with 64 GiB usable VRAM.\n\n"
    lineage = m.get("lineage")
    if lineage:
        developers = " and ".join(lineage["developers"])
        raw += (f"**Model lineage:** Apex Flash 1 is {developers}'s reinforcement-learning "
                "post-train of **GLM 5.3 Flash** for security investigations. This recipe serves "
                "a quantization of the **abliterated Apex derivative**. The "
                f"[publisher's model card]({lineage['model_card']}) describes the standard Apex "
                "checkpoint; its benchmark results do not establish this derivative's quality.\n\n")
        parameters += [["Base model", lineage["base_model"]],
                       ["Post-trained checkpoint", lineage["post_trained_model"]],
                       ["Post-training method", lineage["post_training_method"]],
                       ["Parent checkpoint", f"[{lineage['parent_checkpoint']}](https://huggingface.co/{lineage['parent_checkpoint']}/tree/{lineage['parent_revision']})"]]
    raw += table(["Parameter", "Value"], [row for row in parameters if row[1] not in {"-", "N/A"}])
    raw += f"\n## Reproduce\n\nPrepare the matching [{r['runtime']['id']} runtime](../../docs/REPRODUCING.md), then download the pinned checkpoint:\n\n"
    raw += f"```bash\npython3 scripts/download_model.py {r['id']} \\\n  --directory {download_directory}\n```\n\n"
    if r["runtime"]["id"] == "deepseek":
        raw += "Complete the [TP3 transformation and NVMe Engram preparation](../../docs/REPRODUCING.md) before launching. The launcher builds and runs the pinned Docker Compose service; it does not need a host Python inference environment.\n\n"
    raw += "Run from the repository root. Replace the example device ordinals with your own selection in layer/pipeline order:\n\n"
    raw += f"```bash\nbash recipes/{r['id']}/launch.sh \\\n  --devices {devices}{runtime_option} \\\n  --model-path {model_directory}{extra} \\\n  --dry-run\n```\n\n`--dry-run` prints the command, environment and rendered config without importing a GPU runtime. Remove it to serve. The launcher runs in the foreground; Ctrl-C stops it.\n\n"
    raw += "The engine-native template is in [config.yml](config.yml).\n" if r['runtime']['id']=='tabby' else "The engine argument/settings template is in [engine-config.json](engine-config.json).\n"
    raw += "\n## Interface\n\nChoose the listener with `--host` and `--port`; see [launch options](../../docs/REPRODUCING.md#launch-options).\n\n"
    raw += "Endpoints: `/v1/models`, `/v1/chat/completions` and `/v1/completions`. Chat serving supports the selected engine's tool-call parser and a tool-result continuation.\n"
    raw += capacity_section(r)
    raw += "\n## Measurements\n\n"
    if s["speculation"].get("adaptive"):
        raw += ("These retained throughput waves used fixed MTP3. The current recipe uses "
                "adaptive MTP up to three; [later live serving checks](../../docs/MIXED-SERVING.md) "
                "are a separate dataset.\n\n")
    headers = ["Actual input/request, tokens", "Requests", "Cache", "Output budget/request, tokens", "Decode total tok/s", "Decode/request tok/s",
               "TTFT median, s", "Prefill/request tok/s", "Draft acceptance %", "End-to-end total tok/s", "Test pool tokens / equivalents", "Test context limit, tokens"]
    if rows:
        raw += "Decode is accepted output tokens/s, including reasoning and excluding prefill. Concurrent rates are whole-wave aggregate. TTFT is the median first-token latency across the listed requests. Prefill is the backend's per-request timer, whose boundaries differ between engines. Output budgets are distinct from tokens counted inside the common decode interval.\n\n"
        raw += table(headers, rows)
    else:
        raw += "Qwen 3.8 27B was benchmarked with three independent one-card replicas, at one or sixteen concurrent requests per replica (three or forty-eight requests total). The four cold/warm measurements below use 2,048-8,192 input tokens and a 1,024-output-token budget per request. They do not measure the current eight-slot service at 32k input. Exact values are in [historical-replica-result.json](historical-replica-result.json).\n"
        history = json.loads((folder / "historical-replica-result.json").read_text())
        historic_rows = []
        for mode, waves in history["measurements"].items():
            requests_per_replica = 1 if mode == "one_stream_per_card" else 16
            for state, wave in waves.items():
                historic_rows.append([requests_per_replica, history["replicas"], requests_per_replica * history["replicas"], state,
                                      number(wave["aggregate_generation_tps"]),
                                      number([card["generation_tps"] for card in wave["per_card"]]),
                                      number(wave["window_seconds"]), number(wave["generated_tokens"])])
        raw += "\nHistorical rig measurements at their recorded geometry:\n\n"
        raw += table(["Requests/replica", "Replicas", "Rig requests", "Source wave", "Decode rig total tok/s",
                      "Decode/replica tok/s", "Shared interval s", "Tokens in interval"], historic_rows)
    if historical_rows:
        raw += "\n<details>\n<summary>Earlier measurements of these weights and decoding layout</summary>\n\n"
        raw += "These use the recorded earlier pool/context/runtime geometry. Full configurations and source references are included in the numerical export.\n\n"
        raw += table(headers, historical_rows)
        raw += "\n</details>\n"
    if rows or historical_rows:
        raw += "\nRecorded per-request timers, accepted/proposed counts, decode intervals, cache-hit counters and source SHA256 references: [benchmarks.json](benchmarks.json). Unavailable fields remain null. The configured serving pool and each measured test pool are labeled separately.\n"
    else:
        raw += "\nThe historical export retains shared decode intervals, accepted-token totals, per-replica contributions and backend-rate summaries in [historical-replica-result.json](historical-replica-result.json). Source wave labels `cold` and `warm` are preserved; the export does not independently verify the warm-prefix hit. No current eight-slot wave is supplied in [benchmarks.json](benchmarks.json).\n"
        raw += "\nA separate [saved 32k MTP1 retention check](../../docs/QWEN-32K-EVIDENCE.md) retains two cold requests and two cached continuations. Its C2 workload and historical settings do not supply the missing C1/C8 comparison.\n"
    if r["id"] == "apex-abliterated-awq-dflash2-pp3-balanced":
        raw += "\nThe two 8,192-output observations retain [native prefill recovered from saved metric snapshots](../../docs/RECOVERED-PREFILL.md). Their prefill is kept with that exact workload; the older 256-output C1/C4 rows have no retained native timer.\n"
    if benchmark.get("preferred_headline_cohort") == "selected-serving-native-prefill":
        raw += "\nThe headline pair uses the [selected-serving prefill comparison](../../docs/PREFILL-COMPARISON.md), with zero verified cached input tokens and bulk RAM spilling disabled. The full numerical traces reproduce its synchronized decode values. Earlier results retain their original settings and remain separate.\n"
        if r["runtime"]["id"] in {"apex-awq", "deepseek"}:
            raw += "\nThe exported launch template retains an 8 GiB native offload budget; the timed headline jobs used zero. This setting differs explicitly, and the comparison does not establish an offload speedup or requalify the earlier capacity report.\n"
    raw += "\n## Earlier Verification\n\n" if r.get("qualification", {}).get("capacity_file") else "\n## Verification\n\n"
    if r["runtime"]["id"] == "tabby":
        raw += "The shared runtime includes [long-history checkpoint retention](../../docs/PREFIX-REUSE.md).\n\n"
    checks = evidence["verification"]
    verification_rows = []
    if checks.get("tool_round_trip"):
        verification_rows.append(["Tool-call/result round trip", "passed" if checks["tool_round_trip"]["passed"] else "failed"])
    if checks.get("target_reference_correctness"):
        verification_rows.append(["Recorded target/reference checks", "passed" if checks["target_reference_correctness"]["passed"] else "failed"])
    context = checks.get("context")
    if context:
        verification_rows += [["Context check", "passed" if context["passed"] else "failed"],
                              ["Context-check actual long input, tokens", number(context["actual_long_request_prompt_tokens"])],
                              ["Context-check normalized capacity, token-equivalents" if normalized else "Context-check pool, tokens",
                               number(context["resident_pool_tokens"])],
                              ["Concurrent requests in context check", len(context.get("requests", []))],
                              ["Retrieval answer checked", "yes" if context.get("useful_long_context_retrieval") else "no"],
                              ["RAM history restoration", "passed" if context.get("history_restoration_answer_matched") else "not retested"]]
    if checks.get("historical_validation"):
        verification_rows += [["Historical validation checks", "passed" if checks["historical_validation"]["checks_passed"] else "failed"],
                              ["Historical tested slots/replica", checks["historical_validation"]["tested_slots_per_replica"]],
                              ["Native-context input stages, tokens", number([stage["tokens"] for stage in checks["historical_validation"]["native_context_stages"]])],
                              ["Native-context checks", "passed" if all(stage["passed"] for stage in checks["historical_validation"]["native_context_stages"]) else "failed"],
                              ["RAM history restoration", checks["historical_validation"]["ram_restore"]]]
    if verification_rows:
        raw += table(["Check", "Result"], verification_rows)
    raw += "\nAllocation audits, per-card memory counters, task checks, quantization metadata and verification provenance: [evidence.json](evidence.json). [Data definitions](../../docs/DATA.md) explain measurement scope and missing fields.\n"
    raw += "\n## Tradeoffs\n\n" + evidence["selection_rationale"] + "\n"
    raw += "\n## Qualification And Limits\n\n"
    if normalized:
        raw += ("The legacy `shared_gpu_pool_tokens` metadata field records vLLM's context-normalized "
                "capacity report: calculated full-context concurrency times the configured maximum "
                "context, rounded down. It uses cache-block requirements across groups, including "
                "sliding/compressed attention and state. It is not a literal count of resident token "
                "slots or free cache tokens, and the full-context sizing estimate is not a measured "
                "concurrency limit. See [data definitions](../../docs/DATA.md#memory-and-context).\n\n")
    raw += "\n".join("- " + n for n in r["notes"]) + "\n"
    raw += f"- {r['qualification']['status']}.\n"
    if r["id"] == "deepseek-v41-flash-dspark5-tp3":
        raw += "\n## DeepSeek V4.1 Flash 1017 TP4\n\nThe [four-card configuration](../../profiles/deepseek-v41-flash-1017-dspark5-tp4/README.md) uses the 1017 EXL3 2.9 bpw artifact and its qualified native runtime. Its [long-output and concurrency experiments](../../docs/DEEPSEEK-1017.md) have different weights, software and output budgets from this TP3 configuration; the measurements do not isolate a hardware speedup.\n"
    raw += "\nThis original recipe documentation and data are [CC BY 4.0](../../LICENSES/CC-BY-4.0.txt); attribute SourceHat and link to this recipe when sharing or adapting them. The checkpoint's own model license applies to downloaded weights. Runtime code and patches retain the licenses described in [THIRD_PARTY.md](../../THIRD_PARTY.md).\n"
    return display_names(raw)


def headline_points(recipe, points):
    serving = recipe["serving"]
    cold = [point for point in points if point["headline_eligible"]
            and point["input_target_tokens"] == 32768 and point["cache_state"] == "cold"
            and point["output_tokens_per_request"] in (256, 512)]
    preferred = [point for point in cold if point["cohort"] == "selected-serving-native-prefill"]
    if preferred:
        cold = preferred
    wave = next((point for point in cold if point["concurrency"] == serving["max_requests"]), None)
    if wave is None:
        raise ValueError("Missing cold configured-concurrency measurement: " + recipe["id"])
    single = next((point for point in cold if point["concurrency"] == 1
                   and point["cohort"] == wave["cohort"]
                   and point["test_configuration"] == wave["test_configuration"]
                   and point["output_tokens_per_request"] == wave["output_tokens_per_request"]), None)
    if single is None:
        raise ValueError("Missing matching cold one-request measurement: " + recipe["id"])
    return single, wave


def quant_label(recipe):
    if recipe["id"] == "apex-abliterated-exl3-mtp1-tp3":
        quant = json.loads((REPO / "recipes" / recipe["id"] / "evidence.json").read_text())["quantization"]
        groups = [row for name, row in quant["groups"].items() if name != "native_MTP"]
        bpw = 8 * sum(row["payload_bytes"] for row in groups) / sum(row["logical_parameters"] for row in groups)
        return f"EXL3 {bpw:.2f} bpw"
    labels = {
        "apex-abliterated-awq-dflash2-pp3-balanced": "AWQ INT4, g128",
        "deepseek-v41-flash-dspark5-tp3": "EXL3 2.0 bpw experts (MCG)",
    }
    return labels.get(recipe["id"], recipe["model"]["quantization"])


def summary_row(recipe, points=None):
    serving = recipe["serving"]
    return [f"[{recipe['short_name']}](recipes/{recipe['id']}/README.md)", quant_label(recipe),
            recipe["hardware"]["card_count"], number(serving["context_tokens"]),
            number(serving["kv"]["shared_gpu_pool_tokens"]), serving["max_requests"]]


def performance_row(recipe, points):
    if recipe["id"] == "qwen3.8-27b-exl3" and not any(
            point["headline_eligible"] for point in points):
        history = json.loads((REPO / "recipes" / recipe["id"] / "historical-replica-result.json").read_text())
        single = history["measurements"]["one_stream_per_card"]["cold"]
        wave = history["measurements"]["sixteen_streams_per_card"]["cold"]
        rates = [card["generation_tps"] for card in single["per_card"]]
        c1 = number(sorted(rates)[len(rates) // 2])
        inputs = history["input_range_tokens"]
        workload = f"{number(inputs[0])}-{number(inputs[-1])} / {number(history['output_tokens_per_request'])}"
        requests = wave["per_card"][0]["requests"]
        wave_rates = [card["generation_tps"] for card in wave["per_card"]]
        aggregate = number(sorted(wave_rates)[len(wave_rates) // 2])
        timings = single["request_timing_by_replica"]
        prefill_rates = [value for row in timings for value in row["backend_prefill_tok_s_per_request"]]
        first_tokens = [value for row in timings for value in row["client_ttft_seconds_per_request"]]
        prefill = number(sorted(prefill_rates)[len(prefill_rates) // 2])
        ttft = number(sorted(first_tokens)[len(first_tokens) // 2])
    else:
        single, wave = headline_points(recipe, points)
        workload = f"{number(wave['input_target_tokens'])} / {number(wave['output_tokens_per_request'])}"
        c1 = number(single["decode_tok_s_aggregate"])
        requests = wave["concurrency"]
        aggregate = number(wave["decode_tok_s_aggregate"])
        prefill = number(single.get("backend_prefill_tok_s_per_request_median"))
        ttft = number(single["ttft_median_seconds"])
    return [f"[{recipe['short_name']}](recipes/{recipe['id']}/README.md)", workload, prefill,
            ttft, c1, requests, aggregate]


def archive_result_rows(profile, points):
    return [[profile["name"], point["concurrency"],
             number(point["input_tokens_per_request"]),
             number(point["decode_tok_s_aggregate"]),
             number(point["end_to_end_accepted_tok_s"]),
             number(point["ttft_median_seconds"]),
             number(point["ttft_slowest_seconds"])] for point in points]


def archive_card(profile):
    folder = REPO / "archive" / profile["id"]
    evidence = json.loads((folder / profile["evidence_file"]).read_text())
    points = json.loads((folder / profile["benchmark_file"]).read_text())["points"]
    runtime = json.loads((REPO / profile["runtime_file"]).read_text())
    model, serving = profile["model"], profile["serving"]
    kv = serving["kv"]
    memory = evidence["memory"]
    raw = f"""# {profile['name']}

**Archived historical configuration.** {profile['archive_reason']}

The recommended alternative is [Flash Next EXL3 / MTP2 layer split](../../recipes/{profile['recommended_recipe']}/README.md).
This archive preserves the tested settings and numeric evidence. Its native
Strata server template requires your own runtime setup; the repository's
recipe launcher does not support this archived runtime.

## Model And Runtime

"""
    raw += table(["Setting", "Recorded value"], [
        ["Model", model["name"]],
        ["Main artifact", f"[{model['repository']}](https://huggingface.co/{model['repository']}/tree/{model['revision']}/{model['quantization']})"],
        ["Main revision", f"`{model['revision']}`"],
        ["Main quantization", model["quantization"] + " (mixed tensor formats)"],
        ["MTP source", f"[{model['mtp']['repository']}](https://huggingface.co/{model['mtp']['repository']}/tree/{model['mtp']['revision']})"],
        ["MTP revision", f"`{model['mtp']['revision']}`"],
        ["MTP expert format", "Q2_0, 2.25 stored bits/weight"],
        ["Runtime", f"[Strata {runtime['version']}]({runtime['repository']}/tree/{runtime['revision']})"],
        ["Runtime revision", f"`{runtime['revision']}`"],
        ["Required cards", f"{profile['hardware']['card_count']} x CMP 170HX, 64 GiB usable VRAM each, SM80"],
        ["Measurement power limit", "200 W/card"],
        ["Build", ", ".join(f"{key}={value}" for key, value in profile["build"]["settings"].items())],
    ])
    raw += "\nExact shard names, recorded binary hash and build settings are in [profile.json](profile.json). [runtime.json](../runtime.json) pins Strata and its llama.cpp dependency and identifies the included allocation-audit patch.\n"
    raw += "\n## Context And Memory\n\n"
    raw += table(["Setting / observation", "Value"], [
        ["Configured context limit per request, tokens", number(serving["context_tokens"])],
        ["Allocated batch slots", serving["max_requests"]],
        ["Main / draft KV", "INT8 / INT8, allocation-audited"],
        ["Resident GPU KV per batch slot, tokens", number(kv["resident_gpu_tokens_per_batch_slot"])],
        ["Resident batch GPU KV, tokens", number(kv["resident_batch_gpu_tokens"])],
        ["Logical host-backed batch capacity, tokens", number(kv["logical_batch_tokens"])],
        ["Separate solo GPU workspace, tokens", number(kv["separate_solo_gpu_tokens"])],
        ["Separate solo logical capacity, tokens", number(kv["separate_solo_logical_tokens"])],
        ["Observed host KV allocation, GiB", number(kv["observed_host_allocation_bytes"] / 2**30)],
        ["Sampled peak VRAM per measurement card, GiB", number([x / 1024 for x in memory["sampled_peak_vram_mib_per_card"]])],
        ["Resident expert cache, GiB", number(memory["resident_expert_cache_mib"] / 1024)],
        ["Requested speculation / observed maximum verification, tokens", f"{serving['speculation']['requested_spec_tokens']} / {serving['speculation']['observed_max_verification_tokens']}"],
        ["Maximum native MTP window, tokens", serving["speculation"]["native_mtp_max_tokens"]],
        ["Batch MTP", "Off in the observed allocation; native MTP weights loaded"],
        ["Prompt-lookup n-gram length", serving["speculation"]["prompt_lookup_ngram"]],
    ])
    raw += """
Each batch slot has 32,768 resident GPU tokens within its configured
262,144-token logical capacity. The remaining history uses host-backed operation;
simultaneous full-context requests were not qualified.
The separate solo workspace is not added to the batch pool. The small resident
workspace can require host transfers as active histories grow; their effect
near the configured context limit was not measured.

This historical Strata mechanism backs active KV with host memory; its
recorded settings remain distinct from the selected Tabby recipes.

## Measured Results

One cold wave per mode: a synthetic coding prompt targeting 32,768 input
tokens and 256 accepted output tokens per request, temperature zero, seed
`20261008`, low reasoning effort. Actual input counts appear in the table.
Accepted reasoning tokens count toward output. These are individual waves,
not averages across repeated runs.

"""
    raw += table(["Configuration", "Wave requests", "Actual input tokens/request",
                  "Shared decode tok/s total", "Whole-wave output tok/s",
                  "Median TTFT, s", "Slowest TTFT, s"], archive_result_rows(profile, points))
    raw += """
Shared decode excludes prefill and counts accepted tokens only between the
last request's first generation event and the first completion. Whole-wave
throughput includes prefill, queueing and generation. First-token times
include queueing. A dash means no qualified common decode interval.

"""
    if any(not point["shared_decode_valid"] for point in points):
        raw += "The eight-request IQ4 wave had **no common eight-request decode interval**. Its 6.32 tok/s is whole-wave throughput; concurrent decode throughput remains unqualified.\n\n"
    raw += "Exact intervals, accepted-token numerators, per-request arrays, draft counts and source receipts: [benchmarks.json](benchmarks.json). [evidence.json](evidence.json) preserves memory/precision audits, tensor formats, artifact hashes and verification. The combined [archive CSV](../benchmarks.csv) contains these four waves separately from the recommended recipes.\n"
    raw += "\n## Historical Configuration\n\n"
    raw += """[engine-config.json](engine-config.json) preserves the original native engine
arguments and server settings, with deployment values replaced by placeholders:

"""
    raw += table(["Placeholder", "Supply"], [
        ["`@STRATA_BINARY@`", "Your SM80 Strata build matching the recorded variant"],
        ["`@STRATA_SOURCE@`", "Pinned Strata checkout, also used for its expert profile"],
        ["`@MODEL_ROOT@`", "Directory containing all pinned GGUF shards in their quantization subdirectory"],
        ["`@PACK@`", "Dense/tokenizer pack produced by the pinned iq_pack.py with --compat-bf16"],
        ["`@MTP_PACK@`", "Native MTP runtime pack from the pinned source, Q2_0 experts"],
        ["`@PLE_GGUF@`", "Lossless PLE-only GGUF view; layout and hash retained in evidence.json"],
        ["`@DEVICES@`", "Your ordered device selection, using the recorded card count"],
        ["`@MODEL_NAME@`, `@HOST@`, `@PORT@`", "Your served name and listener"],
        ["`@API_KEY@`, `@LOG_PATH@`", "Your server credential and log destination"],
    ])
    raw += """
The historical build included the metadata-only [allocation-audit patch](../runtime/kv-allocation.patch).
Its [MIT notice](../runtime/LICENSE.Strata.txt) is retained. The original serving
wrapper and a portable Strata installer/launcher are not included; the template
has not been GPU-reproduced from this checkout. No model weights or compiled
binaries are redistributed.

## Limits And Selection

"""
    raw += "\n".join("- " + item for item in profile["limitations"]) + "\n"
    raw += "\nThe recorded tool round trip passed. The legacy completions adapter was CPU-verified after the GPU trial; this archive does not export that adapter or claim complete API compatibility.\n"
    if evidence["verification"]["kernel_parity"]:
        raw += "The Q6 expert, grouped-expert and MMQ K-quant parity checks also passed.\n"
    raw += "\nNo paired general-quality comparison establishes the quality loss from IQ4 versus Q6 or EXL3. Hardware, runtime and quantization differ between alternatives, so their speed differences do not isolate a single cause.\n\n[Archive index](../README.md) | [Recommended recipes](../../README.md) | [Data definitions](../../docs/DATA.md) | [Attribution](../../LICENSE)\n"
    return display_names(raw)


def archive_docs():
    catalog = json.loads((REPO / "archive/catalog.json").read_text())
    profiles = [json.loads((REPO / entry["path"]).read_text()) for entry in catalog["profiles"]]
    configuration_rows, result_rows, csv_rows = [], [], []
    for profile in profiles:
        folder = REPO / "archive" / profile["id"]
        points = json.loads((folder / profile["benchmark_file"]).read_text())["points"]
        (folder / "README.md").write_text(archive_card(profile))
        kv = profile["serving"]["kv"]
        configuration_rows.append([f"[{profile['name']}]({profile['id']}/README.md)",
                                   profile["hardware"]["card_count"], profile["serving"]["max_requests"],
                                   number(profile["serving"]["context_tokens"]),
                                   number(kv["resident_batch_gpu_tokens"]), number(kv["logical_batch_tokens"])])
        result_rows.extend(archive_result_rows(profile, points))
        csv_rows.extend(dict(profile=profile["id"], **point) for point in points)
    raw = """# Strata Runtime Comparisons

Two previously tested Strata configurations, retained as historical alternatives.
Each has a native engine configuration template, checkpoint/runtime pins, exact
measurements and selection limits. These are historical records requiring your
own Strata integration. The [recommended catalog](../catalog.json) and launch
helpers cover the portable entries in the [selected configuration inventory](../README.md).

## Saved Configurations

"""
    raw += table(["Configuration", "Cards", "Batch slots", "Context tokens/request",
                  "Resident batch GPU KV tokens", "Logical host-backed batch tokens"], configuration_rows)
    raw += """
Context is the configured per-request limit. Each batch slot has 32,768 resident
GPU tokens. Batch capacities span the allocated slots; the separate 32,768-token solo GPU workspace is listed only on each
profile's page. Neither configuration was qualified near its full context limit.

## Retained Performance

All four waves use approximately 32k input tokens and 256 accepted output tokens
per request. Each row is one cold wave; request count is explicit.

"""
    raw += table(["Configuration", "Wave requests", "Actual input tokens/request",
                  "Shared decode tok/s total", "Whole-wave output tok/s",
                  "Median TTFT, s", "Slowest TTFT, s"], result_rows)
    raw += """
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
"""
    (REPO / "archive/STRATA.md").write_text(raw)
    with (REPO / "archive/benchmarks.csv").open("w", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=list(csv_rows[0]), lineterminator="\n")
        writer.writeheader()
        for row in csv_rows:
            writer.writerow({key: json.dumps(value, separators=(",", ":")) if isinstance(value, (list, dict)) else value
                             for key, value in row.items()})


def main():
    prefix_verification()
    archive_docs()
    from history_docs import build_history_docs
    build_history_docs(REPO)
    (REPO / "docs/RECOVERED-PREFILL.md").write_text(recovered_prefill_document())
    (REPO / "docs/QWEN-32K-EVIDENCE.md").write_text(qwen_32k_document())
    if (REPO / "data/selected-serving-prefill.json").exists():
        (REPO / "docs/PREFILL-COMPARISON.md").write_text(selected_prefill_document())
    catalog = json.loads((REPO / "catalog.json").read_text())
    publication = json.loads((REPO / "publication.json").read_text())
    recipes = [json.loads((REPO / r["path"]).read_text()) for r in catalog["recipes"]]
    order = ["qwen27-orca-mtp3-native", "qwen-flash-next-mtp2-layer-split", "mimo-flash-mtp1-tp3",
             "glm-5.3-flash-mtp1-tp3", "apex-abliterated-exl3-mtp1-tp3",
             "apex-abliterated-awq-dflash2-pp3-balanced", "deepseek-v41-flash-dspark5-tp3",
             "qwen3.8-27b-exl3"]
    recipes.sort(key=lambda r:order.index(r["id"]))
    rows = []
    performance_rows = []
    csv_rows = []
    for r in recipes:
        (REPO / "recipes" / r["id"] / "README.md").write_text(card(r))
        p = json.loads((REPO / "recipes" / r["id"] / "benchmarks.json").read_text())["points"]
        rows.append(summary_row(r, p))
        performance_rows.append(performance_row(r, p))
        for point in p:
            csv_rows.append(dict(recipe=r["id"], **point))
    raw = """# CMP 170HX Model Recipes

Nine selected language-model serving configurations for NVIDIA CMP 170HX GPUs,
with pinned checkpoints, engine-native settings and measured results from
model and runtime comparisons.

The inventory below covers every configuration in the study. Each entry links
its settings, setup requirements and numerical evidence. Portable launchers
are included for TabbyAPI and the three-card vLLM configurations; the four-card
DeepSeek configuration records its qualified native-runtime dependencies.

"""
    article = publication["article"]
    article_status = ("Publication is pending; the link is the intended SourceHat\n"
                      "article address.") if article['status'] == 'draft' else "Published on SourceHat."
    raw += f"""## Companion Article

[{article['title']}]({article['url']}) explains the configuration choices,
speculative-decoding comparisons, cache-capacity tradeoffs and runtime trials
behind these recipes. {article_status}

## Serving Configurations

Reference hardware: NVIDIA CMP 170HX with **64 GiB usable VRAM per card**,
SM80, 200 W per card, with cmpunlocker exposing the cards' full memory.

**PCIe limitation:** GPU1, GPU2 and GPU3 use **x4 links**; GPU0 uses x8.
The original multi-card comparisons use Gen2 links and host-mediated copies.
This restricted bandwidth likely limits multi-card performance; a wider-link
comparison was not measured. See the [test topology](docs/HARDWARE.md).

**Model identities:** standard Qwen is **Qwen 3.8 27B**. **Orca is Qwen 3.8
27B abliterated**, using the separately pinned uncensored EXL3 checkpoint.
**Apex Flash 1 is Cantina Security and Yeta's reinforcement-learning post-train
of GLM 5.3 Flash** for security investigations; both Apex recipes use quantized
versions of its abliterated derivative.

"""
    native_id = 'deepseek-v41-flash-1017-dspark5-tp4'
    native = json.loads((REPO / 'profiles' / native_id / 'profile.json').read_text())
    native_link = f"[{MODEL_NAMES[native_id]}](profiles/{native_id}/README.md)"
    rows.insert(7, [native_link, 'EXL3 2.9 bpw artifact', 4, number(native['context']),
                    'Automatic; count not recorded', native['max_sessions']])
    raw += table(["Configuration", "Weight quantization", "Cards", "Context, tokens", "GPU KV, tokens / equiv.", "Slots"], rows)
    raw += """
Quantization describes the main weights. Apex EXL3's **4.37 effective bpw** is
calculated from its complete checkpoint, including MTP:
`175,642,473,288 bytes * 8 / 321,323,031,390 parameters = 4.37298 bpw`.
This includes quantization overhead, native tensors and file headers.
The main tensor payload excluding MTP also rounds to 4.37 bpw.
DeepSeek V4.1 Flash TP3's 2.0 bpw is the publisher's routed-expert declaration,
not a whole-model average. See the [quantization source](data/quantization-sources.json)
and each recipe's tensor-format details. KV precision is configured separately.

## Measured Performance

### Short-Output Comparisons

Cold-input measurements for eight configurations. C1 means one request per
model instance; a multi-card model is one instance. Prefill uses the backend's input-processing timer;
TTFT is client time to first token and includes queueing and other overhead.
Decode counts accepted output tokens inside the common generation interval,
excluding prefill. Each row uses matched C1/concurrent runs, not repetition means.
Wave request counts and rates are per model instance.

"""
    raw += table(["Recipe", "Input target / output budget, tokens/request", "C1 prefill, tok/s", "C1 TTFT, s",
                  "C1 decode, tok/s", "Wave requests", "Wave decode, tok/s total"], performance_rows)
    raw += comparison_notes()
    data = json.loads((REPO / 'data/deepseek-1017-20261026/results.json').read_text())
    raw += f"""
### DeepSeek V4.1 Flash 1017 TP4: Long Outputs

{native_link} uses five observations per input/output combination in one process,
with prefix reuse permitted. Generation excludes prefill and the first delivered
token block. These longer-output observations use different weights and a
different native runtime from TP3; they are not substituted into the cold,
short-output comparison above.

"""
    raw += table(['Input target, tokens', 'Output tokens', 'Median generation, tok/s', 'Observations'],
        [[number(r['input_target_tokens']), number(r['output_tokens']),
          number(r['generation_median_tokens_per_second']), r['observations']]
         for r in data['baseline']['primary_summary']])
    raw += """
Both four-request batches completed, at **51.84** and **49.91 aggregate output
tokens/s including prefill and scheduling**. Prefix reuse was permitted; the
mixed batch followed an individual near-full-context request. Thirty primary
observations, two individual long-input requests and eight concurrent requests
give 40 measured requests. The batched Engram candidate stalled twice and was
rejected; no qualifying speedup or candidate concurrency result was established.
The startup compatibility repair passed a fresh launch and four API/code checks;
the intermittent GPU fault remains unresolved. See the
[experiments and charts](docs/DEEPSEEK-1017.md) and
[data definitions](data/deepseek-1017-20261026/README.md).

"""
    raw += """
<details>
<summary>Measurement geometry and serving limits</summary>

Context, KV and configured slots describe the selected recipe. Orca's listed
speed waves used fixed MTP3; current serving uses adaptive MTP up to three.
MiMo's listed speed waves used a 262,144-token pool/context. Earlier Apex AWQ
waves used a 1,167,732-token capacity report at 262,144 context; earlier DeepSeek
waves preceded final automatic sizing and used 262,144 context. The new
selected-serving comparison uses 524,288 context for AWQ and DeepSeek, with
automatic KV sizing. These 32k speed requests do not requalify the larger
capacity reports. Each recipe labels its test geometry.

The context limit is per request. Tabby capacity is an explicitly allocated
shared token pool. Apex AWQ and DeepSeek capacity is vLLM's calculated
full-context token-equivalent report, not a literal resident-token count;
see [data definitions](docs/DATA.md#memory-and-context). The slot count does
not guarantee simultaneous maximum histories.
The selected text recipes use the checkpoints' native context limits; YaRN and
custom positional scaling are not configured.

</details>

## Start Here

1. Read [Hardware Requirements And Test Setup](docs/HARDWARE.md).
2. Prepare the matching [runtime and model assets](docs/REPRODUCING.md).
3. Open the configuration's README for its setup. Portable entries support `launch.sh --dry-run`; the native DeepSeek entry lists its runtime dependencies and configuration placeholders.
4. Select devices and listener settings, then follow that configuration's launch instructions. Portable [launch options](docs/REPRODUCING.md#launch-options) apply to the bundled launchers.

## Archived Alternatives

The [archive](archive/README.md) contains 81 archived model profiles,
additional experimental configurations and retained results. It includes
quantization, speculative-decoding, layout, cache-sizing and context alternatives,
with exact measurements, partial/failed outcomes and explicit evidence gaps.
Its catalog and CSVs document the broader search behind the selected configurations.
Browse the [timing waves](archive/history/RESULTS.md),
[bounded quality comparisons](archive/history/QUALITY.md), and
[all additional test results](archive/history/OBSERVATIONS.md) for the retained
measurements, original/revised grades, allocation checks and negative outcomes.

## Reproducibility

- [Benchmark methodology and limits](docs/BENCHMARKS.md)
- [Completion, chat and Responses interfaces](docs/API-COMPATIBILITY.md)
- [All numerical benchmark points](benchmarks.csv)
- [Detailed evidence and data definitions](docs/DATA.md)
- [Machine-readable catalog](catalog.json)
- [Model/runtime attribution and licenses](THIRD_PARTY.md)
- [Reuse and required attribution](LICENSE)
- [Contributing a recipe](CONTRIBUTING.md)

The original configurations were GPU-tested on the reference host. This
portable export is validated on CPU; it has not been GPU-qualified from a
fresh installation. Model weights, compiled binaries, credentials and raw
conversation logs are referenced or omitted rather than committed.

## License And Attribution

Original recipe documentation, metadata and benchmark data are **CC BY 4.0**.
When sharing or adapting them, credit **SourceHat**, link to this repository or
the relevant recipe, link to the license and identify your changes. For example:

> Based on SourceHat's [CMP 170HX Model Recipes](https://github.com/SourceHat/cmp-170hx-model-recipes), [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Modified by YOUR NAME.

Original standalone code is **Apache-2.0**; retain applicable notices, including
[NOTICE](NOTICE), when redistributing it. Upstream runtime code, patches and
model weights keep their own licenses. See [LICENSE](LICENSE) for the scope and
[THIRD_PARTY.md](THIRD_PARTY.md) for upstream attribution.
"""
    raw += (f"\n---\n\nThis work was performed and is released by **{publication['released_by']}**, "
            f"owner of the **{publication['brand']['name']}** brand.\n")
    (REPO / "README.md").write_text(display_names(raw))
    fields = ["recipe","measurement_id","cohort","headline_eligible","input_target_tokens","input_tokens_per_request","concurrency","cache_state","output_tokens_per_request",
              "decode_tok_s_aggregate","ttft_median_seconds","backend_prefill_tok_s_per_request_median",
              "decode_tok_s_per_request","shared_decode_interval_seconds","shared_decode_accepted_tokens","ttft_slowest_seconds",
              "draft_acceptance_ratio","draft_tokens_proposed","draft_tokens_accepted","cached_tokens_per_request",
              "end_to_end_accepted_tok_s","elapsed_seconds","transport","tested_kv_pool_tokens","test_configuration","measurement","cache_hit_verified","source"]
    with (REPO / "benchmarks.csv").open("w",newline="") as stream:
        writer = csv.DictWriter(stream,fieldnames=fields,extrasaction="ignore",lineterminator="\n")
        writer.writeheader()
        for r in csv_rows:
            writer.writerow({k:json.dumps(v) if isinstance(v,(list,dict)) else v for k,v in r.items()})
    print(f"Built {len(recipes)} recipe cards and {len(csv_rows)} benchmark points")


if __name__ == "__main__":
    main()
    serving_verification()
