from socket import *

HOST = "10.63.0.10"
PORT = 2236
BUFSIZE = 1024

ADDR = (HOST,PORT)

tcpClient = socket(AF_INET,SOCK_STREAM)
tcpClient.connect(ADDR)

while True:
    data = input("~:")
    if not data:
        break
    #发送时候需要编码
    tcpClient.send(data.encode("utf-8"))
    data = tcpClient.recv(BUFSIZE)
    if not data:
        break
    print(data)

tcpClient.close()