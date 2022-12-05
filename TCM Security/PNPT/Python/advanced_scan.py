import socket
import argparse
import threading

# python3 advanced_scan.py -t example.com -p 1-1024 -n 10

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

# Extract the target host and port range from the arguments
host = args.target
port_range = args.portrange

# Split the port range into a start and end port
start_port, end_port = map(int, port_range.split("-"))

# Extract the number of threads to use
num_threads = int(args.numthreads)

# Extract the timeout duration
timeout = int(args.timeout)

# Create a list of ports to scan
ports = list(range(start_port, end_port + 1))

# Divide the list of ports evenly among the threads
port_lists = [ports[i::num_threads] for i in range(num_threads)]

# Define a function to scan a given list of ports
def scan_ports(port_list):
    # Create a socket object
    s = socket.socket()

    # Set the socket timeout
    s.settimeout(timeout)

    # Scan the specified list of ports
    for port in port_list:
        try:
            # Try to connect to the target host and port
            s.connect((host, port))
            print(f"Port {port} is open on {host}")
        except:
            # If the connection fails or times out, print a message indicating that the port is closed
            print(f"Port {port} is closed on {host}")

# Create a list of threads
threads = []

# Start a new thread for each list of ports
for port_list in port_lists:
    thread = threading.Thread(target=scan_ports, args=(port_list,))
    thread.start()
    threads.append(thread)

# Wait for all threads to finish
for thread in threads:
    thread.join()
