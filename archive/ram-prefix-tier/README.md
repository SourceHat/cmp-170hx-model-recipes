# Historical RAM Prefix-Page Tier

The selected Tabby recipes disable bulk KV page spilling. This archive retains
the numerical evidence from the earlier page-tier configuration, including
the original per-model budgets and reuse counters. It is not an activation
guide or a claim of a measured speedup from disabling the tier.

Recurrent checkpoints are separate: hybrid models need matching recurrent
state alongside their GPU KV pages to reuse a prefix. Those checkpoints
remain configured in the selected recipes.

## Retained Capacity Arithmetic

| Configuration | Combined main/draft page, bytes | RAM budget, MiB | Maximum page slots | Token-slot ceiling |
| --- | --- | --- | --- | --- |
| Orca | 9,469,952 | 8,192 | 907 | 232,192 |
| Apex EXL3 | 3,440,640 | 8,192 | 2,496 | 638,976 |

Formula: `floor(budget_MiB * 2^20 / combined_page_bytes) * 256`.
These are arithmetic page-slot ceilings, not measured distinct histories,
active context extensions or concurrent-request limits. Ancestor pages and
matching recurrent state are also required for reuse.

## Retained Reuse Counters

| Configuration | Page saves | Page restores | GPU page allocations | Restores / allocations |
| --- | --- | --- | --- | --- |
| Orca | 15,736 | 358 | 112,062 | 0.0031946600988738377 |
| Apex EXL3 | 110,585 | 29 | 515,563 | 0.00005624918778112471 |

Counts are cumulative operations and can revisit the same prefix. Different
lifetimes, cache state and background traffic prevent a controlled performance
comparison. The later snapshots retain zero page saves/restores and nonzero
recurrent restores; the exact snapshots and definitions remain in
[observations.json](observations.json).

[policy.json](policy.json) records the historical and current budgets for all
six Tabby recipes. Historical benchmark settings remain attached to their
measurements; changing a launch default does not change those test settings.

[Archive](../README.md) | [Selected recipes](../../README.md) | [Runtime setup](../../docs/REPRODUCING.md)
