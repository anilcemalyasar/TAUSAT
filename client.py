import socket
import time
# from testTelemetri import *
from testUcus import *

HEADER = 64
PORT = 5050
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"
SERVER = "192.168.56.1"  
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)

#
#for i in telemetri_list:
#    send(i)

if commandIn() == False:
    operation += 1
    send("{}. Aşamaya geçiliyor!".format(operation))



time.sleep(3)
send(DISCONNECT_MESSAGE)

