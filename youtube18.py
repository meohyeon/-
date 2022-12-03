#4 6 
#19 15 10 17
a,b = map(int, input().split())
c = list(map(int, input().split()))

start=0
end = max(c)
answer = 0
while start <= end:
    cm = 0
    pivot = (start+end) // 2
    for i in c:
        d = i - pivot
        if d >= 1:
            cm += d
    if cm < b:
        end = pivot -1
    else:
        answer = pivot
        start = pivot +1 

print(answer)