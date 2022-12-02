# 동빈나 이코테 모험가 길드 
n = int(input())
data = list(map(int, input().split()))
data.sort()

total = 0 
count = 0 

for i in range(len(data)):
    scary = data[i]
    count +=1
    if count >= scary:
        total += 1
        count =0
    
print("총 그룹 수"+str(total))
