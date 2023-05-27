# front princess
# end baron
# middle priest
# no community name commoners

# input
comName = input()
n = int(input())
people = [input() for i in range(n)]

# comName = 'mentior'
# people = ['mentioromenas','asmentiorones','summentior','menolaxios']

def apaxian(comName,people):
    p = 0
    h = 0
    r = 0
    c = 0
    for man in people:
        if comName in man[:len(comName)]:
            p+=1
        elif comName in man[-len(comName):]:
            h+=1
        elif comName in man:
            r+=1
        else:
            c+=1
    print(p,'PRINCESS')
    print(h,'BARON')
    print(r,'PRIEST')
    print(c, "COMMONER")
    return

apaxian(comName,people)

#22mins
