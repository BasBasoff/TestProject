import socket

HOST = 'localhost'    # The remote host
PORT = 50007              # The same port as used by the server
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(b'0002 C1 01:13:02.877 00CR')
    data = s.recv(1024).decode('utf-8')
print('Received', repr(data))