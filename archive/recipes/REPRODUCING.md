# Reproducing Retired Recipes

These setup instructions reproduce the archived launch templates. Run the commands from the repository root. Use the [shared launch options](../../docs/REPRODUCING.md#launch-options) to choose devices and a listener.

## Apex Flash 1 AWQ / Balanced PP3

This recipe needs the newer pinned vLLM build and the captured SM80 NoPE8,
INT8 draft-cache, parser and allocation changes. Vanilla AWQ flags alone do
not reproduce the measured recipe. See
[the runtime build instructions](../../runtimes/apex-awq/README.md).

Download both the selected AWQ target and its pinned BF16 DFlash2 checkpoint:

```bash
python3 scripts/download_model.py apex-abliterated-awq-dflash2-pp3-balanced \
  --directory /path/to/apex-awq
python3 scripts/download_model.py apex-abliterated-awq-dflash2-pp3-balanced \
  --draft --directory /path/to/original-dflash2
```

Prepare the target-matched embedding with the AWQ runtime's Python, which has
Torch and safetensors installed. This is a CPU operation:

```bash
.local/runtimes/apex-awq/.venv/bin/python scripts/prepare_awq_draft.py \
  --draft /path/to/original-dflash2 \
  --target /path/to/apex-awq \
  --destination /path/to/prepared-dflash2
```

The source drafter weights stay unchanged. A separate BF16
`target_embed_tokens.safetensors` holds the selected target's byte-exact
embedding. Use that prepared directory as `--draft-path`. The serving
partition is 17/15/13. The 17/14/14 comparison uses a smaller KV pool.

## DeepSeek V4.1 Flash / TP3

This recipe depends on a pinned backport image, a vllm-exl3 plugin, SM80/TP3
loader changes and NVMe Engram tables. It is not a stock vLLM 0.13 recipe;
that number is the image's distribution label. See
[the runtime and asset preparation instructions](../../runtimes/deepseek/README.md).

Download the pinned source, then run the captured CPU preparation tools:

```bash
python3 scripts/download_model.py deepseek-v41-flash-dspark5-tp3 \
  --directory /path/to/deepseek-source
python3 runtimes/deepseek/preparation/transform_v41_tp3.py \
  --source /path/to/deepseek-source \
  --source-manifest /path/to/deepseek-source-download.json \
  --destination /path/to/deepseek-tp3
python3 runtimes/deepseek/preparation/stage_v41_engram.py \
  --source-receipt /path/to/deepseek-source-download.json \
  --destination /path/on/nvme/engram-tables
```

The TP3 tool pads attention/output-group geometry without requantizing the
real tensors. Unchanged shards are symlinked to the source; keep that source
available. The staging tool copies and hashes the two Engram table shards
onto your selected NVMe path. It does not assume that your NVMe is the root
filesystem.

The included Docker Compose recipe uses the same absolute source mount to
preserve those symlinks. It does not download or stage weights at startup.
The DeepSeek V4.1 Flash `launch.sh` invokes this container recipe. Supply the transformed
view as `--model-path`, the original checkpoint as `--source-model-path`, and
the staged tables as `--engram-path`. Docker Engine with the Compose and
Buildx plugins, plus the NVIDIA Container Toolkit, is required; no host vLLM
virtual environment is used.
