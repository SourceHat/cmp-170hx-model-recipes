# Qwen 3.8 Flash Next

[Archive](../README.md) | [All archived profiles](../PROFILES.md) | [Additional experiments](../EXPERIMENTS.md)

Recommended recipes with the same recorded checkpoint repository: [qwen-flash-next-mtp2-layer-split](../../recipes/qwen-flash-next-mtp2-layer-split/README.md).

Open each record for its settings, layout, draft, context/cache geometry and exact measurements. Versions can differ in artifact or runtime identity. A linked result is not transferred to another configuration.

The [Strata comparison](../STRATA.md) includes additional engine templates and allocation evidence.

## Archived Profiles

| Profile / experiment | Evidence | Versions | Waves | Checks | Other results |
| --- | --- | --- | --- | --- | --- |
| [qwen-flash-next-int4-huge-host-pair01](../history/profiles/qwen-flash-next-int4-huge-host-pair01.md) | Decode interval measured | 1 | 2 | 6 | 5 |
| [qwen-flash-next-int4-huge-p2p-pair01](../history/profiles/qwen-flash-next-int4-huge-p2p-pair01.md) | Additional test results; no matched decode wave | 1 | 0 | 0 | 1 |
| [qwen-flash-next-int4-huge-sm-write-pair01](../history/profiles/qwen-flash-next-int4-huge-sm-write-pair01.md) | Decode interval measured | 1 | 2 | 4 | 5 |
| [qwen-flash-next-int4-pinned-host-pair01](../history/profiles/qwen-flash-next-int4-pinned-host-pair01.md) | Decode interval measured | 1 | 2 | 6 | 6 |
| [qwen-flash-next-int4-pinned-p2p-pair01](../history/profiles/qwen-flash-next-int4-pinned-p2p-pair01.md) | Definition; no matched test receipt | 1 | 0 | 0 | 0 |
| [qwen-flash-next-int4-pinned-sm-write-pair01](../history/profiles/qwen-flash-next-int4-pinned-sm-write-pair01.md) | Definition; no matched test receipt | 1 | 0 | 0 | 0 |
| [qwen-flash-next-ordinary-native-context](../history/profiles/qwen-flash-next-ordinary-native-context.md) | Additional test results; no matched decode wave | 2 | 0 | 0 | 1 |
| [qwen-flash-next-ordinary-validation](../history/profiles/qwen-flash-next-ordinary-validation.md) | Additional test results; no matched decode wave | 2 | 0 | 0 | 8 |
| [qwen-flash-next-validation](../history/profiles/qwen-flash-next-validation.md) | Additional test results; no matched decode wave | 2 | 0 | 0 | 1 |

## Additional Experiments And Results

| Profile / experiment | Evidence | Versions | Waves | Checks | Other results |
| --- | --- | --- | --- | --- | --- |
| [ab-flash_next-layer_split-control-012](../history/profiles/ab-flash_next-layer_split-control-012.md) | Additional test results; no matched decode wave | 1 | 0 | 0 | 1 |
| [ab-flash_next-tensor_parallel-control-013](../history/profiles/ab-flash_next-tensor_parallel-control-013.md) | Additional test results; no matched decode wave | 1 | 0 | 0 | 1 |
| [ad004-flash_next-layer_split-control-083](../history/profiles/ad004-flash_next-layer_split-control-083.md) | Additional test results; no matched decode wave | 1 | 0 | 0 | 1 |
| [ad004-flash_next-mtp1-original-layer_split-matched-084](../history/profiles/ad004-flash_next-mtp1-original-layer_split-matched-084.md) | Decode interval measured | 1 | 4 | 4 | 7 |
| [ad004-flash_next-mtp2-original-layer_split-matched-085](../history/profiles/ad004-flash_next-mtp2-original-layer_split-matched-085.md) | Decode interval measured | 1 | 4 | 4 | 9 |
| [ad004-flash_next-mtp3-original-layer_split-matched-086](../history/profiles/ad004-flash_next-mtp3-original-layer_split-matched-086.md) | Decode interval measured | 1 | 4 | 4 | 7 |
| [ad017-flash_next-mtp3-original-tensor_parallel-matched-103](../history/profiles/ad017-flash_next-mtp3-original-tensor_parallel-matched-103.md) | Decode interval measured | 1 | 4 | 5 | 8 |
| [ad019-flash_next-mtp3-original-tensor_parallel-sizing-final-smoke-115](../history/profiles/ad019-flash_next-mtp3-original-tensor_parallel-sizing-final-smoke-115.md) | Bounded checks only | 2 | 0 | 2 | 2 |
| [ad024-flash-mtp2-native-final-008](../history/profiles/ad024-flash-mtp2-native-final-008.md) | Bounded checks only | 2 | 0 | 1 | 2 |
| [ad024-flash-p2p-mtp2-004](../history/profiles/ad024-flash-p2p-mtp2-004.md) | Decode interval measured | 1 | 4 | 4 | 8 |
| [ad024-flash-p2p-mtp3-005](../history/profiles/ad024-flash-p2p-mtp3-005.md) | Decode interval measured | 1 | 4 | 4 | 8 |
| [ad024-flash_next-mtp2-original-layer_split-ad024-sizing-final-smoke-002](../history/profiles/ad024-flash_next-mtp2-original-layer_split-ad024-sizing-final-smoke-002.md) | Additional test results; no matched decode wave | 2 | 0 | 0 | 1 |
| [ad024-flash_next-mtp2-original-layer_split-ad024-sizing-final-smoke-003](../history/profiles/ad024-flash_next-mtp2-original-layer_split-ad024-sizing-final-smoke-003.md) | Decode interval measured | 2 | 4 | 5 | 10 |
| [ad026-mtp2-tp2-000](../history/profiles/ad026-mtp2-tp2-000.md) | Decode interval measured | 2 | 4 | 3 | 8 |
| [ad026-mtp2-tp2-allocation-002](../history/profiles/ad026-mtp2-tp2-allocation-002.md) | Bounded checks only | 2 | 0 | 1 | 5 |
| [ad026-mtp3-layer-split-allocation-003](../history/profiles/ad026-mtp3-layer-split-allocation-003.md) | Bounded checks only | 2 | 0 | 1 | 5 |
| [ad026-mtp3-tp2-control-001](../history/profiles/ad026-mtp3-tp2-control-001.md) | Additional test results; no matched decode wave | 2 | 0 | 0 | 1 |
| [configuration-a934cd648727b84b8188](../history/profiles/configuration-a934cd648727b84b8188.md) | Additional test results; no matched decode wave | 1 | 0 | 0 | 3 |
| [record-8daa719f5c8575f3ccd8](../history/profiles/record-8daa719f5c8575f3ccd8.md) | Decode interval measured | 0 | 1 | 0 | 0 |
| [flash_next-mtp1-original-layer_split](../history/profiles/flash_next-mtp1-original-layer_split.md) | Additional test results; no matched decode wave | 1 | 0 | 0 | 13 |
| [flash_next-mtp1-original-tensor_parallel](../history/profiles/flash_next-mtp1-original-tensor_parallel.md) | Definition; no matched test receipt | 1 | 0 | 0 | 0 |
| [flash_next-mtp2-original-layer_split](../history/profiles/flash_next-mtp2-original-layer_split.md) | Additional test results; no matched decode wave | 1 | 0 | 0 | 13 |
| [flash_next-mtp2-original-layer_split-ad024-ctx524288-qualification](../history/profiles/flash_next-mtp2-original-layer_split-ad024-ctx524288-qualification.md) | Bounded checks only | 1 | 0 | 1 | 1 |
| [flash_next-mtp2-original-layer_split-ad024-max](../history/profiles/flash_next-mtp2-original-layer_split-ad024-max.md) | Bounded checks only | 1 | 0 | 2 | 5 |
| [flash_next-mtp2-original-layer_split-ad024-sizing-final-smoke-fit-phase](../history/profiles/flash_next-mtp2-original-layer_split-ad024-sizing-final-smoke-fit-phase.md) | Bounded checks only | 1 | 0 | 1 | 0 |
| [flash_next-mtp2-original-tensor_parallel](../history/profiles/flash_next-mtp2-original-tensor_parallel.md) | Definition; no matched test receipt | 1 | 0 | 0 | 0 |
| [flash_next-mtp3-original-layer_split](../history/profiles/flash_next-mtp3-original-layer_split.md) | Additional test results; no matched decode wave | 1 | 0 | 0 | 13 |
| [flash_next-mtp3-original-tensor_parallel](../history/profiles/flash_next-mtp3-original-tensor_parallel.md) | Additional test results; no matched decode wave | 1 | 0 | 0 | 14 |
| [flash_next-mtp3-original-tensor_parallel-completed](../history/profiles/flash_next-mtp3-original-tensor_parallel-completed.md) | Bounded checks only | 1 | 0 | 2 | 5 |
| [flash_next-mtp3-original-tensor_parallel-ctx524288-qualification](../history/profiles/flash_next-mtp3-original-tensor_parallel-ctx524288-qualification.md) | Bounded checks only | 1 | 0 | 1 | 1 |
| [qwen-flash-next-external-dflash-validation](../history/profiles/qwen-flash-next-external-dflash-validation.md) | Decode interval measured | 2 | 2 | 7 | 17 |
| [qwen-flash-next-fp8-mtp-validation](../history/profiles/qwen-flash-next-fp8-mtp-validation.md) | Bounded checks only | 1 | 0 | 2 | 7 |
| [qwen-flash-next-fp8-ordinary-validation](../history/profiles/qwen-flash-next-fp8-ordinary-validation.md) | Bounded checks only | 1 | 0 | 2 | 3 |
| [qwen-flash-next-int4-mtp-validation](../history/profiles/qwen-flash-next-int4-mtp-validation.md) | Bounded checks only | 1 | 0 | 4 | 7 |
| [qwen-flash-next-int4-ordinary-validation](../history/profiles/qwen-flash-next-int4-ordinary-validation.md) | Bounded checks only | 1 | 0 | 4 | 7 |
| [qwen-flash-next-mtp2-layer-split](../history/profiles/qwen-flash-next-mtp2-layer-split.md) | Additional test results; no matched decode wave | 2 | 0 | 0 | 6 |
| [qwen-flash-next-mtp3-tp2-native](../history/profiles/qwen-flash-next-mtp3-tp2-native.md) | Bounded checks only | 2 | 0 | 1 | 7 |
| [qwen-flash-next-mtp3-tp2-yarn524k](../history/profiles/qwen-flash-next-mtp3-tp2-yarn524k.md) | Definition; no matched test receipt | 1 | 0 | 0 | 0 |
| [qwen-flash-next-native-context](../history/profiles/qwen-flash-next-native-context.md) | Additional test results; no matched decode wave | 2 | 0 | 0 | 3 |
| [record-cb8f1e53c508e62d6917](../history/profiles/record-cb8f1e53c508e62d6917.md) | Additional test results; no matched decode wave | 0 | 0 | 0 | 1 |

[Prefill](../history/PREFILL.md) | [Quality](../history/QUALITY.md) | [All waves](../history/RESULTS.md) | [Data definitions](../history/DATA.md)
