# client
from socket import *
import AI_stuff

def readLocalIP():
    with open('local_ip.txt', mode='r') as ip:
        a = ip.read()
        return a

def readServerIP():
    with open('server_ip.txt', mode='r') as ip:
        a = ip.read()
        return a

def send_to_server(serverName=readServerIP(), serverPort = 23333, data=None):
    BUFSIZ = 1024
    ADDR = (serverName,serverPort)
    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect(ADDR)
    # clientSocket.listen(1)
    # conn, addr = clientSocket.accept()
    # clientSocket.connect(ADDR)
    pass
    clientSocket.send(data)
    # received = clientSocket.recv(BUFSIZ)
    clientSocket.close()
    # try:
    # while True:
    #     if not data:
    #         break
    #     clientSocket.send(data)
    #     returnData = clientSocket.recv(BUFSIZ)
    #     if not returnData:
    #         break
    #     else:
    #         return returnData
    #         clientSocket.close()
    # # except:
    # #     print('client 数据发送失败')
    # clientSocket.close()

