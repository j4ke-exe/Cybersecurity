#!/bin/python3
#Usage: python3 scanner.py <ip>

import sys
import socket
from datetime import datetime as dt

#Define target
if len(sys.argv) == 2: #argv 1 = "scanner.py", argv 2 = "<ip>"
    target = socket.gethostbyname(sys.argv[1]) #translate hostname to IPv4
else:
    print("Invalid amount of arguments.")
    print("Syntax python3 scanner.py <ip>")

#Banner
print("-" * 50)
print("Scanning target: " + target)
print("Time started: " + str(dt.now()))
print("-" * 50)

try:
    for port in range(1, 2000):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = s.connect_ex((target, port)) #error indicator -- if port is open then return print statement
        if result == 0:
            print(f"Port {port} is open.")
        s.close()
        
except KeyboardInterrupt:
    print("\nExiting program.")
    sys.exit()

except socket.gaierror:
    print("\nHostname could not be resolved.")
    sys.exit()
    
except socket.error:
    print("\nCould not connect to the server.")
    sys.exit()
