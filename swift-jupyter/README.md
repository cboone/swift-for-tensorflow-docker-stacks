# ctmnt/swift-jupyter Docker image

This image provides a basic Jupyter Notebook server with Swift for Tensorflow support. It is functionally similar to [google/swift-jupyter's Dockerfile](https://github.com/google/swift-jupyter/blob/master/docker/Dockerfile), with some minor additions.

This image is built on [the swift-jupyter-base image](../swift-jupyter-base). Build that one first.

## Setting up to build the image

Clone or update [the google/swift-jupyter repository](https://github.com/google/swift-jupyter).

## Building the image

From the root of this repository, assuming that the google/swift-jupyter repository is in the same parent directory:

```bash
docker build --file ./swift-jupyter/Dockerfile --tag "ctmnt/swift-jupyter" ../swift-jupyter
```

## Running the image

```bash
docker run --rm --publish 8888:8888 --cap-add SYS_PTRACE --mount type=bind,src=/Users/hpg/Development/swift-neural-intuition,dst=/notebooks ctmnt/swift-jupyter
```

- `--rm` removes the container once it stops running.

- `--publish 8888:8888` exposes the port on which Jupyter is running to the host.

- `--cap-add SYS_PTRACE` adjusts the privileges with which this container is run, which is required for the Swift REPL.

- `--volume <host path>:/notebooks` bind mounts a host directory as a volume where notebooks created in the container will be stored.  If this command is omitted, any notebooks created using the container will not be persisted when the container is stopped.

