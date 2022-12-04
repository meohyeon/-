n = int(input())

count = 0


while n>1:
    a = n -1

    if n % 5 == 0:
        a = min(a,n//5)
    if n % 3 == 0:
        a = min(a,n//3)
    if n % 2 == 0:
        a = min(a,n//2)

    n = a
    count += 1
    

print(count)