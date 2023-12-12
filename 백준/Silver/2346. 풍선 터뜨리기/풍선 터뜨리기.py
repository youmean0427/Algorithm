import sys, math
input = sys.stdin.readline
from collections import deque

N = int(input())
arr = [int(x) for x in input().split()]
q = deque([])

for i in range(len(arr)):
    q.append((arr[i], i+1))

result = []

while q:
    a, b = q.popleft()
    result.append(b)
    if a > 0:
        q.rotate(1-a)
    else:
        q.rotate(-a)

print(*result)