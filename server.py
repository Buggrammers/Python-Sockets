import socket

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # by default ipv4 and TCP
print('Socket Created')

host = socket.gethostname()
port = 224

# bind your socket with port
serversocket.bind((host, port))
serversocket.listen(3)
print('Waiting for connection')

while True:
    clientsocket, address = serversocket.accept()
    name = clientsocket.recv(1024).decode()
    print(f"Connected with {address},{name}")
    message = f"Thank-you {name} for connecting with me..."
    clientsocket.send(bytes(message, 'utf-8'))  # This is convert it into bytes from string
    clientsocket.close()
