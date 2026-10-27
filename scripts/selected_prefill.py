"""Recompute the selected-serving comparison from numerical evidence only."""
import math
import statistics

from native_prefill import recover_prefill

COHORT = "selected-serving-native-prefill"
MATRIX = {"qwen3.8-27b-exl3": 8, "apex-abliterated-awq-dflash2-pp3-balanced": 4,
          "deepseek-v41-flash-dspark5-tp3": 4}


def common_decode(traces):
    if not traces or len({row["label"] for row in traces}) != len(traces):
        raise ValueError("Missing or duplicate numerical traces")
    for trace in traces:
        if (trace["status"] != "complete" or trace.get("truncated") or trace.get("requeued")
                or trace["clock"] != "CLOCK_MONOTONIC" or trace["generated_tokens"] != 256
                or not trace["events"]):
            raise ValueError("Incomplete or invalid accepted-token trace")
        last_time, last_count = -math.inf, -1
        for timestamp, count, prefill in trace["events"]:
            if (type(timestamp) is not int or timestamp <= last_time
                    or type(count) is not int or not last_count <= count <= 256
                    or type(prefill) is not bool):
                raise ValueError("Non-monotonic or malformed accepted-token event")
            last_time, last_count = timestamp, count
        if last_count != 256 or last_time > trace["finished_ns"]:
            raise ValueError("Trace final count/time differs from completion")
    start = max(row["first_generation_ns"] for row in traces)
    end = min(row["finished_ns"] for row in traces)
    seconds = (end - start) / 1e9
    if seconds < .5:
        raise ValueError("No qualified common generation interval")
    per_request = []
    for trace in traces:
        if any(prefill and start < timestamp < end for timestamp, _, prefill in trace["events"]):
            raise ValueError("Prefill overlapped the common generation interval")
        if any(a < end and b > start for a, b in trace.get("prefill_spans", [])):
            raise ValueError("A native prefill span overlapped the common generation interval")
        baseline = max((count for stamp, count, _ in trace["events"] if stamp <= start), default=0)
        final = max((count for stamp, count, _ in trace["events"] if stamp < end), default=baseline)
        per_request.append(final - baseline)
    total = sum(per_request)
    if total <= 0:
        raise ValueError("No accepted tokens inside the common interval")
    return {"seconds": seconds, "accepted_tokens": total, "tok_s": total / seconds,
            "per_request_tokens": per_request, "per_request_tok_s": [count / seconds for count in per_request]}


def validate_dataset(data, recipes):
    if data["cohort"] != COHORT or data["sampling"] != {
            "input_target_tokens": 32768, "input_tolerance_tokens": 64,
            "accepted_output_tokens": 256, "temperature": 0, "seed": 20261008,
            "reasoning_effort": "low", "ignore_eos": True, "min_tokens": 256}:
        raise ValueError("Comparison protocol differs")
    seen = set()
    for cohort in data["cohorts"]:
        ident = cohort["recipe"]
        if ident not in MATRIX or ident in seen:
            raise ValueError("Unexpected or duplicate recipe cohort")
        seen.add(ident)
        recipe = recipes[ident]
        if cohort["model"] != recipe["model"]:
            raise ValueError("Comparison artifact identity differs")
        if {row["concurrency"] for row in cohort["points"]} != {1, MATRIX[ident]} or len(cohort["points"]) != 2:
            raise ValueError("Missing matching C1/concurrent comparison")
        for point, evidence in zip(cohort["points"], cohort["wave_evidence"]):
            count = point["concurrency"]
            if (point["cohort"] != COHORT or not point["headline_eligible"]
                    or point["test_configuration"] != cohort["configuration"]
                    or point["test_configuration"]["ram_kv_mib"] != 0
                    or len(point["requests"]) != count
                    or len(evidence["traces"]) != count
                    or evidence["measurement_id"] != point["measurement_id"]):
                raise ValueError("Comparison configuration or request count differs")
            for request in point["requests"]:
                if (abs(request["usage"]["prompt_tokens"] - 32768) > 64
                        or request["usage"]["completion_tokens"] != 256
                        or request["cached_prompt_tokens"] != 0):
                    raise ValueError("Comparison prompt/output/cache accounting differs")
            first_tokens = [request["ttft_seconds"] for request in point["requests"]]
            if (statistics.median(first_tokens) != point["ttft_median_seconds"]
                    or max(first_tokens) != point["ttft_slowest_seconds"]
                    or count * 256 / point["elapsed_seconds"] != point["end_to_end_accepted_tok_s"]):
                raise ValueError("Client latency or whole-wave throughput differs")
            draft = point.get("draft_counter_evidence")
            if draft is not None:
                proposed = draft["after"]["draft_tokens"] - draft["before"]["draft_tokens"]
                accepted = draft["after"]["accepted_tokens"] - draft["before"]["accepted_tokens"]
                if (not 0 <= accepted <= proposed or proposed != point["draft_tokens_proposed"]
                        or accepted != point["draft_tokens_accepted"]):
                    raise ValueError("Draft counters differ from reported acceptance")
            before, after = evidence["native_metric_before"], evidence["native_metric_after"]
            if before is not None:
                if before["labels"] != after["labels"] or before["epoch_sha256"] != after["epoch_sha256"]:
                    raise ValueError("Native metric identity changed")
                expected = {"prompt_tokens": sum(r["usage"]["prompt_tokens"] for r in point["requests"]),
                            "computed_prompt_tokens": sum(r["usage"]["prompt_tokens"] for r in point["requests"]),
                            "output_tokens": count * 256}
                for name, total in expected.items():
                    if after[name]["count"] - before[name]["count"] != count or after[name]["sum"] - before[name]["sum"] != total:
                        raise ValueError("Native request/token histogram accounting differs")
                if (after["prefix_hits"] != before["prefix_hits"]
                        or after["prefix_queries"] - before["prefix_queries"] != expected["prompt_tokens"]):
                    raise ValueError("Native counters do not establish cold input")
            measured = common_decode(evidence["traces"])
            if (measured["seconds"] != point["shared_decode_interval_seconds"]
                    or measured["accepted_tokens"] != point["shared_decode_accepted_tokens"]
                    or measured["tok_s"] != point["decode_tok_s_aggregate"]
                    or measured["per_request_tok_s"] != point["decode_tok_s_per_request"]):
                raise ValueError("Comparison decode values differ from numerical traces")
            if count == 1:
                native = point["backend_prefill_per_request"][0]
                if evidence["native_metric_before"] is not None:
                    recovered = recover_prefill({"before": evidence["native_metric_before"],
                        "after": evidence["native_metric_after"], "model": cohort["model"],
                        "request": {"input_tokens": point["requests"][0]["usage"]["prompt_tokens"],
                                    "accepted_output_tokens": 256}})
                    if (recovered["backend_prefill_seconds"] != native["backend_prefill_seconds"]
                            or recovered["processed_prompt_tokens"] != native["processed_prompt_tokens"]):
                        raise ValueError("Comparison prefill differs from native histogram")
                else:
                    timings = point["requests"][0]["timings"]
                    if (timings["prompt_ms"] / 1000 != native["backend_prefill_seconds"]
                            or timings["prompt_n"] != native["processed_prompt_tokens"]):
                        raise ValueError("Comparison prefill differs from backend timer")
                rate = native["processed_prompt_tokens"] / native["backend_prefill_seconds"]
                if (rate != native["prefill_tok_s"]
                        or rate != point["backend_prefill_tok_s_per_request_median"]):
                    raise ValueError("Comparison prefill rate does not reproduce")
    for observation in data.get("additional_observations", []):
        traces = observation["traces"]
        if (observation["request_count"] != len(traces) or len(traces) != 8
                or observation["aggregate_shared_decode_tok_s"] is not None
                or observation["shared_decode_valid"]):
            raise ValueError("Additional observation claims an unsupported aggregate")
        try:
            common_decode(traces)
        except ValueError as error:
            if str(error) != "No qualified common generation interval":
                raise
        else:
            raise ValueError("Claimed absence of a common interval does not reproduce")
        seconds = (min(t["finished_ns"] for t in traces) - max(t["first_generation_ns"] for t in traces)) / 1e9
        if seconds != observation["common_interval_seconds"]:
            raise ValueError("Additional interval boundaries differ")
    return {"completed_recipes": len(seen), "completed_waves": 2 * len(seen),
            "remaining_recipes": sorted(set(MATRIX) - seen)}
