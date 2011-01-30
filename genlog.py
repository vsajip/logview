#!/usr/bin/env python
"""
Simple script to generate logging messages and send to TCP/UDP sockets.
"""
import logging
from logging.handlers import (SocketHandler, DatagramHandler,
                              DEFAULT_TCP_LOGGING_PORT,
                              DEFAULT_UDP_LOGGING_PORT)
import optparse
import random
import sys
import time

class LogData(object):
    def __init__(self, loggers):
        self.loggers = loggers
        self.msgno = 0
        self.levels = (logging.DEBUG, logging.INFO, logging.WARNING,
                       logging.ERROR, logging.CRITICAL)

    def what_to_log(self):
        dest = logging.getLogger(random.choice(self.loggers))
        level = random.choice(self.levels)
        msgno = self.msgno
        self.msgno += 1
        return dest, level, msgno

class Thing(object):
    def deep_doo_doo(self, log_data):
        if random.random() <= 0.5:
            raise Exception()
        else:
            dest, level, msgno = log_data.what_to_log()
            dest.log(level, 'Message no. %d', msgno)

thing = Thing()

def doo_doo(log_data):
    if random.random() <= 0.5:
        thing.deep_doo_doo(log_data)
    else:
        if random.random() <= 0.5:
            raise Exception()
        else:
            dest, level, msgno = log_data.what_to_log()
            dest.log(level, 'Message no. %d', msgno)

def get_addr(s, default_port):
    if ':' not in s:
        result = s, default_port
    else:
        h, p = s.split(':')
        result = h, int(p)
    return result

def main():
    parser = optparse.OptionParser()
    parser.add_option('-c', '--count', default=0, type='int', dest='count',
                      help='Number of messages to log')
    parser.add_option('-d', '--delay', default=300, type='int', dest='delay',
                      help='Amount to delay after each iteration (msecs, default is 300)')
    parser.add_option('-e', '--exceptions', default=0.25, type='float', dest='excprob',
                      help='Probability for raising exceptions (default is 0.25)')
    parser.add_option('', '--host', dest='hostname',
                      help='Send all logs to specified host using default ports')
    parser.add_option('-t', '--tcp', default='localhost', dest='tcphost',
                      help='Where to send TCP logs (host[:port])')
    parser.add_option('-u', '--udp', default='localhost', dest='udphost',
                      help='Where to send UDP logs (host[:port])')
    options, args = parser.parse_args()

    tcp_logger = logging.getLogger('tcp')
    udp_logger = logging.getLogger('udp')

    levels = (logging.DEBUG, logging.INFO, logging.WARNING,
              logging.ERROR, logging.CRITICAL)

    components = ['jim', 'fred', 'sheila']

#    The code below is replaced with a literal list, as Python 2.5 doesn't have
#    itertools.permutations
#
#    from itertools import permutations
#    loggers = []
#    for i in range(1, 4):
#        for p in permutations(components, i):
#            s = '.'.join(('tcp',) + p)
#            loggers.append(s)
#            s = '.'.join(('udp',) + p)
#            loggers.append(s)
#    print loggers
    
    loggers = [
        'tcp.jim', 'udp.jim',
        'tcp.fred', 'udp.fred',
        'tcp.sheila', 'udp.sheila',
        'tcp.jim.fred', 'udp.jim.fred',
        'tcp.jim.sheila', 'udp.jim.sheila',
        'tcp.fred.jim', 'udp.fred.jim',
        'tcp.fred.sheila', 'udp.fred.sheila',
        'tcp.sheila.jim', 'udp.sheila.jim',
        'tcp.sheila.fred', 'udp.sheila.fred',
        'tcp.jim.fred.sheila', 'udp.jim.fred.sheila',
        'tcp.jim.sheila.fred', 'udp.jim.sheila.fred',
        'tcp.fred.jim.sheila', 'udp.fred.jim.sheila',
        'tcp.fred.sheila.jim', 'udp.fred.sheila.jim',
        'tcp.sheila.jim.fred', 'udp.sheila.jim.fred',
        'tcp.sheila.fred.jim', 'udp.sheila.fred.jim'
    ]

    logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(levelname)-8s %(name)-19s %(message)s')

    if options.hostname:
        addr = (options.hostname, DEFAULT_TCP_LOGGING_PORT)
    else:
        addr = get_addr(options.tcphost, DEFAULT_TCP_LOGGING_PORT)
    h = SocketHandler(*addr)
    tcp_logger.addHandler(h)
    if options.hostname:
        addr = (options.hostname, DEFAULT_UDP_LOGGING_PORT)
    else:
        addr = get_addr(options.udphost, DEFAULT_UDP_LOGGING_PORT)
    h = DatagramHandler(*addr)
    udp_logger.addHandler(h)

    log_data = LogData(loggers)
    try:
        while True:
            try:
                if random.random() <= options.excprob:
                    doo_doo(log_data)
                else:
                    dest, level, msgno = log_data.what_to_log()
                    dest.log(level, 'Message no. %d', msgno)
            except Exception:
                dest, level, msgno = log_data.what_to_log()
                dest.exception('Exception message no. %d', msgno)
            if options.count and log_data.msgno >= options.count:
                break
            if options.delay:
                time.sleep(options.delay / 1000.0)
    except KeyboardInterrupt:
        pass

if __name__ == '__main__':
    main()