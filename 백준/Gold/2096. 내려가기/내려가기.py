import sys
input = sys.stdin.readline

n = int(input())

dp = [0, 0, 0]
min_dp = [0, 0 ,0]
for i in range(n):
    a, b, c = map(int, input().split())
    if i == 0:
        dp = [a, b, c]
        min_dp = [a, b, c]
    else:
        x = max(dp[0], dp[1]) + a
        y = max(dp[0], dp[1], dp[2]) + b
        z = max(dp[1], dp[2]) + c
        d = min(min_dp[0], min_dp[1]) + a
        e = min(min_dp[0], min_dp[1], min_dp[2]) + b
        f = min(min_dp[1], min_dp[2]) + c
        dp = [x, y, z]
        min_dp = [d, e, f]
print(max(dp), min(min_dp))