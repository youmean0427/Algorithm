import sys
input = sys.stdin.readline

T = int(input())
step = [0]
for _ in range(T):
    step.append(int(input()))

dp = [[0, 0, 0] for _ in range(T+1)]
dp[1][1] = step[1]

for i in range(2, T+1):
    dp[i][0] = max(dp[i-1][1], dp[i-1][2])
    dp[i][1] = dp[i-1][0] + step[i]
    dp[i][2] = dp[i-1][1] + step[i]

print(max(dp[-1][2], dp[-1][1]))
