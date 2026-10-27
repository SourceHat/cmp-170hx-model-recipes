#!/usr/bin/env python3
"""Stage the performance-sensitive Engram tables on an operator-selected NVMe path."""
import argparse
import hashlib
import json
import os
from pathlib import Path
import shutil
import sys
import time

from transform_v41_tp3 import read_header


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--source-receipt', type=Path, required=True)
    parser.add_argument('--destination', type=Path, required=True)
    args = parser.parse_args()
    manifest = json.loads(args.source_receipt.read_text())
    if manifest['revision'] != '982b70452f399814f56b46272fd30394ae10d58c':
        raise ValueError('Engram staging requires the pinned V4.1 checkpoint')
    entries = {e['name']:e for e in manifest['files']}
    names = ['model-00047-of-00048.safetensors','model-00048-of-00048.safetensors']
    source = Path(manifest['directory']).resolve()
    required = sum(entries[n]['bytes'] for n in names)
    args.destination.mkdir(parents=True, exist_ok=False)
    root = args.destination.resolve()
    if shutil.disk_usage(root).free < required:
        raise ValueError('The destination has insufficient space for the Engram tables')
    report = {'started_at':time.time(), 'source_receipt':str(args.source_receipt),
              'destination':str(root), 'revision':manifest['revision'], 'files':[],
              'passed':False, 'scope':'Live lookup cache only;original model stays on SATA'}
    report_path = root/'meshify-staging.json'
    try:
        index = {}
        for name in names:
            original = source/name
            before = original.stat()
            if before.st_size != entries[name]['bytes']:
                raise ValueError('Source table size differs')
            temporary, target = root/(name+'.incomplete'), root/name
            checksum = hashlib.sha256()
            with original.open('rb',buffering=0) as src, temporary.open('xb',buffering=0) as dst:
                while block := src.read(8 * 1024**2):
                    if dst.write(block) != len(block):
                        raise OSError('Short Engram cache write')
                    checksum.update(block)
                os.fsync(dst.fileno())
            if checksum.hexdigest() != entries[name]['lfs_sha256']:
                raise ValueError('Source table SHA256 differs')
            after = original.stat()
            if (before.st_dev,before.st_ino,before.st_size,before.st_mtime_ns) != (
                    after.st_dev,after.st_ino,after.st_size,after.st_mtime_ns):
                raise ValueError('Source table changed during staging')
            with temporary.open('rb') as stream:
                copied_hash = hashlib.file_digest(stream,'sha256').hexdigest()
            if copied_hash != checksum.hexdigest():
                raise ValueError('NVMe readback differs from the pinned table')
            temporary.replace(target)
            with target.open('rb') as stream:
                header,_ = read_header(stream)
            for key in header:
                if key != '__metadata__':
                    if key in index:
                        raise ValueError('Duplicate staged Engram tensor')
                    index[key] = name
            report['files'].append({'name':name,'bytes':before.st_size,'sha256':copied_hash})
            report_path.write_text(json.dumps(report,indent=2)+'\n')
            print(json.dumps({'staged_and_readback_verified':name,'sha256':copied_hash}),flush=True)
        (root/'model.safetensors.index.json').write_text(json.dumps({'weight_map':index},indent=2)+'\n')
        report['passed'] = True
    except Exception as error:
        report['error'] = f'{type(error).__name__}: {error}'
        raise
    finally:
        report['finished_at'] = time.time()
        report_path.write_text(json.dumps(report,indent=2)+'\n')


if __name__=='__main__':
    main()
