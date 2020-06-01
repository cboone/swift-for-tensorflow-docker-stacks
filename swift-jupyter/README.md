# ctmnt/swift-jupyter Docker image

This image is currently a mirror of [google/swift-jupyter's Dockerfile](https://github.com/google/swift-jupyter/blob/master/docker/Dockerfile) and builds on the [base-for-s4tf](../base-for-s4tf) image. Build that one first.

## Requirements

Clone or update the [google/swift-jupyter](https://github.com/google/swift-jupyter) repository.

## Building the image

From the root of this repository, assuming that the google/swift-jupyter repository is in the same parent directory:

```bash
docker build --file ./swift-jupyter/Dockerfile --tag "ctmnt/swift-jupyter" ../swift-jupyter
```
