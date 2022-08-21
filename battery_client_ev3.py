#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Echo client program
import socket
import json
import time

def send_message(s, msg_type, message_data):
    message = json.dumps([msg_type, message_data])
    length = len(message)
    s.sendall('{length:04x}'.format(length=length).encode())
    s.sendall(message.encode())

def get_battery():
    with open('/sys/class/power_supply/lego-ev3-battery/voltage_now') as f:
        voltage = int(f.read())
        voltage = voltage / 1000000
        return voltage


HOST = 'monitor'
PORT = 50007              # The same port as used by the server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
send_message(s, 'Message', dict(msg='Hello world ev3'))
send_message(s, 'Battery', dict(level=get_battery()))
