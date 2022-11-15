import requests
import glob

url = 'http://192.168.1.5:8080/captures/image-from-client'

for filepath in glob.iglob('/home/pi/nightCam/images/*.jpg'):
    files = {'image': open( filepath, 'rb')}
    requests.post(url, files=files)

