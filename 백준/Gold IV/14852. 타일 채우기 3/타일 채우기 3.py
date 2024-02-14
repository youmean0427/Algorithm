import sys
input = sys.stdin.readline

N = int(input())
dp = [0] * (N+4)
dp[0], dp[1], dp[2], dp[3] = 1, 2, 7, 22

if N > 3:
    x = sum(dp[:2])

    for i in range(4, N+1):
        dp[i] = (dp[i-1] * 2 + dp[i-2] * 3 + x * 2) % 1000000007
        x += dp[i-2]

print(dp[N])