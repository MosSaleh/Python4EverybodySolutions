import re
file = open('mbox.txt')
inp = input('Enter a regular expression: ')
count = dict()
for line in file:
    find = re.findall (inp, line)
    if len(find) != 1:
        continue
    else:
        count[inp] = count.get(inp,0) + 1
print(sorted(((v) for k,v in count.items()), reverse=True)[:1])