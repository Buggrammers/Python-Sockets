import socket

clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()
port = 224

clientsocket.connect((host, port))

name = input("Who are you: ")
clientsocket.send(bytes(name, 'utf-8'))
print(clientsocket.recv(1024).decode())  # for decoding byte
message = clientsocket.recv(1024)
clientsocket.close()
