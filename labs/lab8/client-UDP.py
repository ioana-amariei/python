# 2b. Implement a client for the deployed server at 2a: a script that receives
# from the command line an addr string, a port integer, and a string msg,
# and sends a UDP packet to the addr address, the port port, and the msg content.

import socket
import sys

if len(sys.argv) < 4:
    print('Please enter <address> <port> <message')
else:
    ADDRESS = sys.argv[1]
    PORT = int(sys.argv[2])
    MESSAGE = sys.argv[3:]

    content = ''
    for word in MESSAGE:
        content += ' ' + word

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    print(content.encode('UTF-8'))
    client_socket.sendto(content.encode('UTF-8'), (ADDRESS, PORT))

    client_socket.close()
