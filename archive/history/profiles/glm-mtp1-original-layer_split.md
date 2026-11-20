# glm-mtp1-original-layer_split

**Historical record. Additional test results; no matched decode wave.**

Model family: GLM 5.3 Flash.

The campaign inventory recorded status `speed_measured_capacity_pending`. The evidence sections retain any later results separately.

Historical configurations are provided for comparison. The [recommended recipes](../../../README.md) include supported launch scripts.

Current recipes using the same recorded checkpoint repository: [glm-5.3-flash-mtp1-tp3](../../../recipes/glm-5.3-flash-mtp1-tp3/README.md). Context, cache and runtime versions can differ.

## Saved Configuration Versions

Each configuration ID identifies a distinct original settings record. Deployment fields are omitted; versions can have identical published settings after that omission. Upstream runtime commits remain unspecified where the source retained only an integration label.

| Configuration | Recorded artifact / source | Configured card counts | Context tokens | GPU pool tokens | Slots | Draft mode / tokens |
| --- | --- | --- | --- | --- | --- | --- |
| cfg-4d12fa4319c9666224d3 | [turboderp/GLM-5.3-Flash-exl3@2a30229e67](https://huggingface.co/turboderp/GLM-5.3-Flash-exl3/tree/2a30229e67012798ba9f0cd832bb78abf4c363d5) | 3 | 262,144 | 262,144 | 4 | mtp / 1 |

Card counts are saved configuration choices, not a claim that every allowed placement was measured. A derived view can differ from its pinned download source.

<details>
<summary>cfg-4d12fa4319c9666224d3</summary>

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
  "parallelism": "layer_split",
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
| [result-0481c50cff433b4033f2](../observations.json)<br>source-e55a92a1742e783d94e9e8c3.json<br>`/experiments/10/speed/1` | [glm-mtp1-original-layer_split](glm-mtp1-original-layer_split.md) | performance detail | Outcome unspecified | cold_TTFT_median_seconds=157.48 s; configured_slots=4 requests; output_tokens=256 tokens; p50_inter_token_ms=57.33 ms; p95_inter_token_ms=110.00 ms; prompt_tokens=32,767 tokens; Draft accepted / proposed: 472 / 552 tokens; fraction 0.8551 | Exact configuration unresolved |
| [result-06de2107aa2155684f2a](../observations.json)<br>source-e55a92a1742e783d94e9e8c3.json<br>`/experiments/10/speed/0/backend_prefill/0` | [glm-mtp1-original-layer_split](glm-mtp1-original-layer_split.md) | test outcome | Outcome unspecified | backend_prefill_seconds=39.17 s; cached_prompt_tokens=0 tokens; prefill_tok_s=836.51 tokens/s; processed_prompt_tokens=32,766 tokens | Exact configuration unresolved |
| [result-0f26d6778707c28217e9](../observations.json)<br>source-3a9ccee3326aa45871c71e19.json<br>`/` | [glm-mtp1-original-layer_split](glm-mtp1-original-layer_split.md) | correctness check | Pass | 4 response usage/timing records; matched_greedy_target_reference=false | Exact configuration unresolved |
| [result-24a6153759f42967a827](../observations.json)<br>source-e55a92a1742e783d94e9e8c3.json<br>`/experiments/10/speed/0` | [glm-mtp1-original-layer_split](glm-mtp1-original-layer_split.md) | performance detail | Outcome unspecified | cold_TTFT_median_seconds=39.39 s; configured_slots=4 requests; output_tokens=256 tokens; p50_inter_token_ms=25.89 ms; p95_inter_token_ms=52.10 ms; prompt_tokens=32,766 tokens; Draft accepted / proposed: 112 / 144 tokens; fraction 0.7778 | Exact configuration unresolved |
| [result-4a009d185c286fabd24a](../observations.json)<br>source-e55a92a1742e783d94e9e8c3.json<br>`/experiments/10` | [glm-mtp1-original-layer_split](glm-mtp1-original-layer_split.md) | context allocation | Outcome unspecified | matched_workload_host_peak_bytes=63,732,518,912 bytes; per_card_peak_used_MiB_unordered=43,258.00<br>60,828.00<br>61,528.00 | Exact configuration unresolved |
| [result-582030fa57161f7cdf8e](../observations.json)<br>source-e55a92a1742e783d94e9e8c3.json<br>`/experiments/10/speed/1/backend_prefill/0` | [glm-mtp1-original-layer_split](glm-mtp1-original-layer_split.md) | test outcome | Outcome unspecified | backend_prefill_seconds=151.09 s; cached_prompt_tokens=0 tokens; prefill_tok_s=216.87 tokens/s; processed_prompt_tokens=32,767 tokens | Exact configuration unresolved |
| [result-8771c476d99a73e90e37](../observations.json)<br>source-e55a92a1742e783d94e9e8c3.json<br>`/experiments/10/speed/1/backend_prefill/1` | [apex_exl3-dflash23-original-layer_split](apex_exl3-dflash23-original-layer_split.md)<br>[glm-mtp1-original-layer_split](glm-mtp1-original-layer_split.md) | test outcome | Outcome unspecified | backend_prefill_seconds=153.07 s; cached_prompt_tokens=0 tokens; prefill_tok_s=214.07 tokens/s; processed_prompt_tokens=32,767 tokens | Exact configuration unresolved |
| [result-b9ed79737e9693e8a1cf](../observations.json)<br>source-e55a92a1742e783d94e9e8c3.json<br>`/experiments/10/speed/1/backend_prefill/2` | [glm-mtp1-original-layer_split](glm-mtp1-original-layer_split.md) | test outcome | Outcome unspecified | backend_prefill_seconds=151.90 s; cached_prompt_tokens=0 tokens; prefill_tok_s=215.71 tokens/s; processed_prompt_tokens=32,767 tokens | Exact configuration unresolved |
| [result-ca7503b93ab58c64b59e](../observations.json)<br>source-e55a92a1742e783d94e9e8c3.json<br>`/experiments/10/speed/1/backend_prefill/3` | [glm-mtp1-original-layer_split](glm-mtp1-original-layer_split.md) | test outcome | Outcome unspecified | backend_prefill_seconds=151.17 s; cached_prompt_tokens=0 tokens; prefill_tok_s=216.76 tokens/s; processed_prompt_tokens=32,767 tokens | Exact configuration unresolved |
| [result-dea92d2068a6406ff87d](../observations.json)<br>source-a9e622d351a86c8b776605d4.json<br>`/experiments/15` | [glm-mtp1-original-layer_split](glm-mtp1-original-layer_split.md) | context allocation | Outcome unspecified | matched_workload_host_peak_bytes=63,732,518,912 bytes; per_card_peak_used_MiB_unordered=43,258.00<br>60,828.00<br>61,528.00 | Exact configuration unresolved |

These are saved result records, including failures and bounded checks. Copies, individual requests, report summaries and regrading can overlap; their counts are not independent test repetitions. Open each result for exact values, units, configuration binding and source receipts.

[Full archive](../../README.md) | [All retained waves](../RESULTS.md) | [Data definitions](../DATA.md) | [Recommended recipes](../../../README.md)
