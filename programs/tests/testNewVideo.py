import os


#testCommand = ('raspivid -w 1280 -h 720 --sharpness 100 -fps 25 -b 20000000 -pf high -ISO 800 -awb greyworld -o /home/pi/testImages/video/testCommandiso800.h264')

testCommand = ('raspivid -o /home/pi/nightCam/videos/testVideo.h264 -w 1280 -h 720 -awb greyworld -ISO 800 --sharpness 100 -t 10000') 

os.system( testCommand )




















