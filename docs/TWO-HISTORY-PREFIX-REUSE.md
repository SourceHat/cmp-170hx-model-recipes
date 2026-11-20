# Two Long Histories: Prefix Reuse

On the selected Apex Flash 1 EXL3 recipe, six warm follow-ups reused 99.61-99.73% of their input. The concurrent pair used 131,542 and 176,600 input tokens and reached first output in 2.86 and 3.38 seconds. No completed cached pages or state checkpoints were evicted during this check. These are single observations, not averages or a comparison with another runtime.

## Configuration And Protocol

This recorded check used three CMP 170HX 64 GB cards with Apex Flash 1 EXL3, TP3/native MTP1, four request slots, Q8 main/draft KV, a 1,083,136-token shared GPU KV pool, and a 524,288-token configured context limit. The current [recipe](../recipes/apex-abliterated-exl3-mtp1-tp3/README.md) has a separately qualified 1,374,976-token pool; the measurements here retain their original geometry. Bulk host KV spilling is off; the recurrent checkpoint budget remains 16 GiB. Hardware and pinned runtime identities are documented in the recipe and [hardware reference](HARDWARE.md).

Two distinct synthetic histories contain 131,061 and 176,119 content tokens before chat wrapping. Each includes an early assistant reasoning turn. Prime each history once, append the generated assistant turn and a small user turn, submit both follow-ups together, alternate subsequent follow-ups, append a synthetic tool-call/result, then send a warm continuation through LiteLLM Chat Completions. Temperature is zero; minimum and maximum accepted output are 256 tokens. Every request completed with 256 accepted tokens, including reasoning. Backend request counts matched the controlled submissions; no extra requests were observed.

## Measurements

Each row is one request. The two concurrent rows belong to the same two-request wave. The other rows are sequential. Backend decode rate excludes prefill and queue time. First progress and total time are measured by the client and include gateway/network costs.

| Stage | History | Submitted requests | Route | Input, tokens | Cached, tokens | Reuse, % | Output, tokens | Prefill, s | Backend decode, tok/s/request | First progress, s | Client total, s |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Cold prime | A | 1 | Native Chat | 131,273 | 0 | 0.00 | 256 | 201.48 | 32.89 | 202.06 | 209.70 |
| Cold prime | B | 1 | Native Chat | 176,331 | 0 | 0.00 | 256 | 271.65 | 26.39 | 272.25 | 281.92 |
| Concurrent append | A | 2 | Native Chat | 131,542 | 131,072 | 99.64 | 256 | 1.71 | 20.31 | 2.86 | 15.43 |
| Concurrent append | B | 2 | Native Chat | 176,600 | 176,128 | 99.73 | 256 | 1.09 | 21.13 | 3.38 | 15.43 |
| Alternating append | A | 1 | Native Chat | 131,808 | 131,328 | 99.64 | 256 | 1.02 | 28.11 | 1.49 | 10.57 |
| Alternating append | B | 1 | Native Chat | 176,866 | 176,384 | 99.73 | 256 | 0.99 | 35.42 | 1.74 | 8.94 |
| Tool-result append | A | 1 | Native Chat | 132,096 | 131,584 | 99.61 | 256 | 1.04 | 30.69 | 1.77 | 10.06 |
| Gateway append | B | 1 | LiteLLM Chat | 177,133 | 176,640 | 99.72 | 256 | 1.01 | 33.98 | 1.76 | 9.27 |

The six warm requests retained every previously completed matching KV page. Each had one page (256 tokens) of resident KV beyond its last reusable state checkpoint. That small replay plus the new suffix explains why reuse is near 100%, rather than exactly 100%. Cold priming still took 201.48 and 271.65 backend prefill seconds; warm reuse does not eliminate the cost of a new history.

## Scope

This check establishes long-prefix reuse for the submitted stable histories, including concurrent processing, tool-result replay and one gateway Chat continuation. It does not establish the behavior of arbitrary production histories, near-limit requests, a fully occupied retained cache or Responses API conversion in this workload. The selected cache holds 309,248 tokens after the check, well below its 1,083,136-token capacity. No model-quality test or causal before/after speedup claim is made.

[Exact observations and metric definitions](../data/two-history-prefix-reuse.json) - [CSV](../data/two-history-prefix-reuse.csv) - [Anonymous numeric diagnostics](PREFIX-REUSE.md#numerical-diagnostics).

Original documentation/data: [CC BY 4.0](../LICENSES/CC-BY-4.0.txt), with SourceHat attribution.
