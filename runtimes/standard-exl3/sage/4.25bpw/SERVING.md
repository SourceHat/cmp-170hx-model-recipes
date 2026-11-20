# Sage-S2.1-Flash-EXL3-4.25bpw: serving runtime

Use the [updated ExLlamaV3 source](source/) with the [reference settings](REFERENCE-PROFILE.json). Build the native extension for your CUDA and PyTorch environment using the source README. Point the runtime at the local model snapshot downloaded from Hugging Face.

This update adds the measured batched Sage indexer and enables blocking sample readback at the measured batch sizes. Set the environment values from the reference settings before import.

| Requests | Path selected | CPU ms/token before | After | Decode tok/s before | After |
| ---: | --- | ---: | ---: | ---: | ---: |
| 1 | blocking_wait | 142.35 | 99.29 | 19.10 | 19.08 |
| 4 | blocking_wait | 109.29 | 93.57 | 51.74 | 51.01 |

CPU time is measured for the engine process across a short request wave, including prefill and excluding load. Decode rates exclude prefill. The selected paths matched all checked greedy tokens. The runtime uses the model's native context.
