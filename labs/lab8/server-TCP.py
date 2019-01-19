# 1a. Implement using the socket module (TCP),
# a server that writes when a client connects to it the following data:
# the connection time in human-readable format, the address, and the port of the client.

import socket
import time

HOST = '127.0.0.1'
PORT = 1234

# Create a TCP/IP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

start = time.clock()

# Bind the socket to the port
server_socket.bind((HOST, PORT))

# Listen for incoming connections
server_socket.listen(1)

while True:
    # Wait for a connection
    (connection, address) = server_socket.accept()
    try:
        print("Connection time: ", time.clock() - start, ' seconds')
        print("Connected address: ", address[0])
        print("Client port: ", address[1])
    finally:
        # Clean up the connection
        connection.close()
        print("Server closed")


