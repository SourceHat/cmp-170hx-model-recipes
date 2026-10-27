# Attribution And Licenses

Original recipe descriptions, metadata and numerical exports are
[CC BY 4.0](LICENSES/CC-BY-4.0.txt), with attribution to SourceHat. Original
standalone preparation/launch helpers and configuration templates are
[Apache-2.0](LICENSES/Apache-2.0.txt), with applicable attribution in
[NOTICE](NOTICE). [LICENSE](LICENSE) defines the scope. Downloaded model weights
retain their own licenses; this repository does not redistribute them.

| Component | Source | License / scope |
| --- | --- | --- |
| TabbyAPI | [theroyallab/tabbyAPI](https://github.com/theroyallab/tabbyAPI) | AGPL-3.0; `runtimes/tabby/tabbyapi.patch` retains that license |
| ExLlamaV3 | [turboderp-org/exllamav3](https://github.com/turboderp-org/exllamav3) | MIT; license preserved in `runtimes/tabby/licenses/ExLlamaV3.txt` |
| vLLM | [vllm-project/vllm](https://github.com/vllm-project/vllm) | Apache-2.0; copied package files retain upstream notices |
| vLLM backport image | [lazymio/vllm-backport](https://hub.docker.com/r/lazymio/vllm-backport) | Runtime/image dependencies retain their individual licenses |
| vllm-exl3 0.4.2 | [vcruz305/vllm-exl3](https://github.com/vcruz305/vllm-exl3) | AGPL-3.0-only; inherited MIT/Apache notices retained |
| PyTorch | [pytorch/pytorch](https://github.com/pytorch/pytorch) | Upstream BSD-style license; dependency only |
| Strata (archived configurations) | [Niko1221/Strata](https://github.com/Niko1221/Strata) | MIT; allocation-audit patch and original notice in `archive/runtime/` |
| llama.cpp (archived Strata dependency) | [ggml-org/llama.cpp](https://github.com/ggml-org/llama.cpp) | MIT; pinned dependency reference only, source not redistributed |

The pinned TabbyAPI upstream commit plus the complete captured patch identify
the modified source needed for this export. Its license text is in
`runtimes/tabby/licenses/tabbyAPI.txt`. The source patches are separate from
the repository's original Apache-2.0 code.

The vllm-exl3 plugin's current AGPL license, historical Apache license,
copyright notice and third-party notices are preserved together in
[`runtimes/deepseek/overlay/vllm_exl3-0.4.2.dist-info/licenses/`](runtimes/deepseek/overlay/vllm_exl3-0.4.2.dist-info/licenses/).
They identify its inherited ExLlamaV3, Mia's AI Lab and vLLM material and
travel with the runtime overlay. Local modifications to the extracted
plugin source retain the applicable upstream license.

The archived Strata profiles also credit [Unsloth](https://huggingface.co/unsloth/Qwen3.8-Flash-Next-GGUF)
and [Qwen](https://huggingface.co/Qwen/Qwen3.8-Flash-Next) at their recorded
revisions. Their checkpoint cards identify the Qwen Community 1.0 license;
model weights and prepared packs are not redistributed here. The Strata
allocation patch retains MIT, with its original notice in
[archive/runtime/LICENSE.Strata.txt](archive/runtime/LICENSE.Strata.txt).

Checkpoint publishers are credited in every recipe through their pinned
Hugging Face repository: Lygodactylus, turboderp, MikeRoz, SloptimistPrime,
svbmrgd, sfxnz, Qwen and incoai. Base model/runtime creators retain their
attribution and model-card terms. The external DFlash2 head's published
license applies to its downloaded files and any prepared local variant;
only the CPU preparation code is distributed here.

DeepSeek SM80 work also builds on
[StellarVoyager/DeepSeek-V4.1-Flash-A100-A800-SM80](https://huggingface.co/StellarVoyager/DeepSeek-V4.1-Flash-A100-A800-SM80)
at `f4dfddab1d7df657904a8a93eb85e69749437b92`. The preserved headers in the
runtime overlays identify additional upstream contributors.
