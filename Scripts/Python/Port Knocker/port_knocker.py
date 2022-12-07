# Import required libraries
import os
import sys
import ctypes
import socket
import threading
import subprocess
import numpy as np
from datetime import datetime as dt

# Define __main__
if __name__ == "__main__":
    pass

# Resize the terminal window for Mac OS
if os.name == "posix":
    subprocess.run(['resize', '-s', '50', '121'])

# Resize the terminal window for Windows
if os.name == "nt":
    # Windows
    os.system("mode con: cols=121 lines=50")

# Rename terminal window
ctypes.windll.kernel32.SetConsoleTitleW("Port Knocker v1.0.2")

# Define the banner
banner = """
 ______   ______     ______     ______      __  __     __   __     ______     ______     __  __     ______     ______    
/\  == \ /\  __ \   /\  == \   /\__  _\    /\ \/ /    /\ "-.\ \   /\  __ \   /\  ___\   /\ \/ /    /\  ___\   /\  == \   
\ \  _-/ \ \ \/\ \  \ \  __<   \/_/\ \/    \ \  _"-.  \ \ \-.  \  \ \ \/\ \  \ \ \____  \ \  _"-.  \ \  __\   \ \  __<   
 \ \_\    \ \_____\  \ \_\ \_\    \ \_\     \ \_\ \_\  \ \_\\"\_ \  \ \_____\  \ \_____\  \ \_\ \_\  \ \_____\  \ \_\ \_\ 
  \/_/     \/_____/   \/_/ /_/     \/_/      \/_/\/_/   \/_/ \/_/   \/_____/   \/_____/   \/_/\/_/   \/_____/   \/_/ /_/ 

                                                                                                                v1.0.2

                                                    Coded by: wayahlife
                                                https://github.com/wayahlife
"""

# Print the banner
print(banner)

# Format function
def el():
    print("-" * 120)

# Select an option
el(); print("Select an option: ")
print("1. Scan a single host")
print("2. Scan a subnet")
print("3. Exit\n")

# Get the user's option
try:
    option = int(input("Enter an option: "))
except ValueError:
    print("\nInvalid Input. Exiting Port Knocker.\n"); el()
    sys.exit()
except KeyboardInterrupt:
    print("\nKeyboard interrupt detected. Exiting Port Knocker.\n"); el()
    sys.exit()

# Handle the user's option
if option == 1:
    # Scan a single host
    try:
        el(); host = input(("Enter the host to knock: "))
        start_port, end_port = map(int, input("Enter the port range to knock (e.g. 1-65535): ").split("-"))
        start_time = dt.now().replace(microsecond=0)
        el(); print(f"Port Knocker is scanning {host}. " + "Date/Time of Scan: " + str(start_time) + "."); el()
    except ValueError:
        print("\nInvalid Input. Exiting Port Knocker.\n"); el()
        sys.exit()
    except KeyboardInterrupt:
        print("\nKeyboard interrupt detected. Exiting Port Knocker.\n"); el()
        sys.exit()
elif option == 2:
    # Scan a subnet
    try:
        el(); host = input(("Enter the subnet to knock (e.g. <IP>.0/24): "))
        start_port, end_port = map(int, input("Enter the port range to knock (e.g. 1-65535): ").split("-"))
        start_time = dt.now().replace(microsecond=0)
        el(); print(f"Port Knocker is scanning {host}. " + "Date/Time of Scan: " + str(start_time) + "."); el()
    except ValueError:
        print("\nInvalid Input. Exiting Port Knocker.\n"); el()
        sys.exit()
    except KeyboardInterrupt:
        print("\nKeyboard interrupt detected. Exiting Port Knocker.\n"); el()
        sys.exit()
else:
    # Exit the program
    print("\nExiting Port Knocker. Bye.\n")
    sys.exit()

# Define the port scanning function
def scan_port(host, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)
    result = sock.connect_ex((host, port))
    if result == 0:
        try:
            service = socket.getservbyport(port)
            print(f"-> Port {port} is open on {host} ({service})")
            with open("port_knocker_output.txt", "a") as f:
                f.write(f"-> Port {port} is open on {host} ({service})" + "\n")
                f.close()
        except OSError:
            print(f"-> Port {port} is open on {host} (unknown)")
            with open("port_knocker_output.txt", "a") as f:
                f.write(f"-> Port {port} is open on {host} (unknown)" + "\n")
                f.close()
    sock.close()

# Check if a subnet was entered
if ".0/24" in host:
    # Scan the subnet
    for i in range(1, 254):
        ip_address = host.replace(".0/24", "." + str(i))
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

# Output the results
el()
end_time = dt.now().replace(microsecond=0) - start_time
output = os.getcwd() + "\port_knocker_output.txt"
print(f"[+] DONE. Port Knocker has finished scanning {host}. Scan took {end_time} to complete.")
print(f"[+] Results were outputted to {output}.")

# Scan again
el(); print("Scan again? (y/n)")
scan_again = input("Enter an option: ")
if scan_again == "y" or scan_again == "Y":
    os.system("python3 port_knocker.py")
else:
    print("\nExiting Port Knocker. Bye."); el(); print("\n")
    sys.exit()
