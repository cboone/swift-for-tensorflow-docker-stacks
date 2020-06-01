# ctmnt/base-for-s4tf Docker image

This is the base image upon which all the Swift images are built. It is currently based on [tensorflow/swift's base-deps Dockerfile](https://github.com/google/swift-jupyter/blob/master/docker/Dockerfile).

## Building the image

```bash
# from the root of this repository
docker build --file ./base-for-s4tf/Dockerfile --build-arg S4TF_CUDA_VERSION=10.2 --build-arg S4TF_CUDNN_VERSION=7 --tag "ctmnt/base-for-s4tf" .
```
