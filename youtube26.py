# 동빈나 이코테 그 외 들
# 에라토스테네스의 체 알고리즘
n = int(input())
list = [0]*(n+1)
for i in range(2,n+1):
    if list[i] == 0:
        j = 2
        while i * j <=n:
            list[i*j] = 1
            j += 1

for i in range(2,n+1):
    if list[i] == 0:
        print(i,end=" ")