# ZMQ Hello World

Hello world with ZMQ binding in Python3

## CLIENT/SERVER MODE


<p align="center">
    <img src=data/reqrep.png?raw=true" width="500">
</p>

``` cd client.server ```

### Launch Server
```python3 zmq_server.py & ```


### Launch Client
```python3 zmq_client.py```

### Output

```Connecting to server...
CLIENT : Sending request  1 ...
SERVER: Received request:  b'Hello'
CLIENT: Received reply  1 [ b'SERVER: World from 5556' ]
CLIENT : Sending request  2 ...
SERVER: Received request:  b'Hello'
CLIENT: Received reply  2 [ b'SERVER: World from 5556' ]
CLIENT : Sending request  3 ...
SERVER: Received request:  b'Hello'
CLIENT: Received reply  3 [ b'SERVER: World from 5556' ]
CLIENT : Sending request  4 ...
SERVER: Received request:  b'Hello'
CLIENT: Received reply  4 [ b'SERVER: World from 5556' ]
CLIENT : Sending request  5 ...
SERVER: Received request:  b'Hello'
CLIENT: Received reply  5 [ b'SERVER: World from 5556' ]
.....
.....
```

## PUSH/PULL MODE - PRODUCER/CONSUMERS/COLLECTOR

<p align="center">
    <img src=data/pushpull.png?raw=true" width="500">
</p>


``` cd producer.consumers.collector```


### Launch Consumers
```python3 zmq_consumer.py ```


### Launch Collector
```python3 zmq_collector.py  ```


### Launch Producers (THIS MUST BE THE LAST TO LAUNCH)
```python3 zmq_producer.py ```






