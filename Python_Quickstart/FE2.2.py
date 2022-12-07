x = int(input("Enter an integer (1 of 3)"))
y = int(input("Enter an integer (2 of 3)"))
z = int(input("Enter an integer (3 of 3)"))
k = 0

if x%2 != 0:
    k = x
if y%2 != 0 and (k == 0 or y > k) : 
    k = y
if z%2 != 0 and (k == 0 or z > k): 
    k = z
if k == 0:
    print("There are no odd numbers")
else:
    print("The largest odd number is ", k)
