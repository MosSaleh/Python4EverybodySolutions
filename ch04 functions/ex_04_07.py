def computegrade (score):
    if 1.0 < score or score < 0.0:
        print ('Bad score')
    elif 0.9 <= score:
        print ('A')
    elif 0.8 <= score:
        print ('B')
    elif 0.7 <= score:
        print ('C')
    elif 0.6 <= score:
        print ('D')
    elif 0.6 > score:
        print ('F')

score = float(input('Enter score: '))

computegrade(score)