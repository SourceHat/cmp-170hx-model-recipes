"Dispatch HY4's existing packed experts without per-matrix Python calls."

import torch

from hy4_gpu_groups import GpuGroupedExperts

from hy4_standard_expert_pack import PackedExperts

DISPATCH = {"gpu_groups": GpuGroupedExperts}

def resident_dispatch(target, mode):
    result = {}
    for block in target.blocks:
        if isinstance(block.mlp, PackedExperts):
            with torch.cuda.device(block.device):
                result[block.mlp] = DISPATCH[mode](block.mlp)
    return result

def activate_gpu_runner(target, *, fused=True, compact=True):
    import hy4_chunked_prefill
    from hy4_engram_read_ahead import EngramReadAhead

    dispatches = resident_dispatch(target, "gpu_groups")
    for packed, dispatch in dispatches.items():
        packed.forward = dispatch
        packed.gpu_expert_prefill = dispatch.prefill
    target.verified_panel_experts = dispatches
    target.verified_panel_compact = compact
    target.engram_read_ahead = EngramReadAhead(target)
    prior = hy4_chunked_prefill.packed_prefill
    if not getattr(prior, "gpu_dispatch_ready", False):
        def gpu_prefill(packed, hidden):
            fast = getattr(packed, "gpu_expert_prefill", None)
            return fast(hidden) if fast is not None and hidden.shape[1] > 1 else prior(packed, hidden)

        gpu_prefill.gpu_dispatch_ready = True
        hy4_chunked_prefill.packed_prefill = gpu_prefill
    if fused:
        from hy4_fused_mla import attention

        target.device_attention = attention
    return dispatches
