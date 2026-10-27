"""Render the historical catalog and numerical exports from sanitized records."""
import csv
import json
from pathlib import Path

from build_docs import number, table
from history_evidence import NUMERIC_UNITS
from archive_indexes import (archive_documents, prefill_dataset, prefill_documents,
                             prefill_rows, qwen_replica_document, qwen_replica_rows)

STATUS = {
    "synchronized_decode_measured": "Decode interval measured",
    "partial_or_legacy_measurements": "Legacy / incomplete measurements",
    "summary_only_rates": "Rate summary only",
    "bounded_checks_only": "Bounded checks only",
    "job_history_only": "Job history; no matched benchmark",
    "definition_only": "Definition; no matched test receipt",
    "supplemental_results_only": "Additional test results; no matched decode wave",
}


def load_history(repo):
    root = repo / "archive/history"
    def read(name, key):
        return json.loads((root / name).read_text())[key]
    history = {
        "records": read("catalog.json", "records"),
        "configs": {r["configuration_id"]: r for r in read("configurations.json", "configurations")},
        "points": {r["measurement_id"]: r for r in read("measurements.json", "points")},
        "checks": {r["check_id"]: r for r in read("checks.json", "checks")},
        "summaries": {r["summary_id"]: r for r in read("rate-summaries.json", "summaries")},
        "observations": {r["result_id"]: r for r in read("observations.json", "observations")},
        "coverage": json.loads((root / "coverage.json").read_text()),
    }
    history["point_profiles"] = {identity: [record for record in history["records"]
                                            if identity in record["measurement_ids"]]
                                   for identity in history["points"]}
    return history


def distinct(values):
    return list(dict.fromkeys(value for value in values if value is not None))


def settings_for(point, history):
    configs = [history["configs"][key]["settings"] for key in point["configuration_ids"]]
    return configs or point.get("observed_instances", [])


def token_range(values):
    retained = [value for value in values if value is not None]
    if not retained:
        return "-"
    unique = sorted(set(retained))
    result = number(unique[0]) if len(unique) == 1 else f"{number(unique[0])} to {number(unique[-1])}"
    return result + (" (some missing)" if len(retained) != len(values) else "")


def profile_links(records, prefix):
    return "<br>".join(f"[{record['id']}]({prefix}{record['id']}.md)" for record in records)


def layout_draft(configs):
    return "<br>".join(distinct(
        f"{config.get('parallelism') or 'layout unspecified'}; {config.get('draft_mode') or 'draft unspecified'} / {number(config.get('draft_tokens'))}"
        for config in configs)) or "Unspecified"


def point_row(point, history, prefix="profiles/"):
    configs = settings_for(point, history)
    profiles = history["point_profiles"][point["measurement_id"]]
    label = profile_links(profiles, prefix) or "Configuration unresolved"
    geometry = number(distinct(config.get("context") for config in configs)) + " / " + number(distinct(config.get("cache_tokens") for config in configs))
    outputs = token_range(point["accepted_output_tokens_per_request"])
    budget = point.get("requested_output_tokens_per_request")
    if budget is not None:
        outputs += f" (budget {number(budget)})"
    requests = number(point["request_count"])
    if point.get("model_instance_count"):
        requests += f" ({point['model_instance_count']} instances; {number(point['requests_per_instance'])} each)"
    return [label + "<br>" + point["measurement_id"], layout_draft(configs),
            requests, token_range(point["input_tokens_per_request"]), outputs,
            point["cache_state"] + "; reused " + token_range(point["cached_input_tokens_per_request"]), geometry,
            number(point["decode_tok_s_aggregate"]), number(point.get("reported_after_first_token_tok_s_estimate")),
            number(point["end_to_end_accepted_tok_s"]),
            number(point["ttft_median_seconds"]),
            "Pass" if point["report_passed"] is True else "Failed / partial" if point["report_passed"] is False else "Unspecified"]


RESULT_HEADERS = ["Profile / Wave", "Layout; Draft / Tokens", "Requests", "Input tokens/request",
                  "Accepted output tokens/request", "Cache / Reused input tokens", "Context / GPU pool tokens",
                  "Shared decode tok/s total", "Client after-first-token estimate tok/s", "Whole-wave output tok/s", "Median TTFT, s", "Source report"]


def profile_page(record, history):
    raw = f"# {record['id']}\n\n"
    raw += f"**Historical record. {STATUS[record['measurement_status']]}.**\n\n"
    raw += f"Model family: {record['family']}.\n\n"
    if record["recorded_experiment_status"]:
        raw += f"The campaign inventory recorded status `{record['recorded_experiment_status']}`. The evidence sections retain any later results separately.\n\n"
    if record["archive_reason"]:
        raw += "Recorded archive reason: " + record["archive_reason"] + "\n\n"
    raw += "Historical configurations are provided for comparison. The [recommended recipes](../../../README.md) include supported launch scripts.\n\n"
    if record["related_recommended_recipes"]:
        raw += "Current recipes using the same recorded checkpoint repository: " + ", ".join(
            f"[{name}](../../../recipes/{name}/README.md)" for name in record["related_recommended_recipes"]) + ". Context, cache and runtime versions can differ.\n\n"
    raw += "## Saved Configuration Versions\n\n"
    if not record["configuration_ids"]:
        raw += "No exact serving configuration is retained with this summary. Its values are not assigned to another profile.\n\n"
    else:
        raw += "Each configuration ID identifies a distinct original settings record. Deployment fields are omitted; versions can have identical published settings after that omission. Upstream runtime commits remain unspecified where the source retained only an integration label.\n\n"
        rows = []
        for identity in record["configuration_ids"]:
            config = history["configs"][identity]
            settings = config["settings"]
            model = settings.get("model_repository")
            revision = settings.get("model_revision")
            if model and revision:
                artifact = f"[{model}@{revision[:10]}](https://huggingface.co/{model}/tree/{revision})"
            else:
                artifact = model or settings.get("served_model_label") or "Identity not retained"
            if settings.get("derived_model_view_used"):
                artifact += " (derived view)"
            rows.append([identity, artifact, number(settings.get("gpu_counts")),
                         number(settings.get("context")), number(settings.get("cache_tokens")),
                         number(settings.get("max_sessions")),
                         str(settings.get("draft_mode") or "unspecified") + " / " + number(settings.get("draft_tokens"))])
        raw += table(["Configuration", "Recorded artifact / source", "Configured card counts",
                      "Context tokens", "GPU pool tokens", "Slots", "Draft mode / tokens"], rows) + "\n"
        raw += "Card counts are saved configuration choices, not a claim that every allowed placement was measured. A derived view can differ from its pinned download source.\n\n"
        for identity in record["configuration_ids"]:
            config = history["configs"][identity]
            raw += f"<details>\n<summary>{identity}</summary>\n\n"
            raw += "```json\n" + json.dumps(config["settings"], indent=2) + "\n```\n\n"
            raw += "Pinned model revision recorded: " + ("yes" if config["artifact_pin_recorded"] else "no") + ". "
            if config.get("runtime_observation_only"):
                raw += "This is a runtime observation with incomplete artifact identity. "
            raw += "Source receipt labels, hashes and object locators are retained in [configurations.json](../configurations.json).\n\n</details>\n\n"
    raw += "## Retained Measurements\n\n"
    points = [history["points"][key] for key in record["measurement_ids"]]
    if points:
        raw += table(RESULT_HEADERS, [point_row(point, history, prefix="") for point in points]) + "\n"
        raw += "Rates are whole-wave totals over the stated request count. A wave may span multiple independent model instances; [measurements.json](../measurements.json) retains their contributions and the exact configuration IDs. Do not interpret a multi-instance total as one card's rate.\n\n"
    else:
        raw += "No detailed benchmark receipt is matched to this record. A saved definition or a successful job exit alone is not a performance measurement.\n\n"
    raw += "A dash in shared decode means no qualified synchronized interval is available. Whole-wave throughput includes prefill and queueing. A valid decode interval can survive inside an overall failed or partial check; the source-report outcome is preserved. No rows are averaged.\n\n"
    if record["rate_summary_ids"]:
        raw += "## Reported Rate Summaries\n\n"
        rows = []
        for identity in record["rate_summary_ids"]:
            row = history["summaries"][identity]
            rows.append([identity, row["reported_field"], number(row["reported_tok_s"]),
                         number(row["request_count"]), row["configuration_binding"]])
        raw += table(["Summary", "Original field", "Reported tok/s", "Requests", "Configuration binding"], rows) + "\n"
        raw += "These quoted values can overlap detailed waves. A referenced earlier run's rate is not transferred to the citing configuration. Missing input, request and timing-window evidence remains missing. See [rate-summaries.json](../rate-summaries.json).\n\n"
    if record["check_ids"]:
        raw += "## Bounded Checks\n\n"
        rows = []
        for identity in record["check_ids"]:
            check = history["checks"][identity]
            rows.append([identity, "Pass" if check["passed"] else "Failed / partial",
                         json.dumps(check["reported_numeric_fields"], separators=(",", ":"))])
        raw += table(["Check", "Reported outcome", "Retained counts / flags"], rows) + "\n"
        raw += "These checks retain their reported scope. A context/allocation/retrieval check is not a general quality score or a speed qualification at that context. Exact flags and provenance are in [checks.json](../checks.json).\n\n"
    if record.get("observation_ids"):
        raw += "## Additional Test Results\n\n"
        observations = [history["observations"][identity] for identity in record["observation_ids"]]
        raw += table(OBSERVATION_HEADERS, [observation_row(row, history, "../", "") for row in observations]) + "\n"
        raw += "These are saved result records, including failures and bounded checks. Copies, individual requests, report summaries and regrading can overlap; their counts are not independent test repetitions. Open each result for exact values, units, configuration binding and source receipts.\n\n"
    if record["recorded_jobs"]:
        raw += f"There are {len(record['recorded_jobs'])} retained lifecycle records. Their states, exit codes and configuration IDs remain in [catalog.json](../catalog.json); they do not supply missing benchmark results.\n\n"
    raw += "[Full archive](../../README.md) | [All retained waves](../RESULTS.md) | [Data definitions](../DATA.md) | [Recommended recipes](../../../README.md)\n"
    return raw


def csv_value(value):
    if value is None:
        return ""
    return json.dumps(value, separators=(",", ":")) if not isinstance(value, str) else value


def write_csv(path, rows):
    fields = list(dict.fromkeys(key for row in rows for key in row))
    with path.open("w", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=fields, lineterminator="\n")
        writer.writeheader()
        for row in rows:
            writer.writerow({key: csv_value(value) for key, value in row.items()})


def benchmark_csv_rows(history):
    rows = []
    for point in history["points"].values():
        configs = settings_for(point, history)
        row = {key: value for key, value in point.items() if key not in {"requests", "sources", "raw_unqualified_observation"}}
        row.update(model_repositories=distinct(cfg.get("model_repository") for cfg in configs),
                   historical_profile_ids=[record["id"] for record in history["point_profiles"][point["measurement_id"]]],
                   configured_parallelism=distinct(cfg.get("parallelism") for cfg in configs),
                   configured_draft_modes=distinct(cfg.get("draft_mode") for cfg in configs),
                   configured_draft_tokens=distinct(cfg.get("draft_tokens") for cfg in configs),
                   model_revisions=distinct(cfg.get("model_revision") for cfg in configs),
                   configured_context_tokens=distinct(cfg.get("context") for cfg in configs),
                   configured_gpu_pool_tokens=distinct(cfg.get("cache_tokens") for cfg in configs),
                   sources=point["sources"], raw_unqualified_observation=point["raw_unqualified_observation"])
        rows.append(row)
    return rows


OBSERVATION_HEADERS = ["Result / Source", "Profile", "Evidence type", "Reported outcome", "Retained values", "Configuration binding"]


def observation_outcome(row):
    metrics = row["metrics"]
    if row["kind"] in {"quality_evaluation", "quoted_quality_score"}:
        return f"{metrics['passed']} / {metrics['total']} tasks passed"
    passed = metrics.get("flags", {}).get("passed")
    if type(passed) is bool:
        return "Pass" if passed else "Failed / partial"
    return metrics.get("reported_status") or metrics.get("reported_outcome") or metrics.get("reported_result") or ("Error recorded" if metrics.get("error_present") else "Outcome unspecified")


def observation_values(row):
    metrics = row["metrics"]
    if row["kind"] in {"quality_evaluation", "quoted_quality_score"}:
        categories = [f"{key}: {value['passed']} / {value['total'] if value['total'] is not None else '?'}"
                      for key, value in metrics["categories"].items()]
        if "task_total_latency_seconds" in metrics:
            times = metrics["task_total_latency_seconds"]
            categories.append(f"Task latency median {number(times['median'])} s; n={times['count']}")
        return "; ".join(categories) or "Aggregate score only"
    values = [f"{key}={number(value)} {NUMERIC_UNITS[key]}" for key, value in metrics.get("values", {}).items()]
    if metrics.get("reported_error_type"):
        values.append("Reported error type: " + metrics["reported_error_type"])
    if metrics.get("inter_token_latency"):
        values.extend(f"{key}={number(value)} ms" for key, value in metrics["inter_token_latency"].items())
    for key in ("cold_prefill", "prefill"):
        if metrics.get(key):
            rates = [value.get("prefill_tok_s") for value in metrics[key]]
            values.append(f"{key}: per-request {token_range(rates)} tokens/s")
    if metrics.get("draft_acceptance"):
        draft = metrics["draft_acceptance"]
        values.append(f"Draft accepted / proposed: {number(draft.get('accepted'))} / {number(draft.get('proposed'))} tokens; fraction {number(draft.get('ratio'), 4)}")
    if metrics.get("request_batches"):
        values.extend(f"{key}: {len(batch)} requests" for key, batch in metrics["request_batches"].items())
    if metrics.get("response_metrics"):
        values.append(f"{len(metrics['response_metrics'])} response usage/timing records")
    for key in ("long_and_small_requests",):
        if metrics.get(key):
            values.append(f"{len(metrics[key])} mixed-length request records")
    if metrics.get("cache_bytes"):
        values.extend(f"{key} KV={number(value)} bytes" for key, value in metrics["cache_bytes"].items())
    for key in ("per_card_peak_used_MiB_unordered", "allocator_reserved_GiB", "free_GiB", "peak_total_GiB"):
        if key in metrics:
            values.append(f"{key}={number(metrics[key])}")
    if metrics.get("reported_aggregates"):
        values.extend(f"{key}={number(value, 6)} {metrics['units'][key]}"
                      for key, value in metrics["reported_aggregates"].items() if type(value) is not bool)
    false_flags = [key + "=false" for key, value in metrics.get("flags", {}).items() if value is False and key != "passed"]
    values.extend(false_flags)
    if not values:
        values.extend(key + "=" + str(value).lower() for key, value in metrics.get("flags", {}).items())
    return "; ".join(values) or "See exact JSON for retained flags and timers"


def observation_row(row, history, data_prefix="", profiles_prefix="profiles/"):
    profiles = {record["id"]: record for record in history["records"]}
    source = row["sources"][0]
    records = [profiles[identity] for identity in distinct(row["profile_ids"] + row["associated_profile_ids"])]
    location = source.get("json_pointer") or source.get("source_location_id") or "/"
    label = f"[{row['result_id']}]({data_prefix}observations.json)<br>{source['file']}<br>`{location}`"
    return [label, profile_links(records, profiles_prefix) or "Unresolved",
            row["kind"].replace("_", " "), observation_outcome(row), observation_values(row),
            "Recorded configuration/job" if row["configuration_ids"] else "Exact configuration unresolved"]


def observation_csv_rows(history):
    profiles = {record["id"]: record for record in history["records"]}
    rows = []
    for row in history["observations"].values():
        settings = [history["configs"][identity]["settings"] for identity in row["configuration_ids"]]
        rows.append(dict(row, reported_outcome=observation_outcome(row),
                         model_families=distinct(profiles[identity]["family"] for identity in row["profile_ids"]),
                         model_repositories=distinct(cfg.get("model_repository") for cfg in settings)))
    return rows


def observation_documents(history):
    documents = {}
    kinds = distinct(row["kind"] for row in history["observations"].values())
    index = """# Additional Retained Test Results

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

"""
    index += table(["Result category", "Retained records"], [
        [f"[{kind.replace('_', ' ').title()}](observations/{kind}.md)",
         sum(row["kind"] == kind for row in history["observations"].values())] for kind in kinds])
    index += "\n[Exact JSON](observations.json) | [CSV](observations.csv) | [Quality comparison](QUALITY.md) | [Definitions](DATA.md) | [Archive](../README.md)\n"
    documents["OBSERVATIONS.md"] = index
    for kind in kinds:
        rows = [row for row in history["observations"].values() if row["kind"] == kind]
        raw = f"# {kind.replace('_', ' ').title()}\n\n"
        raw += "Each row is a retained source observation. Repeated summaries and related requests can overlap other archive evidence. Exact values and source receipts are in the [JSON](../observations.json); the [definitions](../DATA.md) describe units and limitations.\n\n"
        raw += table(OBSERVATION_HEADERS, [observation_row(row, history, "../", "../profiles/") for row in rows])
        raw += "\n[All result categories](../OBSERVATIONS.md) | [Exact CSV](../observations.csv) | [Archive](../../README.md)\n"
        documents[f"observations/{kind}.md"] = raw
    quality = """# Bounded Quality And Correctness Scores

These small task sets evaluate the recorded checkpoints and serving stacks.
They do not isolate quantization quality or establish a broad coding,
cybersecurity or reasoning benchmark. Different task sets and grading revisions
remain separate, and raw tasks and generated responses are excluded.

The retained Apex checkpoint comparison reports **25/32 for EXL3** and
**27/32 for AWQ**. It changes both checkpoint/backend combinations; the two-task
difference cannot be attributed to quantization alone. The source records one
bounded incomplete answer. The eight-task follow-ups use a different task set.

For the eight-task Orca follow-ups, original scoring reports **6/8** for both
native and extended-context configurations. A later grading pass on the same
responses reports **7/8** for each, accepting both permitted representations of
one action. Both grades are preserved; they are not independent model runs.
The extended-context result does not change the current native-context recipe.

The mathematical-overlay experiment records **22/32** for each of base,
original and expanded arms. Its saved grades demonstrate no task-score gain.
The exact local overlay is not reconstructed or assigned to another artifact.

All ratios below are tasks passed / tasks evaluated. Categories retain their
own denominators. Latency is the median total client time over the stated
saved task requests, not decode throughput. Missing denominators remain `?`.

"""
    rows = [row for row in history["observations"].values() if row["kind"] == "quality_evaluation"]
    quality += table(OBSERVATION_HEADERS, [observation_row(row, history) for row in rows])
    quality += "\nQuoted score summaries without the task records are [listed separately](observations/quoted_quality_score.md). Correctness gates, including failed checks and greedy-reference comparisons, are [separate bounded evidence](observations/correctness_check.md).\n\n[Exact JSON](observations.json) | [CSV](observations.csv) | [All results](OBSERVATIONS.md) | [Archive](../README.md)\n"
    documents["QUALITY.md"] = quality
    return documents


def build_history_docs(repo):
    history = load_history(repo)
    root = repo / "archive/history"
    profiles_dir = root / "profiles"
    profiles_dir.mkdir(exist_ok=True)
    expected = {record["id"] + ".md" for record in history["records"]}
    for path in profiles_dir.glob("*.md"):
        if path.name not in expected:
            path.unlink()
    for record in history["records"]:
        (profiles_dir / (record["id"] + ".md")).write_text(profile_page(record, history))
    for filename, content in archive_documents(history, STATUS).items():
        path = repo / "archive" / filename
        path.parent.mkdir(exist_ok=True)
        path.write_text(content)
    for filename, content in prefill_documents(history).items():
        path = root / filename
        path.parent.mkdir(exist_ok=True)
        path.write_text(content)
    (root / "prefill.json").write_text(json.dumps(prefill_dataset(history), indent=2) + "\n")
    write_csv(root / "prefill.csv", prefill_rows(history))
    qwen = repo / "archive/qwen3.8-27b-replicas"
    qwen.mkdir(exist_ok=True)
    (qwen / "README.md").write_text(qwen_replica_document(repo))
    write_csv(qwen / "benchmarks.csv", qwen_replica_rows(repo))
    requests = json.loads((repo / "recipes/qwen3.8-27b-exl3/historical-replica-requests.json").read_text())["requests"]
    write_csv(qwen / "requests.csv", requests)
    raw = """# All Retained Measurement Waves

Each row is a saved wave, not an average. Request count is the total for the
wave; multiple independent model instances can contribute to that total.
Configuration IDs and per-instance contributions are in the JSON. Values from
an overall failed/partial check retain that report outcome.

Shared decode uses a synchronized accepted-token interval and excludes prefill.
Whole-wave throughput includes prefill and queueing. `Not recorded` marks unavailable evidence;
older after-first-token estimates are separate fields in the downloadable data.
Quoted summaries are [separate](rate-summaries.json) and must not be pooled with
these waves. The [main recipe CSV](../../benchmarks.csv) can overlap this history;
combining the files does not create new repetitions.

"""
    for kind in distinct(point["measurement_kind"] for point in history["points"].values()):
        points = [point for point in history["points"].values() if point["measurement_kind"] == kind]
        raw += f"## {kind.replace('_', ' ').title()}\n\n"
        if kind == "client_estimated_decode_wave":
            raw += "These long-output runs have client stream timing and an estimated first batch. Their retained estimates stay in a separate field in the JSON/CSV; shared decode is unavailable.\n\n"
        raw += table(RESULT_HEADERS, [point_row(point, history) for point in points]) + "\n"
    raw += "[Exact JSON](measurements.json) | [CSV](benchmarks.csv) | [Definitions](DATA.md) | [Archive](../README.md)\n"
    (root / "RESULTS.md").write_text(raw)
    write_csv(root / "benchmarks.csv", benchmark_csv_rows(history))
    write_csv(root / "profiles.csv", history["records"])
    write_csv(root / "rate-summaries.csv", list(history["summaries"].values()))
    write_csv(root / "observations.csv", observation_csv_rows(history))
    for filename, content in observation_documents(history).items():
        path = root / filename
        path.parent.mkdir(exist_ok=True)
        path.write_text(content)
