# apex-awq-dflash2-3-pp3-balanced-171513

**Historical record. Additional test results; no matched decode wave.**

Model family: Apex Flash 1 (GLM 5.3 Flash post-train).

The campaign inventory recorded status `completed`. The evidence sections retain any later results separately.

Historical configurations are provided for comparison. The [recommended recipes](../../../README.md) include supported launch scripts.

## Saved Configuration Versions

No exact serving configuration is retained with this summary. Its values are not assigned to another profile.

## Retained Measurements

No detailed benchmark receipt is matched to this record. A saved definition or a successful job exit alone is not a performance measurement.

A dash in shared decode means no qualified synchronized interval is available. Whole-wave throughput includes prefill and queueing. A valid decode interval can survive inside an overall failed or partial check; the source-report outcome is preserved. No rows are averaged.

## Additional Test Results

| Result / Source | Profile | Evidence type | Reported outcome | Retained values | Configuration binding |
| --- | --- | --- | --- | --- | --- |
| [result-4f03d48f8d3f80e8c49d](../observations.json)<br>source-e55a92a1742e783d94e9e8c3.json<br>`/experiments/28/contexts/0` | [apex-awq-dflash2-3-pp3-balanced-171513](apex-awq-dflash2-3-pp3-balanced-171513.md) | context allocation | Outcome unspecified | context_tokens=524,288 tokens | Exact configuration unresolved |
| [result-604ab460635c9973a18a](../observations.json)<br>source-e55a92a1742e783d94e9e8c3.json<br>`/experiments/28/speed/1` | [apex-awq-dflash2-3-pp3-balanced-171513](apex-awq-dflash2-3-pp3-balanced-171513.md) | performance detail | Outcome unspecified | cold_TTFT_median_seconds=65.92 s; configured_slots=4 requests; output_tokens=256 tokens; p50_inter_token_ms=30.73 ms; p95_inter_token_ms=93.03 ms; prompt_tokens=32,766 tokens; Draft accepted / proposed: 650.00 / 1,113.00 tokens; fraction 0.5840 | Exact configuration unresolved |
| [result-844449730cb457d2be73](../observations.json)<br>source-e55a92a1742e783d94e9e8c3.json<br>`/experiments/28/independently_maximized_config` | [apex-awq-dflash2-3-pp3-balanced-171513](apex-awq-dflash2-3-pp3-balanced-171513.md) | test outcome | Outcome unspecified | context=524,288 tokens | Exact configuration unresolved |
| [result-9c424be0849a9f7c5b82](../observations.json)<br>source-e55a92a1742e783d94e9e8c3.json<br>`/experiments/28` | [apex-awq-dflash2-3-pp3-balanced-171513](apex-awq-dflash2-3-pp3-balanced-171513.md) | context allocation | completed | matched_workload_host_peak_bytes=78,699,196,416 bytes; resident_pool_tokens=1,400,157 tokens; per_card_peak_used_MiB_unordered=64,056.00<br>64,650.00<br>64,657.00; capacity_boundary_measured=false; peak_prefill_and_concurrency_passed=false | Exact configuration unresolved |
| [result-cea28ee02ed41ccadd09](../observations.json)<br>source-d483a94cc2fdbf31ec4c2f97.json<br>`/correctness` | [apex-awq-dflash2-3-pp3-balanced-171513](apex-awq-dflash2-3-pp3-balanced-171513.md) | correctness check | Pass | 4 response usage/timing records | Exact configuration unresolved |
| [result-dbfaca33ec84fcdc18c1](../observations.json)<br>source-e55a92a1742e783d94e9e8c3.json<br>`/experiments/28/speed/0` | [apex-awq-dflash2-3-pp3-balanced-171513](apex-awq-dflash2-3-pp3-balanced-171513.md) | performance detail | Outcome unspecified | cold_TTFT_median_seconds=16.33 s; configured_slots=4 requests; output_tokens=256 tokens; p50_inter_token_ms=25.98 ms; p95_inter_token_ms=55.13 ms; prompt_tokens=32,765 tokens; Draft accepted / proposed: 152.00 / 312.00 tokens; fraction 0.4872 | Exact configuration unresolved |

These are saved result records, including failures and bounded checks. Copies, individual requests, report summaries and regrading can overlap; their counts are not independent test repetitions. Open each result for exact values, units, configuration binding and source receipts.

[Full archive](../../README.md) | [All retained waves](../RESULTS.md) | [Data definitions](../DATA.md) | [Recommended recipes](../../../README.md)
