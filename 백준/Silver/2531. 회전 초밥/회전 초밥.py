import sys
from collections import deque
input = sys.stdin.readline

N, d, k, c = map(int, input().split())
arr = []
for _ in range(N):
    arr.append(int(input()))

arr.extend(arr)
max_count = 0

for i in range(N):
    dish = arr[i:i+k]
    dish.append(c)
    max_count = max(max_count, len(set(dish)))

print(max_count)
