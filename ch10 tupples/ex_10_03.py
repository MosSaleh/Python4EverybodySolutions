inp = input('File name: ')
file = open(inp)
count = dict()
import string
alphabet = string.ascii_lowercase + string.ascii_uppercase
for line in file:
    lowerline = line.lower()
    words=lowerline.split()
    for word in words:
        for letter in word:
            if letter in alphabet:
                count[letter] = count.get(letter,0) +1
            else:
                continue
for k,v in sorted([(v,k) for k,v in count.items()],reverse=True):
    print(k,v)