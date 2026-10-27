"""Experimental SM80 NoPE attention with explicit E4M3 serving KV storage."""
import torch
from vllm.triton_utils import tl,triton
from vllm.config import get_current_vllm_config
from vllm.platforms.interface import DeviceCapability
from vllm.v1.attention.backends.registry import AttentionBackendEnum,register_backend
from vllm.v1.attention.backends.mla.flashattn_mla_sparse import (
    FlashAttnMLASparseBackend,FlashAttnMLASparseImpl)
from vllm.model_executor.layers.attention.sparse_mla_attention import SparseMLACommonImpl
from vllm.v1.attention.backends.mla.sparse_utils import flat_kv_row_view


@triton.jit
def _decode_e4m3(codes):
    bits=codes.to(tl.uint32)
    exponent=(bits>>3)&15
    mantissa=bits&7
    magnitude=tl.where(exponent==0,mantissa.to(tl.float32)*0.001953125,
        (1.+mantissa.to(tl.float32)*.125)*tl.exp2(exponent.to(tl.float32)-7.))
    value=tl.where((bits&128)!=0,-magnitude,magnitude)
    return tl.where((bits&127)==127,float('nan'),value)


@triton.jit
def _nope8_kernel(Q,K,Indices,Counts,Scale,Out,
    q_token_stride:tl.constexpr,q_head_stride:tl.constexpr,
    kv_row_stride:tl.constexpr,index_row_stride:tl.constexpr,
    out_token_stride:tl.constexpr,out_head_stride:tl.constexpr,
    num_heads:tl.constexpr,num_rows:tl.constexpr,topk:tl.constexpr,
    sm_scale:tl.constexpr,BH:tl.constexpr=16,BN:tl.constexpr=32,D:tl.constexpr=512):
    token=tl.program_id(0)
    heads=tl.program_id(1)*BH+tl.arange(0,BH)
    dims=tl.arange(0,D)
    q=tl.load(Q+token*q_token_stride+heads[:,None]*q_head_stride+dims[None,:],
              mask=heads[:,None]<num_heads,other=0.)
    count=tl.load(Counts+token)
    scale=tl.load(Scale)
    maximum=tl.full((BH,),-1.e30,tl.float32)
    denominator=tl.zeros((BH,),tl.float32)
    accum=tl.zeros((BH,D),tl.float32)
    for start in range(0,topk,BN):
        offsets=start+tl.arange(0,BN)
        ids=tl.load(Indices+token*index_row_stride+offsets,mask=offsets<topk,other=-1)
        valid=(offsets<count)&(ids>=0)&(ids<num_rows)
        codes=tl.load(K+ids[None,:].to(tl.int64)*kv_row_stride+dims[:,None],
                      mask=valid[None,:],other=0)
        values=(_decode_e4m3(codes)*scale).to(q.dtype)
        scores=tl.dot(q,values)*sm_scale
        scores=tl.where(valid[None,:]&(heads[:,None]<num_heads),scores,-1.e30)
        next_max=tl.maximum(maximum,tl.max(scores,1))
        rescale=tl.exp(maximum-next_max)
        probabilities=tl.where(valid[None,:],tl.exp(scores-next_max[:,None]),0.)
        accum=accum*rescale[:,None]+tl.dot(probabilities.to(q.dtype),tl.trans(values))
        denominator=denominator*rescale+tl.sum(probabilities,1)
        maximum=next_max
    output=tl.where(denominator[:,None]>0,accum/tl.maximum(denominator[:,None],1.e-30),0.)
    tl.store(Out+token*out_token_stride+heads[:,None]*out_head_stride+dims[None,:],
             output,mask=heads[:,None]<num_heads)


def sparse_nope8(q,cache,indices,counts,scale,sm_scale):
    if (q.dtype!=torch.bfloat16 or q.shape[-1]!=512
            or cache.dtype not in (torch.float8_e4m3fn,torch.uint8) or cache.shape[-1]!=512):
        raise ValueError('NoPE8 requires BF16 query activations and E4M3/byte KV rows')
    if indices.ndim!=2 or indices.shape[0]!=q.shape[0] or counts.shape!=(q.shape[0],):
        raise ValueError('NoPE8 top-k/count geometry differs')
    raw=cache.view(torch.uint8).reshape(-1,512)
    output=torch.empty_like(q)
    _nope8_kernel[(q.shape[0],triton.cdiv(q.shape[1],16))](q,raw,indices,counts,scale,output,
        q.stride(0),q.stride(1),raw.stride(0),indices.stride(0),output.stride(0),output.stride(1),
        q.shape[1],raw.shape[0],indices.shape[1],sm_scale,num_warps=4)
    return output


class NoPE8Impl(FlashAttnMLASparseImpl):
    def __init__(self,num_heads,head_size,scale,num_kv_heads,alibi_slopes,sliding_window,
                 kv_cache_dtype,logits_soft_cap,attn_type,kv_sharing_target_layer_name,
                 topk_indices_buffer=None,indexer=None,**mla_args):
        if (head_size!=512 or kv_cache_dtype!='fp8_e4m3' or alibi_slopes is not None
                or sliding_window is not None or logits_soft_cap is not None):
            raise ValueError('The NoPE8 backend has no precision or geometry fallback')
        SparseMLACommonImpl.__init__(self,num_heads,head_size,scale,num_kv_heads,
            alibi_slopes,sliding_window,kv_cache_dtype,logits_soft_cap,attn_type,
            kv_sharing_target_layer_name,indexer=indexer,topk_indices_buffer=topk_indices_buffer,**mla_args)
        self.supports_quant_query_input=False

    def forward_mqa(self,q,kv_cache,metadata,layer):
        self._meshify_k_scale=layer._k_scale
        return super().forward_mqa(q,kv_cache,metadata,layer)

    def _run_mqa_kernel(self,q_nope,q_rope,kv_cache,topk_indices,valid_counts,block_size,*,cache_is_flat=False):
        if q_rope.shape[-1]!=0:
            raise ValueError('NoPE8 cannot consume RoPE-carrying cache records')
        rows=kv_cache if cache_is_flat else flat_kv_row_view(kv_cache,block_size)[0]
        return sparse_nope8(q_nope,rows,topk_indices,valid_counts,self._meshify_k_scale,self.scale)


@register_backend(AttentionBackendEnum.CUSTOM)
class NoPE8Backend(FlashAttnMLASparseBackend):
    supported_kv_cache_dtypes=['fp8_e4m3']

    @staticmethod
    def get_name():return 'MESHIFY_SM80_NOPE8'

    @staticmethod
    def get_impl_cls():return NoPE8Impl

    @classmethod
    def supports_compute_capability(cls,capability:DeviceCapability):return capability.major==8

    @classmethod
    def supports_combination(cls,head_size,dtype,kv_cache_dtype,block_size,use_mla,
            has_sink,use_sparse,use_mm_prefix,device_capability):
        cfg=get_current_vllm_config().model_config.hf_text_config
        if (device_capability.major!=8 or head_size!=512 or dtype!=torch.bfloat16
                or kv_cache_dtype!='fp8_e4m3' or not use_mla or not use_sparse
                or has_sink or use_mm_prefix or getattr(cfg,'qk_rope_head_dim',None)!=0):
            return 'NoPE8 supports only SM80 sparse NoPE-512 with explicit E4M3 KV'
        return None


def install_sparse_profile_workspace():
    from vllm.model_executor.layers.attention.mla_attention import MLAAttention

    original = MLAAttention.chunked_prefill_workspace_size.fget
    if getattr(original, '_meshify_nope8_workspace', False):
        return

    def workspace_size(attention):
        if attention.attn_backend.get_name() != NoPE8Backend.get_name():
            return original(attention)
        if attention._chunked_prefill_workspace_size is None:
            # Profile the sparse builder's real allocation, not the dense MLA bound.
            attention._chunked_prefill_workspace_size = (
                attention.attn_backend.get_builder_cls().determine_chunked_prefill_workspace_size(
                    attention._vllm_config
                )
            )
        return attention._chunked_prefill_workspace_size

    workspace_size._meshify_nope8_workspace = True
    MLAAttention.chunked_prefill_workspace_size = property(workspace_size)


install_sparse_profile_workspace()


def run_parity():
    generator=torch.Generator(device='cuda:0').manual_seed(20261008)
    q=torch.randn((4,11,512),device='cuda:0',dtype=torch.bfloat16,generator=generator)*.2
    source=torch.randn((97,512),device='cuda:0',dtype=torch.bfloat16,generator=generator)*.2
    scale=torch.tensor(.013,device='cuda:0',dtype=torch.float32)
    cache=(source.float()/scale).to(torch.float8_e4m3fn)
    ids=torch.arange(32,device='cuda:0',dtype=torch.int32).expand(4,-1).clone()
    ids[1,17:]=-1;ids[2,5]=96;ids[3]=-1
    counts=torch.tensor([32,11,32,0],device='cuda:0',dtype=torch.int32)
    actual=sparse_nope8(q,cache,ids,counts,scale,512**-.5)
    expected=torch.zeros_like(q)
    decoded=cache.float()*scale
    for i,n in enumerate([32,11,32,0]):
        if n:
            selected=ids[i,:n];selected=selected[(selected>=0)&(selected<97)]
            values=decoded[selected]
            expected[i]=(torch.softmax(q[i].float()@values.T*512**-.5,-1)@values).to(torch.bfloat16)
    if not torch.isfinite(actual).all() or not torch.allclose(actual,expected,atol=.003,rtol=.03):
        raise ValueError('NoPE8 parity against decoded eight-bit cache rows failed')
    return dict(passed=True,cases=4,kv_dtype='fp8_e4m3',kv_element_bytes=cache.element_size(),
                max_absolute_error=(actual-expected).abs().max().item())
