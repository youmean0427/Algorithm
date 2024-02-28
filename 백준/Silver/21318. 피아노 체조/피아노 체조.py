import sys
# sys.stdin = open("input.txt", 'r')
input = sys.stdin.readline

N = int(input())
arr = [int(i) for i in input().split()]
dp = [0] * (N+1)
for i in range(N-1):
    dp[i+2] = dp[i+1]
    if arr[i] > arr[i+1]:
        dp[i+2] += 1

Q = int(input())
for _ in range(Q):
    x, y = map(int, input().split())
    x, y = x-1, y-1
    if x == y:
        ans = 0
    else:
        ans = dp[y+1]-dp[x+1]
    print(ans)