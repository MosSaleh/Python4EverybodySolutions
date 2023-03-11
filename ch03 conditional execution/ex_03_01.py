hours = input("Hours: ")
hours = float(hours)
rate = input("Rate: ")
rate = float(rate)
if hours > 40:
    overtime = hours - 40
    overtimerate = rate * 1.5
    overtimep = overtime * overtimerate
    hours = 40
    totalp = overtimep + hours * rate
else:
    totalp = hours * 10
print(totalp)
