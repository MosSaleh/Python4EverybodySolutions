filename = input('File name: ') 
file = open(filename)
count = dict()
for line in file:
    words = line.split()
    if line.startswith('From '):
        email = words[1]
        count[email]= count.get(email, 0 ) + 1
    else:
        continue

bigemail= None
bignum = None
for email, num in count.items():
    if bignum is None or num > bignum:
        bignum = num
        bigemail = email
print(bigemail, bignum)