'Replay the existing grouped experts inside the exact four-lane runner.'

import torch

from hy4_decode_graph import GraphExperts

def capture_grouped(target, reference):
    graphs = {}
    streams = {device: torch.cuda.Stream(device=device) for device in target.devices}
    for packed, operation in reference.items():
        device = packed.device
        with torch.cuda.device(device):
            example = torch.zeros((4, 1, target.cfg.hidden_size), dtype=torch.bfloat16, device=device)
            graph = GraphExperts(operation, streams[device], (4,))
            graph.prepare(4, example)
            graphs[packed] = graph
    return graphs
