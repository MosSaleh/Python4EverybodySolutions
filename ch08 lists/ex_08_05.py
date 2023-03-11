file = open('mbox-short.txt')
count = 0
for line in file:
    if not line.startswith ('From '):
        continue
    else: 
        words = line.split()
        print (words[1])
        count = count + 1

print ('There were', count, 'lines in the file with From as the first word')
