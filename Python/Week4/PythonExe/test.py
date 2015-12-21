import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('www.facebook.com', 80))
mysock.send('GET hhttps://www.facebook.com/Athlonefloodrelief/?fref=ts\n\n')

while True:
    data = mysock.recv(512)
    if ( len(data) < 1 ) :
        break
    print data;

mysock.close()
