#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Echo client program
import socket
import json
import time
import sys
from _thread import start_new_thread
import time

def main(argv):

    host = argv[0]
    port = int(argv[1])             # The same port as used by the server

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT, 1)
        s.bind((host, port))
        s.listen(1)
        while True:
            conn, addr = s.accept()
            with conn:
                while True:
                    print('conn.recv 4')
                    data = conn.recv(4)
                    print(data)
                    if not data: break
                    length = int(data, 16)
                    print('conn.recv ' + str(length))
                    data = conn.recv(length)
                    if not data: break
                    print(data)


if __name__ == "__main__":
    main(sys.argv[1:])

