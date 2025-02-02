#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket
import json
import _thread
import time
import queue
import sys


HOST = '0.0.0.0'                 # Symbolic name meaning all available interfaces

q = queue.Queue()

def send_message(s, message):
    length = len(message)
    print('{length:04x}'.format(length=length).encode())
    print(message)
    s.sendall('{length:04x}'.format(length=length).encode())
    s.sendall(message)


def output_thread(host, port):

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT, 1)
        s.bind((host, port))
        s.listen(1)
        while True:
            conn, addr = s.accept()
            with conn:
                print('Output connected by', addr)
                while True:
                    print('conn.recv 4')
                    data = conn.recv(4)
                    if not data: break
                    length = int(data, 16)
                    print('conn.recv ' + str(length))
                    data = conn.recv(length)
                    if not data: break
                    msg_type, msg_data = json.loads(data.decode())
                    print(msg_type, msg_data)
                    break
                while True:
                    print('Waiting for data')
                    data = q.get()
                    print(data)
                    send_message(conn, data)


def main():
    q.put(json.dumps({"msg": "Hello"}).encode())
    while True:
        time.sleep(1)

if __name__ == "__main__":
    host = sys.argv[1]
    port = int(sys.argv[2])
    _thread.start_new_thread(output_thread, (host, port))
    main()

