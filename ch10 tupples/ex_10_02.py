file = open('mbox-short.txt')
count = dict()
for line in file:
    if line.startswith('From '):
        words = line.split()
        time = words[5]
        hour = time[:2]
        count[hour] = count.get(hour, 0) + 1
    else:
        continue
countsrt = sorted((k,v) for k,v in count.items())
for k,v in countsrt:
    print(k,v)