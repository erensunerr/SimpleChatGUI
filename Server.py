#!usr/bin/python3

import socket

serversocket = socket.socket(
            socket.AF_INET,     #           ADDRESS FAMILIES
                                #Name                   Purpose
                                #AF_UNIX, AF_LOCAL      Local communication
                                #AF_INET                IPv4 Internet protocols
                                #AF_INET6               IPv6 Internet protocols
                                #AF_APPLETALK           Appletalk
                                #AF_BLUETOOTH           Bluetooth


            socket.SOCK_STREAM  #           SOCKET TYPES
                                #Name           Way of Interaction
                                #SOCK_STREAM    TCP
                                #SOCK_DGRAM     UDP
            )

host = socket.gethostname()#Might not be correct on windows instead just parse ipconfig
port = 4444
serversocket.bind((host,port)) #bind socket to port and host
serversocket.listen( #optional argument: maximum number of connections; default = 1
) #listen for connections

while True:
    clientsocket, address = serversocket.accept() #accept the connection
    # Message = "message".encode('utf-8')
    # utf-8 -> 16 bytes per char
    # ascii -> 8 bytes per char
    clientsocket.send() # send bytes object
    clientsocket.recv(
    #Optional variable how many bytes
    ) # receive bytes object
clientsocket.close()
