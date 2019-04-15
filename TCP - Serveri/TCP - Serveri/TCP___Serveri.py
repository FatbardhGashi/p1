from socket import*
from _thread import*


serverName = 'localhost'
serverPort = 12000

serverSocket = socket(AF_INET,SOCK_STREAM)
try:
    serverSocket.bind((serverName, serverPort))
except socket.error:
    print

serverSocket.listen(5)
    

