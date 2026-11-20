# Bounded Quality And Correctness Scores

These small task sets evaluate the recorded checkpoints and serving stacks.
They do not isolate quantization quality or establish a broad coding,
cybersecurity or reasoning benchmark. Different task sets and grading revisions
remain separate, and raw tasks and generated responses are excluded.

The retained Apex checkpoint comparison reports **25/32 for EXL3** and
**27/32 for AWQ**. It changes both checkpoint/backend combinations; the two-task
difference cannot be attributed to quantization alone. The source records one
bounded incomplete answer. The eight-task follow-ups use a different task set.

For the eight-task Orca follow-ups, original scoring reports **6/8** for both
native and extended-context configurations. A later grading pass on the same
responses reports **7/8** for each, accepting both permitted representations of
one action. Both grades are preserved; they are not independent model runs.
The extended-context result does not change the current native-context recipe.

The mathematical-overlay experiment records **22/32** for each of base,
original and expanded arms. Its saved grades demonstrate no task-score gain.
The exact local overlay is not reconstructed or assigned to another artifact.

All ratios below are tasks passed / tasks evaluated. Categories retain their
own denominators. Latency is the median total client time over the stated
saved task requests, not decode throughput. Missing denominators remain `?`.

| Result / Source | Profile | Evidence type | Reported outcome | Retained values | Configuration binding |
| --- | --- | --- | --- | --- | --- |
| [result-00d48da009eb38e41e63](observations.json)<br>source-e3b968cfd704593190938f6e.json<br>`/grades/base` | [record-26c850ec689cf58c6b67](profiles/record-26c850ec689cf58c6b67.md)<br>[record-7f0ad416bef4c826bba4](profiles/record-7f0ad416bef4c826bba4.md)<br>[record-d03ade5e113afe82b120](profiles/record-d03ade5e113afe82b120.md) | quality evaluation | 22 / 32 tasks passed | coding: 7 / 8; multi_step_agent: 4 / 8; reasoning: 5 / 8; tool_format: 6 / 8 | Exact configuration unresolved |
| [result-093c4559959908287344](observations.json)<br>source-797606345fa45914fcd85b71.json<br>`/profiles/qwen27-orca-mtp3-native/raw_followup/quality` | [ad024-orca-native-000](profiles/ad024-orca-native-000.md)<br>[qwen27-orca-mtp3-native](profiles/qwen27-orca-mtp3-native.md) | quality evaluation | 6 / 8 tasks passed | Task latency median 4.27 s; n=8 | Recorded configuration/job |
| [result-0e82ac87c4ceaa090b4c](observations.json)<br>source-1b88b19bb8d1f6b6f26ce856.json<br>`/mathematical_historical_evaluation/arms/expanded` | [record-26c850ec689cf58c6b67](profiles/record-26c850ec689cf58c6b67.md) | quality evaluation | 22 / 32 tasks passed | coding: 7 / 8; multi_step_agent: 4 / 8; reasoning: 5 / 8; tool_format: 6 / 8 | Exact configuration unresolved |
| [result-1be76857e570482c47b4](observations.json)<br>source-797606345fa45914fcd85b71.json<br>`/profiles/apex-abliterated-awq-dflash2-pp3-balanced/quality` | [apex-abliterated-awq-dflash2-pp3-balanced](profiles/apex-abliterated-awq-dflash2-pp3-balanced.md) | quality evaluation | 8 / 8 tasks passed | coding: 2 / 2; tool: 2 / 2; agent: 2 / 2; reasoning: 2 / 2; Task latency median 3.21 s; n=8 | Recorded configuration/job |
| [result-2833cb0f0ed66314defe](observations.json)<br>source-797606345fa45914fcd85b71.json<br>`/profiles/apex-abliterated-exl3-mtp1-tp3/quality` | [apex-abliterated-exl3-mtp1-tp3](profiles/apex-abliterated-exl3-mtp1-tp3.md) | quality evaluation | 7 / 8 tasks passed | coding: 1 / 2; tool: 2 / 2; agent: 2 / 2; reasoning: 2 / 2; Task latency median 3.63 s; n=8 | Recorded configuration/job |
| [result-5cded3e6e01d38445b36](observations.json)<br>source-e3b968cfd704593190938f6e.json<br>`/grades/expanded` | [record-26c850ec689cf58c6b67](profiles/record-26c850ec689cf58c6b67.md)<br>[record-7f0ad416bef4c826bba4](profiles/record-7f0ad416bef4c826bba4.md)<br>[record-d03ade5e113afe82b120](profiles/record-d03ade5e113afe82b120.md) | quality evaluation | 22 / 32 tasks passed | coding: 7 / 8; multi_step_agent: 4 / 8; reasoning: 5 / 8; tool_format: 6 / 8 | Exact configuration unresolved |
| [result-695353033d8c3235300c](observations.json)<br>source-797606345fa45914fcd85b71.json<br>`/profiles/qwen27-orca-mtp3-native/quality` | [qwen27-orca-mtp3-native](profiles/qwen27-orca-mtp3-native.md) | quality evaluation | 7 / 8 tasks passed | coding: 2 / 2; tool: 2 / 2; agent: 2 / 2; reasoning: 1 / 2; Task latency median 4.27 s; n=8 | Recorded configuration/job |
| [result-6fe7fe97b5483b418b7a](observations.json)<br>source-0da06bd9a8d7bfaaf6d8cec8.json<br>`/arms/exl3` | [checkpoint-quality-apex-exl3](profiles/checkpoint-quality-apex-exl3.md)<br>[record-26c850ec689cf58c6b67](profiles/record-26c850ec689cf58c6b67.md) | quality evaluation | 25 / 32 tasks passed | coding: 7 / 8; multi_step_agent: 4 / 8; reasoning: 7 / 8; tool_format: 7 / 8 | Recorded configuration/job |
| [result-97ee856f9bebd59c21ac](observations.json)<br>source-797606345fa45914fcd85b71.json<br>`/profiles/apex-abliterated-exl3-mtp1-tp3/raw_followup/quality` | [ad024-apex-exl3-mtp1-tp3-006](profiles/ad024-apex-exl3-mtp1-tp3-006.md)<br>[apex-abliterated-exl3-mtp1-tp3](profiles/apex-abliterated-exl3-mtp1-tp3.md) | quality evaluation | 7 / 8 tasks passed | Task latency median 3.63 s; n=8 | Recorded configuration/job |
| [result-a4874ec3d245f7d4f2f3](observations.json)<br>source-797606345fa45914fcd85b71.json<br>`/profiles/qwen27-orca-mtp3-yarn524k/raw_followup/quality` | [ad024-orca-yarn-001](profiles/ad024-orca-yarn-001.md)<br>[qwen27-orca-mtp3-yarn524k](profiles/qwen27-orca-mtp3-yarn524k.md) | quality evaluation | 6 / 8 tasks passed | Task latency median 4.03 s; n=8 | Recorded configuration/job |
| [result-a6b9dce611b0f20f30fd](observations.json)<br>source-797606345fa45914fcd85b71.json<br>`/profiles/qwen27-orca-mtp3-yarn524k/quality` | [qwen27-orca-mtp3-yarn524k](profiles/qwen27-orca-mtp3-yarn524k.md) | quality evaluation | 7 / 8 tasks passed | coding: 2 / 2; tool: 2 / 2; agent: 2 / 2; reasoning: 1 / 2; Task latency median 4.03 s; n=8 | Recorded configuration/job |
| [result-c3031a616e65ba09b694](observations.json)<br>source-e3b968cfd704593190938f6e.json<br>`/grades/original` | [record-26c850ec689cf58c6b67](profiles/record-26c850ec689cf58c6b67.md)<br>[record-7f0ad416bef4c826bba4](profiles/record-7f0ad416bef4c826bba4.md)<br>[record-d03ade5e113afe82b120](profiles/record-d03ade5e113afe82b120.md) | quality evaluation | 22 / 32 tasks passed | coding: 7 / 8; multi_step_agent: 4 / 8; reasoning: 5 / 8; tool_format: 6 / 8 | Exact configuration unresolved |
| [result-c9498a38e85a1cae44f0](observations.json)<br>source-0da06bd9a8d7bfaaf6d8cec8.json<br>`/arms/awq` | [checkpoint-quality-apex-awq](profiles/checkpoint-quality-apex-awq.md)<br>[record-26c850ec689cf58c6b67](profiles/record-26c850ec689cf58c6b67.md) | quality evaluation | 27 / 32 tasks passed | coding: 8 / 8; multi_step_agent: 5 / 8; reasoning: 7 / 8; tool_format: 7 / 8 | Recorded configuration/job |
| [result-e04c9601d6963dcbcc1d](observations.json)<br>source-797606345fa45914fcd85b71.json<br>`/profiles/apex-abliterated-awq-dflash2-pp3-balanced/raw_followup/quality` | [ad025-apex-awq-dflash2-pp3-balanced-000](profiles/ad025-apex-awq-dflash2-pp3-balanced-000.md)<br>[apex-abliterated-awq-dflash2-pp3-balanced](profiles/apex-abliterated-awq-dflash2-pp3-balanced.md) | quality evaluation | 8 / 8 tasks passed | Task latency median 3.21 s; n=8 | Recorded configuration/job |
| [result-e48ad9ea6e558c27a63d](observations.json)<br>source-1b88b19bb8d1f6b6f26ce856.json<br>`/mathematical_historical_evaluation/arms/original` | [record-26c850ec689cf58c6b67](profiles/record-26c850ec689cf58c6b67.md) | quality evaluation | 22 / 32 tasks passed | coding: 7 / 8; multi_step_agent: 4 / 8; reasoning: 5 / 8; tool_format: 6 / 8 | Exact configuration unresolved |

Quoted score summaries without the task records are [listed separately](observations/quoted_quality_score.md). Correctness gates, including failed checks and greedy-reference comparisons, are [separate bounded evidence](observations/correctness_check.md).

[Exact JSON](observations.json) | [CSV](observations.csv) | [All results](OBSERVATIONS.md) | [Archive](../README.md)
