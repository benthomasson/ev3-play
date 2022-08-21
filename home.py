#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket
import json

HOST = ''                 # Symbolic name meaning all available interfaces
PORT = 50007              # Arbitrary non-privileged port

def main():

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen(1)
        while True:
            conn, addr = s.accept()
            with conn:
                print('Connected by', addr)
                while True:
                    data = conn.recv(4)
                    if not data: break
                    length = int(data, 16)
                    data = conn.recv(length)
                    if not data: break
                    msg_type, msg_data = json.loads(data.decode())
                    print(msg_type, msg_data)


if __name__ == "__main__":
    main()

