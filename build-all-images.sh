#!/usr/bin/env bash
set -Eeuo pipefail

if [ $# -ge 1 ] && [ -n "$1" ]; then
  S4TF_REPO_PATH="$1"
else
  echo "Missing path to google/swift-jupyter repository"
  echo "Usage: $0 ../path/to/swift-jupyter/git-repo"
  exit 1
fi

set -x

git -C $S4TF_REPO_PATH pull --ff-only

docker build --file ./swift-jupyter-base/Dockerfile --build-arg S4TF_CUDA_VERSION=10.2 --build-arg S4TF_CUDNN_VERSION=7 --tag "ctmnt/swift-jupyter-base" .
docker build --file ./swift-jupyter/Dockerfile --tag "ctmnt/swift-jupyter" $S4TF_REPO_PATH
docker build --file ./swift-jupyter-scipy/Dockerfile --tag "ctmnt/swift-jupyter-scipy" .
