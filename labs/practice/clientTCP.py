# 1b. Implement a client for the deployed server at 1a: a script that receives from the command line a
# string addr and an integer port and connects through TCP to the addr address at the port port.
import socket
import sys

if len(sys.argv) < 3:
    raise Exception

else:
    HOST = sys.argv[1]
    PORT = int(sys.argv[2])

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))
