# Mark Gong-Guy

#import socket module
from socket import *
serverSocket = socket(AF_INET, SOCK_STREAM) #Prepare a sever socket
serverPort=8080
serverSocket.bind(('',serverPort))
serverSocket.listen(1)
print 'Web Server on Port',serverPort
while True:
	#Establish the connection
	print 'Ready to serve...'
	connectionSocket, addr = serverSocket.accept()
	try:
		message = connectionSocket.recv(1024)
		print message, '::', message.split()[0],':',message.split()[1]
		filename = message.split()[1]
		print filename, '||',filename[1:]

		f = open(filename[1:])
		outputdata = f.read()
		print outputdata
		#HTTP Header
		connectionSocket.send('\nHTTP/1.1 200 OK\n\n')
		connectionSocket.send(outputdata)
		connectionSocket.close()
     		
	except IOError:
		print "404 Not Found"
		connectionSocket.send('\HTTP/1.1 404 Not Found\n\n')
		connectionSocket.close()	
