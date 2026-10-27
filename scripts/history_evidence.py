"""Select publishable aggregates from historical model experiment receipts."""
import math
import statistics


NUMERIC_UNITS = {
    "context_tokens": "tokens", "context_limit": "tokens", "context": "tokens",
    "resident_pool_tokens": "tokens", "maximum_resident_pool_tokens": "tokens",
    "actual_input_tokens": "tokens", "actual_long_request_prompt_tokens": "tokens",
    "actual_tokenizer_input": "tokens", "configured_slots": "requests",
    "input_tokens": "tokens", "prompt_tokens": "tokens", "output_tokens": "tokens",
    "completion_tokens": "tokens", "total_tokens": "tokens", "cached_tokens": "tokens",
    "compact_tokens": "tokens", "extension_cached_tokens": "tokens",
    "replayed_history_tokens": "tokens", "restored_external_prefix_tokens": "tokens",
    "restored_pages": "pages", "restored_page_images_on_return": "pages",
    "recurrent_restores": "checkpoints", "recurrent_restores_on_return": "checkpoints",
    "history_tokens": "tokens", "pool": "tokens", "cache_tokens": "tokens",
    "gpu_pool_tokens": "tokens", "reported_gpu_pool_tokens": "tokens",
    "ram_cache_tokens": "tokens", "ram_kv_page_image_tokens": "tokens",
    "stored_bytes_before_return": "bytes", "restored_bytes": "bytes",
    "held_bytes": "bytes", "allocated_bytes": "bytes", "reserved_bytes": "bytes",
    "peak_allocated_bytes": "bytes", "peak_reserved_bytes": "bytes", "free_bytes": "bytes",
    "host_peak_bytes": "bytes", "host_memory_peak_bytes": "bytes",
    "matched_workload_host_peak_bytes": "bytes", "host_cgroup_peak_bytes": "bytes",
    "managed_ram_peak_bytes": "bytes", "ram_peak_bytes": "bytes", "rss_peak_bytes": "bytes",
    "total_kv_bytes": "bytes", "total_recurrent_bytes": "bytes",
    "main_page_bytes": "bytes", "draft_page_bytes": "bytes", "paired_page_image_bytes": "bytes",
    "bytes_per_pooled_token": "bytes/token", "reserve_mib": "MiB",
    "planning_reserve_mib": "MiB", "additional_margin_MiB": "MiB",
    "request_count": "requests", "concurrency": "requests", "independent_histories": "histories",
    "elapsed_seconds": "s", "ttft_seconds": "s", "wall_seconds": "s",
    "return_wave_seconds": "s", "load_seconds": "s",
    "processed_prompt_tokens": "tokens", "cached_prompt_tokens": "tokens",
    "backend_prefill_seconds": "s", "prefill_tok_s": "tokens/s",
    "generated_tokens": "accepted tokens", "generation_seconds": "s",
    "generation_tps": "accepted tokens/s", "accepted_decode_tok_s": "accepted tokens/s",
    "generated_only_tok_s": "accepted tokens/s", "generated_tok_s": "accepted tokens/s",
    "aggregate_generated_tok_s": "accepted tokens/s", "generated_tps": "accepted tokens/s",
    "end_to_end_accepted_tok_s": "accepted tokens/s", "end_to_end_output_tps": "accepted tokens/s",
    "cold_TTFT_median_seconds": "s", "median_TTFT_seconds": "s",
    "p50_inter_token_ms": "ms", "p95_inter_token_ms": "ms",
    "accepted": "draft tokens", "proposed": "draft tokens", "ratio": "fraction",
    "native_MTP_accepted_draft_tokens": "draft tokens", "accepted_draft_tokens_per_step": "tokens/step",
    "MTP_actual_storage_bits": "bits", "through_batch": "batches",
    "completed_destinations": "destinations", "task_count": "tasks",
}

FLAGS = {
    "passed", "complete", "complete_answers", "all_answers_complete", "all_complete_answers",
    "all_submitted_tasks_evaluated", "complete_checked_answers", "thinking_closed",
    "bounded_model_answers", "actual_serving_evaluation", "generated_code_isolated",
    "compares_specific_checkpoints_and_backends", "isolated_quantization_quality_claimed",
    "task_count_is_not_broad_quality_evidence", "fixed_output_performance_workload",
    "complete_answer_quality_test", "quality_gain_demonstrated", "quality_gain_assessed_from_tasks",
    "context_smoke_passed", "capacity_smoke_passed", "stable_pool_smoke_passed",
    "exact_boundary_measured", "capacity_boundary_measured", "cache_boundary_measured",
    "final_maximum_context_concurrent_pressure_passed", "peak_prefill_and_concurrency_passed",
    "maximum_pool_pressure_pending", "quality_and_context_not_inferred_from_fit",
    "useful_long_context_retrieval", "history_restoration_tested", "history_restoration_answer_matched",
    "retention_pressure_tested", "RAM_return_qualified", "ram_restoration_qualified",
    "all_four_spaced_fact_sums_correct", "coding_tools_thinking_passed",
    "eight_bit_serving_KV_verified", "eight_bit_verified", "native_MTP_acceptance_observed",
    "matched_greedy_target_reference", "matched_checked_target_answers",
    "identical_prompts_and_sampling", "tool_call_and_result_roundtrip",
    "trace_final_tokens_match_usage", "API_token_totals_verified", "cache_hit_verified",
    "schema_and_values_correct", "candidate_IDs_scores_and_selector_matched",
    "full_Apex_equivalence_qualified", "concurrent_generated_only_rate_qualified",
    "strict_token_parity_not_required", "ordinary_speculative_correctness_qualified",
    "FP32_reference", "TF32_enabled", "actual_GPU_outputs", "CPU_only_analysis",
    "all_logits_finite", "coverage_is_not_quality_evidence", "applies_to_current_refit",
    "offset_detach_reload_passed", "saved_reload_passed", "partial_task_group",
    "target_model_TP_integration_still_requires_matched_checks",
}

USAGE_FIELDS = {
    "prompt_tokens", "completion_tokens", "total_tokens", "prompt_time", "prompt_tokens_per_sec",
    "completion_time", "completion_tokens_per_sec", "total_time",
}
TIMING_FIELDS = {
    "cache_n", "prompt_n", "prompt_ms", "prompt_per_token_ms", "prompt_per_second",
    "predicted_n", "predicted_ms", "predicted_per_token_ms", "predicted_per_second",
    "draft_n", "draft_n_accepted",
}
FINISH_REASONS = {"stop", "length", "tool_calls", "cancelled", "eos", "max_tokens"}
CATEGORIES = {"coding", "tool", "agent", "reasoning", "multi_step_agent", "tool_format"}
OUTCOMES = {"pass", "passed", "fail", "failed", "partial", "blocked", "skipped", "completed",
            "complete", "not_run", "pending", "unsupported", "error", "timeout", "oom", "success"}


def finite_number(value):
    return type(value) in (int, float) and math.isfinite(value)


def numeric_value(value):
    if finite_number(value):
        return value
    if isinstance(value, list) and value and all(finite_number(child) for child in value):
        return value
    return None


def numeric_selection(value, keys):
    return {key: selected for key in sorted(keys & value.keys())
            if (selected := numeric_value(value[key])) is not None}


def flags(value):
    return {key: value[key] for key in sorted(FLAGS & value.keys()) if type(value[key]) is bool}


def request_metrics(value):
    """Usage and timers only: never copy messages, generated text or token IDs."""
    result = numeric_selection(value, {"elapsed_seconds", "ttft_seconds"})
    usage = value.get("usage") or {}
    if isinstance(usage, dict):
        result["usage"] = numeric_selection(usage, USAGE_FIELDS)
        for name in ("prompt_tokens_details", "completion_tokens_details"):
            details = usage.get(name) or {}
            if isinstance(details, dict):
                selected = numeric_selection(details, {"cached_tokens", "reasoning_tokens",
                                                        "accepted_prediction_tokens", "rejected_prediction_tokens"})
                if selected:
                    result["usage"][name] = selected
    timings = value.get("timings") or {}
    if isinstance(timings, dict):
        result["timings"] = numeric_selection(timings, TIMING_FIELDS)
    generation = value.get("generation") or {}
    if isinstance(generation, dict):
        result["generation"] = numeric_selection(generation, {"generated_tokens", "generation_seconds", "generation_tps"})
    if value.get("finish_reason") in FINISH_REASONS:
        result["finish_reason"] = value["finish_reason"]
    if type(value.get("cancelled")) is bool:
        result["cancelled"] = value["cancelled"]
    return {key: child for key, child in result.items() if child != {}}


def quality_metrics(value):
    """Retain grades and their denominators without the evaluated tasks or answers."""
    if type(value.get("passed")) is not int or type(value.get("total")) is not int:
        return None
    result = {"passed": value["passed"], "total": value["total"], "flags": flags(value),
              "categories": {}, "samples": []}
    for index, task in enumerate(value.get("tasks") or []):
        if not isinstance(task, dict):
            continue
        row = {"sample_index": index}
        if task.get("category") in CATEGORIES:
            row["category"] = task["category"]
        grade = task.get("grade") or {}
        passed = grade.get("passed") if isinstance(grade, dict) else None
        passed = task.get("passed") if type(task.get("passed")) is bool else passed
        if type(passed) is bool:
            row["passed"] = passed
        original = task.get("original_grade") or {}
        if isinstance(original, dict) and type(original.get("passed")) is bool:
            row["original_grade_passed"] = original["passed"]
        for key in ("truncated",):
            if type(task.get(key)) is bool:
                row[key] = task[key]
        for key in ("output_limit", "returncode"):
            if type(task.get(key)) is int:
                row[key] = task[key]
        request = task.get("original_result") or task.get("result")
        if isinstance(request, dict):
            row["request"] = request_metrics(request)
        result["samples"].append(row)
    for category, score in (value.get("categories") or {}).items():
        if category not in CATEGORIES:
            continue
        if isinstance(score, dict) and type(score.get("passed")) is int and type(score.get("total")) is int:
            result["categories"][category] = {"passed": score["passed"], "total": score["total"],
                                               "denominator_source": "reported"}
        elif type(score) is int:
            count = sum(row.get("category") == category for row in result["samples"])
            result["categories"][category] = {"passed": score, "total": count or None,
                                               "denominator_source": "retained_task_categories" if count else "unavailable"}
    times = [row["request"]["elapsed_seconds"] for row in result["samples"]
             if finite_number(row.get("request", {}).get("elapsed_seconds"))]
    if times:
        result["task_total_latency_seconds"] = {"count": len(times), "minimum": min(times),
                                                 "median": statistics.median(times), "maximum": max(times)}
    if finite_number(value.get("latency")):
        result["reported_task_latency_median_seconds"] = value["latency"]
    return result


def numerical_metrics(value):
    result = {"values": numeric_selection(value, set(NUMERIC_UNITS)), "flags": flags(value)}
    for key in ("inter_token_latency",):
        if isinstance(value.get(key), dict):
            selected = numeric_selection(value[key], {"p50_ms", "p95_ms"})
            if selected:
                result[key] = selected
    for key in ("cold_prefill", "prefill"):
        if isinstance(value.get(key), list):
            rows = [numeric_selection(row, {"processed_prompt_tokens", "cached_prompt_tokens",
                                            "backend_prefill_seconds", "prefill_tok_s"})
                    for row in value[key] if isinstance(row, dict)]
            if any(rows):
                result[key] = rows
    if isinstance(value.get("draft_acceptance"), dict):
        selected = numeric_selection(value["draft_acceptance"], {"accepted", "proposed", "ratio"})
        if selected:
            result["draft_acceptance"] = selected
    for key in ("cache_bytes",):
        if isinstance(value.get(key), dict):
            selected = numeric_selection(value[key], {"main", "draft"})
            if selected:
                result[key] = selected
    for key in ("per_card_peak_used_MiB",):
        if isinstance(value.get(key), dict) and all(finite_number(child) for child in value[key].values()):
            result[key + "_unordered"] = sorted(value[key].values())
    for key in ("allocator_reserved_GiB", "free_GiB", "peak_total_GiB"):
        selected = numeric_value(value.get(key))
        if selected is not None:
            result[key] = selected
    if isinstance(value.get("usage"), dict):
        result["request"] = request_metrics(value)
    if isinstance(value.get("responses"), list):
        rows = [request_metrics(row) for row in value["responses"] if isinstance(row, dict)]
        if any(rows):
            result["response_metrics"] = rows
    if isinstance(value.get("long_and_small_requests"), list):
        result["long_and_small_requests"] = [request_metrics(row) for row in value["long_and_small_requests"]
                                                if isinstance(row, dict)]
    if isinstance(value.get("restored_request"), dict):
        result["restored_request"] = request_metrics(value["restored_request"])
    batches = {}
    for key in ("cold", "warm", "burst", "cases"):
        rows = value.get(key)
        if isinstance(rows, list) and rows and all(isinstance(row, dict) and isinstance(row.get("usage"), dict) for row in rows):
            batches[key] = [dict(request_metrics(row), check_flags=flags(row)) for row in rows]
    if batches:
        result["request_batches"] = batches
    # Error text can contain prompts, paths and addresses; publish only its presence.
    if value.get("error"):
        result["error_present"] = True
    for key in ("status", "outcome", "result"):
        if isinstance(value.get(key), str) and value[key].lower() in OUTCOMES:
            result["reported_" + key] = value[key].lower()
    return {key: child for key, child in result.items() if child != {} and child != []}
