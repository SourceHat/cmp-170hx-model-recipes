'Read packed HY4 Engram rows from immutable host mappings in bounded batches.'

import json

from pathlib import Path

import struct

import numpy as np

from hy4_engram import FORMAT

from source import REVISION

class HostEngram:
    def __init__(self, receipts, tensor, expected_rows, width, max_ids=16384):
        if expected_rows <= 0 or width <= 0 or width % 2 or max_ids <= 0:
            raise ValueError("Invalid host Engram geometry or lookup budget")
        self.shards = []
        self.rows, self.width, self.max_ids = expected_rows, width, max_ids
        stride = width + 2
        cursor = 0
        for rank, record in enumerate(receipts):
            ident = record["identity"]
            path = Path(record["path"])
            if (record["status"], ident["revision"], ident["tensor"], ident["format"], ident["rank"], ident["width"],
                ident["start"]) != ("verified", REVISION, tensor, FORMAT, rank, width, cursor):
                raise ValueError(f"Unexpected Engram shard or rank order: {path.name}")
            end = ident["end"]
            if (not cursor < end <= expected_rows or record["rows_committed"] != end - cursor or
                    path.stat().st_size != record["bytes"]):
                raise ValueError(f"Incomplete or changed Engram shard: {path.name}")
            with path.open("rb") as f:
                length, = struct.unpack("<Q", f.read(8))
                if not 2 <= length <= 1024**2:
                    raise ValueError("Invalid packed Engram header length")
                header = json.loads(f.read(length))
            payload = (end - cursor) * stride
            meta = header["__metadata__"]
            if (header["rows"] != {"dtype": "U8", "shape": [end-cursor, stride], "data_offsets": [0, payload]} or
                (meta["source_revision"], meta["source_tensor"], meta["format"], meta["row_start"], meta["row_end"]) !=
                    (REVISION, tensor, FORMAT, str(cursor), str(end)) or record["bytes"] != 8 + length + payload):
                raise ValueError(f"Wrong packed Engram byte layout: {path.name}")
            mapped = np.memmap(path, dtype=np.uint8, mode="r", offset=8 + length, shape=(end-cursor, stride))
            self.shards.append((cursor, end, mapped))
            cursor = end
        if cursor != expected_rows:
            raise ValueError("Host Engram tables do not cover the requested tensor")

    def gather(self, ids):
        """Deduplicate and read only the requested rows; -1 represents a masked lookup."""
        ids = np.asarray(ids)
        if not np.issubdtype(ids.dtype, np.signedinteger) or not 0 < ids.size <= self.max_ids:
            raise ValueError("Split Engram prefill into bounded integer lookup chunks")
        keys, inverse = np.unique(ids.reshape(-1), return_inverse=True)
        if keys[0] < -1 or keys[-1] >= self.rows:
            raise ValueError("Engram row ID lies outside its verified table")
        result = np.zeros((len(keys), self.width + 2), dtype=np.uint8)
        for start, end, mapped in self.shards:
            left, right = keys.searchsorted((start, end))
            if left != right:
                result[left:right] = mapped[keys[left:right] - start]
        return result[inverse].reshape(*ids.shape, self.width + 2)

    def gather_decode(self, ids):
        """Read up to four single-token requests without sorting the row IDs."""
        keys = ids.reshape(-1)
        if not np.issubdtype(keys.dtype, np.signedinteger) or not 0 < keys.size <= 64:
            return self.gather(ids)
        first, last = keys.min(), keys.max()
        if first < -1 or last >= self.rows:
            raise ValueError("Engram row ID lies outside its verified table")
        for start, end, mapped in self.shards:
            if start <= first and last < end:
                return mapped[ids - start]
        data = np.zeros((keys.size, self.width + 2), dtype=np.uint8)
        for start, end, mapped in self.shards:
            use = (keys >= start) & (keys < end)
            if use.any():
                data[use] = mapped[keys[use] - start]
        return data.reshape(*ids.shape, self.width + 2)

def decode(packed, lut):
    import torch

    if packed.dtype != torch.uint8 or packed.shape[-1] < 4 or packed.shape[-1] % 2 or lut.shape != (256,):
        raise ValueError("Invalid host Engram staging tensor")
    raw = packed[..., :-2].long()
    scale = packed[..., -2:].view(torch.bfloat16)
    return lut[raw] * scale
