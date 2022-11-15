import RPi.GPIO as GPIO
import time
from picamera import PiCamera
from fractions import Fraction
import datetime

import os

GPIO.setmode(GPIO.BCM)
GPIO.setup(21, GPIO.OUT)

GPIO.output(21, GPIO.HIGH)

cameraCommand = ('raspistill '
'-awb greyworld '
# '-ss 40000 ' # 1/25 of a second had no motion blur at v close range with other smaller light.
'-ISO 400 '
'-o test.jpg' )

os.system( cameraCommand )

'''
camera = PiCamera(framerate=Fraction(1,6))
camera.shutter_speed = 1750000 
camera.iso = 800
awb_mode = 'greyworld'
#time.sleep(5)
camera.exposure_mode = 'off'
outfile = "/home/pi/testImages/1__" + "%s.jpg" % (stub)
camera.capture(outfile)
camera.close()
'''

GPIO.output(21, GPIO.LOW)

GPIO.cleanup()



























