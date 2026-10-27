"""Validate historical configurations without admitting them to the recipe launcher."""
import csv
import hashlib
import json
import math
from pathlib import Path
import re
import statistics

from build_docs import archive_card, number


def require(condition, message):
    if not condition:
        raise ValueError("Archive: " + message)


def source_receipt(origin):
    require(Path(origin["file"]).name == origin["file"]
            and re.fullmatch(r"[0-9a-f]{64}", origin["sha256"]), "invalid source receipt")


def validate_record(profile, benchmark, evidence, config, comparison):
    name = profile["id"]
    require(profile["status"] == "archived" and profile["launcher_supported"] is False,
            "historical configuration must not claim launcher support")
    require(profile["format_version"] == benchmark["format_version"] == evidence["format_version"] == 1
            and benchmark["profile"] == evidence["profile"] == name, "record identities differ")
    require(re.fullmatch(r"[0-9a-f]{40}", profile["model"]["revision"])
            and re.fullmatch(r"[0-9a-f]{40}", profile["model"]["mtp"]["revision"])
            and re.fullmatch(r"[0-9a-f]{64}", profile["build"]["recorded_binary_sha256"]),
            "missing artifact/build identity")
    serving = profile["serving"]
    kv = serving["kv"]
    args = config["args"]
    require(config["api_key"] == "@API_KEY@" and config["host"] == "@HOST@"
            and config["port"] == "@PORT@" and args[args.index("--gpu") + 1] == "@DEVICES@",
            "deployment values must remain placeholders")
    require(int(args[args.index("--max-context") + 1]) == serving["context_tokens"]
            and config["parallel"] == serving["max_requests"], "template and profile geometry differ")
    require(kv["logical_batch_tokens"] == serving["context_tokens"] * serving["max_requests"]
            and kv["resident_gpu_tokens_per_batch_slot"] == int(args[args.index("--kv-resident") + 1])
            and kv["resident_batch_gpu_tokens"] == int(args[args.index("--kv-resident") + 1]) * serving["max_requests"]
            and kv["separate_solo_gpu_tokens"] == int(args[args.index("--kv-resident") + 1])
            and kv["separate_solo_logical_tokens"] == serving["context_tokens"],
            "resident, logical or separate solo KV capacity differs")
    require(str(kv["resident_batch_gpu_tokens"]) == comparison["GPU KV pool, tokens"].replace(",", "")
            and str(kv["logical_batch_tokens"]) == comparison["Batch logical KV capacity, tokens"].replace(",", "")
            and str(serving["max_requests"]) == comparison["Configured slots"]
            and str(profile["hardware"]["card_count"]) == comparison["Cards"],
            "configuration differs from retained comparison")
    require(evidence["memory"]["eight_bit_main_and_draft_verified"]
            and evidence["memory"]["host_kv_allocated_bytes"] == kv["observed_host_allocation_bytes"]
            and number(kv["observed_host_allocation_bytes"] / 2**30) == comparison["Host KV allocation, GiB"]
            and len(evidence["memory"]["sampled_peak_vram_mib_per_card"]) == profile["hardware"]["card_count"]
            and number([x / 1024 for x in evidence["memory"]["sampled_peak_vram_mib_per_card"]])
            == comparison["Observed peak VRAM per selected card, GiB"], "memory evidence differs")
    require(evidence["verification"]["near_limit_context_qualified"] is False
            and evidence["verification"]["general_quality_qualified"] is False,
            "historical 32k trial cannot qualify full context or model quality")
    for origin in evidence["source_receipts"]:
        source_receipt(origin)
    require(len(benchmark["points"]) == 2, "expected one single and one configured-wave result")
    for point in benchmark["points"]:
        count = point["concurrency"]
        require(count == (1 if point["mode"] == "single" else serving["max_requests"])
                and point["repetitions"] == 1, "wave geometry or repetition count differs")
        for key in ("input_tokens_per_request", "accepted_output_tokens_per_request",
                    "cached_tokens_per_request", "ttft_seconds_per_request", "cold_prefill_reported"):
            require(len(point[key]) == count, "incomplete request array: " + key)
        require(all(x == 256 for x in point["accepted_output_tokens_per_request"])
                and all(x == 0 for x in point["cached_tokens_per_request"]), "output/cache counts differ")
        require(point["elapsed_seconds"] > 0
                and math.isclose(sum(point["accepted_output_tokens_per_request"]) / point["elapsed_seconds"],
                                 point["end_to_end_accepted_tok_s"], rel_tol=1e-12),
                "whole-wave throughput denominator differs")
        require(math.isclose(statistics.median(point["ttft_seconds_per_request"]), point["ttft_median_seconds"], rel_tol=1e-12)
                and max(point["ttft_seconds_per_request"]) == point["ttft_slowest_seconds"], "TTFT summary differs")
        if point["shared_decode_valid"]:
            interval, tokens = point["shared_decode_interval_seconds"], point["shared_decode_accepted_tokens"]
            require(interval > 0 and tokens > 0
                    and math.isclose(tokens / interval, point["decode_tok_s_aggregate"], rel_tol=1e-12),
                    "shared decode numerator/denominator differs")
            require(len(point["decode_tok_s_per_request"]) == len(point["shared_decode_accepted_tokens_per_request"]) == count
                    and sum(point["shared_decode_accepted_tokens_per_request"]) == tokens
                    and math.isclose(sum(point["decode_tok_s_per_request"]), point["decode_tok_s_aggregate"], rel_tol=1e-12),
                    "shared-window request counts/rates differ")
        else:
            require(point["decode_tok_s_aggregate"] is None
                    and point["shared_decode_interval_seconds"] is None
                    and point["shared_decode_accepted_tokens"] is None
                    and not point["decode_tok_s_per_request"]
                    and not point["shared_decode_accepted_tokens_per_request"]
                    and point["performance_measurements_qualified"] is False
                    and point["unqualified_decode_observation"]["reason"],
                    "unqualified decode must remain unavailable")
        prefix = f"C{count} "
        for key, field in (("decode_tok_s_aggregate", "decode aggregate, tok/s"),
                           ("end_to_end_accepted_tok_s", "end-to-end accepted, tok/s"),
                           ("ttft_median_seconds", "cold first-token median, s"),
                           ("ttft_slowest_seconds", "cold slowest first-token, s")):
            require(number(point[key]) == comparison[prefix + field], "numeric result differs: " + key)
        require(number(point["input_tokens_per_request"]) == comparison[prefix + "actual input, tokens/request"],
                "input counts differ from retained comparison")
        source_receipt(point["source"])
        source_receipt(point["wave_source"])


def validate_archive(repo, active_ids):
    catalog = json.loads((repo / "archive/catalog.json").read_text())
    comparisons = json.loads((repo / "data/runtime-trials.json").read_text())["cases"]
    runtime = json.loads((repo / "archive/runtime.json").read_text())
    require(catalog["format_version"] == 2 and catalog["status"] == "historical_only"
            and catalog["historical_catalog"] == "archive/history/catalog.json"
            and catalog["coverage_file"] == "archive/history/coverage.json", "invalid catalog status")
    for source in (runtime, runtime["llama_cpp"]):
        require(re.fullmatch(r"[0-9a-f]{40}", source["revision"]), "runtime source is not pinned")
    patch = runtime["allocation_instrumentation"]
    require(hashlib.sha256((repo / patch["file"]).read_bytes()).hexdigest() == patch["sha256"]
            and "MIT License" in (repo / patch["license_file"]).read_text(), "patch identity/license differs")
    ids, rows = set(), []
    for entry in catalog["profiles"]:
        name = entry["id"]
        require(name not in ids and name not in active_ids, "duplicate or active-catalog entry")
        require(entry["path"] == f"archive/{name}/profile.json", "unexpected profile path")
        ids.add(name)
        profile = json.loads((repo / entry["path"]).read_text())
        require(profile["id"] == name and profile["recommended_recipe"] in active_ids,
                "profile identity or recommended alternative differs")
        folder = repo / "archive" / name
        benchmark = json.loads((folder / profile["benchmark_file"]).read_text())
        evidence = json.loads((folder / profile["evidence_file"]).read_text())
        config = json.loads((folder / profile["configuration_file"]).read_text())
        validate_record(profile, benchmark, evidence, config, comparisons[name])
        require((folder / "README.md").read_text() == archive_card(profile), "profile README is stale: " + name)
        rows.extend(dict(profile=name, **point) for point in benchmark["points"])
    require(ids == {path.parent.name for path in (repo / "archive").glob("*/profile.json")}, "catalog omits a profile")
    with (repo / "archive/benchmarks.csv").open(newline="") as stream:
        actual = list(csv.DictReader(stream))
    expected = [{key: json.dumps(value, separators=(",", ":")) if isinstance(value, (list, dict))
                 else "" if value is None else str(value) for key, value in row.items()} for row in rows]
    require(actual == expected, "CSV differs from exact JSON measurements")
    return len(ids), len(rows)
