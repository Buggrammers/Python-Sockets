import socket

c = socket.socket()

c.connect(('localhost', 9998))

name = input("Who are you: ")
c.send(bytes(name, 'utf-8'))

print(c.recv(1024).decode())  # for decoding byte
