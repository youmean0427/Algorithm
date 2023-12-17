import sys
input = sys.stdin.readline

N = int(input())
arr = [int(x) for x in input().split()]
dp = [0] * N
dp[0] = arr[0]
for i in range(1, N):
    dp[i] = max(arr[i] + dp[i-1], arr[i-1] + arr[i], arr[i])
print(max(dp))