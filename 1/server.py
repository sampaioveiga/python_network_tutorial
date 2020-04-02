import socket # network interface library
import sys # system parameters and functions libray

try:
    socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Create socket
except OSError as e:
    print('[-] Error: ' + str(e[0]) + ' - ' + e[1]) # print error
    sys.exit();

print('Sucess') # print success and exit