# 동빈나 이코테 구간합 
list = [1, 2, 3, 2, 5]
a = 0
sumlist = [0]
for i in list:
    a += i
    sumlist.append(a)

n = 3
k = 4

print(sumlist[k]-sumlist[n-1])