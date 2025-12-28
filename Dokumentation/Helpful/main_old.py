import argparse
import rpi_drivers.arduino
import rpi_drivers.plantnet
import rpi_drivers.servo
# import rpi_drivers.gpio
from picamera2 import Picamera2
import io
import os
from PIL import Image
import time

# Console Arguments init
parser = argparse.ArgumentParser(prog = "main.py", 
                                 usage = "python main.py [-h]", 
                                 description = "Intended to run on a Raspberry Pi 5 with AI-HAT and AI-Camera. It detects harmful plants and destroys them.", 
                                 epilog = "Program written for the 'Jugend Forscht'-Competition by Niklas Keim", 
                                 formatter_class=argparse.ArgumentDefaultsHelpFormatter)

motor_drv = rpi_drivers.arduino.Arduino()

plantnet_drv = rpi_drivers.plantnet.PlantNet()

arm = rpi_drivers.servo.Servo()

# Start the Cam
picam2 = Picamera2()
picam2.start()
time.sleep(1)
while True:
    data = io.BytesIO()
    picam2.capture_file(data, format='jpeg')

    data.seek(0)
    img = Image.open(data).convert("RGB")
    w, h = img.size
    mx, my = w // 2, h // 2

    q1 = img.crop((0, 0, mx, my))       # top-left
    q2 = img.crop((mx, 0, w, my))       # top-right
    q3 = img.crop((0, my, mx, h))       # bottom-left
    q4 = img.crop((mx, my, w, h))       # bottom-right

    # Optionally store quadrants as in-memory JPEGs for further processing
    quadrants = []
    for q in (q1, q2, q3, q4):
        buf = io.BytesIO()
        q.save(buf, format='JPEG')
        buf.seek(0)
        quadrants.append(buf)
    
    output_dir = os.path.join(os.path.dirname(__file__), "captures")
    ts = int(time.time() * 1000)
    for i, q in enumerate((q1, q2, q3, q4), start=1):
        fn = os.path.join(output_dir, f"{ts}_q{i}.jpg")
        q.save(fn, format="JPEG")
    
    break