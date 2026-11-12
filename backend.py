#!/usr/bin/env python3
from time import sleep
import subprocess
from adafruit_servokit import ServoKit

class Drawer_Servo:
    def __init__(self):
        # requires pigpiod to run properly
        kit = ServoKit(channels=16)
        self.servos = kit.servo
        self.closed = False
        for i in range(0, 15):
            self.close_drawer(i)

    def open_drawer(self, pin):
        if self.closed:
            self.servos[pin] = 180
            sleep(1)
            self.closed = False

    def close_drawer(self, pin):
        if not self.closed:
            self.servos[pin] = 0
            sleep(1)
            self.closed = True

    def toggle_drawer(self, pin):
        if self.closed:
            self.open_drawer(pin)
        elif not self.closed:
            self.close_drawer(pin)

    def move_servo(self, pin, val):
        self.servos[pin] = val
        sleep(1)

if __name__ == "__main__":
    commands = [
        ["source", "env/bin/activate"], # enter the right environment first
        ["sudo", "pigpiod"]
    ]

    for cmd in commands:
        result = subprocess.run(cmd, check=True, text=True, capture_output=True)
        print(result.stdout)

    left = Drawer_Servo(13)
    right = Drawer_Servo(12)

    left.close_drawer()
    right.close_drawer()

    left.open_drawer()
    right.open_drawer()