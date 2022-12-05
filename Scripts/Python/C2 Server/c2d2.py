import cmd
import socket

# Create a class to handle the C2 server
class C2Server(cmd.Cmd):
    # Initialize the server
    def __init__(self):
        super().__init__()

        # Create a TCP/IP socket
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Bind the socket to the address and port
        self.server_address = ('localhost', 10000)
        print(f'Starting up C2 server on {self.server_address[0]} port {self.server_address[1]}')
        self.sock.bind(self.server_address)

        # Listen for incoming connections
        self.sock.listen(1)

    # Handle the 'connect' command
    def do_connect(self, line):
        # Wait for a connection
        print('Waiting for a connection...')
        self.connection, self.client_address = self.sock.accept()
        print(f'Connection from {self.client_address}')

    # Handle the 'send' command
    def do_send(self, line):
        # Send the specified data to the client
        self.connection.sendall(line.encode())
        print(f'Sent {line} to {self.client_address}')

    # Handle the 'receive' command
    def do_receive(self, line):
        # Receive data from the client
        data = self.connection.recv(16)
        print(f'Received {data} from {self.client_address}')

    # Handle the 'close' command
    def do_close(self, line):
        # Close the connection to the client
        self.connection.close()
        print(f'Connection closed to {self.client_address}')

    # Handle the 'quit' command
    def do_quit(self, line):
        # Quit the program
        return True

# Create an instance of the C2 server and start the command loop
C2Server().cmdloop()
