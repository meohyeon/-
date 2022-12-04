n = int(input())

list = list(map(int,input().split()))
list.reverse()
count = 0
dp = [1] * n
for i in range(1,n):
    for j in range(0,i):
        if list[j] < list [i]:
            dp[i] = max (dp[i], dp[j]+1)
    
print(n-max(dp))