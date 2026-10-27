"""Describe a virtual-head padding candidate; this does not modify checkpoints."""
import math
import struct


HEADS = 64
GROUPS = 8
PADDED_HEADS = 72
PADDED_GROUPS = 9
HEAD_DIM = 512
Q_RANK = 1280
O_RANK = 1024
HIDDEN = 5120
BLOCK = 32


def padding_spec(key, metadata):
    """Return new shape/fill bytes for backbone or MTP attention tensors."""
    if '.attn.' not in key:
        return None
    prefix, suffix = key.rsplit('.attn.', 1)
    if not prefix.startswith(('layers.', 'mtp.')):
        return None
    shape = list(metadata['shape'])
    dtype = metadata['dtype']
    if suffix == 'attn_sink':
        assert shape == [HEADS] and dtype == 'F32', (key, metadata)
        return {'shape': [PADDED_HEADS], 'fill': struct.pack('<f', -math.inf),
                'why': 'The additional heads have no attention sink contribution.'}
    shapes = {
        'wq_b': ([HEADS * HEAD_DIM, Q_RANK], [PADDED_HEADS * HEAD_DIM, Q_RANK]),
        'wo_a': ([GROUPS * O_RANK, HEADS * HEAD_DIM // GROUPS],
                 [PADDED_GROUPS * O_RANK, HEADS * HEAD_DIM // GROUPS]),
        'wo_b': ([HIDDEN, GROUPS * O_RANK], [HIDDEN, PADDED_GROUPS * O_RANK]),
    }
    name, _, field = suffix.partition('.')
    if name not in shapes or field not in ('weight', 'scale'):
        return None
    before, after = shapes[name]
    if field == 'scale':
        before = [n // BLOCK for n in before]
        after = [n // BLOCK for n in after]
        assert dtype == 'F8_E8M0', (key, metadata)
        fill = bytes([127])  # UE8M0 exponent zero represents a unit block scale.
    else:
        assert dtype == 'F8_E4M3', (key, metadata)
        fill = bytes([0])
    assert shape == before, (key, metadata, before)
    return {'shape': after, 'fill': fill,
            'why': 'Keep original heads/groups in order; the extra output group has zero weights.'}


def validate_source_config(config):
    assert config['architectures'] == ['DeepseekV41ForCausalLM']
    text = config['text_config']
    expected = {'num_attention_heads': HEADS, 'o_groups': GROUPS,
                'head_dim': HEAD_DIM, 'q_lora_rank': Q_RANK,
                'o_lora_rank': O_RANK, 'hidden_size': HIDDEN}
    for key, value in expected.items():
        assert text[key] == value, (key, text[key], value)
    assert HEADS // GROUPS == PADDED_HEADS // PADDED_GROUPS
    assert PADDED_HEADS % 3 == PADDED_GROUPS % 3 == 0
    return expected
