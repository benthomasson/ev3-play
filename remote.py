#!/usr/bin/env python3
from ev3dev2.sound import Sound
from ev3dev2.motor import LargeMotor, OUTPUT_A, OUTPUT_B, SpeedPercent, MoveTank
from ev3dev2.sensor import INPUT_1, INPUT_2
from ev3dev2.sensor.lego import TouchSensor
from ev3dev2.led import Leds
from _thread import start_new_thread
import time


sound = Sound()
right_button =  TouchSensor(INPUT_1)
left_button =  TouchSensor(INPUT_2)
my_leds = Leds()


current_music = None
cop = ("-f 659 -l 460 -n -f 784 -l 340 -n -f 659 -l 230 -n -f 659 -l 110 -n -f 880 -l 230 -n -f 659 -l 230 -n -f 587 -l 230 -n -f 659 -l 460 -n -f 988 -l 340 -n -f 659 -l 230 -n -f 659 -l 110 -n -f 1047 -l 230 -n -f 988 -l 230 -n -f 784 -l 230 -n -f 659 -l 230 -n -f 988 -l 230 -n -f 1318 -l 230 -n -f 659 -l 110 -n -f 587 -l 230 -n -f 587 -l 110 -n -f 494 -l 230 -n -f 740 -l 230 -n -f 659 -l 460")
tetris = "-f 330 -l 150 -n -f 1 -l 40 -n -f 494 -l 159 -n -f 1 -l 40 -n -f 660 -l 150 -n -f 1 -l 40 -n -f 590 -l 150 -n -f 660 -l 150 -n -f 494 -l 100 -n -f 494 -l 100 -n -f 523 -l 150 -n -f 1 -l 40 -n -f 440 -l 150 -n -f 1 -l 40 -n -f 494 -l 150 -n -f 1 -l 40 -n -f 392 -l 100 -n -f 392 -l 100 -n -f 440 -l 150 -n -f 370 -l 150 -n -f 1 -l 40 -n -f 392 -l 150 -n -f 1 -l 40 -n -f 330 -l 100 -n -f 330 -l 100 -n -f 370 -l 150 -n -f 1 -l 40 -n -f 294 -l 150 -n -f 1 -l 40 -n -f 330 -l 150 -n -f 247 -l 100 -n -f 247 -l 100 -n -f 261 -l 150 -n -f 1 -l 40 -n -f 311 -l 150 -n -f 1 -l 40 -n -f 330 -l 150 -n -f 1 -l 40 -n -f 247 -l 100 -n -f 247 -l 100 -n -f 262 -l 150 -n -f 1 -l 40 -n -f 370 -l 150 -n -f 1 -l 40 -n -f 330 -l 150 -n -f 1 -l 40 -n -f 494 -l 159 -n -f 1 -l 40 -n -f 660 -l 150 -n -f 1 -l 40 -n -f 590 -l 150 -n -f 660 -l 150 -n -f 494 -l 100 -n -f 494 -l 100 -n -f 523 -l 150 -n -f 1 -l 40 -n -f 440 -l 150 -n -f 1 -l 40 -n -f 494 -l 150 -n -f 1 -l 40 -n -f 392 -l 100 -n -f 392 -l 100 -n -f 440 -l 150 -n -f 370 -l 150 -n -f 1 -l 40 -n -f 392 -l 150 -n -f 1 -l 40 -n -f 330 -l 100 -n -f 330 -l 100 -n -f 370 -l 150 -n -f 1 -l 40 -n -f 294 -l 150 -n -f 1 -l 40 -n -f 330 -l 150 -n -f 247 -l 100 -n -f 247 -l 100 -n -f 261 -l 150 -n -f 1 -l 40 -n -f 311 -l 150 -n -f 1 -l 40 -n -f 330 -l 150 -n -f 1 -l 40 -n -f 247 -l 100 -n -f 247 -l 100 -n -f 262 -l 150 -n -f 1 -l 40 -n -f 370 -l 150 -n -f 1 -l 40 -n -f 330 -l 150 -n -f 1 -l 40"

def music():
    while True:
        if current_music:
            sound.beep(current_music)
        else:
            time.sleep(1)
            


start_new_thread(music, [])

while True:
    if right_button.is_pressed:
        my_leds.set_color('RIGHT', 'RED')
        current_music = cop
    else:
        my_leds.set_color('RIGHT', 'GREEN')
    if left_button.is_pressed:
        my_leds.set_color('LEFT', 'RED')
        current_music = tetris
    else:
        my_leds.set_color('LEFT', 'GREEN')
    if not left_button.is_pressed and not left_button.is_pressed:
        current_music = None
    print('.')



