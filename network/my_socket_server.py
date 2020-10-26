from socket import *
import time

HOST = "0.0.0.0"
PORT = 2236
BUFSIZE = 1024

ADDR = (HOST,PORT)

tcpServer = socket(AF_INET,SOCK_STREAM)
tcpServer.bind(ADDR)
tcpServer.listen(5)

while True:
    print("waiting for connecting....")
    #NOTE:accept每次只能和一个接收一个对象,另一个回话处于阻塞状态
    tcpClient,addr = tcpServer.accept()
    print(f"...connected from {addr}")
    while True:
        data = tcpClient.recv(BUFSIZE)
        if not data:
            break
        print(f"recv data :{data}")
        local_time = time.asctime(time.localtime(time.time()))
        tcpClient.send(local_time.encode("utf-8"))

tcpClient.close()