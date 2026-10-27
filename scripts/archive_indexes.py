"""Build archive navigation and prefill views without changing source records."""
import json
import re

from build_docs import number, table


def family_slug(family):
    names = {
        "Apex Flash 1 (GLM 5.3 Flash post-train)": "apex-flash-1",
        "Orca (Qwen 3.8 27B abliterated)": "orca",
    }
    return names.get(family, re.sub(r"[^a-z0-9.]+", "-", family.lower()).strip("-."))


def record_rows(records, status, prefix="history/profiles/"):
    return [[f"[{row['id']}]({prefix}{row['id']}.md)", status[row["measurement_status"]],
             len(row["configuration_ids"]), len(row["measurement_ids"]),
             len(row["check_ids"]), len(row.get("observation_ids", []))] for row in records]


RECORD_HEADERS = ["Profile / experiment", "Evidence", "Versions", "Waves", "Checks", "Other results"]


def archive_documents(history, status):
    records, coverage = history["records"], history["coverage"]
    archived_ids = set(coverage["archived_profile_ids"])
    families = sorted({row["family"] for row in records})
    documents = {}
    raw = f"""# Archived Profiles And Experiments

**{coverage['archived_profile_count']} archived model profiles**, with saved settings,
measurements and selection evidence. Additional experiments cover quantization,
speculative decoding, layouts, cache sizing and context limits.

## Browse

| Start with | Contents |
| --- | --- |
| [Archived profiles](PROFILES.md) | All {coverage['archived_profile_count']} profiles, grouped by model family |
| [Additional experiments](EXPERIMENTS.md) | Experimental configurations and source result records |
| [Decode and latency](history/RESULTS.md) | Every retained wave, with request counts and timing scope |
| [Prefill](history/PREFILL.md) | Backend input-processing rates, processed/cached tokens and exact timers |
| [Quality and correctness](history/QUALITY.md) | Bounded scores, category denominators and original/revised grades |
| [Other test results](history/OBSERVATIONS.md) | Context, allocation, cache, correctness and failed outcomes |
| [Qwen 3.8 27B replicas](qwen3.8-27b-replicas/README.md) | Three one-card instances at one or sixteen requests each |
| [Strata comparisons](STRATA.md) | One-card IQ4 and two-card Q6, with native server templates |
| [Historical RAM page tier](ram-prefix-tier/README.md) | Earlier capacity arithmetic and reuse counters; disabled in selected recipes |

## By Model Family

"""
    family_rows = []
    for family in families:
        group = [row for row in records if row["family"] == family]
        archived = [row for row in group if row["id"] in archived_ids]
        family_rows.append([f"[{family}](models/{family_slug(family)}.md)", len(archived),
                            len(group) - len(archived),
                            len({identity for row in group for identity in row["measurement_ids"]})])
    raw += table(["Family", "Archived profiles", "Other records", "Linked waves"], family_rows)
    raw += f"""
## Evidence And Downloads

The inventory retains **{coverage['historical_records']} historical records**,
**{coverage['configuration_snapshots']} configuration snapshots** and
**{coverage['unique_measurement_waves']} measurement waves**. Of those waves,
**{coverage['synchronized_decode_waves']} have a valid synchronized decode interval**.
There are also {coverage['bounded_check_records']} bounded checks,
{coverage['reported_rate_summaries']} quoted rate summaries and
{number(coverage['supplemental_result_records'])} additional numeric/functional observations.
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

"""
    raw += table(["Status", "Historical records"], [
        [status[key], value] for key, value in coverage["profile_measurement_status_counts"].items()])
    raw += """
`Definition` and `job history` entries preserve an evidence gap; they do not
claim that a model was never tested. Configured context and allocated cache
do not establish speed or concurrency at those limits. Different artifacts,
settings and timing methods remain separate, including failed and partial runs.

</details>

Historical records are comparison evidence. The [eight recommended recipes](../README.md)
provide the supported launch scripts; archival templates require their stated
runtime integration and have not been newly GPU-qualified from this export.

[Recommended recipes](../README.md) | [Attribution and licenses](../LICENSE)
"""
    documents["README.md"] = raw
    for filename, title, want_archived in (("PROFILES.md", f"{len(archived_ids)} Archived Profiles", True),
                                           ("EXPERIMENTS.md", "Additional Experiments And Results", False)):
        selected = [row for row in records if (row["id"] in archived_ids) == want_archived]
        raw = f"# {title}\n\n"
        raw += ("Open a record for exact configuration versions, artifact pins, all matched "
                "measurements and evidence gaps. Counts describe linked records and can overlap.\n\n")
        raw += "[Archive](README.md) | [Prefill](history/PREFILL.md) | [All waves](history/RESULTS.md) | [Exact catalog](history/catalog.json)\n\n"
        for family in families:
            group = [row for row in selected if row["family"] == family]
            if not group:
                continue
            raw += f"## {family}\n\n[All family records](models/{family_slug(family)}.md).\n\n"
            raw += table(RECORD_HEADERS, record_rows(group, status)) + "\n"
        documents[filename] = raw.rstrip() + "\n"
    for family in families:
        group = [row for row in records if row["family"] == family]
        raw = f"# {family}\n\n"
        raw += "[Archive](../README.md) | [All archived profiles](../PROFILES.md) | [Additional experiments](../EXPERIMENTS.md)\n\n"
        related = sorted({identity for row in group for identity in row["related_recommended_recipes"]})
        if related:
            raw += "Recommended recipes with the same recorded checkpoint repository: " + ", ".join(
                f"[{identity}](../../recipes/{identity}/README.md)" for identity in related) + ".\n\n"
        raw += ("Open each record for its settings, layout, draft, context/cache geometry and "
                "exact measurements. Versions can differ in artifact or runtime identity. "
                "A linked result is not transferred to another configuration.\n\n")
        if family == "Qwen 3.8 27B":
            raw += "The [three-replica comparison](../qwen3.8-27b-replicas/README.md) explains the separate synchronized-decode and older client-timed cohorts.\n\n"
        if family == "Qwen 3.8 Flash Next":
            raw += "The [Strata comparison](../STRATA.md) includes additional engine templates and allocation evidence.\n\n"
        for title, want_archived in (("Archived Profiles", True), ("Additional Experiments And Results", False)):
            selected = [row for row in group if (row["id"] in archived_ids) == want_archived]
            if selected:
                raw += f"## {title}\n\n" + table(RECORD_HEADERS, record_rows(selected, status, "../history/profiles/")) + "\n"
        raw += "[Prefill](../history/PREFILL.md) | [Quality](../history/QUALITY.md) | [All waves](../history/RESULTS.md) | [Data definitions](../history/DATA.md)\n"
        documents[f"models/{family_slug(family)}.md"] = raw
    return documents


def prefill_rows(history):
    rows = []
    for observation in history["observations"].values():
        for field in ("cold_prefill", "prefill"):
            entries = observation["metrics"].get(field, [])
            for index, values in enumerate(entries):
                rows.append({
                    "result_id": observation["result_id"], "source_field": field,
                    "entry_index": index, "entries_in_source_array": len(entries),
                    "configuration_ids": observation["configuration_ids"],
                    "profile_ids": observation["profile_ids"],
                    "associated_profile_ids": observation["associated_profile_ids"],
                    "configuration_binding": observation["configuration_binding"],
                    "reported_passed": observation["metrics"].get("flags", {}).get("passed"),
                    **values, "sources": observation["sources"],
                })
    return rows


def prefill_dataset(history):
    rows = prefill_rows(history)
    return {
        "format_version": 1,
        "scope": "View of the retained observations.json prefill arrays; these are overlapping source entries, not new measurements or independent repetitions.",
        "units": {"processed_prompt_tokens": "tokens", "cached_prompt_tokens": "tokens",
                  "backend_prefill_seconds": "s", "prefill_tok_s": "tokens/s"},
        "rate_definition": "Source-reported processed_prompt_tokens / backend_prefill_seconds. No TTFT substitution, pooled average or aggregate prefill throughput is calculated.",
        "source_array_count": len({(row["result_id"], row["source_field"]) for row in rows}),
        "entry_count": len(rows), "entries": rows,
    }


def prefill_families(row, history):
    profiles = {record["id"]: record for record in history["records"]}
    identities = row["profile_ids"] or row["associated_profile_ids"]
    return sorted({profiles[identity]["family"] for identity in identities}) or ["Unresolved model identity"]


def value_span(values):
    values = [value for value in values if value is not None]
    if not values:
        return "-"
    return number(values[0]) if min(values) == max(values) else f"{number(min(values))} to {number(max(values))}"


def prefill_documents(history):
    rows = prefill_rows(history)
    families = sorted({family for row in rows for family in prefill_families(row, history)})
    documents = {}
    raw = """# Backend Prefill Measurements

Prefill processes input before decoding. These are the saved backend timers
and per-request rates, kept with processed and cached prompt-token counts.
They complement [decode / client latency](RESULTS.md) and are not derived from TTFT.

The JSON and CSV are a view of `observations.json`, not additional experiments.
`cold_prefill` and `prefill` preserve the source field names. Cached-token counts,
rather than the field name alone, show how much input was reused. Report
summaries, individual requests and recipe data can overlap; do not pool them.
No aggregate prefill throughput is inferred by summing per-request rates.

"""
    arrays = {(row["result_id"], row["source_field"]) for row in rows}
    raw += f"**{len(rows)} saved entries from {len(arrays)} source arrays.** The [exact JSON](prefill.json) and [CSV](prefill.csv) retain every entry, its array index, configuration binding and source receipts.\n\n"
    raw += "## Browse By Model Family\n\n"
    summary = []
    for family in families:
        selected = [row for row in rows if family in prefill_families(row, history)]
        summary.append([f"[{family}](prefill/{family_slug(family)}.md)",
                        len({(row["result_id"], row["source_field"]) for row in selected}), len(selected)])
    raw += table(["Family", "Source arrays", "Saved entries"], summary)
    raw += """
Family association is navigation, not proof of an exact configuration; unbound
records remain unbound. A shared result can appear on more than one family page.
Missing backend timers stay unavailable. Source rates use processed tokens
divided by backend prefill seconds, whose recorded precision can differ from
client timers. Warm reuse processes only the uncached suffix; its rate does
not measure cold input processing over the full prompt.

The [recommended recipes](../../README.md#measured-performance) have a separate
matched 32k cold C1 comparison. Their JSON retains all concurrent prefill arrays.
This historical index spans other input lengths and settings; it is not a
ranked model comparison. The [Qwen replica timings](../qwen3.8-27b-replicas/README.md)
include the original backend timers from the same source reports as its
four decode waves. The displayed short-output AWQ and DeepSeek rows lack native
timers. Separate [AWQ long-output snapshots](../../docs/RECOVERED-PREFILL.md)
retain four native prefill observations, kept with their original workloads.

[Archive](../README.md) | [Definitions](DATA.md) | [All result categories](OBSERVATIONS.md) | [Sources](result-sources.json)
"""
    documents["PREFILL.md"] = raw
    for family in families:
        selected = [row for row in rows if family in prefill_families(row, history)]
        grouped = {}
        for row in selected:
            grouped.setdefault((row["result_id"], row["source_field"]), []).append(row)
        raw = f"# {family}: Prefill\n\n"
        raw += ("Each row summarizes one retained source array. Ranges are its minimum and maximum "
                "per-request values, not uncertainty intervals or repetition averages. "
                "The exact entries and provenance remain in [prefill.json](../prefill.json) and "
                "[prefill.csv](../prefill.csv). Arrays and enclosing reports can overlap.\n\n")
        output = []
        for (identity, field), group in grouped.items():
            row = group[0]
            profiles = list(dict.fromkeys(row["profile_ids"] + row["associated_profile_ids"]))
            links = "<br>".join(f"[{name}](../profiles/{name}.md)" for name in profiles) or "Unresolved"
            outcome = "Pass" if row["reported_passed"] is True else "Failed / partial" if row["reported_passed"] is False else "Unspecified"
            output.append([f"{identity}<br>`{field}`<br>{links}", len(group),
                           value_span([item.get("processed_prompt_tokens") for item in group]),
                           value_span([item.get("cached_prompt_tokens") for item in group]),
                           value_span([item.get("backend_prefill_seconds") for item in group]),
                           value_span([item.get("prefill_tok_s") for item in group]), outcome,
                           "<br>".join(row["configuration_ids"]) or "Unresolved"])
        raw += table(["Result / source field / profile", "Entries", "Processed tokens/request",
                      "Cached tokens/request", "Backend prefill, s/request", "Prefill, tok/s/request",
                      "Report outcome", "Configuration IDs"], output)
        raw += "\n[Prefill index](../PREFILL.md) | [Archive](../../README.md) | [Model families](../../README.md#by-model-family)\n"
        documents[f"prefill/{family_slug(family)}.md"] = raw
    return documents


def qwen_replica_rows(repo):
    result = json.loads((repo / "recipes/qwen3.8-27b-exl3/historical-replica-result.json").read_text())
    rows = []
    for mode, waves in result["measurements"].items():
        for cache, wave in waves.items():
            rows.append({
                "mode": mode, "source_wave": cache, "replicas": result["replicas"],
                "requests_per_replica": wave["per_card"][0]["requests"],
                "total_requests": sum(card["requests"] for card in wave["per_card"]),
                "input_range_tokens": result["input_range_tokens"],
                "output_budget_tokens_per_request": result["output_tokens_per_request"],
                "shared_decode_interval_seconds": wave["window_seconds"],
                "accepted_tokens_in_shared_interval": wave["generated_tokens"],
                "decode_tok_s_total": wave["aggregate_generation_tps"],
                "decode_tok_s_per_replica": [card["generation_tps"] for card in wave["per_card"]],
                "request_timing_by_replica": wave["request_timing_by_replica"],
                "source": result["source"],
            })
    return rows


def qwen_replica_document(repo):
    rows = qwen_replica_rows(repo)
    raw = """# Qwen 3.8 27B: Historical Replica Benchmarks

Three independent one-card instances of **Qwen 3.8 27B, EXL3 6 bpw**, with
MTP1, Q8 KV, a 917,504-token pool and 16 configured slots per instance.
Each request uses 2,048-8,192 input tokens and a 1,024-token output budget.
These are standard Qwen weights; Orca is a separate abliterated checkpoint.

The [recommended recipe](../../recipes/qwen3.8-27b-exl3/README.md) currently
configures eight slots. This historical test measured one and sixteen requests
per instance, not eight. The individual instance contributions were measured
simultaneously; they are not isolated one-card runs or repetition averages.

## Synchronized Decode Results

"""
    raw += table(["Replicas", "Requests/replica", "Total wave requests", "Source wave",
                  "Shared decode, tok/s total", "Shared decode/replica, tok/s",
                  "Shared interval, s", "Accepted tokens in interval"], [
        [row["replicas"], row["requests_per_replica"], row["total_requests"], row["source_wave"],
         number(row["decode_tok_s_total"]), number(row["decode_tok_s_per_replica"]),
         number(row["shared_decode_interval_seconds"]), number(row["accepted_tokens_in_shared_interval"])]
        for row in rows])
    raw += """
Each row is one wave. Shared decode counts accepted tokens after the last
request's first-generation event and before the first completion, excluding
prefill. The replica contributions sum to the total. The `cold` / `warm`
source labels are retained. Cached-token counts in the per-request timing
records establish reuse independently of those labels.

[Exact CSV](benchmarks.csv) is a view of the unchanged
[canonical JSON](../../recipes/qwen3.8-27b-exl3/historical-replica-result.json),
not four additional runs. It preserves the source receipt label, SHA256
and pointer. Sampling settings missing from that receipt remain unspecified.

## Prefill And First-Token Latency

All 102 requests from the same source reports are retained in
[per-request JSON](../../recipes/qwen3.8-27b-exl3/historical-replica-requests.json)
and [CSV](requests.csv). The source `prompt_n` already counts processed tokens;
cached tokens are separate. Backend prefill uses `prompt_n / (prompt_ms / 1000)`.
Client TTFT includes queueing and other overhead. The main README uses the
median observed per-replica value, not an average of the C48 wave.
The separate [32k MTP1 retention check](../../docs/QWEN-32K-EVIDENCE.md) uses C2
and does not supply the current C1/C8 benchmark.

## Separate Legacy C48 Results

The [older C48 record](../history/profiles/qwen3.8-27b-three-instances-mtp1-c48-legacy.md)
retains 256-output-token requests and client timing, including all 96 request
records across cold and warm waves. Its wall-time throughput and
after-first-token estimates are separate metrics; it has no qualified
synchronized backend interval. It is not combined with the 1,024-token waves
above.

Native-context checks and RAM-restoration evidence remain on the
[recipe page](../../recipes/qwen3.8-27b-exl3/README.md#verification).
They are bounded checks, not speed measurements at the context limit.

[All Qwen 3.8 27B records](../models/qwen-3.8-27b.md) | [Prefill](../history/PREFILL.md) | [Archive](../README.md) | [Data definitions](../history/DATA.md)
"""
    return raw
