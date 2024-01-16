import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
dp = [[float('inf')] * (N+1) for _ in range(N+1)]

for _ in range(M):
    a, b, c = map(int, input().split())
    dp[a][a] = 0
    dp[a][b] = min(c, dp[a][b])

for i in range(1, N+1):  # stopover
    for j in range(1, N+1):
        for k in range(1, N+1):
            dp[j][k] = min(dp[j][k], dp[j][i] + dp[i][k])

for d in range(1, len(dp)):
    for p in range(1, len(dp)):
        if (dp[d][p] == float('inf')):
            print(0, end=" ")
        else:
            print(dp[d][p], end=" ")
    print()