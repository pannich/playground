
s = 'aibohphobia'

def palindrome(s):
    if s[0] == s[-1]:
        if len(s) == 1 or len(s) ==2:
            return 'PALINDROME'
        else:
            # print(s[1:-1])
            return palindrome(s[1:-1])
    else:
        return 'NOT PALINDROME'


print(palindrome(s))
