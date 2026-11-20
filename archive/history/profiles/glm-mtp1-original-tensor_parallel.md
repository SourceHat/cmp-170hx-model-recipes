# glm-mtp1-original-tensor_parallel

**Historical record. Additional test results; no matched decode wave.**

Model family: GLM 5.3 Flash.

The campaign inventory recorded status `completed`. The evidence sections retain any later results separately.

Historical configurations are provided for comparison. The [recommended recipes](../../../README.md) include supported launch scripts.

Current recipes using the same recorded checkpoint repository: [glm-5.3-flash-mtp1-tp3](../../../recipes/glm-5.3-flash-mtp1-tp3/README.md). Context, cache and runtime versions can differ.

## Saved Configuration Versions

Each configuration ID identifies a distinct original settings record. Deployment fields are omitted; versions can have identical published settings after that omission. Upstream runtime commits remain unspecified where the source retained only an integration label.

| Configuration | Recorded artifact / source | Configured card counts | Context tokens | GPU pool tokens | Slots | Draft mode / tokens |
| --- | --- | --- | --- | --- | --- | --- |
| cfg-5f69d74b8ac050febea5 | [turboderp/GLM-5.3-Flash-exl3@2a30229e67](https://huggingface.co/turboderp/GLM-5.3-Flash-exl3/tree/2a30229e67012798ba9f0cd832bb78abf4c363d5) | 3 | 262,144 | 262,144 | 4 | mtp / 1 |

Card counts are saved configuration choices, not a claim that every allowed placement was measured. A derived view can differ from its pinned download source.

<details>
<summary>cfg-5f69d74b8ac050febea5</summary>

```json
{
  "kind": "tabby",
  "gpu_counts": [
    3
  ],
  "context": 262144,
  "cache_tokens": 262144,
  "cache_mode": "Q8",
  "draft_cache_mode": "Q8",
  "draft_mode": "mtp",
  "draft_tokens": 1,
  "max_sessions": 4,
  "chunk_size": 512,
  "reserve_mib": 2048,
  "ram_kv_mib": 8192,
  "ram_recurrent_mib": 16384,
  "dynamic_draft": false,
  "output_chunk_tokens": 4096,
  "power_watts": 200,
  "host_memory_gib": 80,
  "host_swap_gib": 0,
  "min_vram_mib_per_gpu": 65530,
  "min_effective_vram_mib": 196590,
  "parallelism": "tensor_parallel",
  "transport": "host",
  "host_backing": "ordinary",
  "model_repository": "turboderp/GLM-5.3-Flash-exl3",
  "model_revision": "2a30229e67012798ba9f0cd832bb78abf4c363d5",
  "draft_repository": null,
  "draft_revision": null,
  "recorded_runtime_label": null,
  "served_model_label": "glm-5.3-flash"
}
```

Pinned model revision recorded: yes. Source receipt labels, hashes and object locators are retained in [configurations.json](../configurations.json).

</details>

## Retained Measurements

No detailed benchmark receipt is matched to this record. A saved definition or a successful job exit alone is not a performance measurement.

A dash in shared decode means no qualified synchronized interval is available. Whole-wave throughput includes prefill and queueing. A valid decode interval can survive inside an overall failed or partial check; the source-report outcome is preserved. No rows are averaged.

## Additional Test Results

| Result / Source | Profile | Evidence type | Reported outcome | Retained values | Configuration binding |
| --- | --- | --- | --- | --- | --- |
| [result-2a8c7dbb8a8cc37c6373](../observations.json)<br>source-e55a92a1742e783d94e9e8c3.json<br>`/experiments/11/contexts/0` | [glm-mtp1-original-tensor_parallel](glm-mtp1-original-tensor_parallel.md) | context allocation | Outcome unspecified | context_tokens=524,288 tokens | Exact configuration unresolved |
| [result-2fa33d5e405cc7a4d989](../observations.json)<br>source-e55a92a1742e783d94e9e8c3.json<br>`/experiments/11/speed/1/backend_prefill/1` | [glm-mtp1-original-tensor_parallel](glm-mtp1-original-tensor_parallel.md) | test outcome | Outcome unspecified | backend_prefill_seconds=195.25 s; cached_prompt_tokens=0 tokens; prefill_tok_s=167.82 tokens/s; processed_prompt_tokens=32,767 tokens | Exact configuration unresolved |
| [result-325361f483430b32565a](../observations.json)<br>source-e55a92a1742e783d94e9e8c3.json<br>`/experiments/11/speed/1` | [glm-mtp1-original-tensor_parallel](glm-mtp1-original-tensor_parallel.md) | performance detail | Outcome unspecified | cold_TTFT_median_seconds=199.40 s; configured_slots=4 requests; output_tokens=256 tokens; p50_inter_token_ms=36.86 ms; p95_inter_token_ms=72.67 ms; prompt_tokens=32,767 tokens; Draft accepted / proposed: 474 / 550 tokens; fraction 0.8618 | Exact configuration unresolved |
| [result-5b78d8ed8b66d8593d8d](../observations.json)<br>source-e55a92a1742e783d94e9e8c3.json<br>`/experiments/11/speed/0/backend_prefill/0` | [glm-mtp1-original-tensor_parallel](glm-mtp1-original-tensor_parallel.md) | test outcome | Outcome unspecified | backend_prefill_seconds=49.35 s; cached_prompt_tokens=0 tokens; prefill_tok_s=663.95 tokens/s; processed_prompt_tokens=32,766 tokens | Exact configuration unresolved |
| [result-6a08751c86ae66919550](../observations.json)<br>source-e55a92a1742e783d94e9e8c3.json<br>`/experiments/11/speed/0` | [glm-mtp1-original-tensor_parallel](glm-mtp1-original-tensor_parallel.md) | performance detail | Outcome unspecified | cold_TTFT_median_seconds=49.44 s; configured_slots=4 requests; output_tokens=256 tokens; p50_inter_token_ms=18.80 ms; p95_inter_token_ms=36.77 ms; prompt_tokens=32,766 tokens; Draft accepted / proposed: 117 / 139 tokens; fraction 0.8417 | Exact configuration unresolved |
| [result-8c111ae16953104ac477](../observations.json)<br>source-e55a92a1742e783d94e9e8c3.json<br>`/experiments/11/speed/1/backend_prefill/2` | [glm-mtp1-original-tensor_parallel](glm-mtp1-original-tensor_parallel.md) | test outcome | Outcome unspecified | backend_prefill_seconds=194.44 s; cached_prompt_tokens=0 tokens; prefill_tok_s=168.52 tokens/s; processed_prompt_tokens=32,767 tokens | Exact configuration unresolved |
| [result-9822e2b3decc3a0fcfab](../observations.json)<br>source-e55a92a1742e783d94e9e8c3.json<br>`/experiments/11/speed/1/backend_prefill/0` | [glm-mtp1-original-tensor_parallel](glm-mtp1-original-tensor_parallel.md) | test outcome | Outcome unspecified | backend_prefill_seconds=193.30 s; cached_prompt_tokens=0 tokens; prefill_tok_s=169.51 tokens/s; processed_prompt_tokens=32,767 tokens | Exact configuration unresolved |
| [result-a00ffb828c217117e093](../observations.json)<br>source-e55a92a1742e783d94e9e8c3.json<br>`/experiments/11/speed/1/backend_prefill/3` | [glm-mtp1-original-tensor_parallel](glm-mtp1-original-tensor_parallel.md) | test outcome | Outcome unspecified | backend_prefill_seconds=193.64 s; cached_prompt_tokens=0 tokens; prefill_tok_s=169.22 tokens/s; processed_prompt_tokens=32,767 tokens | Exact configuration unresolved |
| [result-a1d3238168d6da0aeb51](../observations.json)<br>source-e55a92a1742e783d94e9e8c3.json<br>`/experiments/11` | [glm-mtp1-original-tensor_parallel](glm-mtp1-original-tensor_parallel.md) | context allocation | completed | matched_workload_host_peak_bytes=84,940,881,920 bytes; planning_reserve_mib=2,048 MiB; resident_pool_tokens=1,829,376 tokens; per_card_peak_used_MiB_unordered=55,552.00<br>56,057.00<br>56,089.00; capacity_boundary_measured=false; peak_prefill_and_concurrency_passed=false | Exact configuration unresolved |
| [result-bf0d1bc7a1bd014993f1](../observations.json)<br>source-7419c98729f86c1aed84b571.json<br>`/correctness` | [glm-mtp1-original-tensor_parallel](glm-mtp1-original-tensor_parallel.md) | correctness check | Pass | 4 response usage/timing records; matched_greedy_target_reference=false | Exact configuration unresolved |
| [result-e1f63b1620fdd32cb6f0](../observations.json)<br>source-a9e622d351a86c8b776605d4.json<br>`/experiments/16` | [glm-mtp1-original-tensor_parallel](glm-mtp1-original-tensor_parallel.md) | context allocation | Outcome unspecified | matched_workload_host_peak_bytes=84,940,881,920 bytes; per_card_peak_used_MiB_unordered=55,552.00<br>56,057.00<br>56,089.00 | Exact configuration unresolved |
| [result-f35e426dfe5612e2b8a6](../observations.json)<br>source-e55a92a1742e783d94e9e8c3.json<br>`/experiments/11/independently_maximized_config` | [glm-mtp1-original-tensor_parallel](glm-mtp1-original-tensor_parallel.md) | context allocation | Outcome unspecified | cache_tokens=1,829,376 tokens; context=524,288 tokens; reserve_mib=2,048 MiB | Exact configuration unresolved |

These are saved result records, including failures and bounded checks. Copies, individual requests, report summaries and regrading can overlap; their counts are not independent test repetitions. Open each result for exact values, units, configuration binding and source receipts.

[Full archive](../../README.md) | [All retained waves](../RESULTS.md) | [Data definitions](../DATA.md) | [Recommended recipes](../../../README.md)
