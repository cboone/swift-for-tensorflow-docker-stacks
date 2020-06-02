# Start from the swift-jupyter base image
ARG BASE_CONTAINER=ctmnt/swift-jupyter
FROM $BASE_CONTAINER

# Install all OS dependencies for fully functional notebook server
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        dvipng \
        emacs-nox \
        ffmpeg \
        inkscape \
        jed \
        libhdf5-serial-dev \
        libopenblas-dev \
        libsm6 \
        libxext-dev \
        libxrender1 \
        lmodern \
        nano \
        netcat \
        python-dev \
        # ---- nbconvert dependencies ----
        texlive-xetex \
        texlive-fonts-recommended \
        texlive-generic-recommended \
        # Optional dependency
        texlive-fonts-extra \
        # ----
        tzdata \
        unzip \
        vim-tiny \
    && rm -rf /var/lib/apt/lists/*

# Install Python 3 packages
RUN python3 -m pip install --upgrade pip \
    && python3 -m pip install --no-cache-dir \
        # hdf5~=1.10 \
        # matplotlib-base~=3.2
        beautifulsoup4~=4.9 \
        bokeh~=2.0 \
        bottleneck~=1.3 \
        cloudpickle~=1.4 \
        cython~=0.29 \
        dask~=2.15 \
        dill~=0.3 \
        h5py~=2.10 \
        ipympl~=0.5 \
        ipywidgets~=7.5 \
        numba~=0.49 \
        numexpr~=2.7 \
        pandas~=1.0 \
        patsy~=0.5 \
        protobuf~=3.11 \
        scikit-image~=0.16 \
        scikit-learn~=0.22 \
        scipy~=1.4 \
        seaborn~=0.10 \
        sqlalchemy~=1.3 \
        statsmodels~=0.11 \
        sympy~=1.5 \
        tables~=3.6 \
        tensorflow~=2.2 \
        vincent~=0.4 \
        widgetsnbextension~=3.5 \
        xlrd~=1.2 \

    # Activate ipywidgets extension in the environment that runs the notebook server
    && jupyter nbextension enable --py widgetsnbextension \
    # Also activate ipywidgets extension for JupyterLab
    # Check this URL for most recent compatibilities
    # https://github.com/jupyter-widgets/ipywidgets/tree/master/packages/jupyterlab-manager
    && jupyter labextension install @jupyter-widgets/jupyterlab-manager@^2.0.0 --no-build \
    && jupyter labextension install @bokeh/jupyter_bokeh@^2.0.0 --no-build \
    && jupyter labextension install jupyter-matplotlib@^0.7.2 --no-build \
    && jupyter lab build -y \
    && jupyter lab clean -y \
    && npm cache clean --force \
    && rm -rf /.root/.cache/yarn \
    && rm -rf /root/.node-gyp

# Import matplotlib the first time to build the font cache.
ENV XDG_CACHE_HOME /.root/.cache/
RUN MPLBACKEND=Agg python3 -c "import matplotlib.pyplot"
