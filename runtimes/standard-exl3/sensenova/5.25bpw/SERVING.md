# SenseNova-Loop-9B-EXL3-5.25bpw: serving runtime

Use the [updated ExLlamaV3 source](source/) with the [reference settings](REFERENCE-PROFILE.json). Build the native extension for your CUDA and PyTorch environment using the source README. Point the runtime at the local model snapshot downloaded from Hugging Face.

This update keeps precise FP32 routing and adds the selected residual and router replay paths. Where measured, it reuses page rows and waits for sampled tokens without spinning a CPU.

| Requests | Path selected | CPU ms/token before | After | Decode tok/s before | After |
| ---: | --- | ---: | ---: | ---: | ---: |
| 1 | combined | 59.84 | 41.81 | 35.40 | 34.83 |
| 4 | combined | 42.48 | 38.02 | 98.63 | 99.92 |

CPU time is measured for the engine process across a short request wave, including prefill and excluding load. Decode rates exclude prefill. The selected paths matched all checked greedy tokens. The runtime uses the model's native context.
