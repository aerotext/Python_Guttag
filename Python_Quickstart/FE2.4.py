counter = 10
prime = 0
test = 0
while (counter != 0):
    test = int(input('Please enter an integer: '))
    if test%2 != 0 and (prime == 0 or test > prime):
        prime = test
    counter -= 1
if prime == 0:
    print("There are no primes")
else: 
    print("The largest prime is, ", prime, ".")
