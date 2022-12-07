s = '1.223, 54.3,3.1415, 2.74,0.111,11.26'
total = 0
z = 0 

for k in range(0,len(s)):
    if s[k] == ',' and k < len(s) - 1:
       total = (float(s[z:k])) + total
       z = (k+1)
    elif k == len(s) - 1:
        total = (float(s[z:len(s)])) + total 
print(total)