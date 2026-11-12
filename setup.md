# Raspberry Pi Zero Setup
## Soldering on the Pins
Solder on the Pins to the Raspberry Pi Zero board, take note of the orientation

## Installing the OS
[https://www.raspberrypi.com/software/](https://www.raspberrypi.com/software/)
- Download Raspberry Pi imager and go through the setup process on the sd card

## Interfacing with GPIO Pins
This website has the pinout for a raspberry pi zero here: (https://pinout.xyz/)[https://pinout.xyz/]

### Dev environment Setup
[https://gpiozero.readthedocs.io/en/stable/installing.html](https://gpiozero.readthedocs.io/en/stable/installing.html)

1. On fedora, use ```pip install gpiozero``` to install the main environment to interface with the raspberry pi zero.
2. Pigpio requires python3-pigpio and pigpiod to be installed. It is used to stop stuttering in the motor.

3. Build pigpio daemon from the github repository (it is not in the apt repository for whatever reason):

    ```
    git clone https://github.com/joan2937/pigpio
    cd pigpio
    make
    sudo make install
    sudo ldconfig
    ```
3. Run pigpio using ```sudo pigpiod```

## Create Desktop Shortcut for Python Script
[https://stackoverflow.com/questions/28158353/click-desktop-icon-to-execute-python-script-in-raspbian](https://stackoverflow.com/questions/28158353/click-desktop-icon-to-execute-python-script-in-raspbian)

[https://forums.raspberrypi.com/viewtopic.php?t=73529](https://forums.raspberrypi.com/viewtopic.php?t=73529)

[run terminal commands in python](https://stackoverflow.com/questions/3730964/python-script-execute-commands-in-terminal)
1. Add ```#!/usr/bin/env python3``` to the top of the script being used.
2. Create an executable using ```chmod +x /path/script.py```
3. Create text file on desktop, naming it with the ```.desktop``` filetype.
4. Open the file in a text editor and edit the config in this style:

    ```
    [Desktop Entry]
    Name[en_GB]=program.desktop
    Exec=python3 /path/p.py
    Icon[en_US]=/path/icon.png
    Type=Application
    Categories=Programming
    Terminal=false
    ```

## Adafruit Hat
https://learn.adafruit.com/adafruit-16-channel-pwm-servo-hat-for-raspberry-pi/using-the-python-library

The hat we got for this research requires a circuit python library to work. Blinka needs to be installed to serve as a interface layer for the Raspberry Pi.

### Installing Blinka
https://learn.adafruit.com/circuitpython-on-raspberrypi-linux/installing-circuitpython-on-raspberry-pi

1. Follow the tutorial
    - source env/bin/activate is required to start the virtual environment
    - TODO: set up the virtual environment to autorun if necessary
    - There is a nice install script that it will tell you to run

2. It will prompt a Reboot

### Installing the necessary library
1. Activate the virtual environment: source env/bin/activate
2. https://learn.adafruit.com/adafruit-16-channel-pwm-servo-hat-for-raspberry-pi/using-the-python-library
3. pip3 install adafruit-circuitpython-servokit
4. The virtual environment is required to be activated before running a python script with the Servo Hat.