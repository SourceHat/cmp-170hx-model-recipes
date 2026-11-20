'Measure an independently loaded full HY4 target and the native DFly2 parity gate.'

import torch

from hy4_shared_pool import LANES

def align_devices(devices):
    for d in devices:
        torch.cuda.synchronize(d)

def reset(target):
    if target.trial is not None or target.pool.pending is not None:
        raise ValueError("Drain verification before recycling the four lanes")
    for block in target.blocks:
        a = block.attention
        with torch.cuda.device(block.device):
            if block.sparse:
                if a.working is not None or a.index.trial is not None:
                    raise ValueError("The indexed trial must be committed before replay")
                a.index.lengths.zero_()
                a.index.partial.zero_()
                a.index.first.zero_()
            else:
                for lane in range(LANES):
                    a.cache.release(lane)
    for lane in range(LANES):
        target.pool.release(lane)
    target.tail.fill_(target.cfg.engram_pad_id)
