import socket

s = socket.socket()  # by default ipv4 and TCP
print('Socket Created')

# bind your socket with port
s.bind(('localhost', 9998))
s.listen(3)
print('Waiting for connection')

while True:
    c, addr = s.accept()
    name = c.recv(1024).decode()
    print('Connected with', addr,name)
    c.send(bytes('Done', 'utf-8'))  # This is convert it into bytes from string
    c.close()
