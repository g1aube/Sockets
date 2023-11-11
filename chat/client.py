import socket


client = socket.socket()

name = input('Your name: ')
client.connect(('127.0.0.1', 50))
client.send(name.encode())
socket_name = client.recv(1024) 
server_name = socket_name.decode()
print(server_name + ' connected!')

while True:
    message = (client.recv(1024)).decode()
    print(server_name, ':', message)
    message = input('I am: ')
    client.send(message.encode())
