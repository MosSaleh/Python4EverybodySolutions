import xml.etree.ElementTree as ET
import urllib.request, urllib.parse, urllib.error

url = input('Enter url: ')
urlopen = urllib.request.urlopen(url)
data = urlopen.read()
tree = ET.fromstring(data)

#print(data.decode())
numbers = tree.findall('.//count')
count = list()

for element in numbers:
    number = int(getattr(element, 'text'))
    count.append(number)
    
print(sum(count))