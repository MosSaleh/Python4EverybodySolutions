file = open('romeo.txt')
list = list()
for line in file:
    words = line.split()
    for word in words:
        if word not in list:
            list.append(word)
            
list.sort()
   
print(list)