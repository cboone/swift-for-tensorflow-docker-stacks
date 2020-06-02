# A Docker image with all dependencies required to run (not build) an S4TF toolchain.

# Allow builder to specify CUDA versions
ARG S4TF_CUDA_VERSION
ARG S4TF_CUDNN_VERSION

# Start from nvidia/cuda base image
FROM nvidia/cuda:${S4TF_CUDA_VERSION}-cudnn${S4TF_CUDNN_VERSION}-devel-ubuntu18.04

# ARGs from before FROM are cleared after the FROM, so we repeat ourselves.
ARG S4TF_CUDA_VERSION
ARG S4TF_CUDNN_VERSION

ENV DEBIAN_FRONTEND=noninteractive

# Install dependencies
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        build-essential \
        ca-certificates \
        clang \
        curl \
        git \
        libblocksruntime-dev \
        libbsd-dev \
        libcurl4-openssl-dev \
        libicu-dev \
        libncurses5-dev \
        libpython-dev \
        libpython3-dev \
        libxml2 \
        python \
        python-dev \
        python-pip \
        python-setuptools \
        python-tk \
        python3 \
        python3-dev \
        python3-pip \
        python3-setuptools \
        run-one \
    && rm -rf /var/lib/apt/lists/*

# Install Python libraries
RUN python3 -m pip install --upgrade pip \
    && python3 -m pip install --no-cache-dir \
        junit-xml==1.9 \
        psutil==5.7.0

# Configure CUDA
RUN echo "/usr/local/cuda-${S4TF_CUDA_VERSION}/targets/x86_64-linux/lib/stubs" > /etc/ld.so.conf.d/cuda-${S4TF_CUDA_VERSION}-stubs.conf \
    && ldconfig

# Copy local files as late as possible to avoid cache busting
# Jupyter config needs to be copied here, as it's needed by
# the swift-jupyter image but isn't in that image's build context
COPY config/jupyter_notebook_config.py /etc/jupyter/

# Install and configure tini as the ENTRYPOINT
ENV TINI_VERSION="v0.18.0"
RUN curl -SLO https://github.com/krallin/tini/releases/download/${TINI_VERSION}/tini \
  && chmod +x /tini
ENTRYPOINT ["/tini", "-g", "--"]

# Use bash as the default command
CMD ["/bin/bash"]
