import sys
input = sys.stdin.readline

N = int(input())
arr = [[int(x) for x in input().split()] for _ in range(N)]
dp = [[0] * N for _ in range(N)]
dp[0][0] = 1
for i in range(N):
    for j in range(N):

        if j == N-1 and i == N-1:
            break

        if 0 <= j + arr[i][j] < N:
            dp[i][arr[i][j]+j] += dp[i][j]

        if 0 <= i + arr[i][j] < N:
            dp[i+arr[i][j]][j] += dp[i][j]
            
print(dp[-1][-1])