import arduino as arduino
# import plantnet
# import gpio
# import servo
from time import sleep

# TODO: Write a test for all modules used in the main Programm

arduino_drv = arduino.Arduino()

print(1)
arduino_drv.motor(True)
sleep(1)
print(2)
arduino_drv.pump(True)
sleep(1)
print(3)
arduino_drv.motor(False)
sleep(1)
print(4)
arduino_drv.motor(True)
sleep(1)
print(5)
arduino_drv.pump(False)
sleep(1)
print(6)
arduino_drv.pump(True)
sleep(1)
print(7)
arduino_drv.halt()
print(8)
