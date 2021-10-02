#!/usr/bin/env micropython
from ev3dev2.sound import Sound


with open('/sys/class/power_supply/lego-ev3-battery/voltage_now') as f:
    voltage = int(f.read())
    voltage = voltage / 1000000

sound = Sound()

sound.speak('Battery voltage %.2f' % voltage)
