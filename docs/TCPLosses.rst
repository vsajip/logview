Loss of messages sent over TCP
==============================

If you run ``logview`` after your application starts sending, you may lose messages. That's because the ``SocketHandler`` implementation uses an exponential back-off algorithm when a socket error is encountered. When your application fails to open a connection to ``logview`` (because it hasn't been run yet), the ``SocketHandler`` instance will drop the message it was trying to send. When subsequent messages are handled by the same ``SocketHandler`` instance, it will not try connecting until some time has passed. The default parameters are such that the initial delay is one second, and if after that delay the connection still can't be made, the handler will double the delay each time up to a maximum of 30 seconds.

If you encounter this problem, you can either use your own subclass of ``SocketHandler`` which tries connecting every time, or use a solution based on ``ZeroMQ`` using a proxy (see the ``ZeroMQProxy`` page). You can also use a ``DatagramHandler`` rather than a ``SocketHandler``, but as UDP makes no delivery guarantees, you could still lose messages.
