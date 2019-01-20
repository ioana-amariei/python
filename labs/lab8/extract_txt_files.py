# 4. Once the server from 3 is started, extract the .txt file names and write to the console.


import urllib
from urllib import request
import re

url = 'http://localhost:8000/'
TXT_PATTERN = re.compile(b"<a[^>]+href=\"([^\">]+)")

try:
    req = urllib.request.Request(url)
    response = urllib.request.urlopen(req)
    page_content = response.read()

    txt_files = re.findall(TXT_PATTERN, page_content)

    for element in txt_files:
        file = element.decode('utf-8')
        if file.endswith('.txt'):
            print(file)
except Exception as e:
    print('Error -> ', e)
