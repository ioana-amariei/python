# 5. Write a script that receives a URL from the command line (as an argument) and downloads all images
# (img src) to the current directory.

# https://stackoverflow.com/questions/7243750/download-file-from-web-in-python-3

import urllib
import re
from urllib import request

URL = 'https://iampava.com/'
IMAGE_PATTERN = re.compile(b"<img[^>]+src=\"([^\">]+)")

try:
    response = urllib.request.urlopen(URL)
    html = response.read()
    images = re.findall(IMAGE_PATTERN, html)

    count = 1
    for image in images:
        image_src = image.decode("utf-8")
        image_url = URL + image_src
        image_file = 'file' + str(count) + '.jpg'
        f = open(image_file, 'wb')
        urllib.request.urlretrieve(image_url, image_file)
        f.close()
        count += 1

except Exception as e:
    print('Error -> ', e)
