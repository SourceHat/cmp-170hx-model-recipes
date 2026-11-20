'Read the four NVMe backed Engram tables ahead of their decode layers.'

from concurrent.futures import ThreadPoolExecutor

import mmap

import torch

from host_engram import decode

from hy4_engram import hash_rows

from hy4_engram import ngram_tokens

class EngramReadAhead:
    def __init__(self, target):
        self.blocks = tuple(block for block in target.blocks if block.engram is not None)
        self.pool = ThreadPoolExecutor(max_workers=max(len(self.blocks), 1), thread_name_prefix="hy4-engram")
        self.single_hash = None
        self.decode_gathers = {}
        for block in self.blocks:
            layer = block.engram
            table = layer.table
            # Preserve the original reader if this table was loaded before the new hook.
            self.decode_gathers[layer] = getattr(table, "gather_decode", table.gather)
            for _, _, rows in table.shards:
                # Token hashes are random; sequential read-ahead fills RAM with unused pages.
                rows._mmap.madvise(mmap.MADV_RANDOM)

    @staticmethod
    def read(gather, ready, indices):
        ready.synchronize()
        return torch.from_numpy(gather(indices.numpy())).pin_memory()

    def submit(self, ids, history, starts):
        local, pending = {}, {}
        for block in self.blocks:
            layer, device = block.engram, block.device
            cfg = layer.cfg
            with torch.cuda.device(device):
                if device not in local:
                    local[device] = (ids.to(device), history.to(device),
                                     torch.tensor(starts, device=device)[:, None])
                tokens, prefix, positions = local[device]
                if tokens.shape[1] > 1:
                    positions = positions + torch.arange(tokens.shape[1], device=device)
                pad = cfg.engram_pad_id
                if self.single_hash is not None and tokens.shape[1] == 1:
                    rows, valid = self.single_hash(layer, tokens, prefix, positions)
                else:
                    grams = ngram_tokens(tokens, positions, cfg.engram_max_ngram_size, pad, history=prefix)
                    rows = hash_rows(grams, layer.lookup, pad, layer.sizes, layer.offsets, layer.multipliers,
                                     cfg.engram_n_head_per_ngram)
                    valid = (tokens != pad) & (tokens < layer.lookup.numel())
                staging = torch.empty(rows.shape, dtype=rows.dtype, device="cpu", pin_memory=True)
                staging.copy_(rows, non_blocking=True)
                ready = torch.cuda.Event(blocking=True)
                ready.record()
                gather = self.decode_gathers[layer] if tokens.shape[1] == 1 else layer.table.gather
                pending[layer] = (self.pool.submit(self.read, gather, ready, staging), valid)
        return pending

    @staticmethod
    def take(layer, item):
        task, mask = item
        packed = task.result().to(layer.lookup.device, non_blocking=True)
        return decode(packed, layer.lut), mask
