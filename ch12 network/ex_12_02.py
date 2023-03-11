import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org',80))
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)
list = list()
while True:
    data = mysock.recv(3000)
    if len(data) < 1:
        break
    text = data.decode()
counts = []
for character in text:
    counts.append(character)
    if len(counts) == 3000:
        break
    else:
        continue
print (text[:3000])
print ( 'Characters:', len(counts))
mysock.close()