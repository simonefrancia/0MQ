#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#
# @author Simone Francia at musixmatch dot com
# Copyright (c) 2019 Musixmatch spa

import zmq
import sys, os

PORT = os.getenv('PORT', 3005)

context = zmq.Context()
print ("Connecting to server...")
socket = context.socket(zmq.REQ)
socket.connect ("tcp://127.0.0.1:%s" % str(PORT) )

#  Do 10 requests, waiting each time for a response
for request in range (1,10):
    print ("CLIENT : Sending request ", request,"...")
    socket.send_string("Hello")
    #  Get the reply.
    message = socket.recv()
    print ("CLIENT: Received reply ", request, "[", message, "]")