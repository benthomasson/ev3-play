#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Echo client program
import socket
import json
import psutil
import time

def send_message(s, msg_type, message_data):
    message = json.dumps([msg_type, message_data])
    length = len(message)
    s.sendall('{length:04x}'.format(length=length).encode())
    s.sendall(message.encode())

HOST = sys.argv[1]
PORT = int(sys.argv[2])
name = sys.argv[3]
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    send_message(s, 'Hello', dict(msg='Hello', name=name))
    send_message(s, 'Message', dict(msg='Hello world'))
    while True:
        battery = psutil.sensors_battery()
        send_message(s, 'Battery', dict(percent=battery.percent))
        time.sleep(1)
