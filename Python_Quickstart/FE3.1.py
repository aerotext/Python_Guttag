perfect = int(input('Please input an integer: '))
pwr = 1

while pwr < 6:
    if perfect >= 0:
        root = 0
    else:
        root = perfect
    while root**pwr <= perfect:
        if root**pwr == perfect:
            print('root =', root, 'pwr = ', pwr)
        root +=1
    pwr += 1
