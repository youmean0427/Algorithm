import sys
input = sys.stdin.readline
from itertools import combinations

N = int(input())
arr = [int(i) for i in input().split()]
dp = [0] * N

for i in range(N):
    for j in range(i):
        if arr[i] > arr[j]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp)+1)

