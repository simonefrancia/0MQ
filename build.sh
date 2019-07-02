#!/bin/bash
#
# @author Simone Francia (simone dot francia at musixmatch dot com)
# Copyright (c) 2018-2019 Musixmatch spa

docker build --build-arg PORT=$PORT -t $MXM_BASE_CONTAINER:$MXM_VERSION .
    