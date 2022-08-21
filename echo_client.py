#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Echo client program
import socket
import json

HOST = 'localhost'
PORT = 50007              # The same port as used by the server
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    message = json.dumps(['Message', dict(msg='Hello world')])
    length = len(message)
    s.sendall(f'{length:04x}'.encode())
    s.sendall(message.encode())
