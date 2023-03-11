txt = input('Enter file name: ')
count = 0 
try:
    file = open(txt)
except:
    if txt == 'na na boo boo':
        print('NA NA BOO BOO TO YOU - You have been punkd!')
        quit()
    else:
        print ('File cannot be opened:',txt)
        quit()
for line in file:
    if line.startswith ('Subject:'):
        count = count + 1
        continue
print ('There were',count, 'subject lines in', txt)
