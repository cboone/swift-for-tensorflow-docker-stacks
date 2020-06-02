# ctmnt/swift-jupyter Docker image

This image provides a basic Jupyter Notebook server with Swift for Tensorflow support. It is (intended to be) functionally similar to [google/swift-jupyter's Dockerfile](https://github.com/google/swift-jupyter/blob/master/docker/Dockerfile), with some minor additions and some major omissions.

For more information, see [the image details section on the main README](../README.md#image-details).

## Setting up to build the image

- This image is built on [the swift-jupyter-base image](../swift-jupyter-base). Build that one first.

- Clone or update [the google/swift-jupyter repository](https://github.com/google/swift-jupyter).

## Building the image

From the root of this repository, assuming that the google/swift-jupyter repository is in the same parent directory:

```bash
docker build --file ./swift-jupyter/Dockerfile --tag "ctmnt/swift-jupyter" ../swift-jupyter
```

## Running the image

### Running Jupyter Lab

```bash
docker run --rm --publish 8888:8888 --cap-add SYS_PTRACE --mount type=bind,source=/your/local/notebooks,destination=/notebooks ctmnt/swift-jupyter
```

- `--rm` removes the container once it stops running.

- `--publish 8888:8888` exposes the port on which Jupyter is running to the host.

- `--cap-add SYS_PTRACE` adjusts the privileges with which this container is run, which is required for the Swift REPL.

- `--mount type=bind,src=/<host path>,dst=/notebooks` bind mounts a host directory as a volume where notebooks created in the container will be stored.  If this command is omitted, any notebooks created using the container will not be persisted when the container is stopped.
-
Optionally, specify a local configuration file to override the image defaults:

```bash
docker run --rm --publish 8888:8888 --cap-add SYS_PTRACE --mount type=bind,source=/your/local/notebooks,destination=/notebooks --mount type=bind,source=/your/local/jupyter_notebook_config.py,destination=/root/.jupyter/jupyter_notebook_config.py ctmnt/swift-jupyter
```

### Running a Swift for Tensorflow kernel gateway

As of Jupyter Notebook 6.0, you can use `--gateway-url=` to specify a separate [Jupyter Kernel Gateway](https://github.com/jupyter/kernel_gateway). (Or use the [nb2kg](https://github.com/jupyter/nb2kg) server extension for pre-6.0 versions of Notebook.) This allows running the Swift for Tensorflow Jupyter kernel in a Docker container while running Jupyter Notebook somewhere else, such as your local machine.

To run the swift-jupyter image as a kernel gateway:

```bash
docker run --rm --publish 9999:9999 --cap-add SYS_PTRACE ctmnt/swift-jupyter python3 -m jupyter kernelgateway
```

- `python3 -m jupyter kernelgateway` overrides the default command in the Dockerfile to launch the kernel gateway instead (making sure to use the correct Python and respective Jupyter).

- `--publish 9999:9999` exposes the port on which the kernel gateway is running to the host.

With the gateway running, start Jupyter Notebook in your notebook directory and pass the URL of your kernel gateway:

```bash
jupyter notebook --gateway-url 127.0.0.1:9999
```

Optionally, specify a local configuration file to override the image defaults:

```bash
docker run --rm --publish 9999:9999 --cap-add SYS_PTRACE --mount type=bind,source=/your/local/jupyter_kernel_gateway_config.py,destination=/root/.jupyter/jupyter_kernel_gateway_config.py ctmnt/swift-jupyter python3 -m jupyter kernelgateway
```

## Testing the image

```bash
docker run --rm --cap-add SYS_PTRACE ctmnt/swift-jupyter python3 /swift-jupyter/test/all_test_docker.py
```
