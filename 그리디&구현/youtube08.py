# 동빈나 이코테 문자열 재정렬

n = input()

answer = []
total = 0

for i in n:
    if i.isalpha():   #isalpha 문자/숫자 체크 하는 함수
        answer.append(i)
    else:
        total += int(i)
answer.sort()

if total != 0:
    answer.append(str(total))

print(''.join(answer))
