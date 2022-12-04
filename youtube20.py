#동빈나 이코테 6다이나믹 프로그래밍
#피보나치 수열
print("정수 n입력")
n = int(input())
answer = [1,1]
for i in range(2,n):
    answer.append(answer[i-2] + answer[i-1])

print(answer)