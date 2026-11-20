"""Plan a bounded FP16 workspace without inspecting device data."""


def workspace_layout(batch, pages_per_sequence, pool_pages, kv_heads, head_dim, budget_bytes,
                     page_size=256):
    values = (batch, pages_per_sequence, pool_pages, kv_heads, head_dim, budget_bytes, page_size)
    if any(type(value) is not int or value < 1 for value in values):
        raise ValueError('Workspace dimensions and budget must be positive integers')
    if head_dim % 32:
        raise ValueError('Quantized attention head dimensions must be multiples of 32')
    pages = batch * pages_per_sequence
    rounded = min(1 << (pages - 1).bit_length(), max(pages, pool_pages))
    per_head = rounded * page_size * head_dim * 4
    if per_head > budget_bytes:
        rounded = pages
        per_head = rounded * page_size * head_dim * 4
    if per_head > budget_bytes:
        return None
    heads = max(value for value in range(1, kv_heads + 1)
                if kv_heads % value == 0 and value * per_head <= budget_bytes)
    return {'pages': rounded, 'head_group': heads, 'bytes': heads * per_head}
