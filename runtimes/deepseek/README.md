# DeepSeek Runtime And Assets

The recorded package base is:

```text
docker.io/lazymio/vllm-backport@sha256:349690323ab9aba712111529ed1ca60730199205d8202f67895ffde85b451be3
```

Its vLLM distribution metadata says 0.13.0, while its backported model/runtime
tree contains the newer DeepSeek/DSpark launch interfaces. The overlay includes
46 changed package/plugin source and registration files, plus four upstream
license and attribution documents. Torch is
2.13.0+cu130 and vllm-exl3 is 0.4.2.

The Dockerfile applies this source overlay to the pinned package base and
builds the captured ExLlamaV3 source lineage for SM80. The container recipe is
a portable export of a measured host configuration, not a claim of a new
clean-container GPU test.

Prepare the source weights, TP3 view and NVMe Engram files first, following
[REPRODUCING.md](../../docs/REPRODUCING.md). The transformed view contains
symlinks, so the source directory must remain mounted at its absolute path.

```bash
export MODEL_DIR=/absolute/path/to/deepseek-tp3
export SOURCE_MODEL_DIR=/absolute/path/to/deepseek-source
export ENGRAM_DIR=/absolute/path/on/nvme/engram-tables
export DEVICES=0,1,2
docker compose -f recipes/deepseek-v41-flash-dspark5-tp3/compose.yaml up --build
```

Stop with `docker compose ... down`. The container uses no restart policy;
the published listener defaults to `127.0.0.1:8000`. Override `BIND_ADDRESS`
and `PORT` for your deployment. The listener inside the container uses port
8000 so Docker can forward the selected host port.
