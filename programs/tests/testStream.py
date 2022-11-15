import RPi.GPIO as GPIO
import os
import time
import datetime

GPIO.setmode(GPIO.BCM)
GPIO.setup(21, GPIO.OUT)
GPIO.output(21, GPIO.HIGH)

testCommand = ('raspivid -ISO 100      -t 0 -l -awb greyworld -o tcp://0.0.0.0:3333')

# with     vlc tcp/h264://192.168.1.13:3333



os.system( testCommand )


GPIO.output(21, GPIO.LOW)

GPIO.cleanup()



























