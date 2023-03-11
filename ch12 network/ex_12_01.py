import socket
import re 

while True:
    url = input('Url: ')
    hostname = re.findall('http://(.+)/', url)
    if len(hostname) < 1:
        print('invalid url')
        continue
    else: break

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect((hostname[0], 80))
cmd_str = 'GET ' + url + ' HTTP/1.0\r\n\r\n'
cmd = cmd_str.encode()
mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    print(data.decode(), end=(''))
mysock.close()
