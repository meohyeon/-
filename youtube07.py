# 동빈나 이코테 나이트 문제

n = input()
index = int(n[1])
column = int(ord(n[0])) - int(ord('a')) +1  #아스키 코드 숫자로 변환 
total = 0

move = [ (-2,-1),(-2,1) , (2,-1),(2,1) , (-1,-2),(-1,2) , (1,-2),(1,2) ]


for i in move:
    a = index + i[0]
    b = column + i[1]
    if a > 8 or a < 1 or b > 8 or b < 1:
        continue
    total += 1

print(total)