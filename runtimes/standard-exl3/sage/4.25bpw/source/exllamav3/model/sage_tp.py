"""Sage-private NCCL collectives, including partial-rank uneven gathers."""

from itertools import combinations
from datetime import timedelta
import os

import torch
import torch.distributed as dist


class SageNCCL:
    def __init__(self, device, active_devices, output_device, init_method, master, uuid,
                 shbuf_size=None):
        self.device = device
        self.active_devices = list(active_devices)
        self.stats = {'broadcast_bytes': 0, 'gather_bytes': 0, 'reduce_bytes': 0}
        if device < 0:
            return
        self.rank = active_devices.index(device)
        dist.init_process_group('nccl', rank=self.rank, world_size=len(active_devices),
                                init_method=init_method, device_id=torch.device('cuda', device),
                                timeout=timedelta(seconds=int(os.environ.get('SAGE_NCCL_TIMEOUT_SECONDS', '600'))))
        self.groups = {}
        # Create and warm every subgroup in identical global order, before graph capture.
        for count in range(1, len(active_devices) + 1):
            for devices in combinations(active_devices, count):
                ranks = [active_devices.index(d) for d in devices]
                group = dist.group.WORLD if count == len(active_devices) else dist.new_group(
                    ranks=ranks, backend='nccl')
                self.groups[frozenset(devices)] = group
                if device in devices:
                    warm = torch.ones(1, device=device)
                    dist.all_reduce(warm, group=group)
                    torch.cuda.synchronize(device)

    def close(self):
        if self.device >= 0:
            dist.barrier(device_ids=[self.device])
            # Retire child communicators in a global order before their parent.
            for devices, group in reversed(list(self.groups.items())):
                if group is dist.group.WORLD:
                    continue
                if self.device in devices:
                    dist.barrier(group=group, device_ids=[self.device])
                    dist.destroy_process_group(group)
                dist.barrier(device_ids=[self.device])
            dist.destroy_process_group()

    def fwd_barrier(self):
        if self.device >= 0:
            dist.barrier()

    def broadcast(self, tensor, src_device):
        dist.broadcast(tensor, src=self.active_devices.index(src_device))
        self.stats['broadcast_bytes'] += tensor.numel() * tensor.element_size()

    def all_reduce(self, tensor, contribution=True):
        if not contribution:
            tensor.zero_()
        # Never narrow FP32 payloads to a BF16 wire.
        dist.all_reduce(tensor)
        self.stats['reduce_bytes'] += tensor.numel() * tensor.element_size()

    def gather(self, tensor, out_tensor, gather_devices, out_device, ldims):
        devices = gather_devices.tolist() if isinstance(gather_devices, torch.Tensor) else list(gather_devices)
        widths = [int(width) for width in ldims]
        if len(devices) != len(widths) or len(set(devices)) != len(devices):
            raise ValueError('Gather contributors and widths must correspond')
        if any(width < 0 for width in widths):
            raise ValueError('Negative gather width')
        participants = frozenset([*devices, out_device])
        if self.device not in participants:
            return
        group = self.groups[participants]
        template = out_tensor if out_tensor is not None else tensor
        if template is None:
            raise ValueError('Participating gather rank has no shape or dtype')
        offset = 0
        for source, width in zip(devices, widths):
            if not width:
                continue
            if self.device == source:
                payload = tensor.contiguous()
                if payload.shape[-1] != width:
                    raise ValueError('Local gather width differs from its declaration')
            else:
                payload = torch.empty((*template.shape[:-1], width), device=template.device,
                                      dtype=template.dtype)
            dist.broadcast(payload, src=self.active_devices.index(source), group=group)
            if self.device == out_device:
                out_tensor[..., offset:offset + width].copy_(payload)
            offset += width
            self.stats['gather_bytes'] += payload.numel() * payload.element_size()
        if self.device == out_device and offset != out_tensor.shape[-1]:
            raise ValueError('Gather output width differs from the contributors')

    gather_small = gather

    def run_cpu_reduce_jobs(self):
        pass

    def end_cpu_reduce_jobs(self):
        pass
