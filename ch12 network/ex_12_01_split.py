import socket

url = input('Url: ')
try:
    url_pieces = url.split('/')
except:
    print('invalid url')
    
hostname = url_pieces[2]
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect((hostname,80))

str = 'GET ' + url + ' HTTP/1.0\r\n\r\n' 
cmd = str.encode()
mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    print(data.decode(), end='')
mysock.close()