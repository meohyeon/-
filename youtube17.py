#동빈나 이코테 5 이진탐색
from bisect import bisect_left, bisect_right
a = [1, 2, 4, 4, 8]
x = 4

print(bisect_right(a,x))
print(bisect_left(a,x))