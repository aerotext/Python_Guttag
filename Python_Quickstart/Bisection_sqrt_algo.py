x = float(input('please enter a non-negative number: '))
epsilon = 0.01
numGuesses = 0
low = 0.0
high = max(1.0, x)
ans = (high + low)/2

while abs(ans**2-x) >= epsilon:
    print('low = ', low, " high = ", high, 'ans = ', ans)
    numGuesses += 1
    if ans**2 <  x:
        low = ans
    else:
        high = ans
    ans = (high + low)/2 

print('Number of guesses = ', numGuesses)
print(ans, "is close to the square root of ", x)
