import socket

config = {
    'IP': '127.0.0.1',
    'PORT': 8000,
}

server = socket.socket()
server.bind((config['IP'], config['PORT']))
server.listen()

print('Server have started!')

while True:
    client_socket, address = server.accept()
    data = client_socket.recv(1024).decode('utf-8')
    print(data)
    headers = 'HTTP/1.1 200 OK\r\n\Content-Type:text/html; charset=utf-8\r\n\r\n'
    content = 'Hello!'.encode('utf-8')
    client_socket.send(headers.encode('utf-8') + content)
    client_socket.shutdown(socket.SHUT_WR)