#The server and client just connect and send & reply 1 message

from http import client
import socket
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(('172.20.10.4',55055))
s.listen(5)
clientsocket, clientaddress = s.accept()
print(clientsocket)
print('Got a connection from %s' %str(clientaddress))
msg = input('Enter any message: ')
msg_encode = msg.encode('utf-8')
clientsocket.send(msg_encode)
clientsocket.recv(1024)
message_back = clientsocket.recv(1024)
message_back_decode = message_back.decode('utf-8')
print('Respone from the client: '+ message_back_decode)
s.close()