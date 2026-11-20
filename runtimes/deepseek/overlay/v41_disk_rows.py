"""Bounded raw Engram row reads; decoding remains in the GPU runtime."""
from collections import OrderedDict
import json
import os
from pathlib import Path
import struct


def descriptor(root, index, key):
    name = index[key]
    if Path(name).name != name:
        raise ValueError('Engram shard name must be a flat local file')
    path = (root / name).resolve()
    if not path.is_relative_to(root):
        raise ValueError('Engram shard leaves the admitted directory')
    with path.open('rb') as stream:
        prefix = stream.read(8)
        if len(prefix) != 8:
            raise ValueError('Truncated Engram header')
        length = struct.unpack('<Q', prefix)[0]
        if not 2 <= length <= 128 * 1024**2:
            raise ValueError('Engram header exceeds the admitted size')
        header = json.loads(stream.read(length))
    tensor = header[key]
    start, end = tensor['data_offsets']
    if not 0 <= start <= end or 8 + length + end > path.stat().st_size:
        raise ValueError('Engram tensor exceeds its file')
    return path, tensor, 8 + length + start


class DiskRows:
    """Cache packed bytes, preserving original FP8 values and block scales."""
    def __init__(self, root, prefix, rows, dim, *, cache_bytes=64 * 1024**2):
        if not isinstance(cache_bytes, int) or cache_bytes < 0:
            raise ValueError('Engram cache budget must be nonnegative')
        self.root = Path(root).resolve()
        index = json.loads((self.root / 'model.safetensors.index.json').read_text())['weight_map']
        weight = descriptor(self.root, index, prefix + '.embed.weight')
        scale = descriptor(self.root, index, prefix + '.embed.scale')
        if weight[1]['shape'] != [rows, dim] or weight[1]['dtype'] != 'F8_E4M3':
            raise ValueError('Engram weight geometry differs')
        if dim % 32 or scale[1]['shape'] != [rows, dim // 32] or scale[1]['dtype'] != 'F8_E8M0':
            raise ValueError('Engram scale geometry differs')
        for field, size in ((weight, rows * dim), (scale, rows * (dim // 32))):
            begin, end = field[1]['data_offsets']
            if end - begin != size:
                raise ValueError('Engram byte span differs from its geometry')
        self.rows, self.dim, self.scale_dim = rows, dim, dim // 32
        self.weight_offset, self.scale_offset = weight[2], scale[2]
        self.weight_fd = os.open(weight[0], os.O_RDONLY | os.O_CLOEXEC)
        try:
            self.scale_fd = os.open(scale[0], os.O_RDONLY | os.O_CLOEXEC)
        except Exception:
            os.close(self.weight_fd)
            self.weight_fd = None
            raise
        self.cache = OrderedDict()
        self.cache_bytes = cache_bytes
        # Include Python key/value/LRU overhead in the admitted RAM budget.
        self.row_charge = dim + self.scale_dim + 512
        self.max_cached_rows = max(0, cache_bytes // self.row_charge)
        self.hits = self.misses = self.evictions = self.disk_bytes = 0

    def close(self):
        for name in ('weight_fd', 'scale_fd'):
            fd = getattr(self, name, None)
            if fd is not None:
                os.close(fd)
                setattr(self, name, None)

    def __del__(self):
        self.close()

    def row(self, row):
        if not isinstance(row, int) or isinstance(row, bool):
            raise ValueError('Engram index must be an integer')
        if not 0 <= row < self.rows:
            return bytes(self.dim + self.scale_dim)
        found = self.cache.get(row)
        if found is not None:
            self.cache.move_to_end(row)
            self.hits += 1
            return found
        data = os.pread(self.weight_fd, self.dim, self.weight_offset + row * self.dim)
        scale = os.pread(self.scale_fd, self.scale_dim, self.scale_offset + row * self.scale_dim)
        if len(data) != self.dim or len(scale) != self.scale_dim:
            raise OSError('Short Engram row read')
        result = data + scale
        self.misses += 1
        self.disk_bytes += len(result)
        if self.max_cached_rows:
            self.cache[row] = result
            if len(self.cache) > self.max_cached_rows:
                self.cache.popitem(last=False)
                self.evictions += 1
        return result

    def gather(self, rows):
        if len(rows) > 131072:
            raise ValueError('Engram gather exceeds the bounded workspace')
        data = bytearray(len(rows) * self.dim)
        scales = bytearray(len(rows) * self.scale_dim)
        for n, row in enumerate(rows):
            packed = self.row(row)
            data[n*self.dim:(n+1)*self.dim] = packed[:self.dim]
            scales[n*self.scale_dim:(n+1)*self.scale_dim] = packed[self.dim:]
        return data, scales

    def metrics(self):
        return {'hits': self.hits, 'misses': self.misses, 'evictions': self.evictions,
                'disk_bytes': self.disk_bytes, 'cached_rows':len(self.cache),
                'conservative_cache_charge_bytes':len(self.cache)*self.row_charge,
                'cache_limit_bytes':self.cache_bytes}
