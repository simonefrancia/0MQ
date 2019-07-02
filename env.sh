#!/bin/bash
#
# @author Simone Francia (simone dot francia at musixmatch dot com)
# Copyright (c) 2018-2019 Musixmatch spa

export PORT=5556

export MXM_PREFIX=simonefmxm
export MXM_CONTAINER_NAME=0mq
export MXM_BASE_CONTAINER=$MXM_PREFIX/$MXM_CONTAINER_NAME
export MXM_BASE_NAME=$MXM_PREFIX-0mq
export MXM_VERSION=v0.0.1

echo Name:$MXM_CONTAINER_NAME
echo Container:$MXM_BASE_CONTAINER
echo Image:$MXM_BASE_NAME
echo Version:$MXM_VERSION
echo PORT:$PORT