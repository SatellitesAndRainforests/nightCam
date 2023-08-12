import requests
import glob
import os

#url = 'http://192.168.1.23:8080/captures/image-from-client'
url = 'http://10.3.141.133:8080/captures/image-from-client'


def sendImages():
    for filepath in glob.iglob('/home/pi/nightCam/images/*.jpg'):
        files = {'image': open( filepath, 'rb')}
        response = requests.post(url, files=files)
        print(response.status_code)
        if (response.status_code == 200):
            print("sent successfully")
            print("deleting: " + filepath)
            os.system( "rm " + filepath )

def check_status_is_idle_or_exit():
    with open("/home/pi/nightCam/nvCamStatus.txt", "r") as status_file:
        status = status_file.readline().strip()
        print("status is: " + status)
        if (status != "status:idle"):
            print("nvCam is not idle")
            print("exiting sendAllImages.py")
            exit()

def write_status_to_file( status ):
    with open("/home/pi/nightCam/nvCamStatus.txt", "w") as status_file:
        print( status + "\n" )
        status_file.write( status + "\n" )



def main():

    check_status_is_idle_or_exit()
    write_status_to_file("status:sending")
    sendImages()
    write_status_to_file("status:idle")


main()

