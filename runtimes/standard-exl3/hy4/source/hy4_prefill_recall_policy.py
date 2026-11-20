'Opt in to the exact measured HY4 prompt-recall geometry for long tests.'

from contextlib import contextmanager

from functools import partial

from types import FunctionType

import hy4_chunked_prefill as prefill

@contextmanager
def use_recall(policy):
    original = prefill.prompt_recall
    if policy["method"] == "measured_query_and_key_tiles":
        prefill.prompt_recall = FunctionType(original.__code__, {**original.__globals__,
            "QUERY_TILE": policy["query_tile"], "KEY_TILE": policy["key_tile"]},
            argdefs=original.__defaults__)
    elif policy["method"] == "measured_causal_topk":
        from hy4_prompt_recall_topk import prompt_recall_topk

        prefill.prompt_recall = partial(prompt_recall_topk, query_tile=policy["query_tile"],
                                       key_tile=policy["key_tile"], split_ragged=policy["split_ragged"])
    try:
        yield
    finally:
        prefill.prompt_recall = original
