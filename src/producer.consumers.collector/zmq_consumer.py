#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#
# @author Simone Francia at musixmatch dot com
# Copyright (c) 2019 Musixmatch spa

import time, os
import zmq
import random

PORT = os.getenv('PORT', 3005)

IN_PORT = PORT
OUT_PORT = str(int(PORT) + 1)

def consumer():

    consumer_id = random.randrange(1,10005)
    
    context = zmq.Context()

    # receive work
    consumer_receiver = context.socket(zmq.PULL)
    consumer_receiver.connect("tcp://127.0.0.1:%s" % str(IN_PORT))

    # send work
    consumer_sender = context.socket(zmq.PUSH)
    consumer_sender.connect("tcp://127.0.0.1:%s" % str(OUT_PORT) )
    
    while True:
        print("receiving...")
        work = consumer_receiver.recv_json()
        print(work)
        
        data = work['num']
        result = { 'consumer' : consumer_id, 'num' : data}
        if data%2 == 0: 
            consumer_sender.send_json(result)

consumer()