file = open('mbox-short.txt')
count = dict()
for line in file:
    words = line.split()
    if line.startswith('From '):
        email = words[1]
        atpos = email.find('@')
        domain = email[atpos + 1: ]
        count[domain] = count.get(domain, 0) + 1
    else:
        continue
print(count)
