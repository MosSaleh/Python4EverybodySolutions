list = list()
while True:
    num = input('Enter a number: ')
    try: 
        num = float(num)
    except:
        if num == 'done':
            break
        else:
            print('enter numerical number please')
            continue
    list.append(num)

print(max(list), min(list))