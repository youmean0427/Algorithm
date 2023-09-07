import sys
input = sys.stdin.readline

N = int(input())
arr = [int(x) for x in input().split()]

dp = [[0] * 21 for _ in range(N)]
dp[0][arr[0]] += 1

for i in range(N-1):
    for j in range(21):
        if dp[i][j]:
            if j + arr[i+1] <= 20:
                dp[i+1][j+arr[i+1]] += dp[i][j]
            if 0 <= j - arr[i+1]:
                dp[i+1][j-arr[i+1]] += dp[i][j]

print(dp[-2][arr[N-1]])