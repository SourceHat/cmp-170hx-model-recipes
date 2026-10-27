# Hardware Requirements And Test Setup

The reference measurements use NVIDIA CMP 170HX / GA100 / SM80 cards with
**64 GiB usable VRAM each**, at a 200 W power limit. The card count in each
recipe describes that model's device group. The recorded KV allocations
require cmpunlocker to expose the cards' full memory.

## Benchmark Setup

| Measurement device | PCIe path | Measured link |
| --- | --- | --- |
| Reference GPU0 | CPU | Gen2 x8 |
| Reference GPU1 | CPU | Gen2 x4 |
| Reference GPU2 | PCH | Gen2 x4 |
| Reference GPU3 | PCH | Gen2 x4 |

The benchmark system had 96 GiB host RAM. Reference ordinals in the numerical
evidence identify measurement devices; they are not deployment assignments.
PCH paths share upstream bandwidth, so link width, transport and host topology
affect how well these rates transfer to another system.

All cards except GPU0 therefore have x4 links. This narrow Gen2 interconnect,
combined with host-mediated transfers, likely constrains multi-card prefill
and decode. No matched x8/x16 test quantifies the penalty. The older retained
three-card comparisons use reference GPU0/1/2. The selected-serving AWQ and
DeepSeek V4.1 Flash comparisons retain x8/x4/x4 links in rank order, with a different third
physical card. Their evidence does not establish a replacement reference ordinal.

The recipes retain the measured host-copy transport:
`EXLLAMA_NO_P2P_COPY=1` for Tabby and
`NCCL_P2P_DISABLE=1`. Experimental direct-copy measurements are not substituted
for the headline host-copy measurements.

## Selecting Devices

`--devices` takes GPU ordinals or UUIDs in layer/pipeline order. It does not
assign physical slots or start other models. Replace the example ordinals
with the devices on your system. Use the recipe's required card count and
check the selected cards' usable memory and interconnect.

The recipes assume working CUDA devices with the stated memory capacity.
Recurrent checkpoints and Qwen3.8-Flash-Next's n-gram weights also require host RAM;
their budgets are listed separately from GPU KV capacity.
`autosplit_reserve` in the Tabby template is the recorded allocator workspace
setting that produced the listed cache allocation.
