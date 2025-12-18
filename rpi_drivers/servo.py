import time
from adafruit_servokit import ServoKit

kit = ServoKit(channels = 16)

class Servo:
    def __init__(self, offset = 0):
        self.servo0 = 0 + offset
        self.servo1 = 1 + offset
        self.servo2 = 2 + offset
        self.servo3 = 3 + offset
        self.offset = offset

    def goto(self, value0, value1, value2, value3):
        kit.servo[self.servo0].angle = value0
        kit.servo[self.servo1].angle = value1
        kit.servo[self.servo2].angle = value2
        kit.servo[self.servo3].angle = value3

    def goto(self, servo, value):
        kit.servo[servo + self.offset].angle = value

    def reset(self):
        kit.servo[self.servo0].angle = 90
        kit.servo[self.servo1].angle = 90
        kit.servo[self.servo2].angle = 90
        kit.servo[self.servo3].angle = 90
