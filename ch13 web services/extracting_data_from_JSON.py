import json
import urllib.parse, urllib.request, urllib.error

url = input('Url: ')
urlopen = urllib.request.urlopen(url)
data = urlopen.read()
jason = json.loads(data)
lst = list()
info = jason['comments']

for item in info:
    number = item['count']
    realnum = int(number)
    lst.append(realnum)

print(sum(lst))
    