#SMTP Client - Mark Gong-Guy
from socket import *

# Choose a mail server (e.g. Google mail server) and call it mailserver
mailserver = "localhost"
port = 465

#Variables (Settings)
recipient = "<mark.a.gong-guy@biola.edu>"
sender = "<bobby.joe@biola.edu>"
msg = "\r\n I love computer networking!"
endmsg = "\r\n.\r\n"

# Create socket called clientSocket and establish a TCP connection with
# mailserver
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((mailserver, port))
recv = clientSocket.recv(1024)
print recv
if recv[:3] != '220':
         print '220 reply not received from server.'

# Send HELO command and print server response.
heloCommand = 'HELO Alice\r\n'
clientSocket.send(heloCommand)
recv1 = clientSocket.recv(1024)
print recv1
if recv1[:3] != '250':
    print '250 reply not received from server.'

# Send MAIL FROM command and print server response.
mailFrom = 'MAIL FROM: ' + sender + '\r\n'
clientSocket.write(mailFrom)
recv2 = clientSocket.recv(1024)
print recv2
if recv2[:3] != '250':
    print '250 reply not recieved from server.'
                
# Send RCPT TO command and print server response.
rcptTo = 'RCPT TO: ' + recipient + '\r\n'
clientSocket.write(rcptTo)
recv3 = clientSocket.recv(1024)
print recv3
if recv3[:3] != '250':
    print '250 reply not recieved from server.'
                 
# Send DATA command and print server response.
dataCommand = 'DATA\r\n'
clientSocket.write(dataCommand)
recv4 = clientSocket.recv(1024)
print recv4
if recv4[:3] != '354':
    print '345 reply not recieved from server.'
    
# Send message data.
clientSocket.write(msg)
                 
# Message ends with a single period.
clientSocket.write(endmsg)
recv5 = clientSocket.read(1024)
print recv5
if recv5[:3] != '250':
    print '250 reply not recieved from server.'
                 
 # Send QUIT command and get server response.
clientSocket.close()
                 
