y = input('Please enter a string: ')
x = input('Please enter one more string: ')

def isIn(x, y):
    if len(x) >= len(y):
        p = y in x 
    else:
        p = x in y 
    print(p)
    return p

isIn(x,y)




