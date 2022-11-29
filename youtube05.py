# 동빈나 이코테 상하좌우
n = int(input())
data = input().split()

dx = 1
dy = 1

move = {'L': (0,-1), 'R': (0, 1), 'U': (-1,0), 'D': (1,0)}


for i in range(len(data)):
    b, c = move[data[i]]
    bx = dx + b
    by = dy + c
    print(by)
    if bx < 1 or by < 1 or bx > n or by > n:
        continue    
    dx = bx
    dy = by


print(dx, dy)


