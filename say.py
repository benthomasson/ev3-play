#!/usr/bin/env python3
from ev3dev2.sound import Sound
from ev3dev2.motor import LargeMotor, OUTPUT_A, OUTPUT_B, SpeedPercent, MoveTank
from ev3dev2.sensor import INPUT_1
from ev3dev2.sensor.lego import TouchSensor
from ev3dev2.led import Leds


sound = Sound()
m = LargeMotor(OUTPUT_A)

while True:
    command = input('>')

    sound.speak(command)
    if command == "open":
        m.on_for_degrees(SpeedPercent(100), -90)
    if command == "chomp":
        m.on_for_degrees(SpeedPercent(100), 90)
        m.on_for_degrees(SpeedPercent(100), -90)
    if command == "bye":
        break
