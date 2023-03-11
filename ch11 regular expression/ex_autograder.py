import re
file = open('regex_sum_1730134.txt')
OGlist = list()
numbers = list()
for line in file:
    find = re.findall('[^0-9]*([0-9]+)[^0-9]*', line)
    if len(find) > 0:
        OGlist.append(find)
    else:
        continue
for x in OGlist:
    for number in x:
        number = int(number)
        numbers.append(number)

print(sum(numbers), len(numbers))