import sys
# sys.stdin = open("input.txt", 'r')
input = sys.stdin.readline

N = int(input())
ans = float('inf')
arr = []
for _ in range(N):
    arr.append(list(map(int, input().split())))

for idx in range(3):
    dp = [[float('inf'), float('inf'), float('inf')] for _ in range(N)]
    dp[0][idx] = arr[0][idx]
    for i in range(1, N):
        dp[i][0] = arr[i][0] + min(dp[i-1][1], dp[i-1][2])
        dp[i][1] = arr[i][1] + min(dp[i-1][0], dp[i-1][2])
        dp[i][2] = arr[i][2] + min(dp[i-1][0], dp[i-1][1])
    for j in range(3):
        if idx != j:
            ans = min(ans, dp[-1][j])

print(ans)