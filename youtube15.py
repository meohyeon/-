# 동빈나 이코테 계수정렬 
# ex 7 5 9 0 3 1 6 2 9 1 4 8 0 5 2
n = list(map(int, input().split()))

a = [0]*(max(n)+1)
for i in n:
    a[i] += 1
for i in range(len(a)):
    for j in range(a[i]):
        print(i,end=" ")
