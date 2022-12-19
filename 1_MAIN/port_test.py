import argparse
from pythonosc import udp_client

parser = argparse.ArgumentParser()
# OSC server ip: '127.0.0.1'
parser.add_argument("--ip", default='192.168.255.27', help="The ip of the OSC server")
# OSC server port (check on SuperCollider) 57120
parser.add_argument("--port", type=int, default=7500, help="The port the OSC server is listening on")

# Parse the arguments
args, unknown = parser.parse_known_args()

# Start the UDP Client
client = udp_client.SimpleUDPClient(args.ip, args.port)

print(args.port)