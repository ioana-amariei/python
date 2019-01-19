# 6. Write a script that receives a URL from the command line (as argument) and writes the following information
# into a file: response status, response size, response type (if known),
# md5 hash for each fragment of maximum 1000 bytes of response and server response time.

import sys
import urllib
from urllib import request
import time
import hashlib


def compute_md5(my_string):
    m = hashlib.md5()
    m.update(my_string.encode('utf-8'))
    return m.hexdigest()


if len(sys.argv) < 2:
    print('Please enter website <URL>')
else:
    url = sys.argv[1]
    request = urllib.request.Request(url)
    response = urllib.request.urlopen(request)
    start = time.time()
    info = response.info()
    end = time.time()

    # TODO: write info to file
    content = response.read().decode('utf-8')
    print(content)

    print("Server response time: ", start - end, ' seconds')
    print("Response status code: ", response.getcode())
    print("Response size: ", info['Content-Length'])
    print("Response type: ", info['Content-type'])
    print("Method: ", request.get_method())

    length = len(content)
    offset = 0
    while length > 0:
        fragment = ''
        for i in range(offset, 1000):
            fragment += content[i]
        print("md5 hash: ", compute_md5(fragment))
        offset = 1000
        length -= offset
