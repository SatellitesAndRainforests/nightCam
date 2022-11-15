#!/bin/bash
nvCamStatus=$(</home/pi/nightCam/nvCamStatus.txt)
if [ $nvCamStatus == "status:idle" ] 
then
	echo "$nvCamStatus"
	echo "status is idle: starting live stream"
	sudo killall raspimjpeg
	sudo killall php
	sudo killall motion	
	sudo pkill python3
	sudo nohup python3 /home/pi/nightCam/programs/testLiveStream.py &
else 
	echo "nvCam is not idle"
	echo "$nvCamStatus"
	echo "exiting status code:1"
	exit 1
fi

