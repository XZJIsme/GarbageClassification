# server
from socket import *

def send_back(serverName='127.0.0.1', serverPort = 12345, data=None):
    BUFSIZ = 1024
    ADDR = (serverName,serverPort)

    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect(ADDR)

    clientSocket.send(data)
    clientSocket.close()
    print('sent')
