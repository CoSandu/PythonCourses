import socket

myso = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
myso.connect(('www.py4inf.com', 80))

myso.send('GET http://www.py4inf.com/code/romeo.txt HTTP/1.0\n\n')

while True:
    data = myso.recv(512)
    if(len(data)<1):
        break
    print data
myso.close()
