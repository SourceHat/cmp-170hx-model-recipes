"""Restricted single-token Marlin execution for batch-invariant V4.1 draft experts."""
import torch

from vllm import envs
from vllm.model_executor.layers.fused_moe import modular_kernel as mk
from vllm.model_executor.layers.fused_moe.config import RoutingMethodType
from vllm.model_executor.layers.fused_moe.experts.marlin_moe import MarlinExperts
from vllm.model_executor.layers.fused_moe.fused_moe_method_base import FusedMoEMethodBase
from vllm.model_executor.layers.fused_moe.oracle.mxfp4 import Mxfp4MoeBackend
from vllm.model_executor.layers.quantization.mxfp4 import Mxfp4Config, Mxfp4MoEMethod
from vllm.model_executor.layers.quantization.utils.quant_utils import kMxfp4Static


class SingleTokenMarlinExperts(MarlinExperts):
    @staticmethod
    def _supports_batch_invariance():
        return True

    @staticmethod
    def supports_lora():
        return False

    @staticmethod
    def _supports_quant_scheme(weight_key, activation_key):
        return weight_key == kMxfp4Static and activation_key is None

    @staticmethod
    def _supports_parallel_config(config):
        return (config.tp_size == 3 and config.dp_size == config.ep_size == config.pcp_size == config.sp_size == 1
                and not config.use_ep and not config.enable_eplb and not config.use_batched_activation_format
                and MarlinExperts._supports_parallel_config(config))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._single_token_scratch = None

    def apply(self, output, hidden_states, w1, w2, topk_weights, topk_ids,
              activation, global_num_experts, expert_map, a1q_scale, a2_scale,
              workspace13, workspace2, expert_tokens_meta, apply_router_weight_on_input):
        if (hidden_states.ndim != 2 or output.shape != hidden_states.shape
                or topk_ids.ndim != 2 or topk_ids.shape != topk_weights.shape
                or topk_ids.shape[0] != hidden_states.shape[0]
                or a1q_scale is not None or a2_scale is not None or expert_tokens_meta is not None
                or self._lora_context is not None or not self.quant_config.use_mxfp4_w4a16):
            raise ValueError('Single-token Marlin requires unquantized standard-format draft rows without LoRA')
        if hidden_states.shape[0] == 0:
            return
        _, _, n, k, topk = self.moe_problem_size(hidden_states[:1], w1, w2, topk_ids[:1])
        shape13, shape2, _ = super().workspace_shapes(
            1, n, k, topk, global_num_experts, w1.shape[0], None, activation)
        key = (hidden_states.device, workspace13.dtype, workspace2.dtype, shape13, shape2)
        if self._single_token_scratch is None or self._single_token_scratch[0] != key:
            # Modular output may alias its shared workspace. Private row scratch preserves prior outputs.
            self._single_token_scratch = (key,
                torch.empty(shape13, device=hidden_states.device, dtype=workspace13.dtype),
                torch.empty(shape2, device=hidden_states.device, dtype=workspace2.dtype))
        _, scratch13, scratch2 = self._single_token_scratch
        for row in range(hidden_states.shape[0]):
            super().apply(output[row:row + 1], hidden_states[row:row + 1], w1, w2,
                topk_weights[row:row + 1], topk_ids[row:row + 1], activation,
                global_num_experts, expert_map, None, None, scratch13, scratch2, None,
                apply_router_weight_on_input)


class SingleTokenMxfp4MoEMethod(Mxfp4MoEMethod):
    @property
    def supports_eplb(self):
        return False

    def __init__(self, moe):
        if (not envs.VLLM_BATCH_INVARIANT or moe.routing_method != RoutingMethodType.DeepseekV4
                or moe.in_dtype != torch.bfloat16 or moe.max_capture_size):
            raise ValueError('Single-token MXFP4 is restricted to batch-invariant DeepSeek V4 draft experts')
        supported, reason = SingleTokenMarlinExperts.is_supported_config(
            SingleTokenMarlinExperts, moe, kMxfp4Static, None, mk.FusedMoEActivationFormat.Standard)
        if not supported:
            raise ValueError('Single-token MXFP4 does not support this draft configuration: ' + str(reason))
        # Keep the existing MXFP4 weight loading, scale encoding and Marlin conversion unchanged.
        FusedMoEMethodBase.__init__(self, moe)
        self.weight_dtype = 'mxfp4'
        self.mxfp4_backend = Mxfp4MoeBackend.MARLIN
        self.experts_cls = SingleTokenMarlinExperts
        self.max_capture_size = moe.max_capture_size
        self._cache_permute_indices = {}
        self.moe_kernel = None
        self.w13_precision_config = None
        self.w2_precision_config = None


class SingleTokenMxfp4Config(Mxfp4Config):
    def _make_moe_method(self, moe):
        return SingleTokenMxfp4MoEMethod(moe)
