#!/bin/bash
#sudo pkill -9 -f nightWatch.py     # is giving a 137 out of memoury exit code ?

nvCamStatus=$(</home/pi/nightCam/nvCamStatus.txt)
if [ $nvCamStatus != "status:capturing" ] 
then
	echo "Automated capturing is not running."
	echo $nvCamStatus
	echo "exiting status code:1"
	exit 1
fi

sudo pkill python3
exitCode1=$?
python3 /home/pi/nightCam/programs/cleanGPIOs.py
exitCode2=$?
if [ $exitCode1 -eq 0 -a $exitCode2 -eq 0 ] 
then
	echo "nvCam has stopped automated capturing"
       	echo "status:idle"
	echo "status:idle" > '/home/pi/nightCam/nvCamStatus.txt'
else
	echo "** could not stop automated capturing **"
	echo "status:error"
	echo "should reboot"
	echo "status:error" > '/home/pi/nightCam/nvCamStatus.txt'
fi
