txt = input("Enter text: ")
file = open(txt)
nums = 0
count = 0
for line in file:
    if line.startswith("X-DSPAM-Confidence:"):
        colpos = line.find(":")
        num = float(line[colpos + 1 :])
        nums = num + nums
        count = count + 1
        continue
print("Average spam confidence: " + str(nums / count))
