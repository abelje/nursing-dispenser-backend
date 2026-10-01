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