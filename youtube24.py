#2차원 리스트 만드는법 [[0 for j in range(k)] for i in range(n)]
n, k = map(int, input().split())

list = list(map(int, input().split()))
a = []
count = 0
total = 0

for i in range(n):
    b = []
    for j in range(k):
        b.append(list[count])
        count += 1
    a.append(b)

for i in range(1,k): #열
    for j in range(n): #행  
        left = a[j][i-1]
        if j-1 >= 0:
            leftup = a[j-1][i-1]
        else:
            leftup = 0
        if j < n-1:
            leftdown = a[j+1][i-1]
        else:
            leftdown=0
        a[j][i] = a[j][i] + max(left,leftup,leftdown)

for i in range(n):
    total = max(total, a[i][k-1])
print(total)
          
        
        
            




