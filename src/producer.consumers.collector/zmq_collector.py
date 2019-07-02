#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#
# @author Simone Francia at musixmatch dot com
# Copyright (c) 2019 Musixmatch spa

import time, os
import zmq
import pprint


PORT = os.getenv('PORT', 3005)

OUT_PORT = str(int(PORT) + 1)

def result_collector():
    
    context = zmq.Context()
    results_receiver = context.socket(zmq.PULL)
    results_receiver.bind("tcp://127.0.0.1:%s"  % str(OUT_PORT))
    collecter_data = {}

    for x in range(1000):

        print(x)

        result = results_receiver.recv_json()

        if result['consumer'] in collecter_data:
            collecter_data[result['consumer']] = collecter_data[result['consumer']] + 1
        else:
            collecter_data[result['consumer']] = 1

        if x == 999:
            pprint.pprint(collecter_data)

    print(OUT_PORT)

result_collector()