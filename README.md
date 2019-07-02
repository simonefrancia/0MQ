# 0MQ Hello World

Hello world with 0MQ binding in Python3

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
