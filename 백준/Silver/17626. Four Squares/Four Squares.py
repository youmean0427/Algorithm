import sys
input = sys.stdin.readline

n = int(input())
dp = [0, 1]

for i in range(2, n+1):
    min_value = 1e9

    for j in range(int(i ** (1/2)), 0, -1):
        min_value = min(min_value, dp[i - j **2])

    dp.append(int(min_value)+1)
print(dp[n])