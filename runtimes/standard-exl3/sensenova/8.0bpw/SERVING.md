# SenseNova-Loop-9B-EXL3-8.0bpw: serving runtime

Use the [updated ExLlamaV3 source](source/) with the [reference settings](REFERENCE-PROFILE.json). Build the native extension for your CUDA and PyTorch environment using the source README. Point the runtime at the local model snapshot downloaded from Hugging Face.

This update keeps precise FP32 routing and adds the selected residual and router replay paths. Where measured, it reuses page rows and waits for sampled tokens without spinning a CPU.

| Requests | Path selected | CPU ms/token before | After | Decode tok/s before | After |
| ---: | --- | ---: | ---: | ---: | ---: |
| 1 | combined | 65.07 | 43.80 | 32.63 | 32.35 |
| 4 | combined | 43.35 | 38.15 | 117.76 | 116.39 |
| 8 | combined | 39.98 | 37.29 | 217.46 | 213.21 |

CPU time is measured for the engine process across a short request wave, including prefill and excluding load. Decode rates exclude prefill. The selected paths matched all checked greedy tokens. The runtime uses the model's native context.
