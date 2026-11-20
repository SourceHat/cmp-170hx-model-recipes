'Compare long-context decode paths on the same resident weights and cache.'

def activate(runtime, choices):
    choices = {n: mode for n, mode in choices.items() if runtime.selected(tuple(range(n)))
               and not (n == 4 and runtime.pipeline)}
    runtime.reuse_recall_widths = frozenset(choices)
    widths = frozenset(n for n, mode in choices.items() if mode.startswith("sliding_"))
    if choices.get(4) == "sliding_compact":
        runtime.mixed_recall_min, runtime.mixed_recall_max, runtime.mixed_recall_rows = 2048, 4096, 1
    runtime.fused_recall_widths = frozenset(n for n, mode in choices.items() if mode == "sliding_fused_gather")
    runtime.fused_recall_limit = 4096 if runtime.fused_recall_widths else None
    if widths:
        if runtime.dense_graphs is None:
            runtime.enable_rank_graphs(())
        runtime.dense_graphs.long_lanes = widths
    return choices
