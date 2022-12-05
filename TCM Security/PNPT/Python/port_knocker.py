# Import required libraries
import socket
import threading
import numpy as np
import sys

# Define the banner
banner = 
"""
 ______   ______     ______     ______      __  __     __   __     ______     ______     __  __     ______     ______    
/\  == \ /\  __ \   /\  == \   /\__  _\    /\ \/ /    /\ "-.\ \   /\  __ \   /\  ___\   /\ \/ /    /\  ___\   /\  == \   
\ \  _-/ \ \ \/\ \  \ \  __<   \/_/\ \/    \ \  _"-.  \ \ \-.  \  \ \ \/\ \  \ \ \____  \ \  _"-.  \ \  __\   \ \  __<   
 \ \_\    \ \_____\  \ \_\ \_\    \ \_\     \ \_\ \_\  \ \_\\"\_ \  \ \_____\  \ \_____\  \ \_\ \_\  \ \_____\  \ \_\ \_\ 
  \/_/     \/_____/   \/_/ /_/     \/_/      \/_/\/_/   \/_/ \/_/   \/_____/   \/_____/   \/_/\/_/   \/_____/   \/_/ /_/ 


                                                    Coded by: wayahlife
                                                https://github.com/wayahlife
"""

# Print the banner
print(banner)

# Get the host and port range from the user
try:
    host = input("Enter the host to knock: ")
    start_port, end_port = 1, 65535
    print("-" * 120)
    print(f"\nPort Knocker is scanning {host}...\n")
except (ValueError, KeyboardInterrupt):
    print("\nError. Exiting program.\n")
    sys.exit()

# Define the port scanning function
def scan_port(host, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)
    result = sock.connect_ex((host, port))
    if result == 0:
        try:
            service = socket.getservbyport(port)
            print(f"Port {port} is open on host {host} ({service}).")
        except OSError:
            print(f"Port {port} is open on host {host}.")
    sock.close()

# Check if a subnet was entered
if "/24" in host:
    # Scan the subnet
    for i in range(1, 255):
        ip_address = host.replace("/24", "." + str(i))
        threads = []
        # Use numpy and vectorization to create a list of port numbers to scan
        ports = np.arange(start_port, end_port+1)
        for port in ports:
            thread = threading.Thread(target=scan_port, args=(ip_address, port))
            thread.start()
            threads.append(thread)
        for thread in threads:
            thread.join()
else:
    # Scan the specified host
    threads = []
    # Use numpy and vectorization to create a list of port numbers to scan
    ports = np.arange(start_port, end_port+1)
    for port in ports:
        thread = threading.Thread(target=scan_port, args=(host, port))
        thread.start()
        threads.append(thread)
    for thread in threads:
        thread.join()

# Print a completion message
print("\nPort scan complete.\n")
