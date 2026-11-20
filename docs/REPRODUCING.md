# Reproducing A Recipe

Use Linux, Python 3.12, the appropriate CUDA toolkit and a working SM80 device
group with the stated VRAM. The runtime preparation steps build isolated
environments; they do not change drivers or start a model.

Model files are downloaded separately using the full checkpoint revision.
The download helper needs `huggingface_hub`; it uses your normal Hugging Face
authentication when a repository requires access. It writes an artifact
manifest next to the downloaded model for the DeepSeek V4.1 Flash preparation tools.

```bash
python3 -m pip install huggingface_hub
python3 scripts/download_model.py PROFILE_ID --directory /path/to/model
```

## Launch Options

Select your GPU ordinals or UUIDs with `--devices`, in layer/pipeline order.
Device ordinals in the examples are placeholders for the required card count.
The launcher has no fixed physical-slot assignment.

The foreground launcher defaults to `127.0.0.1:8000`. Choose your listener
with `--host` and `--port`. The configuration templates use `@HOST@`, `@PORT@`
and model-path placeholders; the launcher fills them before serving.
Use `--dry-run` to inspect the rendered command and configuration without
loading a GPU runtime.

## TabbyAPI / ExLlamaV3

Six selected profiles share this runtime: Qwen3.8-27B Orca, Qwen3.8-27B, Qwen3.8-Flash-Next, MiMo-V2.6-Flash,
GLM-5.3-Flash and Apex Flash 1 EXL3. Prepare it once:

```bash
python3 scripts/prepare_runtime.py tabby --root .local/runtimes --dry-run
python3 scripts/prepare_runtime.py tabby --root .local/runtimes
```

This checks out the full recorded TabbyAPI and ExLlamaV3 commits, applies the
captured source patches, and builds SM80 against Torch 2.14.0. CUDA 13.1 and
the corresponding PyTorch wheel index are the reference setup. If your wheel
mirror differs, pass `--torch-index`; changing the runtime versions makes the
published performance a reference rather than a matched measurement.

`runtimes/tabby/constraints.txt` records the installed package versions.
`source-pins.json` identifies the exact upstream bases and patch digests.
The startup adapter retains Qwen compatibility and the measured 4,096-token
output allocation budget where the profile explicitly sets it. Standard Qwen
27B retains the upstream output budget without an override. Native MTP uses
the target checkpoint's MTP head.
Additional experimental mHC fusion is not enabled.

The selected Tabby templates set `sysmem_kv_cache: 0`: bulk prefix-page
spilling is disabled. Their separate recurrent checkpoints preserve hybrid
state for prefix reuse and do not add GPU KV token capacity.

The ExLlama patch also includes [mixed prefill/decode scheduling](MIXED-SERVING.md).
Solo prompt ingestion keeps the configured chunk size. With another response
decoding, one prompt at a time receives page-sized prefill chunks and ongoing
responses receive intervening batched decode steps. Historical benchmark points
use retained qualification runs; separate live checks describe mixed traffic.
The startup adapter also installs [Responses compatibility](API-COMPATIBILITY.md)
alongside the native completion/chat endpoints, including reasoning and tool
streaming, final token usage and normal client-disconnect cleanup.

Open the selected recipe's README for its pinned download and foreground
launch. `--runtime-root .local/runtimes` selects this prepared environment.
The helper renders a local config and a symlink carrying the fixed served
model id, so local directory names do not change the API identity.

## Other Runtime Sources

See the [standard EXL3 runtimes](../runtimes/standard-exl3/README.md) for
HY4 Flash, Sage S2.1 Flash and SenseNova Loop 9B. The
[archived setup instructions](../archive/recipes/REPRODUCING.md) retain the
Apex Flash 1 AWQ and DeepSeek V4.1 Flash TP3 launch procedures.

## Verify The Export

```bash
python3 -m pip install -r requirements-dev.txt
python3 scripts/validate.py
python3 -m unittest discover -s tests -v
```

These checks validate recipe data, launch rendering, source overlays and
documentation on CPU. They do not start GPU servers or manufacture new
performance/quality measurements.
