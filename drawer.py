#!/usr/bin/env python3
from time import sleep
import subprocess
from adafruit_servokit import ServoKit

kit = ServoKit(channels=16) # Global kit for servos

def init_hat():
    """Ensure that pigpiod is running and set up hat"""
    s = subprocess.getstatusoutput('sudo pigpiod')
    if s[0] == 0:
        print(s[1])
    else:
        print('Error {}'.format(s[1]))

    for i in range(0, 15): # set all servos angle to 0
        kit.servo[i].angle = 0

def open_drawer(drawer_id):
    """Open selected drawer, then reverse after a short time"""
    kit.servo[drawer_id].angle = 180
    sleep(6)
    kit.servo[drawer_id].angle = 0
    sleep(1)
    



if __name__ == "__main__":

    init_hat()

    open_drawer(0)