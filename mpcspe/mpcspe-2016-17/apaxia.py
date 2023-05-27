first,last = input('Enter:').split(" ")

if len(last) == 5:
    last = last * 4
else:
    last = last * len(last)

print(first, last)
