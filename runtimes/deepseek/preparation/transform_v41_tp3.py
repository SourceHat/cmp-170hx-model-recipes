#!/usr/bin/env python3
"""Build a TP3 checkpoint by padding attention tensors without requantization."""
import argparse
import copy
import hashlib
import json
import math
import os
from pathlib import Path
import struct
import time

from v41_tp3_geometry import padding_spec, validate_source_config


CHUNK = 8 * 1024**2
WIDTHS = {'BOOL': 1, 'U8': 1, 'I8': 1, 'F8_E4M3': 1, 'F8_E5M2': 1,
          'F8_E8M0': 1, 'I16': 2, 'U16': 2, 'F16': 2, 'BF16': 2,
          'I32': 4, 'U32': 4, 'F32': 4, 'I64': 8, 'U64': 8, 'F64': 8}


def read_header(stream):
    prefix = stream.read(8)
    if len(prefix) != 8:
        raise ValueError('Truncated safetensors prefix')
    length = struct.unpack('<Q', prefix)[0]
    if not 2 <= length <= 128 * 1024**2:
        raise ValueError('Safetensors header exceeds the admitted size')
    raw = stream.read(length)
    if len(raw) != length:
        raise ValueError('Truncated safetensors header')
    return json.loads(raw), prefix + raw


def tensor_bytes(metadata):
    shape = metadata['shape']
    if any(not isinstance(n, int) or n < 0 for n in shape):
        raise ValueError('Invalid tensor shape')
    return math.prod(shape) * WIDTHS[metadata['dtype']]


class HashedWriter:
    def __init__(self, stream):
        self.stream, self.hasher = stream, hashlib.sha256()

    def write(self, block):
        if self.stream.write(block) != len(block):
            raise OSError('Short checkpoint write')
        self.hasher.update(block)


def transfer(stream, output, source_hash, count):
    while count:
        block = stream.read(min(count, CHUNK))
        if not block:
            raise ValueError('Truncated tensor data')
        source_hash.update(block)
        output.write(block)
        count -= len(block)


def fill(output, pattern, count):
    if not pattern or count % len(pattern):
        raise ValueError('Padding does not align to the tensor dtype')
    block = pattern * min(CHUNK // len(pattern), count // len(pattern))
    while count:
        part = block[:min(count, len(block))]
        output.write(part)
        count -= len(part)


def rewrite_shard(source, destination, expected_sha256, spec_for=padding_spec):
    """Stream original rows, append zero/unit/negative-infinity padding, verify input."""
    if destination.exists() or destination.is_symlink():
        raise FileExistsError('Checkpoint output already exists: ' + str(destination))
    before = source.stat()
    temporary = destination.with_name(destination.name + '.incomplete')
    changes = {}
    with source.open('rb', buffering=CHUNK) as stream:
        header, original_header = read_header(stream)
        source_hash = hashlib.sha256(original_header)
        ordered = sorted((k for k in header if k != '__metadata__'),
                         key=lambda k: header[k]['data_offsets'][0])
        rewritten = {'__metadata__': copy.deepcopy(header.get('__metadata__', {}))}
        original_offset = new_offset = 0
        for key in ordered:
            metadata = header[key]
            size = tensor_bytes(metadata)
            if metadata['data_offsets'] != [original_offset, original_offset + size]:
                raise ValueError('Noncontiguous source tensor: ' + key)
            original_offset += size
            spec = spec_for(key, metadata)
            result = copy.deepcopy(metadata)
            if spec:
                if len(spec['shape']) != len(metadata['shape']) or len(spec['shape']) not in (1, 2):
                    raise ValueError('Only one/two-dimensional padding is supported')
                if any(b < a for a, b in zip(metadata['shape'], spec['shape'])):
                    raise ValueError('Padding cannot discard original tensor values')
                if len(spec['fill']) != WIDTHS[metadata['dtype']]:
                    raise ValueError('Fill bytes do not match the tensor dtype')
                result['shape'] = spec['shape']
                changes[key] = {'before': metadata['shape'], 'after': spec['shape']}
            new_size = tensor_bytes(result)
            result['data_offsets'] = [new_offset, new_offset + new_size]
            new_offset += new_size
            rewritten[key] = result
        if before.st_size != len(original_header) + original_offset:
            raise ValueError('Source file has missing or unindexed tensor data')
        raw = json.dumps(rewritten, separators=(',', ':')).encode('utf-8')
        raw += b' ' * (-len(raw) % 8)
        with temporary.open('xb', buffering=CHUNK) as target:
            output = HashedWriter(target)
            output.write(struct.pack('<Q', len(raw)) + raw)
            for key in ordered:
                metadata = header[key]
                spec = spec_for(key, metadata)
                if not spec:
                    transfer(stream, output, source_hash, tensor_bytes(metadata))
                    continue
                width = WIDTHS[metadata['dtype']]
                if len(metadata['shape']) == 1:
                    transfer(stream, output, source_hash, tensor_bytes(metadata))
                    fill(output, spec['fill'], tensor_bytes(rewritten[key]) - tensor_bytes(metadata))
                else:
                    old_rows, old_cols = metadata['shape']
                    new_rows, new_cols = spec['shape']
                    if old_cols == new_cols:
                        transfer(stream, output, source_hash, tensor_bytes(metadata))
                    else:
                        for _ in range(old_rows):
                            transfer(stream, output, source_hash, old_cols * width)
                            fill(output, spec['fill'], (new_cols - old_cols) * width)
                    fill(output, spec['fill'], (new_rows - old_rows) * new_cols * width)
            target.flush()
            os.fsync(target.fileno())
            output_hash = output.hasher.hexdigest()
        if source_hash.hexdigest() != expected_sha256:
            raise ValueError('Source SHA256 differs: ' + source.name)
    after = source.stat()
    if (before.st_dev, before.st_ino, before.st_size, before.st_mtime_ns) != (
            after.st_dev, after.st_ino, after.st_size, after.st_mtime_ns):
        raise ValueError('Source checkpoint changed during the transform')
    temporary.replace(destination)
    return {'source': str(source), 'source_sha256': expected_sha256,
            'output': str(destination), 'output_sha256': output_hash,
            'output_bytes': destination.stat().st_size, 'changes': changes}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--source', type=Path, required=True)
    parser.add_argument('--source-manifest', type=Path, required=True)
    parser.add_argument('--destination', type=Path, required=True)
    parser.add_argument('--allow-pending-engram', action='store_true')
    args = parser.parse_args()
    source = args.source.resolve()
    manifest = json.loads(args.source_manifest.read_text())
    if manifest['repository'] != 'sfxnz/DeepSeek-V4.1-Flash-EXL3' or manifest['revision'] != (
            '982b70452f399814f56b46272fd30394ae10d58c'):
        raise ValueError('Checkpoint manifest is not the pinned candidate')
    config = json.loads((source / 'config.json').read_text())
    validate_source_config(config)
    args.destination.mkdir(parents=True, exist_ok=False)
    report = {'started_at': time.time(), 'source': str(source),
              'revision': manifest['revision'], 'files': [], 'passed': False,
              'pending_engram': [], 'gpu_validated': False,
              'transform': '64->72 attention heads,8->9 output groups;no requantization'}
    path = args.destination / 'meshify-transform.json'
    try:
        index = {}
        for entry in manifest['files']:
            relative = Path(entry['name'])
            if relative.name != str(relative):
                raise ValueError('Only flat pinned checkpoint files are admitted')
            target, original = args.destination / relative, source / relative
            if not original.exists():
                if args.allow_pending_engram and relative.name in (
                        'model-00047-of-00048.safetensors', 'model-00048-of-00048.safetensors'):
                    report['pending_engram'].append(relative.name)
                    continue
                raise ValueError('Missing source artifact: ' + str(relative))
            if original.stat().st_size != entry['bytes']:
                raise ValueError('Pinned source size differs: ' + str(relative))
            if relative.suffix != '.safetensors':
                if relative.name not in ('config.json', 'model.safetensors.index.json'):
                    target.symlink_to(original)
                continue
            with original.open('rb') as stream:
                header, _ = read_header(stream)
            changed = any(padding_spec(k, v) for k, v in header.items() if k != '__metadata__')
            if changed:
                row = rewrite_shard(original, target, entry['lfs_sha256'])
                print(json.dumps({'transformed':relative.name, 'tensors':len(row['changes'])}), flush=True)
            else:
                target.symlink_to(original)
                row = {'source':str(original), 'source_sha256':entry['lfs_sha256'],
                       'output':str(target), 'unchanged':True, 'source_verification':'Pending full artifact gate'}
            for key in header:
                if key == '__metadata__':
                    continue
                if key in index:
                    raise ValueError('Duplicate checkpoint tensor: ' + key)
                index[key] = relative.name
            report['files'].append(row)
            path.write_text(json.dumps(report, indent=2) + '\n')
        config['text_config'].update(num_attention_heads=72, o_groups=9)
        (args.destination / 'config.json').write_text(json.dumps(config, indent=2) + '\n')
        (args.destination / 'model.safetensors.index.json').write_text(json.dumps({
            'metadata': {'meshify_source_revision':manifest['revision']}, 'weight_map':index},indent=2)+'\n')
        report['body_transform_passed'] = True
        report['passed'] = not report['pending_engram']
        report['activation_gate'] = 'Full source SHA256 and transformed index verification, runtime and GPU validation still required'
    except Exception as error:
        report['error'] = f'{type(error).__name__}: {error}'
        raise
    finally:
        report['finished_at'] = time.time()
        path.write_text(json.dumps(report, indent=2) + '\n')


if __name__ == '__main__':
    main()
