import sys
# sys.stdin = open("input.txt", 'r')
input = sys.stdin.readline

N = int(input())
dp = [float('inf') for _ in range(N+6)]

dp[0] = 1
dp[1], dp[3] = 0, 0
dp[2], dp[4] = 1, 2
dp[5] = 1

for i in range(6, N+1):

    if dp[i-2] == 0 or dp[i-(i-2)] == 0:
        two = float('inf')
    else:
        two = dp[i-2] + dp[i-(i-2)]

    if dp[i-5] == 0 or dp[i-(i-5)] == 0:
        five = float('inf')
    else:
        five = dp[i-5] + dp[i-(i-5)]

    dp[i] = min(dp[i], two, five)

if dp[N]:
    print(dp[N])
else:
    print(-1)
