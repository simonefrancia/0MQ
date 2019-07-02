#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#
# @author Simone Francia at musixmatch dot com
# Copyright (c) 2019 Musixmatch spa

import time, os
import zmq

PORT = os.getenv('PORT', 3005)


def producer():
    context = zmq.Context()
    zmq_socket = context.socket(zmq.PUSH)
    zmq_socket.bind("tcp://127.0.0.1:%s" % str(PORT) )
    # Start your result manager and workers before you start your producers
    for num in range(20000):
        print("producing...")
        work_message = { 'num' : num }
        print(num)
        time.sleep(1)
        zmq_socket.send_json(work_message)

producer()