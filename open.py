#!/usr/bin/env micropython
from ev3dev2.motor import LargeMotor, OUTPUT_A, OUTPUT_B, SpeedPercent, MoveTank
from ev3dev2.sensor import INPUT_1
from ev3dev2.sensor.lego import TouchSensor
from ev3dev2.led import Leds



m = LargeMotor(OUTPUT_A)
m.on_for_degrees(SpeedPercent(100), -90)
