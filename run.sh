#!/bin/bash
#
# @author Simone Francia (simone dot francia at musixmatch dot com)
# Copyright (c) 2018-2019 Musixmatch spa

docker run --rm -it -p $PORT:$PORT -e PORT=$PORT -v "`pwd`/src":/root/src $MXM_BASE_CONTAINER:$MXM_VERSION bash