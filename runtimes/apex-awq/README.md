# Apex AWQ Runtime

The measured build is vLLM `0.30.1rc1.dev640+g155488d85`, commit
`155488d853a0bc42df227dbfc74005b3fd488e94`, Torch 2.13.0, Python 3.12,
with the 23 captured package-source replacements in `overlay-manifest.json`.
`helpers/meshify_sm80_nope8.py` registers the additional SM80 backend in
the API process and supplies the class imported by workers.

Build in an isolated directory using the matching CUDA toolkit and upstream
vLLM build prerequisites:

```bash
mkdir -p .local/runtimes/apex-awq
python3.12 -m venv .local/runtimes/apex-awq/.venv
.local/runtimes/apex-awq/.venv/bin/python -m pip install --upgrade pip setuptools wheel packaging ninja
.local/runtimes/apex-awq/.venv/bin/python -m pip install torch==2.13.0
git clone --no-checkout https://github.com/vllm-project/vllm.git .local/runtimes/apex-awq/vllm-source
git -C .local/runtimes/apex-awq/vllm-source checkout --detach 155488d853a0bc42df227dbfc74005b3fd488e94
python3 scripts/apply_overlay.py apex-awq --target .local/runtimes/apex-awq/vllm-source
TORCH_CUDA_ARCH_LIST=8.0 MAX_JOBS=4 \
  .local/runtimes/apex-awq/.venv/bin/python -m pip install --no-build-isolation \
  -c runtimes/apex-awq/constraints.txt .local/runtimes/apex-awq/vllm-source
```

The constraints file is the recorded environment, not a claim that every
development version has a stable PyPI wheel. A source build and CUDA toolchain
compatible with Torch are required. This build procedure is CPU-reviewed;
its fresh-machine GPU qualification remains unperformed.

Then follow [draft preparation and launch](../../docs/REPRODUCING.md).
The launcher sets `VLLM_USE_V2_MODEL_RUNNER=1`, the balanced 17/15/13 partition,
host transport and explicit main FP8 E4M3 / draft INT8 cache settings.
