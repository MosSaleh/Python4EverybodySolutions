def computepay(hours, rate):
    if hours <= 40:
        pay = hours * rate
    elif hours > 40:
        pay = 40 * rate + (hours - 40) * (1.5 * rate)
    return pay


hours = float(input("Hours: "))
rate = float(input("Rate: "))
print("Pay", computepay(hours, rate))
