import ipaddress

# Define the network to scan
network = ipaddress.ip_network('192.0.2.0/24')

# Scan the network for connected devices
for host in network.hosts():
    try:
        # Try to connect to the host
        socket.create_connection((host, 80), timeout=0.5)
        print(f'{host} is up')
    except OSError:
        # If the host is not responding, print a message
        print(f'{host} is down')
