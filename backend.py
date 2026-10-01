#!/usr/bin/env python3
from gpiozero import Servo
from time import sleep
from gpiozero.pins.pigpio import PiGPIOFactory
import subprocess

class Drawer_Servo:
    def __init__(self, pwm_pin):
        # requires pigpiod to run properly
        factory = PiGPIOFactory()
        self.servo = Servo(pwm_pin, pin_factory=factory)
        self.close_drawer

    def open_drawer(self):
        if self.closed:
            self.servo.max()
            sleep(1)
            self.closed = False

    def close_drawer(self):
        if not self.closed:
            self.servo.min()
            sleep(1)
            self.closed = True

    def toggle_drawer(self):
        if self.closed:
            self.close_drawer
        if not self.closed:
            self.open_drawer

    def move_servo(self, val):
        self.servo.value = val
        sleep(1)

if __name__ == "__main__":
    s = subprocess.getstatusoutput('sudo pigpiod')
    if s[0] == 0:
        print(s[1])
    else:
        print('Error {}'.format(s[1]))

    left = Drawer_Servo(13)
    right = Drawer_Servo(12)

    left.close_drawer()
    right.close_drawer()

    left.open_drawer()
    right.open_drawer()