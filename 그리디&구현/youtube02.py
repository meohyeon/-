# 동빈나 이코테 n이 1이 될떄까지 
# n%k==0 k로 나누고 아니면 1을 뺀다 
print("정수 2개 입력")
n, k = map(int, input().split())
if n < k:
    n, k = k, n
countA=0

while True :
    if n > k:
        a = (n//k)*k 
        countA += (n-a)
        n = a // k
        countA+=1
    else:
        n-=1
        countA+=1   
    if n <= 1:
        break
    
print("연산횟수 :"+str(countA))
