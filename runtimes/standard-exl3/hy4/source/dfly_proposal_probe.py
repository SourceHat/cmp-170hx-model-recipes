'Check all five released DFly2 draft blocks against an expanded MLA reference.'

from torch.nn import functional as F

from dfly_math import rms_norm

TARGETS = (25, 29, 33, 37, 41)

DRAFT_ROOT = "model.dfly_layers."

def projected_kv(x, projection, weight, dim, eps):
    latent, phase = F.linear(x, projection).split([weight.numel(), dim], dim=-1)
    return rms_norm(latent, weight, eps), phase
