from picamera import PiCamera
from time import sleep
from datetime import datetime
import RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.IN)

camera=PiCamera()

def capture_image():
    camera.start_preview()

    now = datetime.now()
    current_datetime = now.strftime("%d-%m-%y_%H:%M:%S")
    filename = current_datetime + ".jpg"
    filepath = "/home/pi/nightCam/programs/tests/"

    camera.capture(filepath+filename)
    camera.stop_preview()

while True:
    i = GPIO.input(17)      #sensor sends 1 for motion, otherwise 0
    if i==1:
        print("----------- Motion Detected ----------")
        capture_image()
        sleep(10)
