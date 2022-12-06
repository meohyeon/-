n = int(input())
list = list(map(int, input().split()))
start = 0
end = 0
count = 0 
for i in range(n*n):
    print(list[start:end+1])
    if sum(list[start:end+1]) == n:
        count += 1

    if sum(list[start:end+1]) < n:
        if end < n:
            end += 1
    else:
        if start < n:
            start += 1
    
    if start == 5 and end == 5:
        break

print(count)