import sys
input = sys.stdin.readline

N = int(input())
dp = [[0] * (12) for _ in range(N)]
dp[0][1:11] = [1] * 10

for i in range(1,N):
    for j in range(1, 11):
        dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]

print(sum(dp[N-1][2:]) % 1000000000)