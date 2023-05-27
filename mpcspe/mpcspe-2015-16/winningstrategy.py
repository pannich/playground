m = int(input()) #current money
b = int(input()) #current bet
n = int(input())
results = [int(e) for e in input().split()]

# #test case
# m = 100
# b = 5
# n = 4
# results = [0,1,0,0]

def winning(n,m,b):
    b1 = b
    for i,r in enumerate(results):
        if m <= 0:
            print('BROKE')
            break
        else:
            if r == 0 : #lose
                m_next = m - b
                b_next = min(b*2,m_next)
            else: #win
                m_next = m + b
                b_next = min(b1,m_next)
            m = m_next
            b = b_next
            # print("round:",i,"m left:",m, "b next:",b)
    print("last round m:", m)
    return


winning(n,m,b)






# end when n == 0 finish all rounds
