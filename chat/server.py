import socket


server = socket.socket()
server.bind(('127.0.0.1', 50))
server.listen()

print('Server started!')

name = input('Your name: ')
connection, address = server.accept()

client = (connection.recv(1024)).decode()
print(client + ' connected!')
connection.send(name.encode())

while True:
    message = input('I am: ')
    connection.send(message.encode())
    message = connection.recv(1024)
    message = message.decode()
    print(client, ':', message)
    
    