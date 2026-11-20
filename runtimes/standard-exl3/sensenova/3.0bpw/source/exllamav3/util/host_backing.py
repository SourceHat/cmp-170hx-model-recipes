"""Optional hugepage-backed host tensors; use only already-reserved pools."""
import ctypes
import logging
import math
import os
from pathlib import Path
import re
import weakref

import torch

log = logging.getLogger(__name__)
_mappings = {}
libc = ctypes.CDLL(None, use_errno=True)
libc.mmap.argtypes = [ctypes.c_void_p, ctypes.c_size_t, ctypes.c_int,
                      ctypes.c_int, ctypes.c_int, ctypes.c_size_t]
libc.mmap.restype = ctypes.c_void_p
libc.munmap.argtypes = [ctypes.c_void_p, ctypes.c_size_t]
libc.munmap.restype = ctypes.c_int
libc.madvise.argtypes = [ctypes.c_void_p, ctypes.c_size_t, ctypes.c_int]
libc.madvise.restype = ctypes.c_int


def pool_free(page_bytes):
    root=Path('/sys/kernel/mm/hugepages')/f'hugepages-{page_bytes//1024}kB'
    try:
        return int((root/'free_hugepages').read_text()) - int((root/'resv_hugepages').read_text())
    except (OSError,ValueError):
        return 0


def _release(pointer,length,registered):
    if registered:
        try:
            # External registrations do not belong to Torch's event-tracked
            # pinned allocator. Drain users on every job-visible device first.
            for device in range(torch.cuda.device_count()):
                torch.cuda.synchronize(device)
            result=torch.cuda.cudart().cudaHostUnregister(pointer)
            if result.value:
                log.warning('Host unregister failed; retaining the mapped region: %s',result)
                return
        except Exception:
            log.exception('CUDA unavailable while releasing host backing; retaining the mapping')
            return
    if libc.munmap(pointer,length):
        log.warning('munmap failed for host backing: errno=%d',ctypes.get_errno())
    else:
        _mappings.pop(pointer,None)


def mapped_tensor(shape,dtype,*,pin=False,page_bytes=None,thp=False):
    nbytes=math.prod(shape)*torch.empty(0,dtype=dtype).element_size()
    quantum=page_bytes or 4096
    length=-(-nbytes//quantum)*quantum
    if length <= 0:
        raise ValueError('Map a nonempty host tensor')
    flags=0x02|0x20
    if page_bytes:
        flags |= 0x40000|((page_bytes.bit_length()-1)<<26)
    pointer=libc.mmap(None,length,3,flags,-1,0)
    if pointer is None or pointer==ctypes.c_void_p(-1).value:
        raise OSError(ctypes.get_errno(),'Host mmap failed')
    registered=False
    try:
        if thp and libc.madvise(pointer,length,14):
            raise OSError(ctypes.get_errno(),'MADV_HUGEPAGE refused')
        # Torch owns this buffer object until the last storage/view disappears.
        # A raw libc mapping avoids Python mmap.close's exported-buffer failure.
        owner=(ctypes.c_ubyte*length).from_address(pointer)
        region=torch.frombuffer(owner,dtype=torch.uint8)
        result=region[:nbytes].view(dtype).view(shape)
        if pin:
            if not torch.cuda.is_initialized():
                torch.cuda.init()
            status=torch.cuda.cudart().cudaHostRegister(pointer,length,3)
            if status.value:
                raise RuntimeError(f'CUDA host registration failed: {status}')
            registered=True
            if not result.is_pinned():
                raise RuntimeError('CUDA did not acknowledge host registration')
        finalizer=weakref.finalize(owner,_release,pointer,length,registered)
        finalizer.atexit=False
        _mappings[pointer]=dict(length=length,registered=registered,
                               requested='hugetlb' if page_bytes else 'thp' if thp else 'mapped_ordinary')
        return result
    except BaseException:
        _release(pointer,length,registered)
        raise


def host_tensor(shape,dtype,*,pin=False,name=''):
    nbytes=math.prod(shape)*torch.empty(0,dtype=dtype).element_size()
    mode=os.environ.get('MESHIFY_HOST_BACKING','ordinary')
    if mode not in ('ordinary','hugetlb','thp'):
        raise ValueError('Unknown host backing mode')
    if mode=='hugetlb' and nbytes >= 2*1024**2:
        for page_bytes in (1024**3,2*1024**2):
            pages=-(-nbytes//page_bytes)
            if pages*page_bytes > 2*nbytes or pool_free(page_bytes)<pages:
                continue
            try:
                result=mapped_tensor(shape,dtype,pin=pin,page_bytes=page_bytes)
                log.info('Host backing %s: %d-byte hugetlb pages, %d bytes, pinned=%s',
                         name,page_bytes,nbytes,pin)
                return result
            except (OSError,RuntimeError) as exc:
                log.info('Host hugetlb tier unavailable for %s: %s',name,exc)
    if mode=='thp' and nbytes >= 2*1024**2:
        try:
            result=mapped_tensor(shape,dtype,pin=pin,thp=True)
            log.info('Host backing %s: MADV_HUGEPAGE requested, %d bytes, pinned=%s; actual backing requires smaps',
                     name,nbytes,pin)
            return result
        except (OSError,RuntimeError) as exc:
            log.info('Host THP request unavailable for %s: %s',name,exc)
    log.info('Host backing %s: ordinary pages, %d bytes, pinned=%s',name,nbytes,pin)
    return torch.empty(shape,dtype=dtype,device='cpu',pin_memory=pin)


def backing_statistics():
    if not _mappings:
        return dict(requested=os.environ.get('MESHIFY_HOST_BACKING','ordinary'),
                    live_custom_mappings=0, mappings=[], actual_hugetlb_bytes=0,
                    actual_transparent_hugepage_bytes=0)
    records=[]
    active=None
    for line in Path('/proc/self/smaps').read_text().splitlines():
        header=re.match(r'^([0-9a-f]+)-([0-9a-f]+) ',line)
        if header:
            start,stop=(int(v,16) for v in header.groups())
            active=None
            for pointer,row in list(_mappings.items()):
                if start<=pointer<stop:
                    active=dict(row,KernelPageSize_kB=None,AnonHugePages_kB=0,
                                Private_Hugetlb_kB=0,Shared_Hugetlb_kB=0)
                    records.append(active)
                    break
        elif active is not None:
            for name in ('KernelPageSize','AnonHugePages','Private_Hugetlb','Shared_Hugetlb'):
                if line.startswith(name+':'):
                    active[name+'_kB']=int(line.split()[1])
    return dict(requested=os.environ.get('MESHIFY_HOST_BACKING','ordinary'),
        live_custom_mappings=len(_mappings),mappings=records,
        actual_hugetlb_bytes=sum((r['Private_Hugetlb_kB']+r['Shared_Hugetlb_kB'])*1024 for r in records),
        actual_transparent_hugepage_bytes=sum(r['AnonHugePages_kB']*1024 for r in records))
