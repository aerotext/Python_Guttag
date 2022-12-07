def fib(n):
    if n == 0 or n == 1:
        return 1
    else: 
        return fib(n-1) + fib(n-2)

x = int(input("Enter a positive integer: "))
print('The Fibbonaci sum of', x, 'equals', fib(x))
