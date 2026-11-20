# HY4 Flash EXL3 8.0 bpw serving

Use the [serving source](../source/) and the
[measured profile](REFERENCE-PROFILE.json) with the downloaded model
repository. This release uses 3 peer-connected 64 GiB CUDA
GPUs. Rank order is the order in `CUDA_VISIBLE_DEVICES`. The runtime
keeps the four packed Engram tables on NVMe, the embedding, projections
and BF16 head on CUDA, and the original RoPE and native DFly2 path.

Install CUDA-enabled PyTorch and Triton in your Python environment.
Install the ExLlamaV3 build from the sibling source tree with `python -m pip install --no-build-isolation ./hy4/source/exllama`.
Install Transformers for the local tokenizer. PyTorch, the CUDA toolkit
and compiler must support your GPUs and share the same CUDA ABI.

From `runtimes/standard-exl3`, set `PORT` to a free loopback port and
export `CUDA_VISIBLE_DEVICES` in rank order before launching:

```sh
python hy4/source/serve.py --model-dir /path/to/downloaded-model \
  --profile hy4/8.0bpw/REFERENCE-PROFILE.json --port "$PORT"
```

The launcher reads the root fixed-weight index, `standard-expert-packs/`
and `engram/` directly. Use `--engram-dir` if the 12 packed table shards
and their manifest are on a separate local NVMe volume. The loopback
API supports greedy text through `/v1/chat/completions` and
`/v1/completions`. Set `dfly2: true` on a request to use the native draft.
The default request context is 524,288; `max_context_tokens` can request
up to 1,048,576 with enough space in the 1,400,064-token shared Q8 pool.
The pool supports up to four simultaneous requests subject to that
shared capacity.

The 42-layer section replay trial measured 55-58 aggregate decode tokens/s across the tested short histories, versus 18-27 on the previous dispatch. CPU time per token fell 52-67%. The separate drain and refill test matched all ten measured phases. Rates exclude model load and prefill.
