#!/usr/bin/python3
import socket

clientsocket = socket.socket(
               socket.AF_INET,
               socket.SOCK_STREAM
)

host = "The host you are gonna connect in str"

port = 444

clientsocket.connect((host,port)) # Connect to h
message = clientsocket.recv(1024) # Receive 1024 bytes
clientsocket.send(message) # Send message
#Message = message.decode('utf-8')
# utf-8 -> 16 bytes per char
# ascii -> 8 bytes per char
clientsocket.close()
