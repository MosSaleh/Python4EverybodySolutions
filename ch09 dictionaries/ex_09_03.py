file = open('mbox-short.txt')
count = dict()
for line in file:
    words = line.split()
    if line.startswith('From '):
        email = words[1]
        count[email] = count.get(email, 0) + 1
    else:
        continue
print(count)