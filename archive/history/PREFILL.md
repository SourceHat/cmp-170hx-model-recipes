# Backend Prefill Measurements

Prefill processes input before decoding. These are the saved backend timers
and per-request rates, kept with processed and cached prompt-token counts.
They complement [decode / client latency](RESULTS.md) and are not derived from TTFT.

The JSON and CSV are a view of `observations.json`, not additional experiments.
`cold_prefill` and `prefill` preserve the source field names. Cached-token counts,
rather than the field name alone, show how much input was reused. Report
summaries, individual requests and recipe data can overlap; do not pool them.
No aggregate prefill throughput is inferred by summing per-request rates.

**990 saved entries from 293 source arrays.** The [exact JSON](prefill.json) and [CSV](prefill.csv) retain every entry, its array index, configuration binding and source receipts.

## Browse By Model Family

| Family | Source arrays | Saved entries |
| --- | --- | --- |
| [Apex Flash 1 (GLM 5.3 Flash post-train)](prefill/apex-flash-1.md) | 46 | 118 |
| [GLM 5.3 Flash](prefill/glm-5.3-flash.md) | 70 | 178 |
| [MiMo V2.6 Flash](prefill/mimo-v2.6-flash.md) | 60 | 150 |
| [Orca (Qwen 3.8 27B abliterated)](prefill/orca.md) | 57 | 330 |
| [Other model workflows](prefill/other-model-workflows.md) | 12 | 46 |
| [Qwen 3.8 Flash Next](prefill/qwen-3.8-flash-next.md) | 48 | 168 |

Family association is navigation, not proof of an exact configuration; unbound
records remain unbound. A shared result can appear on more than one family page.
Missing backend timers stay unavailable. Source rates use processed tokens
divided by backend prefill seconds, whose recorded precision can differ from
client timers. Warm reuse processes only the uncached suffix; its rate does
not measure cold input processing over the full prompt.

The [recommended recipes](../../README.md#measured-performance) have a separate
matched 32k cold C1 comparison. Their JSON retains all concurrent prefill arrays.
This historical index spans other input lengths and settings; it is not a
ranked model comparison. The [Qwen replica timings](../qwen3.8-27b-replicas/README.md)
include the original backend timers from the same source reports as its
four decode waves. The displayed short-output AWQ and DeepSeek rows lack native
timers. Separate [AWQ long-output snapshots](../../docs/RECOVERED-PREFILL.md)
retain four native prefill observations, kept with their original workloads.

[Archive](../README.md) | [Definitions](DATA.md) | [All result categories](OBSERVATIONS.md) | [Sources](result-sources.json)
