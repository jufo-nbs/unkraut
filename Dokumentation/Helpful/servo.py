# Warning: Make shure to run the "reset"-function for the pan-tilt-kit to work properly
# Warnung: Immer zuerst die "reset"-funktion aufrufen um eine Richtige funktionsweise sicherzustellen

import time
from adafruit_servokit import ServoKit

time.sleep(1)

kit = ServoKit(channels = 16)
kit.servo[0].angle = 45
print(1)
time.sleep(1)
kit.servo[0].angle = 135
print(2)
time.sleep(1)
kit.servo[0].angle = 90
print(3)
time.sleep(1)
kit.servo[1].angle = 180
print(1)
time.sleep(1)
kit.servo[1].angle = 135
print(2)
time.sleep(1)
kit.servo[1].angle = 90
print(3)
