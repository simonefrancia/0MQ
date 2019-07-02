FROM ubuntu:18.04

RUN apt-get update && apt-get install libzmq3-dev -y

RUN apt-get install python3-dev python3-pip -y

RUN pip3 install --no-use-wheel pyzmq


################################################ ENV

WORKDIR /root/src

EXPOSE $PORT
