# See here for image contents: https://github.com/microsoft/vscode-dev-containers/tree/v0.134.0/containers/python-3/.devcontainer/base.Dockerfile
ARG VARIANT="3.5"
ARG ZIPLINE_REF
FROM mcr.microsoft.com/vscode/devcontainers/python:0-${VARIANT}

# [Optional] Allow the vscode user to pip install globally w/o sudo
ENV PIP_TARGET=/usr/local/pip-global
ENV PYTHONPATH=${PIP_TARGET}:${PYTHONPATH}
ENV PATH=${PIP_TARGET}/bin:${PATH}
RUN mkdir -p ${PIP_TARGET} \
  && chown vscode:root ${PIP_TARGET} \
  && echo "if [ \"\$(stat -c '%U' ${PIP_TARGET})\" != \"vscode\" ]; then chown -R vscode:root ${PIP_TARGET}; fi" \
  | tee -a /root/.bashrc /home/vscode/.bashrc /root/.zshrc >> /home/vscode/.zshrc 

ENV ZIPLINE_REF ${ZIPLINE_REF:-master}
ENV ZIPLINE_ROOT /zipline
ENV ZIPLINE_USER zipline
ENV ZIPLINE_GROUP zipline
ENV PYTHONUSERBASE /lib/zipline
ENV PATH $PYTHONUSERBASE/bin:$PATH

RUN apk add --no-cache --virtual .build-deps \
  build-base \
  ca-certificates \
  curl \
  gfortran \
  git \
  openblas-dev \
  python3-dev && \
  apk add --no-cache --virtual .hdf5-dev \
  --repository http://dl-cdn.alpinelinux.org/alpine/edge/testing/ \
  hdf5-dev && \
  ln -v -s /usr/include/locale.h /usr/include/xlocale.h && \
  git clone \
  --single-branch \
  --branch $ZIPLINE_REF \
  https://github.com/quantopian/zipline.git /src/zipline.git && \
  cd /src/zipline.git && \
  export NPY_NUM_BUILD_JOBS=$(getconf _NPROCESSORS_ONLN) && \
  pip3 install \
  --no-cache-dir \
  --no-compile \
  -r etc/requirements.txt && \
  ZIPLINE_SRC=/src/zipline-$(python3 setup.py version |grep ^Version |awk '{print $2}') && \
  mkdir -v \
  $ZIPLINE_SRC && \
  rm -v \
  .gitattributes && \
  git archive \
  --worktree-attributes \
  HEAD |tar -v -C $ZIPLINE_SRC -x && \
  ln -v -s $ZIPLINE_SRC /src/zipline && \
  cd $ZIPLINE_SRC && \
  pip3 install \ 
  --no-cache-dir \
  --no-compile \
  --editable \
  . && \
  rm -rf \
  build \
  /src/zipline.git && \
  addgroup $ZIPLINE_GROUP && \
  adduser \
  -D \
  -G $ZIPLINE_GROUP \
  -h $ZIPLINE_ROOT \
  -s /sbin/nologin \
  $ZIPLINE_USER && \
  chown -R $ZIPLINE_USER:$ZIPLINE_GROUP \
  /src && \
  install -v -d -o $ZIPLINE_USER -g $ZIPLINE_GROUP \
  $PYTHONUSERBASE && \
  apk del --no-cache \
  .build-deps \
  .hdf5-dev && \
  apk add --no-cache \
  ca-certificates \
  libstdc++ \
  openblas \
  # https://github.com/markpfletcher/graphviz-docker/issues/1
  font-bitstream-type1 \
  python3 && \
  apk add --no-cache \
  --repository http://dl-cdn.alpinelinux.org/alpine/edge/testing/ \
  hdf5
RUN pip install requests pandas scipy
RUN pip install zipline
# [Optional] If your pip requirements rarely change, uncomment this section to add them to the image.
# COPY requirements.txt /tmp/pip-tmp/
# RUN pip3 --disable-pip-version-check --no-cache-dir install -r /tmp/pip-tmp/requirements.txt \
#    && rm -rf /tmp/pip-tmp

# [Optional] Uncomment this section to install additional OS packages.
# RUN apt-get update \
#     && export DEBIAN_FRONTEND=noninteractive \
#     && apt-get -y install --no-install-recommends <your-package-list-here>