import sys
# sys.stdin = open("input.txt", 'r')
input = sys.stdin.readline

N, K = map(int, input().split())
W, V = [], []
for _ in range(N):
    a, b = map(int, input().split())
    W.append(a)
    V.append(b)

dp = [[0 for _ in range(K+1)] for _ in range(N+1)]

for n in range(1, N+1):   # 물건 idx
    for m in range(1, K+1):   # 무게
        if m < W[n-1]:
            dp[n][m] = dp[n-1][m]
        else:
            dp[n][m] = max(dp[n-1][m], dp[n-1][m-W[n-1]] + V[n-1])

ans = 0
for i in range(len(dp)):
    ans = max(ans, dp[i][-1])
print(ans)
