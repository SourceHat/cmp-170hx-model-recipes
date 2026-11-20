# Choosing and applying a serving profile

Use the [runtime index](RUNTIMES.json) to select the code, model snapshot
and profile for the same quant. The snapshots are pinned to measured
public revisions. Install only one of the included ExLlamaV3 trees in
each environment.

Run the commands from `runtimes/standard-exl3` in this checkout.

| Build | Devices | Shared KV pool | Session limit | Prefill chunks |
| --- | --- | --- | --- | --- |
| HY4 Flash 4.875 | 2 x 64 GiB with direct CUDA P2P | Q8, 1,400,064 tokens | 4 | HY4 launcher |
| HY4 Flash 8.0 | 3 x 64 GiB with direct CUDA P2P | Q8, 1,400,064 tokens | 4 | HY4 launcher |
| Sage S2.1 Flash 4.25 | 3 x 64 GiB with direct P2P layer split | Q8, 1,048,576 tokens | 8 | 2,048 |
| SenseNova Loop 9B 3.0 | 1 CUDA GPU | Q8, 262,144 tokens | 4 | 1,024 |
| SenseNova Loop 9B 5.25 | 1 CUDA GPU | Q6, 262,144 tokens | 4 | 512 |
| SenseNova Loop 9B 8.0 | 1 CUDA GPU | Q8, 1,048,576 tokens | 8 | 512 |

These are shared pools. A session limit is an admission setting, not a
claim that every session can fill its individual context window at
once. The linked guides give measured scope and the distinction between
decode and first-token time.

## HY4 Flash

Use `hy4/source/serve.py`. Its `--check-layout` mode validates
the downloaded fixed-weight index, expert files and 12 Engram shards
before loading CUDA. Keep the Engram files on NVMe; use `--engram-dir`
when they are outside the model directory. List the visible GPUs in
measured rank order with `CUDA_VISIBLE_DEVICES`; the JSON's
`block_ranks` refers to those local positions. The launcher checks
direct peer access.

The local API serves greedy text. It uses target-only decode unless a
request sets `dfly2: true`. Use 524,288 as the default request ceiling;
larger allowed requests share the same cache pool.

## Sage and SenseNova

Install the matching `source/` directory from the serving guide in a
CUDA PyTorch environment. Run the server with the local model snapshot
as its model directory. Map the profile to these server options:

| Profile field | Server setting |
| --- | --- |
| `parallelism`, `transport` | For Sage, select a whole-layer split across three directly peer-connected devices. Leave tensor parallel disabled for this profile. |
| `cache_mode`, `shared_cache_tokens` | Select the paged KV precision and total token budget across the requests. |
| `max_request_tokens`, `max_sessions` | Set the request token ceiling and concurrent admission limit. |
| `chunk_size` | Set the prefill chunk length shown for the selected build. |
| `draft_mode` | Leave external drafting disabled for these target-only profiles. |
| `env` | For Sage, set `EXL3_SAGE_BATCHED_POOL=1` and `EXL3_SAGE_BATCHED_INDEXER=1` before importing ExLlamaV3. |
| `tuning` | Describes the runtime choices already wired into this source tree. Use the matching source rather than copying defaults between quants. |

Example source install:

```sh
python -m pip install 'setuptools>=77' wheel ninja
python -m pip install --no-build-isolation ./sage/4.25bpw/source
```

The checkout contains CUDA extension source. A CPU-only packaging check
can build a wheel with `EXLLAMA_NOCOMPILE=1`; normal inference still
needs the native extension and a compatible CUDA environment.
