str = "X-DSPAM-Confidence: 0.8475 "


num = float(str[str.find(":") + 1 :].strip())

print(num)
