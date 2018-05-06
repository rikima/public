FROM ubuntu:16.04
ENV LANG=ja_JP.UTF-8 \
    LC_ALL=ja_JP.UTF-8
RUN set -ex && apt-get update && apt-get upgrade -y && apt-get install -y \
    bash-completion \
    curl \
    git \
    language-pack-ja \
    python3 \
    python3-pip \
    sqlite3 \
    vim \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*
RUN echo ". /etc/bash_completion" >> /root/.bashrc
COPY requirements.txt /tmp/
RUN pip3 install -r /tmp/requirements.txt
