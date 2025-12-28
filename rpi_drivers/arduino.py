from smbus import SMBus
import time

class Arduino:
    def __init__(self, address=0x2f):
        self.addr = address # bus address
        self.bus = SMBus(1) # indicates /dev/ic2-1
        self.motorValue = False
        self.pumpValue = False

    def write(self):
        message = 0
        if self.motorValue == True and self.pumpValue == True:
            message = 3
        elif self.pumpValue == True and self.motorValue == False:
            message = 2
        elif self.motorValue == True and self.pumpValue == False:
            message = 1

        self.bus.write_byte(self.addr, message)

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
