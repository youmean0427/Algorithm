import sys
input = sys.stdin.readline
from collections import deque

N, K = map(int, input().split())

arr = deque([int(x) for x in range(1, N+1)])
result = []

while arr:

    for i in range(K-1):
        arr.append(arr.popleft())
    result.append((arr.popleft()))

# print("<", ", ".join(result), ">", sep= "")
print(str(result).replace('[', '<').replace(']', '>'))