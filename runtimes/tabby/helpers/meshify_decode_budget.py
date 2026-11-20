"""Keep output allocation chunks independent of bounded prefill workspace."""
import functools


def validate_budget(value, prefill_chunk=256):
    if (type(value) is not int or not 256 <= value <= 8192 or value % 256
            or type(prefill_chunk) is not int or value < prefill_chunk):
        raise ValueError('Output chunk must be page-aligned,256-8192 tokens,and at least the prefill chunk')
    return value


def install(container_class, budget):
    budget = validate_budget(budget)
    if hasattr(container_class, '_meshify_output_budget'):
        raise ValueError('An output-budget override is already installed')
    original = container_class.job_max_rq_tokens

    @functools.wraps(original)
    def job_max_rq_tokens(self, max_tokens):
        if self.max_rq_tokens is None or max_tokens <= 0:
            return original(self, max_tokens)
        validate_budget(budget, self.chunk_size)
        # Short completions reserve their exact length; longer ones still requeue.
        return None if 0 < max_tokens <= budget else budget

    container_class.job_max_rq_tokens = job_max_rq_tokens
    container_class._meshify_output_budget = budget
    return original
