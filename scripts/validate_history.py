"""Check historical coverage, numerical accounting, provenance and generated exports."""
import csv
import hashlib
import json
import math
from pathlib import Path
import re
import statistics
from collections import Counter

from history_docs import (benchmark_csv_rows, csv_value, load_history, observation_csv_rows,
                          observation_documents, profile_page, STATUS)
from archive_indexes import (archive_documents, prefill_dataset, prefill_documents,
                             prefill_rows, qwen_replica_document, qwen_replica_rows)
from history_evidence import CATEGORIES, FLAGS, NUMERIC_UNITS, finite_number


def require(condition, message):
    if not condition:
        raise ValueError("History: " + message)


def receipt(origin, sources):
    require(Path(origin["file"]).name == origin["file"]
            and re.fullmatch(r"source-[0-9a-f]{24}(?:\.[A-Za-z0-9]+)?", origin["file"])
            and re.fullmatch(r"[0-9a-f]{64}", origin["sha256"])
            and (origin["file"], origin["sha256"]) in sources,
            "invalid or unlisted source receipt")
    pointer = origin.get("json_pointer")
    location = origin.get("source_location_id")
    require((isinstance(pointer, str) and location is None)
            or (pointer is None and isinstance(location, str) and re.fullmatch(r"loc-[0-9a-f]{24}", location)),
            "invalid source object locator")
    if isinstance(pointer, str):
        decoded = pointer.replace("~1", "/").replace("~0", "~")
        require(not re.search(r"/(?:home|srv|opt|root|run|etc|var)/|meshify", decoded, re.I),
                "source locator contains deployment details")


def validate_documents(history, sources):
    coverage = history["coverage"]
    require(not any(key.startswith(("ui_", "meshify_")) or key == "excluded_image_profile_count" for key in coverage),
            "public coverage contains host inventory metadata")
    records, configs, points = history["records"], history["configs"], history["points"]
    record_ids = {record["id"] for record in records}
    require(len(record_ids) == len(records) == coverage["historical_records"], "duplicate or omitted historical record")
    require(len(configs) == coverage["configuration_snapshots"]
            and len(points) == coverage["unique_measurement_waves"]
            and len(history["checks"]) == coverage["bounded_check_records"]
            and len(history["summaries"]) == coverage["reported_rate_summaries"], "coverage totals differ")
    require(len(history["observations"]) == coverage["supplemental_result_records"], "additional result coverage differs")
    require(dict(Counter(row["kind"] for row in history["observations"].values())) == coverage["supplemental_result_kind_counts"],
            "additional result categories differ")
    archived = coverage["archived_profile_ids"]
    require(len(set(archived)) == len(archived) == coverage["archived_profile_count"] == 81
            and not coverage["missing_archived_profiles"] and set(archived) <= record_ids,
            "archived profile coverage is incomplete")
    require({row["id"] for row in records if "archived_profile" in row["origin_types"]} == set(archived),
            "archived profile inventory differs")
    require(not any(identity.isdecimal() for identity in record_ids), "source array index is not a profile name")
    require(dict(Counter(row["measurement_status"] for row in records)) == coverage["profile_measurement_status_counts"],
            "historical evidence status counts differ")
    require(sum(point["shared_decode_valid"] for point in points.values()) == coverage["synchronized_decode_waves"],
            "valid interval coverage differs")
    for identity, config in configs.items():
        serialized = json.dumps(config["settings"], sort_keys=True, separators=(",", ":"), allow_nan=False)
        require(config["configuration_id"] == identity
                and hashlib.sha256(serialized.encode()).hexdigest() == config["settings_sha256"], "configuration digest differs")
        settings = config["settings"]
        if config["artifact_pin_recorded"]:
            require(settings["model_repository"] and re.fullmatch(r"[0-9a-f]{40}", settings["model_revision"]),
                    "claimed artifact pin is absent")
        for origin in config["sources"]:
            receipt(origin, sources)
    for identity, point in points.items():
        require(point["measurement_id"] == identity and set(point["configuration_ids"]) <= configs.keys(), "wave binding differs")
        count = point["request_count"]
        require(type(count) is int and count > 0, "wave request count is missing")
        if point.get("model_instance_count"):
            instances = point["model_instance_count"]
            per_instance = point["requests_per_instance"]
            require(type(instances) is int and instances > 0 and len(per_instance) == instances
                    and all(type(value) is int and value > 0 for value in per_instance)
                    and sum(per_instance) == count, "multi-instance wave accounting differs")
        if point["measurement_kind"] == "client_estimated_decode_wave":
            require(point["shared_decode_valid"] is False and point.get("server_trace_available") is False,
                    "client estimate cannot claim a synchronized backend interval")
        if point["request_data_complete"]:
            require(len(point["requests"]) == len(point["input_tokens_per_request"])
                    == len(point["accepted_output_tokens_per_request"]) == len(point["cached_input_tokens_per_request"]) == count,
                    "wave request geometry differs")
            require(sum(point["accepted_output_tokens_per_request"]) == point["accepted_output_tokens_total"],
                    "completion numerator differs")
        if point["shared_decode_valid"]:
            interval, tokens, rate = (point[key] for key in
                                     ("shared_decode_interval_seconds", "shared_decode_accepted_tokens", "decode_tok_s_aggregate"))
            require(point["source_declared_decode_valid"] is True and interval > 0 and tokens > 0
                    and math.isclose(tokens / interval, rate, rel_tol=1e-9), "shared decode accounting differs")
            rates, request_tokens = point["decode_request_rates_tok_s"], point["decode_request_accepted_tokens"]
            if rates:
                require(len(rates) == len(request_tokens) == count
                        and math.isclose(sum(rates), rate, rel_tol=1e-9)
                        and sum(request_tokens) == tokens, "shared request decomposition differs")
            replicas = point["per_replica_decode"]
            if replicas:
                require(sum(row["accepted_tokens_in_shared_window"] for row in replicas) == tokens,
                        "instance numerator differs from whole wave")
        else:
            require(all(point[key] is None for key in
                        ("decode_tok_s_aggregate", "shared_decode_interval_seconds", "shared_decode_accepted_tokens")),
                    "legacy estimate or invalid window cannot fill qualified decode fields")
        total, elapsed, rate = (point[key] for key in
                                ("accepted_output_tokens_total", "elapsed_seconds", "end_to_end_accepted_tok_s"))
        if all(isinstance(value, (int, float)) for value in (total, elapsed, rate)) and elapsed > 0:
            matches = math.isclose(total / elapsed, rate, rel_tol=1e-9)
            require(point["end_to_end_accounting_matches"] == matches, "whole-wave denominator differs")
            require(matches or point.get("end_to_end_accounting_note"), "source accounting limitation is omitted")
        times = point["ttft_seconds_per_request"]
        if times:
            require(statistics.median(times) == point["ttft_median_seconds"]
                    and max(times) == point["ttft_slowest_seconds"], "first-token summary differs")
        if point["cache_hit_verified"] is True:
            require(point["cached_input_tokens_per_request"]
                    and all(value is not None and value > 0 for value in point["cached_input_tokens_per_request"]),
                    "cache-hit label lacks token counters")
        require(point["sources"], "wave provenance missing")
        for origin in point["sources"]:
            receipt(origin, sources)
        if point.get("request_source"):
            receipt(point["request_source"], sources)
    for summary in history["summaries"].values():
        require(summary["reported_tok_s"] > 0 and set(summary["configuration_ids"]) <= configs.keys()
                and set(summary["citing_configuration_ids"]) <= configs.keys(), "summary binding differs")
        if summary["configuration_binding"] == "referenced_run_only" and not summary["referenced_source_available"]:
            require(not summary["configuration_ids"], "credited result transferred to citing configuration")
        for origin in summary["sources"]:
            receipt(origin, sources)
    for check in history["checks"].values():
        require(type(check["passed"]) is bool and set(check["configuration_ids"]) <= configs.keys(), "check binding differs")
        receipt(check["source"], sources)
    for identity, row in history["observations"].items():
        require(identity == row["result_id"] and set(row["configuration_ids"]) <= configs.keys()
                and set(row["profile_ids"] + row["associated_profile_ids"]) <= record_ids,
                "additional result binding differs")
        require(row["sources"] and row["overlap_policy"], "additional result has no provenance or overlap policy")
        require(bool(row["configuration_ids"]) == (row["configuration_binding"] == "recorded_config_or_job"),
                "unbound result claims a measured configuration")
        for origin in row["sources"]:
            receipt(origin, sources)
        metrics = row["metrics"]
        if row["kind"] in {"quality_evaluation", "quoted_quality_score"}:
            passed, total = metrics["passed"], metrics["total"]
            require(type(passed) is int and type(total) is int and 0 <= passed <= total and total > 0,
                    "quality numerator or denominator is invalid")
            samples = metrics["samples"]
            if samples:
                require(len(samples) == total and [sample["sample_index"] for sample in samples] == list(range(total)),
                        "quality sample accounting differs")
                require(all(type(sample.get("passed")) is bool for sample in samples)
                        and sum(sample["passed"] for sample in samples) == passed, "quality grades differ from total")
            for category, score in metrics["categories"].items():
                require(category in CATEGORIES and type(score["passed"]) is int, "quality category is invalid")
                if score["total"] is not None:
                    require(0 <= score["passed"] <= score["total"], "quality category denominator differs")
                if samples:
                    group = [sample for sample in samples if sample.get("category") == category]
                    require(len(group) == score["total"] and sum(sample["passed"] for sample in group) == score["passed"],
                            "category grades differ from samples")
            times = [sample["request"]["elapsed_seconds"] for sample in samples
                     if finite_number(sample.get("request", {}).get("elapsed_seconds"))]
            if times:
                summary = metrics["task_total_latency_seconds"]
                require(summary == {"count": len(times), "minimum": min(times), "median": statistics.median(times), "maximum": max(times)},
                        "quality latency denominator differs")
                if "reported_task_latency_median_seconds" in metrics:
                    require(math.isclose(metrics["reported_task_latency_median_seconds"], summary["median"], rel_tol=1e-12),
                            "reported quality latency is not the saved task median")
        else:
            for key, value in metrics.get("values", {}).items():
                values = value if isinstance(value, list) else [value]
                require(key in NUMERIC_UNITS and all(finite_number(child) for child in values),
                        "additional metric lacks a unit or finite value")
        require(set(metrics.get("flags", {})) <= FLAGS
                and all(type(value) is bool for value in metrics.get("flags", {}).values()),
                "additional result has an unknown check flag")
    for record in records:
        require(set(record["configuration_ids"]) <= configs.keys()
                and set(record["measurement_ids"]) <= points.keys()
                and set(record["check_ids"]) <= history["checks"].keys()
                and set(record["rate_summary_ids"]) <= history["summaries"].keys()
                and set(record.get("observation_ids", [])) <= history["observations"].keys(), "record has dangling evidence links")
        for identity in record.get("observation_ids", []):
            require(record["id"] in history["observations"][identity]["profile_ids"], "additional evidence backlinks differ")
        require(record["launcher_supported"] is False and record["fresh_export_gpu_verified"] is False,
                "historical record claims a supported or freshly GPU-tested export")
        if record["id"] in archived:
            require("archived_profile" in record["origin_types"], "archived profile origin is missing")
        for job in record["recorded_jobs"]:
            require(job["configuration_id"] in configs, "job configuration missing")
            receipt(job["source"], sources)


def validate_history(repo):
    history = load_history(repo)
    root = repo / "archive/history"
    require(json.loads((root / "observations.json").read_text())["numeric_units"] == NUMERIC_UNITS,
            "additional result unit definitions differ")
    source_rows = json.loads((repo / "archive/history/sources.json").read_text())["sources"]
    sources = {(row["file"], row["sha256"]) for row in source_rows}
    require(len(sources) == len(source_rows), "duplicate source inventory")
    validate_documents(history, sources)
    expected_result_sources = {}
    for row in history["observations"].values():
        for origin in row["sources"]:
            expected_result_sources.setdefault((origin["file"], origin["sha256"]), set()).add(row["result_id"])
    rows = json.loads((root / "result-sources.json").read_text())["sources"]
    actual_result_sources = {(row["file"], row["sha256"]): set(row["observation_ids"]) for row in rows}
    require(len(actual_result_sources) == len(rows) and actual_result_sources == expected_result_sources,
            "additional result source index differs")
    expected_pages = {record["id"] + ".md" for record in history["records"]}
    actual_pages = {path.name for path in (repo / "archive/history/profiles").glob("*.md")}
    require(expected_pages == actual_pages, "profile pages omitted or invented")
    for filename, content in archive_documents(history, STATUS).items():
        require((repo / "archive" / filename).read_text() == content,
                "archive navigation is stale: " + filename)
    expected_family_pages = {filename.removeprefix("models/") for filename in archive_documents(history, STATUS)
                             if filename.startswith("models/")}
    require({path.name for path in (repo / "archive/models").glob("*.md")} == expected_family_pages,
            "model-family index omitted or invented")
    for filename, content in prefill_documents(history).items():
        require((root / filename).read_text() == content, "prefill index is stale: " + filename)
    require(json.loads((root / "prefill.json").read_text()) == prefill_dataset(history),
            "prefill entries differ from retained observations")
    for row in prefill_rows(history):
        require(row["backend_prefill_seconds"] > 0
                and math.isclose(row["prefill_tok_s"], row["processed_prompt_tokens"] / row["backend_prefill_seconds"],
                                 rel_tol=1e-9), "prefill numerator or backend timer differs")
    require((repo / "archive/qwen3.8-27b-replicas/README.md").read_text() == qwen_replica_document(repo),
            "Qwen replica history page is stale")
    for record in history["records"]:
        path = repo / "archive/history/profiles" / (record["id"] + ".md")
        require(path.read_text() == profile_page(record, history), "historical page is stale: " + record["id"])
    for filename, rows in (("benchmarks.csv", benchmark_csv_rows(history)),
                           ("profiles.csv", history["records"]),
                           ("rate-summaries.csv", list(history["summaries"].values())),
                           ("observations.csv", observation_csv_rows(history)),
                           ("prefill.csv", prefill_rows(history)),
                           ("../qwen3.8-27b-replicas/benchmarks.csv", qwen_replica_rows(repo)),
                           ("../qwen3.8-27b-replicas/requests.csv", json.loads((repo / "recipes/qwen3.8-27b-exl3/historical-replica-requests.json").read_text())["requests"])):
        with (repo / "archive/history" / filename).open(newline="") as stream:
            actual = list(csv.DictReader(stream))
        fields = list(dict.fromkeys(key for row in rows for key in row))
        expected = [{key: csv_value(row.get(key)) for key in fields} for row in rows]
        require(actual == expected, "historical CSV differs: " + filename)
    for filename, content in observation_documents(history).items():
        require((repo / "archive/history" / filename).read_text() == content, "additional results page is stale: " + filename)
    return len(history["records"]), len(history["points"])
