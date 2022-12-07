def isPal(s):
    def toChar(s):
        s = s.lower() 
        letters = ''
        for c in s:
            if c in 'abcdefghijklmnopqrstuvwxyz':
                letters = letters + c
        return letters 

    def palindrome(s):
        if len(s) <= 1:
            return True 
        else: 
            return s[0] == s[-1] and palindrome(s[1:-1])
    return palindrome(toChar(s))

s = input('Please enter a word or sentence: ')

if isPal(s) == True:
    print(s, 'is a palindrome')
else:
    print(s, 'is not a palindrome you silly bird')
