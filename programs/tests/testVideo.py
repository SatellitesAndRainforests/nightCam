import RPi.GPIO as GPIO
import os
import time

import datetime
#from picamera import PiCamera

#camera = PiCamera()

stub = datetime.datetime.now().strftime("%Y%m%d%H%M%S")

GPIO.setmode(GPIO.BCM)
GPIO.setup(21, GPIO.OUT)
GPIO.output(21, GPIO.HIGH)

testCommand = ('raspivid -w 1280 -h 720 --sharpness 100 -fps 25 -b 20000000 -pf high -ISO 800 -awb greyworld -o /home/pi/testImages/video/testCommandiso800.h264')


os.system( testCommand )


GPIO.output(21, GPIO.LOW)

GPIO.cleanup()



























