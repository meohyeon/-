

graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

a = [0]*9
b = [0]*9

# DFS
def dfs(grh, i, visit):
    visit[i]=1
    print(i, end=" ")
    for j in grh[i]:
        if visit[j] != 1:
            dfs(grh,j,visit)


dfs(graph, 1, a)

print(" ",end='\n')
# BFS
from collections import deque

def bfs(grh, i, visit):
    que = deque([i])   
    visit[i]=1
    while que:
        j = que.popleft()
        print(j, end=" ")
        for i in grh[j]:
            if visit[i] !=  1:
                que.append(i)
                visit[i]=1
   

    
bfs(graph, 1, b)







