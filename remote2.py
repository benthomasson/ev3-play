#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Echo client program
import socket
import json
import time
import sys
from ev3dev2.sound import Sound
from ev3dev2.motor import LargeMotor, OUTPUT_A, OUTPUT_B, SpeedPercent, MoveTank
from ev3dev2.sensor import INPUT_1, INPUT_2
from ev3dev2.sensor.lego import TouchSensor
from ev3dev2.led import Leds
from _thread import start_new_thread
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


def main(argv):

    host = argv[0]
    port = int(argv[1])             # The same port as used by the server
    name = argv[2]


    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    send_message(s, 'Hello', dict(msg='Hello', name=name))
    send_message(s, 'Battery', dict(level=get_battery()))

    right_button =  TouchSensor(INPUT_1)
    left_button =  TouchSensor(INPUT_2)
    right_stick = LargeMotor(OUTPUT_A)
    left_stick = LargeMotor(OUTPUT_B)
    right_stick.stop_action = 'coast'
    left_stick.stop_action = 'coast'

    while True:
        send_message(s, 'Data', dict(right_button=right_button.is_pressed,
                                     left_button=left_button.is_pressed,
                                     right_stick=right_stick.position,
                                     left_stick=left_stick.position))
        time.sleep(0.1)


if __name__ == "__main__":
    main(sys.argv[1:])
