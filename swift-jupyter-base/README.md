# ctmnt/swift-jupyter-base Docker image

This is the base image upon which all the Swift for Tensorflow images are built. It should be functionally the same as [tensorflow/swift's base-deps Dockerfile](https://github.com/google/swift-jupyter/blob/master/docker/Dockerfile).

For more information, see [the image details section on the main README](../README.md#image-details).

## Building the image

```bash
# from the root of this repository
docker build --file ./swift-jupyter-base/Dockerfile --build-arg S4TF_CUDA_VERSION=10.2 --build-arg S4TF_CUDNN_VERSION=7 --tag "ctmnt/swift-jupyter-base" .
```

## Running the image

There's generally no need to run this image, other than for debugging image generation. But you can:

```bash
docker run -it --rm ctmnt/swift-jupyter-base
```