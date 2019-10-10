#!/usr/bin/env python
 
import socket
 
HOST = "localhost"
PORT = 8080
 
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((HOST, PORT))
 
sock.sendall(bytes("Hello\n",'utf-8'))
data = sock.recv(1024)
dataH = data.decode('utf-8')
print("1)",dataH)
#print(dataS == "olleH\r\n")
 
if (dataH == "olleH\r\n"):
	sock.sendall(bytes("Bye\n",'utf-8'))
	data = sock.recv(1024)
	dataB = data.decode('utf-8')
	print("2)", dataB)

	if (dataB == "eyB\r\n"):
		sock.close()
		print("Socket closed")