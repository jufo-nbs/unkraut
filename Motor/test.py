import gpiod
import time

# Constants
PIN1 = 6
PIN2 = 13
PIN3 = 19
PIN4 = 26

# GPIO setup
chip = gpiod.Chip('gpiochip4')

line1 = chip.get_line(PIN1)
line2 = chip.get_line(PIN2)
line3 = chip.get_line(PIN3)
line4 = chip.get_line(PIN4)

line1.request(consumer="PIN1", type=gpiod.LINE_REQ_DIR_OUT)
line2.request(consumer="PIN2", type=gpiod.LINE_REQ_DIR_OUT)
line3.request(consumer="PIN3", type=gpiod.LINE_REQ_DIR_OUT)
line4.request(consumer="PIN4", type=gpiod.LINE_REQ_DIR_OUT)

# Main code
try:
    for _ in range(25):
        line2.set_value(1)
        time.sleep(1)
        line2.set_value(0)
        line4.set_value(1)
        time.sleep(1)
        line4.set_value(0)
        line3.set_value(1)
        time.sleep(1)
        line3.set_value(0)
        line1.set_value(1)
        time.sleep(1)
        line1.set_value(0)
finally: 
    line1.set_value(0)
    line2.set_value(0)
    line3.set_value(0)
    line4.set_value(0)

    line1.release()
    line2.release()
    line3.release()
    line4.release()
