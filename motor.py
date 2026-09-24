from gpiozero import Servo
from time import sleep
from gpiozero.pins.pigpio import PiGPIOFactory

factory = PiGPIOFactory()

servo = Servo(13, pin_factory=factory)

servo.min()
sleep(1)
servo.max()
sleep(1)