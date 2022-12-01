# 동빈나 이코테 3. DFS & BFS

# 재귀함수 
def function(i):
    if i == 100:
        return
    print(i)
    function(i+1)

function(1)

# 팩토리얼
def factorial(n): 
    if n <=1:
        return 1
    return n * factorial(n-1)

print(factorial(5))

# 최대공약수 계산 (유클리드 호제법)
def gcd(a, b):
    if a % b ==0:
        return b
    else:
        return gcd(b,a % b)

print(gcd(12,5))