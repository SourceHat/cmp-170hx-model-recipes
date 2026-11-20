# SourceHat EXL3 runtimes

Serving source and measured reference settings for six standard EXL3 quants.
Each entry pins the exact public model revision used to stage its runtime.

| Quant | Current serving guide | Model weights |
| --- | --- | --- |
| HY4 Flash 4.875 | [Guide](hy4/4.875bpw/SERVING.md) and [profile](hy4/4.875bpw/REFERENCE-PROFILE.json) | [Hugging Face](https://huggingface.co/SourceHat-Labs/HY4-Flash-EXL3-4.875bpw/tree/d7ce7d4365c4911e6b654207451eef0c84348e6b) |
| HY4 Flash 8.0 | [Guide](hy4/8.0bpw/SERVING.md) and [profile](hy4/8.0bpw/REFERENCE-PROFILE.json) | [Hugging Face](https://huggingface.co/SourceHat-Labs/HY4-Flash-EXL3-8.0bpw/tree/662f38e2cab492ded41833fa9d9c005720119f90) |
| Sage S2.1 Flash 4.25 | [Guide](sage/4.25bpw/SERVING.md) and [profile](sage/4.25bpw/REFERENCE-PROFILE.json) | [Hugging Face](https://huggingface.co/SourceHat-Labs/Sage-S2.1-Flash-EXL3-4.25bpw/tree/87f82b89e304dc995da1ae4ff5e8ad1ee3bd764e) |
| SenseNova Loop 9B 3.0 | [Guide](sensenova/3.0bpw/SERVING.md) and [profile](sensenova/3.0bpw/REFERENCE-PROFILE.json) | [Hugging Face](https://huggingface.co/SourceHat-Labs/SenseNova-Loop-9B-EXL3-3.0bpw/tree/ab54f1cdd26a66696007fc2d94d437916f908ef5) |
| SenseNova Loop 9B 5.25 | [Guide](sensenova/5.25bpw/SERVING.md) and [profile](sensenova/5.25bpw/REFERENCE-PROFILE.json) | [Hugging Face](https://huggingface.co/SourceHat-Labs/SenseNova-Loop-9B-EXL3-5.25bpw/tree/b6470e539a589b4b97e16b46f9cd0128bb0cf327) |
| SenseNova Loop 9B 8.0 | [Guide](sensenova/8.0bpw/SERVING.md) and [profile](sensenova/8.0bpw/REFERENCE-PROFILE.json) | [Hugging Face](https://huggingface.co/SourceHat-Labs/SenseNova-Loop-9B-EXL3-8.0bpw/tree/fd7791abcda85e6e1a9bf77e992f96f9aba0de5a) |

## Build and serve

Run the commands below from `runtimes/standard-exl3` in this checkout.
Use a CUDA-enabled PyTorch environment and a CUDA toolkit and compiler that support your GPU.
Install the source tree for the quant you intend to serve in its own environment: these bundles all install the
`exllamav3` package. For Sage and SenseNova, use the quant's `source/` directory
and apply its JSON settings in your EXL3 server. The JSON is a reference, not a universal server config.
Set Sage's profile environment values before importing the library. Disable external drafting for the
target-only configurations. The [profile guide](PROFILES.md) maps the reference fields to server choices.

HY4 shares one launcher and native source tree across the two quants.
For the example below, export `CUDA_VISIBLE_DEVICES` with the two
peer-connected devices in rank order and set `PORT` to a free loopback port.

```sh
python -m pip install 'setuptools>=77' wheel ninja transformers triton
python -m pip install --no-build-isolation ./hy4/source/exllama
python hy4/source/serve.py --check-layout \
  --model-dir /path/to/HY4-Flash-EXL3-4.875bpw \
  --profile hy4/4.875bpw/REFERENCE-PROFILE.json
python hy4/source/serve.py \
  --model-dir /path/to/HY4-Flash-EXL3-4.875bpw \
  --profile hy4/4.875bpw/REFERENCE-PROFILE.json --port "$PORT"
```

Select two peer-connected 64 GiB devices for 4.875, or three for 8.0. Keep the Engram directory on NVMe.
Use the 8.0 profile and the corresponding weight directory when serving that variant.

## Release scope

This tree carries serving source, profiles, and public model links. It omits model weights, compiled binaries,
private evaluation inputs and responses, and upstream conversion calibration text and evaluation harnesses.
The per-quant serving guides give benchmark scope. See [license notices](LICENSES.md) and [provenance](RUNTIMES.json).

The bundled source uses the published inference paths without changing
decode, prefill or cache settings. The Mistral wrapper descriptions in the
bundled comments are phrased in prose; model dispatch is unchanged. The optional TP fault receipt writer
requires an explicit `EXLLAMA_TP_FAILURE_LOG_DIR` and a managed job ID
when used by a supervisor. Ordinary serving does not write these receipts.
