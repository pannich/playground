# #input
# row_,col_ = list(map(int,input("Enter:").split()))
# x, y = list(map(int,input("start at:").split()))
# M = []
# for r in range(row_):
#     M.append(list(map(int,input().split())))

row_,col_ = [5,7]
M = [[0, 3, 15, 10, 15, 5, 0], [5, 8, 20, 12, 12, 17, 5], [7, 10, 15, 5, 12, 9, 11], [5, 7, 3, 2, 5, 5, 7], [0, 9, 11, 8, 9, 2, 3]]
x, y = [2,1]

def greedy(M,x,y,col_):
    current = M[x][y]
    sum_e = 0

    while y < col_-1 :
        y = y+1

        elevations = list(map(abs,[M[x-1][y]-current,M[x][y]-current,M[x+1][y]-current]))
        min_ = min(elevations)
        count = elevations.count(min_)
        # print(f'count: {count}')
        # print(elevations.index(min_))

        if count == 1:
            x1 = x + (elevations.index(min_) - 1)
        elif count == 3:
            x1 = x
        else:
            if elevations.index(min_) == 1:
                x1 = x
            elif elevations.index(min_) == elevations[0] == elevations[2]:
                x1 = x + 1

        current = M[x1][y]
        sum_e += min_

    print(x1 , y, sum_e)


greedy(M,x,y,col_)



