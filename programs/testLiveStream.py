import RPi.GPIO as GPIO
import time

import os

GPIO.setmode(GPIO.BCM)
GPIO.setup(21, GPIO.OUT)



def write_status_to_file( status ):
    with open("/home/pi/nightCam/nvCamStatus.txt", "w") as status_file:
        print( status + "\n" )
        status_file.write( status + "\n" )


def main():

    write_status_to_file("status:streaming")

    try:
        print(" --- Starting the live stream server --- ")
        print(" --- Streaming for 30 seconds --- ")
        print(" --- Auto Shutdown ---")
        os.system(' /home/pi/nightCam/programs/RPi_Cam_Web_Interface/start.sh ')
        print(" --- Turning ON Light ---")
        GPIO.output(21, GPIO.HIGH)

        for i in range(30, 0, -1):
            print (" --- Server and Light shutting down in      " + str(i) + "      --- ")
            time.sleep(1)
        
        print(" --- Turning OFF Light ---")
        GPIO.output(21, GPIO.LOW)
    
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

























