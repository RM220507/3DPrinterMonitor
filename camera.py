import time, os, glob
from picamera import PiCamera

for f in glob.glob("Images/*.jpg"):
    os.remove(f)

camera = PiCamera()
camera.resolution = (1024, 768)

time.sleep(2)

while True:
    camera.capture("Images/latest.jpg")
    camera.capture(f"{time.time()}.jpg")
    time.sleep(30)
