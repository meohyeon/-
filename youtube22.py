n, k = map(int, input().split())
list = []
count = [10001]*(k+1)
for i in range(n):
    list.append(int(input()))

for i in range(n):
    for j in range(list[i],k+1):
        if j % list[i] == 0:
            count[j] = min((j//list[i]), count[j])
        if count[j-list[i]] != 10001:
            count[j] = min(count[j-list[i]]+1 , count[j])

if count[k] == 10001:
    print(-1)
else:
    print("연산횟수"+str(count[k]))
