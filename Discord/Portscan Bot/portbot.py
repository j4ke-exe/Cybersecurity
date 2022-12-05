import discord
import argparse
import socket
from flask import Flask, render_template, request

# Create a Discord client
client = discord.Client()

# Create a Flask app
app = Flask(__name__)

# Define a function to run a port scan
def port_scan(hostname, port_range, timeout):
    # Split the port range into a start and end port
    start_port, end_port = map(int, port_range.split("-"))

    # Create a list of ports to scan
    ports = list(range(start_port, end_port + 1))

    # Initialize an empty list of open ports
    open_ports = []

    # Iterate over the list of ports
    for port in ports:
        # Create a socket object
        s = socket.socket()

        # Set the timeout duration
        s.settimeout(timeout)

        # Try to connect to the port
        try:
            s.connect((hostname, port))
            open_ports.append(port)
        except:
            pass

        # Close the socket
        s.close()

    # Return the list of open ports
    return open_ports

# Define an event handler for messages
@client.event
async def on_message(message):
    # If the message starts with the command prefix ".scan"
    if message.content.startswith(".scan"):
        # Split the message into a list of words
        words = message.content.split()

        # Check if a hostname and port range were provided
        if len(words) > 2:
            # Get the hostname and port range from the message
            hostname = words[1]
            port_range = words[2]

            # Set the default timeout duration
            timeout = 5

            # Check if a timeout duration was provided
            if len(words) > 3:
                # Get the timeout duration from the message
                timeout = int(words[3])

            # Run a port scan on the hostname
            open_ports = port_scan(hostname, port_range, timeout)

            # Send the list of open ports to the user
            await message.channel.send(f"{hostname} has open ports: {open_ports}")
        else:
            # If the hostname and port range were not provided, send an error message
            await message.channel.send("Please provide a hostname and port range")

# Define a route for the web control panel
@app.route("/", methods=["GET", "POST"])
def index():
    # If the form is submitted
    if request.method == "POST":
        # Get the command from the form
        command = request.form["command"]

        # Send the command to the Discord bot
        client.loop.create_task(client.send_message(client.get_channel(<CHANNEL_ID>), command))

        # Redirect to the control panel page
        return redirect(url_for("index"))

    # If the form is not submitted, render the control panel page
    return
