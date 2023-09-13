import sys
import math
input = sys.stdin.readline


flag = 1
while flag:

    N = int(input())

    if N == 0:
        flag = 0
        break
    dp = [1, 1, 2, 5, 14]

    for i in range(5, N+1):
        total = 0
        start = 0
        end = i - 1
        while end >= 0:

            total += dp[start] * dp[end]
            start += 1
            end -= 1

        dp.append(total)

    print(dp[N])
