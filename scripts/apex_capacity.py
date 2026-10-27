"""Verify the saved Apex KV geometry against retained numerical receipts."""
import argparse
import hashlib
import json
import math
from pathlib import Path
import statistics

RECIPE = "apex-abliterated-exl3-mtp1-tp3"
DATA = Path("data/apex-kv-capacity")


def require(condition, message):
    if not condition:
        raise ValueError(message)


def derive_capacity(root):
    directory = Path(root) / DATA
    read = lambda name: json.loads((directory / name).read_text())
    sources = read("source-verification.json")
    require(sources["passed"], "Source readback did not pass")
    for record in sources["files"]:
        raw = (directory / record["file"]).read_bytes()
        require(len(raw) == record["bytes"]
                and hashlib.sha256(raw).hexdigest() == record["sha256"],
                "Source identity differs: " + record["file"])
    saved, baseline, report = (read(name) for name in (
        "saved-profile.json", "baseline-profile.json", "qualification-report.json"))
    by_hash = {record["original_sha256"]: record["file"] for record in sources["files"]}

    def referenced(reference):
        require(reference["sha256"] in by_hash, "Missing numerical source receipt")
        return read(by_hash[reference["sha256"]])

    require(report["passed"] and not report["model_input_output_retained"],
            "Qualification failed or retains model input/output")
    require(by_hash.get(report["original_profile"]["sha256"]) == "baseline-profile.json",
            "Baseline profile identity differs")
    trial = referenced(report["tested_profile"])
    geometry = ("model", "revision", "context", "cache_tokens", "cache_mode",
                "draft_cache_mode", "max_sessions", "chunk_size", "draft_mode",
                "draft_tokens", "dynamic_draft", "parallelism", "main_reserve_mib_by_uuid")
    require(all(saved[key] == trial[key] for key in geometry),
            "Saved profile differs from the qualified trial")
    require(saved["cache_tokens"] == report["validated_pool_tokens"] == 1374976
            and baseline["cache_tokens"] == report["original_pool_tokens"] == 1083136,
            "Unexpected qualified or baseline pool")
    require(saved["context"] == report["preserved_context"] == 524288
            and saved["max_sessions"] == report["preserved_slots"] == 4
            and saved["draft_tokens"] == report["preserved_mtp_tokens"] == 1
            and saved["dynamic_draft"] is report["preserved_dynamic_draft"] is False
            and saved["cache_mode"] == saved["draft_cache_mode"]
            == report["main_and_draft_cache"] == "Q8",
            "Context, slots, speculation or cache precision differs")
    gain = saved["cache_tokens"] - baseline["cache_tokens"]
    gain_percent = 100 * gain / baseline["cache_tokens"]
    require(gain == report["gain_tokens"]
            and math.isclose(gain_percent, report["gain_percent"], rel_tol=1e-12),
            "KV capacity increase arithmetic differs")
    baseline_performance = referenced(report["baseline_performance"])
    loads, performance = [], []
    ordered_reserves = None
    for observation in report["independent_loads"]:
        lifecycle = referenced(observation["lifecycle"])
        full = referenced(observation["qualification"])
        require(lifecycle["passed"] and full["passed"]
                and lifecycle["current_job"] == full["before"]["job_id"] == observation["job_id"]
                and lifecycle["tested_profile_sha256"] == report["tested_profile"]["sha256"],
                "Independent load or profile binding differs")
        require(all(phase["passed"] for phase in full["phases"]),
                "A qualification phase failed")
        state = full["before"]
        require(state["cache"]["max_tokens"] == saved["cache_tokens"]
                and state["context"] == saved["context"]
                and state["max_batch_size"] == saved["max_sessions"]
                and state["draft_tokens"] == 1 and state["dynamic_draft"] is False,
                "Loaded geometry differs from the saved profile")
        checks = full["checks"]
        smoke, mixed, near, pressure = (checks[key] for key in ("smoke", "mixed", "near", "pressure"))
        require(all(smoke[key] is True for key in ("arithmetic", "tool_call", "tool_result", "cancellation")),
                "Smoke, tool continuation or cancellation failed")
        require(mixed["output_chunk_boundary_crossed"]
                and mixed["output_boundary_slots_verified"] == 4
                and mixed["mixed_answers_verified"] and mixed["long_generation_output_verified"]
                and mixed["mixed_prefill_steps_delta"] > 0, "Mixed prefill/decode or output growth failed")
        require(near["retrieval_verified"] and near["context"] == 524288
                and near["concurrent_companions"] == 3, "Near-context retrieval failed")
        fraction = pressure["distinct_prompt_tokens"] / saved["cache_tokens"]
        require(fraction > .95 and math.isclose(fraction, pressure["pool_fraction"], rel_tol=1e-12)
                and pressure["active_slots_highwater"] == 4
                and len(pressure["retrieval_verified"]) == 4
                and all(pressure["retrieval_verified"])
                and pressure["prefix_reuse_verified"] and pressure["recurrent_restores_delta"] >= 4
                and pressure["cache_audit_after_reuse"]["page_table_valid"],
                "Distinct-history pressure or recurrent-prefix reuse failed")
        memory = observation["memory"]
        require(memory["physical_free_guard_passed"] and memory["sampling_continuous"]
                and memory["covers_interval"] and memory["all_records_cover_selected_gpus"]
                and memory["started_at"] <= full["started_at"]
                and memory["ended_at"] >= full["ended_at"], "Physical-memory interval is unqualified")
        devices = lifecycle["launch"]["gpu_selection"]["devices"]
        reserves = [saved["main_reserve_mib_by_uuid"][device["uuid"]] for device in devices]
        require(reserves == [2560, 2336, 2848], "Qualified GPU-rank reserve order differs")
        require(ordered_reserves in (None, reserves), "Independent placements differ")
        ordered_reserves = reserves
        physical = [memory["gpus"][str(index)] for index in report["gpu_indices"]]
        require(len(physical) == len(devices) == 3
                and all(row["uuid"] == device["uuid"] for row, device in zip(physical, devices))
                and all(row["min_free_bytes"] >= report["physical_margin_mib_required"] * 2**20
                        and row["max_used_bytes"] + row["min_free_bytes"] == row["total_bytes"] == 64 * 2**30
                        for row in physical), "Physical free-memory guard or device identity differs")
        cache = observation["cache"]
        require(sum(cache["component_bytes"].values()) == cache["total_bytes"]
                == saved["cache_tokens"] * cache["bytes_per_token"], "KV payload arithmetic differs")
        replay = observation.get("resident_decode_replay")
        replay_summary = None
        if replay:
            followup = referenced(replay["qualification"])
            replay_pressure = followup["checks"]["pressure"]
            require(followup["passed"] and followup["before"]["job_id"] == observation["job_id"]
                    and replay_pressure["distinct_prompt_tokens"] == pressure["distinct_prompt_tokens"]
                    and replay_pressure["repeated_min_output_tokens"] >= 256
                    and replay_pressure["repeated_decode_overlap_seconds"] > 0
                    and replay_pressure["prefix_reuse_verified"]
                    and all(replay_pressure["retrieval_verified"]), "Resident decode replay failed")
            replay_summary = {key: replay_pressure[key] for key in (
                "repeated_min_output_tokens", "repeated_decode_overlap_seconds", "prefix_reused_tokens")}
        for point in checks["perf"]["waves"]:
            prior = next(row for row in baseline_performance["checks"]["perf"]["waves"]
                         if (row["prompt_target"], row["concurrency"])
                         == (point["prompt_target"], point["concurrency"]))
            rate = lambda wave: statistics.median(request["usage"]["completion_tokens_per_sec"]
                                                  for request in wave["requests"])
            before, after = rate(prior), rate(point)
            performance.append(dict(prompt_tokens=point["prompt_target"], concurrency=point["concurrency"],
                baseline_per_request_median_tps=before, trial_per_request_median_tps=after,
                change_percent=100 * (after / before - 1), trial_job=observation["job_id"]))
        loads.append(dict(job_id=observation["job_id"], qualification=observation["qualification"],
            lifecycle=observation["lifecycle"], context_input_tokens=near["prompt_tokens"],
            distinct_history_input_tokens=pressure["distinct_prompt_tokens"], pool_fraction=fraction,
            active_slots=pressure["active_slots_highwater"], prefix_reused_tokens=pressure["prefix_reused_tokens"],
            recurrent_restores=pressure["recurrent_restores_delta"],
            all_qualification_phases_passed=True, tool_round_trip=True, cancellation=True,
            mixed_prefill_decode=True, output_growth_slots=mixed["output_boundary_slots_verified"],
            physical_min_free_bytes_by_rank=[row["min_free_bytes"] for row in physical],
            physical_peak_occupied_bytes_by_rank=[row["max_used_bytes"] for row in physical],
            cache_payload_bytes=cache, resident_decode_replay=replay_summary))
    require(len(loads) == len({load["job_id"] for load in loads}) == 2, "Expected two independent loads")
    supplied = report["performance_comparison"]["rows"]
    fields = ("prompt_tokens", "concurrency", "baseline_per_request_median_tps",
              "trial_per_request_median_tps", "change_percent", "trial_job")
    require(len(supplied) == len(performance) == 8
            and all(any(all(math.isclose(row[key], other[key], abs_tol=1e-10)
                            if isinstance(row[key], (int, float)) else row[key] == other[key]
                            for key in fields) for other in performance) for row in supplied),
            "Completion-rate probe transcription differs")
    return dict(format_version=1, recipe=RECIPE, resident_pool_tokens=saved["cache_tokens"],
        baseline_pool_tokens=baseline["cache_tokens"], increase_tokens=gain, increase_percent=gain_percent,
        context_tokens=saved["context"], slots=4, main_cache="Q8", draft_cache="Q8",
        mtp_depth=1, adaptive_mtp=False, autosplit_reserve_mib_by_selected_rank=ordered_reserves,
        independent_loads=loads, physical_free_guard_mib=report["physical_margin_mib_required"],
        measured_boundary_is_exhaustive=False, portable_export_gpu_requalified=False,
        timing_scope="Capacity qualification; retained headline throughput belongs to its earlier test geometry. Later backend completion-rate probes use a different timer and are not a synchronized aggregate.",
        performance_probes=performance)


def verify_capacity(root):
    root = Path(root)
    expected = derive_capacity(root)
    actual = json.loads((root / DATA / "evidence.json").read_text())
    require(actual == expected, "Capacity evidence differs from the retained source receipts")
    current = root / "data/current-recipe-settings.json"
    recipe = (next(recipe for recipe in json.loads(current.read_text())["recipes"] if recipe["id"] == RECIPE)
              if current.exists() else json.loads((root / "recipes" / RECIPE / "recipe.json").read_text()))
    require(recipe["serving"]["kv"]["shared_gpu_pool_tokens"] == actual["resident_pool_tokens"]
            and recipe["engine_config"]["model"]["cache_size"] == actual["resident_pool_tokens"]
            and recipe["engine_config"]["model"]["autosplit_reserve"]
            == actual["autosplit_reserve_mib_by_selected_rank"]
            and recipe["engine_config"]["draft_model"]["dynamic_draft"] is False,
            "Exported recipe differs from the qualified capacity or placement")
    return dict(passed=True, independent_loads=2, source_files=10, resident_pool_tokens=actual["resident_pool_tokens"],
                distinct_history_pool_fractions=[load["pool_fraction"] for load in actual["independent_loads"]])


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--write", action="store_true", help="Regenerate the derived numerical evidence")
    args = parser.parse_args()
    if args.write:
        (args.root / DATA / "evidence.json").write_text(json.dumps(derive_capacity(args.root), indent=2) + "\n")
    else:
        print(json.dumps(verify_capacity(args.root), indent=2))
