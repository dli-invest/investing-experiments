FROM mcr.microsoft.com/vscode/devcontainers/anaconda:dev-3

ARG conda_env=algo_trading

RUN conda create -n algo_trading python=3.6.9
ENV PATH /opt/conda/envs/$conda_env/bin:$PATH
ENV CONDA_DEFAULT_ENV $conda_env
# Activate the environment, and make sure it's activated:
# Make RUN commands use the new environment:
# SHELL ["conda", "run", "-n", "algo_trading", "/bin/bash", "-c"]
RUN conda info --envs
RUN python --version
# do zipline install manually
RUN conda install -n algo_trading -c conda-forge zipline
RUN conda install jupyter
# Dont need to copy environment files over
# COPY environment.yml* .devcontainer/noop.txt /tmp/conda-tmp/
# RUN if [ -f "/tmp/conda-tmp/environment.yml" ]; then /opt/conda/bin/conda env update -n base -f /tmp/conda-tmp/environment.yml; fi \
#     && rm -rf /tmp/conda-tmp
COPY scripts/extension.py  .
RUN mkdir -p ~/.zipline && cp extension.py ~/.zipline/extension.py
ENTRYPOINT [ "/bin/bash" ]