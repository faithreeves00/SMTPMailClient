from socket import *

import time

msg = '\r\n I love Computer Networks!'

endmsg = '\r\n.\r\n'

# Choose a mail server (e.g. Google mail server) and call it mailserver
mailserver = ("127.0.0.1", 2000)

# Create socket called clientSocket and establish a TCP connection with mailserver
clientSocket = socket(AF_INET, SOCK_STREAM)

clientSocket.connect(mailserver)

recv = clientSocket.recv(1024)
recv = recv.decode()
print("Message after connection request: " + recv)

if recv[:3] != '220':
    print('220 reply not received from server.')

# Send HELO command and print server response.
heloCommand = 'HELO Faith\r\n'

clientSocket.send(heloCommand.encode())

recv1 = clientSocket.recv(1024)

recv1 = recv1.decode()

print("Message after HELO command: " + recv1)

if recv1[:3] != '250':
    print('250 reply not received from server.')

# Send MAIL FROM command and print server response.
mailFrom = "MAIL FROM: <faithereeves@gmail.com> \r\n"

clientSocket.send(mailFrom.encode())

recv2 = clientSocket.recv(1024)

recv2 = recv2.decode()

print("After MAIL FROM command: " + recv2)

# Send RCPT TO command and print server response.
rcptTo = "RCPT TO: <faithreeves@letu.edu> \r\n"

clientSocket.send(rcptTo.encode())

recv3 = clientSocket.recv(1024)

recv3 = recv3.decode()

print("After RCPT TO command: " + recv3)

# Send DATA command and print server response.
data = "DATA\r\n"

clientSocket.send(data.encode())

recv4 = clientSocket.recv(1024)

recv4 = recv4.decode()

print("After DATA command: " + recv4)

# Send message data.
# Message ends with a single period.
subject = "Subject: SMTP Client Python Script \r\n\r\n"
clientSocket.send(subject.encode())
date = time.strftime("%a, %d %b %Y %H:%M:%S +0000", time.gmtime())
date = date + "\r\n\r\n"
clientSocket.send(date.encode())
clientSocket.send(msg.encode())
clientSocket.send(endmsg.encode())
recv_msg = clientSocket.recv(1024)
print("Response after sending message body: " + recv_msg.decode())

# Send QUIT command and get server response.
quitCmd = "QUIT\r\n"
clientSocket.send(quitCmd.encode())
recv5 = clientSocket.recv(1024)
print(recv5.decode())
clientSocket.close()
