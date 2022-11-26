# 동빈나 이코테 곱하기 혹은 더하기
print("수 입력")
n = list(input())
total = int(n[0])
for i in range(1,len(n)):
    if int(n[i]) <=1 or total <=1:
        total += int(n[i])
    else:
        total *= int(n[i])

print(total)
    

