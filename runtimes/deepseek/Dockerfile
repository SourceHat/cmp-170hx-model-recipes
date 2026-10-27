FROM docker.io/lazymio/vllm-backport@sha256:349690323ab9aba712111529ed1ca60730199205d8202f67895ffde85b451be3

ENV TORCH_CUDA_ARCH_LIST=8.0 MAX_JOBS=4
USER root
RUN apt-get update && apt-get install -y --no-install-recommends git build-essential ninja-build \
    && rm -rf /var/lib/apt/lists/*
COPY runtimes/tabby/exllamav3.patch /tmp/exllamav3.patch
RUN git clone --no-checkout https://github.com/turboderp-org/exllamav3.git /runtime/exllamav3 \
    && git -C /runtime/exllamav3 checkout --detach d3739fd393337b1ff4d6c2a342b12f0c87a9592f \
    && git -C /runtime/exllamav3 apply /tmp/exllamav3.patch \
    && python3 -m pip install --no-deps --no-build-isolation /runtime/exllamav3
COPY runtimes/deepseek/overlay/ /usr/local/lib/python3.12/dist-packages/
COPY scripts/serve_vllm.py /recipe/scripts/serve_vllm.py
ENV PYTHONPATH=/usr/local/lib/python3.12/dist-packages
WORKDIR /recipe
ENTRYPOINT ["python3", "/recipe/scripts/serve_vllm.py", "--runtime", "/runtime", "--engine", "deepseek", "--"]
