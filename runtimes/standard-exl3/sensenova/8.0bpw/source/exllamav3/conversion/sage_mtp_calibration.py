"""Calibrate native MTP from frozen post-norm main states and next input tokens."""

import gc
import json
import os
import time
from pathlib import Path

import torch


def aligned_calibration(targets, input_ids):
    if len(targets) != len(input_ids) or any(
            hidden.ndim != 3 or hidden.shape[:-1] != ids.shape or ids.shape[1] < 2
            for hidden, ids in zip(targets, input_ids)):
        raise ValueError('Main hidden states and token rows are not aligned')
    return ([hidden[:, :-1].contiguous() for hidden in targets],
            [ids[:, 1:].contiguous() for ids in input_ids])


def save_main_states(args, states, input_ids):
    from . import convert_model as cv
    if len(states) != len(input_ids) or any(
            hidden.ndim != 3 or hidden.shape[:-1] != ids.shape
            for hidden, ids in zip(states, input_ids)):
        raise ValueError('Main post-norm states do not align with calibration token IDs')
    directory = Path(args['work_dir']) / 'mtp_calibration'
    directory.mkdir(parents=True, exist_ok=True)
    cv.save_tensor(states, 'mtp_calibration/target_hidden.safetensors', args)
    cv.save_tensor(input_ids, 'mtp_calibration/input_ids.safetensors', args)


def reload_quantized_module(args, module, config, device):
    from . import convert_model as cv
    tensors = {}
    for child in module:
        tensors.update(child.get_tensors())
    module.unload()
    config.stc.close()
    cv.clear_temp_files(args)
    cv.save_tensor(tensors, f'qtensors/{module.key}.safetensors', args)
    # Parallel quantization leaves per-device objects and fused bindings behind.
    config.stc.set_new_tensors(tensors)
    try:
        module.load(device, source=tensors, keep_source_weights=True)
    finally:
        config.stc.set_new_tensors(None)


@torch.inference_mode()
def quantize_mtp(args, model, mtp, config, strategy, devices, ratios, device):
    from . import convert_model as cv
    from ..modules.linear import Linear
    from ..util.memory import free_mem
    calibration = Path(args['work_dir']) / 'mtp_calibration'
    if not (calibration / 'target_hidden.safetensors').is_file():
        raise ValueError('Calibrated MTP requires the main post-norm calibration snapshot')
    targets = cv.load_tensor('mtp_calibration/target_hidden.safetensors', args)
    original_ids = cv.load_tensor('mtp_calibration/input_ids.safetensors', args)
    if len(targets) != len(original_ids) or len(targets) != args['cal_rows']:
        raise ValueError('MTP target-state and token row counts differ')
    targets, tokens = aligned_calibration(targets, original_ids)
    if any(hidden.shape[:-1] != ids.shape for hidden, ids in zip(targets, tokens)):
        raise ValueError('Shifted MTP token/hidden shapes differ')
    mtp.attach_to(model)
    embedding = model.modules[0]
    embedding.load(device, keep_source_weights=True)
    states = tokens
    completed = []

    def progress(stage, index, module, **details):
        path = calibration / 'progress.json'
        temporary = path.with_suffix('.json.tmp')
        temporary.write_text(json.dumps({'at': time.time(), 'stage': stage,
            'module_index': index, 'module': module.key, **details}, indent=2) + '\n')
        temporary.replace(path)

    try:
        for index, module in enumerate(mtp.modules):
            cv.get_temp_buffers.cache_clear()
            free_mem()
            started = time.time()
            progress('loading', index, module)
            module.load(device, keep_source_weights=True)
            capture = {}
            linears = [m for m in module if isinstance(m, Linear) and m.qmap and m.device is not None]
            if linears:
                for row, (value, ids, target) in enumerate(zip(states, tokens, targets)):
                    progress('capturing', index, module, row=row, total_rows=len(states))
                    params = {'attn_mode': 'flash_attn_nc', 'input_ids': ids,
                              'target_hidden': target, 'capture': capture,
                              'activate_all_experts': mtp.calibration_all_experts}
                    mtp.prepare_inputs(ids, params)
                    value = module.prepare_for_device(value, params)
                    output = module.forward(value, params)
                    if not torch.isfinite(output).all():
                        raise ValueError(f'Non-finite MTP calibration module {index}, row {row}')
                missing = {linear.qmap for linear in linears} - capture.keys()
                if missing:
                    raise ValueError('MTP Hessian capture is incomplete: ' + str(sorted(missing)))
                cv.save_tensor(states, f'mtp_calibration/module-{index}-inputs.safetensors', args)
                # Preserve the calibrated H payloads and counts for audit and draft-only replay.
                h_tensors, h_metadata = {}, {}
                for key, value in capture.items():
                    h_metadata[key] = {}
                    for name, child in value.items():
                        if isinstance(child, torch.Tensor):
                            h_tensors[key + ':' + name] = child.cpu()
                        elif isinstance(child, (int, float, str, bool)):
                            h_metadata[key][name] = child
                cv.save_tensor(h_tensors, f'mtp_calibration/module-{index}-hessians.safetensors', args)
                (calibration / f'module-{index}-hessians.json').write_text(json.dumps(h_metadata, indent=2) + '\n')
                del h_tensors, h_metadata
                for linear in linears:
                    linear.inner.swap_cpu()
                progress('quantizing', index, module, linears=len(linears))
                if len(linears) >= len(devices) and all(strategy[m.key] <= 8 for m in linears):
                    cv.quantize_linears_parallel(args, linears, config, strategy, index, devices,
                                                ratios('quant_thread'), capture, states)
                else:
                    cv.quantize_linears_single(args, linears, config, strategy, index, devices,
                                              ratios('quant_tiles'), capture, states)
            capture.clear()
            progress('reloading', index, module, device=str(device))
            reload_quantized_module(args, module, config, device)
            next_states = []
            for row, (value, ids, target) in enumerate(zip(states, tokens, targets)):
                progress('advancing', index, module, row=row, total_rows=len(states))
                params = {'attn_mode': 'flash_attn_nc', 'input_ids': ids, 'target_hidden': target}
                mtp.prepare_inputs(ids, params)
                value = module.prepare_for_device(value, params)
                output = module.forward(value, params)
                if not torch.isfinite(output).all():
                    raise ValueError(f'Non-finite quantized MTP state in module {index}')
                next_states.append(output.cpu())
            states = next_states
            completed.append({'key': module.key, 'rows': len(states), 'calibrated_linears': len(linears),
                              'seconds': time.time() - started, 'state_advance_device': str(device),
                              'reloaded_before_state_advance': True})
            progress('module_complete', index, module, completed_modules=len(completed))
            module.unload()
            config.stc.close()
            del capture
            gc.collect()
            free_mem()
        (calibration / 'receipt.json').write_text(json.dumps({
            'calibrated': True, 'token_alignment': 'next input token paired with preceding main post-norm state',
            'modules': completed, 'bits': args['mtp_bits']}, indent=2) + '\n')
    finally:
        embedding.unload()
