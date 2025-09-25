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

# anpassen, falls andere Sequenz
StepCount = 8
Seq = list(range(0, StepCount))
Seq[0] = [0,1,0,0]
Seq[1] = [0,1,0,1]
Seq[2] = [0,0,0,1]
Seq[3] = [1,0,0,1]
Seq[4] = [1,0,0,0]
Seq[5] = [1,0,1,0]
Seq[6] = [0,0,1,0]
Seq[7] = [0,1,1,0]

#GPIO.output(enable_pin, 1)

def setStep(w1, w2, w3, w4):
    line1.set_value(w1)
    line2.set_value(w2)
    line3.set_value(w3)
    line4.set_value(w4)
 
def forward(delay, steps):
    for i in range(steps):
        for j in range(StepCount):
            setStep(Seq[j][0], Seq[j][1], Seq[j][2], Seq[j][3])
            time.sleep(delay)
 
def backwards(delay, steps):
    for i in range(steps):
        for j in reversed(range(StepCount)):
            setStep(Seq[j][0], Seq[j][1], Seq[j][2], Seq[j][3])
            time.sleep(delay)

forward(0.05, 250)