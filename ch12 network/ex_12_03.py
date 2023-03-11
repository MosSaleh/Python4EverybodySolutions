import urllib.request, urllib.parse, urllib.error

content = urllib.request.urlopen('https://www.dr-chuck.com/dr-chuck/resume/bio.htm').read()
content = content.decode()
print (content[:3000])
print(len(content))
