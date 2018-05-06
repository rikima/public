#!/bin/sh
docker run \
    -it \
    -p 8000:8000 \
    -v $PWD:$PWD -w $PWD \
    -v $HOME/.bash_profile:/root/.bash_profile \
    -v $HOME/.gitconfig:/root/.gitconfig \
    -v $HOME/.ssh:/root/.ssh \
    -v $HOME/.vimrc:/root/.vimrc \
    --name django_ldap \
    --rm \
    django_ldap \
    /bin/bash
