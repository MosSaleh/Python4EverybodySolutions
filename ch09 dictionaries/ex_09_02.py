file = open('mbox-short.txt')
counts = dict()
for line in file:
    words = line.split()
    if line.startswith('From '):
        day = words[2]
        counts[day] = counts.get(day,0) + 1
    else:
        continue     
print (counts)