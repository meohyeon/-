n, k = map(int, input().split())
a = list(map(int,input().split()))
b = [x for x in a if x == k]
print(len(b))