#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket
import json
import _thread
import time
import queue


HOST = ''                 # Symbolic name meaning all available interfaces
OUTPUT_PORT = 50008              # Arbitrary non-privileged port

q = queue.Queue()

def send_message(s, message):
    length = len(message)
    print('{length:04x}'.format(length=length).encode())
    print(message)
    s.sendall('{length:04x}'.format(length=length).encode())
    s.sendall(message)


def output_thread():

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, OUTPUT_PORT))
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
                    data = q.get()
                    print(data)
                    send_message(conn, data)


def main():
    q.put(json.dumps({"msg": "Hello"}).encode())
    while True:
        time.sleep(1)

if __name__ == "__main__":
    _thread.start_new_thread(output_thread, tuple())
    main()

