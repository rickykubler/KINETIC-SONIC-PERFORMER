import argparse
from pythonosc.dispatcher import Dispatcher
from typing import List, Any

parser_reciever = argparse.ArgumentParser()
parser_reciever.add_argument("--ip", default='192.168.1.159')
parser_reciever.add_argument("--port", type=int, default=7400)
args_receiver, unknown = parser_reciever.parse_known_args()

parser_sender = argparse.ArgumentParser()
parser_sender.add_argument("--ip", default='192.168.1.213')
parser_sender.add_argument("--port", type=int, default=7374)
args_sender, unknown = parser_sender.parse_known_args()


dispatcher = Dispatcher()

def set_filter(address: str, *args: List[Any]) -> None:
    # We expect two float arguments
    if not len(args) == 2 or type(args[0]) is not float or type(args[1]) is not float:
        return

    # Check that address starts with filter
    if not address[:-1] == "/filter":  # Cut off the last character
        return

    value1 = args[0]
    value2 = args[1]
    filterno = address[-1]
    print(f"Setting filter {filterno} values: {value1}, {value2}")

dispatcher.map("/filter*", set_filter) 

from pythonosc import osc_server
from pythonosc import udp_client

server = osc_server.BlockingOSCUDPServer((args_receiver.ip, args_receiver.port), dispatcher)
client = udp_client.SimpleUDPClient(args_sender.ip, args_sender.port)

client.send_message("/filter1", [1., 2.])
server.serve_forever()
