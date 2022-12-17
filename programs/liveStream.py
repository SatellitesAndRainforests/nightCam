import RPi.GPIO as GPIO
import time
from sys import exit

import os

GPIO.setmode(GPIO.BCM)
GPIO.setup(21, GPIO.OUT)


def write_status_to_file( status ):
    with open("/home/pi/nightCam/nvCamStatus.txt", "w") as status_file:
        print( status + "\n" )
        status_file.write( status + "\n" )

def check_status_is_idle_or_exit():
    with open("/home/pi/nightCam/nvCamStatus.txt", "r") as status_file:
        status = status_file.readline().strip()
        print("status is: " + status)
        if (status != "status:idle"):
            print("nvCam is not idle")
            print("not starting live stream")
            exit()

def check_status_is_still_streaming_or_exit():
    with open("/home/pi/nightCam/nvCamStatus.txt", "r") as status_file:
        status = status_file.readline().strip()
        if (status != "status:streaming"):
            print("stopping livestream")
            print(" --- Turning OFF Light ---")
            GPIO.output(21, GPIO.LOW)
            exit()

def main():

    check_status_is_idle_or_exit()
    
    print("starting live stream")

    write_status_to_file("status:streaming")

    try:
        print(" --- Starting the live stream server --- ")
        os.system(' /home/pi/nightCam/programs/RPi_Cam_Web_Interface/start.sh ')
        print(" --- Turning ON Light ---")
        GPIO.output(21, GPIO.HIGH)

        while True:
            check_status_is_still_streaming_or_exit()
            time.sleep(1)
        
    except KeyboardInterrupt:
        print(" --- Keyboard Interrupt ---")
    except:
        print(" --- except ---")
    finally:
        print(" --- Finally ---")
        print(" --- Turning OFF Light (making sure) ---")
        GPIO.cleanup()
        print(" --- Stopping live stream server --- ")
        os.system(' /home/pi/nightCam/programs/RPi_Cam_Web_Interface/stop.sh ')
        print(" --- Setting status to idle --- ")
        write_status_to_file( "status:idle" )
        raise SystemExit(0)



main()

























