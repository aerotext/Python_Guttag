#Newton-Raphson Method for finding the root of a polynomial
#To find a square root, find x when such that x^2 -y = 0 within epsilon of k

y = float(input('Please enter a positive number: '))
k = float(input('Please enter a value for epsilon: '))
g = y/2

while abs(g**2 -y) >= k:
    g = (g - ((g**2-y)/(2*g)))
print('The square root of', k ,"equals", g)