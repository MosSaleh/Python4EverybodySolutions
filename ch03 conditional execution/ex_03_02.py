hours = input("Hours?")
rate = 10
try:
    hours = int(hours)
except:
    print("type a numerical number please")
    quit()
if hours > 40:
    overtime = hours - 40
    overtimep = overtime * 15
    hours = 40
    totalp = overtimep + hours * rate
else:
    totalp = hours *10
print('total pay: ', totalp )