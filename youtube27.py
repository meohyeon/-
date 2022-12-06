# 동빈나 이코테 투포인터 
n = int(input())

list = list(map(int,input().split()))

end = 0
count = 0
total = 0

for start in range(len(list)):
    while total < n or end < n:
        total += list[end]
        end += 1
    if total == n:
        count += 1
    total -= list[start]

print(count)