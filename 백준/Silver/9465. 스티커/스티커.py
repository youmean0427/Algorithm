import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    dp = [[0] * N for _ in range(2)]
    arr = []
    for _ in range(2):
        arr.append([int(i) for i in input().split()])

    if N >= 1:
        dp[0][0] = arr[0][0]
        dp[1][0] = arr[1][0]
    if N >= 2:
        dp[0][1] = dp[1][0] + arr[0][1]
        dp[1][1] = dp[0][0] + arr[1][1]

    for j in range(2, N):
        for i in range(2):
            if i == 1:
                dp[i][j] = max( dp[i-1][j-1], dp[i-1][j-2])+arr[i][j]
            else:
                dp[i][j] = max( dp[i+1][j-1], dp[i+1][j-2]) + arr[i][j]

    print(max(dp[0][-1], dp[1][-1]))