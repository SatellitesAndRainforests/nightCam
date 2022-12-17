from time import sleep
from datetime import datetime
import RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.IN)


count = 0

while True:
    i = GPIO.input(17)      #sensor sends 1 for motion, otherwise 0
    if i==1:
        print("----------- Motion Detected ----------")
        print(count)
        count += 1
        sleep(0.7)
