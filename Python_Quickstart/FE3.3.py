x = float(input('please enter a number: '))
epsilon = 0.01
numGuesses = 0
low = 0.0
high = max(1.0, abs(x))
ans = (high + low)/2

while abs(ans**3-abs(x)) >= epsilon:
    print('low = ', low, " high = ", high, 'ans = ', ans)
    numGuesses += 1
    if ans**3 <  abs(x):
        low = ans
    else:
        high = ans
    ans = (high + low)/2 

print('Number of guesses = ', numGuesses)
if x >= 0:
    print(ans, "is close to the cube root of ", x)
else:
    print(ans*-1, "is close to the cube root of", x)