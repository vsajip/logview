# Using a ZeroMQ-based proxy for logging #

Often, the machine on which you run `logview` will not have a stable IP address: for example if it's a desktop machine, it may well have a dynamic IP address obtained via DHCP. If you're using a [ZeroMQHandler](http://code.google.com/p/logview/wiki/ZeroMQHandler) to send log messages from your applications, it could connect to a proxy on a suitable server machine _with_ a stable IP address, to which you can connect `logview`. For example, say you have three logically different machines: `server` which runs the application generating logs, `proxy` which runs a ZeroMQ proxying application, and `desktop` which runs `logview`.

The following script can be run on `proxy`. It assumes that on `server`, a ZeroMQ PUB socket has been set up on port 9024, to which logging events are published. The proxy listens for events published by the server and republishes them on port 9025.

You can then get `logview` to pick up the republished events using

```
logview -z proxy:9025
```

Of course, you would substitute the appropriate host names for `server` and `proxy`.

Here's the proxy script:
```
import zmq

def main():
    ctx = zmq.Context()
    upstream = zmq.Socket(ctx, zmq.SUB)
    upstream.connect('tcp://server:9024')
    downstream = zmq.Socket(ctx, zmq.PUB)
    downstream.bind('tcp://0.0.0.0:9025')
    upstream.setsockopt(zmq.SUBSCRIBE, '')
    try:
        n = 0
        while True:
            message = upstream.recv()
            downstream.send(message)
            n += 1
            if (n % 10) == 0:
                print('%d messages proxied' % n)
    finally:
        upstream.close()
        downstream.close()

if __name__ == '__main__':
    main()
```