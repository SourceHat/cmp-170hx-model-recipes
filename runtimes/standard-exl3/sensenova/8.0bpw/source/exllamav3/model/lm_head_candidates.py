"""Exact vocabulary candidates shared by sharded and reference LM heads."""
import torch


def candidate_priority(ids,vocab_size,scalar_bytes=None):
    if scalar_bytes is None:return ids
    if scalar_bytes not in (2,4) or not 1<=vocab_size<=524288:
        raise ValueError('Unsupported CUDA reference candidate geometry')
    elements=16 if vocab_size<=262144 else 32
    vector=16//scalar_bytes
    block=256*elements
    local=ids.remainder(block)
    thread=local.remainder(256*vector)//vector
    element=(local//(256*vector))*vector+local.remainder(vector)
    # The existing kernel breaks ties by block, warp, lane, then register slot.
    return (ids//block)*block+thread*elements+element


def ordered_topk(scores,ids,k,vocab_size,scalar_bytes=None):
    priority=candidate_priority(ids,vocab_size,scalar_bytes)
    bits=scores.contiguous().view(torch.int32).long()
    bits=torch.where(scores==0,0,bits)
    sortable=torch.where(bits<0,(~bits)&0xffffffff,bits^0x80000000)
    # Unique integer keys retain every FP32 score bit and the reference tie order.
    keys=((sortable-0x80000000)<<32)|(0xffffffff-priority)
    order=torch.topk(keys,k,dim=-1,sorted=True).indices
    return scores.gather(-1,order),ids.expand_as(scores).gather(-1,order)


def vocab_topk(logits, k, *, offset=0, vocab_size=None, scale=1.0, softcap=0.0,
               scalar_bytes=None):
    if type(k) is not int or k < 1 or offset < 0:
        raise ValueError('Invalid vocabulary candidate request')
    vocab_size = vocab_size if vocab_size is not None else offset + logits.shape[-1]
    width = max(0, min(logits.shape[-1], vocab_size - offset))
    values = logits[..., :width].float() * scale
    if softcap > 0:
        if logits.is_cuda and width:
            from ..ext import exllamav3_ext
            # Use the reference kernel's fast-math tanhf before selecting ties.
            values=values.contiguous()
            exllamav3_ext.softcap(values,values,softcap)
        else:
            values = torch.tanh(values / softcap) * softcap
    count = min(k, width)
    if scalar_bytes is None and logits.is_cuda:scalar_bytes=logits.element_size()
    ids=torch.arange(offset,offset+width,dtype=torch.long,device=logits.device)
    scores,ids=ordered_topk(values,ids,count,vocab_size,scalar_bytes)
    if count < k:
        shape = (*logits.shape[:-1], k - count)
        scores = torch.cat((scores, torch.full(shape, -float('inf'), dtype=torch.float32,
                                             device=logits.device)), dim=-1)
        ids = torch.cat((ids, torch.full(shape, vocab_size, dtype=torch.long,
                                       device=logits.device)), dim=-1)
    return scores, ids


def merge_vocab_topk(scores, ids, k, vocab_size,scalar_bytes=None):
    if scores.shape != ids.shape or type(k) is not int or not 1 <= k <= vocab_size:
        raise ValueError('Invalid sharded vocabulary candidates')
    scores = scores.masked_fill((ids < 0) | (ids >= vocab_size), -float('inf'))
    if scalar_bytes is None and scores.is_cuda:scalar_bytes=4
    return ordered_topk(scores,ids,k,vocab_size,scalar_bytes)
