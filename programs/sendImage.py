import requests
url = 'http://192.168.1.5:8080/captures/image-from-client'
image = '11:23:05s__16:09:2022__18.4__71.1__3of4moon_left.jpg'

files = {'image': open( image, 'rb')}
requests.post(url, files=files)

