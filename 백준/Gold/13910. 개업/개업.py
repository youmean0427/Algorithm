import sys
from itertools import combinations

input = sys.stdin.readline

N, M = map(int, input().split())
size = [int(x) for x in input().split()]

cnt = size
combi = combinations(size, 2)
for j in combi:
    cnt.append(sum(j))

dp = [0] * (N+1)

for k in range(1, N+1):
    min_value = 10001

    for j in cnt:
        if k > j:
            min_value = min(min_value, dp[k-j]+1)
        elif k == j:
            min_value = 1
    dp[k] = min_value

if dp[N] == 10001:
    print(-1)
else:
    print(dp[N])