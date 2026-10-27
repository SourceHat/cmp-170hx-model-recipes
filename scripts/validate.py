#!/usr/bin/env python3
"""Validate the public recipe collection without loading inference libraries."""
import ast
import hashlib
import json
import math
from pathlib import Path
import re
import subprocess
import sys

from jsonschema import Draft202012Validator
import yaml
from markdown_it import MarkdownIt

REPO = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO / "scripts"))
from launch import render
from build_docs import (card, performance_row, summary_row, table,
                        recovered_prefill_document, qwen_32k_document, selected_prefill_document)
from native_prefill import recover_prefill
from selected_prefill import validate_dataset
from apex_capacity import RECIPE as APEX_RECIPE, verify_capacity
from validate_archive import validate_archive
from validate_history import validate_history
from deepseek_followup import verify_reference_profile


def public_files():
    names = subprocess.check_output(
        ["git", "ls-files", "--cached", "--others", "--exclude-standard", "-z"], cwd=REPO
    ).decode().split("\0")
    return [REPO / name for name in dict.fromkeys(names) if name and (REPO / name).is_file()]


def require(condition, message):
    if not condition:
        raise ValueError(message)


def validate_recovered_prefill():
    folder = REPO / "recipes/qwen3.8-27b-exl3"
    requests = json.loads((folder / "historical-replica-requests.json").read_text())["requests"]
    result = json.loads((folder / "historical-replica-result.json").read_text())
    require(len(requests) == 102, "Qwen request timing export is incomplete")
    for mode, waves in result["measurements"].items():
        for state, wave in waves.items():
            selected = [row for row in requests if row["mode"] == mode and row["source_wave"] == state]
            require(len(selected) == sum(card["requests"] for card in wave["per_card"]),
                    "Qwen request count differs from its decode wave")
            for replica in wave["request_timing_by_replica"]:
                group = [row for row in selected if row["replica_index"] == replica["replica_index"]]
                require(len(group) == replica["request_count"], "Qwen timing replica count differs")
                for key, source in (("input_tokens_per_request", "input_tokens"),
                                    ("cached_prompt_tokens_per_request", "cached_prompt_tokens"),
                                    ("backend_prefill_tok_s_per_request", "backend_prefill_tok_s"),
                                    ("backend_prefill_seconds_per_request", "backend_prefill_seconds"),
                                    ("client_ttft_seconds_per_request", "client_ttft_seconds")):
                    require(replica[key] == [row[source] for row in group], "Qwen timing summary differs")
                for row in group:
                    timing = row["request"]["timings"]
                    require(row["input_tokens"] == row["processed_prompt_tokens"] + row["cached_prompt_tokens"]
                            and row["processed_prompt_tokens"] == timing["prompt_n"]
                            and row["cached_prompt_tokens"] == timing["cache_n"]
                            and row["backend_prefill_seconds"] == timing["prompt_ms"] / 1000
                            and row["client_ttft_seconds"] == row["request"]["ttft_seconds"]
                            and math.isclose(row["backend_prefill_tok_s"], row["processed_prompt_tokens"] /
                                             row["backend_prefill_seconds"], rel_tol=1e-12),
                            "Qwen prefill counts or timer differ")


def validate_native_prefill_recovery():
    import csv
    data = json.loads((REPO / "data/native-prefill-recovery.json").read_text())
    records = {row["id"]: row for row in data["records"]}
    require(len(records) == len(data["records"]) == 4, "Native prefill recovery is incomplete")
    awq = REPO / "recipes/apex-abliterated-awq-dflash2-pp3-balanced"
    recipe = json.loads((awq / "recipe.json").read_text())
    points = json.loads((awq / "benchmarks.json").read_text())["points"]
    for record in records.values():
        measured = recover_prefill(record)
        require(measured == record["measurement"], "Native prefill result differs from its metric snapshots")
        require(record["model"]["model"] == recipe["model"]["hf_repo"]
                and record["model"]["revision"] == recipe["model"]["revision"]
                and record["concurrency"] == 1 and record["output_budget_tokens"] == 8192
                and record["configuration"]["context"] == 524288,
                "Recovered prefill identity or workload differs")
        require(re.fullmatch(r"source-[0-9a-f]{24}\.json", record["source"]["file"])
                and re.fullmatch(r"[0-9a-f]{64}", record["source"]["sha256"]),
                "Invalid native prefill source receipt")
        if record["profile"] == recipe["id"]:
            selected = [point for point in points if point.get("backend_prefill_evidence", {}).get("record_id") == record["id"]]
            require(len(selected) == 1, "Native prefill has no unique matching recipe wave")
            point = selected[0]
            require(point["concurrency"] == 1 and point["output_tokens_per_request"] == 8192
                    and point["cohort"] == "balanced-long-output" and point["cache_state"] == record["wave"]
                    and point["input_tokens_per_request"] == [measured["input_tokens"]]
                    and point["ttft_seconds_per_request"] == [record["request"]["client_ttft_seconds"]]
                    and point["cached_tokens_per_request"] == [measured["cached_prompt_tokens"]]
                    and point["backend_prefill_tok_s_per_request_median"] == measured["prefill_tok_s"],
                    "Native prefill was assigned to a different workload")
            require(point["backend_prefill_per_request"] == [
                {key: measured[key] for key in ("processed_prompt_tokens", "cached_prompt_tokens",
                                               "backend_prefill_seconds", "prefill_tok_s")}
                | {"source": "single_request_native_histogram_delta"}],
                "Native prefill request details differ")
    with (REPO / "data/native-prefill-recovery.csv").open(newline="") as stream:
        rows = list(csv.DictReader(stream))
    require(len(rows) == 4 and {row["id"] for row in rows} == set(records), "Native prefill CSV is incomplete")
    for row in rows:
        record = records[row["id"]]
        for field, value in record["measurement"].items():
            if field == "request_count":
                continue
            require(float(row[field]) == value, "Native prefill CSV differs: " + field)
        require(float(row["client_ttft_seconds"]) == record["request"]["client_ttft_seconds"]
                and row["source_sha256"] == record["source"]["sha256"], "Native prefill CSV source/TTFT differs")
    require((REPO / "docs/RECOVERED-PREFILL.md").read_text() == recovered_prefill_document()
            and (REPO / "docs/QWEN-32K-EVIDENCE.md").read_text() == qwen_32k_document(),
            "Recovered-evidence documentation is stale")


def validate_selected_prefill():
    path = REPO / "data/selected-serving-prefill.json"
    if not path.exists():
        return
    import csv
    data = json.loads(path.read_text())
    recipes = {folder.name: json.loads((folder / "recipe.json").read_text())
               for folder in (REPO / "recipes").iterdir() if (folder / "recipe.json").exists()}
    result = validate_dataset(data, recipes)
    require(result["completed_recipes"] > 0, "Selected prefill dataset contains no complete cohort")
    with (REPO / "data/selected-serving-prefill.csv").open(newline="") as stream:
        rows = {row["recipe"]: row for row in csv.DictReader(stream)}
    require(len(rows) == result["completed_recipes"], "Selected prefill CSV coverage differs")
    for cohort in data["cohorts"]:
        benchmark = json.loads((REPO / "recipes" / cohort["recipe"] / "benchmarks.json").read_text())
        require(benchmark.get("preferred_headline_cohort") == data["cohort"], "New cohort is not selected as a complete pair")
        for point in cohort["points"]:
            require(point in benchmark["points"], "Selected comparison differs from recipe measurements")
        single = next(p for p in cohort["points"] if p["concurrency"] == 1)
        wave = next(p for p in cohort["points"] if p["concurrency"] > 1)
        row = rows[cohort["recipe"]]
        for field, value in {"c1_prefill_tok_s": single["backend_prefill_tok_s_per_request_median"],
                             "c1_ttft_seconds": single["ttft_median_seconds"],
                             "c1_decode_tok_s": single["decode_tok_s_aggregate"],
                             "wave_decode_tok_s_total": wave["decode_tok_s_aggregate"],
                             "wave_e2e_tok_s_total": wave["end_to_end_accepted_tok_s"],
                             "wave_decode_interval_seconds": wave["shared_decode_interval_seconds"],
                             "wave_accepted_tokens_in_interval": wave["shared_decode_accepted_tokens"],
                             "wave_requests": wave["concurrency"]}.items():
            require(float(row[field]) == value, "Selected comparison CSV differs: " + field)
        require(json.loads(row["wave_actual_input_tokens"]) == wave["input_tokens_per_request"],
                "Selected CSV input counts differ")
    require((REPO / "docs/PREFILL-COMPARISON.md").read_text() == selected_prefill_document(),
            "Selected comparison documentation is stale")


def validate():
    verify_reference_profile(REPO)
    fidelity = json.loads((REPO / "data/selection-comparisons.json").read_text())["apex"]["release_fidelity"]
    require(fidelity["total_tokens"] == fidelity["held_out_windows"] * fidelity["tokens_per_window"],
            "Publisher input-window geometry differs")
    require(fidelity["scored_prediction_tokens"] is None
            and fidelity["BF16_reference_revision"] is None
            and "not an established scored prediction count" in fidelity["total_tokens_scope"],
            "Publisher scoring denominator must remain unspecified")
    schema = json.loads((REPO / "schemas/recipe.schema.json").read_text())
    validator = Draft202012Validator(schema)
    catalog = json.loads((REPO / "catalog.json").read_text())
    ids, model_ids = set(), set()
    measurement_ids = set()
    total_points = 0
    summary_rows = {}
    performance_rows = {}
    historical_waves = 0
    for item in catalog["recipes"]:
        folder = REPO / "recipes" / item["id"]
        r = json.loads((REPO / item["path"]).read_text())
        validator.validate(r)
        require(r["id"] == item["id"] and r["id"] not in ids, "Duplicate or mismatched recipe id")
        ids.add(r["id"])
        model = r["model"]["served_name"]
        require(model not in model_ids, "Model ids must be unique")
        model_ids.add(model)
        require("host" not in r["serving"] and "port" not in r["serving"]
                and "placement" not in r["hardware"] and "role" not in r,
                "Recipe contains deployment-specific assignments")
        if r["runtime"]["id"] in ("apex-awq", "deepseek"):
            require(r["serving"]["kv"].get("capacity_basis") == "vllm_context_normalized_block_capacity",
                    "vLLM capacity must identify its context normalization")
            require(r["serving"]["kv"].get("capacity_context_tokens") == r["serving"]["context_tokens"],
                    "vLLM capacity reporting context differs from the selected recipe")
        plan = render(r, devices=",".join(map(str,range(r["hardware"]["card_count"]))),
                      runtime_root=Path("/example/runtime"), model_path=Path("/example/model with spaces"),
                      draft_path=Path("/example/draft"), engram_path=Path("/example/nvme"),
                      source_model_path=Path("/example/source"),
                      output_dir=Path("/example/output"), host="127.0.0.2", port=9000)
        require(all(isinstance(x,str) for x in plan["argv"]), "Launch arguments must be strings")
        if r["runtime"]["id"] == "tabby":
            config = yaml.safe_load((folder / "config.yml").read_text())
            require(config == r["engine_config"], "Tabby config differs from recipe metadata")
            require(config["network"]["port"] == "@PORT@" and config["network"]["host"] == "@HOST@", "Listener must be configurable")
            network = json.loads(plan["artifacts"]["config.yml"])["network"]
            require(network["port"] == 9000 and network["host"] == "127.0.0.2", "Listener override was not rendered")
            require(config["model"]["cache_size"] == r["serving"]["kv"]["shared_gpu_pool_tokens"], "Wrong KV pool")
            require(config["model"]["max_seq_len"] == r["serving"]["context_tokens"], "Wrong context")
        else:
            require(json.loads((folder / "engine-config.json").read_text()) == r["engine_config"], "Engine config differs from metadata")
            argv = r["engine_config"]["argv"]
            require(argv[argv.index("--host")+1] == "@HOST@", "vLLM host must be configurable")
            require(argv[argv.index("--port")+1] == "@PORT@", "vLLM port must be configurable")
            if r["runtime"]["id"] == "deepseek":
                require(plan["argv"][:2] == ["docker", "compose"], "DeepSeek must use its pinned container runtime")
                require(plan["environment"]["BIND_ADDRESS"] == "127.0.0.2"
                        and plan["environment"]["PORT"] == "9000", "Container listener override was not rendered")
                compose = yaml.safe_load((folder / "compose.yaml").read_text())["services"]["deepseek"]
                require(compose["environment"]["CUDA_VISIBLE_DEVICES"].startswith("${DEVICES:?"), "Container devices must be selected explicitly")
                require(compose["ports"][0]["host_ip"] == "${BIND_ADDRESS:-127.0.0.1}"
                        and compose["ports"][0]["published"] == "${PORT:-8000}", "Container listener must be configurable")
                expected = [arg.replace("@MODEL@", "/models/main").replace("@HOST@", "0.0.0.0").replace("@PORT@", "8000") for arg in argv]
                actual = compose["command"]
                require(len(expected) == len(actual), "Container arguments differ from the engine template")
                for left, right in zip(expected, actual):
                    require(json.loads(left) == json.loads(right) if left.startswith("{") else left == str(right), "Container argument differs from the engine template")
            else:
                rendered = plan["argv"]
                require(rendered[rendered.index("--host")+1] == "127.0.0.2"
                        and rendered[rendered.index("--port")+1] == "9000", "vLLM listener override was not rendered")
        bench = json.loads((folder / r["benchmark_file"]).read_text())
        require(bench["recipe"] == r["id"], "Benchmark identity differs")
        summary_rows[r["id"]] = summary_row(r, bench["points"])
        performance_rows[r["id"]] = performance_row(r, bench["points"])
        require((folder / "README.md").read_text() == card(r), "Recipe README is stale: " + r["id"])
        if r["id"] == "qwen3.8-27b-exl3":
            history = json.loads((folder / "historical-replica-result.json").read_text())
            require(history["replicas"] == history["configuration"]["replicas"] == 3,
                    "Historical Qwen replica count differs")
            require(history["source_sha256"] == history["source"]["sha256"]
                    and any(origin["sha256"] == history["source_sha256"] for origin in r["source_receipts"]),
                    "Historical Qwen source differs")
            for mode, requests_per_replica in (("one_stream_per_card", 1), ("sixteen_streams_per_card", 16)):
                for state in ("cold", "warm"):
                    wave = history["measurements"][mode][state]
                    interval, tokens = wave["window_seconds"], wave["generated_tokens"]
                    require(wave["valid"] and interval > 0 and tokens > 0, "Invalid historical Qwen interval")
                    require(len(wave["per_card"]) == history["replicas"], "Missing historical Qwen replica")
                    require(sum(replica["generated_tokens"] for replica in wave["per_card"]) == tokens,
                            "Historical Qwen replica tokens differ from rig total")
                    require(math.isclose(tokens / interval, wave["aggregate_generation_tps"], rel_tol=1e-9),
                            "Historical Qwen interval does not reproduce rig throughput")
                    for replica in wave["per_card"]:
                        require(replica["requests"] == requests_per_replica,
                                "Historical Qwen request geometry differs")
                        require(math.isclose(replica["generated_tokens"] / interval,
                                             replica["generation_tps"], rel_tol=1e-9),
                                "Historical Qwen interval does not reproduce per-replica throughput")
                    historical_waves += 1
        for point in bench["points"]:
            require(point["concurrency"] >= 1 and point["decode_tok_s_aggregate"] > 0, "Invalid throughput point")
            require(point["transport"] == "host", "Selected recipe must not substitute experimental transport results")
            ratio = point.get("draft_acceptance_ratio")
            require(ratio is None or 0 <= ratio <= 1, "Invalid acceptance ratio")
            require(point["measurement_id"] not in measurement_ids, "Duplicate measurement identity")
            measurement_ids.add(point["measurement_id"])
            require(len(point["input_tokens_per_request"]) == point["concurrency"], "Input count differs from concurrency")
            require(len(point["requests"]) == point["concurrency"], "Request evidence differs from concurrency")
            require(len(point["ttft_seconds_per_request"]) == point["concurrency"], "First-token count differs from concurrency")
            interval, tokens = point["shared_decode_interval_seconds"], point["shared_decode_accepted_tokens"]
            require(interval > 0 and tokens > 0, "Invalid common decode interval")
            require(math.isclose(tokens / interval, point["decode_tok_s_aggregate"], rel_tol=1e-9), "Decode interval does not reproduce throughput")
            rates = point["decode_tok_s_per_request"]
            if rates:
                require(len(rates) == point["concurrency"] and math.isclose(sum(rates), point["decode_tok_s_aggregate"], rel_tol=1e-9),
                        "Per-request rates do not reproduce aggregate throughput")
            require(point["cache_state"] != "cached_prefix" or point["cache_hit_verified"] is True, "Unverified cache-hit label")
            proposed, accepted = point["draft_tokens_proposed"], point["draft_tokens_accepted"]
            if proposed and accepted is not None and ratio is not None:
                require(math.isclose(accepted / proposed, ratio, rel_tol=1e-9), "Draft counts do not reproduce acceptance")
            origin = point["source"]
            require(re.fullmatch(r"[0-9a-f]{64}", origin["sha256"]) and Path(origin["file"]).name == origin["file"], "Invalid measurement provenance")
        total_points += len(bench["points"])
        require((folder / "README.md").is_file() and (folder / "launch.sh").is_file(), "Incomplete recipe folder")
        evidence = json.loads((folder / "evidence.json").read_text())
        require(evidence["recipe"] == r["id"] and evidence["format_version"] == 1, "Evidence identity differs")
        for observation in evidence["memory_observations"]:
            if observation.get("preferred"):
                require(observation["tested_kv_pool_tokens"] == r["serving"]["kv"]["shared_gpu_pool_tokens"], "Preferred memory observation has different KV geometry")
                require(observation["tested_context_tokens"] == r["serving"]["context_tokens"], "Preferred memory observation has different context")
        for origin in evidence["source_receipts"]:
            require(re.fullmatch(r"[0-9a-f]{64}", origin["sha256"]) and Path(origin["file"]).name == origin["file"], "Invalid evidence provenance")
    actual = {p.parent.name for p in (REPO / "recipes").glob("*/recipe.json")}
    require(ids == actual, "The catalog omits or invents recipe folders")
    archived_profiles, archived_waves = validate_archive(REPO, ids)
    history_records, history_waves = validate_history(REPO)
    readme = (REPO / "README.md").read_text()
    for row in [*summary_rows.values(), *performance_rows.values()]:
        require(table([""] * len(row), [row]).splitlines()[-1] in readme,
                "Summary row differs from retained results")
    require("See historical tests" not in readme, "Summary uses a placeholder instead of retained results")
    require(all(value not in {"", "None"}
                for row in [*summary_rows.values(), *performance_rows.values()] for value in map(str, row)),
            "Main README contains an empty cell")
    validate_recovered_prefill()
    validate_native_prefill_recovery()
    validate_selected_prefill()
    verify_capacity(REPO)
    publication = json.loads((REPO / "publication.json").read_text())
    require(publication["released_by"] == publication["brand"]["owner"] == "MCP Capital LLC"
            and publication["brand"]["name"] == "SourceHat"
            and readme.rstrip().endswith("This work was performed and is released by **MCP Capital LLC**, owner of the **SourceHat** brand.")
            and all("Copyright (c) 2026 MCP Capital LLC and contributors" in (REPO / name).read_text()
                    for name in ("NOTICE", "LICENSE")), "Brand ownership or release credit is missing")
    quant_sources = json.loads((REPO / "data/quantization-sources.json").read_text())
    for source in quant_sources["records"]:
        recipe = json.loads((REPO / "recipes" / source["recipe"] / "recipe.json").read_text())
        require(source["repository"] == recipe["model"]["hf_repo"]
                and source["revision"] == recipe["model"]["revision"]
                and re.fullmatch(r"[0-9a-f]{64}", source["source"]["sha256"]),
                "Quantization declaration does not match the pinned artifact")
        if "main_weights" in source:
            quant = json.loads((REPO / "recipes" / source["recipe"] / "evidence.json").read_text())["quantization"]
            main = [row for name, row in quant["groups"].items() if name != "native_MTP"]
            payload = sum(row["payload_bytes"] for row in main)
            parameters = sum(row["logical_parameters"] for row in main)
            require(source["main_weights"]["tensor_payload_bytes"] == payload
                    and source["main_weights"]["logical_parameters"] == parameters
                    and source["main_weights"]["effective_bits_per_weight"] == 8 * payload / parameters
                    == quant["main_payload_bits_per_logical_parameter"],
                    "Effective bpw does not reconstruct from weight bytes and parameters")
            whole = source["complete_checkpoint"]
            require(whole["tensor_payload_bytes"] == sum(row["payload_bytes"] for row in quant["groups"].values())
                    and whole["logical_parameters"] == quant["logical_parameters"]
                    and whole["file_bytes_including_headers"] - whole["header_bytes"] == whole["tensor_payload_bytes"]
                    and whole["effective_file_bits_per_weight"] == 8 * whole["file_bytes_including_headers"] /
                    whole["logical_parameters"], "Checkpoint weight-size calculation differs")
    for name, checksum in {
        "Apache-2.0.txt": "cfc7749b96f63bd31c3c42b5c471bf756814053e847c10f3eb003417bc523d30",
        "CC-BY-4.0.txt": "d557539df68e771cc1eedcc91d13f70fca930e508d11eedcafa4b15db49e3744",
    }.items():
        require(hashlib.sha256((REPO / "LICENSES" / name).read_bytes()).hexdigest() == checksum,
                "License text differs from the complete standard license: " + name)
    require("SourceHat" in (REPO / "NOTICE").read_text(), "Original attribution notice is missing")
    runtime_payloads = []
    for manifest in (REPO / "runtimes").glob("*/overlay-manifest.json"):
        for item in json.loads(manifest.read_text())["files"]:
            payload = REPO / item["file"]
            require(hashlib.sha256(payload.read_bytes()).hexdigest() == item["sha256"], "Overlay checksum differs: "+item["file"])
            runtime_payloads.append(item["file"])
    ignored_payloads = subprocess.run(
        ["git", "check-ignore", "--no-index", "--", *runtime_payloads], cwd=REPO, capture_output=True, text=True
    )
    require(ignored_payloads.returncode == 1,
            "Runtime payloads are excluded from the public checkout: " + ignored_payloads.stdout.strip())
    for item in json.loads((REPO / "runtimes/tabby/source-pins.json").read_text())["sources"]:
        require(hashlib.sha256((REPO / item["patch"]).read_bytes()).hexdigest() == item["patch_sha256"], "Source patch checksum differs")

    serving = json.loads((REPO / "data/serving-fairness-verification.json").read_text())
    ram_policy = json.loads((REPO / "archive/ram-prefix-tier/policy.json").read_text())
    policy_by_recipe = {row["recipe"]: row for row in ram_policy["profiles"]}
    tabby_ids = {item["id"] for item in catalog["recipes"]
                 if json.loads((REPO / "recipes" / item["id"] / "recipe.json").read_text())["runtime"]["id"] == "tabby"}
    require(set(policy_by_recipe) == tabby_ids and ram_policy["performance_improvement_measured"] is False
            and ram_policy["gpu_pool_context_slots_changed"] is False,
            "RAM policy must remain a separate configuration decision")
    require(hashlib.sha256((REPO / ram_policy["observation_file"]).read_bytes()).hexdigest()
            == ram_policy["observation_sha256"], "RAM observation digest differs")
    for name, policy in policy_by_recipe.items():
        recipe = json.loads((REPO / "recipes" / name / "recipe.json").read_text())
        require(recipe["serving"]["kv"]["host_kv_budget_mib"] == policy["current_ram_kv_mib"] == 0
                and recipe["engine_config"]["memory"]["sysmem_kv_cache"] == 0
                and recipe["serving"]["kv"]["host_recurrent_budget_mib"]
                == recipe["engine_config"]["memory"]["sysmem_recurrent_cache"]
                == policy["current_ram_recurrent_mib"], "Tabby RAM defaults differ from policy")
    prefix = json.loads((REPO / "data/prefix-reuse-verification.json").read_text())
    prefix_rows = json.loads((REPO / "data/prefix-reuse-requests.json").read_text())
    coverage = {row["recipe"]: row for row in prefix["profile_coverage"]}
    require(set(coverage) == ids and prefix["cpu_tests_passed"] == 81,
            "Prefix runtime coverage differs from the complete catalog")
    require(prefix["runtime_pins"] == json.loads((REPO / "runtimes/tabby/source-pins.json").read_text()),
            "Prefix runtime patch provenance differs")
    require(len(prefix_rows) == 59 and prefix_rows == [r for c in prefix["cohorts"] for r in c["requests"]],
            "Prefix observation export differs from the cohort records")
    require(not prefix["protocol"]["ordinary_traffic_controlled"]
            and prefix["protocol"]["repetitions"] == 1
            and not prefix["gateway_geometry"]["qualified"],
            "Prefix evidence overstates experimental scope")
    for name, row in coverage.items():
        recipe = json.loads((REPO / "recipes" / name / "recipe.json").read_text())
        tested_pool = (json.loads((REPO / "data/apex-kv-capacity/evidence.json").read_text())["baseline_pool_tokens"]
                       if name == APEX_RECIPE else recipe["serving"]["kv"]["shared_gpu_pool_tokens"])
        require(row["shared_prefix_runtime"] == (name in tabby_ids)
                and row["public_launch_rendered"] and row["installed_launch_validated"]
                and row["context_tokens"] == recipe["serving"]["context_tokens"]
                and row["shared_gpu_kv_tokens"] == tested_pool
                and row["slots"] == recipe["serving"]["max_requests"]
                and row["bulk_ram_kv_budget_mib"] == recipe["serving"]["kv"]["host_kv_budget_mib"]
                and row["recurrent_checkpoint_budget_mib"] == recipe["serving"]["kv"]["host_recurrent_budget_mib"],
                "Prefix profile geometry differs: " + name)
    for cohort in prefix["cohorts"]:
        require(cohort["page_table_valid"] and (cohort["route"] != "gateway"
                or not cohort["history_geometry_qualified"]), "History qualification is overstated")
        trace = cohort.get("concurrency_trace_check")
        if trace:
            require(trace["streams"] == 2 and trace["shared_generator_delivery_timestamps"] > 0
                    and trace["both_streams_completed"] and trace["token_counts_monotonic"],
                    "Final runtime concurrency trace check failed")
    for row in prefix_rows:
        require(row["http_status"] == 200 and row["error"] is None
                and 0 <= row["client_first_progress_seconds"] <= row["client_total_seconds"],
                "Prefix request failed or timing differs")
        if row["accepted_output_tokens"] is not None:
            require(0 <= row["cached_input_tokens"] <= row["input_tokens"]
                    and 0 < row["accepted_output_tokens"] <= row["output_budget_tokens"]
                    and math.isclose(row["client_output_tok_s_per_total_second"],
                                     row["accepted_output_tokens"] / row["client_total_seconds"], rel_tol=1e-12),
                    "Prefix request accounting differs")
        if row["cached_fresh_greedy_continuation_equal"] is not None:
            require(row["cached_fresh_greedy_continuation_equal"], "Cached/fresh continuation differs")
    gateway = json.loads((REPO / "data/prefix-gateway-verification.json").read_text())
    gateway_rows = json.loads((REPO / "data/prefix-gateway-requests.json").read_text())
    require(gateway_rows == gateway["requests"] and len(gateway_rows) == 9,
            "Gateway observations differ")
    require(gateway["verification"]["full_history_geometry_matches_native"]
            and gateway["verification"]["complete_rendered_prompts_match_native"]
            and gateway["verification"]["template_options_match_native"]
            and gateway["verification"]["shared_generator_delivery_timestamps"] == 68
            and not gateway["verification"]["other_models_gateway_retested"],
            "Gateway verification scope differs")
    require(not gateway["verification"]["generated_tool_call_completed"]
            and gateway["remaining_issue"]["gateway_responses_actual_output_tokens"] == 16
            and gateway["remaining_issue"]["native_responses_actual_output_tokens"] == 1,
            "Gateway limitations are omitted")
    for row in gateway_rows:
        require(row["http_status"] == 200
                and 0 <= row["cached_input_tokens"] <= row["input_tokens"]
                and 0 <= row["client_first_progress_seconds"] <= row["client_total_seconds"]
                and math.isclose(row["client_output_tok_s_per_total_second"],
                                 row["output_tokens"] / row["client_total_seconds"], rel_tol=1e-12),
                "Gateway accounting differs")
    for model in serving["models"]:
        recipe = json.loads((REPO / "recipes" / model["recipe"] / "recipe.json").read_text())
        tested_pool = (json.loads((REPO / "data/apex-kv-capacity/evidence.json").read_text())["baseline_pool_tokens"]
                       if model["recipe"] == APEX_RECIPE else recipe["serving"]["kv"]["shared_gpu_pool_tokens"])
        require(model["request_context_tokens"] == recipe["serving"]["context_tokens"]
                and model["physical_request_slots"] == recipe["serving"]["max_requests"]
                and model["shared_gpu_kv_tokens"] == tested_pool,
                "Live serving geometry differs from recipe metadata")
        policy = policy_by_recipe[model["recipe"]]
        require(recipe["serving"]["kv"]["host_kv_budget_mib"] == policy["current_ram_kv_mib"] == 0
                and recipe["serving"]["kv"]["host_recurrent_budget_mib"]
                == policy["current_ram_recurrent_mib"] == 16384,
                "Current RAM policy differs from recipe settings")
        budget = policy["retained_measurement_ram_kv_mib"] * 2**20
        require(model["ram_kv_page_slots"] == budget // model["ram_kv_page_bytes"]
                and model["ram_kv_token_slots"] == model["ram_kv_page_slots"] * 256,
                "RAM KV token-slot arithmetic differs")
        for check in model["checks"]:
            require(check["submitted_requests"] == len(check["requests"]), "Live request count differs")
            for row in check["requests"]:
                require(row["http_status"] == 200 and row["error"] is None
                        and row["accepted_output_tokens"] > 0
                        and 0 <= row["client_first_progress_seconds"] <= row["client_total_seconds"],
                        "Live request did not complete with valid timing")
                require(math.isclose(row["client_output_tokens_per_total_second"],
                                     row["accepted_output_tokens"] / row["client_total_seconds"],
                                     rel_tol=1e-12), "Client throughput denominator differs")
            if check["workload"] == "oversubscribed_native_wave":
                require(check["submitted_requests"] == model["physical_request_slots"] + 2
                        and all(row["accepted_output_tokens"] == 1536 for row in check["requests"][:-1])
                        and check["requests"][-1]["accepted_output_tokens"] == 128,
                        "Occupied-slot test geometry differs")
                require(len(check["resumed_output_traces"]) == check["submitted_requests"]
                        and all(trace["status"] == "complete" and trace["counts_monotonic"]
                                for trace in check["resumed_output_traces"])
                        and check["cache_audit"]["page_table_valid"], "Resumed stream verification failed")
    notices = REPO / "runtimes/deepseek/overlay/vllm_exl3-0.4.2.dist-info/licenses"
    for name in ("LICENSE", "LICENSE.APACHE-2.0", "NOTICE", "THIRD_PARTY_NOTICES.md"):
        require((notices / name).is_file() and (notices / name).stat().st_size > 0,
                "Missing upstream plugin license/attribution: " + name)
    markdown = MarkdownIt("commonmark").enable("table")
    blocked = [r"-----BEGIN (?:OPENSSH |RSA |EC |DSA |ENCRYPTED )?PRIVATE KEY-----",
               r"\bgh[pousr]_[A-Za-z0-9]{25,}\b", r"\bgithub_pat_[A-Za-z0-9_]{40,}\b",
               r"\bhf_[A-Za-z0-9]{25,}\b", r"\b(?:AKIA|ASIA)[A-Z0-9]{16}\b",
               r"\bsk-(?:proj-|svcacct-)?[A-Za-z0-9_-]{25,}\b",
               r"/(?:home|srv|mnt|media)/[A-Za-z0-9_.-]+/", r"192\.168\.\d+\.\d+",
               r"GPU-[0-9a-fA-F]{8}-"]
    for p in public_files():
        if p.suffix == ".py":
            ast.parse(p.read_text(), filename=str(p.relative_to(REPO)))
        if p.suffix in {".py", ".md", ".json", ".csv", ".yml", ".yaml", ".patch", ".txt", ".sh"}:
            text = p.read_text()
            for pattern in blocked:
                require(not re.search(pattern,text), "Private material pattern in "+str(p.relative_to(REPO)))
            if p.suffix == ".md":
                for token in markdown.parse(text):
                    if token.children:
                        for child in token.children:
                            if child.type == "link_open":
                                dest = child.attrGet("href").split("#")[0]
                                if dest and ":" not in dest:
                                    require((p.parent / dest).exists(), "Broken Markdown link in "+str(p.relative_to(REPO))+": "+dest)
    tracked = subprocess.check_output(["git","ls-files"],cwd=REPO,text=True).splitlines()
    require(not any(p.startswith((".deploy/", ".local/")) for p in tracked), "Private local files are tracked")
    ignored = subprocess.run(["git","check-ignore",".deploy/id_ed25519",".deploy/id_ed25519.pub"],cwd=REPO,capture_output=True,text=True)
    require(ignored.returncode == 0 and len(ignored.stdout.splitlines()) == 2, "Deploy key ignore rules are missing")
    print(f"Validated {len(ids)} recipes, {total_points} benchmark waves, {historical_waves} historical Qwen waves, "
          f"{archived_profiles} detailed archived profiles / {archived_waves} Strata waves, "
          f"{history_records} historical records / {history_waves} retained waves, runtime payloads, licenses and public Markdown")


if __name__ == "__main__":
    try:
        validate()
    except (ValueError, OSError) as error:
        raise SystemExit(str(error))
