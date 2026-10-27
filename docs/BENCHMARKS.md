# Benchmark Methodology

Each recipe has numerical `benchmarks.json` records. `benchmarks.csv` is the
combined export. Receipt labels and original SHA256 digests identify the
source measurements without copying private host paths or conversation logs.
The full field definitions, geometry notes and evidence inventory are in
[DATA.md](DATA.md). Per-profile `evidence.json` files preserve cache-precision
audits, per-card memory, context/restoration checks and quantization details.

## Reading The Numbers

The shared campaign client requests temperature 0, seed 20261008 and low
reasoning effort, with minimum and maximum output budgets set to the wave's
requested length. Low effort is a request setting; templates and engines can
interpret it differently, so it is not a calibrated cross-model reasoning
budget. These defaults and their source hashes are in
[benchmark-protocol.json](../data/benchmark-protocol.json). Historical per-run
parameters absent from receipts remain unspecified.

- Decode counts accepted output tokens, including reasoning, and excludes prefill.
- Concurrent decode is the aggregate across all requests in the measured wave.
- TTFT is the median time to first output token; it includes cold input processing and queueing.
- Backend prefill is a per-request timer. Engine timer boundaries differ, so it is not an isolated cross-engine speed ratio.
- `input_target_tokens` is the intended workload; `input_tokens_per_request` records tokenizer counts where available.
- `tested_kv_pool_tokens` describes the speed job, which can differ from the selected serving pool.

Most newer comparisons use approximately 32k input and 256 accepted outputs.
Qwen3.8-27B Orca also has 2k waves and 512-output repeated requests. MiMo-V2.6-Flash's preserved
matched waves use 512 outputs. Apex Flash 1 AWQ additionally has 8,192-output runs.
The long AWQ SSE timer includes client streaming overhead and estimates the
first accepted batch as one token; it is separate from the short server-traced
measurements. A repeated input is not called a verified cache hit unless
backend counters established that hit.

The catalog summary labels the measured input/output geometry and selects cold
32k C1/concurrent pairs for all eight recipes. MiMo-V2.6-Flash uses 512 accepted outputs;
the other displayed pairs use 256. The [selected-serving comparison](PREFILL-COMPARISON.md)
supplies standard Qwen MTP1 C1/C8 and balanced Apex Flash 1 AWQ / DeepSeek V4.1 Flash C1/C4.
It includes native C1 prefill, client TTFT, exact accepted counts and synchronized
decode traces. The whole row comes from its matching pair.

Historical Qwen three-replica measurements and its separate
[32k MTP1 C2 retention check](QWEN-32K-EVIDENCE.md) remain archived with their
original settings. They are not substituted for the new C1/C8 pair.

The older short-output AWQ/DeepSeek V4.1 Flash reports still lack native prefill timers;
their missing fields are preserved. Separate
[AWQ long-output metric snapshots](RECOVERED-PREFILL.md) retain four native
prefill observations at 8,192 accepted outputs. Those measurements remain with
their original workload. Scheduler-span reconstructions and input divided by
TTFT are not substitutes for native timers.

## Context And Memory

The configured context is the per-request total token limit. The GPU KV pool
is aggregate token capacity shared by live requests and cached prefixes.
`pool // context` is capacity arithmetic, not a claim that those maximum-size
histories have been benchmarked concurrently. Host KV/recurrent cache budgets
are separate from the resident GPU pool and must not be summed as additional
GPU token capacity.

Eight-bit serving KV does not mean every activation, recurrent state,
positional key or model tensor is eight-bit. Those retain the engine's
architecture-specific precision policy. Weight quantization is reported
separately from main/draft serving-cache precision.

Native Qwen3.8-27B Orca has context/retrieval and restoration evidence. GLM-5.3-Flash, MiMo-V2.6-Flash, Apex Flash 1
and DeepSeek V4.1 Flash retain their recorded allocation and short near-limit checks;
the campaign did not requalify a complete long-history retention/restoration
stress suite. Qwen3.8-Flash-Next's selected native pool passed allocation and short
concurrency checks; a fresh native near-limit run was not performed. These
trials do not establish model quality at every context or sustained near-limit
throughput.

Measurements span different recorded driver/runtime epochs. SHA references
and per-point methods are preserved; historical results are not relabeled as
fresh matched comparisons. The portable source/config export has CPU checks,
not a new GPU run from a clean community installation.
