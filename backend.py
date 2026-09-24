from gpiozero import Servo
from time import sleep
from gpiozero.pins.pigpio import PiGPIOFactory

class Drawer_Servo:
    def init(self, pwm_pin):
        # requires pigpiod to run properly
        factory = PiGPIOFactory()
        self.servo = Servo(pwm_pin, pin_factory=factory)

    def open_drawer():
        self.servo.max()
        sleep(1)

    def close_drawer():
        self.servo.min()
        sleep(1)

    def move_servo(val):
        self.servo.value = val
        sleep(1)