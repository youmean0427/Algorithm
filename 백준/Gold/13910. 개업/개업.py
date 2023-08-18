import sys
input = sys.stdin.readline

N, M = map(int, input().split())
size = [int(x) for x in input().split()]
size.append(0)

cnt = []
for i in range(M):
    for j in range(i+1, M+1):
        cnt.append(size[i] + size[j])

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