"""Validate per-request prefill recovered from native metric snapshots."""
import math
import re


HISTOGRAMS = ("prefill_seconds", "computed_prompt_tokens", "prompt_tokens", "output_tokens")


def recover_prefill(record):
    before, after = record["before"], record["after"]
    if before["labels"] != after["labels"]:
        raise ValueError("Metric labels changed")
    if not re.fullmatch(r"[0-9a-f]{64}", before["epoch_sha256"]) or before["epoch_sha256"] != after["epoch_sha256"]:
        raise ValueError("Metric epoch changed")
    if before["labels"].get("model_name") != record["model"]["served_name"]:
        raise ValueError("Metrics identify a different model")
    changes = {}
    for name in HISTOGRAMS:
        a, b = before[name], after[name]
        for row in (a, b):
            if not {"count", "sum"} <= row.keys() or any(not isinstance(row[key], (int, float)) or isinstance(row[key], bool)
                   or not math.isfinite(row[key]) or row[key] < 0 for key in ("count", "sum")):
                raise ValueError("Invalid native metric value")
            if row["count"] != int(row["count"]):
                raise ValueError("Nonintegral native request count")
        if b["count"] - a["count"] != 1 or b["sum"] < a["sum"]:
            raise ValueError("Expected exactly one completed request without a metric reset")
        changes[name] = b["sum"] - a["sum"]
    seconds = changes["prefill_seconds"]
    if seconds <= 0:
        raise ValueError("Native prefill duration is not positive")
    for name in HISTOGRAMS[1:]:
        if changes[name] != int(changes[name]):
            raise ValueError("Nonintegral token delta")
    computed, total, output = (int(changes[name]) for name in HISTOGRAMS[1:])
    if not 0 <= computed <= total or output <= 0:
        raise ValueError("Invalid prompt/output token accounting")
    expected = record["request"]
    if total != expected["input_tokens"] or output != expected["accepted_output_tokens"]:
        raise ValueError("Native metrics do not match the recorded request")
    counters = {}
    for name in ("prefix_queries", "prefix_hits"):
        a, b = before[name], after[name]
        if any(not isinstance(value, (int, float)) or isinstance(value, bool)
               or not math.isfinite(value) or value < 0 or value != int(value) for value in (a, b)) or b < a:
            raise ValueError("Invalid prefix counter")
        counters[name] = int(b - a)
    cached = total - computed
    if counters["prefix_queries"] != total or counters["prefix_hits"] != cached:
        raise ValueError("Native computed/cache counts do not match prefix counters")
    return {
        "request_count": 1,
        "input_tokens": total,
        "processed_prompt_tokens": computed,
        "cached_prompt_tokens": cached,
        "accepted_output_tokens": output,
        "backend_prefill_seconds": seconds,
        "prefill_tok_s": computed / seconds,
    }
