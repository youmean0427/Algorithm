import sys, math
input = sys.stdin.readline
from collections import deque

N = int(input())
check = [int(x) for x in input().split()]
arr = [int(x) for x in input().split()]
queue = []

M = int(input())
C = [int(x) for x in input().split()]

for i in range(N-1, -1, -1):
    if check[i] == 0:
        queue.append(arr[i])

for i in C:
    queue.append(i)

print(*queue[:M])