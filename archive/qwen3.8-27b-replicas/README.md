# Qwen 3.8 27B: Historical Replica Benchmarks

Three independent one-card instances of **Qwen 3.8 27B, EXL3 6 bpw**, with
MTP1, Q8 KV, a 917,504-token pool and 16 configured slots per instance.
Each request uses 2,048-8,192 input tokens and a 1,024-token output budget.
These are standard Qwen weights; Orca is a separate abliterated checkpoint.

The [recommended recipe](../../recipes/qwen3.8-27b-exl3/README.md) currently
configures eight slots. This historical test measured one and sixteen requests
per instance, not eight. The individual instance contributions were measured
simultaneously; they are not isolated one-card runs or repetition averages.

## Synchronized Decode Results

| Replicas | Requests/replica | Total wave requests | Source wave | Shared decode, tok/s total | Shared decode/replica, tok/s | Shared interval, s | Accepted tokens in interval |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 3 | 1 | 3 | cold | 135.88 | 45.50<br>45.28<br>45.10 | 22.35 | 3,037 |
| 3 | 1 | 3 | warm | 134.73 | 45.34<br>44.90<br>44.49 | 22.41 | 3,019 |
| 3 | 16 | 48 | cold | 721.38 | 251.22<br>237.45<br>232.71 | 62.00 | 44,726 |
| 3 | 16 | 48 | warm | 718.76 | 247.00<br>237.71<br>234.06 | 63.30 | 45,495 |

Each row is one wave. Shared decode counts accepted tokens after the last
request's first-generation event and before the first completion, excluding
prefill. The replica contributions sum to the total. The `cold` / `warm`
source labels are retained. Cached-token counts in the per-request timing
records establish reuse independently of those labels.

[Exact CSV](benchmarks.csv) is a view of the unchanged
[canonical JSON](../../recipes/qwen3.8-27b-exl3/historical-replica-result.json),
not four additional runs. It preserves the source receipt label, SHA256
and pointer. Sampling settings missing from that receipt remain unspecified.

## Prefill And First-Token Latency

All 102 requests from the same source reports are retained in
[per-request JSON](../../recipes/qwen3.8-27b-exl3/historical-replica-requests.json)
and [CSV](requests.csv). The source `prompt_n` already counts processed tokens;
cached tokens are separate. Backend prefill uses `prompt_n / (prompt_ms / 1000)`.
Client TTFT includes queueing and other overhead. The main README uses the
median observed per-replica value, not an average of the C48 wave.
The separate [32k MTP1 retention check](../../docs/QWEN-32K-EVIDENCE.md) uses C2
and does not supply the current C1/C8 benchmark.

## Separate Legacy C48 Results

The [older C48 record](../history/profiles/qwen3.8-27b-three-instances-mtp1-c48-legacy.md)
retains 256-output-token requests and client timing, including all 96 request
records across cold and warm waves. Its wall-time throughput and
after-first-token estimates are separate metrics; it has no qualified
synchronized backend interval. It is not combined with the 1,024-token waves
above.

Native-context checks and RAM-restoration evidence remain on the
[recipe page](../../recipes/qwen3.8-27b-exl3/README.md#verification).
They are bounded checks, not speed measurements at the context limit.

[All Qwen 3.8 27B records](../models/qwen-3.8-27b.md) | [Prefill](../history/PREFILL.md) | [Archive](../README.md) | [Data definitions](../history/DATA.md)
