from socket import *
serverName = 'LAPTOP-Q0L2FP25'
serverPort = 12009
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect(('localhost', 8080))
sentence = input("Enter file name")

clientSocket.send(sentence.encode())
filecontents = clientSocket.recv(1024).decode()
print ('From Server:', filecontents)
clientSocket.close()
