# ctmnt/swift-jupyter-scipy Docker image

This image provides a more completely functional Jupyter Notebook server with Swift for Tensorflow support. It is (intended to be) functionally similar to [google/swift-jupyter's Dockerfile](https://github.com/google/swift-jupyter/blob/master/docker/Dockerfile), with some major omissions and the addition of a range of popular Python scientific computing packages.

For more information, see [the image details section on the main README](../README.md#image-details).

## Setting up to build the image

This image is built on [the swift-jupyter image](../swift-jupyter). Build that one first.

## Building the image

```bash
docker build --file ./swift-jupyter-scipy/Dockerfile --tag "ctmnt/swift-jupyter-scipy" .
```

## Running the image

For more information, see [the swift-jupyter image](../swift-jupyter/README.md#running-the-image).

### Running Jupyter Lab

```bash
docker run --rm --publish 8888:8888 --cap-add SYS_PTRACE --mount type=bind,source=/your/local/notebooks,destination=/notebooks ctmnt/swift-jupyter-scipy
```

### Running a Swift for Tensorflow kernel gateway

```bash
docker run --rm --publish 9999:9999 --cap-add SYS_PTRACE ctmnt/swift-jupyter-scipy python3 -m jupyter kernelgateway
```

## Testing the image

```bash
docker run --rm --cap-add SYS_PTRACE ctmnt/swift-jupyter-scipy python3 /swift-jupyter/test/all_test_docker.py
```
