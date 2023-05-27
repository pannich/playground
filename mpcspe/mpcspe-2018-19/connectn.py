import numpy as np

row_, col_, n = list(map(int,input().split(" ")))

# make M matrix
M = []
for line in range(row_):
    a = input().split(" ")
    M.append(a)

print(M)

i=0 #row
j=0 #col
winner = M[i][j]
count = 0

#check horizontal
def connectn_horizontal(n, row_, col_, M, winner, count):
    for i in range(row_):
        for j in range(col_):
            current = M[i][j]
            if winner == current:
                count += 1
                # print(M[i][:j+1]) #preview array
                if count == n :
                    if winner != 'O':
                        print(f'found winner horzontal {winner}')
                        break
            else:
                count = 1
                # print(M[i][:j+1])
            winner = current
    winner = 'NONE'
    print(winner)

#check vertical
def connectn_vertical(n, row_, col_, M, winner, count):
    for j in range(col_):
        for i in range(row_):
            current = M[i][j]
            if winner == current:
                count += 1
                if count == n:
                    if winner != 'O':
                        print(f'found winner vertical {winner}')
                        break
            else:
                count = 1
            winner = current
    winner = 'NONE'
    print(winner)


def connectn_cross(n, row_, col_, M, winner, count):
    for j in range(col_): #0 1 2 3 4 5 6
        i = 0 #reset i
        winner = 'O'
        while i< row_ and j< col_:
            current = M[i][j]
            if winner == current:
                count += 1
                if count == n:
                    if winner != 'O':
                        print(f'found winner cross {winner}')
                        break
            else:
                count = 1
            winner = current
            i+=1
            j+=1
    winner = 'NONE'
    print(winner)

def connectn_cross_inv(n, row_, col_, M, winner, count):
    for j in range(1,col_+1): # 1 2 3 4 5 6
        i = 0 #reset i
        j = -j # -1 -2 -3 -4 -5 -6
        winner = 'O'
        while i< row_ and j >= -col_:
            current = M[i][j]
            if winner == current:
                count += 1
                if count == n:
                    if winner != 'O':
                        print(f'found winner cross inv {winner}')
                        break
            else:
                count = 1
            winner = current
            i+=1
            j-=1
    winner = 'NONE'
    print(winner)

connectn_horizontal(n, row_, col_, M, winner, count)
connectn_vertical(n, row_, col_, M, winner, count)
connectn_cross(n, row_, col_, M, winner, count)
connectn_cross_inv(n, row_, col_, M, winner, count)
