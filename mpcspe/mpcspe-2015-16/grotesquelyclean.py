'''if has 6 -> clean
if add up to 30 -> clean
'''

m =[int(e) for e in input().split()]

if 6 in m:
    print('CLEAN')
elif sum(m) >= 30:
    print('CLEAN')
else:
    print('DO NOT CLEAN')
