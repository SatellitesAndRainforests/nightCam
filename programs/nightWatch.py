import os
import Adafruit_DHT
import time
import board
import RPi.GPIO as GPIO
from picamera import PiCamera
from time import sleep
from datetime import datetime
from sys import exit

#GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
# pir
GPIO.setup(17, GPIO.IN)
# light
GPIO.setup(21, GPIO.OUT)
# dht22
DHT_SENSOR = Adafruit_DHT.DHT22
DHT_GPIO_PIN = 24

baseline_new_moon = datetime(2022, 2, 1)    # There was a new moon on this date at 00:46am.

def check_status_is_idle_or_exit():
    with open("/home/pi/nightCam/nvCamStatus.txt", "r") as status_file:
        status = status_file.readline().strip()
        print("status is: " + status)
        if (status != "status:idle"):
            print("nvCam is not idle")
            print("exiting nightWatch.py")
            exit()

def write_to_log( message ):
    with open("/home/pi/nightCam/log.txt", "a") as log_file:
        print( message + "\n" )
        log_file.write( message + "\n" )


def write_status_to_file( status ):
    with open("/home/pi/nightCam/nvCamStatus.txt", "w") as status_file:
        print( status + "\n" )
        status_file.write( status + "\n" )


def capture_image():

    write_to_log(" --- light on --- ")
    GPIO.output(21, GPIO.HIGH)
    
    write_to_log(" --- taking photo --- ")
    cameraCommand = ('raspistill '
            #'-ss 750000 '  #3/4 of a second - fastest best image with motion blur.
            # '-ss 40000 '   #1/25 of a second (very little motion blur at a very close range ~30cm).
            # '-ss 40000 '   #1/25 [New Light] iso 800 grany, dark. little motion blur. try a little longer.
             '-ss 80000 '   #2/25 [New Light] iso 800 grany, dark. little motion blur. try a little longer.
            #'-ss 250000 '   #1/4 of a second (complete background, some motion blur ~2meters) 
                                #Can get some OK images at every distance with the background.
            #'-ss 100000 '  #1/10 of a second (almost no background, motion blur ~2meters).
            #'-ss 150000 '  #1/15  too blury.
            #'-ss 200000 '  #1/20  blurry
            '-ISO 400 '
            '-awb greyworld '
            '--sharpness 100 '
            '--quality 100 '
            '-o /home/pi/nightCam/images/temp/temp.jpg')
    os.system( cameraCommand )
    
    write_to_log(" --- light off --- ")
    GPIO.output(21, GPIO.LOW)




def calc_moon_phase():

    now = datetime.now()
    difference = float((now - baseline_new_moon).days) - 0.0319 # Days since baseline new-moon as a float + 46 mins.
                                                                # subtract 46 mins, 3.19% of a day to give whole-days.
    modulos = difference % 29.53    # Subtract all full moon cycles, (29.53 days, Wikipedia)
                                    # remander is the current mooncycle's progress/ phase.
    moonphase = ""

    if (modulos < 1.84 or modulos >= 27.68 ):       # The new-moon will be really noticable if wrong
        # currently ~ +/- 19 hour variation either way.  
        moonphase = "newMoon"                      # Each phase is 29.53 / 8 (for the 8 phases) with the new-moon center = 0

    elif (modulos >= 1.84 and modulos < 5.53):
        moonphase = "cresent_right_"

    elif (modulos >= 5.53 and modulos < 9.22):
        moonphase = "halfMoon_right_"

    elif (modulos >= 9.22 and modulos < 12.91):
        moonphase = "3of4moon_right_"

    elif (modulos >= 12.91 and modulos < 16.61):
        moonphase = "fullMoon"

    elif (modulos >= 16.61 and modulos < 20.30):
        moonphase = "3of4moon_left_"

    elif (modulos >= 20.30 and modulos < 23.99):
        moonphase = "halfMoon_left_" 

    elif (modulos >= 23.99 and modulos < 27.68):
        moonphase = "cresent_left_"

    return moonphase




def add_information_to_filename():

    filename_sensor_data="sensorError"
    file_ext=".jpg"

    moon_phase = calc_moon_phase()

    current_datetime = datetime.now().strftime("%H:%M:%Ss__%d:%m:%Y__")

    for i in range(3):
        try:

            humidity, temperature = Adafruit_DHT.read_retry( DHT_SENSOR, DHT_GPIO_PIN )
            filename_sensor_data = "{:.1f}c__{:.1f}h".format(temperature, humidity)
            write_to_log( "Temp: {:.1f} C    Humidity: {:.1f}% ".format(temperature, humidity))
            break

        except RuntimeError as error:
            # dht errors are common 
            write_to_log(" --- dht error: attempt 1 of 3 --- ")
            write_to_log(error.args[0])
            time.sleep(0.4)
            continue

    new_filename = current_datetime + filename_sensor_data + "__" + moon_phase + file_ext
    old_name=r"/home/pi/nightCam/images/temp/temp.jpg"
    new_name=r"/home/pi/nightCam/images/" + new_filename
    os.rename(old_name, new_name)
    write_to_log (" --- image saved --- " + new_filename)


def check_status_is_still_capturing_or_exit():
    with open("/home/pi/nightCam/nvCamStatus.txt", "r") as status_file:
        status = status_file.readline().strip()
        if (status != "status:capturing"):
            print("exiting nightWatch.py")
            exit()


def main():

    check_status_is_idle_or_exit()
    write_status_to_file("status:capturing")

    try:
        while True:
            check_status_is_still_capturing_or_exit()
            i = GPIO.input(17)      # sensor sends 1 for motion, otherwise 0
            if i==1:
                write_to_log(" --- Motion Detected --- ")
                capture_image()
                add_information_to_filename()
                sleep(1)

    except KeyboardInterrupt:
        write_to_log(" --- Keyboard Interrupt --- ")
    except:
        write_to_log(" --- except --- ")
    finally:
        write_to_log(" --- GPIO cleanup ---")
        GPIO.cleanup()
        write_to_log(" --- Finally ---")
        write_status_to_file("status:idle")
        raise SystemExit(0)



main()
















