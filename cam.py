from picamera import PiCamera
from time import sleep
import os

upload = "./test.sh"

camera = PiCamera()
camera.start_preview()
sleep(5)
camera.capture('/home/pi/Bilder/picture.jpg')
camera.stop_preview()

os.system(upload)
