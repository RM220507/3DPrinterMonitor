from time import sleep
from os import remove
from glob import glob
from datetime import datetime
from picamera import PiCamera

for f in glob("Images/*.jpg"):
    remove(f)

camera = PiCamera()
camera.resolution = (1024, 768)

sleep(2)

while True:
    print("Taking Image")
    current_time = datetime.now().strftime("%d-%m-%Y %H-%M-%S")
    camera.capture(f"Images/{current_time}.jpg")
    sleep(30)
