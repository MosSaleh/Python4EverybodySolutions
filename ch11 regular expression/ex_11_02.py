import re
file = open('mbox.txt')
list= list()
for line in file:
    NR_num = re.findall('New Revision: ([0-9]+)', line)
    if len(NR_num) != 1:
        continue
    else:
        num =NR_num[0]
        num = float(num)
        list.append(num)
print (int(sum(list)/len(list)))