from smbus import SMBus
import time

class Arduino:
    def __init__(self, address=0x2f):
        self.addr = address # bus address
        self.bus = SMBus(1) # indicates /dev/ic2-1
        self.motorValue = False
        self.pumpValue = False

    def write(self):
        message = 0x00
        if self.pumpValue == True:
            message = 0x10
        elif self.motorValue == True:
            message = 0x01
        elif self.motorValue == True and self.pumpValue == True:
            message = 0x11

        self.bus.write(self.addr, message)

    def motor(self, output: bool):
        self.motorValue = output
        self.write()

    def halt(self):
        self.motorValue = False
        self.pumpValue= False
        self.write()

    def pump(self, output: bool):
        self.pumpValue = output
        self.write()

    def drive_for(self, output:bool, duration_sec: int):
        self.motor(output)
        end_time = time.time() + duration_sec
        while time.time() < end_time:
            pass
        self.halt()