import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(("u-zagidully.ru", 80))

cmd = "GET http://u-zagidully.ru/ HTTP/1.0\r\n\r\n".encode()

mysock.send(cmd)

while True :
    data = mysock.recv(512)
    if len(data) < 1 :
        break
    print(data.decode())

mysock.close()
