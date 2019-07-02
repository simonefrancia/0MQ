#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#
# @author Simone Francia at musixmatch dot com
# Copyright (c) 2019 Musixmatch spa

import zmq
import time
import sys, os


def process_input():
    time.sleep(1)
    return

PORT = os.getenv('PORT', 3005)

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:%s" % PORT)

while True:
    #  Wait for next request from client
    message = socket.recv()
    print ("SERVER: Received request: ", message)
    process_input()
    socket.send_string("SERVER: World from %s" % PORT)