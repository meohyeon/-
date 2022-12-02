# 동빈나 이코테 상하좌우 이동 문제

n = int(input())
data = input().split()

dindex = 1
dcolumn = 1

move = {'L': (0,-1), 'R': (0, 1), 'U': (-1,0), 'D': (1,0)}


for i in range(len(data)):
    b, c = move[data[i]]
    bindex = dindex + b
    bcolumn = dcolumn + c
    if bindex < 1 or bcolumn < 1 or bindex > n or bcolumn > n:
        continue    
    dindex = bindex
    dcolumn = bcolumn

print(dindex, dcolumn)


