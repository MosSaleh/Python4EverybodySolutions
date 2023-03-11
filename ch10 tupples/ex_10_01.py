f_inp = input('Enter file name: ')
file = open(f_inp)
count = dict()
for line in file:
    if line.startswith('From '):
        words = line.split()
        email = words[1]
        count[email] = count.get(email,0) + 1
    else:
        continue
print (sorted([(v,k) for k,v in count.items()], reverse= True)[:1])