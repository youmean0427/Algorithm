import sys
# sys.stdin = open("input.txt", 'r')
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [[] for _ in range(N+1)]

dp = [[float('inf') for _ in range(N+1)] for _ in range(N+1)]
stopover = [[[] for _ in range(N+1)] for _ in range(N+1)]

for _ in range(M):
    a, b, c = map(int, input().split())
    dp[a][a] = 0
    dp[a][b] = c
    dp[b][a] = c

for i in range(1, N+1):
    for j in range(1, N+1):
        for k in range(1, N+1):
            if dp[j][k] > dp[j][i] + dp[i][k]:
                dp[j][k] = dp[j][i] + dp[i][k]
                if stopover[j][i]:
                    stopover[j][k] = [*stopover[j][i]]
                else:
                    stopover[j][k] = [i]

ans = []
for n in range(0, N+1):
    line = []
    for m in range(0, N+1):
        if n == m:
            line.append('-')
            continue

        if stopover[n][m]:
            line.append(*stopover[n][m])
        else:
            line.append(m)
    ans.append(line[1:])

for i in ans[1:]:
    print(*i)