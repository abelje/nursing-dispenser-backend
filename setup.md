# Raspberry Pi Zero Setup
## Soldering on the Pins
Solder on the Pins to the Raspberry Pi Uno board, take note of the orientation

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