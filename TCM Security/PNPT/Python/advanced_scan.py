# python3 advanced_scan.py -t example.com -p 1-1024 -n 10

import socket
import argparse
import threading

# Define a banner to display when the script is run
banner = """
  ____  _    _ _____ _   _ _____ ____ _____ _   _ _____ ____  
 / ___|| |  | | ____| \ | | ____|  _ \_   _| | | | ____|  _ \ 
 \___ \| |  | |  _| |  \| |  _| | |_) || | | | | |  _| | | | |
  ___) | |__| | |___| |\  | |___|  _ < | | | |_| | |___| |_| |
 |____/ \____/|_____|_| \_|_____|_| \_\|_|  \___/|_____|____/ 
                                                                
"""

# Create a parser object to handle command line arguments
parser = argparse.ArgumentParser()

# Add an argument for the target host
parser.add_argument("-t", "--target", help="Target host to scan")

# Add an argument for the range of ports to scan
parser.add_argument("-p", "--portrange", help="Range of ports to scan (e.g. 1-1024)")

# Add an argument for the number of threads to use
parser.add_argument("-n", "--numthreads", help="Number of threads to use")

# Add an argument for the timeout duration
parser.add_argument("-T", "--timeout", help="Timeout duration (in seconds)")

# Parse the command line arguments
args = parser.parse_args()

# Print the banner
print(banner)

# Prompt the user for the target host, if not specified on the command line
if args.target is None:
    host = input("Enter the target host: ")
else:
    host = args.target

# Prompt the user for the port range, if not specified on the command line
if args.portrange is None:
    port_range = input("Enter the port range (e.g. 1-1024): ")
else:
    port_range = args.portrange

# Split the port range into a start and end port
start_port, end_port = map(int, port_range.split("-"))

# Prompt the user for the number of threads to use, if not specified on the command line
if args.numthreads is None:
    num_threads = int(input("Enter the number of threads to use: "))
else:
    num_threads = int(args.numthreads)

# Prompt the user for the timeout duration, if not specified on the command line
if args.timeout is None:
    timeout = int(input("Enter the timeout duration (in seconds): "))
else:
    timeout = int(args.timeout)

# Create a list of ports to scan
ports = list(range(start_port, end_port + 1))

# Divide the list of ports evenly among the threads
port_lists = [ports[i::num_threads] for i in range(num_threads)]
