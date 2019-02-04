# 3. Start a server to expose the files and directories in the current directory.
# Access that server from a browser, and then using a python HTTP client (urllib.request)

import http.server
import socketserver

HOST = '127.0.0.1'
PORT = 8000

Handler = http.server.SimpleHTTPRequestHandler

httpd = socketserver.TCPServer((HOST, PORT), Handler)
print("serving at port", PORT)
httpd.serve_forever()
