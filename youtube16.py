# 동빈나 이코테 두 배열의 원소 교체
n, k = map(int, input().split())
a = sorted(list(map(int,input().split())))
b = sorted(list(map(int,input().split())))

for i in range(k):

    if min(a) < max(b):
        mina = 0
        maxb = 0
        for j in range(n):
            if min(a) == a[j]:
                mina = j
            if max(b) == b[j]:
                maxb = j
        a[mina], b[maxb] = b[maxb], a[mina]
    else:
        break         

print(sum(a))