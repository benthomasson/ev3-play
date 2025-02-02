#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Echo client program
import socket
import json
import time
import sys
from _thread import start_new_thread
import time

def send_message(s, msg_type, message_data):
    message = json.dumps([msg_type, message_data])
    length = len(message)
    s.sendall('{length:04x}'.format(length=length).encode())
    s.sendall(message.encode())


def main(argv):

    host = argv[0]
    port = int(argv[1])             # The same port as used by the server
    name = argv[2]

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    send_message(s, 'Hello', dict(msg='Hello', name=name))

    while True:
        print('s.recv 4')
        data = s.recv(4)
        print(data)
        if not data: break
        length = int(data, 16)
        print('s.recv ' + str(length))
        data = s.recv(length)
        if not data: break
        print(data)


if __name__ == "__main__":
    main(sys.argv[1:])

