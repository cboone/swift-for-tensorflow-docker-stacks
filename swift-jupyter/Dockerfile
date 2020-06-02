# Start from the Swift Jupyter base image
FROM ctmnt/swift-jupyter-base

# Add Swift to the PATH
ENV PATH="$PATH:/swift-tensorflow-toolchain/usr/bin/"

# Allow the caller to specify the toolchain to use
ARG swift_tf_url=https://storage.googleapis.com/swift-tensorflow-artifacts/nightlies/latest/swift-tensorflow-DEVELOPMENT-cuda10.2-cudnn7-ubuntu18.04.tar.gz

# Download and extract S4TF
WORKDIR /swift-tensorflow-toolchain
RUN curl -sL $swift_tf_url | tar -xz

# Install Node (for Jupyter Lab)
RUN curl -sL https://deb.nodesource.com/setup_14.x | bash - \
    && apt-get install -y --no-install-recommends nodejs \
    && rm -rf /var/lib/apt/lists/*

# Install some Python libraries that are useful to call from Swift
WORKDIR /swift-jupyter
RUN python3 -m pip install --upgrade pip \
    && python3 -m pip install --no-cache-dir \
        gym==0.17.2 \
        ipykernel==5.3.0 \
        jupyterhub==1.1.0 \
        jupyterlab==2.1.4 \
        jupyter_kernel_gateway==2.4.0 \
        jupyter_kernel_test==0.3 \
        matplotlib==3.2.1 \
        notebook==6.0.3 \
        numpy==1.18.4 \
        pandas==1.0.4 \
    && jupyter lab build -y \
    && jupyter lab clean -y \
    && npm cache clean --force

# Copy the kernel into the container
WORKDIR /swift-jupyter
COPY . .

# Register the kernel with Jupyter
RUN python3 register.py --user --swift-toolchain /swift-tensorflow-toolchain --swift-python-library /usr/lib/x86_64-linux-gnu/libpython3.6m.so --kernel-name "Swift"

# Create the notebooks dir for mounting
RUN mkdir /notebooks
WORKDIR /notebooks

EXPOSE 8888

# Run Jupyter on container start, using the tini ENTRYPOINT
CMD ["python3", "-m", "jupyter", "lab"]
