from socket import *
serverName='LAPTOP-Q0L2FP25'
serverPort = 12009
serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind(('localhost', 8080))
serverSocket.listen(1)
print ("The server is ready to receive")
while 1:
    connectionSocket, addr = serverSocket.accept()
    sentence = connectionSocket.recv(1024).decode()

    file=open(sentence,"r")
    l=file.read(1024)

    connectionSocket.send(l.encode())
    file.close()
    connectionSocket.close()
