import urllib
from urllib import request

url = 'http://localhost:8000/'

req = urllib.request.Request(url)
response = urllib.request.urlopen(req)
content = response.read().decode('utf-8')

print(content)
