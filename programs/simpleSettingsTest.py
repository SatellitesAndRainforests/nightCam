import os
import time
import board
import RPi.GPIO as GPIO
from picamera import PiCamera

#GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
# light
GPIO.setup(21, GPIO.OUT)

def takePhotos():

    print("light on")
    GPIO.output(21, GPIO.HIGH)
    
   
    print(" --- taking photo2 --- ")
    photo2 = (  'raspistill -ss 40000 -ISO 400 -awb greyworld --sharpness 100 --quality 100 '
                '-o /home/pi/nightCam/images/temp/ss40000iso400.jpg')
    os.system( photo2 )
    print(" --- photo2 saved --- ")

    print(" --- taking photo3 --- ")
    photo3 = (  'raspistill -ss 40000 -ISO 800 -awb greyworld --sharpness 100 --quality 100 '
                '-o /home/pi/nightCam/images/temp/ss40000iso800.jpg')
    os.system( photo3 )
    print(" --- photo3 saved --- ")

    print(" --- taking photo4 --- ")
    photo4 = (  'raspistill -ss 80000 -ISO 400 -awb greyworld --sharpness 100 --quality 100 '
                '-o /home/pi/nightCam/images/temp/ss80000iso400.jpg')
    os.system( photo4 )
    print(" --- photo4 saved --- ")

    print(" --- taking photo5 --- ")
    photo5 = (  'raspistill -ss 80000 -ISO 800 -awb greyworld --sharpness 100 --quality 100 '
                '-o /home/pi/nightCam/images/temp/ss80000iso800.jpg')
    os.system( photo5 )
    print(" --- photo5 saved --- ")

    print(" --- taking photo0 --- ")
    photo0 = (  'raspistill -ss 750000 -ISO 800 -awb greyworld --sharpness 100 --quality 100 '
                '-o /home/pi/nightCam/images/temp/ss750000iso800.jpg')
    os.system( photo0 )
    print(" --- photo0 saved --- ")

    print(" --- taking photo1 --- ")
    photo1 = (  'raspistill -ss 750000 -ISO 400 -awb greyworld --sharpness 100 --quality 100 '
                '-o /home/pi/nightCam/images/temp/ss750000iso400.jpg')
    os.system( photo1 )
    print(" --- photo1 saved --- ")
 
    print(" --- taking photoA --- ")
    photoA = (  'raspistill -ss 250000 -ISO 400 -awb greyworld --sharpness 100 --quality 100 '
                '-o /home/pi/nightCam/images/temp/ss250000iso400.jpg')
    os.system( photoA )
    print(" --- photoA saved --- ")
 
    print(" --- taking photoB --- ")
    photoB = (  'raspistill -ss 250000 -ISO 800 -awb greyworld --sharpness 100 --quality 100 '
                '-o /home/pi/nightCam/images/temp/ss250000iso800.jpg')
    os.system( photoB )
    print(" --- photoB saved --- ")
 

    print(" --- light off --- ")
    GPIO.output(21, GPIO.LOW)
    print("settingsTest.py -- complete --")
    


takePhotos()
















