# 1b. Implement a client for the deployed server at 1a: a script that receives from the command line a
# string addr and an integer port and connects through TCP to the addr address at the port port.

import sys
import socket

print(sys.argv)

if len(sys.argv) < 3:
    print("Please enter <address> and <port>")
else:
    HOST = sys.argv[1]
    PORT = int(sys.argv[2])

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))
