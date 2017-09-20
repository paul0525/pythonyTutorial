import socket

server=('127.0.0.1',28072)

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(server)
sock.listen(5)
conn,address = sock.accept()
print 'connect by',address

while True:
    data = conn.recv(1024)
    if not data: break
    print data
    conn.send(data)
sock.close()