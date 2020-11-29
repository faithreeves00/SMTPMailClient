# SMTP Mail Client
A simple mail client that can send emails to any recipient. The client connects to a mail server, dialogues with the mail server using the SMTP protocol, and then sends an email message to the mail server.

# Note:
Finding an open SMTP server is difficult, so for the server use the following command line:

python3 -m smtpd -c DebuggingServer -n 127.0.0.1:2000

This creates a fake server that will respond to messages. Use the IP address 127.0.0.1 in both the server and the client.
