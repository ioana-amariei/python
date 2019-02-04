# 1a. Implement using the socket module (TCP),
# a server that writes when a client connects to it the following data:
# the connection time in human-readable format, the address, and the port of the client.

import socket
import time

HOST = '127.0.0.1'
PORT = 1234

# Create a TCP/IP socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

start = time.time()

# Bind the socket to the port
s.bind((HOST, PORT))

# Listen for incoming connections
s.listen(1)

while True:
    # Wait for a connection
    (connection, address) = s.accept()
    try:
        current_time = time.time() - start
        print("Connection time: ", time.asctime(time.localtime(current_time)), ' seconds')
        print("Connected address: ", address[0])
        print("Client port: ", address[1])
    finally:
        # Clean up the connection
        connection.close()
        print("Server closed")
