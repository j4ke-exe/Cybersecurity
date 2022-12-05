# Import required libraries
import socket
import threading
import sys

# Define the banner
banner = """
 ______   ______     ______     ______      __  __     __   __     ______     ______     __  __     ______     ______    
/\  == \ /\  __ \   /\  == \   /\__  _\    /\ \/ /    /\ "-.\ \   /\  __ \   /\  ___\   /\ \/ /    /\  ___\   /\  == \   
\ \  _-/ \ \ \/\ \  \ \  __<   \/_/\ \/    \ \  _"-.  \ \ \-.  \  \ \ \/\ \  \ \ \____  \ \  _"-.  \ \  __\   \ \  __<   
 \ \_\    \ \_____\  \ \_\ \_\    \ \_\     \ \_\ \_\  \ \_\\"\_\   \ \_____\  \ \_____\  \ \_\ \_\  \ \_____\  \ \_\ \_\ 
  \/_/     \/_____/   \/_/ /_/     \/_/      \/_/\/_/   \/_/ \/_/   \/_____/   \/_____/   \/_/\/_/   \/_____/   \/_/ /_/ 


Coded by: wayahlife
https://github.com/wayahlife
"""

# Print the banner
print("-" * 120)
print(banner)
print("-" * 120)

# Get the host and port range from the user
try:
    host = input("Enter the host address to scan: ")
    start_port, end_port = map(int, input("Enter the port range to scan (e.g. 1-65535): ").split("-"))
except (ValueError, KeyboardInterrupt):
    print("Exiting.")
    sys.exit()

# Define the port scanning function
def scan_port(host, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)
    result = sock.connect_ex((host, port))
    if result == 0:
        try:
            service = socket.getservbyport(port)
            print("Port {} is open ({})".format(port, service))
        except OSError:
            print("Port {} is open".format(port))
    sock.close()

# Scan the ports
threads = []
for port in range(start_port, end_port+1):
    thread = threading.Thread(target=scan_port, args=(host, port))
    thread.start()
    threads.append(thread)

# Wait for all threads to complete
for thread in threads:
    thread.join()

# Print a completion message
print("Port scan complete.")
