lrg = None
sml = None 
while True:
    inpnum = input('Enter a number: ') 
    try: 
        inpnum = float(inpnum)
    except:
        if inpnum == 'done':
            break
        else:
            print('Enter numerical number')
    if lrg is None or inpnum > lrg:
        lrg = inpnum
    if sml is None or inpnum < sml:
        sml = inpnum
    
print('Largest:', lrg, 'Smallest: ', sml)