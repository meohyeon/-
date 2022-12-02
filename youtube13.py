# 동빈나 이코테 미로탈출
from collections import deque
n, m = map(int,input().split())

dx = [-1, 1, 0 ,0]
dy = [0, 0, 1, -1]
graph = []
for i in range(n):
    graph.append(list(map(int,input())))



def bfs(x,y):
    que = deque()
    que.append((x,y))
    while que:
        a,b = que.popleft()
        for i in range(4):
            bx = a + dx[i]
            by = b + dy[i]
            if bx <= -1 or bx >= n or by <= -1 or by >= m:
                continue
            if graph[bx][by] == 0:
                continue
            if graph[bx][by] == 1:
               
                graph[bx][by] = graph[a][b]+1
                que.append((bx,by))
    print(graph[n-1][m-1])
    
    



bfs(0,0)